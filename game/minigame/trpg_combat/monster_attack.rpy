# survive the underwater minigame (minigame2)

init:
    define BOX_START_POS = [500, 500, 500, 500]
    define PLAYER_START_POS = [750, 850]
    define heart_scale = 0.8
    define heart_size = renpy.image_size("images/turnRPG_combat/life.png")
    define scaled_heart_size = [int(heart_size[0] * heart_scale), int(heart_size[1] * heart_scale)]
    define PLAYER_STEP = 8
    define BOX_STEP = 25
    define BOX_STEP_NUM = 25 # Adjust the number of steps for smoother box movement
    
    default monsterAttack_timeleft = 15
    default player_initial_pos = PLAYER_START_POS
    default BOX = BOX_START_POS # (xpos, width, ypos, height)
    default slide_wall = 0
    default slide_direction = None
    
    transform moving_player_box:
        xpos BOX[0]  # Initial xpos from BOX
        ypos BOX[2]  # Initial ypos from BOX
        function move_player_box  # Use the custom Python function
        pause 0.1  # Adjust the pause duration for smoother movement
        repeat
        
    image player_heart:
        zoom heart_scale
        "images/turnRPG_combat/life.png"

    image bomb:
        zoom 1.5
        'images/turnRPG_combat/bomb.png'

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
            
init python:
    def move_player(trans, at, st):
        if (trans.xpos is None) or (trans.ypos is None):
            trans.xpos = player_initial_pos[0]
            trans.ypos = player_initial_pos[1]
        key_input = pygame.key.get_pressed()
        key_input = pygame.key.get_pressed()  
        if key_input[pygame.K_LEFT]:
            if BOX[0] <= (trans.xpos - PLAYER_STEP) <= BOX[0] + BOX[1]:
                trans.xpos -= PLAYER_STEP
        if key_input[pygame.K_UP]:
            if BOX[2] <= (trans.ypos - PLAYER_STEP) <= BOX[2] + BOX[3]:
                trans.ypos -= PLAYER_STEP
        if key_input[pygame.K_RIGHT]:
            if BOX[0] <= (trans.xpos + PLAYER_STEP) <= BOX[0] + BOX[1]:
                trans.xpos += PLAYER_STEP
        if key_input[pygame.K_DOWN]:
            if BOX[2] <= (trans.ypos + PLAYER_STEP) <= BOX[2] + BOX[3]:
                trans.ypos += PLAYER_STEP
        # Check for collisions with walls
        trans.xpos = max(BOX[0], min(trans.xpos, BOX[0] + BOX[1] - scaled_heart_size[0]))
        trans.ypos = max(BOX[2], min(trans.ypos, BOX[2] + BOX[3] - scaled_heart_size[1]))
        return None

    def move_player_box(trans, at, st):
        global BOX, slide_wall, slide_direction
        if slide_wall == 0:
            slide_direction = random.choice(["up", "down", "left", "right"])
            slide_wall = 5
        else:
            slide_wall -= 1
        xpos, width, ypos, height = BOX

        # Calculate the target position based on the selected direction
        target_xpos = xpos
        target_ypos = ypos

        if slide_direction == "up":
            target_ypos -= BOX_STEP
        elif slide_direction == "down":
            target_ypos += BOX_STEP
        elif slide_direction == "left":
            target_xpos -= BOX_STEP
        elif slide_direction == "right":
            target_xpos += BOX_STEP

        # Ensure that the box stays within the screen boundaries
        target_xpos = max(0, min(target_xpos, renpy.config.screen_width - width))
        target_ypos = max(0, min(target_ypos, renpy.config.screen_height - height))

        # Calculate the step for linear movement
        BOX_STEP_NUM = 25  # Adjust the number of steps for smoother movement
        step_x = int((target_xpos - trans.xpos) / BOX_STEP_NUM)
        step_y = int((target_ypos - trans.ypos) / BOX_STEP_NUM)

        # Linearly move the box
        for _ in range(BOX_STEP_NUM):
            trans.xpos += step_x
            trans.ypos += step_y
            BOX = [trans.xpos, width, trans.ypos, height] # Update the global box position

    # Define the main game class
    class MonsterAttack:
        def __init__(self):
            self.objects = []  # Store falling objects (bubbles and fish)
            self.status = self.Status()
            self.status.is_game_over = False
            self.object_spawn_timer = 0
            self.object_spawn_interval = 0.3  # Adjust this interval as needed
            self.player_pos = At(ImageReference('player_heart'), moving_player_heart)
        
        def round_init(self, player):
            global monsterAttack_timeleft, player_initial_pos, BOX, slide_direction, slide_wall
            monsterAttack_timeleft = 15
            player_initial_pos = PLAYER_START_POS
            BOX = BOX_START_POS # (xpos, width, ypos, height)
            slide_direction = None
            slide_wall = 0
            self.status.player = player
            self.status.is_game_over = False
            self.status.survived = False
            renpy.show('player_heart', what=self.player_pos)
            renpy.show_screen('player_box')

        def round_end(self):
            if self.status.survived:
                narrator("You nearly survived")
            else:
                # renpy.scene('bg minigame3')
                narrator("You Dided...")
            renpy.hide('player_heart')
            renpy.hide_screen('player_box')
            renpy.scene()
            renpy.show('bg minigame3')

        def run(self, player_hp):
            self.round_init(player_hp)
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
                if obj_xpos is not None and (obj_xpos < BOX[0] or obj_xpos > BOX[0] + BOX[1]):
                    obj.hidden = True
                    obj.hide()
                if (obj_ypos < BOX[2]) or (obj_ypos > BOX[2] + BOX[3]):
                    obj.hidden = True
                    obj.hide()
                if self.is_hit(obj):
                    # renpy.music.play('audio/Sound/Underwater Scene Sounds/Breath of air.wav', channel='sound', relative_volume=0.5)
                    # global player_hp
                    hp_change = obj.handle_collision()
                    self.status.player.hp += hp_change

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
            #     obj = self.Item(len(self.objects) + 1)
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

        class Item(FallingObject):
            def __init__(self, id):
                super().__init__(id)
                self.image = 'item'
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
                self.player = None

            def is_fail(self):
                if self.player.hp <= 0:
                    self.is_game_over = True
                    return True
                return False

            def is_clear(self):
                if monsterAttack_timeleft <= 0 and self.player.hp > 0:
                    self.survived = True
                    self.is_game_over = True
                    return True
                return False
