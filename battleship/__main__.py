from board import battleship_board, create_ships

abc = ["A", "B", "C", "D", "E", "F", "G", "H", "J"]
rows_where_ship = int[ "1", "2", "5", "6", "7", "8"]
with open('README.md', 'r') as f:
    print(f.read())
    
while True:
    command = input("Enter a command: ")
    print(command)
    if command == "hello":
         print("hello")
    elif command == "restart":
         exit()
    elif command[0] in abc and int(command[1]) in range(10):
        print("Shot at", command)
        if command[0] in abc[1, 4, 5, 6, 7, 9] and int(command[1]) in rows_where_ship
        ["B5", "B6", "B7", "D8", "E8", "F8", "G8", "J1", "J2"]
            print("THAT'S A HIT!")
        else
            print("Ooh! That's a miss :(")
    else:
         print("Command not valid")
