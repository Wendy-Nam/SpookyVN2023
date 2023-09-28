## UNDERWATER PART
label bash_the_door:
    with vpunch
    """
    {wave=nunderwater_text}With what little you have left in you, your fist slams on the door, hoping that it'll move.{/wave}
    
    {wave=nunderwater_text}You feel the monster swiftly approaching, but before you can do anything more to the door.{/wave}
    """
    scene black with hpunch
    jump its_too_late_the_monster_swallows_you_whole

label check_back:
    """
    {wave=nunderwater_text}The temptation is too strong and you turn your head.{/wave}
    """
    show bg underwater_creature at jumpAttack
    """
    {wave=nunderwater_text}To your horror, the monster's jaw is agape, ready to swallow you whole.{/wave}
    
    {wave=nunderwater_text}You let out a gasp, not realizing that was the last of your air and you stop swimming.{/wave}
    
    {wave=nunderwater_text}With no energy to carry on, you make one push for the door.{/wave}
    """
    scene black with hpunch
    jump its_too_late_the_monster_swallows_you_whole

label enter_the_underwater_cave:
    stop music fadeout 2.0
    play sound 'audio/Sound/Underwater Scene Sounds/Underwater Cave Dripping Sound.WAV' volume 0.2
    scene bg hand_drowning with fade
    show bg hand_drowning at hand_drowning
    """
    {wave=nunderwater_text}You both breach the surface.{/wave}
    
    {wave=nunderwater_text}Just enough space sits between the water and the roof of the cave, enough for you to keep your head above the water.{/wave}

    {wave=nunderwater_text}You tread the water, wondering if you'll be stuck here forever.{/wave}
    
    {wave=nunderwater_text}As you start to run out of energy to stay afloat, you feel a tugging at your leg.{/wave}
    
    {wave=nunderwater_text}You scream in panic and Carla's head pops out of the water, unfazed.{/wave}
    """
    
    scene bg hand_drowning with fade
    
    show Carla at left
    
    $ lipsync(Carla, "act3", 'audio_0', "I found you!")
    
    """
    Her carefree attitude itches at you.
    
    With your voice raised you ask her.
    """
    
    show Parents overlay_fear eye_serious brow_angry
    
    $ lipsync(Parents, "act3", 'audio_1', "Why the hell are we underwater??", 'mouth_E')
     
    "Carla tilts her head" 
    
    $ lipsync(Carla, "act3", 'audio_2', "I wanted to do something with you.")
    $ lipsync(Carla, "act3", 'audio_3', "Isn't this fun?")
    
    $ lipsync(Parents, "act3", 'audio_4', "Excuse me?", 'mouth_fear')
    hide Parents
    show Dad brow_angry eye_serious mouth_C overlay_fear 
    show Mom brow_angry eye_serious mouth_C overlay_fear
    $ lipsync(Mom, "act3", 'audio_5', "This is anything but fun Carla!", 'mouth_fear')
    $ lipsync(Dad, "act3", 'audio_6', "I just wanted to check on you and-", 'mouth_fear')
    with hpunch
    hide Carla with dissolve
    stop sound fadeout 2.0
    play sound 'audio/Sound/Underwater Scene Sounds/Underwater Sound 2.WAV' volume 0.2
    """
    Your anxiety stops you when you feel a tugging on your leg again.

    A powerful force pulls you back underwater as you fight to stay afloat.
    """
    scene black
    scene bg underwater with dissolve
    stop sound fadeout 2.0
    play music 'audio/Music/A_Trick_of_Mind_Underwater.ogg' volume 0.05 fadein 1.0

    menu:
        "{wave=nunderwater_text}Kick at whatever is grabbing your leg.":
            jump kick_at_whatever_is_grabbing_your_leg

label ignore_it_and_keep_going:
    scene bg underwater_door_closeup with dissolve
    """
    {wave=nunderwater_text}With one hand in front of you, the doorknob reaches your grasp.{/wave}
    
    {wave=nunderwater_text}You turn the knob, feeling triumphant.{/wave}
    
    {wave=nunderwater_text}But the door is locked.{/wave}
    """
    
    jump bash_the_door

