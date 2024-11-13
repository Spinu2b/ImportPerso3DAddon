from typing import Dict
from model.perso.subobject_compressed_frame_data_block import SubobjectCompressedFrameDataBlock


class CompressedFrameDataBlock:
    def __init__(self):
        self.data_blocks = dict()  # type: Dict[str, SubobjectCompressedFrameDataBlock]
