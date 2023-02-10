import socket
import signal, sys, subprocess
from rich import print

def def_handler(sig, frame):
    print ("\n Saliendo....")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
clear = subprocess.run("powershell clear")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try: 
        s.connect(("127.0.0.1", 4444))
    except:
        print ("\n\n[red] [[/red][yellow]![/yellow][red]][/red] [green]El Server no esta On[/green]\n\n")
        sys.exit(1)
 #   s.send(("hola server\n").encode("utf-8"))
 #   data = s.recv(1024)
 #   print ("\nMensaje del Servidor:\n\n==> {}\n".format((data.decode("utf-8")).strip()))
    d = s.recv(1024).decode("utf-8")
    print (d)
    print ('''[red]
                    \****__              ____                                              
                |    *****\_      --/ *\-__                                          
                /_          (_    ./ ,/----'                                         
        Art by     \__         (_./  /                                                
        Zud0k4t0     \__           \___----^__                                       
                    _/   _                  \                                      
                |    _/  __/ )\"\ _____         *\                                    
                |\__/   /    ^ ^       \____      )                                   
                \___--"                    \_____ )                                  
                                                "
    [/red]''')
    print ('''
        Commands:
            menu/m
            exit
    ''')
    while True:
 #       data = s.recv(1024).decode("utf-8")
 #       if data:
 #           print (data)
        data_Send = input("~# ")

        # Option Capture Image

        if data_Send == "1":
            # Send Number
            s.send(data_Send.encode("utf-8"))
            # Recived Status Image
            status_Image = s.recv(1024).decode("utf-8")
            print (status_Image)
            # Send Name Image
            name_image = input("Name Image:\n==> ")
            s.send(name_image.encode("utf-8"))
            # Send Name Email
            email_address = input("Email\n==> ")
            s.send(email_address.encode("utf-8"))
            # Recived Status Image
            response_Image = s.recv(1024).decode("utf-8")
            print(response_Image)



        elif data_Send == "2":
            s.send(data_Send.encode("utf-8"))
            response_Data = s.recv(1024).decode("utf-8")
            print (response_Data)

        elif data_Send == "close" or data_Send == "exit" or data_Send == "x" or data_Send == "3":
            s.send(data_Send.encode("utf-8"))
            message_server_Close = s.recv(1024).decode("utf-8")
            print (message_server_Close)
            sys.exit(1)

        s.send(data_Send.encode("utf-8"))
        data_Recivied = s.recv(1024).decode("utf-8")
        
        if data_Recivied:
            print (data_Recivied)

        