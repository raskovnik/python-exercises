from tkinter import *
high = int(input("Enter maximum limit: "))
low, tries = 0, 0

while True:
    guess = int((low + high) / 2)
    correct = input(f"You guessed {guess}..(t/l/h): ").lower()
    tries += 1
    if correct == "l":
        low = guess + 1
    elif correct == "h":
        high = guess
    else:
        print(f"You guessed {guess} and I got it in {tries} tries!!")
        break
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Guess Game")
        master.geometry("300x400")
        master.resizable(width=FALSE, height=FALSE)

        self.correct = Button(master, text = "True")
        self.correct.pack()

        self.low = Button(master, text = "Low")

root = Tk()
game = GUI(root)
root.mainloop()
