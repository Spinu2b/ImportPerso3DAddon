from typing import Dict

from model.animations.model.blender_edit_mode_armature_model import BlenderEditModeArmatureModel
from model.objects.constructing.armature.subobjects_compressed_perso_3d_animated_data_to_blender_edit_mode_armature_model_converter import SubobjectsCompressedPerso3DAnimatedDataToBlenderEditModeArmatureModelConverter
from model.perso.compressed_frame_data_block import CompressedFrameDataBlock
from model.perso.subobject_geometry_data import SubobjectGeometryData


class SubobjectsCompressedPerso3DAnimatedData:
    def __init__(self):
        self.states = dict()  # type: Dict[int, Dict[int, CompressedFrameDataBlock]]
        self.subobjects = dict()  # type: Dict[str, SubobjectGeometryData]

    def get_blender_edit_mode_armature_model(self) -> BlenderEditModeArmatureModel:
        return SubobjectsCompressedPerso3DAnimatedDataToBlenderEditModeArmatureModelConverter().convert(self)