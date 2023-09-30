
label carls_of_course_i_want_to_spend_time_with_you:
    hide Parents
    show Dad brow_sad eye_crying mouth_sad
    show Mom brow_sad eye_crying mouth_sad
    
    $ lipsync(Mom, "act4", 'audio_0', "We're sorry, I don't know why I passed out earlier.")
    
    hide Carla
    show Carla brow_sad eye_crying mouth_sad at left
    $ lipsync(Carla, "act4", 'audio_2', "That's what I was saying...", 'mouth_sad')
    # TODO : add expressions
    $ lipsync(Carla, "act4", 'audio_3', "You need to take your mind off of whatever's bothering you.", 'mouth_fear')
    $ lipsync(Carla, "act4", 'audio_1', "I thought playing would be the thing...", 'mouth_sad')
    
    "You look at Carla, whose concern for your wellbeing forces your emotions to swell through you."
        
    $ lipsync(Mom, "act4", 'audio_4', "You're right missy.")
    $ lipsync(Dad, "act4", 'audio_5', "But we can't play right now, we're just exhausted.")
    
    show Carla brow_sad eye_default mouth_G
    $ lipsync(Carla, "act4", 'audio_7', "Oh... ok...", 'mouth_sad')
    
    $ lipsync(Mom, "act4", 'audio_8', "Just stay here and play on your own for a bit alright?")
    
    $ lipsync(Carla, "act4", 'audio_6', "That's it?", 'mouth_E')
    
    "Cautiously, you get up to leave the room."
    
    $ lipsync(Carla, "act4", 'audio_9', "I love you guys.")
    
    "Ashamed, you look at each other and respond."
    
    hide Mom
    hide Dad
    show Parents brow_sad eye_crying mouth_sad
    
    $ lipsync(Parents, "act4", 'audio_10', "We love you too Carls.")
    
    show Parents eye_default at parents_walk
    
    show Carla brow_sad mouth_H overlay_fear
    
    camera:
        subpixel True crop_relative True 
        zoom 1.0 crop (0.0, 0.0, 1.0, 1.0) 
        linear 0.19 zoom 1.22 crop (0.0, 0.05, 1.0, 1.0) 
        linear 0.19 zoom 1.32 crop (0.00, 0.21, 1.0, 1.0) 
        linear 0.17 zoom 1.6 crop (0.00, 0.33, 1.0, 1.0) 
    with Pause(0.65)
    camera:
        zoom 1.6 crop (0.00, 0.33, 1.0, 1.0) 

    "Carla's kind smile slowly makes a sinsister transition as you walk out."
    
    camera
        
    scene black with dissolve
    
    "you exit the room unable to cope with what you're about to do."
    
    jump you_exit_the_room_unable_to_cope_with_what_youre_about_to_do

label after_defeating_the_monster_adults_ending:
    """
    The monster collapses on the floor, unmoving.
    """
    
    scene bg courtyard
    show Parents mouth_sad overlay_blood eye_closed brow_angry at courtyard_tint_parents
    
    """
    With a heavy sigh, you drop the bat and look around for Carla.
    """
    play music 'audio/Music/A_Trick_of_Mind_End_Game.ogg' volume 0.3 fadein 3.0
    show Parents eye_default
    
    $ lipsync(Parents, "act4", 'audio_11', "Carla?", 'mouth_fear')
    scene black
    show bg courtyard:
        linear 1.0 alpha 0.0
    "The defeated monster begins to fade as well as your surroundings."

    show Parents brow_surprised at corridor_tint
    $ lipsync(Parents, "act4", 'audio_12', "Carls!", 'mouth_fear')
    show Parents overlay_fear
    $ lipsync(Parents, "act4", 'audio_13', "You can come out now!", 'mouth_fear')
    scene black with dissolve
    show bg cell_prison with fade:
        linear 3.0 additive 0.0 blur 1.46 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.08)*SaturationMatrix(1.09)*BrightnessMatrix(0.33)*HueMatrix(0.0) 

    """
    You run through the fading prison, searching for any sign of Carla.
    
    Back in her cell, you find the page you left on the floor.
    """
    camera:
        subpixel True 
        offset (0, 0) zoom 1.0 
        linear 0.87 offset (-1872, -1692) zoom 2.62 
    with Pause(0.97)
    camera:
        offset (-1872, -1692) zoom 2.62 

    menu:
        "Pick it up.":
            jump pick_it_up

label after_defeating_the_monster_childs_ending:
    """
    The monster drops to the floor writhing in pain before succumbing to its injuries.
    """
    show Parents mouth_fear eye_default brow_surprised overlay_blood at courtyard_tint_parents
    play music 'audio/Music/A_Trick_of_Mind_End_Game.ogg' volume 0.3 fadein 3.0
    """
    It immediately fades from existence and Carla runs towards you.
    """
    show Carla brow_angry2 eye_crying mouth_angry2 overlay_dirt overlay_fear overlay_blood with moveinleft:
        courtyard_tint_carla
    """
    You embrace each other tightly.
    """
    show Parents mouth_fear overlay_fear eye_crying brow_surprised at courtyard_tint_parents
    $ lipsync(Parents, "act4", 'audio_14', "Are you hurt?", 'mouth_fear')
    hide Parents
    show Dad mouth_sad eye_crying brow_sad overlay_blood at courtyard_tint_parents
    show Mom mouth_fear overlay_fear eye_crying brow_angry overlay_blood at courtyard_tint_parents
    
    $ lipsync(Mom, "act4", 'audio_15', "My god that was terrifying.", 'mouth_sad')
    
    "Carla's face remains buried into your chest as you check on her further."
    
    $ lipsync(Dad, "act4", 'audio_16', "It's ok, i-it's over...")
    
    hide Dad
    hide Mom
    show Parents mouth_fear overlay_fear eye_default brow_default overlay_blood at courtyard_tint_parents 
    show Carla brow_default eye_default mouth_B
    $ lipsync(Parents, "act4", 'audio_17', "Carls?", 'mouth_fear')
    
    show Carla mouth_C
    """
    Carla looks at you and smiles, but the smile begins to contort her face.
    """
    play sound 'audio/Sound/Carla_giggling.mp3' fadein 2.0 volume 2.0
    show Carla mouth_H at laugh
    hide Carla with fade
    play sound 'audio/Sound/Carla_laugh.mp3' fadein 2.0 volume 2.0
    """
    She laughs as you back away, watching her being fade away as well.
    """
    
    $ lipsync(Parents, "act4", 'audio_18', "No. Carls...", 'mouth_fear')
    show Parents eye_crying brow_surprised
    $ lipsync(Parents, "act4", 'audio_19', "Carls!", 'mouth_fear')
    
    """
    Your anxiety mounts and you begin to feel an increasing pressure on your throat.
    """
    show Parents brow_sad mouth_sad
    """
    Unable to speak you feel paralyzed, only now noticing the set of hands that have wrapped themselves around your neck.
    """
    with vpunch
    show Parents eye_default brow_surprised mouth_fear
    """
    The force increases gradually while you try to flail yourself free.
    """
    scene black with dissolve
    menu:
        "Keep fighting.":
            jump keep_fighting

