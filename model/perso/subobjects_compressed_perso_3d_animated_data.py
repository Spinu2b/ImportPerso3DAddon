from typing import Dict


class SubobjectsCompressedPerso3DAnimatedData:
    def __init__(self):
        self.states = dict()  # type: Dict[int, Dict[int, CompressedFrameDataBlock]]
        self.subobjects = dict()  # type: Dict[str, SubobjectGeometryData]
