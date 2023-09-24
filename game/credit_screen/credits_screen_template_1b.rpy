## 1b: Rewritten 1a to use a for-loop for each credit block in the screen.
# And within that for-loop, another for-loop for the urls.
# if-checks have been added for the spot where it's expecting an image, for example if you purposefully leave out an image.
# Assumes that images are of matching size (250x250)

# - Uses credit_class.rpy (class definition)
# - Uses credit_list in init_credit_objects.rpy (initialisation of the list of credit class objects)

# Credits Screen 
screen template_1b():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("1b: 1a implemented with for-loops"), scroll="viewport"):

        style_prefix "about"

        # vbox for credits
        vbox:
            text "Credits:" style "about_header"

            # spacing for each element
            spacing 50

            # For-loop for Credit blocks
            for credit in credit_list:
                hbox:
                    if credit.image_name is not None:
                        add credit.image_name
                    else:
                        null width 250 # image width in px 
                        null height 250 # image height in px 

                    # distance between logo and text
                    null width 50 

                    vbox:
                        null height 10 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text credit.name style "credits_name"
                        null height 10
                        text credit.role style "credits_role"
                        null height 30

                        for url_tuple in credit.url_list:
                            hbox:
                                if url_tuple[0] is not None:
                                    add url_tuple[0]
                                else:
                                    null width 32 # image width in px   
                                textbutton _(url_tuple[1]) action OpenURL(url_tuple[1]) style "credits_url_button" text_style "credits_url_text"


                     
