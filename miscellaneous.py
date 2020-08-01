import random
board = [
        [7,0,6,9,0,0,0,4,0],
        [0,4,0,0,0,8,0,0,7],
        [0,0,9,7,0,0,0,0,0],
        [3,1,0,0,0,0,0,0,0],
        [0,7,0,1,0,6,0,3,0],
        [9,0,0,0,0,0,0,2,0],
        [5,0,0,0,0,2,6,0,0],
        [2,0,0,8,0,0,0,1,0],
        [0,9,0,0,0,1,0,0,0]
        ]

def print_grid():
    for row in board:
        print(row)

def find_empty(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False

def used_in_col(arr, col, num):
    for i in range (9):
        if arr[i][col] == num:
            return True
    return False

def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i+row][j+col] == num:
                return True

    return False
def check_safe(arr, col, num, row):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row, col, num)

def solve_sudoku(arr):
    l = [0,0]

    if not find_empty(arr, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1,10):
        if check_safe(arr, col, num, row):
            if solve_sudoku(arr):
                return True

if __name__ == "__main__":
    if solve_sudoku(board):
        print_grid()