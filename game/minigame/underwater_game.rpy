# survive the underwater minigame (minigame2)

init:
    screen hp_bar:
        $ air_hp = ExtraAnimatedValue(
                        value=minigame2.status.air_hp, 
                        range=minigame2.status.max_hp * 2, 
                        range_delay=3.0,
                        warper="easein_elastic")
        frame align (0.0, 0.0):
            background "#4f5a6600" 
            padding(50, 25)
            timer 1 repeat True action If(minigame2.status.time_left > 0 and minigame2.status.is_game_over == False, true=[SetVariable('minigame2.status.time_left', minigame2.status.time_left - 1), SetVariable('minigame2.status.air_hp', minigame2.status.air_hp - 1)])
            text "Time Left: [minigame2.status.time_left]" size 50 yoffset 45
        frame align (1.4, 0.0):
            margin (50, 50)
            xmaximum 1000
            background 'tank'
            padding (120, 45)
            bar:
                value air_hp
                left_bar ValueImage(
                    air_hp,
                    'bar_full',
                    'bar_full')
                right_bar 'bar_empty'

            add air_hp.text(
                "{0.current_value:.0f} hp",
                size=30,
                color="#FFF",
                outlines=[(abs(2), "#000")],
                bold=True,
                xcenter=0.25,
                ycenter=0.02)

    default nose_size = renpy.image_size("images/underwater_minigame/nose.png")
    default nose_scale = 1.2
    default scaled_nose_size = [int(nose_size[0] * nose_scale), int(nose_size[1] * nose_scale)]

    image tank:
        xzoom 2.0
        yzoom 1.5
        "images/underwater_minigame/tank.png"
    
    image bar_full:
        xzoom 2.0
        yzoom 1.5
        "images/underwater_minigame/bar_full.png"
    
    image bar_empty:
        xzoom 2.0
        yzoom 1.5
        "images/underwater_minigame/bar_empty.png"
        
    image nose:
        zoom nose_scale
        "images/underwater_minigame/nose.png"

    image bubble:
        'images/underwater_minigame/bubble1.png'
        pause 0.2
        'images/underwater_minigame/bubble2.png'
        pause 0.3
        repeat

    image fish:
        zoom 0.7
        'images/underwater_minigame/fish.png'

    image bg underwater_game:
        'images/underwater_minigame/background water.png'
        parallel:
            function WaveShader(amp=1.0, period=0.5, speed=10.0, direction="both", repeat="mirrored", melt="both", melt_params=(20, 1.0, 0.1))

    # Moving target transform for target animation
    transform falling_object(target_speed=1.0, target_xpos=275):
        xpos target_xpos
        parallel:
            rotate -30
            linear 0.5 rotate 30
            repeat
        parallel:
            zoom 2.0
            linear 0.5 zoom 1.8 
            repeat
        parallel:
            ypos -30
            linear target_speed ypos int(renpy.config.screen_height * 1.2)

    transform object_hitted(xpos, ypos):
        pos (xpos, ypos)
        parallel:
            zoom 2.0
            linear 0.3 zoom 2.5
            linear 0.2 zoom 0.5
        parallel:
            linear 0.5 alpha 0.0

    transform moving_nose:
        function moveNose
        ypos 850
        pause 0.01
        repeat
    
    transform drowning:
        yalign 0.3
        zoom 2.0
        parallel:
            linear 2.5 yalign 0.9
        parallel:
            linear 2.5 zoom 3.0
            
