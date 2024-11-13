import json
from model.constructing.subobjects_compressed_perso_3d_animated_data.subobjects_compressed_perso_3d_animated_data_loader import SubobjectsCompressedPerso3DAnimatedDataLoader


class MainAddonLogic:
    def run(self, file_path: str):
        path_to_perso3d_file = file_path
        perso3d_model = SubobjectsCompressedPerso3DAnimatedDataLoader().load(path_to_perso3d_file)
        print("done!")