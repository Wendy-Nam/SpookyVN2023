
label bash_the_door:
    """
    With what little you have left in you, your fist slams on the door, hoping that it'll move.
    
    You feel the monster swiftly approaching, but before you can do anything more to the door.
    """
    
    jump its_too_late_the_monster_swallows_you_whole

label check_back:
    """
    The temptation is too strong and you turn your head.
    
    To your horror, the monster's jaw is agape, ready to swallow you whole.
    
    You let out a gasp, not realizing that was the last of your air and you stop swimming.
    
    With no energy to carry on, you make one push for the door.
    """
    
    jump its_too_late_the_monster_swallows_you_whole

label check_her_bookshelves:
    """
    The bookshelves are littered with horror movie merchandise that you forgot purchasing.
    
    A suspicious notebook catches your eye.
    """
    
    menu:
        "Read the notebook.":
            jump read_the_notebook
        "Continue your search through Carla's room.":
            jump continue_your_search_through_carlas_room

label check_the_nightstand:
    "Carla’s nightstand has nothing of interest."
    
    jump continue_your_search_through_carlas_room

label check_under_her_bed:
    """
    Under her bed are remnants of her old toys and books before she found her love for horror.
    
    Colorful books and soft plushies that remind you of the carnival incident and compels you to pull away from the bed.
    
    Oddly enough, you’re happy that Carla is in the phase she’s in now.
    """
    
    jump continue_your_search_through_carlas_room

default searched = {'bed':False, 'booksheleves':False, 'nightstand':False}

label continue_your_search_through_carlas_room:
    $ all_searched = not all(searched.values())
    if all_searched == False:
        menu:
            "Check under her bed.":
                $ searched['bed'] = True
                jump check_under_her_bed
            "Check her bookshelves.":
                $ searched['bookshelves'] = True
                jump check_her_bookshelves
            "Check the nightstand.":
                $ searched['nightstand'] = True
                jump check_the_nightstand
    else:
        # Once the player selects all of the options once (They don't have to look at the notebook), they can move on.
        menu:
            "Go back to the living room.":
                jump go_back_to_the_living_room

label enter_the_underwater_cave:
    """
    Though the cave is incredibly small, you manage to squeeze your way through enough to reach an air pocket. 
    
    You have enough space to keep yourself afloat wondering if you’ll be stuck here forever. 
    
    As you start to run out of energy to stay afloat, you feel a tugging at your leg.
    
    You scream in panic and Carla’s head pops out of the water, unfazed by the situation.
    """

    $ lipsync(Carla, "act3", 'audio_0', "I found you!")
    
    """
    Her carefree attitude itches at you.
    
    WIth your voice raised you ask her.
    """
    
    $ lipsync(Parents, "act3", 'audio_1', "Why the hell are we underwater??")
     
    "Carla tilts her head" 
    
    $ lipsync(Carla, "act3", 'audio_2', "I wanted to do something with you.")
    $ lipsync(Carla, "act3", 'audio_3', "Isn’t this fun?")
    
    $ lipsync(Parents, "act3", 'audio_4', "Excuse me?")
    $ lipsync(Mom, "act3", 'audio_5', "This is anything but fun Carla!")
    $ lipsync(Dad, "act3", 'audio_6', "I just wanted to check on you and-")
    
    """
    Your anxiety stops you when you feel a tugging on your leg again.
    
    A powerful force pulls you back underwater as you fight to stay afloat.
    """
    
    jump kick_at_whatever_is_grabbing_your_leg

label go_back_to_the_living_room:

    """Once in the living room, the clues you’ve gathered repeat the same idea you’ve been scared of admitting for the past few weeks.
    
    Carla is starting to get possessed by something.
    
    Whether it’s a demon or a monster, you’re not sure."""
    
    jump the_urge_to_act_on_this_conclusion_is_stopped_when_carla_enters_the_room

