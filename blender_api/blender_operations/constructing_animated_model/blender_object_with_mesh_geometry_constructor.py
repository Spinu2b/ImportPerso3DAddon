import array
from typing import List
from blender_api.blender_operations.general_api_operations.blender_objects_manipulation import BlenderObjectsManipulation
import bpy
from bpy.types import Object, MeshUVLoopLayer, Image, Node

from model.constructing.subobject_geometry_data_dict.subobject_geometry_data_texture_constructor import Color
from model.perso.object_transform import Vector2
from model.perso.subobject_geometry_data import SubobjectGeometryData
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class BlenderImageHelper:
    def get_blender_image(self, width: int, height: int,
                          image_name: str,
                          texture_image_definition: List[Color]) -> Image:
        blender_image = bpy.data.images.new(name=image_name, width=width, height=height, alpha=True)  # type: Image
        pixel_index = 0
        pixels_array = array.array('f',(0,)*len(texture_image_definition) * 4)
        for pixel_color in texture_image_definition:
            pixels_array[pixel_index] = pixel_color.r
            pixels_array[pixel_index + 1] = pixel_color.g
            pixels_array[pixel_index + 2] = pixel_color.b
            pixels_array[pixel_index + 3] = pixel_color.a
            pixel_index += 4

        blender_image.pixels = pixels_array.tolist()
        blender_image.pack()
        return blender_image


class BlenderMeshMaterialApplier:
    def _apply_uv_map(self, uv_map: List[Vector2], mesh_obj: Object,
                      subobject_geometry_data: SubobjectGeometryData) -> MeshUVLoopLayer:
        uv_loops_layer = mesh_obj.data.uv_layers.new(name=subobject_geometry_data.key + "_UV")  # type: MeshUVLoopLayer

        uv_loop_index = 0

        if (len(uv_map) % 3 == 0):
            while uv_loop_index < len(uv_map):
                first_vertex_uv = uv_map[uv_loop_index]
                second_vertex_uv = uv_map[uv_loop_index + 2]
                third_vertex_uv = uv_map[uv_loop_index + 1]

                uv_loops_layer.data[uv_loop_index].uv[0] = first_vertex_uv.x
                uv_loops_layer.data[uv_loop_index].uv[1] = first_vertex_uv.y

                uv_loops_layer.data[uv_loop_index + 1].uv[0] = second_vertex_uv.x
                uv_loops_layer.data[uv_loop_index + 1].uv[1] = second_vertex_uv.y

                uv_loops_layer.data[uv_loop_index + 2].uv[0] = third_vertex_uv.x
                uv_loops_layer.data[uv_loop_index + 2].uv[1] = third_vertex_uv.y

                uv_loop_index += 3

        return uv_loops_layer

    def apply(self, uv: List[Vector2], mesh_obj: Object,
        subobject_geometry_data: SubobjectGeometryData):
        blender_material_data_block = bpy.data.materials.new(
            name=subobject_geometry_data.key + "_MAT")  # type: bpy.types.Material
        blender_material_data_block.use_nodes = True

        blender_material_data_block.node_tree.nodes.clear()

        material_output_node = blender_material_data_block.\
            node_tree.nodes.new(type="ShaderNodeOutputMaterial")  # type: Node
        material_principled_bsdf_node = blender_material_data_block.\
            node_tree.nodes.new(type="ShaderNodeBsdfPrincipled")  # type: Node
        texture_image_node = blender_material_data_block.\
            node_tree.nodes.new(type='ShaderNodeTexImage')  # type: Node
        texture_image_node.image = BlenderImageHelper().get_blender_image(
            width=subobject_geometry_data.texture.width,
            height=subobject_geometry_data.texture.height,
            texture_image_definition=subobject_geometry_data.texture.pixels,
            image_name=subobject_geometry_data.key + "_IMAGE"
        )

        uv_loops_layer = \
            self._apply_uv_map(
                uv_map=uv, mesh_obj=mesh_obj,
                subobject_geometry_data=subobject_geometry_data)  # type: MeshUVLoopLayer

        uv_map_node = blender_material_data_block.node_tree.nodes.new(type="ShaderNodeUVMap")
        uv_map_node.uv_map = uv_loops_layer.name

        blender_material_data_block.node_tree.links.new(material_output_node.inputs['Surface'],
                                                        material_principled_bsdf_node.outputs['BSDF'])
        blender_material_data_block.node_tree.links.new(material_principled_bsdf_node.inputs['Base Color'],
                                                        texture_image_node.outputs['Color'])
        blender_material_data_block.node_tree.links.new(texture_image_node.inputs['Vector'],
                                                        uv_map_node.outputs['UV'])

        mesh_obj.data.materials.append(blender_material_data_block)


class BlenderObjectWithMeshGeometryConstructor:
    def construct(self, subobject_geometry_data: SubobjectGeometryData):
        blender_objects_manipulation = BlenderObjectsManipulation()
        object_name = "OBJECT_" + subobject_geometry_data.key
        mesh_data_block = bpy.data.meshes.new(name=object_name)

        mesh_obj = blender_objects_manipulation.create_new_object_with_linked_datablock(
            object_name=object_name, data_block=mesh_data_block)
        blender_objects_manipulation.link_object_to_the_scene(mesh_obj)

        blender_objects_manipulation.deselect_all_objects()
        blender_objects_manipulation.set_active_object_to(mesh_obj)
        blender_objects_manipulation.select_active_object()

        vertices, edges, faces = subobject_geometry_data.get_blender_pydata_form()

        mesh_obj.data.from_pydata(vertices, edges, faces)
        mesh_obj.animation_data_create()

        # self._apply_normals(subobject_geometry_data, mesh_obj)
        self._apply_mesh_materials(subobject_geometry_data, mesh_obj)
        return mesh_obj
    
    def _apply_mesh_materials(self, subobject_geometry_data: SubobjectGeometryData, mesh_obj: Object):
        blender_mesh_material_applier = BlenderMeshMaterialApplier()
        blender_mesh_material_applier.apply(
            uv=subobject_geometry_data.uv_map.uv,
            mesh_obj = mesh_obj,
            subobject_geometry_data=subobject_geometry_data
        )

    def _apply_normals(self, subobject_geometry_data: SubobjectGeometryData, mesh_obj: Object):
        normals_definitions = subobject_geometry_data.normals  # type: List[Vector3d]
        for mesh_vertex_index, mesh_vertex in enumerate(mesh_obj.data.vertices):
            mesh_vertex.normal[0] = normals_definitions[mesh_vertex_index].x
            mesh_vertex.normal[1] = normals_definitions[mesh_vertex_index].y
            mesh_vertex.normal[2] = normals_definitions[mesh_vertex_index].z