from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator, KeyMap
import bpy
import os

root_dir = "../../../../../"
editing_kit = ""
c = open(root_dir + "config.ini", "r")
lines = c.readlines()
for line in lines:
    line = line.split("=")
    name = line[0]
    if name == "h3ek":
        editing_kit = line[1]

name = bpy.path.basename(bpy.context.blend_data.filepath)

def export_ass():
    bpy.ops.export_scene.fbx()
    os.system(editing_kit + "\\tool_fast.exe fbx-to-ass \"" + os.getcwd() + "\\" + name + ".fbx\" \"" + os.getcwd() + "\\" + name + ".ass\"")

def build_structure_from_blend():
    export_ass()
    os.system("xcopy \"" + name + ".ass\" \"" + editing_kit + "\\data\\levels\\mod_levels\\" + name + "\\structure\\\"")
    os.system(editing_kit + "\\tool_fast.exe structure levels\\mod_levels\\" + name + "\\structure\\")
    
    return {'FINISHED'}
    
class BlendToStructureExporter(Operator):
    bl_idname = "blend_structure_tag.export"
    bl_label = "Export Structure"
    
    def execute(self, context):
        return build_structure_from_blend()
    
def blend_structure_export(self, context):
    self.layout.operator(BlendToStructureExporter.bl_idname, text=".structure tag from geometry")

def register():
    bpy.utils.register_class(BlendToStructureExporter)
    bpy.types.TOPBAR_MT_file_export.append(blend_structure_export)
    
def unregister():
    bpy.utils.unregister_class(BlendToStructureExporter)
    bpy.types.TOPBAR_MT_file_export.remove(blend_structure_export)

if __name__ == "__main__":
    register()