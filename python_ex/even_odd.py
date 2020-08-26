# a python script to sort items in an array... even then odd

a, ev, odd = [i for i in range(10)], [], []

def even(num):
    if num % 2 == 0:
        return True
    return False

def special_sort(arr):
    for i in arr:
        if even(i):
            ev.append(i)
        else:
            odd.append(i)
special_sort(a)    
a = ev + odd
print(a)