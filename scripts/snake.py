# Snake but actually a "python" because it is in python and a python is a snake
import random
import curses
from scripts import snake_node

class Snake():
    def __init__(self, size, use_curses = True):
        """Initializes the various attributes of the Snake object, including size, its board,
        if it ate or is dead, the input, the Snake (comprised of SnakeNodes), and score
        """
        self.size    = size
        self.board   = [0] * (size**2)

        # init bools for snake
        self.did_eat = False
        self.dead    = False

        # starting input
        self.input   = 'd'

        self.snake   = []
        self.score   = 0

        # decide whether to print board
        self.use_curses = use_curses

    def generate_food(self):
        """Generates a single food onto the board, first firsts a free location, then places
        """
        done = False
        # check if location is taken
        # first generate random index, if board[index] is empty, gen food
        while not done:
            index = random.randint(0, self.size**2 - 1)
            if self.board[index] == 0:

                # check if snake is in any position of the board[index]
                for node in self.snake:
                    if self.calc_index(node.pos) is not index:
                        self.board[index] = 1
                        done = True

    def play_game(self):
        """Main method of this Snake. Initializes
        """

        # randomly set starting position, and generate food
        self.snake.append(snake_node.SnakeNode(random.randint(0, self.size - 1),
                                    random.randint(0, self.size - 1)))
        self.generate_food()

        # initialize screen using curses
        if self.use_curses:
            screen = curses.initscr()
            curses.start_color()
            screen.timeout(100)
            curses.noecho()

            # main while loop to continue until player is dead
            while not self.dead:
                # print the UI
                if self.use_curses:
                    screen.clear()
                    screen.addstr(0, 0, "Choose W, A, S, D to move, or Q to quit.",
                                  curses.A_BOLD)
                    screen.addstr(1, 0, self.print_board())
                    screen.refresh()
                else:
                    print(print_board())

                # if ate, make new food
                if self.did_eat:
                    self.generate_food()

                # handle user input, if unchanged, use last input
                inp = screen.getch()
                if inp != -1:
                    self.input = inp

                # if input is 'q', quit game
                if self.input == ord('q'):
                    break

                # check if input is good input
                elif self.input not in [ord('w'), ord('a'), ord('s'), ord('d'), -1]:
                    screen.addstr(0, self.size + 3, "Invalid Input")
                elif inp != -1:
                    self.input = inp

                self.update()

            # print "Game Over!" for 3 seconds
            screen.clear()
            screen.addstr(0, 0, "Game Over!", curses.A_BOLD)
            screen.refresh()
            curses.napms(3000)

            # end window
            curses.endwin()

    def calc_index(self, xy):
        """Calculates index on self.board using x and y coordinates
        """
        return (xy[1] * self.size) + xy[0]

    def update(self):
        """Updates Snake's position based on user input
        """
        # if snake is one node
        if len(self.snake) == 1:
            if self.did_eat:
                self.snake.append(snake_node.SnakeNode(self.snake[0].pos[0],
                                                       self.snake[0].pos[1]))
                self.did_eat = False

            # move head
            if   self.input == ord('w'):
                self.snake[0].pos[1] -= 1
            elif self.input == ord('a'):
                self.snake[0].pos[0] -= 1
            elif self.input == ord('s'):
                self.snake[0].pos[1] += 1
            else:
                self.snake[0].pos[0] += 1

            # check if dead
            if self.calc_index(self.snake[0].pos) > self.size**2 - 1:
                self.dead = True
                return

            # check if ate
            if self.board[self.calc_index(self.snake[0].pos)] == 1:
                self.score += 1
                self.did_eat = True

        # if snake is multiple nodes
        else:
            # move from tail to head
            i = len(self.snake) - 1
            while i != 0:
                self.snake[i].pos = self.snake[i - 1].pos

                # if tail and did eat
                if i == len(self.snake) - 1 and self.did_eat:
                    # add new SnakeNode to self.snake
                    self.snake.append(snake_node.SnakeNode(self.snake[i].pos[0],
                                                self.snake[i].pos[1]))
                    self.did_eat = False
                i -= 1

            # move head by creating new SnakeNode for head,
            # for each input, check if out of bounds
            newHead = snake_node.SnakeNode(self.snake[0].pos[0],
                                           self.snake[0].pos[1])
            if   self.input == ord('w'):
                newHead.pos[1] -= 1
                if newHead.pos[1] < 0:
                    newHead.pos[1] = self.size - 1

            elif self.input == ord('a'):
                newHead.pos[0] -= 1
                if newHead.pos[0] < 0:
                    newHead.pos[0] = self.size - 1

            elif self.input == ord('s'):
                newHead.pos[1] += 1
                if newHead.pos[1] > self.size - 1:
                    newHead.pos[1] = 0

            else:
                newHead.pos[0] += 1
                if newHead.pos[0] > self.size - 1:
                    newHead.pos[0] = 0

            self.snake[0] = newHead

            # check if dead
            for node in self.snake[1:]:
                if node.pos == newHead.pos:
                    self.dead = True
                    return
            if self.calc_index(newHead.pos) > self.size**2 - 1:
                self.dead = True
                return

            # check if ate
            if self.board[self.calc_index(self.snake[0].pos)] == 1:
                self.did_eat = True
                self.score += 1

    def print_board(self):
        """Prints the score and board to the user with a border.
        """
        # output to hold board contents in string
        output = ""

        # draw score
        output += "Score: " + str(self.score) + "\n"

        # draw snake onto self.board
        for node in self.snake:
            self.board[self.calc_index(node.pos)] = 2

        # draw top of board
        i = 0
        while i < self.size * 2 + 4:
            output += "="
            i += 1
        output += "\n"

        # draw board contents and sides
        i = 0
        j = 0
        while i < self.size:
            output += "||"
            j = 0
            while j < self.size:
                if   self.board[(i * self.size) + j] == 2:
                    output += "O"
                    self.board[(i * self.size) + j] = 0
                elif self.board[(i * self.size) + j] == 1:
                    output += "X"
                else:
                    output += " "
                output += " "
                j += 1
            output += "||\n"
            i += 1


        # draw bottom of board
        i = 0
        while i < self.size * 2 + 3:
            output += "="
            i += 1
        output += "=\n"
        return output