label its_too_late_the_monster_swallows_you_whole:
    play sound '<from 1 to 3>audio/Sound/Underwater Scene Sounds/Slimy Slither.wav' volume 3.0
    """
    But It's too late. The monster swallows you whole.
    
    Enveloped in darkness, you stop trying to hold your breath.
    """
    stop music fadeout 2.0
    play sound '<from 5 to 8>audio/Sound/Underwater Scene Sounds/Drowning.mp3' volume 0.5
    """
    The dread sets in while you choke on the water entering your lungs.
    """
    jump knowing_youll_be_back_at_the_start_you_allow_the_cycle_to_continue_anew

label keep_swimming:
    """
    {wave=nunderwater_text}Anticipating the sensation of drowning motivates you to push harder despite the strain on your lungs.{/wave}
    
    {wave=nunderwater_text}However the door moves out of your reach, on its own accord.{/wave}
    
    {wave=nunderwater_text}Feeling the monster getting closer, you're tempted to check again.{/wave}
    """
    menu:
        "{wave=nunderwater_text}Check back.{/wave}":
            jump check_back
        "{wave=nunderwater_text}gnore it and keep going.{/wave}":
            jump ignore_it_and_keep_going

label kick_at_whatever_is_grabbing_your_leg:
    with vpunch
    play sound 'audio/Sound/Underwater Scene Sounds/Underwater Growling.WAV' volume 0.5
    scene bg underwater_creature with dissolve
    
    """    
    {wave=nunderwater_text}Blindly, you use your other leg to kick at the entity holding on to your foot.{/wave}
    """
    with vpunch
    """
    {wave=nunderwater_text}Once free you manage to catch a glimpse at your captor.{/wave}
    
    {wave=nunderwater_text}An ugly monster smiles back at you menacingly.{/wave}
    
    {wave=nunderwater_text}Without hesitation, you exit the cave and try to leave the nightmare.{/wave}
    """
    scene bg underwater_door
    """
    {wave=nunderwater_text}With the air in your body wearing thin, your salvation is within your grasp.{/wave}
    
    {wave=nunderwater_text}A door similar to Carla's bedroom door is close enough for you to reach.{/wave}
    
    {wave=nunderwater_text}You swim faster and faster, not knowing if the nightmare is following behind you.{/wave}
    """
    menu:
        "{wave=nunderwater_text}Look back.{/wave}":
            jump look_back
        "{wave=nunderwater_text}Keep swimming.{/wave}":
            jump keep_swimming

label kick_it:
    with vpunch
    """
    {wave=nunderwater_text}Multiple satisfying kicks wrests your leg free of the monster's control.{/wave}
    
    {wave=nunderwater_text}You move ahead, but you can't shake the feeling that something is wrong.{/wave}
    """
    menu:
        "{wave=nunderwater_text}Keep swimming.{/wave}":
            jump keep_swimming
        "{wave=nunderwater_text}Check back.{/wave}":
            jump check_back

label knock_on_her_door:
    "No response."
    menu:
        "Knock again.":
            jump you_knock_again

label look_back:
    """
    {wave=nunderwater_text}To be sure, you check behind you.{/wave} 
    
    {wave=nunderwater_text}You bitterly regret it as the abomination grabs you by the foot.{/wave}
    """
    menu:
        "{wave=nunderwater_text}Kick it.{/wave}":
            jump kick_it

label open_the_door:
    play target 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 1.0 fadein 1.0
    play weapon 'audio/Sound/Underwater Scene Sounds/Underwater Sound 2.WAV' volume 0.2
    pause 1.0
    play sound 'audio/Sound/Underwater Scene Sounds/Underwater Female Scream.mp3' volume 0.1 fadein 1.0
    play target 'audio/Sound/Underwater Scene Sounds/Underwater Male Scream.mp3' volume 0.1 fadein 2.0
    play music 'audio/Music/A_Trick_of_Mind_Underwater.ogg' volume 0.05 fadein 3.0
    
    scene bg underwater with pixellate
    # show Parents mouth_fear overlay_fear eye_default brow_surprised
    """
    {wave=nunderwater_text}Water rushes out of her room completely filling the living room.{/wave}
    
    {wave=nunderwater_text}You hold your breath as the current spins you around, disorienting you until you both eventually stop.{/wave}
    
    {wave=nunderwater_text}Once again, your fears about Carla have manifested as you find yourself at the bottom of a sea floor.{/wave}
    
    {wave=nunderwater_text}Desperate for air, you swim upwards.{/wave}
    """
    # show Parents mouth_sad overlay_fear eye_serious
    jump swim_to_the_surface

