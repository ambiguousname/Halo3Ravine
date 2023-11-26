from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator, KeyMap
import bpy
import os
import subprocess

bl_info = {
    "name": "Halo Export Tool",
    "blender": (3,6,1),
    "category": "Object",
}

kwargs = {}
root_dir = ""
struct_name = ""
name = ""
tool_path = ""

def export_ass(fbx_dir):
    bpy.ops.export_scene.fbx(filepath=fbx_dir + name + ".fbx", global_scale=0.3, axis_forward='-Z', axis_up='Y', use_active_collection=True)
    fbx_from = os.path.realpath(f"{fbx_dir}\\{name}.fbx")
    ass_to = os.path.realpath(f"{fbx_dir}\\{name}.ass")
    subprocess.run([tool_path, 'fbx-to-ass', fbx_from, ass_to])

def build_structure_from_blend():
    fbx_dir = f"{root_dir}\\{kwargs['blender_directory']}"
    export_ass(fbx_dir)
    subprocess.run(["xcopy", "/y", "/f", f"{fbx_dir}\\{name}.ass", f"{kwargs['h3ek']}\\{kwargs['blender_directory']}"])
    os.chdir(kwargs['h3ek'])
    struct_directory = os.path.normpath(kwargs['tag_directories'] + "\\structure\\" + struct_name + ".ass")
    subprocess.run(["tool_fast.exe", "structure-seams", struct_directory])
    subprocess.run(["tool_fast.exe", "structure", struct_directory])
    os.chdir(root_dir)
    subprocess.run("build.cmd")
    
    return {'FINISHED'}
    
class BlendToStructureExporter(Operator):
    bl_idname = "blend_structure_tag.export"
    bl_label = "Export Structure"
    
    def execute(self, context):
        global root_dir
        global kwargs
        global name
        global struct_name
        global tool_path
        root_dir = bpy.path.abspath("//")
        c = open(root_dir + "\\config.ini", "r")
        lines = c.readlines()
        for line in lines:
            line = line.split("=")
            var_name = line[0]
            kwargs[var_name] = line[1].replace("\n", "")
        
        struct_name = bpy.path.basename(bpy.context.blend_data.filepath).replace(".blend", "")
        name = struct_name + "_" + bpy.context.view_layer.active_layer_collection.name
        tool_path = os.path.realpath(f"{kwargs['h3ek']}\\tool_fast.exe")
        return build_structure_from_blend()
    
def blend_structure_export(self, context):
    self.layout.operator(BlendToStructureExporter.bl_idname, text=".structure tag from collection")

def register():
    bpy.utils.register_class(BlendToStructureExporter)
    bpy.types.TOPBAR_MT_file_export.append(blend_structure_export)
    
def unregister():
    bpy.utils.unregister_class(BlendToStructureExporter)
    bpy.types.TOPBAR_MT_file_export.remove(blend_structure_export)

if __name__ == "__main__":
    register()