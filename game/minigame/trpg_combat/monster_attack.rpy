# survive the underwater minigame (minigame2)

init:
    default player_hp = 100
    default time_left_monsterAttack = 15
    default heart_size = renpy.image_size("images/turnRPG_combat/player_heart.png")
    default heart_scale = 0.8
    default scaled_heart_size = [int(heart_size[0] * heart_scale), int(heart_size[1] * heart_scale)]
    default player_initial_pos = [750, 850] 
    default wall_pos = [500, 500, 500, 500] # (xpos, width, ypos, height)
    default slide_wall = 0
    default slide_direction = None
    default step = 8
    
    transform moving_player_box:
        xpos wall_pos[0]  # Initial xpos from wall_pos
        ypos wall_pos[2]  # Initial ypos from wall_pos
        function move_player_box  # Use the custom Python function
        pause 0.1  # Adjust the pause duration for smoother movement
        repeat

    screen player_box:
        frame pos(wall_pos[0], wall_pos[2]) at moving_player_box:
            minimum (wall_pos[1], wall_pos[3])
            maximum (wall_pos[1], wall_pos[3])
            background "#8c8c8c32"

    screen monster_attack_screen:
        timer 1 repeat True action If (time_left_monsterAttack > 0, true=SetVariable("time_left_monsterAttack", time_left_monsterAttack - 1))
        frame align (0, 0):
            background im.FactorScale("gui/frame.png", 0.4)
            margin (30, 30)
            padding (30, 30)
            hbox:
                spacing 20
                image 'images/turnRPG_combat/clock_icon.png' xalign 0.5 yalign 0.5
                text "Time Left : [time_left_monsterAttack]" size 50 color "#ffffff" xalign 0.5 yalign 0.5
        
        $ bar_val3 = ExtraAnimatedValue(
                    value=player_hp, 
                    range=100, 
                    range_delay=3.0,
                    warper="ease_quart")
        fixed:
                area (1200, 50, 500, 120) # position of the hp-bar 
                bar:
                    value bar_val3
                    left_bar ValueImage(
                        bar_val3,
                        Transform("images/turnRPG_combat/bar/hp_bar_red.png", zoom=0.8),
                        Transform("images/turnRPG_combat/bar/hp_bar_yellow.png", zoom=0.8),
                        Transform("images/turnRPG_combat/bar/hp_bar_green.png", zoom=0.8))
                    right_bar Transform("images/turnRPG_combat/bar/hp_bar_blank.png", zoom=0.8)
                    area (0,0, 800, 150)

                add bar_val3.text(
                    "{0.current_value:.0f} hp",
                    size = 35,
                    color = "#FFF",
                    outlines = [(abs(2), "#000")],
                    bold = True,
                    xcenter = 0.7,
                    ycenter = 0.5)
    
    image player_heart:
        zoom heart_scale
        "images/turnRPG_combat/player_heart.png"

    image bubble:
        'images/underwater_minigame/bubble1.png'
        pause 0.2
        'images/underwater_minigame/bubble2.png'
        pause 0.3
        repeat

    image bomb:
        zoom 1.5
        'images/turnRPG_combat/bomb.png'

    # Moving target transform for target animation
    transform falling_object_monster(target_speed=1.0):
        zoom 1.5
        xpos renpy.random.randint(wall_pos[0], wall_pos[0] + wall_pos[1])  # Random x position within the box
        ypos wall_pos[2]  # Start from the top of the box
        parallel:
            rotate -30 + renpy.random.randint(-10, 10)  # Random rotation angle
            linear 0.5 rotate 30 + renpy.random.randint(-10, 10)  # Random rotation angle
            repeat
        parallel:
            linear target_speed ypos renpy.config.screen_height + 20  # Move objects down to the bottom of the box
        pause 1.0
        # repeat  # Keep the objects looping
        # stop

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
            
