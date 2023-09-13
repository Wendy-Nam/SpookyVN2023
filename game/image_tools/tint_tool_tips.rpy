################################################################################
## Image Tint Tool Tips and Tricks
##
## This file is intended to be used alongside the Image Tint Tool in order to
## easily apply tints to images.
##
## If you use this code in your project,
## please credit me as Feniks @ feniksdev.com
## Also consider tossing me a ko-fi @ https://ko-fi.com/fen
################################################################################
##
## TIPS AND TRICKS
##
################################################################################
## CONFIGURATION
################################################################################
init python in myconfig:
    _constant = True
    ## FOR YOU: Set this to False if tint variants should be generated for
    ## all images, even if they're not layered images. This is True by default
    ## since it saves a bit of work if only layered images need tint variants.
    TINTS_TO_LAYEREDIMAGE_ONLY = True
    ## Otherwise, to save Ren'Py defining tint versions of every image ever,
    ## you can use the set below to specify image tags that should be included
    ## from tint variants.
    INCLUDED_TINT_TAGS = set([
        ## Example of how to fill this out:
        # "eileen", "ashwin", "alice", "zoran", "bg",
    ])
    ## If you don't use the above set and set TINTS_TO_LAYEREDIMAGE_ONLY to
    ## False, then tint variants will be generated for every image in your
    ## game, which should generally only be used in the case that you have too
    ## many image tags to list in the INCLUDED_TINT_TAGS set, and they all need
    ## tint variants.
    ##
    ## Note that there is a special transform included which means you can
    ## show images at a tint without having to define a tint variant for it;
    ## this should be the preferred method to apply a tint to an image without
    ## having to define a tint variant image for it.
    ## The transform looks like:
    # show journal at apply_matrix("night")

################################################################################

## Here is where you can declare tints you'll use in your game. The key in
## this dictionary is the attribute that you'll use to show the character with
## this tint. The value is a matrix that will be applied to the image.
define AVAILABLE_MATRICES = dict(
    sunset = TintMatrix("#ddc5b7")*SaturationMatrix(1.0000)*ContrastMatrix(1.0101),
    night = TintMatrix("#9588ce")*SaturationMatrix(0.8114)*ContrastMatrix(0.8838),
    ## Add more! the format is
    # tag = TintMatrix("#hexcolor")*SaturationMatrix(float)*ContrastMatrix(float),
    ## You can get the matrix from the tint tool by hitting "Copy Matrix"
    ## The matrix can be in a format not from the tinting tool as well e.g.
    # invert = InvertMatrix(),
)

################################################################################
## BACKEND
################################################################################
## You won't generally need to touch the code below this point, but do read
## about the apply_matrix transform just below, since you may use it.

## A helper transform to apply a matrix to an image that isn't a layered image.
## It will take both a string (the name of the matrix) or a matrix object.
## So, this means that in-script you can use this tool like so:
# show eileen at apply_matrix("sunset")
## This is helpful if you have images which don't need a separate tagged
## version with the matrix applied, but you'd still like to apply it as a
## one-off.
transform apply_matrix(mat):
    matrixcolor (mat if isinstance(mat, Matrix)
        else AVAILABLE_MATRICES.get(mat, IdentityMatrix()))

## Next is some code to automatically declare the matrices as image variants.
## By default, these will declare LayeredImageProxy variants of any layered
## images, so you can write `show eileen sunset` for example, assuming you had
## a layered image named `eileen`.
## You can also set it to declare tint variants for all images, even if they're
## not layered images. This is useful if you'd like to apply tints to
## backgrounds or items, for example.
init 999 python:
    # After all images have been defined, auto-define time-of-day variants
    # We don't want to re-look at images we newly defined, so we take a
    # snapshot of the image list to loop over.
    renp_list = list(renpy.list_images())
    for k in renp_list:
        for matname, mat in AVAILABLE_MATRICES.items():
            the_tag = k.split(' ')[0]
            if not (len(myconfig.INCLUDED_TINT_TAGS) == 0
                    or the_tag in myconfig.INCLUDED_TINT_TAGS):
                continue # Not a valid tag

            image_type = renpy.get_registered_image(k)
            if isinstance(image_type, LayeredImage):
                renpy.image(k + ' ' + matname,
                    LayeredImageProxy(k, Transform(matrixcolor=mat)))
            elif not myconfig.TINTS_TO_LAYEREDIMAGE_ONLY:
                try:
                    renpy.image(k + ' ' + matname, At(k, apply_matrix(mat)))
                except Exception as e:
                    print("Error applying matrix", matname, "to", k, ":", e)
                    continue


################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**tint_tool_tips.rpy", None)
    build.classify("**tint_tool_tips.rpyc", "archive")
################################################################################