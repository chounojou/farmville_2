# The script of the game goes in this file.

# Check file define-default untuk melihat definisi karakter/variabel

# The game starts here.

init:
    $ style.default.font = "HinaMincho-Regular.ttf"
    $ style.default.language = "eastasian"

label start:

    jump wyen_ft_q1

#    if persistent.phase1:
#        jump phase1
#    elif persistent.phase2:
#        jump phase2
#    else:
#        jump phase3
