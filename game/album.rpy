init python:
    gallery = Gallery()

    gallery.button("red")
    gallery.unlock_image("CG_red")

    gallery.button("blue")
    gallery.image("CG_blue")
    gallery.condition("persistent.blue_unlocked")

    gallery.button("green_and_orange")
    gallery.unlock_image("CG_green")
    gallery.unlock_image("CG_orange")

    gallery.button("green_and_orange2")
    gallery.condition("persistent.green_unlocked and persistent.orange_unlocked")
    gallery.image("CG_green")
    gallery.image("CG_orange")
    gallery.image("CG_pink")
    gallery.condition("persistent.pink_unlocked")

screen album:
    tag menu
    add "gui/gallery_menu_none.png"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="CGs/small/locked.jpg")
            spacing 15
        textbutton "Return" action Return()


screen gallery:
    tag menu
    add "gui/gallery_menu.png"

    imagebutton:
        xpos 120
        ypos 120
        auto "gui/gallery/gallery_%s.png"
        action ShowMenu('main_menu')

    if persistent.elsyneunlocked:
        imagebutton:
            ypos 570
            xpos 390
            auto "gui/gallery/gallery_%s_elsyne.png"
            action ShowMenu('main_menu')

    if persistent.miraunlocked:
        imagebutton:
            ypos 112
            xpos 1118
            auto "gui/gallery/gallery_%s_mira.png"
            action ShowMenu('gallery')

    if persistent.felixunlocked:
        imagebutton:
            ypos 112
            xpos 390
            auto "gui/gallery/gallery_%s_felix.png"
            action ShowMenu('album')

    if persistent.wyenunlocked:
        imagebutton:
            ypos 570
            xpos 1118
            auto "gui/gallery/gallery_%s_wyen.png"
            action ShowMenu('gallery')
