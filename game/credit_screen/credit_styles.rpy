## styles: change fonts, colours, et cetera over here

## style definitions

style about_header:
    size 60
    color "#FF8066"
    bold True
style credits_category_header:
    size 50
    color "#ffffff"

# inherit style from text_button
style credits_url_button is text_button

# inherit style from hyperlink_text
style credits_url_text is hyperlink_text
style credits_url_text:
    size 18
#########################################################################################################################    

# style definitions only used by template 2

style credits_name_small:
    size 25
    bold True
    color "#FF8066"
    xmaximum 300
style credits_role_small:
    size 20
    color "#c4c4c4"
    bold True

# inherit from hyperlink_text
style credits_url_text_small is hyperlink_text
style credits_url_text_small:
    size 20
    italic True