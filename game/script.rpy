# The script of the game goes in this file.


# Check file define-default untuk melihat definisi karakter/variabel
define e = Character("Eileen")
# The game starts here.
label start:

    if persistent.phase1:
        jump phase1
    elif persistent.phase2:
        jump phase2
    else:
        jump phase3



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene main_menu

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show liana normal

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