label open_your_eyes_again:
    """
    {wave=nunderwater_text}Realizing you hadn't died, you avoid searching for a way out through the surface.{/wave}
    
    {wave=nunderwater_text}Your energy is better spent trying to find a way to survive on the seafloor.{/wave}
    """
    
    # (Here be gameplay for the underwater portion until you find the sea cave)
    scene bg underwater_game
    call screen game_rules_minigame2
    """
    Game Start
    """
    window hide
    play AirTank 'audio/Sound/Underwater Scene Sounds/Air Tank Hiss.WAV' fadein 1.0 volume 0.05
    $ minigame2 = UnderwaterGame()
    $ minigame2.run()
    scene black
    if minigame2.status.survived == False:  
        return # Ending : Drowned...
    if minigame2.status.air_hp > minigame2.status.air_hp:
        $ Practically_Jaws.grant()
    stop AirTank fadeout 1.0
    """
    {wave=nunderwater_text}After aimlessly swimming around, an underwater cave catches your eye.{/wave}
    """
    play sound 'audio/Sound/Underwater Scene Sounds/Treading Water Sound.WAV' volume 0.2
    """
    {wave=nunderwater_text}Hoping to find a large enough air pocket to rest and breathe, you swim into it.{/wave}

    {wave=nunderwater_text}The crevice is smaller than anticipated, but it's enough for you to pull yourself through.{/wave}

    {wave=nunderwater_text}The air provided by the air bubbles gives you enough energy to find an open area.{/wave}

    {wave=nunderwater_text}Above you is a surface you can finally reach.{/wave}
    """
    menu:
        "{wave=nunderwater_text}Enter the underwater cave.{/wave}":
            jump enter_the_underwater_cave

label swim_to_the_surface:

    """
    {wave=nunderwater_text}You ascend as fast as possible to the surface but find that the water's surface never approaches.{/wave}
    
    {wave=nunderwater_text}With every stroke, you feel your lungs collapse as you try to hold on.{/wave}
    
    {wave=nunderwater_text}Unfortunately, you never reach the surface and your dread sets in as you involuntarily try to breathe again.{/wave}
    
    {wave=nunderwater_text}Your eyesight dims and you accept your fate in darkness, choking on the water as you pass out.{/wave}
    """
    menu:
        '{wave=nunderwater_text}Open your eyes again.{/wave}':
            jump open_your_eyes_again

## HOUSE : BEFORE UNDERWATER PART
label the_urge_to_act_on_this_conclusion_is_stopped_when_carla_enters_the_room:
    "The urge to act on this conclusion is stopped when Carla enters the room."
    
    play sound 'audio/Sound/House Scene Sounds/Door Open and Close Intro.WAV' fadein 1.0

    show Carla at left
    $ lipsync(Carla, "act3", 'audio_28', "I'm home!")
    
    "She begins to bombard you with hugs and tells you about her visit to the pool."
    
    $ lipsync(Carla, "act3", 'audio_29', "You totally missed it.")
    $ lipsync(Carla, "act3", 'audio_30', "I got to the edge of the diving board and everyone was cheering me on.")
    
    $ lipsync(Parents, "act3", 'audio_31', "Oh really?")
    
    "Your voices are obviously distracted, but Carla moves on with her tale."
    
    $ lipsync(Carla, "act3", 'audio_32',"It was pretty scary.")
    $ lipsync(Carla, "act3", 'audio_33', "I kept thinking about that movie with the shark, but it didn't make sense because...")
    $ lipsync(Carla, "act3", 'audio_34', "Everyone's already in the pool, and no one was panicking-")
    
    "Carla notices your preoccupied look."
    
    show Parents mouth_G eye_default brow_surprised
    show parents_fear_overlay_mask at center:
        alpha 0.5
    show Carla brow_sad eye_default mouth_sad
    
    $ lipsync(Carla, "act3", 'audio_35', "Are you two ok?")
    
    #<!--(SECOND MAJOR CHOICE)-->
    menu:
        "Huh?":
            $ ending_condition -= 10
            jump huh
        "I'm sorry Carls, keep going.":
            $ ending_condition += 10
            jump im_sorry_carls_keep_going

