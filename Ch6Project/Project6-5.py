
def print_border():
    print("+---+---+---+")


def print_row(board, row):
    print(f"| {board[row-1][0]} | {board[row-1][1]} | {board[row-1][2]} |")


def display_board(board):
    print_border()
    print_row(board, 1)
    print_border()
    print_row(board, 2)
    print_border()
    print_row(board, 3)
    print_border()    


def make_move(board, row, col, character):
    board[row - 1][col - 1] = character


def validate_move(board, row, col):
    if board[row - 1][col - 1] == "X" or board[row - 1][col - 1] == "O":
        return False
    else:
        return True


def user_choice(board, turn):
    if turn == True:
        character = "X"
    else:
        character = "O"
    print(f"{character}'s turn")
    print()
    choose_row = int(input("Pick a row (1, 2, 3): "))
    choose_col = int(input("Pick a column (1, 2, 3): "))
    print()
    valid = validate_move(board, choose_row, choose_col)
    if valid == True:
        make_move(board, choose_row, choose_col, character)
    else:
        print("Space taken. Please choose an empty space.")


def check_for_win(board, turn, win):

    check_win = False
    if turn == True:
        check = ["X", "X", "X"]
        character = "X"
    else:
        check = ["O", "O", "O"]
        character = "O"
    
    row_1 = board[0]
    row_2 = board[1]
    row_3 = board[2]
    col_1 = [board[0][0], board[1][0], board[2][0]]
    col_2 = [board[0][1], board[1][1], board[2][1]]
    col_3 = [board[0][2], board[1][2], board[2][2]]
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[2][0], board[1][1], board[0][2]]

    if check == row_1:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True
    elif check == row_2:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True
    elif check == row_3:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True
    elif check == col_1:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True
    elif check == col_2:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True
    elif check == col_3:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True
    elif check == diagonal_1:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True
    elif check == diagonal_2:
        print(f"{character} wins!")
        print()
        print("Game over!")
        return True



def check_for_full(board):
    for row in board:
        if " " in row:
            return False
    return True        



def main():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    game = True
    turn = True
    win = False
    while game == True:
        user_choice(board, turn)
        display_board(board)
        win = check_for_win(board, turn, win)
        draw = check_for_full(board)
        if win == True:
            break
        elif draw == True:
            print()
            print("It's a draw!")
            break
        else:
            turn = not turn       
        
        


if __name__ == "__main__":
    main()
