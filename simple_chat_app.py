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
        master.geometry("300x450")
        master.resizable(width = False, height = False)
        master.title("Simple Chatapp")

        self.ChatBox = Text(master, bd = 0, bg = "grey", height = "8", width = "50", font = "Arial")
        self.ChatBox.config()
        self.ChatBox.place(x=6,y=6, width=300, height=400)

        self.scrollbar = Scrollbar(master, command = self.ChatBox.yview, cursor = "arrow")
        self.ChatBox["yscrollcommand"] = self.scrollbar.set
        self.scrollbar.place(x=290,y=6, height=386)

        self.Send = Button(master, font = ("Verdana",12,"bold"), text = "send", width = "7", height = 3, bd = 0,
                            bg = "green", activebackground = "#3c9d9b", fg = '#000000', command = self.send)
        self.Send.place(x=6, y=407, height=30)

        self.entext = Entry(master, bd = 0, bg = "grey", font = "Arial")
        self.entext.place(x=128, y=407, height=30, width=175)

    def send(self):
        msg = self.entext.get("1.0",'end-1c').strip()
        self.entext.delete("0.0",END)

        if msg != '':
            self.ChatBox.config(state=NORMAL)
            self.ChatBox.insert(END,"You: " + msg + '\n')
            self.ChatBox.config(foreground="blue", font=("Verdana", 12 ))
            sms = username + msg
            s.send(sms.encode())

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()

def receive_listen(sock):
    while True:
        sleep(5)
        text = s.recv(1024).decode()
        if text:
            GUI.ChatBox.insert(END, text + "\n")  
            GUI.ChatBox.yview(END)

threading.Thread(target=receive_listen, args=(s, )).start()

if __name__ == "__main__":
    main()
 