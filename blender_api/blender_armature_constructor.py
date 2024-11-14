from blender_api.blender_operations.constructing_armature.blender_armature_generator import BlenderArmatureGenerator
from bpy.types import Armature, Object
from typing import Tuple

from model.animations.model.blender_edit_mode_armature_model import BlenderEditModeArmatureModel


class BlenderArmatureConstructor:
    def build_armature(self, name: str,
        blender_edit_mode_armature_model: BlenderEditModeArmatureModel
    ) -> Tuple[Armature, Object]:
        blender_armature_generator = BlenderArmatureGenerator()
        armature, armature_obj = blender_armature_generator.create_armature(name=name)
        for armature_bone_model in blender_edit_mode_armature_model.bones:
            blender_armature_generator.place_bone(
                armature_bone_model=armature_bone_model,
                armature=armature,
                armature_obj=armature_obj
            )

        return armature, armature_obj
        