label you_knock_again:
    $ lipsync(Parents, "act3", 'audio_36', "Carls?", 'mouth_sad')
    
    """
    You both press your ears to the door, bothered by the lack of acknowledgement.

    You search for any signs or sounds from the other side but get nothing in return. 
    
    With a wave of worry, you fear the worst for Carla.
    """
    stop music fadeout 1.0
    show Parents mouth_fear  eye_default brow_surprised
    menu:
        "Open the door":
            jump open_the_door

## HOUSE : SEARCH PART
label act31:
    """
    With your eyes closed, you continue to shudder at the gnashing teeth sinking into your skin.
    
    Carla's screaming rings in your ears when you begin to notice that you don't feel the biting anymore.
    
    You open your eyes.
    """
    stop music fadeout 2.0
    stop weapon fadeout 2.0
    stop target fadeout 2.0
    stop sound fadeout 2.0
    
    scene bg livingroom_night
    show Carla eye_crying brow_angry2 mouth_angry2 overlay_fear at left
    show blink

    camera:
        subpixel True alpha 1.0 
        parallel:
            yoffset -900
            linear 2.22 yoffset -600 
        parallel:
            zoom 1.85 blur 0.0 
            linear 2.07 zoom 2.0 blur 0.2 
            linear 2.15 zoom 1.5 blur 0.0 
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 2.07 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.2)*HueMatrix(0.0) 
            linear 2.08 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.2)*HueMatrix(0.0) 
            linear 2.07 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(2.5)
    camera:
        yoffset -300 zoom 1.5 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    
    camera
    """
    Carla continues to scream, but you find yourself back in the living room.
    
    Which remains undisturbed since you all entered the house.
    """
    show Parents mouth_fear overlay_fear eye_default brow_surprised
    
    $ lipsync(Parents, "act3", 'audio_37', "Huh?", 'mouth_fear')
    
    "Confused, you try to get Carla's attention."
    
    $ lipsync(Parents, "act3", 'audio_38', "Carla.", 'mouth_fear')
    hide Carla
    show Carla brow_sad eye_crying mouth_G at left
    "Carla finally stops screaming but tears still stream down her face."
    
    $ lipsync(Parents, "act3", 'audio_39', "What... happened?", 'mouth_fear')
    
    "She sniffles as she answers your question"
    
    $ lipsync(Carla, "act3", 'audio_40', "Y-you s-aid that you didn't wanna play any more.", 'mouth_sad')
    
    """
    You stand back up and look around the room, the smell of carnival food and its sounds are no longer there.

    Unsure of what transpired you try to relieve yourself of the situation.
    """
    hide Parents
    show Dad brow_sad eye_serious mouth_sad overlay_fear
    show Mom brow_sad eye_serious mouth_sad overlay_fear
    $ lipsync(Mom, "act3", "audio_41", "S-sorry Carls, I'm just extremely tired from the trick or treating.")
    $ lipsync(Dad, "act3", "audio_42", "Is it ok if we go to bed now?")

    "Seeing your distressed face, Carla stops crying and tries to comfort you."
    
    show Carla brow_sad eye_default mouth_sad
    $ lipsync(Carla, "act3", "audio_43", "O-oh, ok...", 'mouth_sad')
    
    "She wipes her tears away"
    hide Dad
    hide Mom
    show Dad brow_sad eye_default mouth_sad
    show Mom brow_sad eye_default mouth_sad
    show parents_fear_overlay_mask
    $ lipsync(Dad, "act3", "audio_44", "We're sorry for yelling at you.")
    
    "With a bewildered look, you look at Carla who's back to her controlled self."
    
    $ lipsync(Mom, "act3", "audio_45", "N-no more candy Carls.", 'mouth_fear')
    $ lipsync(Mom, "act3", "audio_46", "Please, just get changed out of your costume and  go to bed alright?")
    
    hide parents_fear_overlay_mask with dissolve
    
    """
    Carla nods and goes back to her room.
    """
    show Carla at carla_walk
    hide Dad
    hide Mom
    show Parents at walking
    """
    When you take a step to your own room to remove the costume, a sharp pain shoots up dad's leg.
    """
    show Parents mouth_fear overlay_fear eye_default brow_surprised with vpunch
    play sound 'audio/Sound/Scraping Gong.wav' fadein 1.0 volume 0.1
    """
    Shocked eyes widen when they discover a bite mark on his leg.
    """
    
    scene black
    
    # <!--Go to bed.-->
    """
    Months have passed since the incident on Halloween.

    Although Carla doesn't think about it, the events have haunted you both to this day.
    
    Thankfully, Carla hasn't had another episode since, but the fear persisted.

    """
    
    scene bg livingroom_sunset with dissolve
    play music 'audio/Music/A_Trick_of_Mind_House.ogg' fadein 2.0 volume 0.15
    
    """
    The summer heat beats into the apartment while some chores are finished up.
    
    Carla is with some family friends at the pool and you both decide to seize the moment to catch up on some of the research notes you've gathered in the past months
    """
    window auto hide
    
    menu:
        "Go to the office.":
            jump act32a
        "Go to Carla's Room.":
            jump act32b

