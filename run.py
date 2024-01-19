from random import randint

# Initialize game boards for both player and computer
Player_Hidden_Pattern = [[' '] * 8 for _ in range(8)]
Player_Guess_Pattern = [[' '] * 8 for _ in range(8)]
Computer_Hidden_Pattern = [[' '] * 8 for _ in range(8)]
Computer_Guess_Pattern = [[' '] * 8 for _ in range(8)]


# Mappings for columns
let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


# Function to print two game boards side by side
def print_boards(board1, board2, board1_title="Your Guesses", board2_title="Computer's Guesses"):
    print(f'{board1_title:20s}    {board2_title}')
    print('   A B C D E F G H      A B C D E F G H')
    print('   ****************     ****************')
    for row_num in range(8):
        row1 = " ".join(board1[row_num])
        row2 = " ".join(board2[row_num])
        print(f"{row_num + 1}|{row1}|    {row_num + 1}|{row2}|")


def get_ship_location():
    # Enter the row number between 1 to 8
    row = input('Please enter a ship row (1-8): ').upper()
    while row not in '12345678':
        print("Please enter a valid row.")
        row = input('Please enter a ship row (1-8): ')

    # Enter the Ship column from A to H
    column = input('Please enter a ship column (A-H): ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column.")
        column = input('Please enter a ship column (A-H): ')

    return int(row) - 1, let_to_num[column]


def get_computer_location():
    row = randint(0, 7)
    column = randint(0, 7)
    return row, column


def create_ships(board):
    for _ in range(5):
        ship_r, ship_cl = randint(0, 7), randint(0, 7)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def play_battleship():
    create_ships(Hidden_Pattern)
    turns = 10

    while turns > 0:
        print('Welcome to Battleship')
        print_board(Guess_Pattern)
        print()

        # Player's turn
        row, column = get_ship_location()

        if Guess_Pattern[row][column] == '-':
            print('You already guessed that.')
        elif Hidden_Pattern[row][column] == 'X':
            print('Congratulations! You hit a battleship!')
            Guess_Pattern[row][column] = 'X'
            turns -= 1
        else:
            print('Sorry, you missed.')
            Guess_Pattern[row][column] = '-'
            turns -= 1

        if count_hit_ships(Guess_Pattern) == 5:
            print("Congratulations! You have sunk all the battleships.")
            break

        print('You have ' + str(turns) + ' turns remaining.')
        print()

        # Computer's turn
        comp_row, comp_column = get_computer_location()

        if Guess_Pattern[comp_row][comp_column] == '-':
            print("The computer already guessed that.")
        elif Hidden_Pattern[comp_row][comp_column] == 'X':
            print("Oh no! The computer hit your battleship!")
            Guess_Pattern[comp_row][comp_column] = 'X'
            turns -= 1
        else:
            print("Phew! The computer missed.")
            Guess_Pattern[comp_row][comp_column] = '-'
            turns -= 1

        if count_hit_ships(Guess_Pattern) == 5:
            print("Congratulations! You have sunk all the battleships.")
            break

        print('You have ' + str(turns) + ' turns remaining.')
        print()

        if turns == 0:
            print('Game Over')

    print('Hidden Pattern:')
    print_board(Hidden_Pattern)


play_battleship()
