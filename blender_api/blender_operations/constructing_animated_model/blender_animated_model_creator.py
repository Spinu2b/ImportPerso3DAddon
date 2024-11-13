from typing import Dict
from blender_api.blender_operations.constructing_animated_model.blender_object_with_mesh_geometry_constructor import BlenderObjectWithMeshGeometryConstructor
import bpy
from bpy.types import Object

from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class BlenderAnimatedModelCreator:
    def construct_using(self, perso3d_model: SubobjectsCompressedPerso3DAnimatedData):
        blender_mesh_objects = dict()  # type: Dict[str, Object]

        for subobject_geometry_data_hash in perso3d_model.subobjects:
            blender_mesh_obj = BlenderObjectWithMeshGeometryConstructor().construct(
                perso3d_model.subobjects[subobject_geometry_data_hash]
            )
