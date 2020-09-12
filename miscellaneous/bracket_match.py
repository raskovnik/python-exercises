from random import randint, shuffle

stack, l, r = [], randint(1,10), randint(1,10)
brackets = list("("*l + ")"*r)
shuffle(brackets)
print(brackets)
print(l,r)
for i in brackets:
    if i == "(":
        stack.append(i)
    else:
        try:
            stack.pop()
        except IndexError:
            print(stack)
            print("All the brackets did not match")
            break
else:
    if len(stack) > 0:
        print("All the brackets did not match")
    else:
        print("Matched")