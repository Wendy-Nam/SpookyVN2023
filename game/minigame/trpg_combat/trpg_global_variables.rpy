init -1:
    default game_escape_flag = False
    default game_escape_pressed_num = 0
    default player_attack_timeleft = 15
    default monsterAttack_timeleft = 15
    default player_initial_pos = PLAYER_START_POS
    default BOX = BOX_START_POS # (xpos, width, ypos, height)
    default slide_wall = 0
    default slide_direction = None
    default damaged_heart = False
    default damaged_heart_blink = HEART_BLINK_NB
    default damaged_monster = False

    ## For the Monster Attack
    define BOX_START_POS = [500, 500, 500, 500]
    define PLAYER_START_POS = [750, 850]
    define heart_scale = 0.8
    define heart_size = renpy.image_size("images/turnRPG_combat/life.png")
    define scaled_heart_size = [int(heart_size[0] * heart_scale), int(heart_size[1] * heart_scale)]
    define PLAYER_STEP = 8
    define BOX_STEP = 25
    define BOX_STEP_NUM = 25 # Adjust the number of steps for smoother box movement
    define HEART_BLINK_NB = 50
    
    image stick = "images/turnRPG_combat/stick.png"
    image bg minigame3 = "images/turnRPG_combat/bg minigame3.png"
    image player_heart:
        zoom heart_scale
        "images/turnRPG_combat/life.png"
    image bomb:
        zoom 1.5
        'images/turnRPG_combat/bomb.png'
    
    # Moving weapon transform for weapon animation
    transform moving_timing_bar: 
        yalign 0.8
        xpos 100
        linear 0.1 xpos 500
        linear 0.1 xpos 700
        linear 0.1 xpos 1000
        linear 0.1 xpos 1200
        linear 0.1 xpos 1600
        linear 0.1 xpos 1200
        linear 0.1 xpos 1000
        linear 0.1 xpos 700
        linear 0.1 xpos 500
        linear 0.1 xpos 100
        repeat
    
    transform moving_player_box:
        xpos BOX[0]  # Initial xpos from BOX
        ypos BOX[2]  # Initial ypos from BOX
        function move_player_box  # Use the custom Python function
        pause 0.1  # Adjust the pause duration for smoother movement
        repeat

    # Moving target transform for target animation
    transform falling_object_monster(target_speed=1.0):
        zoom 1.5
        xpos renpy.random.randint(BOX[0], BOX[0] + BOX[1])  # Random x position within the box
        ypos BOX[2]  # Start from the top of the box
        parallel:
            rotate -30 + renpy.random.randint(-10, 10)  # Random rotation angle
            linear 0.5 rotate 30 + renpy.random.randint(-10, 10)  # Random rotation angle
            repeat
        parallel:
            linear target_speed ypos renpy.config.screen_height + 20  # Move objects down to the bottom of the box
        pause 1.0

    transform monster_object_hitted(xpos, ypos):
        pos (xpos, ypos)
        parallel:
            zoom 2.0
            linear 0.3 zoom 2.5
            linear 0.2 zoom 0.5
        parallel:
            linear 0.5 alpha 0.0

    transform moving_player_heart:
        function move_player
        pause 0.01
        repeat