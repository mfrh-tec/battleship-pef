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

    if command == "PLACE SHIPS":
        print ("You have 3 ships of different sizes. Ship 1 is 3 squares long, Ship 2 is 4 squares long, and Ship 3 is 2 squares long. Choose wehre you'll place them.")
        user_ship_1 = [input("Coordinates for Ship 1: ")]
        user_ship_2 = [input("Coordinates for Ship 2: ")]
        user_ship_3 = [input("Coordinates for Ship 3: ")]


    elif command == "SHOT ATTEMPT":
        print("Where will you shoot?")
        coordinate = input("Choose a coordinate: ")
        if coordinate[0] in abc and int(coordinate[1]) in range(10):
            coordinate_letter = abc.index(coordinate[0])
            coordinate_number = int(coordinate[1])
            print("Shot at", coordinate)
            print_board(board, coordinate_letter, coordinate_number)
    elif command == "RESTART":
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