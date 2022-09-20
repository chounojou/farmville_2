
screen gallery:

    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Gallery{/font}{/size}{/color}" xpos 980 ypos 125

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action Return()

    imagebutton:
        xpos 975
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('gallery2')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('gallery2')

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

screen gallery2:

    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Gallery{/font}{/size}{/color}" xpos 980 ypos 125

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action Return()

    imagebutton:
        xpos 975
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('gallery')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="cg10",unlocked="CGs/thumbnail/tend_1.png",locked="gui/gallery/blank_photo2.png")
            add gallery.make_button(name="cg11",unlocked="CGs/thumbnail/tend_2.png",locked="gui/gallery/blank_photo2.png")
            add gallery.make_button(name="cg12",unlocked="CGs/thumbnail/tend_3.png",locked="gui/gallery/blank_photo2.png")
            add gallery.make_button(name="cg13",unlocked="CGs/thumbnail/tend_4.png",locked="gui/gallery/blank_photo2.png")
            spacing 15
