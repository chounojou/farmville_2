################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/left.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/right.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png")

style slider:
    ysize gui.slider_size
    left_bar "gui/slider/left_bar.png"
    right_bar "gui/slider/right_bar.png"
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset 31

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

transform sideways:
    rotate -5

screen say(who, what):

    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" at sideways

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xpos 200 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 615
    xanchor gui.name_xalign
    xsize 496
    ypos -285
    ysize 230

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.0
    yalign 0.5
    xpos 75
    ypos 110

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 650
    xsize gui.dialogue_width
    ypos -75


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    style_prefix "input"

    window:


        vbox:

            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button_text:
    font 'BaksoSapi.otf'
    xalign 0.5
    yalign 0.5
    size 26
    color '#ffffff'
    hover_color '#ffce3b'

style choice_vbox:
    xalign 0.5
    ypos 450
    xpos 950
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    imagebutton:
        xpos 1798
        ypos 50
        auto "gui/button/qm_%s.png"
        action ShowMenu('pause_menu')

    if quick_menu and not renpy.get_screen('choice'):

        hbox:
            style_prefix "quick"

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
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

## pause menu ##
screen pause_menu():

    # This ensures that any other menu screen is replaced.
    tag menu



    # The background of the game menu.
    window:
        style "pm_root"

    imagemap:
        ground "gui/pause_menu_2.png"
        idle "gui/button/pause_menu.png"
        hover "gui/button/pause_menu_hover.png"
        selected_idle "gui/button/pause_menu.png"
        selected_hover "gui/button/pause_menu_hover.png"

        hotspot (611, 194, 340, 127) action ShowMenu("save")
        hotspot (997, 202, 332, 115) action ShowMenu('load')
        hotspot (1380, 202, 334, 114) action ShowMenu("preferences")
        hotspot (251, 616, 334, 115) action MainMenu()
        hotspot (698, 616, 338, 113) action Quit(confirm=not main_menu)
        hotspot (103, 137, 279, 78) action Return()


style pause_menu_frame is empty
style pause_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"
###
screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("New Game") action Start() xpos -20 ypos -5
            ypos 720
            xpos 1550

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load Game") action ShowMenu("load") xpos -30 ypos 2
        textbutton _("Gallery") action ShowMenu("gallery")  ypos 5

        textbutton _("Settings") action ShowMenu("preferences2") xpos -10 ypos 10

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu) xpos 35 ypos 5


