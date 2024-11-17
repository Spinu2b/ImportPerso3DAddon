from typing import Dict, Set
from blender_api.blender_armature_constructor import BlenderArmatureConstructor
from blender_api.blender_operations.constructing_animated_model.blender_animation_manipulator import BlenderAnimationManipulator
from blender_api.blender_operations.constructing_animated_model.blender_object_with_mesh_geometry_constructor import BlenderObjectWithMeshGeometryConstructor
from blender_api.blender_operations.constructing_animated_model.blender_rigging_helper import BlenderRiggingHelper
from blender_api.blender_operations.general_api_operations.blender_editor_manipulation import BlenderEditorManipulation
from blender_api.blender_operations.general_api_operations.blender_objects_manipulation import BlenderObjectsManipulation
import bpy
from bpy.types import Object

from model.perso.object_transform import ObjectTransform, Quaternion, Vector3
from model.perso.subobject_compressed_frame_data_block import SubobjectCompressedFrameDataBlock
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class BlenderAnimatedModelCreator:
    def construct_using(self, perso3d_model: SubobjectsCompressedPerso3DAnimatedData):
        blender_mesh_objects = dict()  # type: Dict[str, Object]

        for subobject_geometry_data_hash in perso3d_model.subobjects:
            blender_mesh_obj = BlenderObjectWithMeshGeometryConstructor().construct(
                perso3d_model.subobjects[subobject_geometry_data_hash]
            )
            blender_mesh_objects[subobject_geometry_data_hash] = blender_mesh_obj

        blender_edit_mode_armature_model = perso3d_model.get_blender_edit_mode_armature_model()

        blender_armature_constructor = BlenderArmatureConstructor()
        blender_armature_data_block, blender_armature_obj = blender_armature_constructor.build_armature(
            blender_edit_mode_armature_model=blender_edit_mode_armature_model,
            name="ARMATURE")   
        
        blender_rigging_helper = BlenderRiggingHelper()
        for subobject_hash in blender_mesh_objects:
            subobject = blender_mesh_objects[subobject_hash]
            blender_rigging_helper.parent_blender_object_to_armature_with_bone_vertex_group(
                armature_obj=blender_armature_obj,
                blender_mesh_obj=subobject,
                subobject_hash=subobject_hash,
                subobject_model=perso3d_model.subobjects[subobject_hash]
            )

        self._animate_model_with_subobjects_existence_in_animations(
            perso3d_model=perso3d_model,
            blender_mesh_objects=blender_mesh_objects,
            blender_armature_obj=blender_armature_obj
        )

    def _animate_model_with_subobjects_existence_in_animations(
        self,
        perso3d_model: SubobjectsCompressedPerso3DAnimatedData,
        blender_mesh_objects: Dict[str, Object],
        blender_armature_obj: Object,    
    ):
        blender_animation_manipulator = BlenderAnimationManipulator()
        blender_objects_manipulation = BlenderObjectsManipulation()

        blender_editor_manipulation = BlenderEditorManipulation()
        blender_editor_manipulation.enter_pose_mode()

        blender_editor_manipulation.set_context_area_ui_type_to_dopesheet()
        blender_editor_manipulation.set_context_space_data_ui_mode_to_action()



        for state_index in perso3d_model.states:

            action = blender_editor_manipulation.enter_animation_clip(name="Animation_" + state_index)
            blender_editor_manipulation.set_armature_active_action(blender_armature_obj, action)
            print("state " + str(state_index) + "/" + str(len(perso3d_model.states)))
            for frame_number in perso3d_model.states[state_index]:
                blender_editor_manipulation.enter_frame_number(frame_number=int(frame_number))
                touched_subobjects_hashes = set()  # type: Set[str]
                print("state " + str(state_index) + "/" + str(len(perso3d_model.states)) + ", frame " + frame_number + "/" + str(len(perso3d_model.states[state_index])))
                for subobject_key in perso3d_model.states[state_index][frame_number].data_blocks:
                    blender_objects_manipulation.deselect_all_pose_objects()
                    bpy.ops.pose.select_all(action='SELECT')
                    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

                    blender_animation_manipulator.animate_subobject(
                        blender_armature_obj=blender_armature_obj,
                        state_index=state_index,
                        frame_number=frame_number,
                        subobject=perso3d_model.states[state_index][frame_number].data_blocks[subobject_key],
                        blender_mesh_objects=blender_mesh_objects,
                        action=action,
                        subobject_hash=perso3d_model.states[state_index][frame_number].data_blocks[subobject_key].geometry_data_reference
                    )
                    touched_subobjects_hashes.add(perso3d_model.states[state_index][frame_number].data_blocks[subobject_key].geometry_data_reference)

                    blender_objects_manipulation.deselect_all_pose_objects()
                    bpy.ops.pose.select_all(action='SELECT')
                    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')



                not_touched_subobjects_hashes = set(perso3d_model.subobjects.keys()).difference(touched_subobjects_hashes)
                for not_touched_subobject_hash in not_touched_subobjects_hashes:
                    blender_objects_manipulation.deselect_all_pose_objects()
                    bpy.ops.pose.select_all(action='SELECT')
                    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

                    blender_animation_manipulator.animate_subobject(
                        blender_armature_obj=blender_armature_obj,
                        state_index=state_index,
                        frame_number=frame_number,
                        subobject=SubobjectCompressedFrameDataBlock(
                            key = "a",
                            transform = ObjectTransform(
                                position=Vector3(0,0,0),
                                rotation=Quaternion(0,0,0,1),
                                scale = Vector3(0,0,0)
                            ),
                            geometry_data_reference=not_touched_subobject_hash
                        ),
                        blender_mesh_objects=blender_mesh_objects,
                        subobject_hash=not_touched_subobject_hash,
                        action=action,
                    )

                    blender_objects_manipulation.deselect_all_pose_objects()
                    bpy.ops.pose.select_all(action='SELECT')
                    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
            
