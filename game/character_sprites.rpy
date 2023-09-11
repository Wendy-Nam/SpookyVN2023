############################# DAD #############################
image dad_eyes_default:
    "images/dad/eyes/eyes_open.png"
    pause 1.0
    "images/dad/eyes/eyes_half.png"
    pause 0.1
    "images/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat

image dad_eyes_red:
    "images/dad/eyes/eyes_red.png"
    pause 3.0
    "images/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat

image dad_eyes_cyring:
    "images/dad/eyes/eyes_cry.png"
    pause 3.0
    "images/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat

image dad_eyes_serious:
    "images/dad/eyes/eyes_serious.png"
    pause 3.0
    "images/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat
    
layeredimage Dad:
    at sprite_highlight('Dad') 
    zoom 0.6
    align (0.5, 1.0)
    always:
        "images/dad/base.png"
    group eyes:
        attribute eye_default default:
            'dad_eyes_default'
        attribute eye_crying:
            'dad_eyes_cyring'
        attribute eye_red:
            'dad_eyes_red'
        attribute eye_serious:
            'dad_eyes_serious'
    group brows:
        attribute brow_default default:
            'images/dad/brows/brow_default.png'
        attribute brow_angry:
            'images/dad/brows/brow_angry.png'
        attribute brow_sad:
            'images/dad/brows/brow_sad.png'
        attribute brow_surprised:
            'images/dad/brows/brow_surprised.png'
    group mouth:
        attribute mouth_sad:
            'images/dad/mouth/mouth_sad.png'
        attribute mouth_A default:
            'images/dad/mouth/mouth_A.png'
        attribute mouth_X:
            'images/dad/mouth/mouth_A.png'
        attribute mouth_B:
            'images/dad/mouth/mouth_B.png'
        attribute mouth_C:
            'images/dad/mouth/mouth_C.png'
        attribute mouth_D:
            'images/dad/mouth/mouth_D.png'
        attribute mouth_E:
            'images/dad/mouth/mouth_E.png'
        attribute mouth_F:
            'images/dad/mouth/mouth_F.png'
        attribute mouth_G:
            'images/dad/mouth/mouth_G.png'
        attribute mouth_H:
            'images/dad/mouth/mouth_H.png'
        attribute mouth_surprised:
            'images/dad/mouth/mouth_surprised.png'
        attribute mouth_fear:
            'images/dad/mouth/mouth_fear.png'
    attribute overlay_blood:
        'images/dad/overlay_blood.png'
    attribute overlay_fear:
        'images/dad/overlay_fear.png'

############################# MOM #############################

image mom_eyes_default:
    "images/mom/eyes/eyes_open.png"
    pause 1.0
    "images/mom/eyes/eyes_half.png"
    pause 0.1
    "images/mom/eyes/eyes_closed.png"
    pause 0.1
    repeat

image mom_eyes_serious:
    "images/mom/eyes/eyes_serious.png"
    pause 3.0
    "images/mom/eyes/eyes_closed.png"
    pause 0.1
    repeat

image mom_eyes_cyring:
    "images/mom/eyes/eyes_cry.png"
    pause 3.0
    "images/mom/eyes/eyes_closed.png"
    pause 0.1
    repeat
    
layeredimage Mom:
    at sprite_highlight('Mom')
    crop (0.34, 0.3, 0.66, 1.0) 
    zoom 0.6
    always:
        "images/mom/base.png"
    group eyes:
        attribute eye_default default:
            'mom_eyes_default'
        attribute eye_crying:
            'mom_eyes_cyring'
        attribute eyes_serious:
            'mom_eyes_serious'
    group brows:
        attribute brow_default default:
            'images/mom/brows/brow_default.png'
        attribute brow_angry:
            'images/mom/brows/brow_angry.png'
        attribute brow_sad:
            'images/mom/brows/brow_sad.png'
        attribute brow_surprised:
            'images/mom/brows/brow_surprised.png'
    group mouth:
        attribute mouth_sad:
            'images/mom/mouth/mouth_sad.png'
        attribute mouth_A default:
            'images/mom/mouth/mouth_A.png'
        attribute mouth_X:
            'images/mom/mouth/mouth_A.png'
        attribute mouth_B:
            'images/mom/mouth/mouth_B.png'
        attribute mouth_C:
            'images/mom/mouth/mouth_C.png'
        attribute mouth_D:
            'images/mom/mouth/mouth_D.png'
        attribute mouth_E:
            'images/mom/mouth/mouth_D.png'
        attribute mouth_F:
            'images/mom/mouth/mouth_F.png'
        attribute mouth_G:
            'images/mom/mouth/mouth_G.png'
        attribute mouth_H:
            'images/mom/mouth/mouth_H.png'
        attribute mouth_sad:
            'images/mom/mouth/mouth_sad.png'
        attribute mouth_fear:
            'images/mom/mouth/mouth_fear.png'
    attribute overlay_blood:
        'images/mom/overlay_blood.png'
    attribute overlay_fear:
        'images/mom/overlay_fear.png'

