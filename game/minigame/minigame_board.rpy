
style rule_button_text is text:
    size 45
    hover_color "#FF8066"             # Pink
    outlines [ (1, "#000000", 1, 1) ] # Blue
    color "#FFFFFF"                   # Red
 
# BOARD FOR DISPLAYING RULES OF MINIGAME1
screen game_rules_minigame1:
    frame:
        margin (350, 80)
        background im.FactorScale("images/ruleboard/rule_shooting.png", 2.0)
        padding (450, 500)
        textbutton "{b}START{/b}" action Return() xpos 65 ypos 65 text_style 'rule_button_text'
    pass
    
# BOARD FOR DISPLAYING RULES OF MINIGAME2
default order_rules_mingame2 = 0

screen game_rules_minigame2:
    frame:
        margin (350, 80)
        padding (450, 500)
        if order_rules_mingame2 == 0:
            background im.FactorScale("images/ruleboard/rule_underwater1.png", 2.0)
            textbutton "{b}NEXT{/b}" action SetVariable('order_rules_mingame2', order_rules_mingame2+1) xpos 65 ypos 65 text_style 'rule_button_text'
        else:
            background im.FactorScale("images/ruleboard/rule_underwater2.png", 2.0)
            textbutton "{b}START{/b}" action Return() xpos 65 ypos 65 text_style 'rule_button_text'

# BOARD FOR DISPLAYING RULES OF MINIGAME2
default order_rules_mingame3 = 0

screen game_rules_minigame3:
    frame:
        margin (350, 80)
        padding (450, 500)
        if order_rules_mingame3 == 0:
            background im.FactorScale("images/ruleboard/rule_combat1.png", 2.0)
            textbutton "{b}NEXT{/b}" action SetVariable('order_rules_mingame3', order_rules_mingame3+1) xpos 65 ypos 65 text_style 'rule_button_text'
        
        elif order_rules_mingame3 == 1:
            background im.FactorScale("images/ruleboard/rule_combat2.png", 2.0)
            textbutton "{b}START{/b}" action SetVariable('order_rules_mingame3', order_rules_mingame3+1) xpos 65 ypos 65 text_style 'rule_button_text'
        
        elif order_rules_mingame3 == 2:
            background im.FactorScale("images/ruleboard/rule_combat3.png", 2.0)
            textbutton "{b}START{/b}" action SetVariable('order_rules_mingame3', order_rules_mingame3+1) xpos 65 ypos 65 text_style 'rule_button_text'
        
        elif order_rules_mingame3 == 3:
            background im.FactorScale("images/ruleboard/rule_combat4.png", 2.0)
            textbutton "{b}START{/b}" action SetVariable('order_rules_mingame3', order_rules_mingame3+1) xpos 65 ypos 65 text_style 'rule_button_text'
        elif order_rules_mingame3 == 4:
            background im.FactorScale("images/ruleboard/rule_combat5.png", 2.0)
            textbutton "{b}START{/b}" action Return() xpos 65 ypos 65 text_style 'rule_button_text'