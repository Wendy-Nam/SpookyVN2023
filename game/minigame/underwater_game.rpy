# init -5 python:
#     # 호감도 바 스타일
#     style.fixed_bar = Style(style.default)
    
#     # bar width
#     style.fixed_bar.xmaximum = 600
    
#     # bar height
#     style.fixed_bar.ymaximum = 50
    
#     # bar의 gutter 부분 간격; 5로 지정할 시 5만큼 색이 칠해져있음
#     style.fixed_bar.left_gutter = 0 
#     style.fixed_bar.right_gutter = 0
    
#     style.fixed_bar.left_bar = Frame("images/underwater_minigame/bar_full.png", 0, 0)
#     style.fixed_bar.right_bar = Frame("images/underwater_minigame/bar_empty.png", 0, 0)

# init:
#     default air_hp = 10
#     screen hp_bar:
#         frame:
#             padding (15, 15)
#             background "#4f5a6680"
#             align (1.0, 0.0)
#             xmaximum 800
#             ymaximum 100
#             timer 1 repeat True action If(minigame2.status.time_left > 0 and minigame2.is_round_running == True, true=[SetVariable('minigame2.status.time_left', minigame2.status.time_left - 1), SetVariable('air_hp', air_hp - 1)])
#             vbox:
#                 bar:
#                     value air_hp
#                     range 100
#                     xalign 0.5
#                     style "fixed_bar"

#     image nose:
#         "images/underwater_minigame/nose.png"

#     image bubble:
#         zoom 2.0
#         'images/underwater_minigame/bubble.png'
#         pause 0.5
#         'images/underwater_minigame/bubble_glow.png'
#         pause 0.2
#         repeat
    
#     image bg underwater_game:
#         'images/underwater_minigame/background water.png'
#         parallel:
#             function WaveShader(amp = 1.0, period = 0.5, speed = 10.0, direction = "both", repeat="mirrored", melt="both", melt_params=(20,1.0,0.1))
    
#     # Moving target transform for target animation
#     transform moving_bubble(target_speed=1.0, target_ypos=275, target_scale=1.0):
#         zoom target_scale
#         parallel:
#             rotate -30
#             linear 0.5 rotate 30
#             repeat
#         parallel:
#             ypos target_ypos
#             linear 0.5 yoffset -20
#             yoffset 10
#             repeat
#         parallel:
#             linear target_speed xpos 1500
#             xpos 300
#             repeat
            
#     transform moving_nose:
#         parallel:
#             rotate -15
#             linear 1.0 rotate 15
#             repeat 
#         parallel:
#             zoom 1.0
#             linear 1.0 zoom 1.5
#             repeat
#         parallel:
#             function moveNose
#             pause 0.01
#             repeat

# init python:
#     # Define the main game class
#     class UnderwaterGame:
#         def __init__(self):
#             self.air_hp = 10
#             self.bubble = self.Bubble()
#             self.hp_bar = self.HpBar()
#             self.nose = "images/underwater_minigame/nose.png"
#             self.is_game_over = False

#         def run_game(self):
#             while not self.is_game_over:
#                 self.update_game()
#                 self.handle_events()
#                 self.render_game()

#         def update_game(self):
#             self.bubble.update()
#             self.hp_bar.update()
#             # Check for collisions or other game logic here
#             # Check if the game is over based on some condition
#             if self.air_hp <= 0:
#                 self.is_game_over = True

#         def handle_events(self):
#             # Handle user input events here
#             pass

#         def render_game(self):
#             # Render the game visuals here
#             pass

#         # Define a class for the bubble object
#         class Bubble:
#             def __init__(self):
#                 self.image_paths = [
#                     "images/underwater_minigame/bubble.png",
#                     "images/underwater_minigame/bubble_glow.png"
#                 ]
#                 self.current_image_index = 0
#                 self.pause_duration = 0.5

#             def update(self):
#                 # Update the bubble animation here
#                 # You can use self.image_paths and self.pause_duration to animate the bubble

#         # Define a class for the HP bar
#         class HpBar:
#             def __init__(self):
#                 self.air_hp = 10  # Starting HP
#                 self.max_hp = 100  # Max HP

#             def update(self):
#                 # Update the HP bar here
#                 pass

#     # Create an instance of the game
#     underwater_game = UnderwaterGame()

# label underwater_game:
#     scene bg underwater_game
#     $ underwater_game.run_game()
#     # Handle game over and transitions here
#     if underwater_game.is_game_over:
#         # Game over logic
#         pass

#     show bubble
#     show screen stat_overlay
#     "HIHIHIHI1"
#     # show nose at animated_outline()

#     "HIHIHIHI2"
#     "HIHIHIHI3"
#     "HIHIHIHI4"
