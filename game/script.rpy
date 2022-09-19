# The script of the game goes in this file.


# Check file define-default untuk melihat definisi karakter/variabel

# The game starts here.

label start:

    #set volume audio channels
    #$ renpy.music.set_volume(0.3, delay=0, channel='ambience')
    #$ renpy.music.set_volume(0.05, delay=0, channel='music')
    #$ renpy.music.set_volume(0.3, delay=0, channel='sound')

    #if persistent.phase1:
    jump phase1
    #elif persistent.phase2:
    #    jump phase2
    #else:
    #    jump phase3

    return
