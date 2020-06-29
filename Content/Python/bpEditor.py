import unreal

#This will help run check in a blueprint class:

# get the generated class, using a different load method than assets
blueprint_generated = unreal.load_object(None, "/Game/01_Blueprints/BP_Player.BP_Player_C")

# from that, get the class default object ( the actual template for the blueprint )
blueprint_class_default = unreal.get_default_object(blueprint_generated)

def DoIt():
    # set or get properties
    blueprint_class_default.set_editor_property("BaseTurnRate", 42)
    blueprint_class_default.get_editor_property("BaseTurnRate")