label attack_the_monster:
    $ Swing_Now_Ask_Later.grant()
    show Parents mouth_fear overlay_fear eye_default brow_angry at courtyard_tint_parents
    play weapon 'audio/Sound/Prison Scene Sounds/Bat Impact.WAV' volume 2.0
    """
    You clench your bat and raise it above your head and swing at your attacker.
    """
    play sound 'audio/Sound/Prison Scene Sounds/Monster Gets Hit.wav' volume 3.5 fadein 0.5
    play target 'audio/Sound/Prison Scene Sounds/Monster Snarl.WAV' volume 1.5 fadein 0.5
    """
    It cries out in pain as Carla maintains her focus on you.
    """
    
    $ lipsync(Parents, "act4", 'audio_20', "Leave her alone!", 'mouth_fear')
    
    # -Player does the bat and monster minigame-
    window hide
    scene bg minigame3
    call screen game_rules_minigame3
    $ minigame3 = TurnBasedGame()
    $ minigame3.run()
    # show screen trpg_game_board(game, game.monster, game.player)
    # Handle game over and other outcomes here
    if minigame3.player_win:
        "You have defeated the monster."
    else:
        "You have been defeated."
        return
    if ending_condition < 30:
        jump after_defeating_the_monster_adults_ending
    else:
        jump after_defeating_the_monster_childs_ending

label begin_unlocking_her_door:
    hide Carla with dissolve
    stop music fadeout 3.0
    show Parents mouth_sad eye_serious brow_default
    with sshake3
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 1.0
    """
    You reach up for the first latch and unhook it.
    """
    with sshake3
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 1.5
    """
    The second latch is then undone.
    """
    with sshake3
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 2.0
    """
    The third.
    """
    with sshake3
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 3.0
    """
    Finally, the fourth.
    """
    show Parents mouth_sad eye_serious overlay_fear
    """
    Gently, you turn the knob, bracing yourself for any force to make their way out of Carlas room.
    
    But it never comes. 
    """
    scene bg corridor_empty with fade
    play music 'audio/Music/A_Trick_of_Mind_Prison.ogg' fadein 3.0 volume 0.05
    show Parents mouth_sad eye_default brow_surprised overlay_fear at corridor_tint

    play sound 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 0.8
    """
    Once the door opens fully, to your horror, you find yourself peering into a dark hallway.
    
    You curse to yourself before throwing your voice into the blackness.
    """
    show Parents mouth_fear eye_default brow_surprised
    $ lipsync(Parents, "act4", 'audio_21', "Carla?", 'mouth_fear')
    
    "No response."
    
    $ lipsync(Parents, "act4", 'audio_22', "Carls? We made a deal!", 'mouth_fear')
    
    hide parents_fear_overlay_mask with dissolve
    menu:
        "Shut the door and lock it.":
            jump shut_the_door_and_lock_it
        "Find Carla.":
            jump find_carla

label check_her_shelves:
    $ searched_cells['shelves'] = True
    
    camera:
        subpixel True 
        offset (0, 0) zoom 1.0 
        linear 0.46 offset (-1278, -972) zoom 3.21 
    with Pause(0.56)
    camera:
        offset (-1278, -972) zoom 3.21 

    """
    Carla's shelves are full of small straw dolls...
    
    At least what used to be dolls, their heads have been torn off and a few of them are beyond repair.
    
    One page from her notebook has been torn out.
    """
    menu:
        "Check the page.":
            jump check_the_page
        "Check the rest of the cell.":
            jump check_the_rest_of_the_cell

label check_the_bed:
    $ searched_cells['bed'] = True
    camera:
        subpixel True 
        offset (0, 0) zoom 1.0 
        linear 0.33 offset (-1845, -855) zoom 2.29 
    with Pause(0.43)
    camera:
        offset (-1845, -855) zoom 2.29 
    """
    A makeshift bed lies on the floor of the cell, barely large enough for Carla to sleep on.
    
    You rummage through the sheets for any clue but find nothing.
    """
    
    jump check_the_rest_of_the_cell

label check_the_bucket:
    $ searched_cells['bucket'] = True
    camera:
        subpixel True 
        offset (0, 0) zoom 1.0 
        linear 0.54 offset (-63, -1809) zoom 2.88 
    with Pause(0.64)
    camera:
        offset (-63, -1809) zoom 2.88 
    play sound 'audio/Sound/Prison Scene Sounds/Bucket Check.wav' volume 5.0
    """
    The source of the foul odor coming from the cell is obviously coming from the bucket.
    
    Nervously, you check its contents.
    
    Nothing out of the ordinary, but its mere presence fills you with dread and guilt.
    """
    
    jump check_the_rest_of_the_cell

label check_the_page:
    play sound 'audio/Sound/Prison Scene Sounds/Page Pick Up.wav' volume 5.0
    """
    You pick up the page and carefully make out the image in the dark.
    
    A poorly drawn image of what looks like a monster and Carla are holding hands.
    
    The page falls from your hand, unable to live with the idea that Carla and the monster are now one.
    """
    
    jump check_the_rest_of_the_cell

default searched_cells = {'bed':False, 'bucket':False, 'shelves':False}

label check_the_rest_of_the_cell:
    camera
    "The stench of the cell singes your nose."
    $ all_searched = all(searched_cells.values())
    if all_searched == False:
        menu:
            "Check the bed." if searched_cells['bed'] == False:
                jump check_the_bed
            "Check the bucket." if searched_cells['bucket'] == False:
                jump check_the_bucket
            "Check her shelves." if searched_cells['shelves'] == False:
                jump check_her_shelves    
    # After players investigate the whole of the room, they will move to the next section below:
    else:
        menu:
            "Finish checking the cell.":
                jump finish_checking_the_cell

