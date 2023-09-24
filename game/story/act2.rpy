
label when_you_lose:
    hide Carla
    show Carla brow_surprised eye_default mouth_C at left

    """
    With a defeated look, you put the toy pistol down.
    """
    
    show Dad mouth_B
    show Mom mouth_B
    
    """
    Carla laughs, and you smile at the sight of her having fun.
    """
    
    $ lipsync(Carla, 'act2', 'audio_0', "Told you!")
    $ lipsync(Carla, 'act2', 'audio_1', "I knew you couldn't do it.")
    
    "Carla picks up the gun and waves it at you mockingly."
    
    show Mom brow_default eye_serious mouth_H
    show Dad brow_angry eye_default mouth_X
    $ lipsync(Mom, 'act2', 'audio_2', "Excuse me missy, I don't remember teaching you to be this sassy.")
    
    "your tone noticably forces a shift in the conversation."
    
    show Carla mouth_stingy
    $ lipsync(Carla, 'act2', 'audio_3', "You didn't.", 'mouth_stingy')
    play music 'audio/Music/A_Trick_of_Mind_Carnival_Creepy.ogg' volume 0.03 fadein 3.0   
    play sound '<from 2 to 8>audio/Sound/Fast Heartbeat.wav' fadein 1.0
    
    "The targets from the minigame face towards you and you feel the rate of your heart beat rise."
    
    show Dad mouth_sad eye_default brow_surprised
    show Mom mouth_sad eye_default brow_surprised
    with sshake3
    $ lipsync(Dad, 'act2', 'audio_4', "Carls, what are you doing?", default_mouth="mouth_surprised")
    hide Dad
    hide Mom
    show Carla brow_angry mouth_angry2
    "She open's her mouth to speak, but it opens unnatrually wide."
    show bg carnival_minigame with sshake
    show Parents eye_default brow_surprised mouth_fear overlay_fear
    show Carla brow_angry eye_crying mouth_angry overlay_fear
    play sound 'audio/Sound/Carnival Scene Sounds/Carla Screaming.mp3' fadein 2.0 volume 0.1
    with sshake
    camera:
        linear 0.5 offset (0.0, -1053.0) matrixanchor (0.5, 0.55) zoom 2.16 
    play sound 'audio/Sound/Carnival Scene Sounds/Carla Screaming.mp3' fadein 2.0 volume 0.2
    """
    Carla screams at you and the shooting gallery begins to shudder.
    
    Before you can let out your next words, the targets leap out at you.
    """
    play weapon '<from 0 to 3>audio/Sound/Carnival Scene Sounds/Snarling.WAV' fadein 2.0 loop
    with vpunch
    camera
    show debris2
    show monster_ducklings at monster_ducklings_attack
    show boss_duck at moving_boss_duck
    show Parents overlay_blood
    show bloody_view1
    with vpunch
    play target 'audio/Sound/Carnival Scene Sounds/Eating Guts.wav' volume 0.3 fadein 1.0 loop
    """
    Their endless numbers overwhelm you as you feel teeth sinking into your flesh. 
    """
    with sshake2

    jump act26

label when_you_win:
    
    show Dad brow_default eye_default mouth_D
    
    """
    With a smug grin you rest the rifle on the game stand and look at Carla.
    
    Full of anger, Carla congratulates you.
    """
    
    show Carla brow_angry2 mouth_angry at left
    
    $ lipsync(Carla, 'act2', 'audio_5', "G-good job.", 'mouth_angry')
    
    "she speaks softly, taking you aback."

    hide Mom
    hide Dad
    
    $ lipsync(Parents, 'act2', 'audio_6', "Carls?")
    
    hide Parents
    show Dad
    show Mom
    
    $ lipsync(Carla, 'act2', 'audio_7', "You beat my score...", 'mouth_angry')
    
    $ lipsync(Dad, 'act2', 'audio_8', "Hey, hey.", 'mouth_sad')
    $ lipsync(Dad, 'act2', 'audio_9', "It's alright, it's a game.")
    $ lipsync(Dad, 'act2', 'audio_10', "You can beat my score on your turn Carls.")
    
    $ lipsync(Carla, 'act2', 'audio_11', "It's not just a game, it's my game.", 'mouth_sad')
    $ lipsync(Carla, 'act2', 'audio_12', "You weren't supposed to beat it.", 'mouth_stingy')
    show Carla brow_angry2 mouth_C overlay_fear
    "Carla's eyes shift towards the floor for a few seconds and she looks back at you with a sinister smile."
    $ lipsync(Carla, 'act2', 'audio_13', "You want to play again?")
    menu:
        "Play the game again.":
            jump act25c
        "Carls, we should be going to bed now. I think the game is over.":
            jump act25b

