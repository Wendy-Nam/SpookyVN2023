define Carla = Character("Carla", color="#ffffff", callback= name_callback, cb_name="Carla")
define Parents = Character("Parents", color="#ffffff", callback= name_callback, cb_name="Parents")
define Mom = Character("Mom", color="#ffffff", callback= name_callback, cb_name="Mom")
define Dad = Character("Dad", color="#ffffff", callback= name_callback, cb_name="Dad")
define narrator = Character(callback= name_callback, cb_name="None")

label start:
    jump underwater_game
    # jump act11
    