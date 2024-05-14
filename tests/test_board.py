ship1 = [[1][1] , [1][2] , [1][3]]
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
