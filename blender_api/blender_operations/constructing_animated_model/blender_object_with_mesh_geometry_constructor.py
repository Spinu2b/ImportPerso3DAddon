from blender_api.blender_operations.general_api_operations.blender_objects_manipulation import BlenderObjectsManipulation
import bpy
from bpy.types import Object, MeshUVLoopLayer, Image, Node

from model.perso.subobject_geometry_data import SubobjectGeometryData
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


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
        return mesh_obj
