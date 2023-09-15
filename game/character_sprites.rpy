############################# DAD #############################
image dad_eyes_default:
    "images/charactors/dad/eyes/eyes_open.png"
    pause 1.0
    "images/charactors/dad/eyes/eyes_half.png"
    pause 0.1
    "images/charactors/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat

image dad_eyes_red:
    "images/charactors/dad/eyes/eyes_red.png"
    pause 3.0
    "images/charactors/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat

image dad_eyes_cyring:
    "images/charactors/dad/eyes/eyes_cry.png"
    pause 3.0
    "images/charactors/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat

image dad_eyes_serious:
    "images/charactors/dad/eyes/eyes_serious.png"
    pause 3.0
    "images/charactors/dad/eyes/eyes_closed.png"
    pause 0.1
    repeat
    
layeredimage Dad:
    at sprite_highlight('Dad') 
    zoom 0.65
    yoffset -275
    align (0.5, 1.0)
    always:
        "images/charactors/dad/base.png"
    group eyes:
        attribute eye_default default:
            'dad_eyes_default'
        attribute eye_crying:
            'dad_eyes_cyring'
        attribute eye_closed:
            'images/charactors/dad/eyes/eyes_closed.png'
        attribute eye_red:
            'dad_eyes_red'
        attribute eye_serious:
            'dad_eyes_serious'
    group brows:
        attribute brow_default default:
            'images/charactors/dad/brows/brow_default.png'
        attribute brow_angry:
            'images/charactors/dad/brows/brow_angry.png'
        attribute brow_sad:
            'images/charactors/dad/brows/brow_sad.png'
        attribute brow_surprised:
            'images/charactors/dad/brows/brow_surprised.png'
    group mouth:
        attribute mouth_X:
            'images/charactors/dad/mouth/mouth_neutral.png'
        attribute mouth_A default:
            'images/charactors/dad/mouth/mouth_A.png'
        attribute mouth_B:
            'images/charactors/dad/mouth/mouth_B.png'
        attribute mouth_C:
            'images/charactors/dad/mouth/mouth_C.png'
        attribute mouth_D:
            'images/charactors/dad/mouth/mouth_D.png'
        attribute mouth_E:
            'images/charactors/dad/mouth/mouth_E.png'
        attribute mouth_F:
            'images/charactors/dad/mouth/mouth_F.png'
        attribute mouth_G:
            'images/charactors/dad/mouth/mouth_G.png'
        attribute mouth_H:
            'images/charactors/dad/mouth/mouth_H.png'
        attribute mouth_surprised:
            'images/charactors/dad/mouth/mouth_surprised.png'
        attribute mouth_fear:
            'images/charactors/dad/mouth/mouth_fear.png'
        attribute mouth_sad:
            'images/charactors/dad/mouth/mouth_sad.png'
    attribute overlay_blood:
        'images/charactors/dad/overlay_blood.png'
    attribute overlay_fear:
        'images/charactors/dad/overlay_fear.png'

############################# MOM #############################

image mom_eyes_default:
    "images/charactors/mom/eyes/eyes_open.png"
    pause 1.0
    "images/charactors/mom/eyes/eyes_half.png"
    pause 0.1
    "images/charactors/mom/eyes/eyes_closed.png"
    pause 0.1
    repeat

image mom_eyes_serious:
    "images/charactors/mom/eyes/eyes_serious.png"
    pause 3.0
    "images/charactors/mom/eyes/eyes_closed.png"
    pause 0.1
    repeat

image mom_eyes_cyring:
    "images/charactors/mom/eyes/eyes_cry.png"
    pause 3.0
    "images/charactors/mom/eyes/eyes_closed.png"
    pause 0.1
    repeat
    