style navigation_button is gui_button
style navigation_button_text:
    size 40
    color '#fbb03b'
    selected_color '#ffffff'
    hover_color '#ffffff'
    outlines [(0, '#381301', 5, 5)]

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():


    tag menu
    add "gui/history.png"
    imagebutton:
        xpos 30
        ypos 80
        auto "gui/gallery/back_%s_button.png"
        action Return()
    text "{size=+20}Credit{/size}" xpos 850 ypos 120

    vbox:
        xalign 0.3
        ypos 250
        viewport id "vpgrid":
            yinitial 0
            draggable True
            mousewheel True
            xmaximum 1400
            ymaximum 700
            yfill True
            scrollbars "vertical"
            xsize 1000 ysize 750
            xpos 100 ypos -50

            vbox:

                text _("{size=+5}Project Assist: Terrabyd{/size}") xalign 0.5

                grid 3 1:
                    xalign 0.5
                    text _("{color=#ffce3b}{font=Happy Chicken.otf}Story:{/font}{/color}\n-Maru (Lead)\n-Filia (V.Lead)\n-IzunaLord\n-Grenin\n-Renko\n-Galabun\n-Radice\n-Zenyastra")
                    text _("{color=#ffce3b}{font=Happy Chicken.otf}Visual:{/font}{/color}\n-Wawa (Lead)\n-ComicSans (V.Lead)\n-Cantalea\n-Vira k.\n-Farichi\n-Rarugo\n-Dino Brando\n-Salaaad")
                    text _("\n-Xerael\n-Aifira\n-Hotaru Setsuna\n-Rei Holysoto\n-Hebi Hanster\n-Anna Freyya\n-Hannu")
                spacing 30
                grid 3 1:
                    xalign 0.5
                    text _("{color=#ffce3b}{font=Happy Chicken.otf}  IT:{/font}{/color}\n-Chounojou (Lead)\n-Kuro Stark\n-Lucifenn\n-Yukio Defender")
                    text _("{color=#ffce3b}{font=Happy Chicken.otf}  Audio:{/font}{/}\n-Alto Ether (Lead)\n-No15e (V.Lead)\n-Riordan Hayton")
                    text _("{color=#ffce3b}{font=Happy Chicken.otf}RiddleMaker:{/font}{/color}\n-Keppachi (Lead)\n-Rayden Rin (V.Lead)\n-mifmif")
                grid 2 1:
                    xalign 0.5
                    text _("{color=#ffce3b}{font=Happy Chicken.otf}        BGM & SFX:{/font}{/color}\n{a=https://dova-s.jp\nhttps://freesound.org}dova-s.jp{/a}\n{a=https://opengameart.ord}opengameart.ord{/a}\n{a=https://sound-effect.bbcrewind.co.uk}sound-effect.bbcrewind.co.uk{/a}")
                    text _("{color=#ffce3b}{font=Happy Chicken.otf}        Background:{/font}{/color}\n{a=https://www.freepik.com/free-photo/group-pigs-domestic-animals-pig-farm_11036358.htm#query=inside%20barn&position=27&from_view=search}Freepik: Barn{/a}\n{a=https://www.freepik.com/free-photo/beautiful-shot-forest-with-tall-green-trees_10978866.htm#query=forest&position=15&from_view=keyword}Freepik: Forest{/a}\n{a=https://unsplash.com/photos/zCQ06B18v0Q}Unsplash: Farm{/a}\n{a=https://unsplash.com/photos/Q2TO1NfHS8E}unsplash :Corn Field{/a}\n{a=https://stock.adobe.com/id/images/cotswolds/304711814}Adobe Stock : Village{/a}\n{a=https://www.pexels.com/photo/people-walking-on-street-6159067/}Pexels : Market{/a}\n{a=https://unsplash.com/photos/8janMgWWR8A}Unsplash : River{/a}\n{a=https://unsplash.com/photos/PaKHbtTDqt0}Unsplash: Jail{/a}\n{a=https://pixabay.com/photos/blacksmith-workshop-equipment-500776/}Pixabay: Shed{/a}\n{a=https://pxhere.com/en/photo/1637467}Pxhere: Cave Branch{/a}\n{a=https://www.flickr.com/photos/coconinonationalforest/20578435368}Flickr :Cave Tunnel{/a}\n{a=https://unsplash.com/photos/sXxwbzfNdR4}Unsplash: Cave Final{/a}") xpos 150
                    
                label "\n[config.name!t]" xalign 0.5
                text _("Version [config.version!t]\n") xalign 0.5

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n" xalign 0.5

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") xalign 0.5


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot"), FileSaveName(number))
    add FileScreenshot(number) xpos -1 ypos 0


