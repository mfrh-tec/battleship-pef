from battleship.board import new_board
from battleship.actions import coordinate_to_shoot, verify_if_sink, shuffle_shipss


def test_coordinate_to_shoot():
    print("Choose a coordinate to shoot at")
    board=new_board()
    coordinate_to_shoot(board, 0,0)
    assert board[0][0] == "X"
#make sure that in position 0,0 there is X 
