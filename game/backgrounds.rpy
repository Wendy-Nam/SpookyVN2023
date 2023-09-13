# CARNIVAL
image bg carnival = 'images/backgrounds/Carnival/carnival_wheel.png'

# HOUSE
## CHILD BEDROOM
image bg bedroom_sunset = 'images/backgrounds/House/Child Bedroom/bedroom_clean_sunset.png'
image bg bedroom_day = 'images/backgrounds/House/Child Bedroom/bedroom_clean_day.png'
image bg bedroom_night = 'images/backgrounds/House/Child Bedroom/bedroom_clean_night.png'
image bg bedroom_dark = 'images/backgrounds/House/Child Bedroom/child_bedroom_dark.png'
## LIVING ROOM
image bg livingroom_sunset = 'images/backgrounds/House/Living Room/LivingRoom_Sunset.png'
image bg livingroom_day = 'images/backgrounds/House/Living Room/LivingRoom_Day.png'
image bg livingroom_night = 'images/backgrounds/House/Living Room/LivingRoom_Night.png'
### OFFICE
image bg office_sunset = 'images/backgrounds/House/Office/Office_Sunset.png'
image bg office_day = 'images/backgrounds/House/Office/Office_Day.png'
image bg office_night = 'images/backgrounds/House/Office/Office_Night.png'

## UnderWater
image bg underwater = 'images/backgrounds/Underwater/underwater.png'
image bg underwater_door = 'images/backgrounds/Underwater/underwater.door.png'
image bg underwater_creature = 'images/backgrounds/Underwater/underwater_creature.png'
image bg hand_drowning = 'images/backgrounds/Underwater/hand_drowning.png'

image blink:
    "images/effects/mask_blink_half.png"
    .5
    "images/effects/mask_blink_close.png" 
    .2
    "images/effects/mask_blink_open.png"
    .1
    alpha 0.0

transform carnival_wheel_tint:
    matrixcolor TintMatrix("#e0ddb6")*SaturationMatrix(1.0000)*ContrastMatrix(1.0000)

transform jumpAttack:
    linear 0.5 zoom 3.0