############################# PARENTS #############################

image parents_eyes_default:
    "images/parents/eyes/eyes_open.png"
    pause 1.0
    "images/parents/eyes/eyes_half.png"
    pause 0.1
    "images/parents/eyes/eyes_closed.png"
    pause 0.1
    repeat

image parents_eyes_serious:
    "images/parents/eyes/eyes_serious.png"
    pause 3.0
    "images/parents/eyes/eyes_closed.png"
    pause 0.1
    repeat

image parents_eyes_cyring:
    "images/parents/eyes/eyes_cry.png"
    pause 3.0
    "images/parents/eyes/eyes_closed.png"
    pause 0.1
    repeat
    
layeredimage Parents:
    at sprite_highlight('Parents')
    zoom 0.6
    always:
        "images/parents/base.png"
    group eyes:
        attribute eye_default default:
            'parents_eyes_default'
        attribute eye_crying:
            'parents_eyes_cyring'
        attribute eyes_serious:
            'parents_eyes_serious'
    group brows:
        attribute brow_default default:
            'images/parents/brows/brow_default.png'
        attribute brow_angry:
            'images/parents/brows/brow_angry.png'
        attribute brow_sad:
            'images/parents/brows/brow_sad.png'
        attribute brow_surprised:
            'images/parents/brows/brow_surprised.png'
    group mouth:
        attribute mouth_sad:
            'images/parents/mouth/mouth_sad.png'
        attribute mouth_A default:
            'images/parents/mouth/mouth_A.png'
        attribute mouth_X:
            'images/parents/mouth/mouth_A.png'
        attribute mouth_B:
            'images/parents/mouth/mouth_B.png'
        attribute mouth_C:
            'images/parents/mouth/mouth_C.png'
        attribute mouth_D:
            'images/parents/mouth/mouth_D.png'
        attribute mouth_E:
            'images/parents/mouth/mouth_D.png'
        attribute mouth_F:
            'images/parents/mouth/mouth_F.png'
        attribute mouth_G:
            'images/parents/mouth/mouth_G.png'
        attribute mouth_H:
            'images/parents/mouth/mouth_H.png'
        attribute mouth_sad:
            'images/parents/mouth/mouth_sad.png'
        attribute mouth_fear:
            'images/parents/mouth/mouth_fear.png'
    attribute overlay_blood:
        'images/parents/overlay_blood.png'
    attribute overlay_fear:
        'images/parents/overlay_fear.png'

############################# Carla #############################

image kid_eyes_default:
    "images/kid/eyes/eyes_default.png"
    pause 1.0
    "images/kid/eyes/eyes_half.png"
    pause 0.1
    "images/kid/eyes/eyes_closed.png"
    pause 0.1
    repeat

image kid_eyes_cyring:
    "images/kid/eyes/eyes_cry.png"
    pause 3.0
    "images/kid/eyes/eyes_closed.png"
    pause 0.1
    repeat
    
layeredimage Carla:
    at sprite_highlight('Carla')
    zoom 0.6
    crop (0.27, 0.35, 0.47, 0.67)
    always:
        "images/kid/base.png" pos (-40, -140)
    group eyes:
        attribute eye_default default:
            'kid_eyes_default'
        attribute eye_crying:
            'kid_eyes_cyring'
    group brows:
        attribute brow_default default:
            'images/kid/brows/brow_default.png'
        attribute brow_angry:
            'images/kid/brows/brow_angry.png'
        attribute brow_angry2:
            'images/kid/brows/brow_angry2.png'
        attribute brow_sad:
            'images/kid/brows/brow_sad.png'
        attribute brow_surprised:
            'images/kid/brows/brow_surprised.png'
    group mouth:
        attribute mouth_A default:
            'images/kid/mouth/mouth_A.png'
        attribute mouth_X:
            'images/kid/mouth/mouth_A.png'
        attribute mouth_B:
            'images/kid/mouth/mouth_B.png'
        attribute mouth_C:
            'images/kid/mouth/mouth_C.png'
        attribute mouth_D:
            'images/kid/mouth/mouth_D.png'
        attribute mouth_E:
            'images/kid/mouth/mouth_D.png'
        attribute mouth_F:
            'images/kid/mouth/mouth_F.png'
        attribute mouth_G:
            'images/kid/mouth/mouth_G.png'
        attribute mouth_H:
            'images/kid/mouth/mouth_H.png'
        attribute mouth_sad:
            'images/kid/mouth/mouth_sad.png'
        attribute mouth_stingy:
            'images/kid/mouth/mouth_stingy.png'
        attribute mouth_fear:
            'images/kid/mouth/mouth_fear.png'
        attribute mouth_angry:
            'images/kid/mouth/mouth_angry.png'
        attribute mouth_angry2:
            'images/kid/mouth/mouth_angry2.png'
    attribute overlay_blood:
        'images/kid/overlay_blood.png'
    attribute overlay_fear:
        'images/kid/overlay_fear.png'
    attribute overlay_dirt:
        'images/kid/overlay_dirt.png'
