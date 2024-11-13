from typing import List

from model.perso.object_transform import Vector3


class SubobjectGeometryData:
    def __init__(self, key: str, vertices: List[Vector3], triangles: List[int]):
        self.key = key  # type: str
        self.vertices = vertices  # type: List[Vector3]
        self.triangles = triangles  # type: List[int]
