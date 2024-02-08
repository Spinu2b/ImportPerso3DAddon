import json

from model.constructing.perso_3d_animated_data.perso_3d_animated_data_constructor import Perso3DAnimatedDataConstructor
from model.perso.perso_3d_animated_data import Perso3DAnimatedData


class Perso3DAnimatedDataLoader:
    def load(file_path: str) -> Perso3DAnimatedData:
        with open(file_path, 'r') as json_file:
            json_dict = json.loads(json_file.read())
        return Perso3DAnimatedDataConstructor().construct_from_json(json_dict)
    
