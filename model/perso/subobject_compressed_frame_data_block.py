from model.perso.object_transform import ObjectTransform


class SubobjectCompressedFrameDataBlock:
    def __init__(self, key: str, transform: ObjectTransform, geometry_data_reference: str):
        self.key = key
        self.transform = transform
        self.geometry_data_reference = geometry_data_reference
