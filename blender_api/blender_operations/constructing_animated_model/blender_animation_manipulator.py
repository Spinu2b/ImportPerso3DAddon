
from blender_api.blender_operations.constructing_animated_model.blender_animation_transform_manipulation import BlenderAnimationTransformManipulation
from blender_api.blender_operations.general_api_operations.blender_editor_manipulation import BlenderEditorManipulation
from blender_api.blender_operations.general_api_operations.blender_objects_manipulation import BlenderObjectsManipulation
import bpy
from bpy.types import Object
from typing import Dict
from model.perso.subobject_compressed_frame_data_block import SubobjectCompressedFrameDataBlock


class BlenderAnimationManipulator:
    def __init__(self):
        self.blender_editor_manipulation = BlenderEditorManipulation()

    def animate_subobject(
        self, state_index: int, frame_number: int,
        subobject: SubobjectCompressedFrameDataBlock,
        blender_mesh_objects: Dict[str, Object]
    ):
        blender_animation_transform_manipulation = \
            BlenderAnimationTransformManipulation()

        blender_objects_manipulation = BlenderObjectsManipulation()
        blender_objects_manipulation.deselect_all_objects()
        blender_objects_manipulation.select_object(
            blender_mesh_objects[subobject.geometry_data_reference])
        
        blender_animation_transform_manipulation.transform_object(
            blender_mesh_objects[subobject.geometry_data_reference],
            subobject.transform,
        )

        # blender_mesh_objects[subobject.geometry_data_reference].keyframe_insert(data_path="location", frame=int(frame_number))
        # blender_mesh_objects[subobject.geometry_data_reference].keyframe_insert(data_path="rotation_quaternion", frame=int(frame_number))
        # blender_mesh_objects[subobject.geometry_data_reference].keyframe_insert(data_path="scale", frame=int(frame_number))

        blender_animation_transform_manipulation.lock_rotation_scale_position()
        