label explore_the_rest_of_the_prison:
    scene bg corridor_empty with dissolve
    """
    The prison hallways are as dirty as Carla's cell. It's tight feeling along with the darkness chokes you.

    One by one you pass by another empty cell, wondering what could've been held behind the bars.
    
    You recall that Carla has manifested and drawn several monsters. Could they be what was hidden here? 
    
    The thought stops you in your tracks.
    
    No. You can't allow for that attitude from stopping your search for Carla.
    """
    scene bg double_doors with fade
    """
    The end of the hallway leads to a set of double doors.
    """
    
    jump open_the_doors

label find_carla:
    """
    Inside, you are begging for Carla to come out of the dark.
    
    However you know that won't be the case.
    
    You cease calling out to Carla and decide, the next best step is to traverse the darkness to find her.
    """
    show Parents mouth_sad eye_serious brow_angry
    """
    You grab the bat by the door and tightly grip it, ready to attack anything coming your way.
    """
    play target 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 2.0
    with vpunch
    """
    With a controlled breath, you step in and shut the door behind you.
    """  
    jump inside_the_hallway

label finish_checking_the_cell:
    """
    Unsurprisingly, there is nothing in the cell that can conclusively tell you where Carla is.
    """
    show Parents mouth_fear eye_default brow_surprised at prison_tint
    """
    You contemplate where she could be but a thought jumps into your mind.
    
    Carla could be running towards the exit.
    """
    show Parents mouth_sad eye_serious brow_sad
    """
    But would she?
    
    You shudder at the idea and hold on to the hope that she may still be in here... Maybe.
    """
    
    # <!--(FOURTH MAJOR CHOICE)-->
    menu:
        "Head back to the bedroom door.":
            $ ending_condition -= 10
            jump head_back_to_the_bedroom_door
        "Explore the rest of the prison.":
            $ ending_condition += 10
            jump explore_the_rest_of_the_prison

label get_closer:
    scene bg courtyard_creature_carla at step_in
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 4.0 fadein 0.2
    pause 0.5
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 4.0 fadein 0.2
    pause 0.5
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 4.0 fadein 0.2
    pause 0.5
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 4.0 fadein 0.2
    pause 0.5
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 4.0 fadein 0.2
    pause 0.5
    "Both the monster and Carla sit still, nearly oblivious to your presence."
    stop sound fadeout 2.0
    show Parents mouth_fear overlay_fear brow_surprised eye_default at courtyard_tint_parents
    
    $ lipsync(Parents, "act4", 'audio_23', "C-Carla?", 'mouth_fear')
    
    "Carlas face remains fixed to the floor."
    
    show Carla brow_sad eye_default mouth_X overlay_dirt at courtyard_tint_carla
    
    $ lipsync(Carla, "act4", 'audio_24', "You came to play?", 'mouth_X')
    
    show Parents mouth_sad overlay_fear eye_serious brow_sad
    
    $ lipsync(Parents, "act4", 'audio_25', ".... No.")
    
    show Carla brow_angry
    
    $ lipsync(Carla, "act4", 'audio_26', "Why did you come?", 'mouth_G')
    
    $ lipsync(Parents, "act4", 'audio_27', "We came because we was worried about you Carla.", 'mouth_sad')
    
    show Carla brow_angry2 eye_default mouth_angry overlay_dirt
    
    $ lipsync(Carla, "act4", 'audio_28', "You're not worried about me.", 'mouth_angry')
    
    jump the_monster_leaves_carlas_side_and_faces_you_its_grotesque_features_make_your_skin_crawl_but_you_respond

label grab_carlas_food:
    """
    Through great effort and care, you still prepare Carla a meal with love.
    
    A plate of body part shaped-chicken nuggets you made yourself along with a slice of cherry pie with a blood red sauce oozing out of the filling.
    """
    hide Mom
    hide Dad
    show Parents mouth_B eye_serious brow_sad at laugh:
        center
    """
    You chuckle to yourself knowing you did this hoping that Carla, wherever she is, will appreciate this meal.
    """
    show Parents mouth_sad overlay_fear eye_serious brow_angry
    """
    After grabbing the plate, you move towards her door eyeing the bat you prepared for any monsters in anticipation.
    
    Before interacting with the door, you take a moment to look at the numerous runes, religious symbols, and wards that you had placed on it.
    
    Your conflicting emotions swirl through you as you grab the knob on the foot of the door you use to pass Carla her food.
    """
    play sound 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 0.6
    with vpunch
    """
    The knob is jammed.
    """
    menu:
        "Pull the knob harder.":
            jump pull_the_knob_harder
        "Pass the food directly to Carla.":
            jump pass_the_food_directly_to_carla

label head_back_to_the_bedroom_door:
    show Parents mouth_sad  eye_serious brow_angry
    
    """
    You can't afford to let Carla escape in the state that she's in.
    """
    
    show Parents mouth_fear overlay_fear brow_surprised
    
    play sound "audio/Sound/Scraping Gong.wav" volume 1.0
    with vpunch
    """
    As you run back the way you came you realize that the door you entered through isn't there.
    """
    scene bg corridor_empty with dissolve
    """    
    Doubting your navigation you try to make your way back to the cell to no avail.
    """
    show Parents at corridor_tint
    $ lipsync(Parents, "act4", 'audio_29', "C-Carls?", 'mouth_fear')
    play sound 'audio/Sound/Carla_giggling.mp3' fadein 1.0 volume 0.8
    """
    Your cries for help are met with a quiet laughter.
    """
    pause 1.0
    show Parents mouth_fear overlay_fear eye_crying brow_surprised at running
    play target 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 0.5 loop
    """
    Anxiety transforms into panic and you begin running.
    
    The direction is unclear, only until you can find //something//.
    """
    play sound 'audio/Sound/Carla_giggling.mp3' fadein 0.5 volume 2.0
    """
    The unsettling laughter rises until it finds a place in your ears and stays there.
    """
    show Parents at running2
    """
    Desperately, you start to scream for Carla or anyone.
    """
    with sshake3
    stop target fadeout 2.0
    scene bg double_doors with dissolve
    
    """
    A set of doors finally catches your line of sight.
    """
    hide Parents
    menu:
        "Sprint for the doors.":
            jump sprint_for_the_doors

