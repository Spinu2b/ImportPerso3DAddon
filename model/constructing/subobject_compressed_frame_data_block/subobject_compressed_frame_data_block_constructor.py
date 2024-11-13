from model.constructing.export_object.object_transform_constructor import ObjectTransformConstructor
from model.perso.subobject_compressed_frame_data_block import SubobjectCompressedFrameDataBlock


class SubobjectCompressedFrameDataBlockConstructor:
    def construct_from_json(self, subobject_compressed_frame_data_block_dict):
        return SubobjectCompressedFrameDataBlock(
            key = subobject_compressed_frame_data_block_dict["key"],
            transform = ObjectTransformConstructor().construct_from_json(subobject_compressed_frame_data_block_dict["transform"]),
            geometry_data_reference = subobject_compressed_frame_data_block_dict["geometryDataReference"],
        )
