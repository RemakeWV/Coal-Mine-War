#										_
#									   (_)
#  _ __ ___   __ _ _ __ ___   ___  _ __  _  ___ _ __ ___
# | '_ ` _ \ / _` | '_ ` _ \ / _ \| '_ \| |/ _ \ '_ ` _ \
# | | | | | | (_| | | | | | | (_) | | | | |  __/ | | | | |
# |_| |_| |_|\__,_|_| |_| |_|\___/|_| |_|_|\___|_| |_| |_|
#					www.mamoniem.com
#					  www.ue4u.xyz
#Copyright 2020 Muhammad A.Moniem (@_mamoniem). All Rights Reserved.
#

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
                unreal.log(">>>>>> Deleteing >>>>> %s" % asset)
                AssetLib.delete_asset(asset)
            if ST.should_cancel():
                break
            ST.enter_progress_frame (1, processingAssetPath)