label ignore:
    $ lipsync(Carla, "act4", 'audio_30', "Nothing?", 'mouth_E')
    $ lipsync(Carla, "act4", 'audio_31', "Really?", 'mouth_stingy')
    
    """
    Your attempts to block out Carla are proving difficult, but you continue reading through an interesting article.
    
    The article recounts a story about a child who murdered their family singlehandedly.
    
    Allegedly the child had shown no symptoms of possession until the very last moment.
    
    Their true colors were shown once their guards were down and they had shown vulnerability towards the child.
    
    You glance at Carla's door, unsure whether to feel disgust or pity for the entiy inside that room.
    """
    
    $ lipsync(Carla, "act4", 'audio_32', "Please?", 'mouth_E')
    $ lipsync(Carla, "act4", 'audio_33', "I'm getting hungry.", 'mouth_sad')
    
    """
    The vagueness of the story you recounted causes you to doubt its legitimacy after hearing Carla's voice.
    
    How can a monster beg for food in this moment? Carla has been nothing but compliant through your entire breakdown.
    
    That may be because she understands, rather understood her own situation. The monster may have taken her over this point, looking for an opportunity to strike.
    
    Even so, you still care for your child.
    """
    hide Carla with dissolve
    menu:
        "Grab Carla's food.":
            jump grab_carlas_food

label inside_the_hallway:
    scene black
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 1.0
    pause 0.6
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 1.0
    pause 0.6
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 1.0
    pause 0.6
    play sound 'audio/Sound/Prison Scene Sounds/Stone Footstep.wav' volume 1.0
    """
    You blindly move through the blackness until you stop in front of a dimly lit cell.
    """
    stop sound fadeout 1.0
    """
    No Carla.
    """
    play sound 'audio/Sound/Prison Scene Sounds/Prison Metal Bar Cell Door Roll Close - QuickSounds.com.mp3' volume 2.0
    scene bg cell_prison with fade
    show Parents mouth_fear brow_surprised overlay_fear at prison_tint
    """
    The sight of the small cell's condition makes you wince.
    """
    hide Parents
    show Parents mouth_sad eye_serious brow_default at prison_tint
    """
    You look for any clues for Carla's whereabouts in the cell.
    """
    hide Parents    
    menu:
        "Check the bed.":
            jump check_the_bed
        "Check the bucket.":
            jump check_the_bucket
        "Check her shelves.":
            jump check_her_shelves

label keep_fighting:
    """
    With the bat practically useless in this endeavor, you attempt to slip your fingers between the murderous hands and your neck.

    You manage to get some space, but your arms are gripped by another force. Another set of hands.
    
    They pull your arms towards your side and you feel your consciousness slipping until you can no longer attempt to writhe yourself free.
    """
    pause 2.0
    show layer master at glitch
    show Carla brow_angry2 eye_default mouth_D overlay_fear overlay_dirt overlay_blood:
        center
        zoom 1.28
        matrixcolor InvertMatrix(0.92)*ContrastMatrix(1.33)*SaturationMatrix(1.46)*BrightnessMatrix(0.08)*HueMatrix(0.0) 
        alpha 0.0
        parallel:
            linear 2.0 zoom 1.5
        parallel:
            linear 2.0 alpha 1.0 
    
    $ lipsync(Carla, "act4", 'audio_34', "No more distractions.", 'mouth_H')
    show Carla brow_surprised
    $ lipsync(Carla, "act4", 'audio_35', "No more excuses.", 'mouth_D')
    
    play sound 'audio/Sound/Evil_laugh.mp3' fadein 2.0 volume 5.0
    show Carla brow_default at laugh
    """
    A devilish laugh creeps into your ears.
    """
    stop sound fadeout 2.0
    scene bg child_ending with dissolve
    """
    You feel your neck snapping in several places until your vision is swallowed by the blackness.
    """
    $ child_ending.grant()
    $ lipsync(Demon, 'act4', 'audio_36', "Whether dead or alive, all I need is a little imagination to play with you.", invisible=True)
    scene black
    pause 2.0
    "GAME END."
    
    return

label knowing_youll_be_back_at_the_start_you_allow_the_cycle_to_continue_anew:
    stop sound fadeout 2.0
    scene bg bedroom_sunset
    show blink
    show Carla brow_sad eye_crying mouth_angry2 overlay_fear at left
    
    $ lipsync(Carla, "act4", 'audio_37', "Hello??", 'mouth_angry2')
    $ lipsync(Carla, "act4", 'audio_38', "Wake up!", 'mouth_angry2')
    
    play music 'audio/Music/A_Trick_of_Mind_House.ogg' fadein 3.0 volume 0.3
    
    """
    Carla's cries bring you both back to reality.

    On the ground, Carla tugs at your leg. You pull away and immediately stand up.
    """
    
    show Parents mouth_E overlay_fear eye_serious brow_angry
    
    $ lipsync(Parents, "act4", 'audio_39', "Carla!", 'mouth_fear')
    
    hide Parents
    show Dad overlay_fear eye_serious brow_angry mouth_fear
    show Mom overlay_fear eye_serious brow_angry mouth_fear
    
    $ lipsync(Dad, "act4", 'audio_40', "I'm sick of these games.", 'mouth_fear')
    $ lipsync(Mom, "act4", 'audio_41', "Whatever you're doing you need to STOP.", 'mouth_X')
    
    show Carla brow_sad eye_default mouth_angry2 overlay_fear
    $ lipsync(Carla, "act4", 'audio_42', "I haven't done anything!", 'mouth_angry2')
    
    show Mom mouth_D
    
    "Carla's face shows an innocent desperation."
    
    $ lipsync(Mom, "act4", 'audio_43', "Don't lie to me.", 'mouth_H')
    $ lipsync(Dad, "act4", 'audio_44', "First the carnival and then this?")
    $ lipsync(Mom, "act4", 'audio_45', "It might be fun for you, but it's not for me!", 'mouth_sad')
    
    show Carla brow_surprised eye_default overlay_fear
    $ lipsync(Carla, "act4", 'audio_46', "That again?", 'mouth_angry2')
    show Carla brow_angry eye_crying
    $ lipsync(Carla, "act4", 'audio_47', "I told you I didn't have anything to do with that.", 'mouth_G')
    $ lipsync(Carla, "act4", 'audio_48', "You did the same thing again today!", 'mouth_angry2')
    show Carla eye_default
    $ lipsync(Carla, "act4", 'audio_49', "The second we started playing, you /passed/ out //again//. ", 'mouth_sad')
    
    "Carla purses her lips and she speaks again."
    show Carla eye_crying
    $ lipsync(Carla, "act4", 'audio_50', "If you don't want to spend time with me then just tell me.", 'mouth_angry')
    $ lipsync(Carla, "act4", 'audio_51', "You don't have to fake it.", 'mouth_angry')
    
    # <!--(THIRD MAJOR CHOICE)-->
    
    hide Dad
    hide Mom
    show Parents mouth_fear eye_default brow_surprised
    show parents_fear_overlay_mask
    """
    Carla's words cut deeply, but there is more at play here.
    
    Your account of the past events conflicts with Carla's retelling.

    What do you do?
    """
    hide parents_fear_overlay_mask with dissolve
    menu:
        "Carls, of course I want to spend time with you.":
            $ ending_condition += 10
            jump carls_of_course_i_want_to_spend_time_with_you
        "Leave the room.":
            $ ending_condition -= 10
            jump leave_the_room

