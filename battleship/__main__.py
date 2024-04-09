from board import battleship_board, create_ships

with open('README.md', 'r') as f:
    print(f.read())
    
while True:
    command = input("Enter a command: ")
    print(command)
    if command == "hello":
         print("hello")
    elif command == "restart":
         exit()
    elif command[0] in ["A", "B", "C", ] and int(command[1]) in range(10):
        print("Shot at", command)
    else:
         print("Command not valid")
