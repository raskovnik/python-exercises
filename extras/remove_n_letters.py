from random import randint, shuffle
alphabet = list("abcdefghijklmnopqrstuvwxyz")
ax = []
for _ in range(randint(1,20)): #choose a random number for the length of our characters
    shuffle(alphabet)
    ax.append(alphabet[randint(0,25)]) #appends a random character alphabet[i] from our shuffled list for a random number of times, i

n = randint(0, len(ax)) #number of digits to remove
removed = 0 #Number of removed digits
print(f"Remove {n} letters!!")
while removed != n:
    pop_index = randint(0, len(ax)-1) # choose a random index then pop our letter
    print(f"Pop letter at index {pop_index}")
    ax.pop(pop_index)
    removed += 1
    print(ax)

