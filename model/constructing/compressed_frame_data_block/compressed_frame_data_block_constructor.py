from model.constructing.subobject_compressed_frame_data_block.subobject_compressed_frame_data_block_constructor import SubobjectCompressedFrameDataBlockConstructor
from model.perso.compressed_frame_data_block import CompressedFrameDataBlock


class CompressedFrameDataBlockConstructor:
    def construct_from_json(self, compressed_frame_data_block_dict):
        result = CompressedFrameDataBlock()

        for subobject_key in compressed_frame_data_block_dict["dataBlocks"]:
            result.data_blocks[subobject_key] = \
                SubobjectCompressedFrameDataBlockConstructor() \
                    .construct_from_json(compressed_frame_data_block_dict["dataBlocks"][subobject_key])
            
        return result    
