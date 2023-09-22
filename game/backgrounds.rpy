
# CARNIVAL
image bg carnival:
    'images/backgrounds/Carnival/carnival_wheel.png'
    parallel:
        linear 2.0 zoom 1.04
        .1
        linear 1.5 zoom 1.02
        .1
        repeat
    parallel:
        linear 2.0 xoffset 8
        .1
        linear 1.5 xoffset 0
        repeat
    parallel:
        linear 3.5 yoffset 4
        .1
        linear 1.5 yoffset 0
        repeat
image bg carnival_minigame:
    'images/backgrounds/Carnival/carnival_minigame.png'
image bg carnival_foodtent:
    'images/backgrounds/Carnival/carnival_foodtent.png'

# HOUSE
## CHILD BEDROOM
image bg bedroom_sunset:
    zoom 0.9
    'images/backgrounds/House/Child Bedroom/bedroom_clean_sunset.png'
image bg bedroom_day:
    zoom 0.9
    'images/backgrounds/House/Child Bedroom/bedroom_clean_day.png'
image bg bedroom_night:
    zoom 0.9
    'images/backgrounds/House/Child Bedroom/bedroom_clean_night.png'
image bg bedroom_dark:
    zoom 0.9
    'images/backgrounds/House/Child Bedroom/child_bedroom_dark.png'
## LIVING ROOM
image bg livingroom_sunset:
    zoom 0.9
    'images/backgrounds/House/Living Room/LivingRoom_Sunset.png'
image bg livingroom_day:
    zoom 0.9
    'images/backgrounds/House/Living Room/LivingRoom_Day.png'
image bg livingroom_night:
    zoom 0.9
    'images/backgrounds/House/Living Room/LivingRoom_Night.png'

### OFFICE
image bg office_sunset:
    zoom 0.9
    'images/backgrounds/House/Office/Office_Sunset.png'
image bg office_day:
    zoom 0.9
    'images/backgrounds/House/Office/Office_Day.png'
image bg office_night:
    zoom 0.9
    'images/backgrounds/House/Office/Office_Night.png'

## UnderWater
image bg underwater:
    zoom 0.9
    'images/backgrounds/Underwater/underwater.png'
    parallel:
        linear 2.0 zoom 1.2
        .1
        linear 1.5 zoom 1.0
        .1
        linear 1.0 zoom 1.1
        .1
    parallel:
        function WaveShader(amp = 12.0, period = 2.0, speed = 1.0, direction = "both", damp = 1.0, double=None, double_params=None, melt=None, melt_params=None, repeat=None)
    # repeat
    
image bg underwater_door:
    zoom 0.9
    'images/backgrounds/Underwater/underwater.door.png'
    parallel:
        linear 1.0 zoom 1.05
        linear 1.0 zoom 1.3
        linear 1.0 zoom 1.1
        linear 1.0 zoom 1.2
        repeat
    parallel:
        function WaveShader(amp = 1.0, period = 1.0, speed = 10.0, direction = "both", repeat="mirrored", melt="both", melt_params=(10,1.0,0.1))

image bg underwater_door_closeup:
    zoom 2.0
    'images/backgrounds/Underwater/underwater.door.png'
    yalign 0.5
    function WaveShader(amp = 1.0, period = 0.5, speed = 1.0, direction = "both", repeat="mirrored", melt="both", melt_params=(10,1.0,0.1))


image bg underwater_creature:
    zoom 0.9
    'images/backgrounds/Underwater/underwater_creature.png'
    parallel:
        linear 0.5 zoom 1.1
        linear 0.5 zoom 1.0
        repeat
    parallel:
        function WaveShader(amp = 2.0, period = 0.5, speed = 7.0, direction = "horizontal", melt="both", melt_params=(20,1.0,0.2))
        
image bg hand_drowning = 'images/backgrounds/Underwater/hand_drowning.png'

transform hand_drowning:
    zoom 1.2
    linear 0.5 xalign 1.0 yalign 0.9 zoom 1.1
    linear 0.5 xalign 0.8 yalign 1.0 zoom 1.2
    zoom 0.9
    repeat