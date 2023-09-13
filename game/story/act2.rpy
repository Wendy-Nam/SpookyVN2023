
label when_you_lose:
    
    show Carla brow_surprised eye_default mouth_C
    
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
    
    show Mom brow_default eyes_serious mouth_H
    show Dad brow_angry eye_default mouth_X
    $ lipsync(Mom, 'act2', 'audio_2', "Excuse me missy, I don't remember teaching you to be this sassy.")
    
    "your tone noticably forces a shift in the conversation."
    
    show Carla mouth_stingy
    $ lipsync(Carla, 'act2', 'audio_3', "You didn't.", 'mouth_stingy')

    "The targets from the minigame face towards you and you feel the rate of your heart beat rise."
    
    show Dad mouth_sad eye_default brow_surprised
    show Mom mouth_sad eye_default brow_surprised
    
    $ lipsync(Dad, 'act2', 'audio_4', "Carls, what are you doing?", default_mouth="mouth_surprised")
    
    hide Dad
    hide Mom

    show Parents eye_default brow_surprised mouth_fear overlay_fear
    show Carla brow_angry eye_crying mouth_angry overlay_fear
    """
    Carla screams at you and the shooting gallery begins to shudder.
    
    Before you can let out your next words, the targets leap out at you.
    
    Their endless numbers overwhelm you as you feel teeth sinking into your flesh. 
    """
    show Parents overlay_blood
    jump act26

label when_you_win:
    
    show Dad brow_default eye_default mouth_D
    
    """
    With a smug grin you rest the pistol on the game stand and look at Carla.
    
    Full of anger, Carla congratulates you.
    """
    
    $ lipsync(Carla, 'act2', 'audio_5', "G-good job.")
    
    show Carla brow_angry2 mouth_angry
    
    "she speaks softly, taking you aback."

    hide Mom
    hide Dad
    
    $ lipsync(Parents, 'act2', 'audio_6', "Carls?")
    
    hide Parents with dissolve
    show Dad
    show Mom
    
    $ lipsync(Carla, 'act2', 'audio_7', "You beat my score...", 'mouth_angry')
    
    $ lipsync(Dad, 'act2', 'audio_8', "Hey, hey.", 'mouth_sad')
    $ lipsync(Dad, 'act2', 'audio_9', "It's alright, it's a game.")
    $ lipsync(Dad, 'act2', 'audio_10', "You can beat my score on your turn Carls.")
    
    $ lipsync(Carla, 'act2', 'audio_11', "It's not just a game, it's my game.", 'mouth_sad')
    $ lipsync(Carla, 'act2', 'audio_12', "You weren't supposed to beat it.", 'mouth_stingy')

    "Carla's eyes shift towards the floor for a few seconds and she looks back at you with a sinister smile."
    
    $ lipsync(Carla, 'act2', 'audio_13', "You want to play again?")

    menu:
        "Play the game again.":
            jump act25c
        "Carls, we should be going to bed now. I think the game is over.":
            jump act25b


