init python:
    gallery = Gallery()

    gallery.button("cg1")
    gallery.image("CG1")
    gallery.condition("persistent.cg1_unlocked")

    gallery.button("cg2")
    gallery.image("CG2")
    gallery.condition("persistent.cg2_unlocked")

    gallery.button("cg3")
    gallery.image("CG3")
    gallery.condition("persistent.cg3_unlocked")

    gallery.button("cg4")
    gallery.image("CG4")
    gallery.condition("persistent.cg4_unlocked")

    gallery.button("cg5")
    gallery.image("CG5")
    gallery.condition("persistent.cg5_unlocked")

    gallery.button("cg6")
    gallery.image("CG6")
    gallery.condition("persistent.cg6_unlocked")

    gallery.button("cg7")
    gallery.image("CG7")
    gallery.condition("persistent.cg7_unlocked")

    gallery.button("cg8")
    gallery.image("CG8")
    gallery.condition("persistent.cg8_unlocked")

    gallery.button("cg9")
    gallery.image("CG9")
    gallery.condition("persistent.cg9_unlocked")

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