label act32a:
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 0.5
    scene bg office_sunset with pushleft
    
    window auto hide
    camera:
        subpixel True 
        offset (-567, -756) zoom 1.81 
        linear 0.63 offset (-1404, -1134) zoom 2.09 
    with Pause(0.73)
    camera:
        offset (-1404, -1134) zoom 2.09 
    window auto show

    """
    Your desk is littered with papers concerning all manners of paranormal activity, mythical beings, and supernatural occurrences.
    
    A few old news clippings and articles catch your eye.
    """
    menu:
        "HELP WANTED: Paranormal Investigator Required":
            jump act32c
        "Family Mourns Child's Death at the Hands of the Father":
            jump act32d
            
label act32b:
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 0.5
    scene bg bedroom_day with pushright
    """
    Carla's room always terrifies you, her sweet personality never made sense with her favorite movie genre to you, but you love her regardless.

    Your trip here isn't for nostalgia's sake, you're searching for any out of the ordinary clues, so you start looking.
    """
    menu:
        "Check under her bed.":
            jump check_under_her_bed
        "Check her bookshelves.":
            jump check_her_bookshelves
        "Check the nightstand.":
            jump check_the_nightstand
        "Go to the office":
            jump act32a

label act32c:
    camera
    play sound 'audio/Sound/House Scene Sounds/Paper Rustling.wav' volume 0.5 fadein 2.0
    "HELP WANTED: Paranormal Investigator Required"
    
    "Family in need of experienced investigators to look into changing surroundings in the house. Protection needed."
    
    "The story resonates with you"
    
    show Dad brow_angry eye_serious
    
    $ lipsync(Dad, "act3", "audio_47", "Changing surroundings...", 'mouth_fear')
    $ lipsync(Dad, "act3", "audio_48", "I tried to dig deeper into the case and the paranormal investigators insisted that there was a demon or something that was changing everything.", 'mouth_sad')
    
    "you cringe at the thought and move on."
    
    jump act32d

label act32d:
    camera
    scene bg office_day with dissolve
    "The faded news clipping is barely legible, even with the copy made on the computer."
    
    """
    The Washington family mourns the loss of one of their own this morning
    
    Seven year old Dell was found bludgeoned to death with a blunt weapon allegedly by his own father.
    
    When pressed for questions, he denied malicious intent and spouted nonsense about his child having powers out of his control.
    """
    
    """
    You wish that there were more specifics.
    
    but with the mountain of papers on your desk, you feel a sense of comfort knowing you're not the only one experiencing this.
    """
    
    jump act32b

default searched = {'bed':False, 'bookshelves':False, 'nightstand':False}

