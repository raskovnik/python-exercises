a = [2,6,2,5,0,1,2,3]
a_ = []
def reverse(a):
    for i in range(len(a)):
        a_.append(a[len(a) - 1 - i])

    return a_

print(a)
print(reverse(a))