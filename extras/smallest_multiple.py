 #project euler problem 5: which is the smallest positive number that is evenly divisible by all the numbers from 1 to 20
from random import randint
def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        return gcd(n, r)

def lcm(m, n):
    lcm = m*n / gcd(m, n)
    return lcm

arr = []
for x in range(1, 21):
    arr.append(x)

def lcm_arr(arr):
    l = arr[0]
    for x in range(1, len(arr)):
        l = lcm(l, arr[x])
    return l

def gcd_arr(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    return g

print(f"The LCM is:{lcm_arr(arr)}")