def new_board():
    board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
    return board 
def print_board(board, shot_coordinate):
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
    print("-----------------------------------------")
    for i in range(len(board)):
        row = f"{abc[i]} |"
        for j in range(len(board[i])):
            if (i, j) == shot_coordinate:
                row += " X |"  # Print "X" at the shot coordinate
            else:
                row += f" {board[i][j]} |"
        print(row)
        print("-----------------------------------------")
# Assuming new_board() returns the initial empty board
print_board(new_board())