################################################################################
##
## Layered Image Visualizer by Feniks (feniksdev.itch.io / feniksdev.com)
##
################################################################################
## This file contains code for a layered image visualizer, designed to work
## alongside Image Tools, found here:
## https://feniksdev.itch.io/image-tools-for-renpy
##
## The files in Image Tools for Ren'Py are required in order for this code
## to work.
## If you use these tools during development, credit me as Feniks @ feniksdev.com
##
## This tool is designed to be used during development only, and should be
## excluded from a proper build. The code to do so is included with this file.
##
## It also has a visual component, and includes in-game tutorials you can
## go through to learn how to use the tools.
## To access the tools, simply make yourself a button (probably on the main
## menu) that goes to the main tool screen, image_tools:
##
# textbutton "Image Tools" action ShowMenu("image_tools")
##
## Then you can select a tool and get started. You will be shown the tutorial
## the first time you use a tool.
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################
## CONFIGURATION
################################################################################
init python in myconfig:
    _constant = True
    ## FOR YOU: Change this to False if you're having trouble with your images'
    ## DynamicDisplayable attributes showing up in the tool.
    FILTER_DYNAMIC_ATTRIBUTES = True

################################################################################
## VARIABLES
################################################################################
## Persistent ##################################################################
################################################################################
## The crop coordinates for a given tag. Persistent so you don't have to
## plug it in every time.
default persistent.sprt_crop_coords = dict()
## The layered image groups included for a given tag
default persistent.sprt_included_layeredimage_groups = dict()
## The attributes being applied to the image in the visual expression tool
default persistent.sprt_current_image_attributes = dict()
## The attributes which shouldn't be selected when randomizing attributes
default persistent.sprt_no_random_attributes = dict()
## A dictionary of layered image groups which have default attributes
default persistent.sprt_layeredimage_default_attributes = dict()

## Tutorial flags
default persistent.dev_crop_tutorial_shown = False
default persistent.dev_grid_tutorial_shown = False

## All the layered image groups for a given tag
default persistent.current_layeredimage_groups = dict()
## The size of the grid images
default persistent.sprt_grid_div = 9.0

## Normal ######################################################################
################################################################################
## A temporary holding ground to ensure an entered tag is a layered image tag
default sprt.temp_who = ""

