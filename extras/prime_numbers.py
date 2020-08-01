from random import randint
from math import sqrt

a = randint(1,100)
print(f"prime numbers between 1 and {a}:\n")
def is_prime(n):
    for z in range(2, int(sqrt(n)) +1):
        if n % z == 0:
            return False
    return True

for x in range(2, a+1):
    if is_prime(x):
        print(x)