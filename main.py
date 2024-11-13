import json
from model.constructing.subobjects_compressed_perso_3d_animated_data.subobjects_compressed_perso_3d_animated_data_loader import SubobjectsCompressedPerso3DAnimatedDataLoader
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


def remove_empty_states(perso3d_model: SubobjectsCompressedPerso3DAnimatedData):
    perso3d_model.states = {k: v for k, v in perso3d_model.states.items() if len(v) > 0}

class MainAddonLogic:
    def run(self, file_path: str):
        path_to_perso3d_file = file_path
        perso3d_model = SubobjectsCompressedPerso3DAnimatedDataLoader().load(path_to_perso3d_file)
        remove_empty_states(perso3d_model)
        print("done!")