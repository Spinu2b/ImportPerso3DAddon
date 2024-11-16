from model.perso.object_transform import ObjectTransform, Quaternion, Vector2, Vector3


class Vector2Constructor:
    def construct_from_json(self, json_dict) -> Vector2:
        result = Vector3(0,0,0)
        result.x = json_dict["x"]
        result.y = json_dict["y"]
        return result

class Vector3Constructor:
    def construct_from_json(self, json_dict) -> Vector3:
        result = Vector3(0,0,0)
        result.x = json_dict["x"]
        result.y = json_dict["z"]
        result.z = json_dict["y"]
        return result

class QuaternionConstructor:
    def construct_from_json(self, json_dict) -> Quaternion:
        result = Quaternion(0,0,0,1)
        result.x = json_dict["x"]
        result.y = json_dict["z"]    
        result.z = json_dict["y"]
        result.w = -json_dict["w"]
        return result


class ObjectTransformConstructor:
    def construct_from_json(self, json_dict) -> ObjectTransform:
        result = ObjectTransform(position=Vector3(0,0,0), rotation=Quaternion(0,0,0,1), scale=Vector3(1,1,1))
        result.position = Vector3Constructor().construct_from_json(json_dict["position"])
        result.rotation = QuaternionConstructor().construct_from_json(json_dict["rotation"])
        result.scale = Vector3Constructor().construct_from_json(json_dict["scale"])
        return result
