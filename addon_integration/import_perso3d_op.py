import bpy
from main import MainAddonLogic

class ImportPerso3DOperator(bpy.types.Operator):
    bl_idname = "view3d.import_perso3d"
    bl_label = "Simple operator"
    bl_description = "Import Perso 3D"

    def execute(self, context):
        MainAddonLogic().run(context.scene.perso_importer.path)
        return {'FINISHED'}