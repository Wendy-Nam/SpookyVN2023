### Game Rules ###

# This is a first-person shooter game from the minigame1er's point of view.
# Configure the number of targets per round, the number of rounds, time limits for each round, and the player's life count.

# 1. The player must eliminate all targets within the time limit for each round.
# 2. Failure to eliminate a target within the time limit results in an attack on the player.
# 3. The player can shoot targets by clicking the mouse.
init python:   
    # Define the game configuration class
    class GameConfig:
        def __init__(self,
                     target_nb=10,
                     time_limit=30,
                     bullet_max=5,
                     target_speed_range=(1, 2.5),
                     target_scale_range=(1.0, 1.0)):
            self.target_nb = target_nb
            self.time_limit = time_limit
            self.bullet_max = bullet_max
            self.target_speed_range = target_speed_range
            self.target_scale_range = target_scale_range
            # Image paths for various game elements
            self.IMG_BULLET = 'images/shooting_minigame/bullet.png'
            self.IMG_BULLET_EMPTY = 'images/shooting_minigame/bullet.png'
            self.IMG_AIM_IDLE = 'images/shooting_minigame/crosshair_idle.png'
            self.IMG_AIM_HOVER = 'images/shooting_minigame/crosshair_hover.png'
            self.IMG_WEAPON = 'images/shooting_minigame/rifle.png'
            # Determine size of the weapon image
            self.IMG_SIZE_WEAPON = renpy.image_size(self.IMG_WEAPON)
    # renpy.config.choice_sound = renpy.audio.music.play("audio/Sound/Choice Click Sound.wav", channel="choice", relative_volume=0.5, loop=False)

