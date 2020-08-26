#A simple as py python script for checking if the items in an array are permutated

a = [0,5,2,1,8]
a_ = [0,1,2,5, 7]

def is_permutated(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in arr1:
        if i  not in arr2:
            return False

    return True

print(is_permutated(a, a_))