label huh:
    "Carla’s worried look catches your attention but it’s too late."
    
    $ lipsync(Carla, "act3", 'audio_7', "Why do you look sick?")
    $ lipsync(Parents, "act3", 'audio_8', "Nothing.")
    $ lipsync(Dad, "act3", 'audio_9', "I’m sorry, I had a lot to do while you were gone and I still have more to take care of.")
    
    "Carla contemplates for a moment." 
    
    $ lipsync(Carla, "act3", 'audio_10', "Oh!")
    $ lipsync(Carla, "act3", 'audio_11', "I know what we can do.")
    $ lipsync(Carla, "act3", 'audio_12', "Let’s play.")
    $ lipsync(Carla, "act3", 'audio_13', "It’ll take your mind off-")
    
    """
    Her words bring out a primal response from within.
    
    Your response is blurted out before you can think about it.
    """
    
    $ lipsync(Parents, "act3", 'audio_14', "NO")
    
    "Carla pouts at your response as you snap back to reality," 
    
    $ lipsync(Parents, "act3", 'audio_15', "Wait, Carls.")
    
    """
    Your apology falls on deaf ears, and Carla swiftly retreats to her room.
    
    After a few minutes, you decide what to say and head to Carla’s room to apologize.
    """
    
    jump knock_on_her_door

label im_sorry_carls_keep_going:
    """
    Thrilled at your interest in her, Carla continues to speak but her words fade away while you watch her speak.
    
    After a few moments, Carla finishes her story.
    """
    
    $ lipsync(Carla, "act3", 'audio_16', "-then I was like dun dun.")
    $ lipsync(Carla, "act3", 'audio_17', "Dun dun.")
    $ lipsync(Carla, "act3", 'audio_18', "Then I jumped out of the water and tackled them!" )
    
    "Carla stops for a moment and observes the glazed look in your eyes."
    
    $ lipsync(Carla, "act3", 'audio_19', "I think we should play something together, you look like you need it…")

    """
    Before you say anything, Carla’s disturbed look stops you from giving her your initial answer. 
    
    You rationalize your decision internally. Maybe that was a one time thing?
    
    It hasn’t happened at school, it probably won’t happen here again.
    
    These questions raise your confidence and you give Carla your answer.
    """
    
    $ lipsync(Parents, "act3", 'audio_20', "Y-yeah.")
    $ lipsync(Parents, "act3", 'audio_21', "Let’s do that.")
    $ lipsync(Parents, "act3", 'audio_22', "I need a break anyway.")
    
    $ lipsync(Carla, "act3", 'audio_23', "Great!")
    $ lipsync(Carla, "act3", 'audio_24', "I’ll get everything ready.")
     
    "Carla runs for her room and closes the door."
    
    $ lipsync(Parents, "act3", 'audio_25', "Get what ready?")
    
    """
    Minutes pass and you begin to wonder what Carla had to collect to declare the game as "ready". 
    
    The idea is troubling and you head for her room to check on her.
    """
    
    jump knock_on_her_door

label ignore_it_and_keep_going:
    """
    With one hand in front of you, the doorknob reaches your grasp.
    
    You turn the knob, feeling triumphant.
    
    But the door is locked.
    """
    
    jump bash_the_door

label its_too_late_the_monster_swallows_you_whole:
    """
    Enveloped in darkness, you stop trying to hold your breath.
    
    The dread sets in while you choke on the water entering your lungs.
    """
    
    jump knowing_youll_be_back_at_the_start_you_allow_the_cycle_to_continue_anew

label keep_swimming:
    """
    Anticipating the sensation of drowning motivates you to push harder despite the strain on your lungs.
    
    However the door moves out of your reach, on its own accord.
    
    Feeling the monster getting closer, you're tempted to check again.
    """
    
    menu:
        "Check back.":
            jump check_back
        "Ignore it and keep going.":
            jump ignore_it_and_keep_going

label kick_at_whatever_is_grabbing_your_leg:
    """
    
    Blindly, you use your other leg to kick at the entity holding on to your foot.
    
    Once free you manage to catch a glimpse at your captor.
    
    An ugly monster smiles back at you menacingly.
    
    Without hesitation, you exit the cave and try to leave the nightmare.
    """
    
    # (Escape gameplay?)
    
    """
    With the air in your body wearing thin, your salvation is within your grasp.
    
    A door similar to Carla's bedroom door is close enough for you to reach.
    
    You swim faster and faster, not knowing if the nightmare is following behind you.
    """
    
    menu:
        "Look back.":
            jump look_back
        "Keep swimming.":
            jump keep_swimming

