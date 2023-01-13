# Design of the board
row_divider = ['-------------']
row1 = ["|", " ", "|", " ", "|", " ", "|"]
row2 = ["|", " ", "|", " ", "|", " ", "|"]
row3 = ["|", " ", "|", " ", "|", " ", "|"]

# Playable rows as a list of lists
row_group = [row1, row2, row3]

# Entire board
board = [row_divider, row1, row_divider, row2, row_divider, row3, row_divider]

# Functions, starting with the main function that runts the game
def main():
    print("Welcome to the game! You know the rules, right?\nPalyer one plays 'X' and player 2 plays'O")
    while True:
        print("Here is the board:")
        print_board()
        player = swith_player()
        input_validated = validate_input()
        truefalse = validate_placement(input_validated)
        if truefalse == True:
            modify_board(input_validated[0], input_validated[1], player)
            input_validated = modify_board(input_validated[0], input_validated[1], player)
            any_winner = check_winner(player)
            if any_winner == True:
                print_board()
                print("Here is the final results.")
                print("The game has ended!")
                if player == 'X':
                    print(f"The winner is player 1!\nPress enter to quit")
                elif player == 'O':
                    print(f"The winner is player 2!\nPress enter to quit")
                input("")
                break            
            else:
                print("The game carries on")
                pass
        else:
            print("Invalid, space allready taken. Choose another one.")

def print_board():
    for i in board:
        print(*i)

def get_input():
    while True:
        mark_row = input("On what row would you like to place your mark? (1/2/3)")
        if mark_row == "":
            print("Invalid input. Try again")
            continue
        else:
            mark_row = int(mark_row)
            break
       
    while True: 
        mark_place = input("Alright, on what place would you like to place your mark? (1/2/3)")
        if mark_place == "":
            print("Invalid input. Try again")
            continue
        else:
            mark_place = int(mark_place)
            break

    return (mark_row, mark_place)

def modify_board(mark_row: int, mark_place: int, player: str): # when running the function, get result of get_input() into here
    if mark_place == 1:
        index_place = mark_place
    elif mark_place == 2:
        index_place = mark_place+1
    elif mark_place == 3:
        index_place = mark_place+2
    if mark_row == 1:
        row1[index_place] = player 
    elif mark_row == 2:
        row2[index_place] = player
    elif mark_row == 3:
        row3[index_place] = player

def validate_placement(inp): # returns poistions mark_row, mark_place
    in_0 = inp[0]
    in_1 = 1
    if inp[1] == 2:
        in_1 = 3
    elif inp[1] == 3:
        in_1 = 5
    else:
        pass
    if inp[0] == 1:     
        if row1[in_1] != ' ':
            return False
        else:
            return True
    if inp[0] == 2:
        if row2[in_1] != ' ':
            return False
        else:
            return True
    if inp[0] == 3:
        if row3[in_1] != ' ':
            return False
        else:
            return True
    cleared_list = []
    return cleared_list

def validate_input():
    run = True
    while run == True:
        input_list = []
        input_list = get_input()
        if all(isinstance(i, int) and 1 <= i <= 3 for i in input_list):
            return(input_list)
            break
        else:
            print(f"Invalid. You entered", input_list[0], "and", input_list[1])
            print("Inputs must be 1, 2 or 3.")

def swith_player():
    if row_group[0].count('X')+row_group[1].count('X')+row_group[2].count('X') > row_group[0].count('O')+row_group[1].count('O')+row_group[2].count('O'):
        player = 'O'
        print(f"Time for player 2,", player)
        return player
    if row_group[0].count('X')+row_group[1].count('X')+row_group[2].count('X') == row_group[0].count('O')+row_group[1].count('O')+row_group[2].count('O'):        
        player = 'X'
        print(f"Time for player 1,", player)
        return player
    else:
        player = 'X'
        print(f"Time for", player)
        return player

def check_winner(player):
    # Check for winner horizontally
    if row_group[0].count(player) == 3 or row_group[1].count(player) == 3 or row_group[2].count(player) == 3 :
        return True
    # check for winner vertically
    place1 = 0
    place2 = 0
    place3 = 0
    for i in row_group: # checks every index per row. Make it only check one index?
        place1 += i[1:2].count(player)
        place2 += i[3:4].count(player)     
        place3 += i[5:6].count(player)
        if place1 == 3 or place2 == 3 or place3 == 3:
            return True
        else:
            pass
    # Check for winners diagonally
    if row_group[0][1] == player and row_group[1][3] == player and row_group[2][5] == player:
        return True
    elif row_group[0][5] == player and row_group[1][3] == player and row_group[2][1] == player:
        return True

main()