from test_board import new_board
from test_actions import 


def test_coordinate_to_shoot():
    print("Choose a coordinate to shoot at")
    board=new_board()
    coordinate_to_shoot(board, row, column, 0,0)
    assert board[0][0] == board[0]

