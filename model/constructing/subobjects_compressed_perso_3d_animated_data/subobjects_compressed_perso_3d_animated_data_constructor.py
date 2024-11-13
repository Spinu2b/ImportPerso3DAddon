from model.constructing.subobjects_compressed_perso_3d_animated_data.subobjects_compressed_perso_3d_animated_data_builder import SubobjectsCompressedPerso3DAnimatedDataBuilder
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class SubobjectsCompressedPerso3DAnimatedDataConstructor:
    def construct_from_json(self, json_dict) -> SubobjectsCompressedPerso3DAnimatedData:
        result_builder = SubobjectsCompressedPerso3DAnimatedDataBuilder()
        result_builder.parse_subobjects(json_dict["subobjects"])
        for state_index in json_dict["states"]:
            result_builder.add_state(
                state_index=state_index,
                state_frames_dict=json_dict["states"][state_index]
            )     
        return result_builder.build()

