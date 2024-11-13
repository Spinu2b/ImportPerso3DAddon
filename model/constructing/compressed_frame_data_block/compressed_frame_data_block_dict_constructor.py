

from model.constructing.compressed_frame_data_block.compressed_frame_data_block_constructor import CompressedFrameDataBlockConstructor


class CompressedFrameDataBlockDictConstructor:
    def __init__(self):
        self.result = dict()  # type: Dict[int, CompressedFrameDataBlock]

    def construct_from_json(self, compressed_frame_data_block_dict):
        for frame_number in compressed_frame_data_block_dict:
            self.result[frame_number] = \
                CompressedFrameDataBlockConstructor().construct_from_json(compressed_frame_data_block_dict[frame_number])
            
        return self.result
