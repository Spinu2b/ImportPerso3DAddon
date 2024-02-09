from model.perso.object_transform import ObjectTransform, Quaternion, Vector3

class Vector3Constructor:
    def construct_from_json(self, json_dict) -> Vector3:
        result = Vector3()
        result.x = json_dict["x"]
        result.y = json_dict["y"]
        result.z = json_dict["z"]

class QuaternionConstructor:
    def construct_from_json(self, json_dict) -> Quaternion:
        result = Quaternion()
        result.x = json_dict["x"]
        result.y = json_dict["y"]    
        result.z = json_dict["z"]
        result.w = json_dict["w"]


class ObjectTransformConstructor:
    def construct_from_json(self, json_dict) -> ObjectTransform:
        result = ObjectTransform()
        result.position = Vector3Constructor().construct_from_json(json_dict["position"])
        result.rotation = QuaternionConstructor().construct_from_json(json_dict["rotation"])
        result.scale = Vector3Constructor().construct_from_json(json_dict["scale"])
        return result
