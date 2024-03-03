from random import randint

def initialize_game_boards():
    '''
        Initialize game boards before the game
    '''
    player_hidden_pattern = [[' '] * 8 for _ in range(8)]
    player_guess_pattern = [[' '] * 8 for _ in range(8)]
    computer_hidden_pattern = [[' '] * 8 for _ in range(8)]
    computer_guess_pattern = [[' '] * 8 for _ in range(8)]

    return (player_hidden_pattern,
            player_guess_pattern,
            computer_hidden_pattern,
            computer_guess_pattern)


def print_boards(board1, board2, 
                 board1_title="Your Guesses", board2_title="Computer's Guesses"):
    '''
        Function to print two game boards side by side

        input : 
            board1 : list of characters related to the user
            board2 : list of characters related to the computer
            board1_title : title of the user board
            board2_title : title of the computer board

        output : 
            prints the title of two boards and then the boards themselves

    '''
    print(f'{board1_title:20s}    {board2_title}')
    print('   A B C D E F G H      A B C D E F G H')
    print('   ****************     ****************')
    for row_num in range(8):
        row1 = " ".join(board1[row_num])
        row2 = " ".join(board2[row_num])
        print(f"{row_num + 1}|{row1}|    {row_num + 1}|{row2}|")


def get_row_from_user():
    '''
        Get the row as a input from the user and then
        validate the user input. If it is not correct,
        let the user again enter the row. Once a valid 
        input is detected, convert that to an int and return.
    '''

    while True:
        row = input('Please enter a ship row (1-8): ')
        if row not in ['1','2','3','4','5','6','7','8']:
            print("Please enter a valid row ( 1<= row <= 8 ) ")
            continue
        else:
            return int(row)-1


def get_col_from_user():
    '''
        Get the column as a input from the user and then
        validate the user input. If it is not correct,
        let the user again enter the row. Once a valid 
        input is detected, get the corresponding index value and return.

    '''

    # Mappings for columns
    letters_to_index_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    while True:
        column = input('Please enter a ship column (A-H): ').upper()
        if column not in ['A','B','C','D','E','F','G','H']:
            print("Please enter a valid column ( A <= column <= H ) ")
            continue
        else:
            return letters_to_index_mapping[column]


def get_computer_location():
    '''
        Get the location choosen by the computer. This location
        is randomly decided.
    '''
    return randint(0, 7), randint(0, 7)


def create_ships(board, num_ships):
    '''
        This function places ships on the board randomly.

        input : number of ships to be placed on the board.
    '''
    for _ in range(num_ships):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_col] == 'X':
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = 'X'


def count_hit_ships(board):
    '''
        Count the number of ships that are hit.

        input : board to count the hit number of ships
    '''
    return sum(row.count('X') for row in board)


def handle_user_turn(
        player_guess_pattern,
        computer_hidden_pattern,
        number_of_ships,
        player_hits):
    '''
        Handle the player's turn

        Input :
        player_guess_pattern : to identify whether user has entered a previous guess.
        computer_hidden_pattern : to identify whether player hit a ship.
        number_of_ships : to decide whether the player has won.
        player_hits : to decide if the player has won and also to update the varaible.
    
    '''

    player_win_condition = False
    
    row = get_row_from_user()
    column = get_col_from_user()
    
    if player_guess_pattern[row][column] == '-':
        print('You already guessed that.')
    elif computer_hidden_pattern[row][column] == 'X':
        print('Congratulations! You hit a battleship!')
        player_guess_pattern[row][column] = 'X'
        player_hits += 1

        if player_hits == number_of_ships:
            print(
                "Congratulations! You have sunk all " + 
                "the computer's battleships."
            )
            player_win_condition = True

            return player_hits,player_win_condition
            
    else:
        print('Sorry, you missed.')
        player_guess_pattern[row][column] = '-'

    return player_hits,player_win_condition


