from random import choice
from copy import deepcopy

def printBoard(board):
    for row in board:
        print(row)

def finished(board, x, y, ch):
    inp = 3 * x + y
    if all(map(lambda k: k == ch, board[x])) or all(map(lambda k: k == ch, [board[0][y], board[1][y], board[2][y]])):
        return True, False
    elif inp in [0, 4, 8] and all(map(lambda k: k == ch, [board[0][0], board[1][1], board[2][2]])):
        return True, False
    elif inp in [2, 4, 6] and all(map(lambda k: k == ch, [board[0][2], board[1][1], board[2][0]])):
        return True, False
    elif board[0].count('-') + board[1].count('-') + board[2].count('-') == 0:
        return True, True
    return False, False

def utility(board, x, y, c_inp, turn): # turn = True (computer)
    won, draw = finished(board, x, y, c_inp)

    if draw:
        return 0
    elif turn:
        if won: return 1
        else: return 2
    else:
        if won: return -1
        else: return 2

def computer_move(board, c_inp, turn):
    global n
    if not turn:
        ch = 'x' if c_inp == 'o' else 'o'
    else:
        ch = c_inp

    best_coords, best = [-1, -1], -10
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = ch
                ut = utility(board, i, j, c_inp, turn)
                if ut != 2 and ut > best:
                    best_coords = [i, j]
                    best = ut

                if ut == 2:
                    ut2 = computer_move(deepcopy(board), c_inp, not turn)
                    if ut2[1] != 2 and ut2[1] > best:
                        best_coords = [i, j]
                        best = ut2[1]
    return best_coords, best


board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

stop, cmp_turn = False, choice([True, False])
c_inp = choice(['x', 'o'])
h_inp = 'x' if c_inp == 'o' else 'o'
printBoard(board)
print(f"You're playing {h_inp}")

while not stop:
    positions = []
    if cmp_turn:
        print("Computer's Turn")
        x, y = computer_move(deepcopy(board), c_inp, True)[0]
        ch = c_inp
    else:
        print("Your Turn")
        inp = int(input("Enter the position: "))
        x, y = inp // 3, inp % 3
        # x, y = computer_move(deepcopy(board), h_inp, True)[0]
        ch = h_inp
        
    if board[x][y] != '-':
        print("Position is already filled. SMH!")
        continue

    board[x][y] = ch
    printBoard(board)
    won, draw = finished(board, x, y, ch)
    cmp_turn = not cmp_turn

    if draw:
        print("Draaaaaaaw!")
        stop = True
    else:
        if won and cmp_turn:
            print("You won!")
            stop = True
        elif won and not cmp_turn:
            print("Computer won!")
            stop = True