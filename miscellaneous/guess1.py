from tkinter import *

limit = int(input("Enter the upper limit: "))
guess, lowx, highx = 0, 0, 0

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Guessing game")
        master.geometry("300x400")
        master.resizable(width=FALSE, height=FALSE)

        self.correct = Button(master, text = "Correct", activeforeground = "cyan", background = "grey")
        self.correct.place(x = 80, y = 360, width = 55)

        self.low = Button(master, text = "Low", activeforeground = "green", background = "grey")
        self.low.place(x = 5, y = 360, width = 55)

        self.high = Button(master, text = "High", activeforeground = "red", background = "grey")
        self.high.place(x = 155, y = 360, width = 55)

    def guesz(self, *args):
        global guess, limit
        guess = limit / 2
        self.guesser = Label(self.master,text = f"You guessed {guess}")
        self.guesser.config()
    

def main():
    root = Tk()
    game = GUI(root)
    root.bind('<Return>', game.guesz)
    root.mainloop()

if __name__ == "__main__":
    main()

    