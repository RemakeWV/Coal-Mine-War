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
import sys

actorsCount = int(float(sys.argv[1]))
rotationStep = int(float(sys.argv[2]))
positionOffset = float(sys.argv[3])
slowTaskDisplayText = "Spawning actors in the level...."

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass



selectedAssets = MyEditorUtility().get_selected_assets()

with unreal.ScopedSlowTask(actorsCount, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for x in range (actorsCount):
        if ST.should_cancel():
            break
        unreal.EditorLevelLibrary.spawn_actor_from_object(selectedAssets[0], unreal.Vector(positionOffset*x, positionOffset*x, 30.0), unreal.Rotator(0.0, 0.0, rotationStep*x))
        unreal.log("Just added an actor to the level!")
        ST.enter_progress_frame(1)