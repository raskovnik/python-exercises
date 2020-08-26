# A simple python script to determine if the number of even numbers is equal to the  number of odd numbers

def is_even(num):
    if num % 2 == 0:
        return True
    return False

a, even, odd = [i for i in range(10)], 0, 0

for i in a:
    if is_even(i):
        even += 1

    else:
        odd += 1

if odd == even:
    print(f"array {a} has a balanced no of evens and odds!")
else:
    print(f"array {a} doesn't have a balanced no of evens and odds!")