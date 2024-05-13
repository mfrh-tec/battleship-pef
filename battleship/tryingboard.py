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

def print_board(board):
    print(
        f"""
  {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} | {board[0][5]} | {board[0][6]} | {board[0][7]} | {board[0][8]} | {board[0][9]} 
----------------------------------------
  {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]} | {board[1][5]} | {board[1][6]} | {board[1][7]} | {board[1][8]} | {board[1][9]} 
----------------------------------------
  {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} | {board[2][5]} | {board[2][6]} | {board[2][7]} | {board[2][8]} | {board[2][9]} 
----------------------------------------
  {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} | {board[3][5]} | {board[3][6]} | {board[3][7]} | {board[3][8]} | {board[3][9]} 
----------------------------------------
  {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} | {board[4][5]} | {board[4][6]} | {board[4][7]} | {board[4][8]} | {board[4][9]} 
----------------------------------------
  {board[5][0]} | {board[5][1]} | {board[5][2]} | {board[5][3]} | {board[5][4]} | {board[5][5]} | {board[5][6]} | {board[5][7]} | {board[5][8]} | {board[5][9]} 
----------------------------------------
  {board[6][0]} | {board[6][1]} | {board[6][2]} | {board[6][3]} | {board[6][4]} | {board[6][5]} | {board[6][6]} | {board[6][7]} | {board[6][8]} | {board[6][9]} 
----------------------------------------
  {board[7][0]} | {board[7][1]} | {board[7][2]} | {board[7][3]} | {board[7][4]} | {board[7][5]} | {board[7][6]} | {board[7][7]} | {board[7][8]} | {board[7][9]} 
----------------------------------------
  {board[8][0]} | {board[8][1]} | {board[8][2]} | {board[8][3]} | {board[8][4]} | {board[8][5]} | {board[8][6]} | {board[8][7]} | {board[8][8]} | {board[8][9]} 
----------------------------------------
  {board[9][0]} | {board[9][1]} | {board[9][2]} | {board[9][3]} | {board[9][4]} | {board[9][5]} | {board[9][6]} | {board[9][7]} | {board[9][8]} | {board[9][9]} 
"""
    )

print_board(new_board())

ship1 = [[1][1], [1][2], [1][3]]
ship2 = [[3][8], [4][8], [5][8], [6][8]]
ship3 = [[8][1], [8][2]]
ship4 = [[6][3], [6][4], [6][5], [6][6], [6][7]]
ship5 = [[5][9], [6][9], [7][9]]
computers_ships_all = [ship1, ship2, ship3, ship4, ship5]

def computerships():
  if ship1 == True:
    print("You sunk Ship #1")
  elif ship2 == True:
    print("You sunk Ship #2")
  elif ship3 == True:
    print("You sunk Ship #3")
  elif ship4 == True:
    print("You sunk ship #4")
  elif ship5 == True:
    print("You sunk Ship #5")
  elif computers_ships_all == True:
    print("CONGRATS! YOU WON, YOU SUNK ALL SHIPS!")



