from setting import Board

def print_blue(text):
    print("\033[94m" + text + "\033[0m", end='') # ]]

def print_red(text):
    print("\033[91m" + text + "\033[0m", end='') # ]]

def print_green(text):
    print("\033[92m" + text + "\033[0m", end='') # ]]

def show(b):
    print("   ", end='')
    for i in range(b.N):
        print_green(f"{i} ")
    print()

    print_blue("  +")
    for j in range(b.N):
        if (b.board[0][j].UP == False):
            print_blue("-+")
        else:
            print_red("-")
            print_blue("+")
    print()

    for i in range(b.N):
        print_green(f"{i} ")
        for j in range(b.N):
            if (b.board[i][j].LEFT == False):
                print_blue("| ")
            else:
                print_red("| ")
        if (b.board[i][-1].RIGHT == False):
            print_blue("| ")
        else:
            print_red("| ")

        print()

        print_blue("  +")
        for j in range(b.N):
            if (b.board[i][j].BOTTOM == False):
                print_blue("-+")
            else:
                print_red("-")
                print_blue("+")
        print()



