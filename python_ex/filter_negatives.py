# a simple python script to filter out the negatives in an array
a = [i for i in range(-5, 5)]

def filter(a):
    for i in a:
        if i > 0:
            print(i)

print(filter(a))