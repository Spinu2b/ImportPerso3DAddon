from typing import Dict

from model.constructing.perso_3d_frame_export_data.perso_3d_frame_export_data_constructor import Perso3DFrameExportDataConstructor
from model.perso.perso_3d_frame_export_data import Perso3DFrameExportData


class Perso3DFrameExportDataFramesConstructor:
    def construct_from_json(self, json_dict) -> Dict[int, Perso3DFrameExportData]:
        result = dict()

        for frame_number in json_dict:
            result[frame_number] = Perso3DFrameExportDataConstructor().construct_from_json(json_dict[frame_number])

        return result        
