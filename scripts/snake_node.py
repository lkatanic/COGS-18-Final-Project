# The SnakeNode is what makes up the Snake in the Snake.py file.
# It contains two attributes, an x and y value, stored as pos = [x, y]

class SnakeNode():
    def __init__(self, x, y):
        """Initializes SnakeNode to contain x, y values in pos
        """
        self.pos  = [x, y]
