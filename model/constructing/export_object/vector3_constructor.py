from model.perso.object_transform import Vector3


class Vector3Constructor:
    @classmethod
    def construct_from_json(cls, vector3_dict):
        return Vector3(
            x = vector3_dict["x"],
            y = vector3_dict["y"],
            z = vector3_dict["z"]
        )