label kick_it:
    """
    Multiple satisfying kicks wrests your leg free of the monster's control.
    
    You move ahead, but you can't shake the feeling that something is wrong.
    """
    
    menu:
        "Keep swimming.":
            jump keep_swimming
        "Check back.":
            jump check_back

label knock_on_her_door:
    "No response."
    
    jump you_knock_again

label knowing_youll_be_back_at_the_start_you_allow_the_cycle_to_continue_anew:
    $ lipsync(Carla, "act3", 'audio_26', "Hello??")
    $ lipsync(Carla, "act3", 'audio_27', "Wake up!")
    
    """
    Carla's cries bring you to reality.
    
    On the ground, Carla tugs at your leg. You pull away and immediately stand up.
    """

label look_back:
    """
    To be sure, you check behind you. 
    
    You bitterly regret it as the abomination grabs you by the foot.
    """
    
    jump kick_it

label open_the_door:
    """
    Water rushes out of her room completely filling the room. 
    
    You hold your breath as the current spins you around, disorienting you until you eventually stop. 
    
    Once again, your fears about Carla have manifested again as you find yourself at the bottom of the sea floor.
    """
    
    jump swim_to_the_surface

label open_your_eyes_again:
    """
    Realizing you hadn’t died, you avoid searching for a way out through the surface. 
    
    Your energy is better spent trying to find a way to survive on the seafloor.
    """
    
    # (Here be gameplay for the underwater portion until you find the sea cave)
    
    jump enter_the_underwater_cave

label read_the_notebook:
    """
    The notebook doesn’t have any notes, but drawings."
    
    There are many references to monsters in movies that you’re familiar with.
    
    Amazed with Carla’s artistic talent, you aren’t surprised that she managed to create a world of her own.
    
    However, the monsters that you don’t recognize lead you to believe that Carla may be seeing these monstrosities outside of the movies.
    """
    
    jump continue_your_search_through_carlas_room

label swim_to_the_surface:
    """
    You ascend as fast as possible to the surface but find that the water’s surface never approaches. 
    
    With every stroke, you feel your lungs collapse as you try to hold on. 
    
    Unfortunately, you never reach the surface and your dread sets in as you involuntarily try to breathe again. 
    
    Your eyesight dims and you accept your fate in darkness, choking on the water as you pass out.
    """
    
    jump open_your_eyes_again

label the_urge_to_act_on_this_conclusion_is_stopped_when_carla_enters_the_room:
    "With a shortened breath, Carla exclaims,"
    
    $ lipsync(Carla, "act3", 'audio_28', "I’m home!")
    
    "She begins to bombard you with hugs and tells you about her visit to the pool."
    
    $ lipsync(Carla, "act3", 'audio_29', "You totally missed it.")
    $ lipsync(Carla, "act3", 'audio_30', "I got to the edge of the diving board and everyone was cheering me on.")
    $ lipsync(Parents, "act3", 'audio_31', "Oh really?")
    
    "Your voice obviously shows that you’re distracted, but Carla moves on with her tale."
    
    $ lipsync(Carla, "act3", 'audio_32',"It was pretty scary.")
    $ lipsync(Carla, "act3", 'audio_33', "I kept thinking about that movie with the shark, but it didn’t make sense because…")
    $ lipsync(Carla, "act3", 'audio_34', "Everyone’s already in the pool, and no one was panicking-")
    
    "Carla notices your distracted look."
    
    $ lipsync(Carla, "act3", 'audio_35', "Are you ok?")
    
    #<!--(SECOND MAJOR CHOICE)-->
    
    menu:
        "Huh?":
            jump huh
        "I'm sorry Carls, keep going.":
            jump im_sorry_carls_keep_going

label you_knock_again:
    $ lipsync(Parents, "act3", 'audio_36', "Carls?")
    
    """
    You press your ear to the door for any signs but get nothing in return. 
    
    With a wave of worry, you fear the worst for Carla.
    """
    
    jump open_the_door

