screen gallery:

    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Gallery{/font}{/size}{/color}" xpos 980 ypos 125

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action Return()


    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 3 3:
            add gallery.make_button(name="cg1",unlocked="CGs/thumbnail/cg1_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg2",unlocked="CGs/thumbnail/cg2_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg3",unlocked="CGs/thumbnail/cg3_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg4",unlocked="CGs/thumbnail/cg4_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg5",unlocked="CGs/thumbnail/cg5_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg6",unlocked="CGs/thumbnail/cg6_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg7",unlocked="CGs/thumbnail/cg7_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg8",unlocked="CGs/thumbnail/cg8_tn.png",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="cg9",unlocked="CGs/thumbnail/cg9_tn.png",locked="gui/gallery/blank_photo.png")
            spacing 15

screen gallery_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if gallery_menu:

        hbox:
            style_prefix "gallerym"

            xalign 0.5
            yalign 1.0

            imagemap:
                ground "gui/button/ingame_idle.png"
                idle "gui/button/ingame_idle.png"
                hover "gui/button/ingame_hover.png"
                selected_idle "gui/button/ingame_idle.png"
                selected_hover "gui/button/ingame_hover.png"

                hotspot (1115, 961, 89, 91) action Preference("auto-forward", "toggle")
                hotspot (1217, 966, 85, 86) action HideInterface()
                hotspot (1315, 964, 92, 85) action Skip() alternate Skip(fast=True, confirm=True)
                hotspot (1418, 966, 88, 84) action ShowMenu('save')
                hotspot (1519, 966, 89, 86) action ShowMenu('history')
                hotspot (1793, 43, 84, 85) action ShowMenu('pause_menu')




## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("gallery_menu")

default gallery_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("gallery_button")

style quick_button_text:
    properties gui.button_text_properties("gallery_button")