label act21:
    scene black with dissolve
    show Parents eye_closed at closed_eye_tint
    
    play sound "<from 6 to 15>audio/Sound/House Scene Sounds/Plastic Wrapping.mp3" volume 0.2 
    
    """
    Candy wrappers rustle while Carla shuffles around.
    """
    
    play sound "<from 0 to 3>audio/Sound/Carnival Scene Sounds/Abandoned Carnival.mp3" volume 0.02 fadein 1.0
    
    """
    You begin humming a tune to yourself.
    
    After a brief moment you realize you don't hear Carla moving, but feel a breeze of the wind against your face.
    
    Unsure of what's happening, you ask.
    """
    hide Parents
    
    show Dad eye_closed brow_surprised mouth_fear at closed_eye_tint
    show Mom eye_closed brow_surprised mouth_fear at closed_eye_tint
    with vpunch
    $ lipsync(Dad, 'act2', 'audio_14', "D-did you just open the window?")
    
    show Dad mouth_surprised
    show Carla brow_angry2 mouth_angry2 at left
    
    $ lipsync(Carla, 'act2', 'audio_15', "No!")
    stop sound fadeout 2.0
    show Carla mouth_angry2
    
    $ lipsync(Carla, 'act2', 'audio_16', "Keep your eyes closed until I say it's ok to open them please...")
    
    show Carla mouth_angry2
    show Dad mouth_X
    
    "Carla insists."
    
    hide Carla with dissolve
    
    show Mom mouth_sad
    
    """
    Going against your better judgement, you keep your eyes shut.
    
    You take a deep breath and begin smelling... food.
    
    Specifially popcorn and churros.
    
    The scent catches you off guard, but since nothing is burning, you trust Carla with the set up.

    You continue to hum your tune, patiently waiting for Carla to finish.
    
    Your attention is further grabbed hearing music similar to your hum.
    
    To double check, you stop and realize that there //is// music playing in the background.  
    """
    
    show Dad mouth_C
    
    """
    Before you can voice your concerns, Carla finally breaks her silence from your left.
    """
    
    show Dad mouth_sad
    show Carla at left
    
    $ lipsync(Carla, 'act2', 'audio_17', "Ok.")
    $ lipsync(Carla, 'act2', 'audio_18', "You can open your eyes now!")
    
    play sound "audio/Sound/Carnival Scene Sounds/Abandoned Carnival.mp3" volume 0.1 fadein 1.0
    
    scene bg carnival
    show blink
    with hpunch
        
    window auto hide
    camera:
        subpixel True 
        anchor (405, 342) zoom 1.4 
        linear 0.39 anchor (0, 0) zoom 1.0 
    with Pause(0.49)
    camera:
        anchor (0, 0) zoom 1.0 
    window auto show

    show Parents eye_default brow_surprised mouth_fear
    """
    Nervously, you open your eyes and find that the set up was not what you expected at all.
    
    To your shock, you're sitting on a ferris wheel overlooking a carnival.
    """
    show Parents overlay_fear
    """
    The sudden change in height frightens you, causing you to hold on to Carla.

    In a panicked voice, you question her.
    """
    
    $ lipsync(Parents, 'act2', 'audio_19', "C-Carla!")
    hide Parents
    show Dad brow_surprised eye_default mouth_fear overlay_fear
    show Mom brow_surprised eye_serious mouth_fear overlay_fear
    $ lipsync(Mom, 'act2', 'audio_20', "What the hell is this?")
    
    show Carla brow_surprised eye_default at left
    
    $ lipsync(Carla, 'act2', 'audio_21', "It's great isn't it?!", 'mouth_D')
    
    hide Mom
    hide Dad
    show Parents eye_default brow_surprised mouth_fear
    show parents_fear_overlay_mask
    hide parents_fear_overlay_mask with dissolve

    """
    Carla seems oblivious to your distress as you try to comprehend what's going on.
    
    The ferris wheel makes its descent and you have a moment to take in the sight.
    
    Conflicted, you press Carla for answers.
    """
    $ quick_menu = False
    play music 'audio/Music/A_Trick_of_Mind_Carnival.ogg' fadein 3.5 volume 0.03
    menu:
        "This isn't funny. What did you do?":
            jump act22a
        "Wow... this is amazing. How did you do this?":
            jump act22b

