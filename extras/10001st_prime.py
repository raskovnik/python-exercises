#project euler problem 7:what is the 10001st prime number?
from math import sqrt

print(f"The 10001st prime number:")
def is_prime(n):
    for z in range(2, int(sqrt(n)) +1):
        if n % z == 0:
            return False
    return True
counter = 0
for x in range(1, 900000):
    if is_prime(x):
        counter += 1
    if counter == 10001:
        print(x)
        break