from model.constructing.perso_3d_model_loader import Perso3DModelLoader


class MainAddonLogic:
    def run(self):
        path_to_perso3d_file = "D:/"

        perso3d_model = Perso3DModelLoader().load(path_to_perso3d_file)
