from typing import List
from blender_api.blender_operations.general_api_operations.blender_objects_manipulation import BlenderObjectsManipulation
import bpy
from bpy.types import Object, MeshUVLoopLayer, Image, Node

from model.perso.subobject_geometry_data import SubobjectGeometryData
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class BlenderMeshMaterialApplier:
    


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

        self._apply_normals(subobject_geometry_data, mesh_obj)
        self._apply_mesh_materials(subobject_geometry_data, mesh_obj)
        return mesh_obj
    
    def _apply_mesh_materials(self, subobject_geometry_data: SubobjectGeometryData, mesh_obj: Object):
        blender_mesh_material_applier = BlenderMeshMaterialApplier()
        blender_mesh_material_applier.apply(
            uv_map=subobject_geometry_data.uv_map,
            mesh_obj = mesh_obj,
            subobject_geometry_data=subobject_geometry_data
        )

    def _apply_normals(self, subobject_geometry_data: SubobjectGeometryData, mesh_obj: Object):
        normals_definitions = subobject_geometry_data.normals  # type: List[Vector3d]
        for mesh_vertex_index, mesh_vertex in enumerate(mesh_obj.data.vertices):
            mesh_vertex.normal[0] = normals_definitions[mesh_vertex_index].x
            mesh_vertex.normal[1] = normals_definitions[mesh_vertex_index].y
            mesh_vertex.normal[2] = normals_definitions[mesh_vertex_index].z