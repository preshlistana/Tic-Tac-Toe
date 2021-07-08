# Gameplay grid
grid = [["", "", ""], ["", "", ""], ["", "", ""]]


def game():
    user_input()


def user_input():
    acceptable_values = ["0", "1", "2"]
    row_num = "WRONG"
    col_num = "WRONG"

    # While input != [0-2], keep asking user until they give input between 0-2
    while row_num not in acceptable_values or col_num not in acceptable_values:
        # Row Input
        row_num = input("Pick a row #: ")
        while not row_num.isdigit() or row_num not in acceptable_values:
            print("Please type a number between 0-2")
            row_num = input("Pick a row #: ")

        # Col Input
        col_num = input("Pick a col #: ")
        while not col_num.isdigit() or col_num not in acceptable_values:
            print("Please type a number between 0-2")
            col_num = input("Pick a col #: ")

    # Cast row_num & col_num as int2
    row_num = int(row_num)
    col_num = int(col_num)

    # Pos is filled
    if grid[row_num][col_num]:
        print("There's a player here already. Try another position after viewing the grid below!")
        print(grid)
        user_input()
    # Pos is not filled
    else:
        # Player input
        player = input("Which player: O or X? ")
        player_values = ["X", "O", "x", "o"]

        # While player != "O" or "X", ask user to input the correct player
        while player not in player_values:
            print("Please type 'O' or 'X'")
            player = input("Which player: O or X? ")
            # Converts lowercase char to uppercase
            if player == "x" or player == "o":
                player = player.upper()

        # Puts UI into grid
        place_to_grid(row_num, col_num, player)


def place_to_grid(row_num, col_num, player):
    grid[row_num][col_num] = player

    # Win by 3 in a row
    if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        print("Player X has won")
        play_again()
    elif grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        print("Player O has won")
        play_again()
    # If no winners, keep asking for UI
    else:
        print(grid)
        grid = [["", "", ""], ["", "", ""], ["", "", ""]]
        user_input()


def play_again():
    restart = input("Do you want to play again? Type 'Y' or 'N' ")
    restart = restart.upper()
    restart_values = ['Y', 'N']

    while restart not in restart_values:
        print("Please type 'Y' or 'N'")
        restart = input("Do you want to play again? Type 'Y' or 'N' ")

    # Restart the game if player inputs "Y"
    if restart == "Y":
        game()
    # End the game if player inputs "N"
    else:
        print("Thanks for playing!")


game()


# Priorities
# 1) Scoring system (rows, columns, diagonals):
# Methods
# a) Win by rows: grid[0][0-3] OR grid[1][0-3] OR grid[2][0-3] are all "Os" or "X"
# b) Win by diagonals: grid[0][0], grid[1][1], grid[2][2] OR grid[0][2], grid[1][1], grid[2][0] are all "Os" or "Xs"
# c) Win by columns: grid[0][0], grid[1][0], grid[2][0] OR grid[0][1], grid[1][1], grid[2][1] OR grid[0][2], grid[1][2] OR grid[2][2]

# 2) Resetting the grid when the player has won

# Extra features:
# Toggle player on and off without needing user input
