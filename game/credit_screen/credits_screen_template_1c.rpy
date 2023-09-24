## 1c: Variant on the basic layout template with big credits blocks on each row.
# With dividers on the role category. These are only some examples of role categories.
# A person can be credited more than once when they fulfilled roles in multiple categories.

# Credits Screen 
screen template_1c():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("1c: one column, split into categories"), scroll="viewport"):

        style_prefix "about"

        # vbox for credits
        vbox:
            # spacing between each element
            spacing 50

            text "Credits:" style "about_header" 

            null height 25  # manual extra vertical spacing

            # "Director" divider
            text "Director:" style "credits_category_header" 

            # Credit block
            hbox:
                add "logo" # zoom 0.5 -> if images are not resized properly you can do it with zoom

                null width 50 # manual horizontal spacing

                vbox:
                    null height 10 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                    text "Gaming Variety Potato" style "credits_name"
                    null height 10  # manual vertical spacing
                    text "Lead & Concept" style "credits_role"
                    null height 30
                    hbox:
                        add "itch-io"
                        textbutton _("https://gaming-variety-potato.itch.io/" ) action OpenURL("https://gaming-variety-potato.itch.io/" ) style "credits_url_button" text_style "credits_url_text"  
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"                      

            null height 25  # manual extra vertical spacing

            # "Writing" divider
            text "Writing:" style "credits_category_header" 

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Gaming Variety Potato" style "credits_name"
                    null height 10
                    text "Script Writer" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Editor Name" style "credits_name"
                    null height 10
                    text "Editor" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            null height 25  # manual extra vertical spacing

            # "Art" divider
            text "Art:" style "credits_category_header" 

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Gaming Variety Potato" style "credits_name"
                    null height 10
                    text "General Artist" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Artist Name" style "credits_name"
                    null height 10
                    text "BG Artist" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"             

            null height 25  # manual extra vertical spacing

            # "Audio" divider
            text "Audio:" style "credits_category_header" 

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Musician Name" style "credits_name"
                    null height 10
                    text "OST Composer" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            null height 25  # manual extra vertical spacing

            # "Programmming" divider
            text "Programming:" style "credits_category_header" 

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Programmer Name" style "credits_name"
                    null height 10
                    text "GUI Programmer" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            null height 25  # manual extra vertical spacing

            # "VA" divider
            text "VA:" style "credits_category_header" 

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Voice Actor #1 Name" style "credits_name"
                    null height 10
                    text "Protagonist's Voice" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Voice Actor #2 Name" style "credits_name"
                    null height 10
                    text "Antagonist's Voice" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"            

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Voice Actor #3 Name" style "credits_name"
                    null height 10
                    text "Protagonist's Voice" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Voice Actor #4 Name" style "credits_name"
                    null height 10
                    text "Antagonist's Voice" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  

            # Credit block
            hbox:
                add "logo"

                null width 50  

                vbox:
                    null height 10
                    text "Voice Actor #5 Name" style "credits_name"
                    null height 10
                    text "Protagonist's Voice" style "credits_role"
                    null height 30
                    hbox:
                        add "twitter-original"
                        textbutton _("https://www.twitter.com/gaming_v_potato/") action OpenURL("https://www.twitter.com/gaming_v_potato/") style "credits_url_button" text_style "credits_url_text"  