layeredimage Mom:
    at sprite_highlight('Mom')
    crop (0.34, 0.3, 0.66, 1.0) 
    zoom 0.65
    yoffset -275
    always:
        "images/charactors/mom/base.png"
    group eyes:
        attribute eye_default default:
            'mom_eyes_default'
        attribute eye_crying:
            'mom_eyes_cyring'
        attribute eyes_serious:
            'mom_eyes_serious'
        attribute eye_closed:
            'images/charactors/mom/eyes/eyes_closed.png'
    group brows:
        attribute brow_default default:
            'images/charactors/mom/brows/brow_default.png'
        attribute brow_angry:
            'images/charactors/mom/brows/brow_angry.png'
        attribute brow_sad:
            'images/charactors/mom/brows/brow_sad.png'
        attribute brow_surprised:
            'images/charactors/mom/brows/brow_surprised.png'
    group mouth:
        attribute mouth_sad:
            'images/charactors/mom/mouth/mouth_sad.png'
        attribute mouth_X:
            'images/charactors/mom/mouth/mouth_neutral.png'
        attribute mouth_A default:
            'images/charactors/mom/mouth/mouth_A.png'
        attribute mouth_B:
            'images/charactors/mom/mouth/mouth_B.png'
        attribute mouth_C:
            'images/charactors/mom/mouth/mouth_C.png'
        attribute mouth_D:
            'images/charactors/mom/mouth/mouth_D.png'
        attribute mouth_E:
            'images/charactors/mom/mouth/mouth_D.png'
        attribute mouth_F:
            'images/charactors/mom/mouth/mouth_F.png'
        attribute mouth_G:
            'images/charactors/mom/mouth/mouth_G.png'
        attribute mouth_H:
            'images/charactors/mom/mouth/mouth_H.png'
        attribute mouth_sad:
            'images/charactors/mom/mouth/mouth_sad.png'
        attribute mouth_fear:
            'images/charactors/mom/mouth/mouth_fear.png'
    attribute overlay_blood:
        'images/charactors/mom/overlay_blood.png'
    attribute overlay_fear:
        'images/charactors/mom/overlay_fear.png'

############################# PARENTS #############################

image parents_eyes_default:
    "images/charactors/parents/eyes/eyes_open.png"
    pause 1.0
    "images/charactors/parents/eyes/eyes_half.png"
    pause 0.1
    "images/charactors/parents/eyes/eyes_closed.png"
    pause 0.1
    repeat

image parents_eyes_serious:
    "images/charactors/parents/eyes/eyes_serious.png"
    pause 3.0
    "images/charactors/parents/eyes/eyes_closed.png"
    pause 0.1
    repeat

image parents_eyes_cyring:
    "images/charactors/parents/eyes/eyes_cry.png"
    pause 3.0
    "images/charactors/parents/eyes/eyes_closed.png"
    pause 0.1
    repeat

image parents_fear_overlay_mask:
    zoom 0.65
    yoffset -275
    'images/charactors/parents/overlay_fear.png'

layeredimage Parents:
    at sprite_highlight('Parents')
    zoom 0.65
    yoffset -275
    always:
        "images/charactors/parents/base.png"
    group eyes:
        attribute eye_default default:
            'parents_eyes_default'
        attribute eye_crying:
            'parents_eyes_cyring'
        attribute eyes_serious:
            'parents_eyes_serious'
        attribute eye_closed:
            'images/charactors/parents/eyes/eyes_closed.png'
    group brows:
        attribute brow_default default:
            'images/charactors/parents/brows/brow_default.png'
        attribute brow_angry:
            'images/charactors/parents/brows/brow_angry.png'
        attribute brow_sad:
            'images/charactors/parents/brows/brow_sad.png'
        attribute brow_surprised:
            'images/charactors/parents/brows/brow_surprised.png'
    group mouth:
        attribute mouth_sad:
            'images/charactors/parents/mouth/mouth_sad.png'
        attribute mouth_X:
            'images/charactors/parents/mouth/mouth_neutral.png'
        attribute mouth_A default:
            'images/charactors/parents/mouth/mouth_A.png'
        attribute mouth_B:
            'images/charactors/parents/mouth/mouth_B.png'
        attribute mouth_C:
            'images/charactors/parents/mouth/mouth_C.png'
        attribute mouth_D:
            'images/charactors/parents/mouth/mouth_D.png'
        attribute mouth_E:
            'images/charactors/parents/mouth/mouth_D.png'
        attribute mouth_F:
            'images/charactors/parents/mouth/mouth_F.png'
        attribute mouth_G:
            'images/charactors/parents/mouth/mouth_G.png'
        attribute mouth_H:
            'images/charactors/parents/mouth/mouth_H.png'
        attribute mouth_sad:
            'images/charactors/parents/mouth/mouth_sad.png'
        attribute mouth_fear:
            'images/charactors/parents/mouth/mouth_fear.png'
    attribute overlay_blood:
        'images/charactors/parents/overlay_blood.png'
    attribute overlay_fear:
        'images/charactors/parents/overlay_fear.png'

