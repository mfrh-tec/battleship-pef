from battleship.board import new_board
from battleship.actions import coordinate_to_shoot, flattened_ships


def test_coordinate_to_shoot():
    print("Choose a coordinate to shoot at")
    board=new_board() 
    coordinate_to_shoot(board, 0,0)
    assert board[0][0] == "X"
#make sure that in position 0,0 there is X 


def test_flattened_ships():
    board=new_board()
    flattened_ships(board, 0,0)
    assert board[0][0] == "X"


def test_verify_if_sink ():
    board=new_board()
    coordinate_to_shoot(board, 0,0)
    assert board[0][0] == "X"