screen load:

    tag menu
    #current page
    default curpage = 1

    imagemap:
        ground 'gui/saveload/ground_save.png'
        idle 'gui/saveload/ground_save.png'
        hover 'gui/saveload/ground_save.png'
        selected_idle 'gui/saveload/ground_save.png'
        selected_hover 'gui/saveload/ground_save.png'
        cache False
        
        #lucii
        # hotspot (57, 980, 78, 72) action FilePagePrevious(max=5, wrap=True, auto=False, quick=False)
        # hotspot (195, 981, 67, 66) action FilePageNext(max=5, wrap=True, auto=False, quick=False)
        
        #sans
        if curpage == 1 :
            hotspot (57, 980, 78, 72) action [FilePagePrevious(max=5, wrap=True, auto=False, quick=False), SetScreenVariable("curpage", 5)]
            hotspot (195, 981, 67, 66) action [FilePageNext(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage+1)]
        if curpage >1 and curpage <5 :
            hotspot (57, 980, 78, 72) action [FilePagePrevious(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage-1)]
            hotspot (195, 981, 67, 66) action [FilePageNext(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage+1)]
        if curpage == 5 :
            hotspot (57, 980, 78, 72) action [FilePagePrevious(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage-1)]
            hotspot (195, 981, 67, 66) action [FilePageNext(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", 1)]

        ## You might get confused but these one below are the save/load slots, those boxes.
        
        #lucii
        # hotspot (229, 387, 286, 150) action FileAction(1):
        #     use load_save_slot(number=1)
        # hotspot (219, 721, 285, 150) action FileAction(2):
        #     use load_save_slot(number=2)
        # hotspot (1140, 370, 285, 150) action FileAction(3):
        #     use load_save_slot(number=3)
        # hotspot (1139, 720, 286, 150) action FileAction(4):
        #     use load_save_slot(number=4)

        #sans
        if curpage ==1 :
            hotspot (229, 387, 286, 150) action FileAction(1):
                use load_save_slot(number=1)
            hotspot (219, 721, 285, 150) action FileAction(2):
                use load_save_slot(number=2)
            hotspot (1140, 370, 285, 150) action FileAction(3):
                use load_save_slot(number=3)
            hotspot (1139, 720, 286, 150) action FileAction(4):
                use load_save_slot(number=4)
        if curpage ==2 :
            hotspot (229, 387, 286, 150) action FileAction(5):
                use load_save_slot(number=5)
            hotspot (219, 721, 285, 150) action FileAction(6):
                use load_save_slot(number=6)
            hotspot (1140, 370, 285, 150) action FileAction(7):
                use load_save_slot(number=7)
            hotspot (1139, 720, 286, 150) action FileAction(8):
                use load_save_slot(number=8)
        if curpage ==3 :
            hotspot (229, 387, 286, 150) action FileAction(9):
                use load_save_slot(number=9)
            hotspot (219, 721, 285, 150) action FileAction(10):
                use load_save_slot(number=10)
            hotspot (1140, 370, 285, 150) action FileAction(11):
                use load_save_slot(number=11)
            hotspot (1139, 720, 286, 150) action FileAction(12):
                use load_save_slot(number=12)
        if curpage == 4 :
            hotspot (229, 387, 286, 150) action FileAction(13):
                use load_save_slot(number=13)
            hotspot (219, 721, 285, 150) action FileAction(14):
                use load_save_slot(number=14)
            hotspot (1140, 370, 285, 150) action FileAction(15):
                use load_save_slot(number=15)
            hotspot (1139, 720, 286, 150) action FileAction(16):
                use load_save_slot(number=16)
        if curpage==5 :
            hotspot (229, 387, 286, 150) action FileAction(17):
                use load_save_slot(number=17)
            hotspot (219, 721, 285, 150) action FileAction(18):
                use load_save_slot(number=18)
            hotspot (1140, 370, 285, 150) action FileAction(19):
                use load_save_slot(number=19)
            hotspot (1139, 720, 286, 150) action FileAction(20):
                use load_save_slot(number=20)


        hotspot (357, 980, 68, 64) action ShowMenu('load')
        hotspot (633, 980, 69, 63) action ShowMenu('save')
        hotspot (55, 87, 66, 68) action Return()


    add "gui/saveload/high_save.png"
    zorder 200

    textbutton _("{color=#ffce3b}Back{/color}") action Return() xpos 130 ypos 75
    text "{color=#ffce3b}{size=+40}{font=happy chicken.otf}Load{/font}{/size}{/color}" xpos 820 ypos 89
    textbutton "{color=#ffce3b}{font=happy chicken.otf}{size=-3}Load{/size}{/font}{/color}" action ShowMenu('load') xpos 450 ypos 970
    textbutton "{color=#ffce3b}{font=happy chicken.otf}{size=-3}Save{/size}{/font}{/color}" action ShowMenu('save') xpos 720 ypos 970

    #lucii
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}001{/size}{/font}{/color}" xpos 170 ypos 305
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}002{/size}{/font}{/color}" xpos 170 ypos 632
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}003{/size}{/font}{/color}" xpos 1075 ypos 300
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}004{/size}{/font}{/color}" xpos 1075 ypos 628
    
    #sans
    if curpage == 1 :
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}001{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}002{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}003{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}004{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 2:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}005{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}006{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}007{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}008{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 3:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}009{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}010{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}011{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}012{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 4:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}013{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}014{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}015{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}016{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 5:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}017{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}018{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}019{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}020{/size}{/font}{/color}" xpos 1075 ypos 628