label act21:
    hide Carla with dissolve
    show Parents eye_closed
    """
    You can hear candy wrappers being moved and Carla shuffling around while you begin humming a tune to yourself.
    
    After a brief moment you realize you don't hear Carla moving, but feel a breeze of the wind against your face.
    
    Unsure of what's happening, you ask.
    """
    hide Parents
    
    show Dad eye_closed brow_surprised mouth_fear
    show Mom eye_closed brow_surprised mouth_fear
    
    $ lipsync(Dad, 'act2', 'audio_14', "D-did you just open the window?")
    
    show Dad mouth_surprised
    show Carla brow_angry2 mouth_angry2 at left
    
    $ lipsync(Carla, 'act2', 'audio_15', "No!")
    
    show Carla mouth_angry2
    
    $ lipsync(Carla, 'act2', 'audio_16', "Keep your eyes closed until I say it's ok to open them please...")
    
    show Carla mouth_angry2
    show Dad mouth_sad
    
    "Carla insists."
    
    hide Carla with dissolve
    
    show Mom mouth_sad
    
    """
    Going against your better judgement, you keep your eyes shut.
    
    You take a deep breath and begin smelling... food.
    
    Specifially popcorn and churros.
    
    The smell catches you off guard, but since nothing is burning, you trust Carla with the set up.
    
    You continue to hum your tune, patiently waiting for Carla to finish.
    
    You notice that there is music similar to your hum.
    
    To double check, you stop and realize that there //is// music playing in the background. 
    
    Troubled, you start to speak up.
    """
    
    show Dad mouth_C
    
    """
    Before saying anything, Carla finally breaks her silence.
    """
    
    show Dad mouth_sad
    show Carla at left
    
    $ lipsync(Carla, 'act2', 'audio_17', "Ok.")
    $ lipsync(Carla, 'act2', 'audio_18', "You can open your eyes now.")

    scene bg carnival
    show blink
    show Parents eye_default brow_surprised mouth_fear
    
    """
    from your left, Carla's voice breaks through the tune you've been listening to.
    
    Nervously, you open your eyes and find that the set up was not what you expected at all.
    
    To your shock, you're sitting on a ferris wheel overlooking a carnival.
    """
    show Parents overlay_fear
    """
    The height frightens you, causing you to hold on to Carla.
    
    In a panicked voice, you question her.
    """
    
    $ lipsync(Parents, 'act2', 'audio_19', "C-Carla!")
    hide Parents
    show Dad brow_surprised eye_default mouth_fear overlay_fear
    show Mom brow_surprised eyes_serious mouth_fear overlay_fear
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
    
    The ferris wheel makes its descent and you take a moment to take in the sight.
    
    You press Carla for answers.
    """
    
    menu:
        "This isn't funny. What did you do?":
            jump act22a
        "Wow... this is amazing. How did you do this?":
            jump act22b

label act22a:
    
    $ lipsync(Carla, 'act2', 'audio_22', "It's //Story Time// isn't it?")
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
    show Mom brow_surprised eyes_serious mouth_fear
    
    "You interrupt Carla out of instinct."
    
    $ lipsync(Mom, 'act2', 'audio_27', "Carls, please no monsters.")
    $ lipsync(Mom, 'act2', 'audio_28', "I had plenty of those to deal with tonight.")
    
    
    $ lipsync(Carla, 'act2', 'audio_29', "They were fake though!")
    $ lipsync(Carla, 'act2', 'audio_30', "It won't be violent, I promise.")
    
    "You give Carla a stern look and she concedes."
    
    show Dad brow_default
    $ lipsync(Dad, 'act2', 'audio_31', "Fine, but just wait till you see what at the bottom.")
    
    jump act23

label act22b:
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
    $ lipsync(Carla, 'act2', 'audio_37', "//Story Time// is gonna be amazing.")
    show Carla eye_default mouth_B
    
    $ lipsync(Mom, 'act2', 'audio_38', "Excuse me?")
    show Mom brow_surprised eyes_serious mouth_H
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
    your efforts to reach out to her are futile and you step off the ferris wheel.
    
    You begin to look for Carla.
    
    Your first instinct takes you to some food carts parked in front of a tent.
    
    Oddly enough, there is no one available to serve you.
    
    Knowing you have to focus on finding Carla, you only have time to look at one cart.
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
    The aroma of churros hovers over the cart. Curiosity gets the better of you, causing you to peek into the cart.
    
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
    show Dad brow_surprised
    show Mom brow_surprised

    """
    You pass the food cart and hear Carla cheering for excitement followed by what sounds like a game with sound effects.
    
    Following the source, you reach Carla, who seems to be playing a minigame involving a gun and some targets.
    
    Carla skillfully shoots at the targets and finishes the game as you approach.
    
    As you get closer, the targets appear to be looking at you for a brief moment.
    """
    
    show Mom brow_surprised eye_default mouth_C
    
    $ lipsync(Mom, 'act2', 'audio_45', "Ohh fun!")
    $ lipsync(Mom, 'act2', 'audio_46', "I remember a game like this when I was a kid.")
    
    show Mom mouth_C
    show Dad mouth_C
    """
    your smile beams while you observe the targets and the gun.
    
    Carla puts the gun down and cheerfully tells you her accomplishments.
    """
    
    show Carla brow_default eye_default mouth_E at left
    
    $ lipsync(Carla, 'act2', 'audio_47', "I got the high score, I bet you can't beat me.")
    
    """
    she points at the game and motions you to play.
    
    You look at Carla's smile and back at the game.
    
    The excitement of what Carla has created during this //Story Time// has worn off, but you don't want to disappoint her.
    """
    show Dad eye_default brow_default mouth_X
    show Mom eye_default brow_default mouth_X
    # <!--(FIRST MAJOR CHOICE)-->
    
    menu:
        "Ok missy, one game only.":
            jump act25a
        "Carls, we should be going to bed now. I think the game is over.":
            jump act25b

label act24d:
    """
    You grab some popcorn and begin eating it.
    
    After a few scoops, you realize that there is no taste and you don't feel yourself getting full from eating it.
    """
    
    show Dad brow_sad eye_default mouth_sad
    show Mom brow_sad eye_default mouth_sad
    $ lipsync(Dad, 'act2', 'audio_48', "Ugh, c'mon Carls, you make all of this, but I can't have any popcorn?")

    "Annoyed, you continue your search."
    
    jump act24c

label act25a:
    "You pick up the toy pistol and play the game."
    
    menu:
        "When you win":
            jump when_you_win
        "When you lose":
            jump when_you_lose

label act25b:
    $ lipsync(Carla, 'act2', 'audio_49', "I set all of this up and it's already over?")
    show Carla brow_sad eye_default mouth_stingy overlay_fear
    
    "Carla's frustration begins to show."
    
    $ lipsync(Dad, 'act2', 'audio_50', "What you did here is amazing, but it's late Carls.")
    show Dad brow_sad eye_serious mouth_sad
    
    "you try to appease Carla, but fail."
    
    $ lipsync(Carla, 'act2', 'audio_51', "We barely even started!")
    show Carla brow_angry2 eye_default mouth_angry2    
    "Carla's voice cracks"
    
    $ lipsync(Carla, 'act2', 'audio_52', "It's not fair.")
    
    show Mom brow_angry eyes_serious mouth_C
    "You sternly answer"
    
    $ lipsync(Mom, 'act2', 'audio_53', "Excuse me?")
    $ lipsync(Mom, 'act2', 'audio_54', "That's enough.")
    $ lipsync(Mom, 'act2', 'audio_55', "We're going to put all of...")
    $ lipsync(Mom, 'act2', 'audio_56', "Whatever this is away and it'll be bed time.")
    show Carla brow_angry eye_default mouth_angry
    """
    Carla angrily looks at you.
    
    Her eyes begin to water and she begins to scream.
    """
    show Carla brow_angry eye_crying mouth_angry overlay_fear
    """
    The environment begins to shake and you notice the targets from the minigame have morphed into disfigured versions of their previous incarnation.
    """
    hide Mom
    hide Dad
    show Parents mouth_fear overlay_fear eye_default brow_surprised
    """
    The decaying situation raises your heart rate again and you begin yelling back at Carla to stop.
    """
    
    $ lipsync(Parents, 'act2', 'audio_57', "Stop!")

    """
    Carla's scream continues and the targets face you again.
    
    Before you can act, they begin jumping at you until you're overwhelmed.
    
    The abominations begin gnawing at your body as you cry out in agony.
    """
    show Parents overlay_blood
    jump act26

label act25c:
    "You play the game again, but its difficulty has shot up exponentially and you fail the game."
    
    jump when_you_lose

label act26:
    $ lipsync(Parents, 'act2', 'audio_58', "Carla!", default_mouth="mouth_fear")
    $ lipsync(Parents, 'act2', 'audio_59', "Please!", default_mouth="mouth_fear")
    
    scene black with dissolve
    """
    Your vision blurrs as the blood drains from your body.
    
    With every ounce of strength you have, you try to fight off the monsters but to no avail.
    """
    
    jump act31