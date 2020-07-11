import random
board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
]
def print_board(board):
    for row in board:
        print(row)

def fill_row():
        pass


a = {"aartg" :343, "bart" : 984, "crter" : 74}
b = max(a.values())
def get_key(val):
        for key , value in a.items():
                if val == value:
                        return key
print(get_key(b))