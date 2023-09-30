# minigame3
# Undertale style. hp bar / striking by matching the certain position of bar / turn based / etc.
init -1:
    image monster_minigame3:
        zoom 0.7
        pause 0.1
        'images/turnRPG_combat/monster/monster_eye_1.png'
        pause 0.1
        'images/turnRPG_combat/monster/monster_eye_2.png'
        pause 0.1
        'images/turnRPG_combat/monster/monster_eye_3.png'
        repeat
    
    image weapon_bat:
        rotate -30
        'images/turnRPG_combat/attack/bat.png'
        linear 0.2 rotate 60
        repeat

    image swing:
        alpha 1.0
        linear 0.1 alpha 0.2
        'images/turnRPG_combat/attack/swing.png'
        repeat
    
init python:
    # def fake_escape_button_msg():
    #     narrator()
    class TurnBasedGame:
        def __init__(self):
            self.player = self.Player()
            self.monster = self.Monster()
            self.current_turn = "Player"
            self.attack_started = False
            self.player_win = False
            self.player_attack_missed = False

        def run(self):
            renpy.scene()
            renpy.show('bg minigame3')
            self.player_win = False
            while self.player.hp > 0 and self.monster.hp > 0:
                self.take_turn()
                if game_escape_flag:
                    narrator("You found the secret escape button!")
                    self.player_win = True
                    break
                if self.player.hp <= 0:
                    # "You have been defeated."
                    break
                elif self.monster.hp <= 0:
                    # "You have defeated the monster."
                    self.player_win = True 
                    break
            renpy.hide_screen('trpg_game_board')

        def take_turn(self):
            # renpy.hide_screen('trpg_game_board')
            if self.current_turn == "Player":
                self.player_turn()
                self.current_turn = "Monster"
            else:
                self.monster_turn()
                self.current_turn = "Player"

        def player_turn(self): 
            global monster_damaged
            # renpy.show_screen('player_hp_bar', self.player)
            renpy.show_screen('trpg_game_board', self, self.player, self.monster)
            renpy.call_screen('trpg_player_menu_board', self.player)
            self.attack_started = True
            if game_escape_flag:
                return
            damage = self.player.attack()
            self.monster.hp -= damage
            if damage == 0:
                self.player_attack_missed = True
                narrator("You failed to attack!")
            else:
                narrator("You striked the monster successfully!")
                monster_damaged = True
            self.attack_started = False

        def monster_turn(self):
            global monster_damaged
            renpy.pause(2.5)
            monster_damaged = False
            narrator("The monster is ready to attack you.")
            self.attack_started = True
            self.monster.attack(self.player)
            self.attack_started = False
    
        class Player:
            def __init__(self):
                self.hp = 100
                self.max_hp = 100
                self.inventory = Inventory()
                self.inventory.addItem('Popcorn', amount=7)
                self.inventory.addItem('Churros', amount=2)
                self.inventory_mode = False
                self.attack_mechanism = PlayerAttack()
        
            def attack(self):
                self.player_attack_missed = False
                self.inventory_mode = False
                damage = self.attack_mechanism.run()
                narrator('damage: ' + str(damage))
                return (damage)
                # Implement the player's attack logic
                # Calculate damage to the monster and update its HP
        
            def use_item(self, name):
                if self.hp >= self.max_hp:
                    return
                if name == "Popcorn":
                    self.hp += 10
                elif name == "Churros":
                    self.hp += 20
                if self.hp >= self.max_hp:
                    self.hp = self.max_hp
                self.inventory.deleteItem(name)
                # Implement item usage logic
        
        class Monster:
            def __init__(self):
                self.hp = 100
                self.max_hp = 100
                self.attack_mechanism = MonsterAttack()
        
            def attack(self, target):
                self.attack_mechanism.run(target)
                # Implement the monster's attack logic
                # Calculate damage to the player and update their HP
                pass

    def toggle_inventory(player):
        player.inventory_mode = not (player.inventory_mode)
        return None