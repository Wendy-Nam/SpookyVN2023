## 1d: Added extra things to 1b for showcase
# > Shows the use of AlphaMask on the avatar
# > Shows the use of Composite on the avatar
# > text blurb where team members have a small space to write anything

# - Uses credit_class.rpy (class definition)
# - Uses credit_list in init_credit_objects.rpy (initialisation of the list of credit class objects)

# NOTE: im (image manipulator) https://www.renpy.org/doc/html/im.html is deprecated, so transform equivalents should be used instead.
transform transform_avatar:
    zoom 0.8 # becomes 200x200
    matrixcolor SepiaMatrix() # becomes sepia
    

# Credits Screen 
screen template_1d():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("1d: 1b with AlphaMask, Composite, text blurbs"), scroll="viewport"):

        style_prefix "about"

        # vbox for credits
        vbox:
            text "Credits:" style "about_header"

            # spacing for each element
            spacing 50

            # For-loop for Credit blocks
            for credit in credit_list:
                hbox:
                    # uses default avatar in else, when no image is supplied... but in truth I only wanted to show both the AlphaMask and Composite examples on one screen.
                    if credit.image_name is not None:
                        add AlphaMask(credit.image_name, At("avatar_mask")) 
                    else:
                        add Composite(
                            (250, 250),
                            (0, 0), "avatar_mask",
                            (25, 25), At("logo", transform_avatar)
                        )

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

                # text blurb: instead of using this hard-coded string, add a new field to "Credit" class in credit_class.rpy, to store a text blurb. In init_credit_objects.rpy you can fill in the text content.
                text "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin eleifend, magna non efficitur suscipit, diam nisi euismod massa, id cursus mi sapien vel nisi. Phasellus ut lorem lorem. Maecenas aliquet suscipit blandit. Curabitur vitae auctor velit. Donec egestas diam ac nisi mattis, sed luctus ante fermentum. Aliquam erat volutpat. Aenean id velit sapien. Donec ligula lorem, dignissim at est convallis, scelerisque cursus arcu. Sed massa leo, iaculis quis ullamcorper quis, sodales et ligula."

                null height 10 # extra vertical space
                     
