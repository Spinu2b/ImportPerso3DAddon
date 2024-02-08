from model.constructing.perso_3d_frame_export_data \
    .perso_3d_frame_export_data_frames_constructor import Perso3DFrameExportDataFramesConstructor
from model.perso.perso_3d_animated_data import Perso3DAnimatedData


class Perso3DAnimatedDataBuilder:
    def __init__(self):
        self.result = Perso3DAnimatedData()

    def add_state(self, state_index: int, state_frames_dict):
        self.result.states[state_index] = \
            Perso3DFrameExportDataFramesConstructor().construct_from_json(state_frames_dict)

    def build(self) -> Perso3DAnimatedData:
        return self.result
