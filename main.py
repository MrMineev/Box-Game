from setting import Board
from show import show
from player import Player

b = Board(n=4)
DEPTH = 2

def human_move():
    x, y = map(int, input(">>> ").split())
    print("\n== DIRECTION ==")

    print("\t0 - UP")
    print("\t1 - BOTTOM")
    print("\t2 - LEFT")
    print("\t3 - RIGHT")

    print("== DIRECTION ==")

    dir = int(input(">>> "))

    res = b.put(x, y, dir)
    show(b)
    print(f"PLAY ONE MORE MOVE = {b.play_one_more_move()}")

    if res == True:
        human_move()

def computer_move():
    x, y, dir = player.calc(b, depth=DEPTH)
    res = b.put(x, y, dir)
    print(f"{{ X = {x}, Y = {y}, DIR = {dir} }}")
    show(b)

    if res == True:
        computer_move()


show(b)

player = Player()

while True:
    human_move()
    computer_move()

