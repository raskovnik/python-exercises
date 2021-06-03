from tkinter import *
guess = 0
# high = int(input("Enter maximum limit: "))
# low, tries = 0, 0

#typing.bind("<Return>", keys_pressed)

# while True:
#     guess = int((low + high) / 2)
#     correct = input(f"You guessed {guess}..(t/l/h): ").lower()
#     tries += 1
#     if correct == "l":
#         low = guess + 1
#     elif correct == "h":
#         high = guess
#     else:
#         print(f"You guessed {guess} and I got it in {tries} tries!!")
#         break
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Guess Game")
        master.geometry("300x400")
        master.resizable(width=FALSE, height=FALSE)

        self.correct = Button(master, text = "Correct", activeforeground = "cyan", background = "grey")
        self.correct.place(x = 80, y = 360, width = 55)

        self.low = Button(master, text = "Low", activeforeground = "green", background = "grey", command = self.lowx() )
        self.low.place(x = 5, y = 360, width = 55)

        self.high = Button(master, text = "High", activeforeground = "red", background = "grey")
        self.high.place(x = 155, y = 360, width = 55)
        
        self.limit = Label(master, text = "Enter the maximum limit: ")
        self.limit.place(x = 5, y = 5)

        self.enter = Entry(master, bd = 2, background = "grey", width = 7)
        self.enter.place(x = 175, y = 5)
        self.enter.focus()
       

    def guessable(self):
        global guess
        high_ = int(self.enter.get())
        low_, tries = 0, 0
        guess = int((low_ + high_) / 2)
        while True:
            #correct = input(f"You guessed {guess}..(t/l/h): ").lower()
            self.guesser = Label(self.master,text = f"You guessed {guess}")
            self.guesser.config()
            y_axis = 25
            self.guesser.place(x = 5, y = y_axis)
            tries += 1
            y_axis += 25

            # if self.low == "l":
            #     low = guess + 1
            # elif correct == "h":
            #     high = guess
            # else:
            #     print(f"You guessed {guess} and I got it in {tries} tries!!")
            #     break

    def lowx(self):
        low_ = guess + 1


    def get_limit(self, *args):
        self.guessable()
        print(high)

def main():
    root = Tk()
    game = GUI(root)
    root.bind('<Return>', game.get_limit)
    root.mainloop()

if __name__ == "__main__":
    main()

