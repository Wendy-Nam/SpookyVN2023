# minigame3
# Undertale style. hp bar / striking by matching the certain position of bar / turn based / etc.

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

        def run(self):
            renpy.scene()
            renpy.show('bg minigame3')
            self.player_win = False
            # renpy.show_screen('trpg_game_board', self, self.monster, self.player)
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
            
        # def display_game_status(self):
            
            # Implement a screen to display game status (HP bars, etc.)
            # You can use Ren'Py screens for this.

        def take_turn(self):
            # renpy.hide_screen('trpg_game_board')
            if self.current_turn == "Player":
                self.player_turn()
                self.current_turn = "Monster"
            else:
                self.monster_turn()
                self.current_turn = "Player"

        def player_turn(self): 
            # renpy.show_screen('player_hp_bar', self.player)
            renpy.show_screen('trpg_game_board', self, self.player, self.monster)
            renpy.call_screen('trpg_player_menu_board', self.player)
            self.attack_started = True
            if game_escape_flag:
                return
            self.monster.hp -= self.player.attack()
            self.attack_started = False

        def monster_turn(self):
            renpy.pause(2.0)
            narrator("HAHAHA your turn is done!!!!")
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