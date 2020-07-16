import socket
s = socket.socket()
s.bind(('', 1676))
s.listen(4)
print("Waiting for connection...")
while True:
    conn, addr = s.accept()
    print(f"{addr} has connected to the server")
    message= conn.recv(1024).decode()
    conn.sendall(message.encode())
    s.close()
