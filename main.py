# Gameplay grid
grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_grid(grid):
    for row in grid:
        print(row)


def user_input():
    acceptable_values = ["1", "2", "3"]
    row_num = "WRONG"
    col_num = "WRONG"

    # While input != [1-3], keep asking user until they give input between 1-3
    while row_num not in acceptable_values or col_num not in acceptable_values:
        # Row Input
        row_num = input("Pick a row #: ")
        while not row_num.isdigit() or row_num not in acceptable_values:
            print("Please type a number between 1-3")
            row_num = input("Pick a row #: ")

        # Col Input
        col_num = input("Pick a col #: ")
        while not col_num.isdigit() or col_num not in acceptable_values:
            print("Please type a number between 1-3")
            col_num = input("Pick a col #: ")

    # Cast row_num & col_num as int2
    row_num = int(row_num) - 1
    col_num = int(col_num) - 1

    # Pos is filled
    if grid[row_num][col_num] != " ":
        print("There's a player here already. Try another position after viewing the grid below!")
        print_grid(grid)
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

    # Win by 3 in a row for X
    if (grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X") or (grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X") or (grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X"):
        print("Player X has won")
        play_again()
    # Win by 3 in a row for O
    elif (grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O") or (grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O") or (grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O"):
        print("Player O has won")
        play_again()
    # Win by 3 in a column for X
    elif (grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X") or (grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X") or (grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X"):
        print("Player X has won")
        play_again()
    # Win by 3 in a column for O
    elif (grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O") or (grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O") or (grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O"):
        print("Player O has won")
        play_again()
    # Win by 3 in a diagonal for X
    elif (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X"):
        print("Player X has won")
        play_again()
    # Win by 3 in a diagonal for O
    elif (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O"):
        print("Player O has won")
        play_again()
    # Tie
    elif not (any(" " in item for item in grid)):
        print("It's a tie!")
        play_again()
    # If no winners, keep asking for UI
    else:
        print_grid(grid)
        user_input()


def play_again():
    global grid
    print_grid(grid)
    restart = input("Do you want to play again? Type 'Y' or 'N' ")
    restart = restart.upper()
    restart_values = ['Y', 'N']

    while restart not in restart_values:
        print("Please type 'Y' or 'N'")
        restart = input("Do you want to play again? Type 'Y' or 'N' ")

    # Restart the game if player inputs "Y"
    if restart == "Y":
        grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        user_input()
    # End the game if player inputs "N"
    else:
        print("Thanks for playing!")


user_input()

# Extra features:
# Toggle player on and off without needing user input (have it switch off with conditionals)
