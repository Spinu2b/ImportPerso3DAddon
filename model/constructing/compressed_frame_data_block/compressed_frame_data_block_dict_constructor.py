

class CompressedFrameDataBlockDictConstructor:
    def __init__(self):
        self.result = dict()  # type: Dict[int, CompressedFrameDataBlock]

    def construct_from_json(self, compressed_frame_data_block_dict):
        raise NotImplementedError    
