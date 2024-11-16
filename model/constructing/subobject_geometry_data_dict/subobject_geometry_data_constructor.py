from model.constructing.subobject_geometry_data_dict.subobject_geometry_data_texture_constructor import SubobjectGeometryDataTextureConstructor
from model.constructing.subobject_geometry_data_dict.subobject_geometry_data_triangles_list_constructor import SubobjectGeometryDataTrianglesListConstructor
from model.constructing.subobject_geometry_data_dict.subobject_geometry_data_uv_map_constructor import SubobjectGeometryDataUvMapConstructor
from model.constructing.subobject_geometry_data_dict.subobject_geometry_data_vertices_list_constructor import SubobjectGeometryDataVerticesListConstructor
from model.perso.subobject_geometry_data import SubobjectGeometryData


class SubobjectGeometryDataConstructor:
    def __init__(self):
        self.result = None  # type: SubobjectGeometryData

    def construct_from_json(self, subobject_geometry_data_dict):
        return SubobjectGeometryData(
            key=subobject_geometry_data_dict["key"],
            vertices=SubobjectGeometryDataVerticesListConstructor().construct_from_json(subobject_geometry_data_dict["vertices"]),
            triangles=SubobjectGeometryDataTrianglesListConstructor().construct_from_json(subobject_geometry_data_dict["triangles"]),
            uv_map=SubobjectGeometryDataUvMapConstructor().construct_from_json(subobject_geometry_data_dict["uvMap"]),
            texture=SubobjectGeometryDataTextureConstructor().construct_from_json(subobject_geometry_data_dict["texture"])
        )
        