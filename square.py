class Direction:
    UP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, val):
        self.l = val 

    def get(self):
        return self.l

class Square:
    ALIVE = True

    def __init__(self):
        self.BOTTOM = False
        self.UP = False
        self.LEFT = False
        self.RIGHT = False

    def bottom(self):
        self.BOTTOM = True

    def up(self):
        self.UP = True

    def left(self):
        self.LEFT = True

    def right(self):
        self.RIGHT = True

    def get(self, val):
        if val == Direction.BOTTOM:
            return self.BOTTOM
        if val == Direction.UP:
            return self.UP
        if val == Direction.LEFT:
            return self.LEFT
        if val == Direction.RIGHT:
            return self.RIGHT

    def is_alive(self):
        if (self.LEFT and self.RIGHT and self.BOTTOM and self.UP) == False:
            return True
        else:
            self.ALIVE = False
            return False



