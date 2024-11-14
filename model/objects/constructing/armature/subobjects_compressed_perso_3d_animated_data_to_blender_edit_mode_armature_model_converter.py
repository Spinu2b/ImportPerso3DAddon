

from model.animations.model.blender_edit_mode_armature_model import BlenderEditModeArmatureModel, BlenderEditModeArmatureNodeModel
from model.perso.object_transform import Quaternion, Vector3
from utils.blender.edit_mode_bones.blender_edit_mode_bones_construction_helper import BlenderEditModeBonesConstructionHelper


class SubobjectsCompressedPerso3DAnimatedDataToBlenderEditModeArmatureModelConverter:
    def convert(self, perso3d_model) -> BlenderEditModeArmatureModel:
        result = BlenderEditModeArmatureModel()
        for subobject_hash in perso3d_model.subobjects:
            result.add_bone(self._get_blender_edit_mode_armature_node(name=subobject_hash))
        return result
    
    def _get_blender_edit_mode_armature_node(self, name: str) -> BlenderEditModeArmatureNodeModel:

        head_position, tail_position = BlenderEditModeBonesConstructionHelper().calculate_head_and_tail_position()

        return BlenderEditModeArmatureNodeModel(
            name=name,
            head_position_x=head_position[0],
            head_position_y=head_position[1],
            head_position_z=head_position[2],
            tail_position_x=tail_position[0],
            tail_position_y=tail_position[1],
            tail_position_z=tail_position[2],
            position=Vector3(0,0,0),
            rotation=Quaternion(0,0,0,1),
            scale=Vector3(1,1,1)
        )