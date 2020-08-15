#project euler problem 1: Find the sum of all the multiples of 3 and 5 below 1000
mlpl_s = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        mlpl_s += i

print(mlpl_s)