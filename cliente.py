import socket, time
import signal, sys, subprocess
from rich import print

def def_handler(sig, frame):
    print ("\n\n Saliendo....\n\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
def clear_screen():
    try :
        # Windows
        clear = subprocess.run("powershell clear")
    except:
        # Linux
        clear = subprocess.run("clear")
clear_screen()

ip =  input("IP\n==> ")
if "tcp://" in ip or "http://" in ip:
    ip = ip.split("//")[1]
port = int(input("Port\n==> "))
#ip = "8.tcp.ngrok.io"
#port = 15279

clear_screen()    

print (f"\n[green italic]Try Connect:[/green italic]\n\n[red italic]Ip[/red italic] [yellow]==>[/yellow] [cyan]{ip}[/cyan]\n[red]Port[/red] [yellow]==>[/yellow] [cyan]{port}[/cyan]")

def ascii_string():
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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try: 
        s.connect((ip, port))
    except:
        print ("\n\n[red][[/red][yellow]![/yellow][red]][/red] [green]The Server is not ON[/green]\n\n")
        sys.exit(1)
 #   s.send(("hola server\n").encode("utf-8"))
 #   data = s.recv(1024)
 #   print ("\nMensaje del Servidor:\n\n==> {}\n".format((data.decode("utf-8")).strip()))
    d = s.recv(1024).decode("utf-8")
    clear_screen()
    print (d)
    ascii_string()
    def menu():
        print ('''\n
                    [yellow]###[/yellow] [purple italic]MENU[/purple italic] [green]@@@[/green]
                    \n
                    [red blink]1)[/red blink] [yellow italic]Capture Image[/yellow italic]
                    [red blink]2)[/red blink] [yellow italic]Send Data[/yellow italic]
                    [red blink]3)[/red blink] [yellow italic]Close Script[/yellow italic]
                    [red blink]4)[/red blink] [yellow italic]Clear Screen[/yellow italic]
                    [red blink]5)[/red blink] [yellow italic]Help[/yellow italic]
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
                clear_screen()
                print("\n[red italic][!][/red italic] [yellow italic]Hemos perdido Conexion :([/yellow italic]")
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
            ~~[green italic]Menu Capture Image: [/green italic]~~
            [blue][1][/blue] [purple italic]Image Name[/purple italic] [yellow](default={})[/yellow]
            [blue][2][/blue] [purple italic]Email[/purple italic] [yellow](default={})[/yellow]
            [blue][2][/blue] [purple italic]Asunto[/purple italic] [yellow](default={})[/yellow]
            [blue][3][/blue] [purple italic]Send[/purple italic]
            [blue][4][/blue] [purple italic]Show[/purple italic]
            [blue][5][/blue] [purple italic]Exit[/purple italic]
                '''.format(name_image, email))
            menu_image()
            while True:
                data_option = input("~(IMAGE)~# ")
                if data_option == "1":
                    # Set Image
                    set_image = input("Name Image:\n==> ")
                elif data_option == "2":
                    # Set Email
                    print ("[red][!][/red][green]Email[/green]")
                    set_email = input("\n==> ")
                elif data_option == "3":
                    clear_screen()
                    try:
                        print ("[red italic][!][/red italic] [green italic]Subject[/green italic]")
                        subject = input("\n==>")
                        s.send(b'continue')
                        s.sendall(set_image.encode("utf-8"))
                        time.sleep(2)
                        s.sendall(set_email.encode("utf-8"))
                        time.sleep(2)
                        s.sendall(subject.encode("utf-8"))
                        reponse_data = s.recv(1024).decode("utf-8")
                        print ("\n[cyan italic]{}[/cyan italic]".format(reponse_data))
                        break
                    except:
                        clear_screen()
                        print ("\n[red italic][!][/red italic] [yellow italic]Hemos perdido la Conexión[/yellow italic] [cyan italic]:([/cyan italic]")
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
                        clear_screen()
                        print ("\n[red italic][!][/red italic] [yellow italic]Hemos perdido la Conexión[/yellow italic] [cyan italic]:([/cyan italic]")
                        sys.exit(1)

                else:
                    print ("\n[red italic][!][/red italic] [yellow]Enter a number[yellow] [purple]\/0-0\/[/purple]\n")
                # Recived Status Image
                #response_Image = s.recv(1024).decode("utf-8")
                #print(response_Image)



        elif data_Send == "2":
            try_connection()
            s.send(data_Send.encode("utf-8"))
            print ('''
            [red italic]##########################[/red italic]
                [yellow italic]Options ( a,b,c,d )[/yellow italic]
            [red italic]@@@@@@@@@@@@@@@@@@@@@@@@@@[/red italic]
            \n[cyan italic]Choose option[/cyan italic]''')
            letter_option = input("\n==> ")
            s.send(letter_option.encode("utf-8"))

        elif data_Send == "close" or data_Send == "exit" or data_Send == "x" or data_Send == "3":
            try:
                s.send(data_Send.encode("utf-8"))
                sys.exit(1)
            except:
                print ("\n\n[red italic][[/red italic][yellow italic]![/yellow italic][red italic]][/red italic] [green italic]Saliendo...[/green italic]")
                sys.exit(1)
        elif data_Send == "clear" or data_Send == "cls" or data_Send == "4":
            clear_screen()
        elif data_Send == "help" or data_Send == "h" or data_Send == "5" or data_Send == "menu":
             clear_screen()
             menu()
        else:
            print ("\n[red][[/red][yellow italic]![/yellow italic][red]][/red] [cyan]No envies pelotudeces...[/cyan]\n")
            time.sleep(2)
            #print (s.getsockname())

        