init python:
    def move_player(trans, at, st):
        if (trans.xpos is None) or (trans.ypos is None):
            trans.xpos = player_initial_pos[0]
            trans.ypos = player_initial_pos[1]
        #for eve in pygame.event.get():
            # if eve.type==pygame.QUIT:
            #     pygame.quit()
        key_input = pygame.key.get_pressed()
        key_input = pygame.key.get_pressed()  
        if key_input[pygame.K_LEFT]:
            if wall_pos[0] <= (trans.xpos - step) <= wall_pos[0] + wall_pos[1]:
                trans.xpos -= step
        if key_input[pygame.K_UP]:
            if wall_pos[2] <= (trans.ypos - step) <= wall_pos[2] + wall_pos[3]:
                trans.ypos -= step
        if key_input[pygame.K_RIGHT]:
            if wall_pos[0] <= (trans.xpos + step) <= wall_pos[0] + wall_pos[1]:
                trans.xpos += step
        if key_input[pygame.K_DOWN]:
            if wall_pos[2] <= (trans.ypos + step) <= wall_pos[2] + wall_pos[3]:
                trans.ypos += step
        # Check for collisions with walls
        trans.xpos = max(wall_pos[0], min(trans.xpos, wall_pos[0] + wall_pos[1] - scaled_heart_size[0]))
        trans.ypos = max(wall_pos[2], min(trans.ypos, wall_pos[2] + wall_pos[3] - scaled_heart_size[1]))
        return None

    def move_player_box(trans, at, st):
        global wall_pos, slide_wall, slide_direction
        if slide_wall == 0:
            slide_direction = random.choice(["up", "down", "left", "right"])
            slide_wall = 5
        else:
            slide_wall -= 1
        # direction = random.choice(["up", "down", "left", "right"])
        # direction = random.choice(["up", "down", "left", "right"])
        
        step_distance = 25  # Adjust this value as needed
        xpos, width, ypos, height = wall_pos

        # Calculate the target position based on the selected direction
        target_xpos = xpos
        target_ypos = ypos

        if slide_direction == "up":
            target_ypos -= step_distance
        elif slide_direction == "down":
            target_ypos += step_distance
        elif slide_direction == "left":
            target_xpos -= step_distance
        elif slide_direction == "right":
            target_xpos += step_distance

        # Ensure that the box stays within the screen boundaries
        target_xpos = max(0, min(target_xpos, renpy.config.screen_width - width))
        target_ypos = max(0, min(target_ypos, renpy.config.screen_height - height))

        # Calculate the step for linear movement
        num_steps = 25  # Adjust the number of steps for smoother movement
        step_x = int((target_xpos - trans.xpos) / num_steps)
        step_y = int((target_ypos - trans.ypos) / num_steps)

        # Linearly move the box
        for _ in range(num_steps):
            trans.xpos += step_x
            trans.ypos += step_y
            wall_pos = [trans.xpos, width, trans.ypos, height]
            
        # Update the wall_pos variable with the new position
        # wall_pos = [trans.xpos, width, trans.ypos, height]

    # Define the main game class
    class MonsterAttack:
        def __init__(self):
            self.objects = []  # Store falling objects (bubbles and fish)
            self.status = self.Status()
            self.status.is_game_over = False
            self.object_spawn_timer = 0
            self.object_spawn_interval = 0.3  # Adjust this interval as needed
            self.player_pos = At(ImageReference('player_heart'), moving_player_heart)
        
        def round_init(self):
            renpy.show_screen('monster_attack_screen')
            renpy.show_screen('player_box')
            renpy.show('player_heart', what=self.player_pos)

        def round_end(self):
            if self.status.survived:
                narrator("You nearly survived")
            else:
                renpy.scene()
                narrator("You Dided...")
            renpy.hide_screen('monster_attack_screen')
            renpy.hide_screen('player_box')

        def run(self):
            self.round_init()
            while not self.status.is_game_over:
                renpy.pause(0.1)
                self.update()
            self.round_end()

        def update(self):
            self.object_spawn_timer += 0.1  # Increase the timer
            if self.status.is_clear() or self.status.is_fail():
                return
            # Check if it's time to spawn a new object
            if self.object_spawn_timer >= self.object_spawn_interval:
                self.spawn_object()
                self.object_spawn_timer = 0
            for obj in self.objects:
                if obj.hitted or obj.hidden:
                    continue
                obj_ypos = obj.get_pos()[1]
                obj_xpos = obj.get_pos()[0]
                if obj_ypos is None:
                    continue
                # Check if the object is out of bounds and hide it
                if obj_xpos is not None and (obj_xpos < wall_pos[0] or obj_xpos > wall_pos[0] + wall_pos[1]):
                    obj.hidden = True
                    obj.hide()
                if (obj_ypos < wall_pos[2]) or (obj_ypos > wall_pos[2] + wall_pos[3]):
                    obj.hidden = True
                    obj.hide()
                if self.is_hit(obj):
                    # renpy.music.play('audio/Sound/Underwater Scene Sounds/Breath of air.wav', channel='sound', relative_volume=0.5)
                    global player_hp
                    hp_change = obj.handle_collision()
                    player_hp += hp_change

        def is_hit(self, obj):
            player_xpos, player_ypos = self.player_pos.xpos, self.player_pos.ypos
            obj_xpos, obj_ypos = obj.get_pos()
            obj_size = obj.image_size
        
            if obj_xpos is None or obj_ypos is None:
                return False
        
            # Calculate the boundaries of the player and the object
            player_left = player_xpos - scaled_heart_size[0] / 2
            player_right = player_xpos + scaled_heart_size[0] / 2
            player_top = player_ypos
            player_bottom = player_ypos + scaled_heart_size[1]
        
            obj_left = obj_xpos - obj_size[0] / 2
            obj_right = obj_xpos + obj_size[0] / 2
            obj_top = obj_ypos - obj_size[1] / 2
            obj_bottom = obj_ypos + obj_size[1] / 2
        
            # Check for collision
            if (
                player_right >= obj_left
                and player_left <= obj_right
                and player_bottom >= obj_top
                and player_top <= obj_bottom
            ):
                obj.hitted = True
                return True
        
            return False


        def spawn_object(self):
            # Create a new object (either bubble or fish) with random properties
            # object_type = renpy.random.choice(["bubble", "bubble", "bubble", "bubble", "fish"])
            # if object_type == "bubble":
            #     obj = self.Bubble(len(self.objects) + 1)
            # else:
            obj = self.Bomb(len(self.objects) + 1)
            self.objects.append(obj)
            obj.display()
        
        class FallingObject:
            def __init__(self, id):
                self.id = str(id)
                self.hitted = False
                self.hidden = False
                self.target_speed = renpy.random.choice([1.0, 1.5, 2.0])
        
            def display(self):
                renpy.show(name=self.id, what=self.position)

            def get_pos(self):
                return self.position.xpos, self.position.ypos

            def hide(self):
                hitted_position = At(ImageReference(self.image), monster_object_hitted(xpos=self.position.xpos, ypos=self.position.ypos))
                renpy.show(name=str(-int(self.id)), what=hitted_position)
                renpy.hide(self.id)

            def handle_collision(self):
                self.hide()
                return self.hp_change

        class Bubble(FallingObject):
            def __init__(self, id):
                super().__init__(id)
                self.image = 'bubble'
                self.image_path = 'images/underwater_minigame/bubble1.png'
                self.target_scale = 2.0
                self.image_size = [renpy.image_size(self.image_path)[0] * self.target_scale, renpy.image_size(self.image_path)[1] * self.target_scale]
                self.position = At(ImageReference(self.image), falling_object_monster(self.target_speed))
                self.hp_change = 1  # Increase HP when the bubble is hit

        class Bomb(FallingObject):
            def __init__(self, id):
                super().__init__(id)
                self.image = 'bomb'
                self.image_path = 'images/turnRPG_combat/bomb.png'
                self.target_scale = 1.5
                self.image_size = [renpy.image_size(self.image_path)[0] * self.target_scale, renpy.image_size(self.image_path)[1] * self.target_scale]
                self.position = At(ImageReference(self.image), falling_object_monster(self.target_speed))
                self.hp_change = -5 # Decrease HP when the fish is hit

        class Status:
            def __init__(self):
                # self.air_hp = 20  # Starting HP
                # self.max_hp = 50  # Max HP
                # self.time_max = 30  # Time Max
                # self.time_left = 30  # Time left in seconds
                self.is_game_over = False
                self.survived = False

            def is_fail(self):
                if player_hp <= 0:
                    self.is_game_over = True
                    return True
                return False

            def is_clear(self):
                if time_left_monsterAttack <= 0 and player_hp > 0:
                    self.survived = True
                    self.is_game_over = True
                    return True
                return False

label minigame3_monsterAttack_test:
    $ test2 = MonsterAttack()
    # show screen monster_attack_screen
    "Start"
    window hide
    $ test2.run()