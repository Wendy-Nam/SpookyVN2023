define Carla = Character("Carla", color="#ffffff", callback= name_callback, cb_name="Carla")
define Parents = Character("Parents", color="#ffffff", callback= name_callback, cb_name="Parents")
define Mom = Character("Mom", color="#ffffff", callback= name_callback, cb_name="Mom")
define Dad = Character("Dad", color="#ffffff", callback= name_callback, cb_name="Dad")
define narrator = Character(callback= name_callback, cb_name="None")
define Demon = Character("????", color="#ffffff")
default ending_condition = 0 # > 30 for adult ending, < 30 for child ending

define underwater_text = WaveShader(amp = 0, melt="both", melt_params=(15, 0.5, 1, 0.2))

label start:
    jump act11
    