from copy import deepcopy
from time import time

grid = [[0 for _ in range(5)] for _ in range(5)]
grid[2][4] = 1
n = 0
start = time()

def getSum(grid, cols, diagonals):
    for row in grid:
        if row.count(0) == 0:
            return sum(row)

    for col in cols:
        if col.count(0) == 0:
            return sum(col)

    for diagonal in diagonals:
        if diagonal.count(0) == 0:
            return sum(diagonal)

    return -1

def validGrid(grid):
    cols = []
    for i in range(5):
        cols.append([grid[0][i], grid[1][i], grid[2][i], grid[3][i], grid[4][i]])
    diagonals = [[grid[0][0], grid[1][1], grid[2][2]], [grid[3][3], grid[4][4], grid[4][0], grid[3][1], grid[2][2]], [grid[1][3], grid[0][4] ]]
    total = getSum(grid, cols, diagonals)
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5:0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15:0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0,22: 0, 23: 0, 24: 0, 25: 0 }
    if total != -1:
        for row in grid:
            for i in range(1, 26):
                count[i] += row.count(i)
            if row.count(0) == 0 and sum(row) != total: return False
        for col in cols:
            if col.count(0) == 0 and sum(col) != total: return False
        for diagonal in diagonals:
            if diagonal.count(0) == 0 and sum(diagonal) != total: return False
    for val in count.values():
        if val > 1: return False
    return True

def filledUp(grid):
    for row in grid:
        if row.count(0) > 0:
            return False
    return True

def pretty_print(grid):
    for row in grid:
        print(row)
    print()

def fillGrid(grid):
    global n
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 0:
                for k in range(1, 10):
                    g_cp = deepcopy(grid)
                    g_cp[i][j] = k
                    if validGrid(g_cp):
                        if filledUp(g_cp):
                            n += 1
                            print(f"solution {n}:")
                            pretty_print(g_cp)
                        fillGrid(g_cp)
                return

print("Grid to solve:")
pretty_print(grid)
fillGrid(grid)
print(f"Found {n} solutions in {round(time()- start, 2)}s.".format(n=n))