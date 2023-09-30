define Carla = Character("Carla", color="#ffffff", callback= name_callback, cb_name="Carla")
define Parents = Character("Parents", color="#ffffff", callback= name_callback, cb_name="Parents")
define Mom = Character("Mom", color="#ffffff", callback= name_callback, cb_name="Mom")
define Dad = Character("Dad", color="#ffffff", callback= name_callback, cb_name="Dad")
define narrator = Character(callback= name_callback, cb_name="None")
define Demon = Character("????", color="#ffffff")

default ending_condition = 0 # > 30 for child ending, < 30 for adult ending

define -2 all_achievements = Achievement(
    name=_("Platinum Achievement"),
    id="platinum_achievement",
    description=_("Congrats! You unlocked every achievement!"),
    unlocked_image=Transform("gui/achievements/all.png"),
    hide_description=_("Get all other achievements."),
)
define adults_ending = Achievement(name=_("The Real Monster"), id="The_Real_Monster", description=_("Get Adult's Ending"), unlocked_image="gui/achievements/adults_ending.png", hide_description=True) 
define child_ending = Achievement(name=_("Just a Bit of Imagination"), id="Just_a_Bit_of_Imagination", description=_("Get Child's Ending"), unlocked_image="gui/achievements/childs_ending.png", hide_description=True) 
define Perfect_Parent = Achievement(name=_("Perfect Parent"), id="Perfect_Parent", description=_("Select every major choice for the Child's Ending"), unlocked_image="gui/achievements/perfect_parent.png", hide_description=True) 
define Carlas_Nightmare = Achievement(name=_("Carla's Nightmare"), id="Carlas_Nightmare", description=_("Select every major choice for the Adult's Ending"), unlocked_image="gui/achievements/carlas_nightmare.png", hide_description=True) 
define Swing_Now_Ask_Later = Achievement(name=_("Swing Now, Ask Later"), id="Swing_Now_Ask_Later", description=_("Attack the Prison monster at the first opportunity."), unlocked_image="gui/achievements/swing_now.png", hide_description=True) 
define Practically_Jaws = Achievement(name=_("Practically Jaws"), id="Practically_Jaws", description=_("Fill your air meter all the way during the underwater minigame."), unlocked_image="gui/achievements/jaws.png", hide_description=True) 

label start:
    jump act11 