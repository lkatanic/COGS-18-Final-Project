# This is the file that calls Snake.py and runs the game

from scripts import snake

# This can be adjusted to choose the size of the game
GAME_SIZE = 25

# create new Snake object, then play game
game = snake.Snake(GAME_SIZE)
game.play_game()
