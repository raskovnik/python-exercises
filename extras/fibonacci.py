from random import randint
a = randint(0, randint(0,100))
print(f"Fibonacci for {a}")
n_1, n_2, fib, count = 0, 1, [1], 0
while count < a:
    fib.append(n_1 + n_2)
    n_1 += 1
    n_2 += 1
    count += 1

print(fib)