label leave_the_room:
    show Parents mouth_sad eye_serious brow_angry
    
    "You urgently move for the door but Carla tries to talk to you."
    
    show Carla brow_surprised eye_default mouth_angry2 with hpunch
    $ lipsync(Carla, "act4", 'audio_52', "Wait where are you going?", 'mouth_angry2')
    
    """
    For a brief moment you hesitate, compelled to tell Carla what's happening.
    
    The demon might act if you give it away.
    """
    show Parents mouth_sad eye_serious brow_sad
    $ lipsync(Parents, "act4", 'audio_53', "I'll be back.", 'mouth_sad')
    
    show Carla brow_sad eye_default mouth_angry overlay_fear
    $ lipsync(Carla, "act4", 'audio_54', "So you don't want to spend time with me?", 'mouth_fear')

    hide Parents
    show Dad mouth_sad brow_angry
    show Mom mouth_sad eye_serious brow_angry
    
    $ lipsync(Mom, "act4", 'audio_55', "That's not what I said, I just remembered I need to take care of something.")
    show Mom at mom_walk
    play sound 'audio/Sound/House Scene Sounds/Wood Footstep Shuffle.wav' volume 0.2
    pause 0.2
    play sound 'audio/Sound/House Scene Sounds/Wood Footstep Shuffle.wav' volume 0.2
    pause 0.2
    play sound 'audio/Sound/House Scene Sounds/Wood Footstep Shuffle.wav' volume 0.2
    pause 0.2
    stop sound fadeout 0.5
    """
    Your mind is focused and Carla's voice fades out as you leave. 

    You can't allow yourself to be convinced by Carla's words since she can't be fully trusted.
    
    You feel shame and guilt wash over you both but you press on.
    """
    show Dad eye_serious brow_sad at dad_walk
    play sound 'audio/Sound/House Scene Sounds/Wood Footstep Shuffle.wav' volume 0.5
    pause 0.5
    play sound 'audio/Sound/House Scene Sounds/Wood Footstep Shuffle.wav' volume 0.5
    pause 0.5
    play sound 'audio/Sound/House Scene Sounds/Wood Footstep Shuffle.wav' volume 0.5
    pause 0.5
    """
    You exit the room unable to cope with what you're about to do.
    """
    scene black with dissolve
    
    jump you_exit_the_room_unable_to_cope_with_what_youre_about_to_do

label open_the_doors:
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 2.5
    play target 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 1.0
    with vpunch
    """
    The doors are an entrance to a courtyard of some sorts.
    """
    scene bg courtyard with dissolve
    """
    Even in the open, you feel confined.
    
    Your attention is drawn towards an evil aura coming from a large shadow at the center of the courtyard.
    """
    
    show Parents mouth_fear overlay_fear eye_crying brow_surprised at courtyard_tint_parents
    
    $ lipsync(Parents, "act4", 'audio_56', "Carla?", 'mouth_fear')
    
    show Parents mouth_sad overlay_fear eye_crying brow_angry
    """
    Step by step, you cautiously approach the shadow.

    Every inch closer to the being brings out a wave of rage inside of you. 
    
    Seething anger at your situation.
    """
    show Parents mouth_sad overlay_fear eye_serious brow_angry
    """
    Unending rage towards Carla.

    Spiteful resentment to yourself.
    
    You manage to get close enough for the shadow to subside.
    """
    scene bg courtyard_creature_carla with dissolve
    """
    A gargantuan monster, comforts Carla, who silently watches the floor.
    """
    menu:
        "Get closer.":
            jump get_closer

