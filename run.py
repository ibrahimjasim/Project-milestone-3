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


def get_row_from_user():
    while True:
        row = input('Please enter a ship row (1-8): ')
        if row not in ['1','2','3','4','5','6','7','8']:
            print("Please enter a valid row(1<= row <= 8)")
            continue
        else:
            return int(row)-1

def get_col_from_user():
    while True:
        column = input('Please enter a ship column (A-H): ').upper()
        if column not in ['A','B','C','D','E','F','G','H']:
            print("Please enter a valid column(A <= column <= H)")
            continue
        else:
            return let_to_num[column]

# Function to get a random location for the computer's turn
def get_computer_location():
    return randint(0, 7), randint(0, 7)


# Function to create ships on the board with variable difficulty
def create_ships(board, num_ships):
    for _ in range(num_ships):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_col] == 'X':
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = 'X'


# Function to count the number of hit ships
def count_hit_ships(board):
    return sum(row.count('X') for row in board)

# Main function to play the game
def play_battleship():
    print('Welcome to Battleship')

    # Setting different difficulties: 5 ships for player, 3 ships for computer
    create_ships(Player_Hidden_Pattern, 5)
    create_ships(Computer_Hidden_Pattern, 5)
    turns = 10
    player_hits = 0
    computer_hits = 0

    while turns > 0:
        print_boards(Player_Guess_Pattern, Computer_Guess_Pattern)
        print()

        # Player's turn
        row = get_row_from_user()
        column = get_col_from_user()

        if Player_Guess_Pattern[row][column] == '-':
            print('You already guessed that.')
        elif Computer_Hidden_Pattern[row][column] == 'X':
            print('Congratulations! You hit a battleship!')
            Player_Guess_Pattern[row][column] = 'X'
            player_hits += 1
        else:
            print('Sorry, you missed.')
            Player_Guess_Pattern[row][column] = '-'
        turns -= 1

        if player_hits == 5:  # Win condition based on computer's ships
            print("Congratulations! You have sunk all the computer's battleships.")
            break

        print('You have ' + str(turns) + ' turns remaining.')
        print()

        # Computer's turn
        comp_row, comp_column = get_computer_location()

        if Computer_Guess_Pattern[comp_row][comp_column] in ['X', '-']:
            continue
        elif Player_Hidden_Pattern[comp_row][comp_column] == 'X':
            print("Oh no! The computer hit your battleship!")
            Computer_Guess_Pattern[comp_row][comp_column] = 'X'
            computer_hits += 1
        else:
            print("The computer missed!")
            Computer_Guess_Pattern[comp_row][comp_column] = '-'

        if computer_hits == 5:  # Computer's win condition
            print("Oh no! The computer has sunk all your battleships.")
            break

    if turns == 0:
        print('Game Over')
        print_boards(Player_Guess_Pattern, Computer_Guess_Pattern)
        if player_hits > computer_hits:
            print("Congratulations! You have won with more hits.")
        elif computer_hits > player_hits:
            print("Oh no! The computer has won with more hits.")
        else:
            print("It's a tie based on hits!")

# play the game
play_battleship()