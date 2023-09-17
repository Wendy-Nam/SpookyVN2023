define Carla = Character("Carla", color="#ffffff", callback= name_callback, cb_name="Carla")
define Parents = Character("Parents", color="#ffffff", callback= name_callback, cb_name="Parents")
define Mom = Character("Mom", color="#ffffff", callback= name_callback, cb_name="Mom")
define Dad = Character("Dad", color="#ffffff", callback= name_callback, cb_name="Dad")
define narrator = Character(callback= name_callback, cb_name="None")

screen Image_Tools:
    textbutton "Image Tools" action ShowMenu("image_tools")

label start:
    # jump shooting_game
    # show screen Image_Tools
    # show Dad
    # show Mom
    # show Parents at right
    scene bg livingroom_night
    show Dad
    show Mom
    show Carla at left
    jump act11
    