label pass_the_food_directly_to_carla:
    hide Parents
    show Dad brow_sad eye_default mouth_sad
    show Mom brow_sad eye_serious mouth_sad
    
    $ lipsync(Dad, "act4", 'audio_57', "Carla, I have to open your door to pass your food.", 'mouth_sad')
    
    show Carla brow_sad eye_default mouth_sad at left:
        matrixcolor TintMatrix("#380e0e")*SaturationMatrix(1.0000)*ContrastMatrix(1.6574)
    
    $ lipsync(Carla, "act4", 'audio_58', "So I get to see you finally?", 'mouth_sad')
    
    "Carla's innocence strikes a nerve in your heart, but you continue the negotiation."
    
    show Mom brow_sad eye_default mouth_sad
    
    $ lipsync(Mom, "act4", 'audio_59', "Yes, on one condition.", 'mouth_sad')
    
    "Carlas snappily responds."
    
    show Carla brow_angry2 eye_default mouth_angry
    $ lipsync(Carla, "act4", "audio_60", "Who's making the condition?", 'mouth_angry')
    $ lipsync(Carla, "act4", "audio_61", "You or me?", 'mouth_angry2')
    
    show Mom brow_angry eye_serious mouth_sad
    show Dad brow_angry mouth_sad
    
    $ lipsync(Dad, "act4", 'audio_62', "Very funny Carls, but sure, lets start with you.", 'mouth_sad')
    
    $ lipsync(Carla, "act4", 'audio_63', "My condition is...")
    $ lipsync(Carla, "act4", 'audio_64', "chicken nuggets with... a milkshake.", 'mouth_B')
    show Dad brow_surprised eye_default mouth_B
    show Mom brow_sad eye_serious
    $ lipsync(Mom, "act4", 'audio_65', "Sorry missy, best I can do is a pie.", 'mouth_C')
    
    show Carla brow_surprised eye_default
    $ lipsync(Carla, "act4", 'audio_66', "Ew. Nevermind.", 'mouth_stingy')
    show Parents brow_surprised at laugh:
        center
    hide Mom
    hide Dad
    play sound 'audio/Sound/Dad_laugh.mp3' fadein 0.5 volume 0.3
    play target 'audio/Sound/Mom_laugh.mp3' fadein 0.5 volume 0.5
    $ lipsync(Parents, "act4", 'audio_67', "Ha. Ha.", 'mouth_C')
    $ lipsync(Parents, "act4", 'audio_68', "I know you love cherry pie.", 'mouth_B')
    stop sound fadeout 0.5
    stop target fadeout 0.5
    show Carla brow_default eye_default mouth_fear
    $ lipsync(Carla, "act4", 'audio_69', "Oh nevermind my nevermind then.", 'mouth_fear')
    show Carla Carla brow_surprised eye_default mouth_sad
    $ lipsync(Carla, "act4", 'audio_70', "What's your condition then?", 'mouth_sad')
    
    show Parents eye_serious brow_angry
    $ lipsync(Parents, "act4", 'audio_71', "No games.", 'mouth_sad')
    $ lipsync(Parents, "act4", 'audio_72', "That's it.", 'mouth_sad')
    show Carla brow_surprised eye_default mouth_G
    "Carla hesitates for a moment before answering calmly, her demeanor has changed."
    show Parents mouth_C eye_default brow_surprised
    
    $ lipsync(Carla, "act4", 'audio_73', "Ok.", 'mouth_X')
    
    menu:
        "Begin unlocking her door.":
            jump begin_unlocking_her_door

label pick_it_up:
    """
    The image on the page isn't the same as the one before.
    """
    scene black with dissolve
    camera
    pause 2.0
    scene bg bedroom_sunset
    camera:
        zoom 1.0
        red_blue_beam
        repeat
    show blink:
        pause 2.0
    play sound 'audio/Sound/Prison Scene Sounds/Police Sirens.mp3' loop volume 1.0
    """
    As reality returns and something else you didn't expect happens.
    
    Red and blue lights beam through Carla's bedroom window.
    """
    show Parents mouth_fear eye_default brow_surprised:
        matrixcolor TintMatrix("#7b7cbb")*SaturationMatrix(0.2352)*ContrastMatrix(2.4722)
        center
    $ adults_ending.grant()
    $ lipsync(Parents, "act4", 'audio_74', "...Carls?", 'mouth_fear')
    scene bg adults_ending with dissolve
    pause 2.0
    "GAME END."

    return

label pull_the_knob_harder:
    """
    Both of you tightly grip the knob to the compartment and take a deep breath.

    With a strong and quick tug you pull on the handle, hoping to make enough space to pass Carla her food.
    """
    play sound 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 1.0
    with sshake3
    """
    The door starts to give which signals you that you're almost there.

    One more pull and...
    """
    play sound 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 2.0
    with sshake2
    """
    The knob snaps off of the door, causing you to fly backwards into the floor.
    """
    hide Parents with dissolve
    show Carla brow_angry2 eye_default mouth_C at left:
        matrixcolor TintMatrix("#380e0e")*SaturationMatrix(1.0000)*ContrastMatrix(1.6574)
    play sound 'audio/Sound/Carla_laugh.mp3' fadein 0.5 volume 2.0 loop
    """
    Carla belts out in laughter as you pick yourself up.
    """
    show Carla at laugh    
    show Parents mouth_sad  eye_serious brow_angry
    $ lipsync(Parents, "act4", 'audio_75', "Ugh, shut up.", 'mouth_sad')
    show Carla at laugh
    play sound 'audio/Sound/Carla_giggling.mp3' fadein 0.5 volume 2.0
    "Carla continues to laugh."
    hide Parents
    show Dad mouth_sad eye_serious brow_angry
    show Mom mouth_sad  eye_serious brow_angry
    $ lipsync(Mom, "act4", 'audio_76', "I guess you're not eating today then.")
    
    stop sound fadeout 0.5
    show Carla brow_sad eye_default mouth_stingy overlay_fear
    "The laughter immediately ceases and Carla begs."
    
    $ lipsync(Carla, "act4", 'audio_77', "Wait please, I'm starving.", 'mouth_stingy')
    $ lipsync(Carla, "act4", 'audio_78', "I won't laugh any more I promise.", 'mouth_E')
    
    "Unwilling to let her starve, you decide to pass the food another way"
    
    jump pass_the_food_directly_to_carla

label respond:
    $ lipsync(Mom, "act4", "audio_79", "I'll get to you when I can.")
    $ lipsync(Dad, "act4", "audio_80", "just hang in there alright?", 'mouth_sad')
    
    $ lipsync(Carla, "act4", "audio_81", "Sure.")
    $ lipsync(Carla, "act4", "audio_82", "Sure. I'll just wait here, not like I can go anywhere else.")
    
    hide Mom
    hide Dad
    show Parents mouth_fear eye_serious brow_angry
    $ lipsync(Parents, "act4", "audio_83", "Excuse me missy.", 'mouth_sad')
    
    hide Parents
    show Dad mouth_sad eye_serious brow_angry
    show Mom mouth_sad eye_serious brow_angry
    
    $ lipsync(Mom, "act4", "audio_84", "I'm trying to save you.", 'mouth_sad')
    $ lipsync(Dad, "act4", "audio_85", "Hell, I'm not even sure if you're //you// right now.", 'mouth_sad')

    show Carla brow_default eye_default mouth_C overlay_fear at laugh
    play sound 'audio/Sound/Carla_laugh.mp3' fadein 0.5 volume 1.0
    # matrixcolor TintMatrix("#211619")*Saturatio   nMatrix(1.0000)*ContrastMatrix(1.6574)

    "Carla laughs, making you uneasy as you start to put your papers down."
    
    $ lipsync(Carla, "act4", "audio_86", "Even after all those stupid tests we did you still don't believe me?", 'mouth_C')
    $ lipsync(Mom, "act4", "audio_87", "There was something wrong with them.")
    
    show Carla brow_angry2 eye_default mouth_stingy
    play sound 'audio/Sound/House Scene Sounds/Sigh.wav' volume 3.0
    
    "Exasperated, Carla lets out a sigh."
    
    $ lipsync(Carla, "act4", "audio_88", "What's wrong with yo-", 'mouth_stingy')
    stop sound fadeout 2.0
    $ lipsync(Dad, "act4", "audio_89", "You'll get fed, and that'll be that.")
    
    hide Dad
    hide Mom
    show Parents mouth_sad eye_serious brow_sad
    $ lipsync(Parents, "act4", "audio_90", "Wait here.", 'mouth_sad')
    hide Carla with dissolve
    jump grab_carlas_food

