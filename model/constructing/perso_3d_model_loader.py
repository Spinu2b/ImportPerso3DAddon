import json

from model.constructing.perso_3d_model_constructor import Perso3DModelConstructor


class Perso3DModelLoader:
    def load(file_path: str) -> 'Perso3DModel':
        with open(file_path, 'r') as json_file:
            json_dict = json.loads(json_file.read())
        return Perso3DModelConstructor().construct_from_json(json_dict)
    
