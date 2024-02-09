import bpy

from bpy_extras.io_utils import ImportHelper

class FilteredFiledialog(bpy.types.Operator, ImportHelper):
    bl_idname = "pathload.test"
    bl_label = ''
    filename_ext = ''
    filter_glob = bpy.props.StringProperty(
        default="",
        options={'HIDDEN'},
        maxlen=255  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        setattr(self.string_prop_namespace, self.string_prop_name, bpy.path.relpath(self.filepath))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.filter_glob = "*" + ";*".join(self.ext)
        return super().invoke(context, event)

    @classmethod
    def add(cls, layout, string_prop_namespace, string_prop_name, *ext):
        cls.ext = ext
        cls.string_prop_namespace = string_prop_namespace
        cls.string_prop_name = string_prop_name
        col = layout.split(factor = .33)
        col.label(string_prop_namespace.bl_rna.properties[string_prop_name].name)
        row = col.row(align=True)
        if string_prop_namespace.bl_rna.properties[string_prop_name].subtype != 'NONE':
            row.label("ERROR: Change subtype of {} property to 'NONE'".format(string_prop_name), icon='ERROR')
        else:
            row.prop(string_prop_namespace, string_prop_name, icon_only=True)
            row.operator(cls.bl_idname, icon='FILESEL')

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