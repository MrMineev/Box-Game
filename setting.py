from square import Direction, Square

class Board:
    FIRST_PLAYER = 0
    SECOND_PLAYER = 0
    TURN = 0

    def __init__(self, n=4):
        self.N = n
        self.board = []
        for i in range(n):
            mas = []
            for j in range(n):
                mas.append(Square())
            self.board.append(mas)

        self.marked_board = []
        for i in range(n):
            mas = []
            for j in range(n):
                mas.append(2)
            self.marked_board.append(mas)

    def eval(self):
        if self.TURN % 2 == 0:
            return float(self.FIRST_PLAYER - self.SECOND_PLAYER)
        else:
            return float(self.SECOND_PLAYER - self.FIRST_PLAYER)

    def put(self, x, y, dir):
        if dir == Direction.UP:
            self.board[x][y].UP = True

            if x - 1 >= 0:
                self.board[x - 1][y].BOTTOM = True
        elif dir == Direction.BOTTOM:
            self.board[x][y].BOTTOM = True

            if x + 1 < self.N:
                self.board[x + 1][y].UP = True
        elif dir == Direction.LEFT:
            self.board[x][y].LEFT = True

            if y - 1 >= 0:
                self.board[x][y - 1].RIGHT = True
        elif dir == Direction.RIGHT:
            self.board[x][y].RIGHT = True

            if y + 1 < self.N:
                self.board[x][y + 1].LEFT = True

        res = self.play_one_more_move()

        if res == True and self.TURN % 2 == 0:
            self.FIRST_PLAYER += 1
        elif res == True and self.TURN % 2 == 1:
            self.SECOND_PLAYER += 1

        self.TURN += 1

        return res

    def play_one_more_move(self):
        a = False
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j].ALIVE == True and self.board[i][j].is_alive() == False:
                    self.marked_board[i][j] = self.TURN % 2
                    a = True
        return a




