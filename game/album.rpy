init python:
    gallery = Gallery()

    gallery.button("CG1")
    gallery.image("CGs/CG_1.png")
    gallery.condition("persistent.cg1_unlocked")

    gallery.button("CG2")
    gallery.image("CGs/CG_2.png")
    gallery.condition("persistent.cg2_unlocked")

    gallery.button("CG3")
    gallery.image("CGs/CG_3.png")
    gallery.condition("persistent.cg3_unlocked")

    gallery.button("CG4")
    gallery.image("CGs/CG_4.png")
    gallery.condition("persistent.cg4_unlocked")

    gallery.button("CG5")
    gallery.image("CGs/CG_5.png")
    gallery.condition("persistent.cg5_unlocked")

    gallery.button("CG6")
    gallery.image("CGs/CG_6.png")
    gallery.condition("persistent.cg6_unlocked")

    gallery.button("CG7")
    gallery.image("CGs/CG_7.png")
    gallery.condition("persistent.cg7_unlocked")

    gallery.button("CG8")
    gallery.image("CGs/CG_8.png")
    gallery.condition("persistent.cg8_unlocked")

    gallery.button("CG9")
    gallery.image("CGs/CG_9.png")
    gallery.condition("persistent.cg9_unlocked")

screen album:
    tag menu
    add "images/CustomUI/bg gallery.jpg"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        grid 3 3:
            add gallery.make_button(name="CG1",unlocked="CGs/CG_1.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG2",unlocked="CGs/CG_2.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG3",unlocked="CGs/CG_3.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG4",unlocked="CGs/CG_4.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG5",unlocked="CGs/CG_5.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG6",unlocked="CGs/CG_6.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG7",unlocked="CGs/CG_7.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG8",unlocked="CGs/CG_8.png",locked="CGs/small/locked.jpg")
            add gallery.make_button(name="CG9",unlocked="CGs/CG_9.png",locked="CGs/small/locked.jpg")
            spacing 15
        textbutton "Return" action Return()
