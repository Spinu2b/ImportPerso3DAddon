from typing import List
from model.constructing.export_object.object_transform_constructor import Vector3Constructor
from model.perso.object_transform import Vector3


class SubobjectGeometryDataVerticesListConstructor:
    def construct_from_json(self, vertices_dicts_list):
        result = []  # type: List[Vector3]

        for vertex_dict in vertices_dicts_list:
            result.append(
                Vector3Constructor().construct_from_json(
                    vertex_dict                    
                )
            )

        return result