from random import randint
#a = input("Enter a number:")
a = str(randint(1,9999999999999999999999999999))
print(a)
for i in range(10):
    print(f"Number of {i}s :{a.count(str(i))}")