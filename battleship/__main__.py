from board import print_board
from board import new_board
#Instructions and guidelines
with open('README.md', 'r') as f:
    print(f.read())
#Where the computer´s ships will be found
computer_ship_1 = ["B5", "B6", "B7"] 
computer_ship_2 = ["D8", "E8", "F8", "G8"]
computer_ship_3 = ["J1", "J2"] 
computer_ships_all = [computer_ship_1, computer_ship_2, computer_ship_3]
#defining variables
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
board = new_board()
print_board(board, shot_coordinate=None)
#game loop
while True:
    command = input("Enter a command: ")
    if command == "Shot Attempt" or "shot attempt" or "SHOT ATTEMPT":
        print("Where will you shoot?")
        coordinate = input("Choose a coordinate: ")
        if coordinate[0] in abc and int(coordinate[1]) in range(10):
            coordinate_letter = abc.index(coordinate[0])
            coordinate_number = int(coordinate[1])
            print("Shot at", coordinate)
            print_board(board, (coordinate_letter, coordinate_number))
    elif command == "restart" or "Restart" or "RESTART":
        exit()
    else:
        print("Command not valid")
#player 1 attacks 
coordinate_player1=input("Give your coordinate")
if coordinate_player1 == (shuffle_ships,shuffle_ships): #not sure it is right 
    print ("red")
    print ("hit")
else:
    print ("white") 
    print ("miss") 