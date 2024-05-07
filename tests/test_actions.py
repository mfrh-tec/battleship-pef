from battleship.board import new_board
from battleship.actions import coordinate_to_shoot, verify_if_sink, shuffle_shipss


def test_coordinate_to_shoot():
    print("Choose a coordinate to shoot at")
    board=new_board()
    coordinate_to_shoot(board, 0,0)
    assert board[0][0] == "X"
#make sure that in position 0,0 there is X 

def test_flattened_ships(computers_ships_all):
    return_ships = []
    for i in computers_ships_all:
        for j in i:
            return_ships.insert(0, j)
    return return_ships