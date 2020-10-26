import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

EdUtil = MyEditorUtility()

selectedActors = EdUtil.get_selection_set()

for actor in selectedActors:
    #actor.set_editor_property("group_name", "SmallProp")
    unreal.log_warning(actor.get_full_name())
    actor.set_editor_property("generate_lightmap_u_vs", "true")