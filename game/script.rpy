define Carla = Character("Carla", color="#00ff00", callback= name_callback, cb_name="Carla")
define Parents = Character("Parents", color="#0000ff", callback= name_callback, cb_name="Parents")
define Mom = Character("Mom", color="#71009e", callback= name_callback, cb_name="Mom")
define Dad = Character("Dad", color="#047fc2", callback= name_callback, cb_name="Dad")
define narrator = Character(color="#000000", callback= name_callback, cb_name="None")

screen Image_Tools:
    textbutton "Image Tools" action ShowMenu("image_tools")

label start:
    show screen Image_Tools
    # show Dad
    # show Mom
    # show Parents at right
    scene bg livingroom_night
    show Dad
    show Mom
    show Carla at left
    jump act11
    