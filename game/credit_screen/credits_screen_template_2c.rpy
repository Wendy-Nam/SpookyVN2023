## 2c: Lists split up into categories over 2 columns
# Added a for-loop over 2b's structure to loop over the categories.

# - Uses credit_class.rpy (class definition)
# - Uses categorised_credit_list in init_credit_objects.rpy (initialisation of the list of credit class objects)

# Credits Screen 
screen template_2c():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("2c: two columns, categorised lists"), scroll="viewport"):

        style_prefix "about"

        text "Credits:" style "about_header" 
        null height 100 # manual vertical spacing

        # Iterate over the categories
        for categorised_credits in categorised_credits_list:

            # Header for the credits category
            text categorised_credits.category style "credits_category_header" 
            null height 50 # manual vertical spacing

            # syntax: grid <amount_columns> <amount_rows>
            # vpgrid is also an option over grid depending on preference.
            # NOTE As fas as I know, you can't give fixed coordinates to grid slots, positions are calculated for slots in relation to each other.
            # Such as having long text strings in first column will push the second column more to the right. Play around with xspacing value for the look you want.

            $ amount_credits = len(categorised_credits.credit_list)
            $ is_odd = amount_credits % 2 == 1

            # // is floor division
            if is_odd:
                $ rows = amount_credits // 2 + 1
            else:
                $ rows = amount_credits // 2

            grid 2 rows:            
                # horizontal spacing
                xspacing 100
                # vertical spacing
                yspacing 100

                # For-loop for Credit blocks
                for credit in categorised_credits.credit_list:
                    hbox:
                        if credit.image_name is not None:
                            add credit.image_name zoom 0.6
                        else:
                            null width 150 # image width in px 
                            null height 150 # image height in px 

                        # distance between logo and text
                        null width 25 

                        vbox:
                            null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                            text credit.name style "credits_name_small"
                            null height 10
                            text credit.role style "credits_role_small"
                            null height 10

                            for url_tuple in credit.url_list:
                                hbox:
                                    if url_tuple[0] is not None:
                                        add url_tuple[0]
                                    else:
                                        null width 32 # image width in px     
                                    textbutton _(url_tuple[1]) action OpenURL(url_tuple[1]) style "credits_url_button" text_style "credits_url_text_small"

                # exited for-loop, check if 'null' is necessary to fill up empty space (when elements number is not even)
                if is_odd:
                    null

            null height 100 # manual vertical spacing
