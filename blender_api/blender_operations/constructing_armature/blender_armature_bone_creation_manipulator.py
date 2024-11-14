

from typing import Tuple

import mathutils
from bpy.types import Armature, EditBone, Object
from model.perso.object_transform import Quaternion, Vector3


class BlenderArmatureBoneCreationManipulator:
    def add_bone(self,
                 head_position: Tuple[float, float, float],
                 tail_position: Tuple[float, float, float],
                 position: Vector3,
                 rotation: Quaternion,
                 scale: Vector3,
                 armature_obj: Object,
                 armature: Armature,
                 name: str):
        edit_bone = armature.edit_bones.new(name=name)  # type: EditBone
        edit_bone.head[0] = head_position[0]
        edit_bone.head[1] = head_position[1]
        edit_bone.head[2] = head_position[2]

        edit_bone.tail[0] = tail_position[0]
        edit_bone.tail[1] = tail_position[1]
        edit_bone.tail[2] = tail_position[2]

        if name != "ROOT_CHANNEL":
            loc = mathutils.Matrix.Translation(mathutils.Vector((
                position.x,
                position.y,
                position.z)))
            rot = mathutils.Quaternion(mathutils.Vector((
                rotation.w,
                rotation.x,
                rotation.y,
                rotation.z)),
            ).to_matrix().to_4x4()
            scale_mat = mathutils.Matrix()
            scale_mat[0][0] = scale.x
            scale_mat[1][1] = scale.y
            scale_mat[2][2] = scale.z
            world_mat = loc @ rot @ scale_mat
            edit_bone.matrix = armature_obj.convert_space(
                #pose_bone=complementary_pose_bone,
                matrix=world_mat,
                from_space='WORLD',
                to_space='LOCAL')

