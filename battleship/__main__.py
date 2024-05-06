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

#game loop
while True:
    print_board(board)
    command = input("Enter a command: ")
    if command == "Shot Attempt" or "shot attempt" or "SHOT ATTEMPT":
        print("Where will you shoot?")
        coordinate = input("Choose a coordinate: ")
        if coordinate[0] in abc and int(coordinate[1]) in range(10):
            coordinate[0] = abc.index(coordinate[0])
            print("Shot at", coordinate)
            print("X", print_board(coordinate))
    elif command == "restart" or "Restart" or "RESTART":
        exit()
    else:
        print("Command not valid")




while True:
    print_board(board)
    command = input("Enter a command: ")
    if command == "hello":
         print("hello")
    elif command == "restart":
         exit()
    elif command[0] in abc and int(command[1]) in range(10):
        print("Shot at", command)
        pri("X", command, board)
        if command in computer_ships_all:
            print("THAT'S A HIT!")
        else:
            print("Ooh! That's a miss :(")
    else:
         print("Command not valid")



#player 1 attacks 
coordinate_player1=input("Give your coordinate")
if coordinate_player1 == (shuffle_ships,shuffle_ships): #not sure it is right 
 print red 
 print hit 
 else if print white 
print miss 