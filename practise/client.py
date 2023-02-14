import socket

class conexion_server():
    def __init__(self, ip="192.168.120.82", port=4444):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self):
        while True:
            try:
                self.socket.connect((self.ip, self.port))
                while True:
                    try:
                        data = input("==> ")
                        if data == "exit":
                            self.socket.close()
                        self.socket.send(data.encode("utf-8"))
                    except:
                        pass
            except:
                pass
    
c = conexion_server()
c.connect()