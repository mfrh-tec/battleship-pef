#Creating the board for computer
computer_board = [[""] * 10 for x in range(10)]

#Creating the board for the user to play in
user_board = [[""] * 10 for c in range(10)]

def battleship_board(board):
    print(" A    B  C   D   E   F   G   H   I   J ")
    print(" --------------------------------------")
    rows = 1
    for rows in board:
        print()
        rows += 1
#Ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"