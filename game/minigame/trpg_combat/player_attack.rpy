# player attack part
# : Instead of directly hitting monsters, players must hit a specific area within a timed hit box (rectangle) to damage the monster.
            
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
            self.hit_zone = [(200, 100), (400, 200),  (700, 400), (1200, 200), (1500, 100)]
            self.damage_list = [30, 20, 10, 20, 30]
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
            renpy.scene()
            renpy.show('bg minigame3')
            renpy.show_screen("attack_box", self)
        
        def round_end(self, result):
            # End the current round
            renpy.hide_screen('attack_box')
            renpy.scene()
            renpy.show('bg minigame3')
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
            self.position = At(ImageReference('stick'), moving_timing_bar)
            renpy.show(name='stick', what=self.position)
            self.striked = renpy.call_screen('attack_timing_bar', self)
            self.hit_pos = self.position.xpos
            renpy.hide('stick')
            # print("Stricked Position : ", self.hit_pos)
            renpy.with_statement(vpunch)
            if self.check_hit():
                renpy.say(who=None, what="HIT", interact=True)
                return self.damage
            else:
                renpy.say(who=None, what="MISS", interact=True)
                return self.damage
            
        def check_hit(self):
            # Check if a hit has occurred
            for i in range(len(self.hit_zone)):
                # print("hit check : ", self.hit_zone[i][0], self.hit_pos, self.hit_zone[i][0] + self.hit_zone[i][1])
                if self.hit_zone[i][0] <= self.hit_pos <= (self.hit_zone[i][0] + self.hit_zone[i][1]):
                    self.damage = self.damage_list[i]
                    return True
            return False
