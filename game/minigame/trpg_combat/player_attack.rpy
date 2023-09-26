# player attack part
# : Instead of directly hitting monsters, players must hit a specific area within a timed hit box (rectangle) to damage the monster.

init -1:
    default time_left_playerAttack = 15
    default striked_playerAttack = False
    default striked_xpos = 0

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
    
    image stick:
        "images/turnRPG_combat/stick.png"
    
    default hit_zone = [(200, 100), (400, 200),  (700, 300), (1200, 200), (1500, 100)]
    default damage_zone = [10, 20, 30, 20, 10]
    screen attack_box:
        # Screen to display the attack box
        frame align (0, 0):
            background im.FactorScale("gui/frame.png", 0.4)
            margin (30, 30)
            padding (30, 30)
            hbox:
                spacing 20
                image 'images/turnRPG_combat/clock_icon.png' xalign 0.5 yalign 0.5
                text "Time Left : [time_left_playerAttack]" size 50 color "#ffffff" xalign 0.5 yalign 0.5
        # background "images/turnRPG_combat/fight_slider.png"
        $ hit_zone_nb = len(hit_zone)
        for i in range(hit_zone_nb):
            vbar:
                area(hit_zone[i][0], 500, hit_zone[i][1], 400) 
            $ damage_size = damage_zone[i]
            text "[damage_size]" size 50 color "#ffffff" area (hit_zone[i][0], 500, hit_zone[i][1], 400) offset (100, 20)
        timer 1 repeat True action [If (time_left_playerAttack > 0, true=SetVariable("time_left_playerAttack", time_left_playerAttack - 1))]
    
    screen attack_timing_bar:
        key ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'mouseup_1'] :
            action [SetVariable("striked_playerAttack", True), Return("fired")]
        timer 1 repeat True action If(time_left_playerAttack > 0, false=Return("timeout"))

init python:
    # Define the main game class
    class PlayerAttack:
        def __init__(self, weapon):
            # Initialize game elements based on provided configuration
            self.config = config
            self.weapon = weapon
            self.result = 0
            self.damage = 0
            self.is_game_running = True
            self.hit_pos = 0
            time_left_playerAttack = 15
            striked_playerAttack = False
            
            # self.time_left = 30
            #self.striked = False

        def run(self):
            # Run through rounds of the game
            self.round_init()
            while self.is_game_running:
                self.attack()
                self.handle_events()
            return self.damage
            
        def round_init(self):
            # Initialize round elements
            time_left_playerAttack = 15
            striked_playerAttack = False
            self.striked = False
            renpy.scene('black')
            # renpy.say(who=None, what="ROUND " + str(self.status.round_now), interact=True)
            renpy.show_screen("attack_box")
            self.is_game_runnning = True
        
        def round_end(self, result):
            # End the current round
            renpy.hide_screen("board")
            renpy.scene('black')
            self.is_game_running = False
            renpy.say(who=None, what=result, interact=True)
            return
        
        def handle_events(self):
            # Handle various game events
            if time_left_playerAttack <= 0:
                self.round_end("TIME UP")
                return
            if self.striked:
                self.round_end("CLEAR")
                return
    
        def attack(self):
            # Perform player attack and hit detection
            tmbar_position = At(ImageReference('stick'), moving_timing_bar)
            renpy.show(name='stick', what=tmbar_position)
            print("tmbar_position :", tmbar_position.xpos)
            renpy.call_screen('attack_timing_bar')
            self.hit_pos = tmbar_position.xpos
            renpy.hide('stick')
            print("Stricked Position : ", self.hit_pos)
            if self.check_hit():
                self.striked = True
                renpy.say(who=None, what="HIT", interact=True)
                return
            else:
                renpy.say(who=None, what="MISS", interact=True)
                return
            renpy.with_statement(vpunch)
            
        def check_hit(self):
            # Check if a hit has occurred
            for i in range(len(hit_zone)):
                print("hit check : ", hit_zone[i][0], self.hit_pos, hit_zone[i][0] + hit_zone[i][1])
                if hit_zone[i][0] <= self.hit_pos <= (hit_zone[i][0] + hit_zone[i][1]):
                    self.damage = damage_zone[i]
                    return True
            return False

label minigame3_playerAttack_test:
    $ testGame = PlayerAttack("Bat")
    $ damage = testGame.run()
    "Damage : [damage]"