label act31:
    """
    With your eyes closed, you continue to shudder at the gnashing teeth sinking into your skin.
    
    Carla’s screaming rings in your ears when you begin to notice that you don’t feel the biting anymore.
    
    You open your eyes.
    
    Carla continues to scream, but you find yourself back in the living room.
    
    Which remains undisturbed since you both entered the house.
    """
    
    $ lipsync(Parents, "act3", 'audio_37', "Huh?")
    
    "confused, you try to get Carla’s attention."
    
    $ lipsync(Parents, "act3", 'audio_38', "Carla.")
    
    "Carla finally stops screaming but tears still stream down her face."
    
    $ lipsync(Parents, "act3", 'audio_39', "What… happened?")
    
    "She sniffles as she answers your question"
    
    $ lipsync(Carla, "act3", 'audio_40', "Y-you s-aid that you didn’t wanna play any more.")
    
    """
    You stand back up and look around the room, the smell of carnival food and its sounds are no longer there.

    Unsure of what transpired you try to relieve yourself of the situation.
    """
    
    $ lipsync(Mom, "act3", "audio_41", "S-sorry Carls, I'm just extremely tired from the trick or treating.")
    $ lipsync(Dad, "act3", "audio_42", "Is it ok if we go to bed now?")

    "Seeing your distressed face, Carla stops crying and tries to comfort you."
    
    $ lipsync(Carla, "act3", "audio_43", "O-oh, ok…")
    
    "she wipes her tears away"
    
    $ lipsync(Dad, "act3", "audio_44", "I’m sorry for yelling at you.")
    
    "With a bewildered look, you look at Carla who’s back to her controlled self and respond"
    
    $ lipsync(Mom, "act3", "audio_45", "N-no more candy Carls.")
    $ lipsync(Mom, "act3", "audio_46", "Please, just get changed out of your costume and  go to bed alright?")
    
    """
    Carla nods and goes back to her room.
    
    When you take a step to your own room to remove the costume, a sharp pain shoots up your leg.
    
    Your eyes widen as you find a bite mark on your leg.
    """
    # <!--Go to bed.-->
    
    """
    Months have passed since the incident on Halloween.
    
    Although Carla has completely forgotten about it, the events have haunted you to this day.
    
    Thankfully, Carla hasn’t had another "episode" since, but the fear has continued to eat at you.
    
    The summer heat beats into your apartment while you finish up some chores.
    
    Carla has been with some family friends at the pool and you decide to seize the moment to catch up on some of the research notes you’ve gathered in the past month.
    """
    
    menu:
        "Go to the office.":
            jump act32a
        "Go to Carla’s Room.":
            jump act32b

label act32a:
    """
    Your desk is littered with papers concerning all manners of paranormal activity, mythical beings, and supernatural occurrences.
    
    A few old news clippings and articles catch your eye.
    """
    
    menu:
        "HELP WANTED: Paranormal Investigator Required":
            jump act32c
        "Family Mourns Child’s Death at the Hands of the Father":
            jump act32d

label act32b:
    """
    Carla’s room always terrifies you, her sweet personality never made sense with her favorite movie genre to you, but you love her regardless.
    
    Your trip here isn’t for nostalgia’s sake, you’re searching for any out of the ordinary clues, so you start looking.
    """
    
    menu:
        "Check under her bed.":
            jump check_under_her_bed
        "Check her bookshelves.":
            jump check_her_bookshelves
        "Check the nightstand.":
            jump check_the_nightstand

label act32c:
    "HELP WANTED: Paranormal Investigator Required"
    
    "Family in need of experienced investigators to look into changing surroundings in the house. Protection needed."
    
    "The story resonates with you"
    
    $ lipsync(Dad, "act3", "audio_47", "Changing surroundings...")
    $ lipsync(Dad, "act3", "audio_48", "I tried to dig deeper into the case and the paranormal investigators insisted that there was a demon or something that was changing everything.")
    
    "you cringe at the thought and move on."
    
    jump act32d

label act32d:
    "The faded news clipping is barely legible, even with the copy made on the computer."
    
    """
    The Washington family mourns the loss of one of their own this morning
    
    Seven year old Dell was found bludgeoned to death with a blunt weapon allegedly by his own father.
    
    When pressed for questions, he denied malicious intent and spouted nonsense about his child having powers out of his control.
    """
    
    """
    You wish that there were more specifics.
    
    but with the mountain of papers on your desk, you feel a sense of comfort knowing you’re not the only one experiencing this.
    """
    
    jump act32b

