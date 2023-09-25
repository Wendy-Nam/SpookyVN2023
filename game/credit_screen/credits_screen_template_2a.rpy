## 2a: The layout template with two columns for smaller credit blocks
# I used zoom 0.6 on the original image size, so here they're 150x150. But this is because I didn't want to add another image asset.

# Credits Screen 
screen template_2a():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"
        text "Credits" style "about_header" line_spacing 20
        
        if gui.about:
            text "[gui.about!t]\n"
        ## gui.about is usually set in options.rpy.
        null height 100 # manual vertical spacing

        # syntax: grid <amount_columns> <amount_rows>
        # You need to calculate this manually to fill in these <amount_columns> and <amount_rows> values.
        # Unused slots need to be filled with null (see the end of the code, because we got 7 elements while there is space for 8 (=2*4)).
        # vpgrid is also an option over grid depending on preference.
        # NOTE As fas as I know, you can't give fixed coordinates to grid slots, positions are calculated for slots in relation to each other.
        # Such as having long text strings in first column will push the second column more to the right. Play around with xspacing value for the look you want.
        grid 2 3:            
            # horizontal spacing
            xspacing -150
            # vertical spacing
            yspacing 50
            # Credit block
            for member in credit_list:
                hbox:
                    add member.image_name zoom 0.3
                    null width 25 # manual horizontal spacing
                    vbox:
                        null height 5 # yalign 0.5 is an alternative option, but yalign is more suited when there is equal amount of elements in this vbox
                        text member.name style "credits_name_small"
                        null height 10  # manual vertical spacing
                        text member.role style "credits_role_small"
                        null height 10
                        for link in member.url_list:
                            hbox:
                                add link[0] zoom 0.15 yalign 0.5
                                textbutton link[1] action OpenURL(link[1]) style "credits_url_button" text_style "credits_url_text_small"
            # fill unused grid spot (when amount is uneven) with null
            null
        null
        label "[config.name!t]"
        text _("Version [config.version!t]\n")
        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
        
        # style_prefix "about"
            
