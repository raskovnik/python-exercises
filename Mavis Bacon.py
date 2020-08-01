from tkinter import *
import time
from random import choice
import keyboard

file = open("lorem_ipsum.txt")
sentences = file.read().splitlines()
file.close()
root = Tk()
root.geometry("1000x500")
root.title("Mavis Bacon_typing speed test")
typing = Entry(root,bg = "grey", bd = 5, width = 450)
typing.pack()
typing.focus()
reset = Button(root, bg = "red", height = 1, width = 3, text = "Reset", command = lambda: typing.delete(0, "end"))
snt = choice(sentences)
sentence = Label(root, bg = "grey", bd = 5, text = snt)
sentence.config()
sentence.pack()
reset.pack()
start = time.time()
a = 0
inp, comp = [], []
global z
global percent
def keys_pressed(typing):
    global percent, a, stop, ttk
    stop = time.time()
    ttk = stop-start
    results()
    for i in snt:
        comp.append(i)
    for j in omy:
        inp.append(j)
    for l in range(len(comp)):
        if inp[l] == comp[l]:
            a += 1
    print(inp)
    print(ttk)
    print(a)
    percent = a/len(comp) * 100
    z = a
    print(percent)
root.resizable(False, False)
def get_accuracy():
   pass
typing.bind("<Return>", keys_pressed)
def results():
    global omy
    omy = typing.get()
    t = Label(root, bg = "green", height = 1, width = 15, text = f"Time:{round(ttk,2)}s")
    accuracy = Label(root, bg = "cyan", height = 1, width = 10, text = "Accuracy:")
    wpm = Label(root, bg = "blue", height = 1, width = 5, text = "WPM")
    t.pack()
    accuracy.pack()
    wpm.pack()

root.mainloop()