screen save:

    tag menu
    default curpage = 1

    imagemap:
        ground 'gui/saveload/ground_save.png'
        idle 'gui/saveload/ground_save.png'
        hover 'gui/saveload/ground_save.png'
        selected_idle 'gui/saveload/ground_save.png'
        selected_hover 'gui/saveload/ground_save.png'
        cache False

        # hotspot (57, 980, 78, 72) action FilePagePrevious(max=5, wrap=True, auto=False, quick=False)
        # hotspot (195, 981, 67, 66) action FilePageNext(max=5, wrap=True, auto=False, quick=False)

        if curpage == 1 :
            hotspot (57, 980, 78, 72) action [FilePagePrevious(max=5, wrap=True, auto=False, quick=False), SetScreenVariable("curpage", 5)]
            hotspot (195, 981, 67, 66) action [FilePageNext(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage+1)]
        if curpage >1 and curpage <5 :
            hotspot (57, 980, 78, 72) action [FilePagePrevious(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage-1)]
            hotspot (195, 981, 67, 66) action [FilePageNext(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage+1)]
        if curpage == 5 :
            hotspot (57, 980, 78, 72) action [FilePagePrevious(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", curpage-1)]
            hotspot (195, 981, 67, 66) action [FilePageNext(max=5, wrap=True, auto=False, quick=False),SetScreenVariable("curpage", 1)]

        ## You might get confused but these one below are the save/load slots, those boxes.

        #lucii
        # hotspot (229, 387, 286, 150) action FileAction(1):
        #     use load_save_slot(number=1)
        # hotspot (219, 721, 285, 150) action FileAction(2):
        #     use load_save_slot(number=2)
        # hotspot (1140, 370, 285, 150) action FileAction(3):
        #     use load_save_slot(number=3)
        # hotspot (1139, 720, 286, 150) action FileAction(4):
        #     use load_save_slot(number=4)

        #sans
        if curpage ==1 :
            hotspot (229, 387, 286, 150) action FileAction(1):
                use load_save_slot(number=1)
            hotspot (219, 721, 285, 150) action FileAction(2):
                use load_save_slot(number=2)
            hotspot (1140, 370, 285, 150) action FileAction(3):
                use load_save_slot(number=3)
            hotspot (1139, 720, 286, 150) action FileAction(4):
                use load_save_slot(number=4)
        if curpage ==2 :
            hotspot (229, 387, 286, 150) action FileAction(5):
                use load_save_slot(number=5)
            hotspot (219, 721, 285, 150) action FileAction(6):
                use load_save_slot(number=6)
            hotspot (1140, 370, 285, 150) action FileAction(7):
                use load_save_slot(number=7)
            hotspot (1139, 720, 286, 150) action FileAction(8):
                use load_save_slot(number=8)
        if curpage ==3 :
            hotspot (229, 387, 286, 150) action FileAction(9):
                use load_save_slot(number=9)
            hotspot (219, 721, 285, 150) action FileAction(10):
                use load_save_slot(number=10)
            hotspot (1140, 370, 285, 150) action FileAction(11):
                use load_save_slot(number=11)
            hotspot (1139, 720, 286, 150) action FileAction(12):
                use load_save_slot(number=12)
        if curpage == 4 :
            hotspot (229, 387, 286, 150) action FileAction(13):
                use load_save_slot(number=13)
            hotspot (219, 721, 285, 150) action FileAction(14):
                use load_save_slot(number=14)
            hotspot (1140, 370, 285, 150) action FileAction(15):
                use load_save_slot(number=15)
            hotspot (1139, 720, 286, 150) action FileAction(16):
                use load_save_slot(number=16)
        if curpage==5 :
            hotspot (229, 387, 286, 150) action FileAction(17):
                use load_save_slot(number=17)
            hotspot (219, 721, 285, 150) action FileAction(18):
                use load_save_slot(number=18)
            hotspot (1140, 370, 285, 150) action FileAction(19):
                use load_save_slot(number=19)
            hotspot (1139, 720, 286, 150) action FileAction(20):
                use load_save_slot(number=20)

        hotspot (357, 980, 68, 64) action ShowMenu('load')
        hotspot (633, 980, 69, 63) action ShowMenu('save')
        hotspot (55, 87, 66, 68) action Return()


    add "gui/saveload/high_save.png"
    zorder 200

    textbutton _("{color=#ffce3b}Back{/color}") action Return() xpos 130 ypos 75
    text "{color=#ffce3b}{size=+40}{font=happy chicken.otf}Save{/font}{/size}{/color}" xpos 820 ypos 89
    textbutton "{color=#ffce3b}{font=happy chicken.otf}{size=-3}Load{/size}{/font}{/color}" action ShowMenu('load') xpos 450 ypos 970
    textbutton "{color=#ffce3b}{font=happy chicken.otf}{size=-3}Save{/size}{/font}{/color}" action ShowMenu('save') xpos 720 ypos 970

    #lucii
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}001{/size}{/font}{/color}" xpos 170 ypos 305
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}002{/size}{/font}{/color}" xpos 170 ypos 632
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}003{/size}{/font}{/color}" xpos 1075 ypos 300
    # text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}004{/size}{/font}{/color}" xpos 1075 ypos 628

    #number slot increased when pagination
    #sans
    if curpage == 1 :
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}001{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}002{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}003{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}004{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 2:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}005{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}006{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}007{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}008{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 3:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}009{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}010{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}011{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}012{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 4:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}013{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}014{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}015{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}016{/size}{/font}{/color}" xpos 1075 ypos 628
    elif curpage == 5:
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}017{/size}{/font}{/color}" xpos 170 ypos 305
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}018{/size}{/font}{/color}" xpos 170 ypos 632
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}019{/size}{/font}{/color}" xpos 1075 ypos 300
        text "{color=#ffce3b}{font=happy chicken.otf}{size=+20}020{/size}{/font}{/color}" xpos 1075 ypos 628

