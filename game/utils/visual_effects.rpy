
image blink:
    "images/effects/mask_blink_half.png"
    .2
    "images/effects/mask_blink_close.png" 
    .3
    "images/effects/mask_blink_open.png"
    .1
    alpha 0.0

transform carnival_wheel_tint:
    matrixcolor TintMatrix("#fff7af")*SaturationMatrix(1.0000)*ContrastMatrix(1.4074)
    center
transform closed_eye_tint:
    matrixcolor TintMatrix("#221b2b")*SaturationMatrix(1.0000)*ContrastMatrix(2.8426)
    center

image bloody_view1:
    alpha 0.0  # Start with zero transparency
    zoom 5.0
    yalign -0.1
    blend 'multiply'
    .5
    blend 'normal'
    .9
    parallel:
        linear 0.1 alpha 1.0  # Gradually make it visible
        'images/effects/blood1.png'  # Display the blood image
        pause 0.1  # Pause to display the blood
        repeat
    parallel:
        linear 0.5
        zoom 3.5 xalign 0.2 yalign 0.1
        linear 0.4
        zoom 3.8 xalign 0.15 yalign 0.05  # Slightly adjust position and zoom
        linear 0.1
        zoom 4.0 xalign 0.2 yalign 0.1  # Return to the original position and zoom
        repeat
    parallel:
        linear 0.2 alpha 0.0  # Fade out the blood
        repeat
    repeat

image bloody_view2:
    zoom 5.0
    blur 5.0
    alpha 0.5
    'images/effects/blood2.png'
    parallel:
        blur 0.0
        linear 0.5 blur 8.0
        linear 0.2 blur 0.5
        linear 0.2 blur 8.0
        repeat
    parallel:
        linear 0.5
        zoom 3.5 xalign 0.2 yalign 0.1
        repeat
    parallel:
        linear 5.0 alpha 0.0
    repeat



transform jumpAttack:
    linear 0.5 zoom 3.0

transform mom_walk:
    parallel:
        ease 2.5 xalign 2.5 # will take 3 sec to make it to the final pos (center of the screen, in this case)
    parallel:
        ease 2.5 alpha 0.8 # will fade out the character while she's walking
    parallel:
        block:
            ease 0.07 yoffset 10 # will move the character up and down while he's "walking"
            ease 0.21 yoffset 0
            repeat 8 # number of "steps". May be adjusted
        yoffset 0
        
transform dad_walk:
    parallel:
        ease 2.5 xalign 7.0 # will take 3 sec to make it to the final pos (center of the screen, in this case)
    parallel:
        ease 2.5 alpha 0.8 # will fade out the character while he's walking
    parallel:
        block:
            ease 0.07 yoffset 15 # will move the character up and down while he's "walking"
            ease 0.5 yoffset 0
            repeat 5 # number of "steps". May be adjusted
        yoffset 0
        
transform parents_walk:
    parallel:
        ease 5.5 xalign 7.5 # will take 3 sec to make it to the final pos (center of the screen, in this case)
    parallel:
        ease 2.5 alpha 0.9 # will fade out the character while he's walking
    parallel:
        block:
            ease 0.07 yoffset 15 # will move the character up and down while he's "walking"
            ease 0.5 yoffset 0
            repeat 5 # number of "steps". May be adjusted
        yoffset 0
        
transform carla_walk:
    parallel:
        ease 2.5 xalign -0.5 # will take 3 sec to make it to the final pos (center of the screen, in this case)
    parallel:
        ease 1.5 alpha 0.7 # will fade out the character while he's walking
    parallel:
        block:
            ease 0.07 yoffset 10 # will move the character up and down while he's "walking"
            ease 0.5 yoffset 0
            repeat 5 # number of "steps". May be adjusted
        yoffset 0

transform walking:
    yalign 1.1
    parallel:
        ease 3.5 xalign 0.7 # will take 3 sec to make it to the final pos (center of the screen, in this case)
    parallel:
        block:
            ease 0.07 yoffset -5 # will move the character up and down while he's "walking"
            ease 0.5 yoffset 0
            repeat 3 # number of "steps". May be adjusted

transform laugh:
    ease 0.03 yoffset -5 # will move the character up and down while he's "walking"
    ease 0.2 yoffset 0
    repeat 5

transform running:
    yalign 1.1
    parallel:
        ease 0.07 yoffset 10
        ease 0.1 yoffset 0
        repeat
    parallel:
        ease 0.07 xoffset 2
        ease 0.1 xoffset -5
        repeat
    parallel:
        zoom 0.9
        linear 0.3 zoom 1.0
        repeat

transform running2:
    yalign 1.1
    parallel:
        ease 0.07 yoffset -20
        ease 0.1 yoffset 0
        repeat
    parallel:
        zoom 0.9
        linear 0.3 zoom 1.0
        repeat
image monster_ducklings = Snow('images/effects/monster_duckling.png', max_particles=20, speed=100, wind=500, depth=100)

transform monster_ducklings_attack:
    # parallel:
    #     xalign 0.0
    #     linear 0.5 xalign 0.5
    #     repeat
    parallel:
        xalign 1.0
        linear 0.5 xalign 0.0
        linear 0.5 xalign 1.0
        repeat
    parallel:
        zoom 1.0
        linear 0.5 zoom 2.5
        repeat

    