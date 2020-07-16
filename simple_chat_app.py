import socket
from tkinter import *
s = socket.socket()
s.connect(("127.0.0.1", 1676))
username = "Anon:"
def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END,"You: " + msg + '\n')
        ChatBox.config(foreground="blue", font=("Verdana", 12 ))
        sms = username + msg
        s.send(sms.encode())
        text = s.recv(1024).decode()
        ChatBox.insert(END, text + "\n")  
        ChatBox.config(state=DISABLED)
        ChatBox.yview(END)
 

root = Tk()
root.title("Simple ChatApp")
root.geometry("300x450")
root.resizable(width=FALSE, height=FALSE)

ChatBox = Text(root, bd=0, bg="grey", height="8", width="50", font="Arial",)

ChatBox.config(state=DISABLED)

scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="arrow")
ChatBox['yscrollcommand'] = scrollbar.set

SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="7", height=3,
                    bd=0, bg="green", activebackground="#3c9d9b",fg='#000000',
                    command= send )

EntryBox = Text(root, bd=0, bg="grey",width="29", height="5", font="Arial")

scrollbar.place(x=290,y=6, height=386)
ChatBox.place(x=6,y=6, width=300, height=400)
EntryBox.place(x=128, y=407, height=30, width=175)
SendButton.place(x=6, y=407, height=30)

root.mainloop()
