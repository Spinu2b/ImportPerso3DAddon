import bpy
from bpy.types import Object
from mathutils import Matrix, Vector, Quaternion
from model.perso.object_transform import ObjectTransform

class BlenderAnimationTransformManipulation:
    def transform_object(self, object: Object, transform: ObjectTransform):
        

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

        object.matrix_world = world_mat

    def lock_rotation_scale_position(self):
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
        # bpy.ops.action.keyframe_insert(type='ALL')
        # bpy.ops.action.keyframe_insert(type='ALL')