init python:
    config.thumbnail_width = 290
    config.thumbnail_height = 150

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3


style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    imagemap:
        ground "gui/game_menu.png"
        idle "gui/button/set.png"
        hover "gui/button/set_hover.png"
        selected_idle "gui/button/set.png"
        selected_hover "gui/button/set_hover.png"

        hotspot (376, 818, 79, 90) action Return()
        hotspot (617, 818, 231, 83) action ShowMenu("about")
        hotspot (483, 804, 102, 112) action MainMenu()

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display") xpos 435 ypos 153
                        textbutton _("          Window") action Preference("display", "window") xpos 385 ypos 188
                        textbutton _("          Fullscreen") action Preference("display", "fullscreen") xpos 385 ypos 205

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side") xpos 503 ypos 153
                    textbutton _("           Disable") action Preference("rollback side", "disable") xpos 447 ypos 188
                    textbutton _("           Left") action Preference("rollback side", "left") xpos 447 ypos 205
                    textbutton _("           Right") action Preference("rollback side", "right") xpos 447 ypos 224

                vbox:
                    style_prefix "check"
                    label _("Skip") xpos 684 ypos 153
                    textbutton _("           Unseen Text") action Preference("skip", "toggle") xpos 615 ypos 188
                    textbutton _("           After Choices") action Preference("after choices", "toggle") xpos 615 ypos 205
                    textbutton _("           Transitions") action InvertSelected(Preference("transitions", "toggle")) xpos 615 ypos 224

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:


                    label _("Text Speed") ypos -7 xpos 1

                    bar value Preference("text speed") ypos 1

                    label _("Auto-Forward Time") ypos 3 xpos 1

                    bar value Preference("auto-forward time") ypos 8

                    xpos 382
                    ypos 205



                vbox:

                    if config.has_music:
                        label _("Music Volume") ypos -8 xpos 25

                        hbox:
                            bar value Preference("music volume")
                        xpos 563
                        ypos 205

                    if config.has_sound:

                        label _("Sound Volume") ypos 1 xpos 25

                        hbox:
                            bar value Preference("sound volume") ypos 5

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume") ypos 8 xpos 25

                        hbox:
                            bar value Preference("voice volume") ypos 10

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

            textbutton _("           Mute All"):
                action Preference("all mute", "toggle")
                style "mute_all_button"
                ypos 235
                xpos 1070



style pref_label is gui_label
style pref_label_text:
    size 23
    outlines [(0, '#59173e', 1, 1)]
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text:
    size 23
    color '#ffce3b'
    outlines [(0, '#59173e', 1, 1)]
style radio_button is gui_button
style radio_button_text:
    size 23
    color '#ffffff'
    selected_color '#ffce3b'
    hover_color '#ffce3b'
    outlines [(0, '#59173e', 1, 1)]
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text:
    size 23
    color '#ffce3b'
    outlines [(0, '#59173e', 1, 1)]
