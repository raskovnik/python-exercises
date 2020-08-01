import asyncore
import socket
import logging

class Server(asyncore.dispatcher):
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.logger = logging.getLogger("server")
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(address)
        self.address = self.socket.getsockname()
        self.logger.debug("Binding to %s:", self.address)
        self.clients = []
        self.listen(5)

    def handle_accept(self):
        # return super().handle_accept()
        client_info = self.accept()
        if client_info is not None:
            self.logger.debug("handle_accept() => %s", client_info[1])
            self.clients.append(ClientHandler(client_info[0], client_info[1], self))

    def flood(self, client_src, msg):
        for client in self.clients:
            if client != client_src:
                sent = client.send(msg)
                self.logger.debug("handle_write() => (%d) %s",sent, msg[:sent].rstrip())
            

class ClientHandler(asyncore.dispatcher):
    def __init__(self, sock, address, server):
        #super().__init__(sock, map)
        self.server = server
        asyncore.dispatcher.__init__(self, sock)
        self.logger = logging.getLogger("Client " + str(address))
        self.data_to_write = []

    def writable(self):
        return bool(self.data_to_write)

    def handle_write(self):
        #return super().handle_write()
        data = self.data_to_write.pop()
        self.server.flood(self, data[:1024])

    def handle_read(self):
        data = self.recv(1024)
        self.logger.debug("handle_read() => (%d) %s", len(data), data.rstrip())
        self.data_to_write.insert(0, data)
    
    def handle_close(self):
        #return super().handle_accepted(sock, addr)
        self.logger.debug("handle_close()")
        self.close()

def main():
    logging.basicConfig(level=logging.DEBUG, format = "%(name)s:[%(levelname)s]:%(message)s")
    HOST = "0.0.0.0"
    PORT = 1778
    s = Server((HOST, PORT))
    asyncore.loop()

if __name__ == "__main__":
    main()