label act22a:
    $ quick_menu = True
    $ lipsync(Carla, 'act2', 'audio_22', "It's a part of the game isn't it?")
    $ lipsync(Carla, 'act2', 'audio_23', "This is the start of our story at the carnival.")
    show Carla brow_surprised eye_default mouth_D
    
    "Carla's excitment with her upcoming story puts you on edge."
    
    $ lipsync(Carla, 'act2', 'audio_24', "We start here on the ferris wheel and...")
    $ lipsync(Carla, 'act2', 'audio_25', "there's a MONSTER waiting for us at the bottom-")
    hide Mom
    hide Dad
    show Parents brow_angry eye_serious mouth_fear
    $ lipsync(Parents, 'act2', 'audio_26', "NO.")
    hide Parents
    show Dad brow_sad mouth_sad
    show Mom brow_surprised eye_serious mouth_fear
    
    "You interrupt Carla out of instinct."
    
    $ lipsync(Mom, 'act2', 'audio_27', "Carls, please no monsters.")
    $ lipsync(Mom, 'act2', 'audio_28', "I had plenty of those to deal with tonight.")
    
    $ lipsync(Carla, 'act2', 'audio_29', "They were fake though!")
    $ lipsync(Carla, 'act2', 'audio_30', "It won't be violent, I promise.")
    
    "You give Carla a stern look and she concedes."
    
    show Dad brow_default
    $ lipsync(Carla, 'act2', 'audio_31', "Fine, but just wait till you see the rest.")
    
    jump act23

label act22b:
    $ quick_menu = True
    show Parents mouth_D eye_default brow_surprised
    $ lipsync(Carla, 'act2', 'audio_32', "You really think it's amazing?")
    
    "Carla proudly looks over her creation."
    hide Parents
    show Dad
    show Mom
    
    $ lipsync(Dad, 'act2', 'audio_33', "I mean...")
    $ lipsync(Dad, 'act2', 'audio_34', "I don't know if I'm hallucinating.")
    $ lipsync(Dad, 'act2', 'audio_35', "But from what I see, it's impressive Carls.")
    
    $ lipsync(Carla, 'act2', 'audio_36', "Wait until you see whats at the bottom.")
    $ lipsync(Carla, 'act2', 'audio_37', "This is gonna be amazing.")
    show Carla eye_default mouth_B
    
    $ lipsync(Mom, 'act2', 'audio_38', "Excuse me?")
    show Mom brow_surprised eye_serious mouth_H
    
    play sound '<from 2 to 8>audio/Sound/Normal Heartbeat.wav' fadein 1.0 volume 0.5
    
    "your nerves begin to raise your heart rate while you imagine what Carla is about to put you through."
    
    $ lipsync(Carla, 'act2', 'audio_39', "Nothing!")
    show Carla brow_surprised eye_default mouth_D
    jump act23

label act23:
    """
    Carla's eyes illuminate again as the ferris wheel settles down on the ground.
    
    As soon as the ferris wheel touches the ground, Carla pulls off the seat harness and bolts out in front of you.
    """
    
    $ lipsync(Carla, 'act2', 'audio_40', "C'mon!")
    $ lipsync(Carla, 'act2', 'audio_41', "Let's look around!")
    
    "Carla yells back at you as she runs forward."
    
    hide Carla with dissolve
    hide Dad
    hide Mom
    show Parents eye_default brow_surprised
    
    $ lipsync(Parents, 'act2', 'audio_42', "Carls!", 'mouth_fear')
    
    hide Parents with dissolve
    """
    You reach out to grab her in a futile attempt.

    It's too late. You take off the harness and step off the ferris wheel to find Carla.
    """
    scene bg carnival_foodtent
    
    window auto hide
    camera:
        subpixel True additive 0.19 
        anchor (81, 252) zoom 1.26 blur 5.46 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.59)*BrightnessMatrix(0.22)*HueMatrix(0.0) 
        linear 1.60 anchor (0, 0) zoom 1.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(1.70)
    camera

    play sound 'audio/Sound/Carnival Scene Sounds/Carnival Ambience with Rides and People.mp3' fadein 3.0 volume 0.1
    
    """
    Your first instinct takes you to some food carts parked in front of a tent.

    Oddly enough, there is no one available to serve you.

    Knowing you have to focus on finding Carla, you only have time to look at one cart
    """
    menu:
        "Look at the first food cart.":
            jump act24a
        "Look at the second food cart.":
            jump act24b
        "Continue looking for Carla.":
            jump act24c

