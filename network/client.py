import socket


class GameClient:
    
    def connect(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall('Hello, world')
        data = s.recv(1024)
        s.close()
        print 'Received', repr(data)
        
        
if __name__ == "__main__":
    
    test = GameClient();
    test.connect("localhost", 32000);