label continue_your_search_through_carlas_room:
    camera
    $ all_searched = all(searched.values())
    if all_searched == False:
        menu:
            "Check under her bed." if searched['bed'] == False:
                jump check_under_her_bed
            "Check her bookshelves."  if searched['bookshelves'] == False:
                jump check_her_bookshelves
            "Check the nightstand." if searched['nightstand'] == False:
                jump check_the_nightstand
    else:
        scene bg bedroom_night with dissolve
        # Once the player selects all of the options once (They don't have to look at the notebook), they can move on.
        menu:
            "Go back to the living room.":
                jump go_back_to_the_living_room
    
label check_her_bookshelves:
    $ searched['bookshelves'] = True
    
    window auto hide
    camera:
        subpixel True additive 0.0 
        offset (0, 0) zoom 1.0 blur 1.99 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 1.17 offset (-243, -756) zoom 2.37 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.2)*SaturationMatrix(0.79)*BrightnessMatrix(-0.03)*HueMatrix(0.0) 
    with Pause(1.27)
    camera:
        offset (-243, -756) zoom 2.37 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.2)*SaturationMatrix(0.79)*BrightnessMatrix(-0.03)*HueMatrix(0.0) 
    window auto show

    """
    The bookshelves are littered with horror movie merchandise that you forgot purchasing for her.

    A suspicious notebook catches your eye.
    """
    menu:
        "Read the notebook.":
            jump read_the_notebook
        "Continue your search through Carla's room.":
            jump continue_your_search_through_carlas_room

label check_the_nightstand:
    $ searched['nightstand'] = True
    
    window auto hide
    camera:
        subpixel True 
        offset (0, 0) zoom 1.0 blur 3.55 
        linear 0.77 offset (-828, 0) zoom 2.13 blur 0.0 
    with Pause(0.87)
    camera:
        offset (-828, 0) zoom 2.13 blur 0.0 
    window auto show
    
    "Carla's nightstand has nothing of interest."
    
    jump continue_your_search_through_carlas_room

label check_under_her_bed:
    $ searched['bed'] = True
    
    window auto hide
    camera:
        subpixel True matrixanchor (0.5, 0.5) 
        offset (0, 0) zoom 1.0 additive 0.0 blur 4.44 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.91 offset (-1026, -1260) zoom 2.2 additive 0.12 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.87)*BrightnessMatrix(-0.07)*HueMatrix(0.0) 
    with Pause(1.01)
    camera:
        offset (-1026, -1260) zoom 2.2 additive 0.12 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.87)*BrightnessMatrix(-0.07)*HueMatrix(0.0) 
    window auto show

    """
    Under her bed are remnants of her old toys and books before she found her love for horror.

    Colorful books and soft duck plushies remind you of the carnival incident, compelling you to pull away from the bed.

    Oddly enough, you're happy that Carla is in the phase she's in now.
    """
    
    jump continue_your_search_through_carlas_room


label read_the_notebook:
    play sound 'audio/Sound/House Scene Sounds/Notebook Page Pick Up.wav' volume 0.7 fadein 1.0
    
    """
    The notebook doesn't have any notes, but drawings.

    There are many references to monsters in movies that you're familiar with.

    Amazed with Carla's artistic talent, you aren't surprised that she managed to create a world of her own before.

    However, there are monsters that you don't recognize.
    """
    
    jump continue_your_search_through_carlas_room

label go_back_to_the_living_room:
    scene bg livingroom_night with dissolve
    """
    Once in the living room, the clues repeat the same idea that's been circulating for the past few weeks.
    
    Carla is getting possessed by something.
    
    Whether it's a demon or a monster, it's not clear.
    
    Yet.
    """
    
    jump the_urge_to_act_on_this_conclusion_is_stopped_when_carla_enters_the_room

