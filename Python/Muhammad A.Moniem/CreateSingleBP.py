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

blueprintName = "MyEpicBPActorClass"
blueprintPath = "/Game/AutoCreated"

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.PlayerController)

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
myFancyNewAssetFile = assetTools.create_asset(blueprintName, blueprintPath, None, factory)

unreal.EditorAssetLibrary.save_loaded_asset(myFancyNewAssetFile)