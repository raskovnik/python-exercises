import socket
s = socket.socket()
s.bind(('', 1234))
s.listen(4)
conn, addr = s.accept()