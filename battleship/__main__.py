from board import print_board
from board import new_board
from actions import flattened_ships


#Instructions and guidelines
with open('README.md', 'r') as f:
    print(f.read())
#Where the computer´s ships will be found


#computer_ships_all = [computer_ship_1, computer_ship_2, computer_ship_3, computer_ship_4, computer_ship_5]
ship1 = [[1, 1], [1, 2], [1, 3]]
ship2 = [[3, 8], [4, 8], [5, 8], [6, 8]]
ship3 = [[8, 1], [8, 2]]
ship4 = [[6, 3], [6, 4], [6, 5], [6, 6], [6, 7]]
ship5 = [[5, 9], [6, 9], [7, 9]]
computers_ships_all = [ship1, ship2, ship3, ship4, ship5]
#defining variables
abc = enumerate["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
board = new_board()

#game loop
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
    else:
        print("Invalid. Try to enter a command from the ones established in the instructions")
    def computerships():
        if all(coordinate in flattened_ships(computers_ships_all) for coordinate in ship1):
            print("You sunk Ship #1")
        elif all(coordinate in flattened_ships(computers_ships_all) for coordinate in ship2):
            print("You sunk Ship #2")
        elif all(coordinate in flattened_ships(computers_ships_all) for coordinate in ship3):
            print("You sunk Ship #3")
        elif all(coordinate in flattened_ships(computers_ships_all) for coordinate in ship4):
            print("You sunk Ship #4")
        elif all(coordinate in flattened_ships(computers_ships_all) for coordinate in ship5):
            print("You sunk Ship #5")