style check_button is gui_button
style check_button_text:
    size 23
    color '#ffffff'
    selected_color '#ffce3b'
    hover_color '#ffce3b'
    outlines [(0, '#59173e', 1, 1)]
style check_vbox is pref_vbox

style pref_slider is gui_slider
style slider_label is pref_label
style slider_label_text:
    size 23
    outlines [(0, '#59173e', 1, 1)]
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text:
    size 23
    outlines [(0, '#59173e', 1, 1)]
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text:
    size 23
    color '#ffffff'
    selected_color '#ffce3b'
    hover_color '#ffce3b'
    outlines [(0, '#59173e', 1, 1)]

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 2.0

style pref_vbox:
    xsize 300

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 475
    ysize 62

style slider_text:
    xalign 1.0

style slider_button:
    properties gui.button_properties("slider_button")
    xalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 350

####pref2

screen preferences2():

    tag menu

    imagemap:
        ground "gui/game_menu.png"
        idle "gui/button/set.png"
        hover "gui/button/set_hover.png"
        selected_idle "gui/button/set.png"
        selected_hover "gui/button/set_hover.png"

        hotspot (376, 818, 79, 90) action Return()
        hotspot (617, 818, 231, 83) action ShowMenu("about")
        hotspot (483, 804, 102, 112) action ShowMenu("main_menu")

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display") xpos 435 ypos 153
                        textbutton _("          Window") action Preference("display", "window") xpos 385 ypos 188
                        textbutton _("          Fullscreen") action Preference("display", "fullscreen") xpos 385 ypos 205

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side") xpos 503 ypos 153
                    textbutton _("           Disable") action Preference("rollback side", "disable") xpos 447 ypos 188
                    textbutton _("           Left") action Preference("rollback side", "left") xpos 447 ypos 205
                    textbutton _("           Right") action Preference("rollback side", "right") xpos 447 ypos 224

                vbox:
                    style_prefix "check"
                    label _("Skip") xpos 684 ypos 153
                    textbutton _("           Unseen Text") action Preference("skip", "toggle") xpos 615 ypos 188
                    textbutton _("           After Choices") action Preference("after choices", "toggle") xpos 615 ypos 205
                    textbutton _("           Transitions") action InvertSelected(Preference("transitions", "toggle")) xpos 615 ypos 224

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:


                    label _("Text Speed") ypos -7 xpos 1

                    bar value Preference("text speed") ypos 1

                    label _("Auto-Forward Time") ypos 3 xpos 1

                    bar value Preference("auto-forward time") ypos 8

                    xpos 382
                    ypos 205



                vbox:

                    if config.has_music:
                        label _("Music Volume") ypos -8 xpos 25

                        hbox:
                            bar value Preference("music volume")
                        xpos 563
                        ypos 205

                    if config.has_sound:

                        label _("Sound Volume") ypos 1 xpos 25

                        hbox:
                            bar value Preference("sound volume") ypos 5

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume") ypos 8 xpos 25

                        hbox:
                            bar value Preference("voice volume") ypos 10

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

            textbutton _("           Mute All"):
                action Preference("all mute", "toggle")
                style "mute_all_button"
                ypos 235
                xpos 1070


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    add "gui/history.png"
    text "{size=+20}History{/size}" xpos 850 ypos 120
    imagebutton:
        xpos 30
        ypos 80
        auto "gui/gallery/back_%s_button.png"
        action Return()

    ## Avoid predicting this screen, as it can be very large.
    predict False
    style_prefix "history"
    vbox:
        xalign 0.3
        ypos 250
        viewport id "vpgrid":
            yinitial 1.0
            draggable True
            mousewheel True
            xmaximum 1400
            ymaximum 700
            yfill True
            scrollbars "vertical"
            xsize 1000 ysize 750
            xpos 100 ypos -50
            vbox:

                for h in _history_list:
                    if h.who:
                        text h.who xalign 0.0 text_align 0.0:
                            size 50
                            color u"#ffce3b"

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        color "#ffffff"
                        substitute False
                    text " "
                if not _history_list:
                    text _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()
style history_label_text:
    xpos 350
    ypos 50
    size 90


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                imagebutton:
                    auto "gui/button/no_%s_button.png"
                    action no_action
                imagebutton:
                    auto "gui/button/yes_%s_button.png"
                    action yes_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")






## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

#### there are none
