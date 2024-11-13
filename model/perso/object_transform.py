
class Vector3:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Quaternion:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class ObjectTransform:
    def __init__(self):
        self.position = Vector3(0,0,0)
        self.rotation = Quaternion(0,0,0,1)
        self.scale = Vector3(1,1,1)

    def __init__(self, position, rotation, scale):
        self.position = position
        self.rotation = rotation
        self.scale = scale    
