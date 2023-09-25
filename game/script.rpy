define Carla = Character("Carla", color="#ffffff", callback= name_callback, cb_name="Carla")
define Parents = Character("Parents", color="#ffffff", callback= name_callback, cb_name="Parents")
define Mom = Character("Mom", color="#ffffff", callback= name_callback, cb_name="Mom")
define Dad = Character("Dad", color="#ffffff", callback= name_callback, cb_name="Dad")
define narrator = Character(callback= name_callback, cb_name="None")
define Demon = Character("????", color="#ffffff")

default ending_condition = 0 # > 30 for adult ending, < 30 for child ending

define adults_ending = Achievement(name=_("The Real Monster"), id="The_Real_Monster", description=_("Get Adult's Ending"), unlocked_image="gui/achievements/itch_io.png", hide_description=False) 
define child_ending = Achievement(name=_("Just a Bit of Imagination"), id="Just_a_Bit_of_Imagination", description=_("Get Child's Ending"), unlocked_image="gui/achievements/itch_io.png", hide_description=False) 
define Perfect_Parent = Achievement(name=_("Perfect Parent"), id="Perfect_Parent", description=_("Select every major choice for the Child's Ending"), unlocked_image="gui/achievements/itch_io.png", hide_description=False) 
define Carlas_Nightmare = Achievement(name=_("Carla's Nightmare"), id="Carlas_Nightmare", description=_("Select every major choice for the Adult's Ending"), unlocked_image="gui/achievements/itch_io.png", hide_description=False) 
define Swing_Now_Ask_Later = Achievement(name=_("Swing Now, Ask Later"), id="Swing_Now_Ask_Later", description=_("Attack the Prison monster at the first opportunity."), unlocked_image="gui/achievements/itch_io.png", hide_description=False) 
define Practically_Jaws = Achievement(name=_("Practically Jaws"), id="Practically_Jaws", description=_("Fill your air meter all the way during the underwater minigame."), unlocked_image="gui/achievements/itch_io.png", hide_description=False) 

screen main_ui:
    textbutton _("Achievements") action ShowMenu("achievement_gallery") xalign 0.95 yalign 0.02
    # textbutton _("Reset Achivements") action Achievement.Reset() xalign 0.8 yalign 0.0
label start:
    show screen main_ui
    jump act11
