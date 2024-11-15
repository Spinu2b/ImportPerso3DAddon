import bpy
from bpy.types import Object
from mathutils import Matrix, Vector, Quaternion
from model.perso.object_transform import ObjectTransform

class BlenderAnimationTransformManipulation:
    def transform_object(
            self, pose_bone: Object,
            transform: ObjectTransform,
            armature_obj: Object):
        

        loc = Matrix.Translation(Vector((
                transform.position.x,
                transform.position.y,
                transform.position.z)))
        rot = Quaternion(Vector((
                transform.rotation.w,
                transform.rotation.x,
                transform.rotation.y,
                transform.rotation.z)),
                ).to_matrix().to_4x4()
        scale = Matrix()
        scale[0][0] = transform.scale.x
        scale[1][1] = transform.scale.y
        scale[2][2] = transform.scale.z
        world_mat = loc @ rot @ scale

        pose_bone.matrix = armature_obj.convert_space(
                pose_bone=pose_bone,
                matrix=world_mat,
                from_space='WORLD',
                to_space='POSE')

    def lock_rotation_scale_position(self):
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
        # bpy.ops.action.keyframe_insert(type='ALL')
        # bpy.ops.action.keyframe_insert(type='ALL')
