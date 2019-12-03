# This is the file that calls Snake.py and runs the game

from scripts import snake
import sys

# If argument is given, check if it is an int, then play
if len(sys.argv) > 1:
    try:
        game = snake.Snake(int(sys.argv[1]))
        game.play_game()
    except:
        print("Invalid Input! Choose a size as a number or leave blank for the default size (25)")

# if not argument is given, use default size (25)
else:
    game = snake.Snake(25)
    game.play_game()
