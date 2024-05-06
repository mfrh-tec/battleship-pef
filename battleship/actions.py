

def shuffle_shipss():
    pass


def coordinate_to_shoot(board, row, column):
    pass


def verify_if_sink(board, ship_coordinates):
    pass

def flattened_ships(computers_ships_all):
    return_ships = []
    for i in computers_ships_all:
        for j in i:
            return_ships.insert(0, j)
    return return_ships