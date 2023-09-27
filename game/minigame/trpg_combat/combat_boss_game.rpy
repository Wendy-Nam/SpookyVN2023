# minigame3
# Undertale style. hp bar / striking by matching the certain position of bar / turn based / etc.
init:
    screen monster_hp_bar(monster):
        $ monster_hp = ExtraAnimatedValue(
                    value=monster.hp, 
                    range=monster.max_hp, 
                    range_delay=3.0,
                    warper="ease_quart")
        fixed:
            area (1200, 50, 500, 120) # position of the hp-bar 
            bar:
                value monster_hp
                left_bar ValueImage(
                    monster_hp,
                    Transform("images/turnRPG_combat/bar/hp_bar_red.png", zoom=0.8),
                    Transform("images/turnRPG_combat/bar/hp_bar_yellow.png", zoom=0.8),
                    Transform("images/turnRPG_combat/bar/hp_bar_green.png", zoom=0.8))
                right_bar Transform("images/turnRPG_combat/bar/hp_bar_blank.png", zoom=0.8)
                area (0,0, 800, 150)

            add monster_hp.text(
                "{0.current_value:.0f} hp",
                size = 35,
                color = "#FFF",
                outlines = [(abs(2), "#000")],
                bold = True,
                xcenter = 0.7,
                ycenter = 0.5)
    
    screen player_hp_bar(player):
        $ player_hp = ExtraAnimatedValue(
            value=player.hp, 
            range=player.max_hp, 
            range_delay=3.0,
            warper="ease_quart")
        textbutton "{b}Escape{b}" area (100, 50, 800, 120) action [Hide('player_hp_bar')]
        fixed:
            drag:
                drag_name "draggable_player_hp_bar"
                droppable True
                area (100, 50, 800, 120) # position of the hp-bar 
                bar:
                    value player_hp
                    left_bar ValueImage(
                        player_hp,
                        Transform("images/turnRPG_combat/bar/hp_bar_red.png", zoom=0.8),
                        Transform("images/turnRPG_combat/bar/hp_bar_yellow.png", zoom=0.8),
                        Transform("images/turnRPG_combat/bar/hp_bar_green.png", zoom=0.8))
                    right_bar Transform("images/turnRPG_combat/bar/hp_bar_blank.png", zoom=0.8)
                    area (0,0, 800, 150)
                add player_hp.text(
                    "{0.current_value:.0f} hp",
                    size = 35,
                    color = "#FFF",
                    outlines = [(abs(2), "#000")],
                    bold = True,
                    xcenter = 0.4,
                    ycenter = 0.5)
    
    screen trpg_player_menu_board(player):
        frame align (0.85, 0.8):
            background im.FactorScale("images/turnRPG_combat/trpg_player_menu.png", 0.8)
            padding (120, 80)
            vbox:
                spacing 10
                textbutton "{b}Attack{/b}" action [NullAction()] text_size 45
                textbutton "{b}Inventory{/b}" action [NullAction()] text_size 45
                textbutton "{b}Hp{/b}" action [NullAction(), Show('player_hp_bar', None, player)] text_size 45
                textbutton "{b}Escape{/b}" action [NullAction()] text_size 45

    screen display_turn(game):
        $ turn = game.current_turn
        frame align (0, 0):
            background im.FactorScale("gui/frame.png", 0.4)
            margin (30, 30)
            padding (30, 30)
            hbox:
                spacing 20
                image 'images/turnRPG_combat/clock_icon.png' xalign 0.5 yalign 0.5
                text "Turn - [turn]" size 50 color "#ffffff" xalign 0.5 yalign 0.5

    screen trpg_game_board(game, monster, player):
        use display_turn(game)
        # use player_hp_bar(player)
        use monster_hp_bar(monster)
        # use player_hp_bar(player)
        use trpg_player_menu_board(player)

init python:
    class TurnBasedGame:
        def __init__(self):
            self.player = self.Player()
            self.monster = self.Monster()
            self.current_turn = "Player"
            self.player_win = False

        def run(self):
            self.player_win = False
            renpy.show_screen('trpg_game_board', self, self.monster, self.player)
            while self.player.hp > 0 and self.monster.hp > 0:
                self.take_turn()
                if self.player.hp <= 0:
                    "You have been defeated."
                    break
                elif self.monster.hp <= 0:
                    "You have defeated the monster."
                    self.player_win = True 
                    break
            renpy.hide_screen('trpg_game_board')
            

        # def display_game_status(self):
            
            # Implement a screen to display game status (HP bars, etc.)
            # You can use Ren'Py screens for this.

        def take_turn(self):
            if self.current_turn == "Player":
                self.player_turn()
                self.current_turn = "Monster"
            else:
                self.monster_turn()
                self.current_turn = "Player"

        def player_turn(self): 
            renpy.pause(20.0)
            pass
            
            # narrator("Player's turn")
            # Implement the player's turn logic
            # Show the menu (Attack / Item / HP / Escape)
            # Handle player's choice and update game state accordingly

        def monster_turn(self):
            renpy.pause(20.0)
            pass
            # narrator("Monster's turn")
            # Implement the monster's turn logic
            # Determine the monster's action (e.g., attack)
            # Calculate damage to the player and update game state
    
        class Player:
            def __init__(self):
                self.hp = 100
                self.max_hp = 100
                self.inventory = []
                self.armor = 'Bat'
        
            def attack(self, target):
                # Implement the player's attack logic
                # Calculate damage to the monster and update its HP
                pass
        
            def use_item(self):
                # Implement item usage logic
                pass
        
        class Monster:
            def __init__(self):
                self.hp = 100
                self.max_hp = 100
        
            def attack(self, target):
                # Implement the monster's attack logic
                # Calculate damage to the player and update their HP
                pass

# Define Ren'Py screens and UI elements to display game status and handle menu choices.

# Start the game
label start_game:
    $ game = TurnBasedGame()
    $ game.run()
    # show screen trpg_game_board(game, game.monster, game.player)
    # Handle game over and other outcomes here
    if game.player_win:
        "You have defeated the monster."
    else:
        "You have been defeated."
