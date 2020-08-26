#A simple python program to chech if an array has duplicates

a = [2,6,2,5,0,1,2,3]
a_ = [i for i in range(10)]
def has_duplicates(arr):
    for i in arr:
        if arr.count(i) > 1:
            return True
    return False
    
print(has_duplicates(a))