from model.constructing.export_object.frame_hierarchy_tree_constructor import FrameHierarchyTreeConstructor
from model.constructing.export_object.object_transform_constructor import ObjectTransformConstructor
from model.perso.perso_3d_frame_export_data import Perso3DFrameExportData


class Perso3DFrameExportDataConstructor:
    def construct_from_json(self, json_dict) -> Perso3DFrameExportData:
        result = Perso3DFrameExportData()
        result.perso_transform = ObjectTransformConstructor().construct_from_json(json_dict["persoTransform"])
        result.frame_hierarchy_tree = FrameHierarchyTreeConstructor().construct_from_json(json_dict["frameHierarchyTree"])
        return result
