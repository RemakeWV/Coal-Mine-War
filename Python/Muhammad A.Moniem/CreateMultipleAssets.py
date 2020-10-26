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

totalRequiredBlueprints = 70
newAssetName = "BP_pythonMade_%d"
createdAssetsPath = "/Game/TestStuff"
slowTaskDisplayText = "Createing new assets....."

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Pawn)

assetTools = unreal.AssetToolsHelpers.get_asset_tools()

with unreal.ScopedSlowTask(totalRequiredBlueprints, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range(totalRequiredBlueprints):
        if ST.should_cancel():
            break
        newAsset = assetTools.create_asset(newAssetName%(x), createdAssetsPath, None, factory)
        unreal.EditorAssetLibrary.save_loaded_asset(newAsset)
        unreal.log("Just created an asset BP_PythonMade_%d via PYTHON API" %(x))
        ST.enter_progress_frame(1)