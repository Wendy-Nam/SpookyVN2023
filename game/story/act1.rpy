label act11:
    """
    You and your child, Carla, walk into your home on Halloween night after a successful Trick or Treat adventure.
    
    She excitedly sets her full bucket of candy down and begins taking out empty candy wrappers.
    
    After a few moments, she stops to ask you a question.
    """
    
    $ lipsync(Carla, 'act1', "audio_0", "Why do people leave 'Take One Only' signs in front of their door?")
    $ lipsync(Carla, 'act1', "audio_1", "It makes me want to take more than that?")

    "Carla finishes taking out the wrappers and holds them up towards you."
    
    $ lipsync(Mom, 'act1', "audio_2", "Good thing I was there so you wouldn't take more than one.")
    
    "you chuckle to yourself as you take the empty candy wrappers Carla has collected."
    
    $ lipsync(Carla, 'act1', "audio_3", "Hehe that's what you think..")
    
    "she slyly retorts."

    $ lipsync(Dad, 'act1', "audio_4", "Excuse me?")
    
    """
    Carla realizes her mistake and ignores your question by pretending to put her bucket of candy away.
    
    You yawn loudly, which catches her attention and you begin to explain your next move
    """
    
    $ lipsync(Dad, 'act1', "audio_5", "Well!")
    $ lipsync(Dad, 'act1', "audio_6", "After all that walking we did, I think it's time to start getting ready for bed, Carls.")
    $ lipsync(Carla, 'act1', "audio_7", "What??")
    
    """
    Carla frowns as you begin taking off your costume.
    
    The frown turns into a devious smile as she starts to bargain.
    """
    
    $ lipsync(Carla, 'act1', "audio_8", "Can I at least have one of the king size candy bars?")
    
    "Amused with her request, you stop taking off your costume and begin the negotiation."
    
    
    $ lipsync(Mom, 'act1', "audio_9", "Definitely not missy.")
    $ lipsync(Mom, 'act1', "audio_10", "Besides, you ate a lot of your candy on the way home //after// I told you not to.")
    $ lipsync(Dad, 'act1', "audio_11", "Half of one?")
    
    "Carla widens her eyes to imitate a puppy face but you remain steadfast."
    
    $ lipsync(Mom, 'act1', "audio_12", "Nope, no king size candy bars, no regular candy bars, or any candy for the rest of the night.")
    
    "Carla holds her puppy face and you continue."
    
    $ lipsync(Dad, 'act1', "audio_13", "You'll be able to have more candy tomorrow ok?")
    $ lipsync(Dad, 'act1', "audio_14", "At least let me wait until next week to bring you to the dentist.")
        
    $ lipsync(Carla, 'act1', "audio_15", "Ew, nevermind.")
    
    "Carla stops her puppy face."
    
    $ lipsync(Carla, 'act1', "audio_16", "No dentist for me.")
        
    $ lipsync(Dad, 'act1', "audio_17", "No dentist for me.")
    $ lipsync(Dad, 'act1', "audio_18", "Now c'mon, lets get you changed out of that scary costume.")
    
    "With a sigh of relief, you begin to head to Carla's room until she stops you."
    
    jump act12

label act12:

    $ lipsync(Carla, 'act1', "audio_19", "Can we at least do one thing?")
    $ lipsync(Carla, 'act1', "audio_20", "Please?")
    
    """
    she asks politely.
    
    You stop in your tracks and turn around.
    """
    
    $ lipsync(Mom, 'act1', "audio_21", "What is it Carls?")
        
    $ lipsync(Carla, 'act1', "audio_22", "I know it's late but...")
    $ lipsync(Carla, 'act1', "audio_23", "can we at least play //Story Time// before we go to sleep?")
    
    """
    Carla refrains from using her puppy face.
    She sincerely looks at you.
    """
    
    menu:
        "You have school tomorrow, we can't.":
            jump act13a
        "Fine. On one condition.":
            jump act13b

label act13b:
    "Carla excitedly jumps up and down after your initial agreement."
    
    $ lipsync(Mom, 'act1', "audio_24", "You do the set up //and// the clean up.")
    
    "you give Carla a devious smile of your own."
    
    $ lipsync(Carla, 'act1', "audio_25", "Deal, but you have do let me set up with your eyes closed.")
    
    "Carla smiles widely and gets ready to gather her materials."
    
    $ lipsync(Dad, 'act1', "audio_26", "Ok.")
    $ lipsync(Dad, 'act1', "audio_27", "Nothing too messy, please Carls?")
    
    jump act21

label act13a:

    $ lipsync(Carla, 'act1', "audio_28", "But we're practically in costume already...")
    $ lipsync(Carla, 'act1', "audio_29", "That's like half of the work!")

    "Carla's voice breaks with a bit of desperation."
    
    $ lipsync(Dad, 'act1', "audio_30", "It was so much work getting it on though...")
        
    $ lipsync(Carla, 'act1', "audio_31", "Just one story.")
    $ lipsync(Carla, 'act1', "audio_32", "I promise?")
    $ lipsync(Carla, 'act1', "audio_33", "I won't sneak any of my candy to my room?")
        
    $ lipsync(Mom, 'act1', "audio_34", "Excuse me?")
    $ lipsync(Carla, 'act1', "audio_35", "I promise I won't sneak any of my candy to my room.")
    $ lipsync(Dad, 'act1', "audio_36", "You shouldn't be doing that in the first place.")
    
    "After seeing Carla try to spend more time with you. you to break."
    
    jump act13b
