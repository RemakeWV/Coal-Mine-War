import unreal

# Path on disk to the asset you want to import
mesh_path = 'C:/path/to/mesh.fbx'
#This would bet set in the editor, using command line before running fbxImporter.import_assets()

# helper function for easy task creation, like a template
def build_mesh_import_task(filename, destination_path, destination_name=''):

    # the task, and the additional fbx options, since it is a mesh
    task = unreal.AssetImportTask()
    fbx_options = unreal.FbxImportUI()

    # basic task properties
    task.set_editor_property('automated', True)
    task.set_editor_property('filename', filename)
    task.set_editor_property('destination_path', destination_path)
    # if destination_name is '' it will use the on-disk filename
    task.set_editor_property('destination_name', destination_name)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    task.set_editor_property('options', fbx_options)

    # additional options specifically for meshes
    fbx_options.set_editor_property('import_mesh', True)
    fbx_options.set_editor_property('import_textures', False)
    fbx_options.set_editor_property('import_as_skeletal', False)
    fbx_options.set_editor_property('import_materials', False)

    # settings specifically for static meshes
    fbx_options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    fbx_options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', False)
    return task

def import_assets():
    # construct the task, passing the path on disk and the location to store it. 
    mesh_import_task = build_mesh_import_task(mesh_path, '/Game/07_Props')


    # using the very handy AssetToolsHelpers to do the work.
    # Note it takes a list, and so many imports can be batched
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([mesh_import_task])