# Initialize the game
init:
    image normal_target:
        'images/shooting_minigame/targets/duck1.png'
        pause 2.0
        'images/shooting_minigame/targets/duck2.png'
        pause 1.0
        'images/shooting_minigame/targets/duck3.png'
        pause 1.0
        'images/shooting_minigame/targets/duck4.png'
        pause 2.0
        repeat

    # image avoid_target:
    #     'images/shooting_minigame/targets/carla1.png'
    #     pause 1.0
    #     'images/shooting_minigame/targets/carla2.png'
    #     pause 0.5
    #     repeat
    
    image boss_duck:
        'images/shooting_minigame/targets/duck_boss.png'

    transform target_hitted(xpos, ypos):
        pos (xpos, ypos)
        parallel:
            linear 0.8 yzoom 0.1 yoffset 100
        parallel:
            linear 1.5 alpha 0.0
    
    # Define transforms for animations
    # Moving aim transform to follow the cursor
    transform moving_aim:
        function moveAim
        pause 0.01
        repeat

    # Moving target transform for target animation
    transform moving_target(target_speed=1.0, target_ypos=275, target_scale=1.0):
        zoom target_scale
        parallel:
            ypos target_ypos
            linear 0.5 yoffset -20
            yoffset 10
            repeat
        parallel:
            linear target_speed xpos 1500
            xpos 300
            repeat
    
    transform moving_boss_duck(target_speed=1.0, target_ypos=275, target_scale=1.0):
        zoom target_scale
        parallel:
            linear 0.5 zoom 2.0
            linear 0.5 zoom 2.5
            repeat
        parallel:
            ypos target_ypos
            linear 0.2 yoffset -50
            yoffset 50
            repeat
        parallel:
            linear target_speed ypos -50
            ypos renpy.random.choice([180, 420, 650])
            repeat
        parallel:
            linear 1.5 xpos 1500
            xpos -300
            repeat
    
    # Moving weapon transform for weapon animation
    transform moving_weapon:    
        function moveWeapon
        pause 0.01
        repeat
    
    # Alpha dissolve transform for fading effects
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0

    # Screen displaying game status
    screen board():
        # Frame to display round and score information
        frame align(0, 0, 1.0):
            margin (30, 30)
            padding (15, 15)
            background "#ffffff00"
            vbox:
                # Display remaining targets and total targets
                text "{b}{i}Scores: {color=#ffff00}%d{/color} / %d{/i}{/b}  " % (minigame1.status.target_nb - minigame1.status.target_now, minigame1.status.target_nb) size 35 color "#ffffff" yalign 0.5 line_spacing 5
                # Display time left with red color if running out
                timer 1 repeat True action If(minigame1.status.time_left > 0 and minigame1.is_game_running == True, true=[SetVariable('minigame1.status.time_left', minigame1.status.time_left - 1)])
                text "{b}{i}Time Left : %d{/i}{/b}  " % (minigame1.status.time_left) size 35 line_spacing 5 at alpha_dissolve:
                    if minigame1.status.time_left <= 2:
                        color "#ff0000"
                    else:
                        color "#ffffff"
        # Frame to display bullet and life information
        frame align (1.0, 0.0):
            margin (30, 30)
            padding (10, 10)
            background "#4f5a6680"
            hbox:
                # Display remaining bullets
                text "{b}{i} Bullets: %d{/i}{/b}  " % minigame1.status.bullet_now size 35 color "#ffffff" yalign 0.5
                # Display bullet images based on remaining bullets
                for i in range(minigame1.status.bullet_max):
                    if minigame1.status.bullet_max > minigame1.status.bullet_now + i:
                        image minigame1.config.IMG_BULLET_EMPTY:
                            xalign 0.5 yalign 0.5 alpha 0.25 zoom 2.0
                    else:
                        image minigame1.config.IMG_BULLET:
                            xalign 0.5 yalign 0.5 zoom 2.0
                            
    screen boss_round_board():
        # Frame to display round and score information
        frame align(0, 0, 1.0):
            margin (30, 30)
            padding (15, 15)
            background "#ffffff00"
            vbox:
                # Display remaining targets and total targets
                text "{b}{i}HP: {color=#ffff00}%d{/color} / %d{/i}{/b}  " % (minigame1.boss_target.life_now, minigame1.boss_target.life_max) size 35 color "#ffffff" yalign 0.5 line_spacing 5
                # Display time left with red color if running out
                timer 1 repeat True action If(minigame1.status.time_left > 0 and minigame1.is_game_running == True, true=[SetVariable('minigame1.status.time_left', minigame1.status.time_left - 1)])
                text "{b}{i}Time Left : %d{/i}{/b}  " % (minigame1.status.time_left) size 35 line_spacing 5 at alpha_dissolve:
                    if minigame1.status.time_left <= 2:
                        color "#ff0000"
                    else:
                        color "#ffffff"
        # Frame to display bullet and life information
        frame align (1.0, 0.0):
            margin (30, 30)
            padding (10, 10)
            background "#4f5a6680"
            hbox:
                # Display remaining bullets
                text "{b}{i} Bullets: %d{/i}{/b}  " % minigame1.status.bullet_now size 35 color "#ffffff" yalign 0.5
                # Display bullet images based on remaining bullets
                for i in range(minigame1.status.bullet_max):
                    if minigame1.status.bullet_max > minigame1.status.bullet_now + i:
                        image minigame1.config.IMG_BULLET_EMPTY:
                            xalign 0.5 yalign 0.5 alpha 0.25 zoom 2.0
                    else:
                        image minigame1.config.IMG_BULLET:
                            xalign 0.5 yalign 0.5 zoom 2.0

    image aim_idle:
        zoom 0.5
        minigame1.config.IMG_AIM_IDLE
    
    image aim_hover:
        zoom 0.5
        minigame1.config.IMG_AIM_HOVER
    
    # Screen for the aim that follows the mouse
    screen gun():
        # Timer to control game time and actions
        timer 1 repeat True action If(minigame1.status.time_left > 0, false=Return("timeout"))
        # Imagebutton for aim with hover effect
        imagebutton idle 'aim_idle' hover 'aim_hover' xalign 0.5 yalign 0.5 action [SetVariable('minigame1.player.fired', True), Return("fired")] at moving_aim
        frame:
            background "#ffffff00"
            xalign 0.0 yalign 1.5
            image minigame1.config.IMG_WEAPON at moving_weapon:
                rotate -15

