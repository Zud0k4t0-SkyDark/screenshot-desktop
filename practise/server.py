import socket
import threading

class conexion():
    def __init__(self,ip="127.0.0.1", port=4444):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.listen(10)
        self.socket.setblocking(False)
        self.clientes = []
        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)

        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()


    def aceptarCon(self):
        while True:
            try:
                conexion, add = self.socket.accept()
                conexion.setblocking(False)
                self.clientes.append(conexion)
            except Exception as e:
                print("Error en aceptarCon:", e)

    def procesarCon(self):
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024).decode('utf-8')
                        if data:
                            print(data)
                    except Exception as e:
                        print("Error en procesarCon:", e)


c = conexion()

