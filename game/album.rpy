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
            action ShowMenu('elsyne_album')

    if persistent.miraunlocked:
        imagebutton:
            ypos 112
            xpos 1118
            auto "gui/gallery/gallery_%s_mira.png"
            action ShowMenu('mira_album')

    if persistent.felixunlocked:
        imagebutton:
            ypos 112
            xpos 390
            auto "gui/gallery/gallery_%s_felix.png"
            action ShowMenu('elsyne_album')

    if persistent.wyenunlocked:
        imagebutton:
            ypos 570
            xpos 1118
            auto "gui/gallery/gallery_%s_wyen.png"
            action ShowMenu('gallery')

screen felix_album:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Felix's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('felix_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('felix_album2')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15

screen felix_album2:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Felix's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('felix_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('felix_album')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15

screen mira_album:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Mira's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('mira_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('mira_album2')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15

screen mira_album2:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Mira's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('mira_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('mira_album')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15

screen elsyne_album:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Elsyne's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('elsyne_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('elsyne_album2')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15

screen elsyne_album2:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Elsyne's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('elsyne_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('elsyne_album')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15

screen wyen_album:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Wyen's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('wyen_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('wyen_album2')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15

screen wyen_album2:
    tag menu
    add "gui/gallery2_menu.png"

    text "{color=#59173e}{size=+20}{font=happy chicken.otf}Wyen's Gallery{/font}{/size}{/color}" xpos 845 ypos 100

    imagebutton:
        xpos 110
        ypos 72
        auto "gui/gallery/back_%s_button.png"
        action ShowMenu('gallery')

    imagebutton:
        xpos 980
        ypos 890
        auto "gui/gallery/before_%s_gallery.png"
        action ShowMenu('wyen_album')

    imagebutton:
        xpos 1150
        ypos 890
        auto "gui/gallery/next_%s_gallery.png"
        action ShowMenu('wyen_album')

    hbox:
        ## xpos before edited is 570
        xpos 600
        ypos 250
        spacing 100
        grid 2 2:
            add gallery.make_button(name="red",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="blue",unlocked="CGs/small/blue_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange",unlocked="CGs/small/green_small.jpg",locked="gui/gallery/blank_photo.png")
            add gallery.make_button(name="green_and_orange2",unlocked="CGs/small/red_small.jpg",locked="gui/gallery/blank_photo.png")
            spacing 15