############################# Carla #############################

image kid_eyes_default:
    "images/charactors/kid/eyes/eyes_default.png"
    pause 1.0
    "images/charactors/kid/eyes/eyes_half.png"
    pause 0.1
    "images/charactors/kid/eyes/eyes_closed.png"
    pause 0.1
    repeat

image kid_eyes_cyring:
    "images/charactors/kid/eyes/eyes_cry.png"
    pause 3.0
    "images/charactors/kid/eyes/eyes_closed.png"
    pause 0.1
    repeat
    
layeredimage Carla:
    at sprite_highlight('Carla')
    zoom 0.65
    yoffset -275
    crop (0.27, 0.35, 0.47, 0.67)
    
    always:
        "images/charactors/kid/base.png" pos (-40, -140)
    group eyes:
        attribute eye_default default:
            'kid_eyes_default'
        attribute eye_crying:
            'kid_eyes_cyring'
    group brows:
        attribute brow_default default:
            'images/charactors/kid/brows/brow_default.png'
        attribute brow_angry:
            'images/charactors/kid/brows/brow_angry.png'
        attribute brow_angry2:
            'images/charactors/kid/brows/brow_angry2.png'
        attribute brow_sad:
            'images/charactors/kid/brows/brow_sad.png'
        attribute brow_surprised:
            'images/charactors/kid/brows/brow_surprised.png'
    group mouth:
        attribute mouth_A default:
            'images/charactors/kid/mouth/mouth_A.png'
        attribute mouth_B:
            'images/charactors/kid/mouth/mouth_B.png'
        attribute mouth_C:
            'images/charactors/kid/mouth/mouth_C.png'
        attribute mouth_D:
            'images/charactors/kid/mouth/mouth_D.png'
        attribute mouth_E:
            'images/charactors/kid/mouth/mouth_neutral.png'
        attribute mouth_F:
            'images/charactors/kid/mouth/mouth_F.png'
        attribute mouth_G:
            'images/charactors/kid/mouth/mouth_G.png'
        attribute mouth_H:
            'images/charactors/kid/mouth/mouth_H.png'
        attribute mouth_sad:
            'images/charactors/kid/mouth/mouth_sad.png'
        attribute mouth_stingy:
            'images/charactors/kid/mouth/mouth_stingy.png'
        attribute mouth_fear:
            'images/charactors/kid/mouth/mouth_fear.png'
        attribute mouth_angry:
            'images/charactors/kid/mouth/mouth_angry.png'
        attribute mouth_angry2:
            'images/charactors/kid/mouth/mouth_angry2.png'
        attribute mouth_X:
            'images/charactors/kid/mouth/mouth_neutral2.png'
    attribute overlay_blood:
        'images/charactors/kid/overlay_blood.png'
    attribute overlay_fear:
        'images/charactors/kid/overlay_fear.png'
    attribute overlay_dirt:
        'images/charactors/kid/overlay_dirt.png'
