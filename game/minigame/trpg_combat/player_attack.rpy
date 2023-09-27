# player attack part
# : Instead of directly hitting monsters, players must hit a specific area within a timed hit box (rectangle) to damage the monster.

init -1:
    default player_attack_timeleft = 15
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
    
    screen attack_box(P1):
        # Screen to display the attack box
        frame align (0, 0):
            background im.FactorScale("gui/frame.png", 0.4)
            margin (30, 30)
            padding (30, 30)
            hbox:
                spacing 20
                image 'images/turnRPG_combat/clock_icon.png' xalign 0.5 yalign 0.5
                text "Time Left : [player_attack_timeleft]" size 50 color "#ffffff" xalign 0.5 yalign 0.5
        # background "images/turnRPG_combat/fight_slider.png"
        $ hit_zone_nb = len(P1.hit_zone)
        for i in range(hit_zone_nb):
            vbar:
                area(P1.hit_zone[i][0], 500, P1.hit_zone[i][1], 400) 
            $ damage_size = P1.damage_list[i]
            text "[damage_size]" size 50 color "#ffffff" area (P1.hit_zone[i][0], 500, P1.hit_zone[i][1], 400) offset (100, 20)
        timer 1 repeat True action [If (player_attack_timeleft > 0, true=SetVariable("player_attack_timeleft", player_attack_timeleft - 1))]
    
    screen attack_timing_bar(P1):
        key ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'mouseup_1'] :
            action Return(True)
        timer 1 repeat True action If(player_attack_timeleft > 0, false=Return(False))

init python:
    # Define the main game class
    class PlayerAttack:
        def __init__(self):
            # Initialize game elements based on provided configuration
            self.result = 0
            self.damage = 0
            self.is_game_running = True
            self.hit_pos = 0
            self.time_left = 15
            self.striked = False
            self.hit_zone = [(200, 100), (400, 200),  (700, 300), (1200, 200), (1500, 100)]
            self.damage_list = [10, 20, 30, 20, 10]
            self.position = At(ImageReference('stick'), moving_timing_bar)

        def run(self):
            # Run through rounds of the game
            self.round_init()
            self.attack()
            while self.is_game_running:
                self.handle_events()
            self.round_end(self.result)
            return self.damage
            
        def round_init(self):
            # Initialize round elements
            global player_attack_timeleft
            player_attack_timeleft = 15
            self.damage = 0
            self.striked = False
            self.hit_pos = 0
            self.result = 0
            self.is_game_runnning = True
            renpy.scene('black')
            renpy.show_screen("attack_box", self)
        
        def round_end(self, result):
            # End the current round
            renpy.hide_screen("board")
            renpy.hide_screen("attack_box")
            renpy.hide_screen("attack_timing_bar")
            renpy.scene('black')
            return
        
        def handle_events(self):
            # Handle various game events
            if player_attack_timeleft <= 0:
                self.is_game_running = False
                self.round_end("TIME UP")
                return
            if self.striked:
                self.is_game_running = False
                self.round_end("CLEAR")
                return
    
        def attack(self):
            # Perform player attack and hit detection
            # tmbar_position = At(ImageReference('stick'), moving_timing_bar)
            self.position = At(ImageReference('stick'), moving_timing_bar)
            renpy.show(name='stick', what=self.position)
            self.striked = renpy.call_screen('attack_timing_bar', self)
            # self.striked = True
            self.hit_pos = self.position.xpos
            renpy.hide('stick')
            print("Stricked Position : ", self.hit_pos)
            renpy.with_statement(vpunch)
            if self.check_hit():
                renpy.say(who=None, what="HIT", interact=True)
                return
            else:
                renpy.say(who=None, what="MISS", interact=True)
                return
            
        def check_hit(self):
            # Check if a hit has occurred
            for i in range(len(self.hit_zone)):
                print("hit check : ", self.hit_zone[i][0], self.hit_pos, self.hit_zone[i][0] + self.hit_zone[i][1])
                if self.hit_zone[i][0] <= self.hit_pos <= (self.hit_zone[i][0] + self.hit_zone[i][1]):
                    self.damage = self.damage_list[i]
                    return True
            return False

# label minigame3_playerAttack_test:
#     $ testGame = PlayerAttack()
#     $ damage = testGame.run()
#     "Damage : [damage]"