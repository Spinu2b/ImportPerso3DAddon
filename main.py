from model.constructing.perso_3d_animated_data.perso_3d_animated_data_loader import Perso3DAnimatedDataLoader


class MainAddonLogic:
    def run(self):
        path_to_perso3d_file = "D:/"

        perso3d_model = Perso3DAnimatedDataLoader().load(path_to_perso3d_file)
