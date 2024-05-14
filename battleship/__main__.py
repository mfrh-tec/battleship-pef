from board import print_board
from board import new_board
from actions import flattened_ships

#Setting up the instructions
with open('README.md', 'r') as f:
   print(f.read())

#Where the computer's ships are found
computer_ship_1 = ["B5", "B6", "B7"]
computer_ship_2 = ["D8", "E8", "F8", "G8"]
computer_ship_3 = ["J1", "J2"]
computer_ship_4 = ["H3", "H4", "H5", "H6", "H7"]
computer_ship_5 = ["F9", "G9", "H9"]
computer_ships_all = [computer_ship_1, computer_ship_2, computer_ship_3, computer_ship_4, computer_ship_5]

abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
board = new_board()

#GAMELOOP
while True:
   print_board(board)
   command = input("Enter a command: ")#Restart or shoot
   if command == "SHOOT":
       print("Where will you shoot?")
       coordinate = input("Choose a coordinate: ")
       if coordinate[0] in abc and int(coordinate[1]) in range(10):#converting the lettered coordinates into numbered
           coordinate_letter = abc.index(coordinate[0])
           coordinate_number = int(coordinate[1])
           print("Shot at", coordinate)
           board[coordinate_number][coordinate_letter] = "X"
           temp = flattened_ships(computer_ships_all)#recovering ship coordinates
           if coordinate in temp:
               print("YOU HIT A BATTLESHIP")
               board[coordinate_number][coordinate_letter] = "O"
           else:
               print("Oh! That's a miss :(")
   elif command == "RESTART":
       exit()
   else:
       print("Invalid. Try to enter a command from the ones established in the instructions")