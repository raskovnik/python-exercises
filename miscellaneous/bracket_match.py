from random import randint, shuffle

brackets, l, r = [], randint(1,10), randint(1,10)
s = '(' * l + ")" * r
for b in s:
    brackets.append(b)
shuffle(brackets)

stack1, stack2 = [], []

for i in brackets:
    if i == "(" :
        stack1.append(i)
    else:
        stack2.append(i)

if len(stack1) == len(stack2):
    print("All the brackets matched")
else:
    print("All the brackets did not match")