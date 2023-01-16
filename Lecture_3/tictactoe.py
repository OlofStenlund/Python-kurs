# Design of the board
row_divider = ['-------------']
row1 = ['|  ', '|  ', '|  ', "|"]
row2 = ['|  ', '|  ', '|  ', "|"]
row3 = ['|  ', '|  ', '|  ', "|"]

# Playable rows as a list of lists
row_group = [row1, row2, row3]

# Entire board
board = [row_divider, row1, row_divider, row2, row_divider, row3, row_divider]

# Functions, starting with the main function that runts the game
def main():
    print("Welcome to the game! You know the rules, right?\nPlayer one plays 'X' and player 2 plays 'O'")
    while True:
        print("Here is the board:")
        print_board()
        player = switch_player()
        input_validated = validate_input()
        truefalse = validate_placement(input_validated)
        if truefalse == True:
            modify_board(input_validated[0], input_validated[1], player)
            any_winner = check_winner(player)
            if any_winner == 1:
                print_board()
                print("Here is the final results.\nThe game has ended!")
                if player == 'X':
                    input(f"The winner is player 1!\nPress enter to quit")
                elif player == 'O':
                    input(f"The winner is player 2!\nPress enter to quit")
                break  
            elif any_winner == 2:
                print_board()
                input("The board is full, game over.\nPress enter to quit.")
                break          
            # elif any_winner != 1 and any_winner != 2:
            else:
                print("The game carries on")
                pass
        else:
            print("Invalid, space allready taken. Choose another one.")

# Other functions
def print_board():
    for i in board:
        print(*i)

def switch_player():
    if row_group[0].count('| X')+row_group[1].count('| X')+row_group[2].count('| X') > row_group[0].count('| O')+row_group[1].count('| O')+row_group[2].count('| O'):
        player = 'O'
        print(f"Time for player 2,", player)
        return player
    if row_group[0].count('| X')+row_group[1].count('| X')+row_group[2].count('| X') == row_group[0].count('| O')+row_group[1].count('| O')+row_group[2].count('| O'):        
        player = 'X'
        print(f"Time for player 1,", player)
        return player
    else:
        player = 'X'
        print(f"Time for", player)
        return player

def get_input():
    while True:
        mark_row = input("On what row would you like to place your mark? (1/2/3)")
        if mark_row.isnumeric():
            mark_row = int(mark_row)
            break
        else:
            print("Invalid input. Try again")
            continue
       
    while True: 
        mark_place = input("Alright, on what place would you like to place your mark? (1/2/3)")
        if mark_place.isnumeric():
            mark_place = int(mark_place)
            break
        else:
            print("Invalid input. Try again")
            continue

    return (mark_row, mark_place)

def validate_input():
    run = True
    while run == True:
        input_list = get_input() 
        if all(1 <= i <= 3 for i in input_list):
            return(input_list)
            break
        else:
            print(f"Invalid. You entered", input_list[0], "and", input_list[1])
            print("Inputs must be 1, 2 or 3.")
            continue

def validate_placement(inp: int): # returns poistions mark_row, mark_place
    if inp[0] == 1:     
        if row1[inp[1]-1] == '|  ':
            return True
    if inp[0] == 2:
        if row2[inp[1]-1] == '|  ':
            return True
    if inp[0] == 3:
        if row3[inp[1]-1] == '|  ':
            return True
    else:
        return False

def modify_board(mark_row: int, mark_place: int, player: str): # when running the function, get result of get_input() into here
    if mark_row == 1:
        row1[mark_place-1] = (f"| {player}") 
    elif mark_row == 2:
        row2[mark_place-1] = (f"| {player}")
    elif mark_row == 3:
        row3[mark_place-1] = (f"| {player}")

def check_winner(player):
    # Check for winner horizontally
    if row_group[0].count(f"| {player}") == 3 or row_group[1].count(f"| {player}") == 3 or row_group[2].count(f"| {player}") == 3 :
        return 1
    # check for winner vertically
    place1 = 0
    place2 = 0
    place3 = 0
    for i in row_group: 
        place1 += i[0:1].count(f"| {player}")
        place2 += i[1:2].count(f"| {player}")     
        place3 += i[2:3].count(f"| {player}")
        if place1 == 3 or place2 == 3 or place3 == 3:
            return 1
        else:
            pass
    # Check for winners diagonally
    if row_group[0][0] == (f"| {player}") and row_group[1][1] == (f"| {player}") and row_group[2][2] == (f"| {player}"):
        return 1
    elif row_group[0][2] == (f"| {player}") and row_group[1][1] == (f"| {player}") and row_group[2][0] == (f"| {player}"):
        return 1

    if row_group[0][0:3].count("|  ") + row_group[1][0:3].count("|  ") + row_group[2][0:3].count("|  ") == 0:
        return 2

main()