label shut_the_door_and_lock_it:
    play weapon 'audio/Sound/Prison Scene Sounds/Monster Heavy Breathing.wav' fadein 2.5 volume 1.0
    show Parents mouth_C eye_serious brow_angry
    
    "After moments of waiting for any response, you decide to make one last effort to get Carla's attention."
    
    $ lipsync(Parents, "act4", "audio_91", "Ok Carla!", 'mouth_C')
    show Parents mouth_sad
    $ lipsync(Parents, "act4", "audio_92", "I'm gonna wait until you're done then.", 'mouth_C')
    scene bg corridor_empty with fade
    """
    The unnerving silence eats at you as your internal voice tells you to shut the door.
    """
    pause 1.0
    scene bg corridor_creature with dissolve

    play target 'audio/Sound/Prison Scene Sounds/Monster Snarl.WAV' fadein 0.5 volume 3.0
    pause 1.0
    """
    You decide that you waited long enough, but before you can act you see a monster reach out from the the blackness.
    """
    play target 'audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 2.5
    scene bg livingroom_night:
        matrixcolor TintMatrix("#993131")*SaturationMatrix(1.0000)*ContrastMatrix(0.8981)
    show Parents mouth_fear overlay_fear eye_default brow_surprised:
        matrixcolor TintMatrix("#993131")*SaturationMatrix(1.0000)*ContrastMatrix(0.8981)
        center
    """
    The terrifying sight urges you to slam the door shut and begin latching it.
    """
    with sshake2
    play sound 'audio/Sound/House Scene Sounds/Door Hitting1.wav' volume 3.0
    """
    As you begin locking the door, the hands slam into it, pushing you away.
    """
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 2.0
    """
    You rush back to the door forcing all of your might into it, trying to keep the demon inside as you continue to lock it.
    """
    play target 'audio/Sound/House Scene Sounds/Door Hitting1.wav' volume 10.0
    with sshake
    """
    The first lock. The hands continue to bang at the door.
    """
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 3.0
    play target 'audio/Sound/House Scene Sounds/Door Hitting2.wav' volume 10.0
    with sshake
    """
    The second lock.
    """
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 4.0
    play target 'audio/Sound/House Scene Sounds/Door Hitting2.wav' volume 10.0
    with sshake3
    """
    On the third lock you feel the door start to give and you press your feet to the ground, hoping you have enough strength to get the final lock.
    """
    play target 'audio/Sound/House Scene Sounds/Door Hitting3.wav' volume 10.0
    play sound 'audio/Sound/House Scene Sounds/Lock and Unlock Door.wav' volume 5.0
    stop target fadeout 2.0
    """
    On the fourth lock, the slamming ceases.
    
    You've managed to shut the entity away. For now.
    """
    show Parents mouth_sad overlay_fear eye_serious brow_angry
    """
    Backing away from the door, you grab the bat by the door, ready to strike.
    """
    stop sound fadeout 1.0
    stop target fadeout 1.0
    stop weapon fadeout 1.0
    """
    Silence.
    """
    with sshake
    show Parents mouth_fear eye_default brow_surprised
    play weapon '<from 0 to 1>audio/Sound/House Scene Sounds/Door Slam Close.WAV' volume 5.0
    play target 'audio/Sound/Prison Scene Sounds/Monster Snarl.WAV' volume 3.0
    pause 1.5
    play sound 'audio/Sound/House Scene Sounds/Dad Scream.wav' volume 3.5
    play target 'audio/Sound/House Scene Sounds/Mom Scream.wav' volume 3.5
    """
    The door bursts open and the hands successfully grab at you and pull you in. The door slams behind you as you get further and further away.
    """
    play target 'audio/Sound/Prison Scene Sounds/Monster Snarl.WAV' volume 3.0
    pause 1.5
    scene black with dissolve
    """
    You do your best to swing at the hands but become suffocated by the darkness.
    """
    jump inside_the_hallway

label sprint_for_the_doors:
    stop sound fadeout 2.0
    play sound 'audio/Sound/Carla_laugh.mp3' fadein 0.5 volume 1.0
    """
    As you approach them the laughter subsides.
    
    You take a moment to breathe, hoping that the other side may be the exit.
    """
    menu:
        "Open the doors.":
            jump open_the_doors

