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

totalFrames = 500000
textDisplay = "i love python, an i guess i'll be using this for a while!"

with unreal.ScopedSlowTask(totalFrames, textDisplay) as ST:
    ST.make_dialog(True)
    for i in range (totalFrames):
        if ST.should_cancel():
            break
        unreal.log("one step!!!!")
        ST.enter_progress_frame(1)