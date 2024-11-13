from typing import Dict

from model.perso.compressed_frame_data_block import CompressedFrameDataBlock
from model.perso.subobject_geometry_data import SubobjectGeometryData


class SubobjectsCompressedPerso3DAnimatedData:
    def __init__(self):
        self.states = dict()  # type: Dict[int, Dict[int, CompressedFrameDataBlock]]
        self.subobjects = dict()  # type: Dict[str, SubobjectGeometryData]
