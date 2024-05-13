from tryingboard import print_board
from tryingboard import new_board
from tryingactions import flattened_ships

ship1 = [[1][1] , [1][2] , [1][3]]
ship2 = [[3][8], [4][8], [5][8], [6][8]]
ship3 = [[8][1], [8][2]]
ship4 = [[6][3], [6][4], [6][5], [6][6], [6][7]]
ship5 = [[5][9], [6][9], [7][9]]
computers_ships_all = [ship1, ship2, ship3, ship4, ship5]

while True:
    print_board(board)
    command = input("Enter a command: ")
    if command == "SHOOT":
        print("Where will you shoot?")
        coordinate = input("Choose a coordinate: ")
        if coordinate[0] in abc and int(coordinate[1]) in range(10):
            coordinate_letter = abc.index(coordinate[0])
            coordinate_number = int(coordinate[1])
            print("Shot at", coordinate)
            temp = flattened_ships(computer_ships_all)
            if coordinate in temp:
                print("YOU HIT A BATTLESHIP")    
            else:
                print("Oh! That's a miss :(")
    elif command == "RESTART":
        exit()
    elif command == "PLACE":
        print("You have 5 ships of different lengths. Choose the coordinates at each end of every ship")
    else:
        print("Invalid. Try to enter a command from the ones established in the instructions")