label act24a:
    """
    The aroma of churros hovers over the cart.
    
    Curiosity gets the better of you, causing you to peek into the cart.
    
    Surprisingly, no churros are available for you to take.
    """
    
    show Dad brow_sad
    show Mom brow_sad
    $ lipsync(Dad, 'act2', 'audio_43', "Very funny Carls.")
    $ lipsync(Dad, 'act2', 'audio_44', " I guess this is payback for those times I've told you no churros at the festivals.")
    
    jump act24c

label act24b:
    """
    Heat emanates from the cart and you pick up the smell of buttered popcorn.
    
    You suddenly feel hungry and step closer to the cart.
    
    A tub of hot popcorn sits in the center.
    """
    menu:
        "Reach for some popcorn.":
            jump act24d
        "Continue looking for Carla.":
            jump act24c

label act24c:
    stop sound fadeout 2.0
    show Dad brow_surprised
    show Mom brow_surprised

    scene bg carnival_minigame
    
    """
    You pass the food cart and hear Carla cheering for excitement followed by what sounds like a game with sound effects.
    
    Following the source, you reach Carla, who seems to be playing a minigame involving a gun and some targets.
    
    Carla skillfully shoots at the targets and finishes the game as you approach.
    
    As you get closer, the targets appear to be looking at you for a brief moment.
    
    Pretending to ignore what you saw, you express excitement.
    """
    
    show Mom brow_surprised eye_default mouth_C
    
    $ lipsync(Mom, 'act2', 'audio_45', "Ohh fun!")
    $ lipsync(Mom, 'act2', 'audio_46', "I remember a game like this when I was a kid.")
    
    show Mom mouth_C
    show Dad mouth_C
    """
    your smile beams while you observe the targets and the gun.
    
    Carla puts the rifle down and cheerfully tells you her accomplishments.
    """
    
    show Carla brow_default eye_default mouth_E at left
    
    $ lipsync(Carla, 'act2', 'audio_47', "I got the high score, I bet you can't beat me.")
    
    """
    she points at the game and motions you to play.
    
    You look at Carla's smile and back at the game.
    
    The excitement of what Carla has created during the game has worn off, but you don't want to disappoint her.
    """
    show Dad eye_default brow_default mouth_X
    show Mom eye_default brow_default mouth_X
    # <!--(FIRST MAJOR CHOICE)-->
    menu:
        "Ok missy, one game only.":
            $ ending_condition += 10
            show Dad mouth_A
            show Mom mouth_A
            jump act25a
        "Carls, we should be going to bed now. I think the game is over.":
            $ ending_condition -= 10
            show Mom mouth_sad
            jump act25b

label act24d:
    """
    You grab some popcorn and begin eating it.
    
    After a few scoops, you realize that there is no taste and you don't feel yourself getting full from eating it.
    """
    
    show Dad brow_sad eye_default mouth_sad
    show Mom brow_sad eye_default mouth_sad
    $ lipsync(Dad, 'act2', 'audio_48', "Ugh, c'mon Carls, you make all of this, but I can't have any popcorn?", 'mouth_X')

    "Annoyed, you continue your search."
    show Dad mouth_sad
    
    jump act24c

label act25a:
    "You pick up the toy pistol and play the game."
    "Instructions: Click on the targets to fire." 
    "You have 10 bullets and 30 seconds."
    "Game Start"
    window hide
    scene bg carnival_minigame
    $ my_game_config1 = GameConfig(target_nb=7, time_limit=30, bullet_max=10)
    $ minigame1 = ShootingGame(my_game_config1)
    $ minigame1.run()
    $ score = [(minigame1.status.target_nb - minigame1.status.target_now), minigame1.status.target_nb] 
    $ karma = [(minigame1.status.karma)]
    "Score : [score[0]]/[score[1]]"
    scene bg carnival_minigame
    stop music fadeout 2.0
    if score[0] == score[1]:
        jump when_you_win
    else:
        jump when_you_lose

