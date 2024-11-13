from typing import List, Tuple

from model.perso.object_transform import Vector3


class SubobjectGeometryData:
    def __init__(self, key: str, vertices: List[Vector3], triangles: List[int]):
        self.key = key  # type: str
        self.vertices = vertices  # type: List[Vector3]
        self.triangles = triangles  # type: List[int]

    def get_blender_pydata_form(self):
        def flatten(object):
            for item in object:
                if isinstance(item, (list)):
                    yield from flatten(item)
                else:
                    yield item

        reformed_triangles = []  # type: List[List[int]]

        for triangle_index in range(int(len(self.triangles) / 3)):
            reformed_triangles.append(
                [self.triangles[triangle_index*3],
                 self.triangles[triangle_index*3+1],
                 self.triangles[triangle_index*3+2]]
            )

        vertices_list = [(v.x, v.y, v.z) for v in self.vertices]
        edges_list = [list(x) for x in list(set(flatten([[frozenset([f[0], f[1]]), frozenset([f[1], f[2]]),
                                                          frozenset([f[2], f[0]])] for f in
                                                         reformed_triangles])))]
        triangles_list = [(f[0], f[1], f[2]) for f in reformed_triangles]
        return vertices_list, edges_list, triangles_list
