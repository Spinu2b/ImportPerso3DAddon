from typing import Dict

from blender_api.blender_operations.general_api_operations.blender_objects_manipulation import BlenderObjectsManipulation
from bpy.types import Object, VertexGroup, Modifier
from model.perso.subobject_geometry_data import SubobjectGeometryData


class BlenderRiggingHelper:
    def parent_blender_object_to_armature_with_bone_vertex_group(
            self,
            armature_obj: Object,
            blender_mesh_obj: Object,
            subobject_hash: str,
            subobject_model: SubobjectGeometryData):
        blender_objects_manipulation = BlenderObjectsManipulation()
        blender_objects_manipulation.parent_object_to(child=blender_mesh_obj, parent=armature_obj)

        blender_vertex_group = blender_mesh_obj.vertex_groups.new(name=subobject_hash)  # type: VertexGroup
        for vertex_in_group_index in range(len(subobject_model.vertices)):
            vertex_in_group_weight = 1.0
            blender_vertex_group.add(index=[vertex_in_group_index], weight=vertex_in_group_weight,
                                         type='ADD')

        self._add_armature_modifier(armature_obj, blender_mesh_obj)

    def _add_armature_modifier(self, armature_obj: Object, blender_mesh_obj: Object):
        armature_modifier = blender_mesh_obj.modifiers.new(name="ARMATURE_MODIFIER", type="ARMATURE")  # type: Modifier
        armature_modifier.object = armature_obj
