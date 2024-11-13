

class SubobjectGeometryDataDictConstructor:
    def __init__(self):
        self.result = dict()  # type: Dict[str, SubobjectGeometryData]

    def construct_from_json(self, subobject_geometry_data_dict):
        raise NotImplementedError