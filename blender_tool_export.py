from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator, KeyMap
import bpy
import os
import subprocess

root_dir = os.path.realpath(__file__ + "\\..\\..\\")
kwargs = {}
c = open(root_dir + "\\config.ini", "r")
lines = c.readlines()
for line in lines:
    line = line.split("=")
    var_name = line[0]
    kwargs[var_name] = line[1].replace("\n", "")

name = bpy.path.basename(bpy.context.blend_data.filepath).replace(".blend", "")
tool_path = os.path.realpath(f"{kwargs['h3ek']}\\tool_fast.exe")

def export_ass(fbx_dir):
    bpy.ops.export_scene.fbx(filepath=fbx_dir + name + ".fbx")
    fbx_from = os.path.realpath(f"{fbx_dir}\\{name}.fbx")
    ass_to = os.path.realpath(f"{fbx_dir}\\{name}.ass")
    subprocess.run([tool_path, 'fbx-to-ass', fbx_from, ass_to])

def build_structure_from_blend():
    fbx_dir = f"{root_dir}\\{kwargs['blender_directory']}"
    export_ass(fbx_dir)
    subprocess.run(["xcopy", f"{fbx_dir}\\{name}.ass", "{kwargs['h3ek']}\\{kwargs['blender_directory']}\\structure"])
    subprocess.run([tool_path, "structure", f"{kwargs['tag_directories']}\\structure"])
    subprocess.run("build.cmd")
    
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