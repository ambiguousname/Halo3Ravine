from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator, KeyMap
import bpy
import os

root_dir = os.path.realpath(__file__ + "\\..\\..\\")
kwargs = {}
c = open(root_dir + "\\config.ini", "r")
lines = c.readlines()
for line in lines:
    line = line.split("=")
    var_name = line[0]
    kwargs[var_name] = line[1].replace("\n", "")

name = bpy.path.basename(bpy.context.blend_data.filepath).replace(".blend", "")

def export_ass(fbx_dir):
    bpy.ops.export_scene.fbx(filepath=fbx_dir + name + ".fbx")
    os.system(f"\"{kwargs['h3ek']}\\tool_fast.exe\" fbx-to-ass \"{fbx_dir}\\{name}.fbx\" \"{fbx_dir}\\{name}.ass\"")

def build_structure_from_blend():
    fbx_dir = f"{root_dir}\\{kwargs['blender_directory']}"
    export_ass(fbx_dir)
    os.system(f"xcopy \"{fbx_dir}\\{name}.ass\" \"{kwargs['h3ek']}\\{kwargs['blender_directory']}\\structure\\\"")
    os.system(f"\"{kwargs['h3ek']}\\tool_fast.exe\" structure {kwargs['tag_directories']}\\structure\\")
    os.system("build.cmd")
    
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