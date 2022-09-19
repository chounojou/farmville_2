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