init python:
    # Define transform functions
    # Transform function to move aim based on cursor position
    def moveAim(trans, at, st):
        trans.pos = trackCursor()
        trans.zoom = distance_zoom(renpy.get_mouse_pos()[1], 0.5, 1.0)
        return None

    # Transform function to move weapon based on cursor position
    def moveWeapon(trans, at, st):
        trans.zoom = distance_zoom(renpy.get_mouse_pos()[1], 0.8, base=2.0)
        trans.alpha = alpha_zoom()
        trans.pos = trackCursor(xpos_offset=int(minigame1.config.IMG_SIZE_WEAPON[0] * 2), ypos_offset=int((minigame1.config.IMG_SIZE_WEAPON[1]) * 1.0))
        trans.alpha = 1 - (renpy.get_mouse_pos()[1] / config.screen_height) * 1.2
        return None
    
    # Calculate zoom based on cursor position for various elements
    def distance_zoom(ypos, mult, base):
        return (-((config.screen_height / 2 - ypos) / config.screen_height) * mult + base)
        
    # Track cursor position with optional offsets
    def trackCursor(xpos_offset=0, ypos_offset=0):
        return (renpy.get_mouse_pos()[0] - xpos_offset, renpy.get_mouse_pos()[1] - ypos_offset)

    # Calculate alpha value based on cursor position
    def alpha_zoom():
        return (1 - (renpy.get_mouse_pos()[1] / config.screen_height) * 0.2)

    # Define the main game class
    class ShootingGame:
        def __init__(self, config):
            # Initialize game elements based on provided configuration
            self.config = config
            self.player = self.Player(self.config)
            self.targets = []
            self.status = self.Status(self.config.target_nb, self.config.time_limit, self.config.bullet_max)
            self.is_game_running = True
        def run(self):
            # Run through rounds of the game
            self.round_init()
            while self.is_game_running:
                self.player.attack(self.status, self.targets)
                self.handle_events()
            return None
            
        def round_init(self):
            # Initialize round elements
            renpy.scene('black')
            # renpy.say(who=None, what="ROUND " + str(self.status.round_now), interact=True)
            renpy.show_screen("board")
            normal_target_nb = self.config.target_nb
            # avoid_target_nb = int(self.config.target_nb / 2)
            # total_target_nb = normal_target_nb + avoid_target_nb
            for i in range(normal_target_nb):
                self.targets.append(self.Target(self.config, i+1))
                self.targets[i].display()
            # for i in range(avoid_target_nb):
            #     self.targets.append(self.AvoidTarget(self.config, normal_target_nb+i+1))
            #     self.targets[normal_target_nb+i].display()
            self.is_game_runnning = True
        
        def round_end(self, result):
            # End the current round
            renpy.hide_screen("board")
            renpy.scene()
            renpy.show("bg carnival_minigame")
            self.targets.clear()
            self.is_game_running = False
            renpy.say(who=None, what=result, interact=True)
            return
        
        def handle_events(self):
            # Handle various game events
            if self.status.is_clear():
                self.round_end("CLEAR")
                return
            if self.status.is_time_up():
                self.round_end("TIME UP")
                return
            if self.status.is_no_bullets():
                self.round_end("GAME OVER : No Bullets Left")
                return
    
        # Define the Player class
        class Player:
            def __init__(self, config):
                # Initialize player attributes
                self.config = config
                self.hit_pos = None
                self.fired = False
    
            def attack(self, status, targets):
                # Perform player attack and hit detection
                renpy.call_screen("gun")
                renpy.music.play('audio/Sound/Carnival Scene Sounds/Rifle Shot.WAV', channel='weapon', loop=False, relative_volume=0.01)
                self.hit_pos = [renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1]]
                targets_nb = int(self.config.target_nb)
                for i in range(targets_nb):
                    if not targets[i].killed:
                        pos = targets[i].get_pos()
                        if self.is_hit(pos, targets[i].image_size):
                            targets[i].hide()
                            targets[i].killed = True
                            if targets[i].image == 'normal_target':
                                status.target_now -= 1
                                renpy.music.play('audio/Sound/Carnival Scene Sounds/Target Hit.mp3', channel='target', loop=False, relative_volume=0.)
                                renpy.music.play('<from 0 to 0.8>audio/Sound/Carnival Scene Sounds/Ducks Quacking.wav', channel='sound', loop=False, relative_volume=0.1)
                                
                            # elif targets[i].image == 'avoid_target':
                            #     status.bullet_now -= 1
                            #     status.karma += 1
                renpy.with_statement(vpunch)
                if self.fired:
                    status.bullet_now -= 1
                    self.fired = False
                return None
            
            def is_hit(self, target_pos, target_size):
                # Check if a hit has occurred
                if target_pos[0] <= self.hit_pos[0] <= target_pos[0] + target_size[0]:
                    if target_pos[1] <= self.hit_pos[1] <= target_pos[1] + target_size[1]:
                        return True
                return False
    
        # Define the Target class
        class Target:
            def __init__(self, config, id):
                # Initialize target attributes
                self.config = config
                self.id = str(id)
                self.image = 'normal_target'
                self.image_path = 'images/shooting_minigame/targets/duck1.png'
                self.target_speed = renpy.random.uniform(*self.config.target_speed_range)
                self.target_ypos = renpy.random.choice([180, 420, 650])
                self.target_scale = renpy.random.uniform(*self.config.target_scale_range)
                self.image_size = [renpy.image_size(self.image_path)[0] * self.target_scale, renpy.image_size(self.image_path)[1] * self.target_scale]
                self.position = At(ImageReference(self.image), moving_target(self.target_speed, self.target_ypos, self.target_scale))
                self.killed = False
            
            def display(self):
                # Display the target on screen
                self.position = At(ImageReference(self.image), moving_target(self.target_speed, self.target_ypos, self.target_scale))
                renpy.show(name=self.id, what=self.position)

            def get_pos(self):
                # Get the current position of the target
                return self.position.xpos, self.position.ypos
            
            def hide(self):
                # Hide the target
                hitted_position = At(ImageReference(self.image), target_hitted(xpos=self.position.xpos, ypos=self.position.ypos))
                renpy.show(name=str(-int(self.id)), what=hitted_position)
                renpy.hide(self.id)
                
        # class AvoidTarget(Target):
        #     def __init__(self, config, id):
        #         # Initialize target attributes
        #         super().__init__(config, id)
        #         self.image = 'avoid_target'
        #         self.image_path = 'images/shooting_minigame/targets/carla1.png'
        #         self.image_size = [renpy.image_size(self.image_path)[0] * self.target_scale, renpy.image_size(self.image_path)[1] * self.target_scale]

        # Define the Status class
        class Status:
            def __init__(self, target_nb, time_limit, bullet_max):
                # Initialize game status attributes
                self.target_nb = target_nb
                self.time_limit = time_limit
                self.bullet_max = bullet_max
                self.target_now = target_nb
                self.time_left = time_limit
                self.bullet_now = bullet_max
                self.karma = 0 # how many "don't hit" targets were hit
            
            def is_no_bullets(self):
                # Check if the game is over
                if self.bullet_now <= 0:
                    return True
                return False
            
            def is_clear(self):
                # Check if the round is clear
                if self.target_now <= 0:
                    return True
                return False
                
            def is_time_up(self):
                # Check if time is up for the current round
                if self.time_left <= 0:
                    return True
                return False