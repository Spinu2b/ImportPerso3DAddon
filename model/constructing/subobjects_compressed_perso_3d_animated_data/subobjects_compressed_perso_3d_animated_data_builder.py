from model.constructing.compressed_frame_data_block.compressed_frame_data_block_dict_constructor import CompressedFrameDataBlockDictConstructor
from model.constructing.subobject_geometry_data_dict.subobject_geometry_data_dict_constructor import SubobjectGeometryDataDictConstructor
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class SubobjectsCompressedPerso3DAnimatedDataBuilder:
    def __init__(self):
        self.result = SubobjectsCompressedPerso3DAnimatedData()

    def parse_subobjects(self, subobjects_dict):
        self.result.subobjects = \
            SubobjectGeometryDataDictConstructor().construct_from_json(subobjects_dict)

    def add_state(self, state_index: int, state_frames_dict):
        self.result.states[state_index] = \
            CompressedFrameDataBlockDictConstructor().construct_from_json(state_frames_dict)

    def build(self) -> SubobjectsCompressedPerso3DAnimatedData:
        return self.result
