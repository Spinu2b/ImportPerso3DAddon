from model.constructing.export_object.object_transform_constructor import Vector2Constructor
from model.perso.uv_map import UVMap


class SubobjectGeometryDataUvMapConstructor:
    def construct_from_json(self, uv_map_dict):
        result = UVMap()
        for coordinates in uv_map_dict["uv"]:
            result.uv.append(Vector2Constructor().construct_from_json(coordinates))
        return result    
