from blender_api.blender_operations.constructing_animated_model.blender_animated_model_creator import BlenderAnimatedModelCreator
from model.perso.subobjects_compressed_perso_3d_animated_data import SubobjectsCompressedPerso3DAnimatedData


class BlenderAnimatedModelConstructor:
    def build_animated_model(self, perso3d_model: SubobjectsCompressedPerso3DAnimatedData):
        BlenderAnimatedModelCreator().construct_using(
            perso3d_model=perso3d_model
        )
