# File to test the contents of snake.py and snake_node.py

from scripts import snake, snake_node

def test_generate_food():
    """Tests Snake.py::generate_food() by calling it and checking if one has
    been generated.
    """
    test_game = snake.Snake(5, use_curses = False)
    number_of_food = 0
    test_game.snake.append(snake_node.SnakeNode(2, 2))
    test_game.generate_food()
    index = 0
    while index < 25:
        if test_game.board[index] == 1:
            number_of_food += 1
        index += 1

    assert number_of_food == 1

def test_generate_food():
    """Tests Snake.py::generate_food() by calling it and
    checking if one has been generated.
    """
    test_game = snake.Snake(5, use_curses = False)
    number_of_food = 0
    test_game.snake.append(snake_node.SnakeNode(2, 2))
    test_game.generate_food()
    index = 0
    while index < 25:
        if test_game.board[index] == 1:
            number_of_food += 1
        index += 1

    assert number_of_food == 1

def test_print_board():
    """Tests Snake.py::print_board() by creating a sample board and
    testing if the ouput is the same as the board.
    """
    test_game = snake.Snake(5, use_curses = False)
    test_game.snake.append(snake_node.SnakeNode(2, 2))
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "    ||\n||          ||\n||    O     ||\n||          ||\n||          " + \
    "||\n==============\n"

def test_update():
    """Tests Snake.py::update() by creating a Snake and moving it in
    multiple directions and checking if those are translated onto the board.
    """
    test_game = snake.Snake(5, use_curses = False)
    test_game.snake.append(snake_node.SnakeNode(2, 2))
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "   ||\n||          ||\n||    O     ||\n||          ||\n||          |" + \
    "|\n==============\n"

    test_game.input = ord("d")
    test_game.update()
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "    ||\n||          ||\n||      O   ||\n||          ||\n||          " + \
    "||\n==============\n"

    test_game.input = ord("w")
    test_game.update()
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "    ||\n||      O   ||\n||          ||\n||          ||\n||          " + \
    "||\n==============\n"

def test_print_board():
    """Tests Snake.py::print_board() by creating a sample board and testing
    if the ouput is the same as the board.
    """
    test_game = snake.Snake(5, use_curses = False)
    test_game.snake.append(snake_node.SnakeNode(2, 2))
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "    ||\n||          ||\n||    O     ||\n||          ||\n||          " + \
    "||\n==============\n"

def test_update():
    """Tests Snake.py::update() by creating a Snake and moving it in multiple
    directions and checking if those are translated onto the board.
    """
    test_game = snake.Snake(5, use_curses = False)
    test_game.snake.append(snake_node.SnakeNode(2, 2))
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "    ||\n||          ||\n||    O     ||\n||          ||\n||          " + \
    "||\n==============\n"
    test_game.input = ord("d")
    test_game.update()
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "    ||\n||          ||\n||      O   ||\n||          ||\n||          " + \
    "||\n==============\n"
    test_game.input = ord("w")
    test_game.update()
    assert test_game.print_board() == "Score: 0\n==============\n||      " + \
    "    ||\n||      O   ||\n||          ||\n||          ||\n||          " + \
    "||\n==============\n"
