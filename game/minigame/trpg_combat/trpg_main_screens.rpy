init:
    # MAIN TRPG SCREEN
    screen trpg_player_menu_board(player):
        frame align (0.7, 0.85):
            background "#ffff0000"
            # background "gui/textbox.png"
            vbox:
                hbox:
                    spacing 50
                    textbutton "{b}Attack{/b}" action [Return()] text_size 50
                    textbutton "{b}Inventory{/b}" action [NullAction()] text_size 50
                    # textbutton "{b}Hp{/b}" action [NullAction(), Show('player_hp_bar', None, player)] text_size 50
                    textbutton "{b}Escape{/b}" action [Show('fooling_msg'), SetVariable('game_escape_pressed_num', game_escape_pressed_num+1), If (game_escape_flag == True, true=Return())] text_size 50
        timer 1 repeat True action If (game_escape_flag == True, true=Return())

    screen trpg_game_board(game, player, monster):
        if game.attack_started:
            use attack_timer(game.current_turn)
        if (game.attack_started and game.current_turn == "Player"):
            use trpg_hp_bar(monster, name="monster")
        elif (game.attack_started and game.current_turn == "Monster"):
            use trpg_hp_bar(player, name="player")
        else:
            use trpg_hp_bar(monster, name="monster")
            use trpg_hp_bar(player, name="player")


    screen attack_timer(turn):
        frame align (0, 0):
            background im.FactorScale("images/turnRPG_combat/timer.png", 0.7)
            margin (30, 50)
            padding (125, 55)
            if turn == "Player":
                timer 1 repeat True action [If (player_attack_timeleft > 0, true=SetVariable("player_attack_timeleft", player_attack_timeleft - 1))]
                text "Time Left : [player_attack_timeleft]" size 40 color "#ffffff"
            elif turn == "Monster":
                timer 1 repeat True action If (monsterAttack_timeleft > 0, true=SetVariable("monsterAttack_timeleft", monsterAttack_timeleft - 1))
                text "Time Left : [monsterAttack_timeleft]" size 40 color "#ffffff"
                
    screen trpg_hp_bar(character, name):
        zorder 50
        $ hp = ExtraAnimatedValue(
                    value=character.hp, 
                    range=character.max_hp, 
                    range_delay=3.5,
                    warper="easein_bounce")
        if name is "player":
            textbutton "{bt=3}{size=30}{color=#FF0000}{i}{b}Exit{/b}{/i}{/color}{/size}{/bt}" action [SetVariable('game_escape_flag', True), Return()] xpos 200 ypos 880
        fixed:
            if name is "monster":
                area (1200, 50, 800, 120)
            if name is "player":
                area (100, 800, 800, 120) # position of the hp-bar
            bar:
                value hp
                left_bar ValueImage(
                    hp,
                    "images/turnRPG_combat/bar/hp_bar_red.png",
                    "images/turnRPG_combat/bar/hp_bar_yellow.png",
                    "images/turnRPG_combat/bar/hp_bar_green.png")
                right_bar "images/turnRPG_combat/bar/hp_bar_blank.png"
                area (0,0, 600, 200)
            add hp.text(
                "{0.current_value:.0f} hp ({1})".format(hp, name),
                size = 35,
                color = "#FFF",
                outlines = [(abs(2), "#000")],
                bold = True,
                xcenter = 0.35,
                ycenter = 0.75)
                
    transform fooling_msg_trans:
        alpha 1.0
        align (0.5, 0.5)
        linear 3.0 alpha 0.0

    screen fooling_msg:
        if game_escape_pressed_num == 0:
            text "{sc=5}{bt=1}{size=+50}Do you think you can escape from this game? LOL{/size}{/bt}{/sc}" at fooling_msg_trans
        elif game_escape_pressed_num == 1:
            text "{sc=5}{bt=1}{size=+50}This button is {i}{b}fake{/b}{/i}.{/size}{/bt}{/sc}" at fooling_msg_trans
        else:
            text "{sc=5}{bt=1}{size=+50}Find the {color=#FF0000}{b}Real{/b}{/color} Button!{/size}{/bt}{/sc}" at fooling_msg_trans
    
    # Player Attack Screens
    
    screen attack_box(P1):   
        # background "images/turnRPG_combat/fight_slider.png"
        $ hit_zone_nb = len(P1.hit_zone)
        $ style_list = ["green", "yellow", "red", 'yellow', 'green']
       
        for i in range(hit_zone_nb):
            vbar:
                style 'hit_zone_'+style_list[i]
                area(P1.hit_zone[i][0], 500, P1.hit_zone[i][1], 500) 
            $ damage_size = P1.damage_list[i]
            text "[damage_size]" size 50 color "#ffffff" area (P1.hit_zone[i][0], 500, P1.hit_zone[i][1], 400) offset (100, 20)
    
    screen attack_timing_bar(P1):
        key ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'mouseup_1'] :
            action Return(True)
        timer 1 repeat True action If(player_attack_timeleft > 0, false=Return(False))

    # Monster Attack Screens
    
    screen player_box:
        frame pos(BOX[0], BOX[2]) at moving_player_box:
            minimum (BOX[1], BOX[3])
            maximum (BOX[1], BOX[3])
            background 'images/turnRPG_combat/box.png'

init -5 python:
    #custom bar -----------------------
    style.hit_zone_red = Style(style.default)
    style.hit_zone_red.left_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_red.png", 0, 0)
    style.hit_zone_red.right_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_red.png", 0, 0)
    style.hit_zone_red.hover_left_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_red.png", 0, 0)
    
    style.hit_zone_yellow = Style(style.default)
    style.hit_zone_yellow.left_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_yellow.png", 0, 0)
    style.hit_zone_yellow.right_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_yellow.png", 0, 0)
    style.hit_zone_yellow.hover_left_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_yellow.png", 0, 0)
    
    style.hit_zone_green = Style(style.default)
    style.hit_zone_green.left_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_green.png", 0, 0)
    style.hit_zone_green.right_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_green.png", 0, 0)
    style.hit_zone_green.hover_left_bar = Frame("images/turnRPG_combat/hit_zone/hit_zone_green.png", 0, 0)
    
    # style.hit_zone.right_bar = Frame("bar_empty.png", 0, 0)
    # style.hit_zone.hover_left_bar = Frame("bar_hover.png", 0, 0)