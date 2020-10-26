import unreal

blueprintName = "M_NewMaterial"
blueprintPath = "/Game/04_Materials"

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Material)

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
myFancyNewAssetFile = assetTools.create_asset(blueprintName, blueprintPath, None, factory)

unreal.EditorAssetLibrary.save_loaded_asset(myFancyNewAssetFile)