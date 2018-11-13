import sys
from cx_Freeze import setup, Executable


includefiles = [
                #images
                ('assets/background.png','assets/background.png'),
                ('assets/beer.png','assets/beer.png'),
                ('assets/beer2.png','assets/beer2.png'),
                ('assets/cat_black.png','assets/cat_black.png'),
                ('assets/cat_blue.png','assets/cat_blue.png'),
                ('assets/cat_green.png','assets/cat_green.png'),
                ('assets/cat_pink.png','assets/cat_pink.png'),
                ('assets/cat_red.png','assets/cat_red.png'),
                ('assets/clock.png','assets/clock.png'),
                ('assets/clock_slow.png','assets/clock_slow.png'),
                ('assets/clock_trans.png','assets/clock_trans.png'),
                ('assets/coffee_machine.png','assets/coffee_machine.png'),
                ('assets/cup.png','assets/cup.png'),
                ('assets/frame.png','assets/frame.png'),
                ('assets/frame_trans.png','assets/frame_trans.png'),
                ('assets/frootloops.png','assets/frootloops.png'),
                ('assets/game_over.png','assets/game_over.png'),
                ('assets/hand.png','assets/hand.png'),
                ('assets/live.png','assets/live.png'),
                ('assets/live_trans.png','assets/live_trans.png'),
                ('assets/penis.png','assets/penis.png'),
                ('assets/pizza.png','assets/pizza.png'),
                ('assets/rock_hand.png','assets/rock_hand.png'),
                ('assets/room_k.png','assets/room_k.png'),
                ('assets/room_lr.png','assets/room_lr.png'),
                ('assets/star.png','assets/star.png'),
                ('assets/star_bw.png','assets/star_bw.png'),
                ('assets/star_bw_trans.png','assets/star_bw_trans.png'),
                ('assets/star_trans.png','assets/star_trans.png'),
                ('assets/title.png','assets/title.png'),
                ('assets/title2.png','assets/title2.png'),  
                #sounds              
                ('sounds/BeepBox-Song.wav', 'sounds/BeepBox-Song.wav'),
                ('sounds/Catch.wav', 'sounds/Catch.wav'),
                ('sounds/Explosion.wav', 'sounds/Explosion.wav'),
                ('sounds/gameover.wav', 'sounds/gameover.wav'),
                ('sounds/miau.wav', 'sounds/miau.wav'),
                ('sounds/Powerup.wav', 'sounds/Powerup.wav'),
                ('sounds/test.wav', 'sounds/test.wav')
                ]

# Dependencies are automatically detected, but it might need fine tuning.
#"packages": ["os"], "excludes": ["tkinter"]
build_exe_options = {'include_files':includefiles}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Catch All Things",
        version = "0.1",
        description = "Beitrag zur GPPCC11",
        author="Wolfy7",
        options = {"build_exe": build_exe_options},
        executables = [Executable("gppcc11.py", base=base,icon="icon.ico")])