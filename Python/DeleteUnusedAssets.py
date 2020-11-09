import unreal

workingPath = "/Game/"

@unreal.uclass()
class MyEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

AssetLib = MyEditorAssetLibrary()

allAssets = AssetLib.list_assets(workingPath, True, False)

processingAssetPath = ""
allAssetsCount = len(allAssets)

if (allAssetsCount > 0):
    with unreal.ScopedSlowTask(allAssetsCount, processingAssetPath) as ST:
        ST.make_dialog(True)
        for asset in allAssets:
            processingAssetPath = asset
            deps = AssetLib.find_package_referencers_for_asset(asset, False)
            if (len(deps) <= 0):
                unreal.log("Deleteing %s" % asset)
                AssetLib.delete_asset(asset)
            if ST.should_cancel():
                break
            ST.enter_progress_frame (1, processingAssetPath)