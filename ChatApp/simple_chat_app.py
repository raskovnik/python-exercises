import socket
import threading
from time import sleep
from tkinter import *

s = socket.socket()
s.connect(("0.0.0.0", 1778))

username = input("Enter username: ")
username += ":"

class GUI:
    def __init__(self, master):
        self.master = master
        master.geometry("317x450")
        master.resizable(width = False, height = False)
        master.title("Simple Chatapp")

        self.ChatBox = Text(master, bd = 0, bg = "grey", font = "Arial")
        self.ChatBox.config()
        self.ChatBox.place(x=6,y=6, width=300, height=400)

        self.scrollbar = Scrollbar(master, command = self.ChatBox.yview, cursor = "arrow")
        self.ChatBox["yscrollcommand"] = self.scrollbar.set
        self.scrollbar.place(x=307,y=6, width = 7,  height=386)

        self.Send = Button(master, font = ("Verdana",12,"bold"), text = "send", width = "7", height = 3, bd = 0,
                            bg = "green", activebackground = "#3c9d9b", fg = '#000000', command = self.send)
        self.Send.place(x=6, y=407, height=30)

        self.entext = Entry(master, bd = 0, bg = "grey", font = "Arial")
        self.entext.place(x=128, y=407, height=30, width=175)
        self.entext.focus()

        threading.Thread(target=self.receive_listen, args=(s, )).start()

    def send(self):
        msg = self.entext.get().strip()
        self.entext.delete(0,END)

        if msg != '':
            self.ChatBox.config(state=NORMAL)
            self.ChatBox.tag_configure("tag", justify = "right")
            self.ChatBox.insert(END,"You: " + msg + '\n', "tag")
            self.ChatBox.config(foreground="blue", font=("Verdana", 12 ))
            sms = username + msg
            s.send(sms.encode())

    def receive_listen(self, sock):
        while True:
            sleep(5)
            text = s.recv(1024).decode()
            if text:
                self.ChatBox.insert(END, text + "\n")  
                self.ChatBox.yview(END)

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
 