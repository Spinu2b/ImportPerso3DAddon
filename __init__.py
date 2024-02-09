# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Perso3DImporter",
    "author" : "Spinu2b",
    "description" : "",
    "blender" : (4, 0, 2),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.absolute()))

import bpy
from bpy.props import (StringProperty, PointerProperty)
                       
from bpy.types import (PropertyGroup)

from addon_integration.import_perso3d_op import ImportPerso3DOperator
from addon_integration.addon_panel import AddonPanel

# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------

class MyProperties(PropertyGroup):
    path: StringProperty(
        name="",
        description="Path to .perso3d file",
        default="",
        subtype='FILE_PATH')

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------
    
classes = (
    MyProperties,
    ImportPerso3DOperator,
    AddonPanel
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.perso_importer = PointerProperty(type=MyProperties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.perso_importer
