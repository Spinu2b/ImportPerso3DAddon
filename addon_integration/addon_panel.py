import bpy

class AddonPanel(bpy.types.Panel):
    bl_idname = "spinu2b_addon_panel"
    bl_label = "Raymap Perso 3D Import"
    bl_category = "Import Perso 3D addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        row = layout.row()
        row.prop(scene.perso_importer, "path", text="")
        operator_row = layout.row()
        operator_row.operator("view3d.import_perso3d", text="Import Perso 3D")