################################################################################
## CONSTANTS
################################################################################
## The xmaximum of the image preview (full image image)
define sprt.PREVIEW_XMAX = int(config.screen_width//3.0)
## The ymaximum of the image preview (full image image)
define sprt.PREVIEW_YMAX = int(config.screen_height*4.0/5.0)
## The xmaximum of the cropped preview image
define sprt.CROP_XMAX = int(sprt.PREVIEW_XMAX/3.0*2.0)
## The ymaximum of the cropped preview image
define sprt.CROP_YMAX = sprt.CROP_XMAX
## The width of the visual grid
define sprt.GRID_WIDTH = int(config.screen_width/9.0*5.0)+int(config.screen_width/9.0/7.0*6.0)
## A dummy layered image to use until the user enters a proper one
define sprt.placeholder_layered_image = LayeredImage([Attribute("base", "base",
    Placeholder(), default=True)], name="sprt_placeholder")

################################################################################
## IMAGES
################################################################################
## The mouse images used for resizing. Based on some special ASCII characters.
image move = Text("↔", style="sprt_move_cursor")
image left_right_cursor = Text("↔", style="sprt_move_cursor")
image top_bottom_cursor = Text("↕", style="sprt_move_cursor")
image diagonal_cursor1 = Transform("move", rotate=-45, rotate_pad=False)
image diagonal_cursor2 = Transform("move", rotate=45, rotate_pad=False)
image move_cursor = Fixed("left_right_cursor",
    Transform("top_bottom_cursor", align=(0.5, 0.5)), fit_first=True)

style sprt_move_cursor:
    font "DejaVuSans.ttf"
    color "#fff"
    outlines [(1, "#000")]
    size sprt.BIG_TEXT
    align (0.5, 0.5)

## An image to use if the user hasn't entered a valid layered image tag
image notransform = Fixed(
    sprt.MAROON,
    Text("Click the button in the top left corner and\nselect How to Use to learn how to use the tool!",
        size=sprt.BIG_TEXT, color=sprt.WHITE, outlines=[(6, "#000")],
        align=(0.5, 0.5), text_align=0.5),
    xysize=(sprt.PREVIEW_XMAX, sprt.PREVIEW_YMAX)
)

################################################################################
## FUNCTIONS
################################################################################
init -80 python in sprt:

    from store import SetScreenVariable, LayeredImage, LayeredImageProxy

    def copy_visual_to_clipboard(copy_all=True):
        """
        Copy the image attributes to the clipboard. If copy_all is True, also
        copies the tag/name of the image. Otherwise, just copies the
        attributes (suitable for copying into dialogue, for example).
        This version is specifically for the visual expression grid.
        """
        global persistent
        attrs = construct_image_attributes(persistent.sprt_who).strip()
        if not copy_all:
            # Take out the tag
            attrs = attrs.replace(persistent.sprt_who, "").strip()
        copy_to_clipboard(attrs)

    def show_cropped_image(st, at, img, crop_rect):
        """
        Display the cropped version of the MakeRectangle CDD,
        in real-time. A DynamicDisplayable function.
        """
        return Transform(img, crop=crop_rect.crop_tuple), 0.01

    def save_crop_coords(who, rect):
        """
        Save the crop coordinates for this tag.
        """
        global persistent
        persistent.sprt_crop_coords[who] = rect.crop_tuple

    def get_layered_obj(who):
        """
        Get the LayeredImage object from the provided image name. Loops
        through LayeredImageProxy objects until it gets to the actual
        LayeredImage.
        """
        img = renpy.get_registered_image(who)
        while isinstance(img, LayeredImageProxy):
            img = renpy.get_registered_image(img.name)
        return img

    def get_multiple_attributes(img):
        """
        Get the attributes that are not part of a group in a layered image (that
        is, they're set to "multiple" so more than one can display at once).

        Parameters:
        -----------
        img : LayeredImage
            The LayeredImage to check the attributes of.
        """
        attrs = img.attributes
        groupless = [ ]
        for att in attrs:
            if att.group is None:
                groupless.append(att.attribute)
        return groupless

    def set_dev_expression_who(s):
        """
        A callback used on the visual expression tool to ensure
        persistent.sprt_who isn't set unless it's a valid
        layered image.

        Parameters:
        -----------
        s : string
            The name of the image to check.
        """
        global persistent
        if get_layered_image(s):
            persistent.sprt_who = s
            tg = s
            ## There are a bunch of screen variables to change when there's
            ## a valid layered image.
            renpy.run(SetScreenVariable("layered_obj",
                get_layered_image(tg)))
            renpy.run(SetScreenVariable("layered_img_groups",
                get_layered_obj(tg).group_to_attributes))
            renpy.run(SetScreenVariable("multiple_attributes",
                get_multiple_attributes(get_layered_obj(tg))))
            renpy.restart_interaction()

            check_expression_who(s)

    def construct_image_attributes(who, group=None, new_att=None,
            layered_img_groups=None):
        """
        Given the image tag, figure out which attributes should be applied
        to it. Allows swapping out a new attribute to display instead of
        the current one. Returns a string of the tag + attributes.

        Parameters:
        -----------
        who : string
            The name of the image to check.
        group : string
            If provided, the group the attribute being applied or removed is in.
        new_att : string
            If provided, the attribute to apply or remove.
        layered_img_groups : dict
            If provided, the groups and attributes for the layered image. Used
            to support short forms.
        """
        global persistent
        ## Grab the current image attributes
        ret = who
        if who.endswith(" notransform"):
            who = who[:-len(" notransform")]

        if group == "short forms" and new_att is not None:
            adjusted_attrs = adjust_short_form_conflicts(who, new_att,
                layered_img_groups)
            return ret + ' ' + adjusted_attrs

        attrs = persistent.sprt_current_image_attributes.setdefault(who, dict())

        for grp, val in attrs.items():
            ## Handle attributes where multiple can apply at a time
            if grp == "multiple":
                ret += " " + " ".join(val)
                if new_att is not None and new_att not in val:
                    ret += " " + new_att
            elif group == grp and new_att is None:
                # Remove this attribute/don't include it
                continue
            elif group != grp and val is not None:
                ret += " " + val

        if new_att is not None:
            ret += " " + new_att

        return ret

    def short_form_applied(who, short, layered_img_groups):
        """
        Return True if the provided short form is already applied to
        the image.

        Parameters:
        -----------
        who : string
            The name of the image to check.
        short : string
            The short form to check.
        layered_img_groups : dict
            The groups and attributes for the layered image.
        """
        global persistent
        ## Grab the current image attributes
        ret = who
        if who.endswith(" notransform"):
            who = who[:-len(" notransform")]

        attrs = persistent.sprt_current_image_attributes.setdefault(who, dict())

        if not attrs: # Empty dictionary
            return False

        ## Adjust the short form
        expanded = transform_attr(who, short)
        if expanded.startswith(who):
            expanded = expanded[len(who):].strip()
        ## Turn it into a list to iterate over
        expanded = expanded.split(' ')
        ## Get the current attributes and turn them into a list too
        original = construct_image_attributes(ret).split(' ')

        return set(expanded).issubset(set(original))

    def adjust_short_form_conflicts(who, short, layered_img_groups):
        """
        If the user is trying to apply a short form attribute which conflicts
        with an attribute already applied, remove the conflicting attribute
        and return the resulting attributes as a space-separated string.

        Parameters:
        -----------
        who : string
            The name of the image to check.
        short : string
            The short form being applied to the image.
        layered_img_groups : dict
            The groups and attributes for the layered image.
        """
        global persistent
        ## Grab the current image attributes. Returns a dict like eyes="angry"
        attrs = persistent.sprt_current_image_attributes.setdefault(who, dict())

        ## Adjust the short form
        expanded = transform_attr(who, short)
        if expanded.startswith(who):
            expanded = expanded[len(who):].strip()
        ## Turn it into a list to iterate over
        expanded = expanded.split(' ')
        conflicting_groups = [ ]
        short_group_dict = dict()

        ## Now find the group associated with each short form attribute
        for grp, atts in layered_img_groups.items():
            for att in atts:
                if att in expanded:
                    ## This is the group the short form attribute is in
                    conflicting_groups.append(grp)
                    short_group_dict[grp] = att
        ## Assume any leftovers are in the "multiple" group
        if len(expanded) > len(conflicting_groups):
            conflicting_groups.append("multiple")
            short_group_dict["multiple"] = [x for x in expanded if x not in short_group_dict.values()]

        new_current_attrs = attrs.copy()
        new_current_attrs["multiple"] = new_current_attrs.get("multiple", list()).copy()
        ## Replace any attributes which are in a conflicting group
        for grp, att in short_group_dict.items():
            if grp in conflicting_groups:
                if grp == 'multiple':
                    ## Can just append
                    if short_group_dict[grp] not in new_current_attrs.setdefault(grp, []):
                        new_current_attrs[grp].extend(short_group_dict[grp])
                else:
                    new_current_attrs[grp] = short_group_dict[grp]

        ## Put together that dictionary into a space-separated tag list
        ret = ''
        if new_current_attrs.get("multiple"):
            ret += ' '.join(new_current_attrs["multiple"])

        ret += ' '.join([x for x in new_current_attrs.values() if not isinstance(x, list) and x])

        return ret

    def toggle_shortform(short, layered_img_groups):
        """
        Apply or remove a short form from the image.

        Parameters:
        -----------
        short : string
            The short form to apply or remove.
        layered_img_groups : dict
            The groups and attributes for the layered image.
        """
        global persistent

        who = persistent.sprt_who

        expanded = transform_attr(who, short)
        if expanded.startswith(who):
            expanded = expanded[len(who):].strip()
        ## Turn it into a list to iterate over
        expanded = expanded.split(' ')
        used_attrs = [ ]

        attrs = persistent.sprt_current_image_attributes.setdefault(who, dict())

        if short_form_applied(who, short, layered_img_groups):
            ## Remove the short form
            for grp, atts in layered_img_groups.items():
                for att in atts:
                    if att in expanded:
                        attrs[grp] = get_attr_default(grp)
                        used_attrs.append(att)
            ## Make sure we didn't miss any that are in the multiple group
            leftovers = [x for x in expanded if x not in used_attrs]
            for le in leftovers:
                if le in attrs.setdefault("multiple", []):
                    attrs["multiple"].remove(le)

        else:
            ## Add the short form; remove any conflicting attributes
            for grp, atts in layered_img_groups.items():
                for att in atts:
                    if att in expanded:
                        attrs[grp] = att
                        used_attrs.append(att)
            ## Make sure we don't miss any multiple attributes
            leftovers = [x for x in expanded if x not in used_attrs]
            for le in leftovers:
                if le not in attrs.setdefault("multiple", []):
                    attrs["multiple"].append(le)


    def toggle_multiple_attribute(att, grp):
        """
        Append or remove the provided attribute from the image.

        Parameters:
        -----------
        att : string
            The attribute to apply or remove.
        grp : string
            The group the attribute is in. Used to change behaviour based on
            whether it's a "multiple" group or not.
        """
        global persistent
        who = persistent.sprt_who
        group_dict = persistent.sprt_current_image_attributes.setdefault(
            who, dict())
        if att is None and grp == "multiple":
            group_dict["multiple"] = [ ]
            return
        if att in group_dict.setdefault("multiple", []):
            group_dict["multiple"].remove(att)
        else:
            group_dict["multiple"].append(att)
        return

    def get_attr_default(grp):
        """
        Get the default value for this group.
        """
        global persistent
        return persistent.sprt_layeredimage_default_attributes.get(
            persistent.sprt_who, dict()).get(grp, None)

    def randomize_attributes(who, groups, multiple_attrs):
        """
        Randomly select attributes from selected layered image groups.

        Parameters:
        -----------
        who : string
            The name of the image to randomize attributes for.
        groups : dict
            A dictionary of all the groups in this layered image and their
            attributes.
        multiple_attrs : list
            A list of attributes which are applied at the same time.
        """
        global persistent

        possible_groups = persistent.sprt_included_layeredimage_groups.setdefault(
            who, list())
        ## For each group, randomly pick an attribute
        for grp in possible_groups:
            excluded_attributes = persistent.sprt_no_random_attributes.get(
                    who, dict()).get(grp, set())
            if grp == "short forms":
                continue
            elif grp == "multiple" and multiple_attrs:
                ## Multiple attributes to add
                multi = multiple_attrs.copy()
                ## Remove any excluded attributes
                multi = [x for x in multi if x not in excluded_attributes]
                ## Shuffle the list
                renpy.random.shuffle(multi)
                ## Pick a random selection of the attributes
                if None in excluded_attributes:
                    ## Can't have an empty list; ensure there's at least one
                    ## item (so long as they're not all excluded too)
                    if multi:
                        num = renpy.random.randint(1, len(multi))
                    else:
                        num = 0
                else:
                    num = renpy.random.randint(0, len(multi))
                group_dict = persistent.sprt_current_image_attributes.setdefault(
                    who, dict())
                group_dict["multiple"] = multi[:num]
                continue
            ## Group is "multiple" but there are no valid multiple attributes
            elif grp == "multiple":
                continue
            group_dict = persistent.sprt_current_image_attributes.setdefault(
                who, dict())
            ## Remove any excluded attributes
            possible_attrs = [x for x in list(groups[grp]) if (
                x not in excluded_attributes)]
            if persistent.sprt_layeredimage_default_attributes.get(who,
                    dict()).get(grp, None) is not None:
                ## Means there's a default attribute, so don't pick None
                random_attr = renpy.random.choice(possible_attrs)
            elif None in excluded_attributes:
                random_attr = renpy.random.choice(possible_attrs)
            else:
                random_attr = renpy.random.choice(possible_attrs + [None])

            group_dict[grp] = random_attr
        renpy.restart_interaction()

    def reset_all_attributes(groups):
        """
        Reset all currently applied attributes and all excluded attributes.
        """
        global persistent
        who = persistent.sprt_who
        for grp in groups.keys():
            persistent.sprt_current_image_attributes.setdefault(who, dict())[grp] = None
            persistent.sprt_no_random_attributes.setdefault(who, dict())[grp] = set()
        persistent.sprt_current_image_attributes.setdefault(who, dict())["multiple"] = [ ]

    def get_layered_image(s):
        """
        Return the LayeredImage if this is a LayeredImage or a
        LayeredImageProxy.

        Parameters:
        -----------
        s : string
            The name of the image to check.
        """
        if not s:
            return

        ## Strip it
        s = s.strip()
        ## Find out if it's a layered image
        img = renpy.get_registered_image(s)
        while isinstance(img, LayeredImageProxy):
            ## It's a proxy; get the real image
            img = renpy.get_registered_image(img.name)

        if img is None or not isinstance(img, LayeredImage):
            ## Doesn't exist or isn't a layered image
            return

        return img

    def check_expression_who(s):
        """
        A callback used by the input for persistent.sprt_who which
        confirms if the input is a valid layeredimage name or not.

        Parameters:
        -----------
        s : string
            The name of the image to check.
        """
        global persistent

        img = get_layered_image(s)
        if img is None:
            return

        ## It's a layered image. Grab the groups.
        groups_dict = img.group_to_attributes
        ## List of groups
        group_list = list(img.group_to_attributes.keys())
        persistent.current_layeredimage_groups[s] = group_list
        ## Figure out which groups have a default attribute and what it is
        find_default_attributes(img)

    def find_default_attributes(img):
        """
        Find the default attributes for each group in the layered image.
        Saves them in a persistent dictionary.

        Parameters:
        -----------
        img : LayeredImage
            The layered image to find the default attributes for.
        """
        global persistent

        attrs = img.attributes
        ## Reset the attributes
        persistent.sprt_default_attributes[persistent.sprt_who] = dict()

        for att in attrs:
            if att.default:
                persistent.sprt_default_attributes[
                    persistent.sprt_who][att.group] = att.attribute

## This is important to get layered images to work even if they have
## transforms applied to them
init 999 python in dev_tool:
    import store, copy
    renp_list = list(renpy.list_images())

    def no_dynamic_attributes(img):
        """
        Remove any DynamicDisplayables from the attributes of a layered image.
        """
        attrs = [ x for x in img.attributes ]
        new_attrs = [ ]
        new_layers = img.layers.copy()
        img.layers = new_layers

        for att in attrs:
            if isinstance(att.image, store.DynamicDisplayable):
                raw_child, redraw = att.image.function(0, 0,
                    *att.image.args, **att.image.kwargs)
                new_att = copy.copy(att)
                new_att.image = renpy.easy.displayable(raw_child)

                if att in img.layers:
                    img.layers.remove(att)
                    img.layers.append(new_att)
            else:
                new_att = att
            new_attrs.append(new_att)

        img.attributes = new_attrs

        return img

    for k in renp_list:
        # Is it a layered image?
        if k.endswith(" notransform"):
            continue
        layered_img = store.sprt.get_layered_image(k)
        if layered_img is None:
            continue
        # Yes. Make a version without any transforms for our tool
        new_img = store.LayeredImage([], name="{} notransform".format(k))
        new_img.__dict__ = layered_img.__dict__.copy()
        new_img.at = [ ]
        new_img.transform_args = {}
        new_img.fixed_args = dict(xfit=True, yfit=True)

        ## Go through and remove DynamicDisplayables from the attributes/make
        ## them static (one to save on calls and two so they don't blink
        ## a bunch when you crop them).
        if store.myconfig.FILTER_DYNAMIC_ATTRIBUTES:
            new_img = no_dynamic_attributes(new_img)

        renpy.image("{} notransform".format(k), new_img)

################################################################################
## CLASSES
################################################################################
init -80 python in sprt:

    from store import Null, Fixed
    import pygame

    class MakeRectangle(renpy.Displayable):
        """
        A CDD which allows the player to adjust a rectangle over an image.

        Attributes:
        -----------
        image : Displayable
            The image which is being cropped.
        width : int
            The width of the image (automatically calculated).
        height : int
            The height of the image (automatically calculated).
        dragging : bool
            Whether the player is currently dragging the cropping rectangle.
        which_edge : string
            The edge the player was closest to when dragging.
        drag_touchdown : tuple
            The position where the player touched the screen when dragging.
            Helps so the crop doesn't go off-screen.
        left : float
            The x coordinate of the left edge of the cropping rectangle.
        right : float
            The x coordinate of the right edge of the cropping rectangle.
        top : float
            The y coordinate of the top edge of the cropping rectangle.
        bottom : float
            The y coordinate of the bottom edge of the cropping rectangle.
        x : int
            The current x coordinate of the mouse.
        y : int
            The current y coordinate of the mouse.
        """
        ## How close the player has to be to the edge for it to be draggable
        CROP_SENSITIVITY = 0.05
        def __init__(self, image, *args, **kwargs):
            super(MakeRectangle, self).__init__(*args, **kwargs)

            self.image = renpy.easy.displayable(image)

            self.width = None
            self.height = None

            self.dragging = False
            self.which_edge = None
            self.drag_touchdown = None

            if kwargs.get('start_crop', None) is not None:
                start_crop = kwargs.get('start_crop', None)
                self.left = start_crop[0]
                self.top = start_crop[1]
                self.right = self.left + start_crop[2]
                self.bottom = self.top + start_crop[3]
            else:
                self.left = 0.0
                self.right = 1.0
                self.top = 0.0
                self.bottom = 1.0

            self.x = 0
            self.y = 0

            self.images_for_prediction = [
                self.image,
                renpy.get_registered_image('left_right_cursor'),
                renpy.get_registered_image('top_bottom_cursor'),
                renpy.get_registered_image('diagonal_cursor1'),
                renpy.get_registered_image('diagonal_cursor2'),
                renpy.get_registered_image('move_cursor'),
            ]

        def visit(self):
            return self.images_for_prediction

        @property
        def crop_tuple(self):
            """
            Returns a tuple of (x, y, width, height), suitable for crop
            rectangles or areas.
            """
            return (self.left, self.top, self.right-self.left,
                self.bottom-self.top)

        def rectangle(self):
            """
            Return the crop rectangle and any mouse images which should be
            rendered under the cursor.
            """
            if self.which_edge in ("left", "right"):
                mouse_img = Transform("left_right_cursor",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge in ("top", "bottom"):
                mouse_img = Transform("top_bottom_cursor",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge in ("top left", "bottom right"):
                ## Diagonal from top left to bottom right
                mouse_img = Transform("diagonal_cursor2",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge in ("top right", "bottom left"):
                ## Diagonal from top right to bottom left
                mouse_img = Transform("diagonal_cursor1",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge == "move":
                ## Moving the whole image at once
                mouse_img = Transform("move_cursor",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            else:
                ## Not within the valid event area
                mouse_img = Null()

            if self.which_edge:
                ## Make the mouse invisible if they're dragging so they
                ## can see the icons
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)

            ## The rectangle
            rect = Transform(construct_frame("#fff", "#0000"),
                xsize=self.right-self.left, ysize=self.bottom-self.top,
                xpos=self.left, ypos=self.top)
            resize_rect = Transform("#fff", xysize=(13, 13), anchor=(0.5, 0.5))
            rect_width = 5

            ret = Fixed(
                rect,
                ## Some squares around the rectangle to make it clear that it's
                ## for resizing
                Transform(resize_rect, xpos=self.left, ypos=self.top,
                    xoffset=rect_width//2, yoffset=rect_width//2),
                Transform(resize_rect, xpos=self.left, ypos=self.bottom,
                    xoffset=rect_width//2, yoffset=-rect_width//2),
                Transform(resize_rect, xpos=self.right, ypos=self.top,
                    xoffset=-rect_width//2, yoffset=rect_width//2),
                Transform(resize_rect, xpos=self.right, ypos=self.bottom,
                    xoffset=-rect_width//2, yoffset=-rect_width//2),
                Transform(resize_rect, xpos=(self.right-self.left)/2.0+self.left,
                    ypos=self.top, xoffset=rect_width//2,
                    yoffset=rect_width//2),
                Transform(resize_rect, xpos=(self.right-self.left)/2.0+self.left,
                    ypos=self.bottom, xoffset=rect_width//2,
                    yoffset=-rect_width//2),
                Transform(resize_rect, xpos=self.right,
                    ypos=(self.bottom-self.top)/2.0+self.top,
                    xoffset=-rect_width//2, yoffset=-rect_width//2),
                Transform(resize_rect, xpos=self.left,
                    ypos=(self.bottom-self.top)/2.0+self.top,
                    xoffset=rect_width//2, yoffset=-rect_width//2),
                ## The resizing arrows, if applicable
                mouse_img,
                xysize=(self.width, self.height)
            )
            return ret

        def render(self, width, height, st, at):
            """Render the crop rectangle to the screen."""

            ## Make it the size of the image
            if self.width is None:
                ## Get the image dimensions, so we can keep the crop area
                ## relative to the image dimensions
                ren = renpy.render(self.image, width, height, st, at)
                self.width = int(ren.width)
                self.height = int(ren.height)

            ## Create the initial render
            r = renpy.Render(self.width, self.height)

            rect = self.rectangle()
            img = Fixed(Transform(construct_frame(RED, "#0006"),
                    xysize=(self.width, self.height)),
                self.image, rect, xysize=(self.width, self.height))

            ## Render the rectangle and any little mouse images under the cursor
            ren = renpy.render(img, self.width, self.height, st, at)
            r.blit(ren, (0, 0))
            renpy.redraw(self, 0)
            return r

        def get_edge(self, x, y):
            """Return which edge(s) this point is near."""
            left = False
            right = False
            top = False
            bottom = False

            within_xbounds = (-self.CROP_SENSITIVITY+self.left < x
                < self.CROP_SENSITIVITY+self.right)
            within_ybounds = (-self.CROP_SENSITIVITY+self.top < y
                < self.CROP_SENSITIVITY+self.bottom)

            ## CROP_SENSITIVITY is so you don't have to be exactly at
            ## the edge for it to consider you able to drag from that edge
            if (self.left-self.CROP_SENSITIVITY < x
                    < self.left+self.CROP_SENSITIVITY):
                if within_ybounds:
                    left = True
            if (self.right-self.CROP_SENSITIVITY < x
                    < self.right+self.CROP_SENSITIVITY):
                if within_ybounds:
                    right = True
            if (self.top+self.CROP_SENSITIVITY > y
                    > self.top-self.CROP_SENSITIVITY):
                if within_xbounds:
                    top = True
            if (self.bottom+self.CROP_SENSITIVITY > y
                    > self.bottom-self.CROP_SENSITIVITY):
                if within_xbounds:
                    bottom = True

            ## Check for combos near the corners
            if left and top:
                return "top left"
            elif left and bottom:
                return "bottom left"
            elif right and top:
                return "top right"
            elif right and bottom:
                return "bottom right"
            ## Regular edges
            elif left:
                return "left"
            elif right:
                return "right"
            elif top:
                return "top"
            elif bottom:
                return "bottom"
            ## Somewhere in the middle for moving
            elif self.left < x < self.right and self.top < y < self.bottom:
                return "move"
            else:
                return None

        def restrict_crop_areas(self):
            """Ensure the crop area doesn't go below 0 or above 1."""
            self.left = max(0.0, self.left)
            self.right = min(1.0, self.right)
            self.top = max(0.0, self.top)
            self.bottom = min(1.0, self.bottom)

        def event(self, ev, x, y, st):
            """
            The event method for the crop rectangle. Listens for mouse button
            down, up, and movement events to detect clicking and dragging.
            """
            self.x = int(x)
            self.y = int(y)

            ## Make x/y relative to the image dimensions
            x = x / self.width
            y = y / self.height

            exact_sensitivity = (int(self.CROP_SENSITIVITY*self.width),
                                int(self.CROP_SENSITIVITY*self.height))

            within_xbounds = (-exact_sensitivity[0] < self.x
                < self.width+exact_sensitivity[0])
            within_ybounds = (-exact_sensitivity[1] < self.y
                < self.height+exact_sensitivity[1])

            if not (within_xbounds and within_ybounds) and not self.dragging:
                ## Out of bounds, not dragging
                if self.which_edge is not None:
                    self.which_edge = None
                    renpy.redraw(self, 0)
                return
            ## Make sure whichever edge is being hovered, that it's still active
            elif not self.dragging and self.which_edge is not None:
                current_edge = self.get_edge(x, y)
                if current_edge != self.which_edge:
                    self.which_edge = current_edge
                    renpy.redraw(self, 0)
                    return

            ####################################################################

            ## Dragging the mouse around
            if (ev.type == pygame.MOUSEMOTION and self.dragging
                    and self.which_edge is not None):

                if self.which_edge == "move":
                    # Moving the whole thing around
                    if x - self.drag_touchdown[0] < 0:
                        # Moving it left
                        self.left = (self.original_crop[0] + x
                            - self.drag_touchdown[0])
                        self.left = max(0.0, self.left)
                        # Adjust the right side to keep the width the same
                        self.right = self.left + (self.original_crop[2]
                            - self.original_crop[0])
                    else:
                        # Moving it right
                        self.right = (self.original_crop[2] + x
                            - self.drag_touchdown[0])
                        self.right = min(1.0, self.right)
                        # Adjust the left side to keep the width the same
                        self.left = self.right - (self.original_crop[2]
                            - self.original_crop[0])

                    if y - self.drag_touchdown[1] < 0:
                        # Moving it up
                        self.top = (self.original_crop[1] + y
                            - self.drag_touchdown[1])
                        self.top = max(0.0, self.top)
                        # Adjust the bottom side to keep the height the same
                        self.bottom = self.top + (self.original_crop[3]
                            - self.original_crop[1])
                    else:
                        # Moving it down
                        self.bottom = (self.original_crop[3] + y
                            - self.drag_touchdown[1])
                        self.bottom = min(1.0, self.bottom)
                        # Adjust the top side to keep the height the same
                        self.top = self.bottom - (self.original_crop[3]
                            - self.original_crop[1])

                    renpy.redraw(self, 0)
                    return

                ## Move the edge. Don't allow it to be completely
                ## 0 width/height though or you can't see the area
                if "left" in self.which_edge:
                    self.left = min(x, self.right-self.CROP_SENSITIVITY)
                if "right" in self.which_edge:
                    self.right = max(x, self.left+self.CROP_SENSITIVITY)
                if "top" in self.which_edge:
                    self.top = min(y, self.bottom-self.CROP_SENSITIVITY)
                if "bottom" in self.which_edge:
                    self.bottom = max(y, self.top+self.CROP_SENSITIVITY)
                self.restrict_crop_areas()

            ## Moving the mouse around but not dragging; add icon to show
            ## that they CAN drag it
            elif ev.type == pygame.MOUSEMOTION and not self.dragging:
                ## Is it close to an edge?
                self.which_edge = self.get_edge(x, y)

            ## Pressing down to start a drag
            elif (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1
                    and not self.dragging):
                self.dragging = True
                ## Is it close to an edge?
                self.which_edge = self.get_edge(x, y)
                ## Only let them drag the whole thing around if it's within
                ## the crop area
                if (self.which_edge == "move"):
                    ## Can move the whole thing from the center
                    self.drag_touchdown = (x, y)
                    self.original_crop = (self.left, self.top,
                                        self.right, self.bottom)
                else:
                    self.drag_touchdown = None

            ## Releasing the mouse button to end the drag
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.dragging = False
                self.drag_touchdown = None

            renpy.redraw(self, 0)

            if (within_xbounds and within_ybounds
                    and ev.type == pygame.MOUSEBUTTONUP
                    and ev.button == 1):
                ## Ignore the click
                raise renpy.IgnoreEvent()
            return

################################################################################
## SCREENS
################################################################################
screen layered_image_crop(demonstration=False):
    tag menu

    ## Ensure the user sees the tutorial the first time they open this screen
    if not persistent.sprt_tutorial2_shown:
        on 'replace' action ShowMenu("sprt_tutorial2")
        on 'show' action ShowMenu("sprt_tutorial2")

    ## The displayable with the crop square and the image
    default crop_rect = sprt.MakeRectangle(Transform(
        persistent.sprt_who + " notransform",
        xysize=(sprt.PREVIEW_XMAX, sprt.PREVIEW_YMAX),
        fit="contain"),
        start_crop=persistent.sprt_crop_coords.get(persistent.sprt_who, None))

    ## Note: if you have DynamicDisplayables as part of a layered image (e.g.
    ## for blinking) this can cause them to blink very rapidly as the image
    ## updates in real-time.
    default cropped_img = DynamicDisplayable(
        sprt.show_cropped_image,
        img=persistent.sprt_who + " notransform",
        crop_rect=crop_rect
    )

    add sprt.GRAY

    vbox:
        style_prefix 'sprt_crop'
        text "Click and drag the white box edges to select a crop area"
        hbox:
            fixed:
                ## The image with the rectangle for cropping
                add crop_rect
            vbox:
                text "Preview"
                fixed:
                    xysize (sprt.CROP_XMAX, sprt.CROP_YMAX)
                    frame:
                        background sprt.construct_frame(sprt.RED, sprt.BLUE, sprt.PADDING)
                        add cropped_img fit "contain" align (0.5, 0.5):
                            xysize (sprt.CROP_XMAX, sprt.CROP_YMAX)
        textbutton _("Confirm"):
            action [Function(sprt.save_crop_coords, persistent.sprt_who,
                        crop_rect),
                    ShowMenu("layered_image_visualizer")]

    use hamburger_menu():
        style_prefix 'hamburger'
        textbutton _("Return") action Return()
        textbutton "How to Use" action ShowMenu("sprt_tutorial2")

screen layered_image_visualizer(demonstration=False):
    tag menu

    ## Ensure the user sees the tutorial the first time they open this screen
    if not persistent.sprt_tutorial3_shown:
        on 'replace' action ShowMenu("sprt_tutorial3")
        on 'show' action ShowMenu("sprt_tutorial3")

    default layered_obj = sprt.placeholder_layered_image if not sprt.get_layered_image(persistent.sprt_who) else sprt.get_layered_obj(persistent.sprt_who)
    default layered_img_groups = layered_obj.group_to_attributes
    default multiple_attributes = sprt.get_multiple_attributes(layered_obj)
    default sprt_who_input = SpecialInputValue(sprt, 'temp_who',
        set_callback=sprt.set_dev_expression_who,
        starting_value=persistent.sprt_who)
    default dev_hide_groups = False
    default compact_layout = False

    predict False ## Too much happening in this screen to predict

    add sprt.GRAY

    ## The tag input
    frame:
        style_prefix 'sprt_small'
        xpos sprt.MENU_SIZE+sprt.SPACER*2
        has hbox
        textbutton "Tag:" action CaptureFocus("tag_drop")

        button:
            style_prefix 'sprt_input'
            key_events True
            selected renpy.get_editable_input_value() == (sprt_who_input, True)
            action [sprt_who_input.Toggle(),
                Function(sprt.save_xyinitial),
                ## Ensure we don't have attribute conflicts
                If(not sprt_who_input.editable,
                [SetField(sprt, "what", ""),
                SetField(sprt, "swap_attr", "")])]
            input value sprt_who_input allow sprt.INPUT_ALLOW

        textbutton "Clear":
            sensitive sprt.temp_who
            action [SetField(sprt, "temp_who", ""),
                    SetField(persistent, "sprt_who", ""),
                    ## Also clear the attributes associated with them
                    SetField(sprt, "what", ""),
                    Function(sprt.save_xyinitial),
                    SetField(sprt, "swap_attr", "")]
        textbutton "Save":
            sensitive (persistent.sprt_who
                and persistent.sprt_who not in persistent.sprt_tags)
            action [AddToSet(persistent.sprt_tags, persistent.sprt_who),
                Notify("Saved!")]

    frame:
        style_prefix 'sprt_grid'
        has vbox
        null height sprt.PADDING
        hbox:
            xalign 0.5 spacing int(sprt.SPACER/2)
            textbutton "Size -":
                style_prefix 'sprt_small'
                action SetField(persistent, "sprt_grid_div",
                    persistent.sprt_grid_div+0.5)
            textbutton "{} Groups".format(
                    "Show" if dev_hide_groups else "Hide"):
                style_prefix 'sprt_small'
                action ToggleScreenVariable("dev_hide_groups")
            textbutton "Reset":
                style_prefix 'sprt_small'
                action Function(sprt.reset_all_attributes, layered_img_groups)
            textbutton "Swap Layout":
                style_prefix 'sprt_small'
                action ToggleScreenVariable("compact_layout")
            textbutton "Size +":
                style_prefix 'sprt_small'
                action SetField(persistent, "sprt_grid_div",
                    persistent.sprt_grid_div-0.5)
        if not dev_hide_groups:
            null height int(sprt.SPACER/2)
            hbox:
                style_prefix 'sprt_groups'
                for g in sorted(persistent.current_layeredimage_groups.get(
                        persistent.sprt_who, [])):
                    textbutton g:
                        action ToggleSetMembership(
                            persistent.sprt_included_layeredimage_groups.setdefault(
                                persistent.sprt_who, list()), g)
                if multiple_attributes:
                    textbutton "multiple":
                        action ToggleSetMembership(
                            persistent.sprt_included_layeredimage_groups.setdefault(
                                persistent.sprt_who, list()),
                                "multiple")
                if persistent.sprt_who and any(filter(lambda x : sprt.has_adjusted_attr(
                        persistent.sprt_who, x), persistent.sprt_shortforms)):
                    ## Has short forms
                    textbutton "short forms":
                        action ToggleSetMembership(
                            persistent.sprt_included_layeredimage_groups.setdefault(
                                persistent.sprt_who, list()),
                                "short forms")
        null height int(sprt.SPACER/2)

        # Add a divider
        add Transform("#fff2", ysize=max(1, config.screen_height//300), yalign=1.0)

        viewport:
            mousewheel True draggable True
            scrollbars "vertical"
            style_prefix 'sprt_disp'
            has vbox
            if compact_layout:
                box_layout "horizontal" style 'sprt_disp_hbox'
            for grp in persistent.sprt_included_layeredimage_groups.get(
                    persistent.sprt_who, list()):
                if not compact_layout:
                    label grp
                    hbox:
                        use sprt_grid_button(multiple_attributes, grp,
                            layered_img_groups)
                else:
                    label grp style 'sprt_disp2_label':
                        xsize int(config.screen_width/persistent.sprt_grid_div)-sprt.PADDING*2
                    use sprt_grid_button(multiple_attributes, grp,
                        layered_img_groups)

            null height sprt.SPACER

    hbox:
        style_prefix 'sprt_copy'
        textbutton "Copy All":
            action Function(sprt.copy_visual_to_clipboard, True)
        textbutton "Copy Attrs":
            action Function(sprt.copy_visual_to_clipboard, False)

    vbox:
        style_prefix 'sprt_final'
        add sprt.construct_image_attributes(persistent.sprt_who
                + " notransform"):
            crop persistent.sprt_crop_coords.get(persistent.sprt_who,
                (0.0, 0.0, 1.0, 1.0))
            fit "contain" xsize int(config.screen_width/7.0)*2
            ysize int(config.screen_height//5*2)
            xalign 0.5
        hbox:
            textbutton "Update crop":
                style_prefix 'sprt_small'
                action ShowMenu("layered_image_crop")
            textbutton "Randomize" action Function(sprt.randomize_attributes,
                    persistent.sprt_who, layered_img_groups,
                    multiple_attributes):
                style_prefix 'sprt_small'
        fixed:
            xsize int(config.screen_width/7.0)*2
            ysize int(config.screen_height//5*2)
            add sprt.construct_image_attributes(persistent.sprt_who
                    + " notransform"):
                fit "contain" xsize int(config.screen_width/7.0)*2
                ysize int(config.screen_height//5*2)
                xalign 0.5
            text sprt.construct_image_attributes(persistent.sprt_who):
                style 'sprt_disp_text'

    if GetFocusRect("tag_drop"):
        add sprt.GRAY alpha 0.7
        dismiss action ClearFocus("tag_drop")
        nearrect:
            focus "tag_drop"
            frame:
                modal True style_prefix 'sprt_drop'
                has vbox
                for tg in sorted([x for x in persistent.sprt_tags
                        if sprt.get_layered_image(x) is not None]):
                    hbox:
                        textbutton tg:
                            yalign 0.5 text_yalign 0.5
                            action [SetField(sprt, "what", ""),
                                SetField(sprt, "swap_attr", ""),
                                SetField(persistent, "sprt_who", tg),
                                SetField(sprt, "temp_who", tg),
                                SetScreenVariable("layered_obj",
                                    sprt.get_layered_image(tg)),
                                SetScreenVariable("layered_img_groups",
                                    sprt.get_layered_obj(tg).group_to_attributes),
                                SetScreenVariable("multiple_attributes",
                                    sprt.get_multiple_attributes(sprt.get_layered_obj(tg))),
                                ClearFocus("tag_drop"),
                                If(persistent.sprt_crop_coords.get(
                                    persistent.sprt_who, None) is None,
                                    ShowMenu("layered_image_crop"))]
                        textbutton "(Remove)" size_group None:
                            background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                            hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                            action RemoveFromSet(persistent.sprt_tags, tg)

    use hamburger_menu():
        style_prefix 'hamburger'
        textbutton _("Return") action Return()
        textbutton "How to Use" action ShowMenu("sprt_tutorial3")

## A helper screen to facilitate two different layouts
screen sprt_grid_button(multiple_attributes, grp, layered_img_groups):
    if grp == "short forms":
        ## Special case for short forms
        for exp in sorted(filter(lambda x : sprt.has_adjusted_attr(
                persistent.sprt_who, x), persistent.sprt_shortforms)):
            use expression_button(exp, grp, False, True,
                layered_img_groups)
    elif multiple_attributes and grp == "multiple":
        for exp in sorted(multiple_attributes):
            use expression_button(exp, grp, True)
    else:
        ## Show the image preview with the attribute
        for exp in sorted(layered_img_groups[grp]):
            use expression_button(exp, grp, False)
    if grp != "short forms" and persistent.sprt_layeredimage_default_attributes.get(
            persistent.sprt_who,
            dict()).get(grp, None) is None:
        ## There is no default attribute for this group
        ## Option for "None"
        use expression_button(None, grp, (grp == "multiple"))

## Helper screen to display the cropped image with the correct
## attribute(s)
screen expression_button(exp, grp, is_multiple=False,
        is_short=False, layered_img_groups=None):
    button:
        if is_multiple:
            if exp is None:
                selected not (persistent.sprt_current_image_attributes.get(
                persistent.sprt_who, dict()).get("multiple", []))
            else:
                selected exp in (persistent.sprt_current_image_attributes.get(
                    persistent.sprt_who, dict()).get("multiple", []))
        elif is_short:
            selected sprt.short_form_applied(persistent.sprt_who + " notransform",
                exp, layered_img_groups)
        else:
            selected (persistent.sprt_current_image_attributes.get(
                persistent.sprt_who, dict()).get(grp, None) == exp)

        if is_multiple:
            action Function(sprt.toggle_multiple_attribute, exp, grp)
        elif is_short:
            action Function(sprt.toggle_shortform, exp, layered_img_groups)
        else:
            action If(persistent.sprt_current_image_attributes.get(
                persistent.sprt_who, dict()).get(grp, None) == exp,
            SetDict(persistent.sprt_current_image_attributes.setdefault(
            persistent.sprt_who, dict()), grp, sprt.get_attr_default(grp)),
            SetDict(persistent.sprt_current_image_attributes.setdefault(
            persistent.sprt_who, dict()), grp, exp))

        ## Right-click to set whether this attribute
        ## is excluded from randomization
        if not is_short:
            alternate ToggleSetMembership(
                persistent.sprt_no_random_attributes.setdefault(
                persistent.sprt_who, dict()).setdefault(grp, set()), exp
            )
        if exp in persistent.sprt_no_random_attributes.get(
                persistent.sprt_who, dict()).get(grp, set()):
            foreground sprt.construct_frame(sprt.MAROON, "#0000", sprt.PADDING)
            hover_foreground sprt.construct_frame(sprt.RED, "#0000", sprt.PADDING)
            selected_foreground sprt.construct_frame(sprt.ORANGE, "#0000", sprt.PADDING)
            background sprt.construct_frame("#5b0202", "#880303dd", sprt.PADDING)
        has fixed:
            fit_first True
        add sprt.construct_image_attributes(
                persistent.sprt_who + " notransform", grp, exp, layered_img_groups):
            crop persistent.sprt_crop_coords.get(persistent.sprt_who,
                (0.0, 0.0, 1.0, 1.0))
            fit "contain" xsize int(config.screen_width/persistent.sprt_grid_div)-sprt.PADDING*2
            align (0.5, 0.5)
            if exp in persistent.sprt_no_random_attributes.get(
                    persistent.sprt_who, dict()).get(grp, set()):
                matrixcolor SaturationMatrix(0.5)
        if exp is None:
            text "(None)"
        else:
            text exp

################################################################################
## STYLES
################################################################################
## Note that these are also coded in a fairly specific way in order to adapt
## to various projects. It borrows heavily from default styling without relying
## on any images so the tool can be as lightweight as possible.
style sprt_crop_button:
    xalign 0.5 yalign 1.0 bottom_margin 30
    is sprt_small_button
style sprt_crop_button_text:
    is sprt_small_button_text
style sprt_crop_vbox:
    xalign 0.5 yalign 0.5
    spacing int(sprt.SPACER/2.0)
style sprt_crop_text:
    is sprt_text
    layout "subtitle" xalign 0.5 text_align 0.5
style sprt_crop_hbox:
    xalign 0.5 yalign 0.5
style sprt_crop_fixed:
    xysize (sprt.PREVIEW_XMAX, sprt.PREVIEW_YMAX)

style sprt_final_vbox:
    xalign 1.0 yalign 1.0 spacing sprt.PADDING*4
    xsize config.screen_width-sprt.GRID_WIDTH-sprt.SPACER
style sprt_final_hbox:
    spacing sprt.PADDING*4 xalign 0.5

style sprt_disp_label:
    background None yalign 0.5
    ypadding sprt.PADDING
style sprt_disp_label_text:
    is sprt_text
    size sprt.BIG_TEXT
    color sprt.YELLOW
style sprt_disp2_label:
    background sprt.YELLOW align (0.5, 0.5)
    size_group 'sprt_exp_button'
style sprt_disp2_label_text:
    is sprt_disp_label_text
    size sprt.MED_TEXT
    color sprt.GRAY
    align (0.5, 0.5) text_align (0.5)
style sprt_disp_hbox:
    spacing int(sprt.SPACER/2.5)
    box_wrap_spacing int(sprt.SPACER/2.5) box_wrap True
    xmaximum sprt.GRID_WIDTH
style sprt_disp_button:
    size_group 'sprt_exp_button'
    background None
    hover_background sprt.construct_frame(sprt.ORANGE, "#fff2", sprt.PADDING)
    selected_background sprt.construct_frame(sprt.RED, "#fff1", sprt.PADDING)
    selected_hover_background sprt.construct_frame(sprt.RED, "#fff2", sprt.PADDING)
style sprt_disp_button_text:
    is sprt_text
style sprt_disp_text:
    is sprt_text
    size sprt.SMALL_TEXT
    outlines [(1, "#000b")]
    align (0.5, 1.0)
    layout 'subtitle'
style sprt_disp_vscrollbar:
    base_bar sprt.MAROON
    thumb sprt.RED
    xsize sprt.PADDING*3
    xoffset -sprt.PADDING
    unscrollable "hide"

style sprt_grid_frame:
    ysize config.screen_height-sprt.MENU_SIZE-sprt.SPACER*2
    yalign 1.0
    xsize sprt.GRID_WIDTH+sprt.PADDING*2
    background sprt.construct_frame(sprt.RED, sprt.BLUE, sprt.PADDING)
    padding (sprt.PADDING, sprt.PADDING)
style sprt_grid_vbox:
    xsize sprt.GRID_WIDTH

style sprt_groups_hbox:
    spacing int(sprt.SPACER/2) box_wrap True box_wrap_spacing int(sprt.SPACER/2)
    xmaximum sprt.GRID_WIDTH
style sprt_groups_button:
    left_padding sprt.SPACER+sprt.PADDING
    background sprt.construct_checkbox(sprt.RED, inside="#000d",
        width=sprt.PADDING, box_size=(sprt.SPACER, sprt.SPACER), checked=False)
    selected_background sprt.construct_checkbox(sprt.RED, inside="#000d",
        width=sprt.PADDING, box_size=(sprt.SPACER, sprt.SPACER), checked=True)
style sprt_groups_button_text:
    is sprt_small_button_text
    hover_color sprt.ORANGE

################################################################################
## TUTORIAL
################################################################################
## Note that this is coded in a pretty specific way due to the flexibility
## of the tool. It's not meant to be a good example of how to code a screen,
## in particular due to the repeated code. Normally it would be easier to
## have images showing highlighted areas of the screen, which isn't possible
## here due to how the tool adapts to different projects + I didn't want to
## include unnecessary images in the tool.
################################################################################
init 30 python in sprt:
    tut2 = Tutorial(
        TutorialText(None, "Layered Image Crop Tool",
        "This tool will let you select an area of an image to display expression variations on in the layered image visualizer.",
        "You can click and drag from the edges of the white box on the left of the screen to adjust its position over your image.",
        "A preview of the results is to the right of the image, in a red box.",
        "When you're done adjusting the crop area, click \"Confirm\" at the bottom of the screen.",
        "Click on the white crop rectangle to test out the cropping functionality, or click anywhere else to close this tutorial.",
        xalign=1.0, xsize=int(config.screen_width/5.0*2.0))
    )

    tut3 = Tutorial(
        TutorialText("intro", "Welcome to the Layered Image Visualizer!",
        "This tool provides a more visual way to select character expressions. It's currently only designed to work with layered images.",
        "This tutorial will show you how to use the tool.",
        xalign=0.5),
        TutorialText("tag1", "Entering an image tag",
        "The first thing you need to do is type an image tag in the input box beside the \"Tag\" button.",
        "(This is just a tutorial so you can't type anything here, now!)",
        "This can be be any image tag, but it's usually a character name like \"eileen\", or sometimes a multi-word tag like \"side mc\" or \"bg\" for backgrounds.",
        "The \"Clear\" button will remove all text in the tag field.",
        xalign=1.0),
        TutorialText("tag2", "Saving an Image Tag",
        "You can also save tags to quickly access later with the \"Save\" button.",
        "Tags that you've saved can be accessed by clicking the \"Tag\" text to the left of the input box.",
        "This will show a dropdown of all the tags you've saved. Click \"(Remove)\" to remove a saved tag from this list, or click the tag itself to switch to it.",
        "Clicking on a tag or anywhere outside of the dropdown will close the dropdown.",
        xalign=1.0),
        TutorialText("crop1", "Cropping an Image",
        "After entering an image tag, you should see the image displayed on the right side of the screen.",
        "Remember that this tool only works with layered images, so regular image tags won't work, unless they're a layered image.",
        "In the middle of the screen is a button that says \"Update crop\". Click this to open the cropping screen.",
        "Once you've cropped your image, you will be returned to this screen."
        ),
        TutorialText("groups", "Image Groups",
        "Once you've entered a valid layered image, the viewport on the left will show a list of groups you declared for that layered image.",
        "Click on a group to display all the attributes in that group in the grid below.",
        "You can use the \"Size\u00A0-\" and \"Size\u00A0+\" buttons to adjust the size of the images in the grid, and the \"Hide Groups\" button to hide the groups list.",
        "The \"Swap Layout\" button will switch between a more compact layout and a more spread out layout.",
        xalign=1.0, xsize=int(config.screen_width-sprt.GRID_WIDTH-sprt.PADDING*2)
        ),
        TutorialText("groups2", "Special Groups",
        "There are two special groups you may see for your images: {b}multiple{/b} and {b}short forms{/b}.",
        "The {b}multiple{/b} group will contain any attributes you declared as \"multiple\", i.e. more than one attribute in that group can be applied at the same time. You can toggle multiple of these attributes at once.",
        "The {b}short forms{/b} group is only present if you've entered short forms using the {b}Image Attributes Tool{/b}, and at least one of the short forms applies to the current image. It will contain the short forms you've entered, and will correctly swap out multiple attributes at once when you apply it.",
        "If you need more information on short forms, click the {b}How To Use{/b} button on the {b}Image Attributes Tool{/b} screen.",
        xalign=1.0, xsize=int(config.screen_width-sprt.GRID_WIDTH-sprt.PADDING*2)
        ),
        TutorialText("attrs1", "Selecting Attributes",
        "The images in the attribute grid use the crop area you selected earlier. You can use it to narrow in on the desired attribute area, such as a sprite's face, so you can see it change.",
        "The name of the attribute is displayed at the bottom of the image. Click on the image to select it, and it will be applied to the image on the right.",
        "After you've selected an attribute, the preview images for other attributes will update so you can see how a new attribute will look with your currently selected attributes.",
        xalign=1.0, xsize=int(config.screen_width-sprt.GRID_WIDTH-sprt.PADDING*2)
        ),
        TutorialText("random1", "Randomizing Attributes",
        "You can also randomize attributes by clicking the \"Randomize\" button on the right side of the screen.",
        "It will only select attributes from the groups you checked off earlier. It's a good way to experiment with attribute combinations you might not have thought of, or to find errors with your images.",
        "If you don't want a group to be included in the randomization, just click on the group on the left to exclude it. You can always add it back and apply attributes from that group to the image manually later.",
        ),
        TutorialText("random2", "Randomizing Attributes 2",
        "You can also right-click on a particular attribute so that it isn't selected when randomization is used. It will have a red background to indicate it's excluded from randomization, but you can still manually add it to the expression.",
        "Right-click on the attribute again to allow it to be part of randomization again.",
        "You can also use the \"Reset\" button at the top of the grid to reset all the attributes you excluded from randomization, and set all the image attributes to their default values.",
        xalign=1.0, xsize=int(config.screen_width-sprt.GRID_WIDTH-sprt.PADDING*2)
        ),
        TutorialText("copy1", "Copying Attributes",
        "There are two buttons in the top right corner which will let you copy the image attributes to your clipboard so you can paste it into your script.",
        "The first is the \"Copy All\" button, which will copy {b}both{/b} the image tag {b}and{/b} the currently applied attributes to the clipboard.",
        "This makes it most suitable for use with the {b}show{/b} statement."),
        TutorialText("copy2", "Copying Attributes 2",
        "So, if your character tag is \"eileen\", and you've applied the attributes \"happy_eyes\" and \"happy_mouth\" to her, \"Copy All\" will copy the text {b}show eileen happy_eyes happy_mouth{/b} to your clipboard.",
        "You can then paste that into your script wherever you like."),
        TutorialText("copy3", "Copying Attributes 3",
        "The second is the \"Copy Attrs\" button, which will only copy the currently applied attributes and NOT the image tag.",
        "This makes it most suitable for side images or attributes applied during dialogue, like {b}e happy_eyes \"Some happy dialogue.\"{/b}.",
        "So, if your character tag is \"eileen\" and you've applied the attributes \"happy_eyes\" and \"happy_mouth\" to her, \"Copy Attrs\" will copy the text {b}happy_eyes happy_mouth{/b} to your clipboard.", "You can then paste that into your script wherever you like."),
        TutorialText("conclusion", "Conclusion",
        "And that's everything! I hope this helped you learn how to use the layered image visualizer, and that it helps you during development.",
        "To view this tutorial again, click the three lines in the top left corner and select \"How to Use\".",
        "If you run into any problems or have questions, feel free to leave a comment on itch.io.",
        "You can find more of my Ren'Py tools at {a=https://feniksdev.itch.io/}feniksdev.itch.io{/a}.",
        xalign=0.5)
    )

screen sprt_tutorial2():
    tag menu
    on 'show' action SetField(persistent, 'sprt_tutorial2_shown', True)
    on 'replace' action SetField(persistent, 'sprt_tutorial2_shown', True)

    default step = 0

    add sprt.GRAY

    ## Click anywhere to continue
    dismiss action If(step < sprt.tut2.length-1, SetScreenVariable("step", step+1), ShowMenu("layered_image_crop"))
    key 'dismiss' action If(step < sprt.tut2.length-1, SetScreenVariable("step", step+1), ShowMenu("layered_image_crop"))
    ## Esc or right-click to exit the tutorial
    key 'game_menu' action ShowMenu("layered_image_crop")
    ## Rollback to see the previous step
    key 'rollback' action SetScreenVariable("step", max(step-1, 0))

    ############################################ Duplicate code
    default crop_rect = sprt.MakeRectangle(Transform(
        Transform(Placeholder(), zoom=1.5),
        xysize=(sprt.PREVIEW_XMAX, sprt.PREVIEW_YMAX),
        fit="contain"),
        start_crop=(0.05, 0.1, 0.8, 0.4))

    default cropped_img = DynamicDisplayable(
        sprt.show_cropped_image,
        img=Transform(Placeholder(), zoom=1.5),
        crop_rect=crop_rect
    )

    vbox:
        style_prefix 'sprt_crop' xanchor 0.0 xpos sprt.MENU_SIZE+sprt.SPACER
        text "Click and drag the white box edges to select a crop area"
        hbox:
            fixed:
                ## The image with the rectangle for cropping
                add crop_rect
            vbox:
                text "Preview"
                fixed:
                    xysize (sprt.CROP_XMAX, sprt.CROP_YMAX)
                    frame:
                        background sprt.construct_frame(sprt.RED, sprt.BLUE, sprt.PADDING)
                        add cropped_img fit "contain" align (0.5, 0.5):
                            xysize (sprt.CROP_XMAX, sprt.CROP_YMAX)
        textbutton _("Confirm") foreground "#000b"
    ############################################

    use sprt_tutorial_text(sprt.tut2, step, None)

screen sprt_tutorial3():
    tag menu
    on 'show' action SetField(persistent, 'sprt_tutorial3_shown', True)
    on 'replace' action SetField(persistent, 'sprt_tutorial3_shown', True)

    default step = 0

    add sprt.GRAY
    ############################################################ Duplicate code
    default layered_obj = sprt.placeholder_layered_image
    default layered_img_groups = layered_obj.group_to_attributes
    default multiple_attributes = sprt.get_multiple_attributes(layered_obj)

    ## The tag input
    frame:
        if sprt.tut3.after_id("tag2", step):
            foreground Transform(sprt.GRAY, alpha=0.9)
        style_prefix 'sprt_small'
        xpos sprt.MENU_SIZE+sprt.SPACER*2
        has hbox
        textbutton "Tag:" action NullAction():
            if sprt.tut3.tut(step).id != "tag2":
                foreground "#000b"
        button:
            style_prefix 'sprt_input'
            if sprt.tut3.tut(step).id != "tag1":
                foreground "#000b"
            key_events True
            action NullAction()
            text "eileen" style "sprt_input_input"

        textbutton "Clear" action NullAction():
            if sprt.tut3.tut(step).id != "tag1":
                foreground "#000b"
        textbutton "Save" action NullAction():
            if sprt.tut3.tut(step).id != "tag2":
                foreground "#000b"

    frame:
        style_prefix 'sprt_grid'
        if (not sprt.tut3.between_ids("groups", "attrs1", step)
                and sprt.tut3.tut(step).id != "random2"):
            foreground Transform(sprt.GRAY, alpha=0.9)
        has vbox
        xsize sprt.GRID_WIDTH
        null height sprt.PADDING
        hbox:
            xalign 0.5 spacing int(sprt.SPACER/2)
            textbutton "Size -":
                if not sprt.tut3.tut(step).id in ("groups", "groups2"):
                    foreground "#000b"
                style_prefix 'sprt_small'
                action NullAction()
            textbutton "Show Groups":
                if not sprt.tut3.tut(step).id in ("groups", "groups2"):
                    foreground "#000b"
                style_prefix 'sprt_small'
                action NullAction()
            textbutton "Reset":
                if not sprt.tut3.tut(step).id == "random2":
                    foreground "#000b"
                style_prefix 'sprt_small'
                action NullAction()
            textbutton "Swap Layout":
                if not sprt.tut3.tut(step).id in ("groups", "groups2"):
                    foreground "#000b"
                style_prefix 'sprt_small'
                action NullAction()
            textbutton "Size +":
                if not sprt.tut3.tut(step).id in ("groups", "groups2"):
                    foreground "#000b"
                style_prefix 'sprt_small'
                action NullAction()
        null height int(sprt.SPACER/2)
        hbox:
            style_prefix 'sprt_groups'
            for g in ("base", "brows", "eyes", "mouth", "outfit"):
                textbutton g action NullAction() selected g in ("brows", "mouth")
        null height int(sprt.SPACER/2)

        # Add a divider
        add Transform("#fff2", ysize=max(1, config.screen_height//300), yalign=1.0)

        viewport:
            mousewheel True draggable True
            scrollbars "vertical"
            style_prefix 'sprt_disp'
            has vbox
            for grp in ("brows", "mouth"):
                label grp
                hbox:
                    for exp in ("angry_", "happy_", "sad_", "surprised_", None):
                        button:
                            action NullAction()
                            if ((exp == "happy_" and grp == "brows")
                                    or (exp == "sad_" and grp == "mouth")):
                                selected True
                            elif exp is None or (exp == "surprised_" and grp == "brows"):
                                foreground sprt.construct_frame(sprt.MAROON, "#0000", sprt.PADDING)
                                hover_foreground sprt.construct_frame(sprt.RED, "#0000", sprt.PADDING)
                                selected_foreground sprt.construct_frame(sprt.ORANGE, "#0000", sprt.PADDING)
                                background sprt.construct_frame("#5b0202", "#880303dd", sprt.PADDING)
                            has fixed:
                                fit_first True
                            add Placeholder():
                                crop (0.05, 0.1, 0.8, 0.4)
                                fit "contain" xsize int(config.screen_width/persistent.sprt_grid_div)-sprt.PADDING*2
                                align (0.5, 0.5)
                                if False:
                                    matrixcolor SaturationMatrix(0.5)
                            if exp is None:
                                text "(None)"
                            else:
                                text exp+grp

            null height sprt.SPACER

    hbox:
        style_prefix 'sprt_copy'
        textbutton "Copy All" action NullAction():
            if not sprt.tut3.between_ids("copy1", "copy3", step):
                foreground "#000d"
        textbutton "Copy Attrs" action NullAction():
            if not sprt.tut3.between_ids("copy1", "copy3", step):
                foreground "#000d"

    vbox:
        style_prefix 'sprt_final'
        add Placeholder():
            crop (0.05, 0.1, 0.8, 0.4)
            fit "contain" xsize int(config.screen_width/7.0)*2
            ysize int(config.screen_height//5*2)
            xalign 0.5
        hbox:
            textbutton "Update crop":
                style_prefix 'sprt_small' action NullAction()
                if not sprt.tut3.between_ids("crop1", "crop1", step):
                    foreground "#000d"
            textbutton "Randomize" action NullAction() style_prefix 'sprt_small':
                if not sprt.tut3.between_ids("random1", "random1", step):
                    foreground "#000d"
        fixed:
            xsize int(config.screen_width/7.0)*2
            ysize int(config.screen_height//5*2)
            add Placeholder():
                fit "contain" xsize int(config.screen_width/7.0)*2
                ysize int(config.screen_height//5*2)
                xalign 0.5
            text "eileen happy_brows sad_mouth" style 'sprt_disp_text'

    if sprt.tut3.tut(step).id == "tag2":
        frame:
            modal True style_prefix 'sprt_drop'
            xpos sprt.MENU_SIZE+sprt.SPACER*2
            ypos sprt.MENU_SIZE+sprt.SPACER*2
            has vbox
            for tg in ("ashwin", "side mc", "xia", "zoran"):
                hbox:
                    textbutton tg:
                        yalign 0.5 text_yalign 0.5
                        action NullAction()
                    textbutton "(Remove)" size_group None:
                        background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                        hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                        action NullAction()

    if sprt.tut3.tut(step).id in ("intro", "conclusion"):
        use hamburger_menu()

    if sprt.tut3.tut(step).id == "intro":
        add sprt.GRAY alpha 0.9

    ############################################################ Duplicate code

    use sprt_tutorial_text(sprt.tut3, step, "layered_image_visualizer")

################################################################################
## Code to remove these files for a distributed game. Do not remove.
init python:
    build.classify("**layered_image_visualizer.rpy", None)
    build.classify("**layered_image_visualizer.rpyc", None)
################################################################################