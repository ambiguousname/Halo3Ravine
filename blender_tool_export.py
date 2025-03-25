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
tool_path = ""
struct_name = ""
struct_directory = ""
    
class BlendToStructureExporter(Operator):
    bl_idname = "blend_structure_tag.export"
    bl_label = "Export Active Collection As .structure"

    def export_ass(self, fbx_dir):
        bpy.ops.export_scene.fbx(filepath=f"{fbx_dir}{self.name}.fbx", global_scale=0.3, axis_forward='-Z', axis_up='Y', use_active_collection=True, use_mesh_modifiers=True)
        fbx_from = os.path.realpath(f"{fbx_dir}\\{self.name}.fbx")
        ass_to = os.path.realpath(f"{fbx_dir}\\{self.name}.ass")
        subprocess.run([tool_path, 'fbx-to-ass', fbx_from, ass_to])

    def build_structure(self):
        fbx_dir = f"{root_dir}\\{kwargs['blender_directory']}"
        self.export_ass(fbx_dir)
        subprocess.run(["xcopy", "/y", "/f", f"{fbx_dir}\\{self.name}.ass", f"{kwargs['h3ek']}\\{kwargs['blender_directory']}"])
        os.chdir(kwargs['h3ek'])
        subprocess.run(["tool_fast.exe", "structure", struct_directory + "\\structure\\" + self.name + ".ass"])
        os.chdir(root_dir)
        subprocess.run("build.cmd")
        return {'FINISHED'}
    
    def execute(self, context):
        self.name = struct_name + "_" + bpy.context.view_layer.active_layer_collection.name
        return self.build_structure()

class ExportSeams(Operator):
    bl_idname = "blend_seam_structure.export"
    bl_label = "Generate Structure Seams"

    def execute(self, context):
        os.chdir(kwargs['h3ek'])
        subprocess.run(["tool_fast.exe", "structure-seams", struct_directory])
        return {'FINISHED'}

class HaloHelper(bpy.types.Panel):
    bl_idname = "UI_PT_halo_helper"
    bl_label = "Halo Helper"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Halo Helper"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Export Tags")
        box.operator("blend_structure_tag.export")
        box.operator("blend_seam_structure.export")

def blend_structure_export(self, context):
    self.layout.operator(BlendToStructureExporter.bl_idname, text=".structure tag from collection")

def register():
    bpy.utils.register_class(BlendToStructureExporter)
    bpy.utils.register_class(ExportSeams)
    bpy.utils.register_class(HaloHelper)
    
def unregister():
    bpy.utils.unregister_class(BlendToStructureExporter)
    bpy.utils.unregister_class(ExportSeams)
    bpy.utils.unregister_class(HaloHelper)

if __name__ == "__main__":
    root_dir = bpy.path.abspath("//")

    c = open(root_dir + "\\config.ini", "r")
    lines = c.readlines()
    for line in lines:
        line = line.split("=")
        var_name = line[0]
        kwargs[var_name] = line[1].replace("\n", "")
    tool_path = os.path.realpath(f"{kwargs['h3ek']}\\tool_fast.exe")
    
    struct_directory = os.path.normpath(kwargs['tag_directories'])
    struct_name = bpy.path.basename(bpy.context.blend_data.filepath).replace(".blend", "")
    
    register()