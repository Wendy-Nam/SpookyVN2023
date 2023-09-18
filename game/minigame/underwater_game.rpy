init -5 python:
    # 호감도 바 스타일
    style.fixed_bar = Style(style.default)
    
    # bar width
    style.fixed_bar.xmaximum = 400
    
    # bar height
    style.fixed_bar.ymaximum = 30
    
    # bar의 gutter 부분 간격; 5로 지정할 시 5만큼 색이 칠해져있음
    style.fixed_bar.left_gutter = 0 
    style.fixed_bar.right_gutter = 0
    
    style.fixed_bar.left_bar = Frame("images/underwater_minigame/bar_full.png", 0, 0)
    style.fixed_bar.right_bar = Frame("images/underwater_minigame/bar_empty.png", 0, 0)

init:
    default air_hp = 0
    screen stat_overlay:
        # 호감도 창
        frame:
            # 호감도 창 테두리와 컨텐츠와의 간격
            padding (15, 15)
            # 호감도 배경 (반투명 - 뒤 2자리 코드가 투명도)
            background "#4f5a6680"
            # x, y축 정렬
            align (1.0, 0.0)
            # 호감도 창 크기
            xmaximum 250
            ymaximum 200
            vbox:
                bar:
                    value air_hp
                    range 100
                    xalign 0.5
                    style "fixed_bar"
 

    image nose:
        rotate -15
        "images/underwater_minigame/nose.png"
        parallel:
            rotate -15
            linear 1.0 rotate 15
            repeat 
        parallel:
            zoom 1.0
            linear 1.0 zoom 1.5
            repeat

    image bubble:
        zoom 2.0
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
    transform moving_bubble(target_speed=1.0, target_ypos=275, target_scale=1.0):
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

init python:
    # Define the main game class
    class GetBubbles:
        def __init__(self, config):
            # Initialize game elements based on provided configuration
            self.config = config
            self.player = self.Player(self.config)
            self.targets = []
            self.boss_target = None
            self.status = self.Status(self.config.target_nb, self.config.time_limit, self.config.bullet_max)
            self.is_round_running = True
            self.is_game_running = True

        def run(self):
            boss_round_started = False
            # Run through rounds of the game
            self.round_init()
            while self.is_round_running and self.is_game_running:
                self.player.attack(self.status, self.targets)
                self.handle_events()
            if self.is_game_running:
                self.boss_round_init()
                boss_round_started = True
            while self.is_game_running:
                self.player.attack_boss(self.status, self.boss_target)
                self.handle_events()
            if boss_round_started:
                self.boss_round_end()
            return None
            
        def round_init(self):
            # Initialize round elements
            renpy.scene('black')
            # renpy.say(who=None, what="ROUND " + str(self.status.round_now), interact=True)
            renpy.show_screen("board")
            normal_target_nb = self.config.target_nb
            avoid_target_nb = int(self.config.target_nb / 2)
            total_target_nb = normal_target_nb + avoid_target_nb
            for i in range(normal_target_nb):
                self.targets.append(self.Target(self.config, i))
                self.targets[i].display()
            for i in range(avoid_target_nb):
                self.targets.append(self.AvoidTarget(self.config, normal_target_nb+i))
                self.targets[normal_target_nb+i].display()
            self.is_round_running = True
                
        def round_end(self, result, is_game_over=False):
            # End the current round
            renpy.hide_screen("board")
            renpy.scene()
            renpy.show("bg carnival_minigame")
            self.targets.clear()
            self.is_round_running = False
            renpy.say(who=None, what=result, interact=True)
            if is_game_over:
                self.is_game_running = False
            return
        
        def handle_events(self):
            # Handle various game events
            if self.boss_target:
                if self.boss_target.killed:
                    self.round_end("clear")
                    self.is_game_running = False
                    return
            if self.status.is_game_over():
                self.round_end("GAME OVER", True)
                return
            if (self.boss_target is None) and self.status.is_clear():
                self.round_end("clear")
                return
            if self.status.is_time_up():
                self.round_end("time up", True)
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
                self.hit_pos = [renpy.get_mouse_pos()[0], renpy.get_mouse_pos()[1]]
                targets_nb = int(self.config.target_nb * 3/2)
                for i in range(targets_nb):
                    if not targets[i].killed:
                        pos = targets[i].get_pos()
                        if self.is_hit(pos, targets[i].image_size):
                            targets[i].hide()
                            targets[i].killed = True
                            if targets[i].image == 'normal_target':
                                status.target_now -= 1
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
                self.image = 'bubble'
                self.image_path = 'images/shooting_minigame/targets/bubble.png'
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
                self.boss_killed = False
                self.karma = 0 # how many "don't hit" targets were hit
            
            def is_game_over(self):
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
                
label underwater_game:
    scene bg underwater_game
    show bubble
    show screen stat_overlay
    "HIHIHIHI1"
    # show nose at animated_outline()

    "HIHIHIHI2"
    "HIHIHIHI3"
    "HIHIHIHI4"
