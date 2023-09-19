init -5 python:
    # 호감도 바 스타일
    style.fixed_bar = Style(style.default)
    
    # bar width
    style.fixed_bar.xmaximum = 600
    
    # bar height
    style.fixed_bar.ymaximum = 50
    
    # bar의 gutter 부분 간격; 5로 지정할 시 5만큼 색이 칠해져있음
    style.fixed_bar.left_gutter = 0 
    style.fixed_bar.right_gutter = 0
    
    style.fixed_bar.left_bar = Frame("images/underwater_minigame/bar_full.png", 0, 0)
    style.fixed_bar.right_bar = Frame("images/underwater_minigame/bar_empty.png", 0, 0)

init:
    screen hp_bar:
        frame:
            padding (15, 15)
            background "#4f5a6680"
            align (1.0, 0.0)
            xmaximum 800
            ymaximum 100
            timer 1 repeat True action If(minigame2.status.time_left > 0 and minigame2.is_game_over == False, true=[SetVariable('minigame2.status.time_left', minigame2.status.time_left - 1), SetVariable('minigame2.status.air_hp', minigame2.status.air_hp - 1)])
            vbox:
                text "Time Left: [minigame2.status.time_left]"
                bar:
                    value minigame2.status.air_hp
                    range 100
                    xalign 0.5
                    style "fixed_bar"

    image nose:
        "images/underwater_minigame/nose.png"

    image bubble:
        zoom 1.5
        'images/underwater_minigame/bubble.png'
        pause 0.5
        'images/underwater_minigame/bubble_glow.png'
        pause 0.2
        repeat
    
    image bg underwater_game:
        'images/underwater_minigame/background water.png'
        parallel:
            function WaveShader(amp = 1.0, period = 0.5, speed = 10.0, direction = "both", repeat="mirrored", melt="both", melt_params=(20,1.0,0.1))
    
    # Moving target transform for target animation
    transform falling_bubble(target_speed=1.0, target_xpos=275):
        xpos target_xpos
        parallel:
            rotate -30
            linear 0.5 rotate 30
            repeat
        parallel:
            ypos -30
            linear target_speed ypos 1000
            repeat
            
    transform moving_nose:
        function moveNose
        yalign 0.9
        pause 0.01
        repeat

init python:
    def moveNose(trans, at, st):
        trans.xpos = renpy.get_mouse_pos()[0]
        return None
    # Define the main game class
    class UnderwaterGame:
        def __init__(self):
            self.bubble = self.Bubble()
            self.status = self.Status()
            self.nose = "images/underwater_minigame/nose.png"
            self.is_game_over = False
        
        def round_init(self):
            renpy.show('nose',at_list=[moving_nose])
            self.bubble.display()
            self.status.display()
        
        def run(self):
            self.round_init()
            while not self.is_game_over:
                renpy.pause(0.1)
                if self.status.air_hp <= 0:
                    self.is_game_over = True
                if self.is_hit():
                    self.status.air_hp += 30
                    self.bubble.hide()
    
        # Define a class for the bubble object
        def is_hit(self):
            if self.bubble.popped == False:
                mouse_x, mouse_y = renpy.get_mouse_pos()[0], 800
                bubble_pos = self.bubble.get_pos() # NOTE : 왜 NONE이 나오는가?
                bubble_size = self.bubble.image_size
                print(mouse_x, mouse_y, bubble_pos, bubble_size)
                if bubble_pos[0] is None:
                    return False
                if bubble_pos[0] <= mouse_x <= bubble_pos[0] + bubble_size[0]:
                    if bubble_pos[1] <= mouse_y <= bubble_pos[1] + bubble_size[1]:
                        self.bubble.popped = True
                        return True
                    return False

        class Bubble:
            def __init__(self):
                self.image = 'bubble'
                self.image_path = 'images/underwater_minigame/bubble.png'
                self.image_size = renpy.image_size(self.image_path)
                self.id = str(1)
                self.pause_duration = 0.5
                self.target_speed = renpy.random.choice([1.0, 1.5, 2.0, 2.5, 3.0])
                self.target_xpos = renpy.random.choice([275, 300, 325, 350, 375, 400, 425, 450, 475, 500])
                self.position = At(ImageReference(self.image), falling_bubble(self.target_speed, self.target_xpos))
                self.popped = False
            def display(self):
                # self.position = At(ImageReference(self.image), falling_bubble(self.target_speed, self.target_xpos))
                renpy.show(name=self.id, what=self.position)
            
            def get_pos(self):
                # Get the current position of the target
                return self.position.xpos, self.position.ypos
            
            def hide(self):
                # Hide the target
                hitted_position = At(ImageReference(self.image), target_hitted(xpos=self.position.xpos, ypos=self.position.ypos))
                renpy.show(name=str(-int(self.id)), what=hitted_position)
                renpy.hide(self.id)

        # Define a class for the HP bar
        class Status:
            def __init__(self):
                self.air_hp = 25  # Starting HP
                self.max_hp = 50  # Max HP
                self.time_max = 30 # Time Max
                self.time_left = 30 # Time left in seconds
                
            def display(self):
                renpy.show_screen('hp_bar')
                pass
        
            def is_game_over(self):
                if self.air_hp <= 0:
                    return True
            
            def is_clear(self):
                if self.time_left <= 0 and self.air_hp > 0:
                    return True
                return True
    # Create an instance of the game
    

label underwater_game:
    scene bg underwater_game
    $ minigame2 = UnderwaterGame()
    $ minigame2.run()
    scene black
    
    "HIHIHIHI1"
    # show nose at animated_outline()

    "HIHIHIHI2"
    "HIHIHIHI3"
    "HIHIHIHI4"
