#project euler problem 10: find the sum of all primes below two million
from time import time
from math import sqrt

a, primesum = 2000000, 0
print("calculating...")
t = time()
def is_prime(n):
    for z in range(2, int(sqrt(n)) +1):
        if n % z == 0:
            return False
    return True

for x in range(2, a+1):
    if is_prime(x):
        primesum += x
print(f"Sum of prime numbers between 1 and {a}: {primesum}")
print(f"Time taken: {time()- t}")