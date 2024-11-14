import copy
from typing import List
from model.perso.object_transform import Quaternion, Vector3


class BlenderEditModeArmatureNodeModel:
    def __init__(self,
                 name: str,
                 head_position_x: float, head_position_y: float, head_position_z: float,
                 tail_position_x: float, tail_position_y: float, tail_position_z: float,
                 position: Vector3, rotation: Quaternion, scale: Vector3):
        self.name = name  # type: str
        self.head_position_x = head_position_x  # type: float
        self.head_position_y = head_position_y  # type: float
        self.head_position_z = head_position_z  # type: float
        self.tail_position_x = tail_position_x  # type: float
        self.tail_position_y = tail_position_y  # type: float
        self.tail_position_z = tail_position_z  # type: float

        self.position = copy.deepcopy(position)  # type: Vector3
        self.rotation = copy.deepcopy(rotation)  # type: Quaternion
        self.scale = copy.deepcopy(scale)  # type: Vector3

class BlenderEditModeArmatureModel:
    def __init__(self):
        self.bones = []  # type: List[BlenderEditModeArmatureNodeModel]

    def add_bone(self, bone: BlenderEditModeArmatureNodeModel):
        self.bones.append(bone)    
