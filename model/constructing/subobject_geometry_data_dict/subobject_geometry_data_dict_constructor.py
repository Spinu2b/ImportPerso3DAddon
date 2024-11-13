from model.constructing.subobject_geometry_data_dict.subobject_geometry_data_constructor import SubobjectGeometryDataConstructor


class SubobjectGeometryDataDictConstructor:
    def __init__(self):
        self.result = dict()  # type: Dict[str, SubobjectGeometryData]

    def construct_from_json(self, subobject_geometry_data_dict):
        for subobject_geometry_data_hash in subobject_geometry_data_dict:
            self.result[subobject_geometry_data_hash] = \
                SubobjectGeometryDataConstructor().construct_from_json(subobject_geometry_data_dict[subobject_geometry_data_hash])
        return self.result