label the_monster_leaves_carlas_side_and_faces_you_its_grotesque_features_make_your_skin_crawl_but_you_respond:
    "the monster leaves Carla's side and faces you. Its grotesque features make your skin crawl, but you respond."
    
    hide Parents
    show Dad mouth_sad eye_default brow_angry at courtyard_tint_parents
    show Mom mouth_sad eye_default brow_angry at courtyard_tint_parents
    
    $ lipsync(Mom, "act4", "audio_93", "All of this is for protection.", 'mouth_C')
    
    show Carla brow_angry eye_default mouth_angry overlay_dirt
    $ lipsync(Carla, "act4", "audio_94", "For you it was.", 'mouth_B')
    show Mom mouth_sad
    $ lipsync(Carla, "act4", "audio_95", "I was the one stuck in the room.", 'mouth_B')
    
    show Dad eye_serious
    show Mom eye_serious
    $ lipsync(Dad, "act4", "audio_96", "Because what you're doing is dangerous.", 'mouth_sad')
    $ lipsync(Mom, "act4", "audio_97", "Can't you see what this is?")
    $ lipsync(Mom, "act4", "audio_98", "What it means?")
    
    show Carla brow_surprised eye_default mouth_angry2 overlay_dirt
    $ lipsync(Carla, "act4", "audio_99", "Dangerous?", 'mouth_stingy')
    show Carla brow_angry2
    $ lipsync(Carla, "act4", "audio_100", "It's just //Story Time//.", 'mouth_angry2')
    $ lipsync(Carla, "act4", "audio_101", "It's a game, that's all it's been.", 'mouth_angry2')
    
    "The monster creeps its way in your direction, causing you to instinctually hold up your bat."
    show Dad overlay_fear
    show Mom overlay_fear
    $ lipsync(Dad, "act4", "audio_102", "That didn't feel like a game Carls.", 'mouth_sad')
    show Dad eye_crying
    $ lipsync(Dad, "act4", "audio_103", "I felt everything that happened to me...", 'mouth_sad')
    show Mom eye_crying
    $ lipsync(Mom, "act4", "audio_104", "The biting, the drowning...", 'mouth_sad')

    "the monster shifts closer to you."
    
    show Carla brow_angry
    $ lipsync(Carla, "act4", "audio_105", "Then why did you play along?", 'mouth_angry2')
    
    hide Mom
    hide Dad
    show Parents mouth_fear overlay_fear eye_default brow_angry at courtyard_tint_parents
    
    $ lipsync(Parents, "act4", "audio_106", "We had no choice.", 'mouth_fear')
    
    """
    The monster is close enough for you to strike. The aura of hatred seethes under your skin.
    """
    show Parents brow_surprised
    play target 'audio/Sound/Prison Scene Sounds/Monster Snarl.WAV' fadein 1.0 volume 3.5
    """
    It lifts its tree trunk arms as if they were to crush you in its embrace.
    """
    hide Parents
    # <!--(FIFTH MAJOR CHOICE)-->
    menu:
        "Attack the monster.":
            $ ending_condition += 10
            if ending_condition == 50:
                $ Perfect_Parent.grant()
            jump attack_the_monster
        "Wait.":
            $ ending_condition -= 10
            if ending_condition == -50:
                $ Carlas_Nightmare.grant()
            jump wait

label wait:
    "Carla stands up to face you and angrily protests your stance."
    
    show Carla brow_angry overlay_fear
    $ lipsync(Carla, "act4", "audio_107", "You chose to lock me up!", 'mouth_angry')
    
    "The monster swings its arms at you and you deftly step back to avoid the impact."
    show Carla brow_angry2    
    $ lipsync(Carla, "act4", "audio_108", "I'm not the one who keeps avoiding the game!", 'mouth_angry2')
    
    """
    The monster swings again, prompting you to hold up your bat.
    
    As Carla's anger grows, the monster's aggression increases.
    """
    
    show Parents mouth_fear overlay_fear eye_default brow_surprised at courtyard_tint_parents
    
    $ lipsync(Parents, "act4", "audio_109", "Carls, stop!", 'mouth_fear')
    
    hide Parents
    show Dad mouth_fear overlay_fear eye_default brow_surprised at courtyard_tint_parents
    show Mom mouth_fear overlay_fear eye_default brow_surprised at courtyard_tint_parents
    $ lipsync(Mom, "act4", "audio_110", "This isn't you!", 'mouth_fear')
    $ lipsync(Dad, "act4", "audio_111", "You love horror movies and love playing games, you don't hurt people!", 'mouth_fear')
    
    show Carla brow_angry2 eye_default mouth_D overlay_fear at laugh
    play target 'audio/Sound/Prison Scene Sounds/Monster Snarl.WAV' fadein 2.0 volume 0.5
    """
    Carla evily smiles at you before the monster strikes again.
    """
        
    hide Mom
    hide Dad
    show Parents mouth_G overlay_fear eye_serious brow_angry at courtyard_tint_parents
    """
    Having the bat empowers you to act unlike before.
    
    No longer outnumbered or in the wrong environment, you feel something you hadn't before.
    
    Control.
    """
    menu:
        "Attack the monster.":
            jump attack_the_monster

label you_exit_the_room_unable_to_cope_with_what_youre_about_to_do:
    scene bg livingroom_night with fade
    """
    Halloween approaches and your anxiety mounts.
    
    After combing through every resource available, your patience wears incredibly thin.
    
    You've contacted every expert you can think of, paranormal, mythical, and religious.
    
    Despite all of your effort, no one has given you a satisfactory solution or answer.
    """
    show Dad brow_angry eye_serious mouth_sad
    show Mom eye_serious mouth_fear brow_angry
    $ lipsync(Dad, "act4", "audio_112", "Don't bullshit me.", 'mouth_sad')
    $ lipsync(Dad, "act4", "audio_113", "I've seen it and you've seen these kinds of things too.", 'mouth_X')
    $ lipsync(Mom, "act4", "audio_114", "It's TEXTBOOK possession.", 'mouth_sad')
    $ lipsync(Mom, "act4", "audio_115", "My girl is still in there somewhere.")
    
    "A wave of anger takes over. This expert is fake like the others."
    hide Dad
    hide Mom
    show Parents eye_serious brow_angry overlay_fear
    
    camera:
        subpixel True crop_relative True xzoom 1.0 crop (0.0, 0.0, 1.0, 1.0) 
        anchor (0, 0) zoom 1.0 
        linear 0.15 anchor (351, 315) zoom 1.5 
    with Pause(0.2)
    camera:
        anchor (351, 315) zoom 1.5 

    $ lipsync(Parents, "act4", "audio_116", "I'm telling you.", 'mouth_fear')
    $ lipsync(Parents, "act4", "audio_117", "There //is// something here!", 'mouth_fear')
    
    camera
    
    hide Parents
    """
    To avoid the converstation from dragging on any longer you hang up.
    
    Carla speaks from behind her bedroom door.
    """
    scene bg bedroom_dark with fade
    show Carla brow_sad at left
    $ lipsync(Carla, "act4", "audio_118", "Is everything ok?", 'mouth_E')
    
    """
    You continue sifting through your notes ignoring Carla.
    
    Carla ruffles around in her room, before she speaks again.
    """
    
    $ lipsync(Carla, "act4", "audio_119", "I'm hungry.", 'mouth_sad')
    scene bg livingroom_night with pushleft
    show Dad brow_angry eye_default mouth_X
    show Mom brow_sad eye_default mouth_C
    show Carla brow_sad eye_default overlay_fear at left:
        matrixcolor TintMatrix("#380e0e")*SaturationMatrix(1.0000)*ContrastMatrix(1.6574)
    menu:
        "Respond.":
            jump respond
        "Ignore.":
            jump ignore

