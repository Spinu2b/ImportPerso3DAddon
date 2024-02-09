from model.constructing.perso_3d_animated_data.perso_3d_animated_data_builder import Perso3DAnimatedDataBuilder
from model.perso.perso_3d_animated_data import Perso3DAnimatedData


class Perso3DAnimatedDataConstructor:
    def construct_from_json(self, json_dict) -> Perso3DAnimatedData:
        result_builder = Perso3DAnimatedDataBuilder()
        for state_index in json_dict["states"]:
            result_builder.add_state(
                state_index=state_index,
                state_frames_dict=json_dict["states"][state_index]
            )     
        return result_builder.build()

