from model.perso.texture import Texture

class Color:
    pass


class ColorConstructor:
    def construct_from_json(self, color_dict):
        result = Color()
        result.r = color_dict["r"]
        result.g = color_dict["g"]
        result.b = color_dict["b"]
        result.a = color_dict["a"]
        return result

class SubobjectGeometryDataTextureConstructor:
    def construct_from_json(self, texture_dict):
        result = Texture()
        result.width = texture_dict["width"]
        result.height = texture_dict["height"]
        for pixel in texture_dict["pixels"]:
            result.pixels.append(ColorConstructor().construct_from_json(pixel))
        return result
