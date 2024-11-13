from typing import Dict
from blender_api.blender_operations.constructing_animated_model.blender_animation_manipulator import BlenderAnimationManipulator
from blender_api.blender_operations.constructing_animated_model.blender_object_with_mesh_geometry_constructor import BlenderObjectWithMeshGeometryConstructor
from blender_api.blender_operations.general_api_operations.blender_editor_manipulation import BlenderEditorManipulation
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
            blender_mesh_objects[subobject_geometry_data_hash] = blender_mesh_obj

        self._animate_model_with_subobjects_existence_in_animations(
            perso3d_model=perso3d_model,
            blender_mesh_objects=blender_mesh_objects
        )

    def _animate_model_with_subobjects_existence_in_animations(
        self,
        perso3d_model: SubobjectsCompressedPerso3DAnimatedData,
        blender_mesh_objects: Dict[str, Object]    
    ):
        blender_animation_manipulator = BlenderAnimationManipulator()


        blender_editor_manipulation = BlenderEditorManipulation()
        # blender_editor_manipulation.enter_pose_mode()

        blender_editor_manipulation.set_context_area_ui_type_to_dopesheet()
        blender_editor_manipulation.set_context_space_data_ui_mode_to_action()



        for state_index in perso3d_model.states:

            action = blender_editor_manipulation.enter_animation_clip(name="Animation_" + state_index)
            for frame_number in perso3d_model.states[state_index]:
                blender_editor_manipulation.enter_frame_number(frame_number=int(frame_number))
                for subobject_key in perso3d_model.states[state_index][frame_number].data_blocks:
                    blender_animation_manipulator.animate_subobject(
                        state_index=state_index,
                        frame_number=frame_number,
                        subobject=perso3d_model.states[state_index][frame_number].data_blocks[subobject_key],
                        blender_mesh_objects=blender_mesh_objects
                    )