from board import print_board
from board import new_board
with open('README.md', 'r') as f:
    print(f.read())

ship_coordinate = ["B5", "B6", "B7", "D8", "E8", "F8", "G8", "J1", "J2"] 
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
board = new_board()
while True:
    print_board(board)
    command = input("Enter a command: ")
    if command == "hello":
         print("hello")
    elif command == "restart":
         exit()
    elif command[0] in abc and int(command[1]) in range(10):
        print("Shot at", command)
        if command in ship_coordinate:
            print("THAT'S A HIT!")
        else:
            print("Ooh! That's a miss :(")
    else:
         print("Command not valid")