def handle_computer_turn(
        computer_guess_pattern,
        player_hidden_pattern,
        number_of_ships,
        computer_hits):
    
    '''
        Handle the player's turn

        Input :
        computer_guess_pattern : to identify whether computer has guessed a previous guess.
        player_hidden_pattern : to identify whether computer hit a ship.
        number_of_ships : to decide whether the computer has won.
        computer_hits : to decide if the computer has won and also to update the varaible.
    
    '''
    
    computer_win_conditon = False
    
    comp_row, comp_column = get_computer_location()

    if computer_guess_pattern[comp_row][comp_column] == '-':
        print('You guessed an already guessed location.')
    elif player_hidden_pattern[comp_row][comp_column] == 'X':
        print("Oh no! The computer hit your battleship!")
        computer_guess_pattern[comp_row][comp_column] = 'X'
        computer_hits += 1
        if computer_hits == number_of_ships:
            print("Oh no! The computer has sunk all your battleships.")
            computer_win_conditon = True
            return computer_hits,computer_win_conditon
    else:
        print("The computer missed!")
        computer_guess_pattern[comp_row][comp_column] = '-'

    return computer_hits,computer_win_conditon


def game_over_condition_handler(
        turns,
        player_guess_pattern,
        computer_guess_pattern,
        player_hits,
        computer_hits):
    
    '''
        Check whether if the game is over and handles that

        Input :
        turns : to see whether there are any turns left
        player_guess_pattern : to print the player guessing.
        computer_guess_pattern : to print the computer guessing.
        player_hits : to decide the winner
        computer_hits : to decide the winner
    
    '''
    
    if turns == 0:
        print('Game Over')
        print_boards(player_guess_pattern, computer_guess_pattern)
        if player_hits > computer_hits:
            print("Congratulations! You have won with more hits.")
        elif computer_hits > player_hits:
            print("Oh no! The computer has won with more hits.")
        else:
            print("It's a tie based on hits!")


def restart_condition_handler():
    '''
        Check whether the user want to play another game.
    '''

    while True:
        user_input = input("Do you want to play another game (y/n) ? ").upper()
        if user_input not in ["Y","N"]:
            print("Invalid entry! Please enter y or n")
        else:
            if user_input=="Y":
                return True
            else:
                return False


def play_one_battleship_game():
    '''
        This function allow the user to play one battleship game
    '''

    # initialize game boards for both player and computer
    player_hidden_pattern,player_guess_pattern,computer_hidden_pattern,computer_guess_pattern  = initialize_game_boards()

    # initialize the variables related to one game
    turns = 10
    number_of_ships = 5
    player_hits = 0
    computer_hits = 0
    player_win_condition = False
    computer_win_condition = False
    
    # setting different difficulties using number of ships
    create_ships(player_hidden_pattern, number_of_ships)
    create_ships(computer_hidden_pattern, number_of_ships)

    print_boards(player_hidden_pattern,computer_hidden_pattern)

    print('Welcome to Battleship')
    print('=====================')
    while turns > 0:
        print_boards(player_guess_pattern, computer_guess_pattern)
        print()

        player_hits,player_win_condition = handle_user_turn(
            player_guess_pattern,
            computer_hidden_pattern,
            number_of_ships,
            player_hits)
        
        if player_win_condition:
            break

        turns -= 1

        print('You have ' + str(turns) + ' turns remaining.')
        print()

        # Computer's turn
        computer_hits,computer_win_condition = handle_computer_turn(
        computer_guess_pattern,
        player_hidden_pattern,
        number_of_ships,
        computer_hits)

        if computer_win_condition:
            break
    
        game_over_condition_handler(
            turns,
            player_guess_pattern,
            computer_guess_pattern,
            player_hits,
            computer_hits)


def play_battleship():
    '''
        Main driver of the game
        Allows the user to create a new game as well.
    '''

    while True:
        play_one_battleship_game()

        if not restart_condition_handler():
            print("Good Bye!")
            break


# play the game
play_battleship()