# Import randint function from random module
from random import randint

Hidden_Pattern = [[' ']*8 for x in range(8)]
Guess_Pattern = [[' ']*8 for x in range(8)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

# Function is defined to print the board of battleship


def print_board(board):
    print("  A B C D E F G H ")
    print('  **************** ')
    row_num = 1
    for row in board:
        print("%d | %s |" % (row_num, " | ".join(row)))
        row_num += 1


