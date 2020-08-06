#project euler problem 20: find the sum of the digits of the number 100!
def factorial(n):
    nn, factorial_sum = n, 0
    for i in range(1,n-1):
      nn += nn * i
    nn_p = str(nn)
    for j in range(0, len(nn_p)):
        factorial_sum += int(nn_p[j])
    print(factorial_sum)

factorial(100)