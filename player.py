from setting import Board
from square import Square, Direction
import copy

INF = int(1e9)

class Player:
    def __init__(self, depth=3):
        self.depth = depth

    def calc(self, board, depth=3):
        mini = INF
        x = -1
        y = -1
        dir = -1

        for i in range(board.N):
            for j in range(board.N):
                directions = []
                if i == 0 and j == 0:
                    directions = [Direction.UP, Direction.BOTTOM, Direction.LEFT, Direction.RIGHT]
                elif j == 0:
                    directions = [Direction.BOTTOM, Direction.RIGHT, Direction.LEFT]
                elif i == 0:
                    directions = [Direction.UP, Direction.BOTTOM, Direction.RIGHT]
                else:
                    directions = [Direction.BOTTOM, Direction.RIGHT]

                for direction in directions:
                    if board.board[i][j].get(direction) == True:
                        continue

                    b = copy.deepcopy(board)
                    b.put(i, j, direction)
                    e = self.eval(b, depth=depth - 1)
                    if mini > e:
                        mini = e
                        x = i
                        y = j
                        dir = direction 

        return x, y, dir

    def eval(self, board, depth=3) -> float:
        if depth == 0:
            return board.eval()
        mini = INF
        for i in range(board.N):
            for j in range(board.N):
                directions = [Direction.UP, Direction.BOTTOM, Direction.LEFT, Direction.RIGHT]
                for direction in directions:
                    b = copy.deepcopy(board)
                    b.put(i, j, direction)
                    e = self.eval(b, depth=depth - 1)
                    if mini > e:
                        mini = e
        return -mini