label act25b:
    stop music fadeout 2.0
    play music 'audio/Music/A_Trick_of_Mind_Carnival_Creepy.ogg' volume 0.1 fadein 3.0
    $ lipsync(Carla, 'act2', 'audio_49', "I set all of this up and it's already over?")
    show Carla brow_sad eye_default mouth_stingy overlay_fear
    
    "Carla's frustration begins to show."
    
    $ lipsync(Dad, 'act2', 'audio_50', "What you did here is amazing, but it's late Carls.")
    show Dad brow_sad eye_serious mouth_sad
    
    "Your attempt to appease Carla fails."
    
    $ lipsync(Carla, 'act2', 'audio_51', "We barely even started!")
    show Carla brow_angry2 eye_default mouth_angry2    
    
    "Carla's voice cracks"
    
    $ lipsync(Carla, 'act2', 'audio_52', "It's not fair.")
    
    show Mom brow_angry eye_serious mouth_C
    
    "You sternly answer"
    
    $ lipsync(Mom, 'act2', 'audio_53', "Excuse me?")
    $ lipsync(Mom, 'act2', 'audio_54', "That's enough.")
    $ lipsync(Mom, 'act2', 'audio_55', "We're going to put all of...")
    $ lipsync(Mom, 'act2', 'audio_56', "Whatever this is away and it'll be bed time.")
    camera:
        linear 0.5 offset (0.0, -1053.0) matrixanchor (0.5, 0.55) zoom 2.16 
    show Carla brow_angry eye_default mouth_angry
    
    """
    Carla angrily looks at you.
    """
    show Carla brow_angry eye_crying mouth_angry overlay_fear
    play sound 'audio/Sound/Carnival Scene Sounds/Carla Screaming.mp3' fadein 2.0 volume 0.1
    """
    Her eyes begin to water and she begins to scream.
    """
    camera
    show bg carnival_minigame with sshake3
    play weapon '<from 0 to 3>audio/Sound/Carnival Scene Sounds/Snarling.WAV' fadein 2.0 loop
    """
    The environment begins to shake and you notice the targets from the minigame have morphed into disfigured versions of their previous incarnation.
    """
    hide Mom
    hide Dad
    show Parents mouth_fear overlay_fear eye_default brow_surprised
    with sshake2
    show debris2
    play sound '<from 2 to 8>audio/Sound/Fast Heartbeat.wav' fadein 1.0
    """
    The decaying situation raises your heart rate again and you begin yelling back at Carla to stop.
    """
    with sshake2
    $ lipsync(Parents, 'act2', 'audio_57', "Stop!", 'mouth_fear')
    with sshake3
    play sound 'audio/Sound/Carnival Scene Sounds/Carla Screaming.mp3' fadein 2.0 volume 0.2
    """
    Carla's scream continues and the targets face you again.
    
    They've completely transformed.
    """
    show monster_ducklings at monster_ducklings_attack
    show boss_duck at moving_boss_duck
    show Parents overlay_blood
    show bloody_view1
    play target 'audio/Sound/Carnival Scene Sounds/Eating Guts.wav' volume 0.3 fadein 1.0 loop
    """
    Before you can act, they begin jumping at you until you're overwhelmed.
    
    The abominations begin gnawing at your body as you cry out in agony.
    """
    with sshake2
    jump act26

label act25c:
    "You play the game again, but its difficulty has shot up exponentially and you fail the game."
    
    jump when_you_lose

label act26:
    play weapon '<from 0 to 6>audio/Sound/Carnival Scene Sounds/Flesh Squishing.wav' fadein 2.0 volume 1.5 noloop
    show debris1
    play sound 'audio/Sound/Carnival Scene Sounds/Carla Screaming.mp3' fadein 2.0 volume 0.3
    stop target fadeout 2.0
    $ lipsync(Parents, 'act2', 'audio_58', "Carla!", default_mouth="mouth_fear")
    $ lipsync(Parents, 'act2', 'audio_59', "Please!", default_mouth="mouth_fear")
    hide Parents
    with sshake2
    
    scene black with dissolve
    show bloody_view2
    """
    Your vision blurrs as the blood drains from your body.
    """
    """
    With every ounce of strength you have, you try to fight off the monsters but to no avail.
    """
    jump act31