init python:
    def moveNose(trans, at, st):
        trans.xpos = renpy.get_mouse_pos()[0] - int(scaled_nose_size[0] / 4)
        return None

    # Define the main game class
    class UnderwaterGame:
        def __init__(self):
            self.objects = []  # Store falling objects (bubbles and fish)
            self.status = self.Status()
            self.status.is_game_over = False
            self.object_spawn_timer = 0
            self.object_spawn_interval = 0.1  # Adjust this interval as needed
            
        def round_init(self):
            renpy.show('nose', at_list=[moving_nose])
            self.status.display()

        def round_end(self):
            if self.status.survived:
                narrator("You nearly survived")
            else:
                renpy.scene()
                renpy.show('blink')
                renpy.show('bg underwater_game', at_list=[drowning])
                renpy.music.play('<from 5>audio/Sound/Underwater Scene Sounds/Drowning.mp3', channel='music', relative_volume=2.0)
                narrator("You Drowned...")
            renpy.hide_screen('hp_bar')

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
                if obj.hitted:
                    continue
                if self.is_hit(obj):
                    renpy.music.play('audio/Sound/Underwater Scene Sounds/Breath of air.wav', channel='sound', relative_volume=2.5)
                    hp_change = obj.handle_collision()
                    if self.status.air_hp < self.status.max_hp:
                        self.status.air_hp += hp_change

        def is_hit(self, obj):
            # Get mouse position
            mouse_x, mouse_y = renpy.get_mouse_pos()[0], 850
            
            # Get object position and size
            obj_x, obj_y = obj.get_pos()
            obj_width, obj_height = obj.image_size 
            
            # Check if object position is valid
            if obj_x is None or obj_y is None:
                return False
        
            # Calculate boundaries for the object and player nose
            obj_left = min(obj_x - obj_width / 2, obj_x - scaled_nose_size[0] / 2)
            obj_right = max(obj_x + obj_width / 2, obj_x + scaled_nose_size[0] / 2)
            obj_top = min(obj_y - obj_height / 2, obj_y - scaled_nose_size[1] / 2)
            obj_bottom = max(obj_y + obj_height / 2, obj_y + scaled_nose_size[1] / 2)
            
            player_nose_top = 850
            player_nose_bottom = 850 + scaled_nose_size[1]
        
            # Check for collision
            if obj_left <= mouse_x <= obj_right and obj_top <= player_nose_bottom and player_nose_top <= obj_bottom:
                obj.hitted = True
                return True
        
            return False


        def spawn_object(self):
            # Create a new object (either bubble or fish) with random properties
            object_type = renpy.random.choice(["bubble", "bubble", "bubble", "bubble", "fish"])
            if object_type == "bubble":
                obj = self.Bubble(len(self.objects) + 1)
            else:
                obj = self.Fish(len(self.objects) + 1)
            self.objects.append(obj)
            obj.display()
        
        class FallingObject:
            def __init__(self, id):
                self.id = str(id)
                self.hitted = False
                self.target_speed = renpy.random.choice([1.0, 1.5, 2.0, 2.5])
                self.target_xpos = renpy.random.choice([200, 400, 600, 800, 1000, 1200, 1400, 1600])

            def display(self):
                renpy.show(name=self.id, what=self.position)

            def get_pos(self):
                return self.position.xpos, self.position.ypos

            def hide(self):
                hitted_position = At(ImageReference(self.image), object_hitted(xpos=self.position.xpos, ypos=self.position.ypos))
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
                self.position = At(ImageReference(self.image), falling_object(self.target_speed, self.target_xpos))
                self.hp_change = 1  # Increase HP when the bubble is hit

        class Fish(FallingObject):
            def __init__(self, id):
                super().__init__(id)
                self.image = 'fish'
                self.image_path = 'images/underwater_minigame/fish.png'
                self.target_scale = 2.0
                self.image_size = [renpy.image_size(self.image_path)[0] * self.target_scale, renpy.image_size(self.image_path)[1] * self.target_scale]
                self.position = At(ImageReference(self.image), falling_object(self.target_speed, self.target_xpos))
                self.hp_change = -2 # Decrease HP when the fish is hit

        class Status:
            def __init__(self):
                self.air_hp = 20  # Starting HP
                self.max_hp = 50  # Max HP
                self.time_max = 30  # Time Max
                self.time_left = 30  # Time left in seconds
                self.is_game_over = False
                self.survived = False

            def display(self):
                renpy.show_screen('hp_bar')

            def is_fail(self):
                if self.air_hp <= 0:
                    self.is_game_over = True
                    return True
                return False

            def is_clear(self):
                if self.time_left <= 0 and self.air_hp > 0:
                    self.survived = True
                    self.is_game_over = True
                    return True
                return False
