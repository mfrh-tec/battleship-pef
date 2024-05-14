def coordinate_to_shoot(board, row, column):
    print("Choose a coordinate to shoot at")
    board = new_board() # type: ignore #used to work, stopped last night, worked around it
    coordinate_to_shoot(board, 0,0)
    assert board[0][0] == "X"

def flattened_ships(computers_ships_all): #recollects the ships' positions
    return_ships = []
    for i in computers_ships_all:
        for j in i:
            return_ships.insert(0, j)
    return return_ships
