# The script of the game goes in this file.

# Check file define-default untuk melihat definisi karakter/variabel

# The game starts here.
label start:

    if persistent.phase1:
        jump phase1
    elif persistent.phase2:
        jump phase2
    else:
        jump phase3
