#project euler problem 48
def powers(a):
    pwr_sum = 0
    for i in range(1, a+1):
        pwr_sum += i**i
    pwr_ = str(pwr_sum)
    print(pwr_[-10:])

powers(1000)