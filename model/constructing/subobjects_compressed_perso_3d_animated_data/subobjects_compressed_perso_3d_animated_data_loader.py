import json

from model.constructing.subobjects_compressed_perso_3d_animated_data.subobjects_compressed_perso_3d_animated_data_constructor import SubobjectsCompressedPerso3DAnimatedDataConstructor
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class SubobjectsCompressedPerso3DAnimatedDataLoader:
    def load(self, file_path: str) -> SubobjectsCompressedPerso3DAnimatedData:
        with open(file_path, 'r') as json_file:
            json_dict = json.loads(json_file.read())
        return SubobjectsCompressedPerso3DAnimatedDataConstructor().construct_from_json(json_dict)
    