label huh:
    "Carla's worried look catches your attention but it's too late."

    $ lipsync(Carla, "act3", 'audio_7', "Why do you look sick?")
    
    $ lipsync(Parents, "act3", 'audio_8', "Nothing.")
    
    hide Parents
    hide parents_fear_overlay_mask
    show Dad brow_sad eye_default mouth_sad
    show Mom brow_sad eye_default mouth_sad
    
    $ lipsync(Dad, "act3", 'audio_9', "I'm sorry, I had a lot to do while you were gone and I still have more to take care of.")
    
    "Carla contemplates for a moment." 
    
    show Carla brow_surprised eye_default mouth_G
    
    $ lipsync(Carla, "act3", 'audio_10', "Oh!")
    $ lipsync(Carla, "act3", 'audio_11', "I know what we can do.")
    $ lipsync(Carla, "act3", 'audio_12', "Let's play.")
    $ lipsync(Carla, "act3", 'audio_13', "It'll take your mind off-")
    
    """
    Her words bring out a primal response from within.
    
    Your response is blurted out before you can think about it.
    """
    hide Dad
    hide Mom
    show Parents mouth_fear overlay_fear eye_default brow_surprised    
    $ lipsync(Parents, "act3", 'audio_14', "NO", 'mouth_fear')
    
    # TODO : Add expression
    """
    Carla is startled by your anguished look.

    You snap back to reality finding that your face is nearly two inches from hers.

    She steps back from you with fear in her eyes.
    """
    
    # TODO : add some visual effects and expressions
    
    $ lipsync(Carla, "act3", "audio_001", "Ok...", 'mouth_sad')
    
    "With her head down, Carla quickly retreats to her room."
    
    hide Parents
    show Parents eye_default brow_surprised
    
    $ lipsync(Parents, "act3", 'audio_002', "Wait, Carls.", 'mouth_fear')
    $ lipsync(Parents, "act3", 'audio_003', "I'm really sorry!", 'mouth_fear')
    hide Carla with moveoutleft
    show Parents mouth_sad  eye_serious brow_sad
    """
    Your apology falls on deaf ears, and Carla swiftly retreats to her room.

    After a few minutes, you decide what to say and head to Carla's room.
    """
    menu:
        "Knock on her door.":
            jump knock_on_her_door

label im_sorry_carls_keep_going:
    """
    Thrilled at the interest in her, Carla continues to speak but her words fade away.
    
    A demon? She can't be.
    
    Carla may be a bit mischievous, but she wouldn't hurt anyone.
    
    Right?
    
    The pain in Dad's leg has subsided and the scar is disappeared, but it feels off.
    
    Carla's recounts her time at the pool, but her words continue to pass by.
    
    After a few moments, Carla finishes her story.
    """
    
    $ lipsync(Carla, "act3", 'audio_16', "-then I was like dun dun.")
    $ lipsync(Carla, "act3", 'audio_17', "Dun dun.")
    $ lipsync(Carla, "act3", 'audio_18', "Then I jumped out of the water and tackled them!" )
    
    "Carla stops for a moment and observes the glazed look in your eyes."
    
    $ lipsync(Carla, "act3", 'audio_19', "I think we should play something together, you look like you need it...")
    
    show Parents mouth_fear  eye_default brow_surprised
    
    """
    Before you say anything, Carla's disturbed look stops you from giving her your answer. 
    
    You look at each other as you rationalize your decision internally. Maybe that was a one time thing?
    
    It hasn't happened at school, it probably won't happen here again.
    
    These questions raise your confidence as you look at each other and give Carla your answer.
    """
    
    $ lipsync(Parents, "act3", 'audio_20', "Y-yeah.")
    $ lipsync(Parents, "act3", 'audio_21', "Let's do that.")
    $ lipsync(Parents, "act3", 'audio_22', "I need a break anyway.")
    
    $ lipsync(Carla, "act3", 'audio_23', "Great!")
    $ lipsync(Carla, "act3", 'audio_24', "I'll get everything ready.")
     
    hide Carla with moveoutleft
    play sound 'audio/Sound/House Scene Sounds/Door Open and Close Intro.WAV' fadein 1.0
    
    "Carla runs for her room and closes the door."
    
    hide parents_fear_overlay_mask with dissolve
    show Parents mouth_fear eye_default brow_surprised
    $ lipsync(Parents, "act3", 'audio_25', "Get what ready?", 'mouth_sad')
    
    """
    Minutes pass and you begin to wonder what Carla had to collect to declare the game as //ready//. 

    You're troubled by the idea and head for her room to check on her.
    """
    menu:
        "Knock on her door.":
            jump knock_on_her_door
