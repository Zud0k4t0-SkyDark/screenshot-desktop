import socket
from pynput import mouse,keyboard
import pyautogui
import subprocess
import threading
import options
import signal, time
import sys
from rich import print
from comand import ngrok_send_Telegram

# Start Process ngrok
run = subprocess.run("powershell Start-Process $env:tmp\/ngrok 'tcp 4444' -WindowStyle Hidden")
time.sleep(4)
# Send Telegram ip and port
response = ngrok_send_Telegram()
print (response)

#Get-Process | Select-Object Id,ProcessName | findstr Taskmgr
def def_handler(sig, frame):
    print("[red][!][/red]  [yellow italic]Saliendo....[/yellow italic]\n\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

option = options

# Proceso Aparte Corriendo en un Hilo

def image():
    path_image = option.capture_image("screenshot_desktop")
    option.send_image(path_image)
    #remove_image = subprocess.run("powershell rm -Path {} -Force".format(path_image), shell=True)

def key_press(key):
    if key == keyboard.Key.ctrl_l:
        image()

def listen_keyboard():
    with keyboard.Listener(on_press=key_press) as listener:
        listener.join()
tarea = threading.Thread(target=listen_keyboard, name="listen_keyboard")
tarea.start()

host = "127.0.0.1"

# Mouse Option

def mouse_move(letter_option):
    if letter_option == "a":
        pyautogui.moveTo(294, 220)
    elif letter_option == "b":
        pyautogui.moveTo(1501, 220)
    elif letter_option == "c":
        pyautogui.moveTo(283, 814)
    elif letter_option == "d":
        pyautogui.moveTo(1539, 766)

#294 220		1501 220
#283 814		1539 766

# Servidor
#print ("[red]######################[/red][yellow]~~[/yellow]Inciado el Servidor[yellow]~~[/yellow][green]@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[/green]")
#print ('''[cyan]
#                            _ ___                /^^\ /^\  /^^\_
#            _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
#        _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
#        / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
#        ( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
#        ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
#        _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
#        < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
#        \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
#        `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
#[/cyan]''')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, 4444))
        s.listen(3)
        conexion, addr = s.accept()
        conexion.sendall(b'###~~~Connect to Server~~~###')
        print ("\n[red][!][/red][yellow]Conexion Realizada con el Cliente[/yellow]\n\n")
        while True:
            #data = input("~# ")
            #conexion.send(data.encode("utf-8"))

            data_client = conexion.recv(1024).decode("utf-8")
            if data_client == "1":
                data = conexion.recv(1024).decode("utf-8")
                print(data)
                if data == "ihere":
                    conexion.send(b'ihere')
                    pass
                elif data == "continue":
                    image_name = conexion.recv(1024).decode("utf-8")
                    print (image_name)
                    email = conexion.recv(1024).decode("utf-8")
                    print (email)
                    print ("Data Recived:\n==> {}\n==> {}".format(image_name, email))
                    path_image = option.capture_image(image_name)
                    option.send_image(path_image, email)
                    remove_image = subprocess.run("powershell rm -Path {} -Force".format(path_image), shell=True)
                    conexion.send(b"Captura Sacada...check email... :)")
                    # Finish code

            elif data_client == "2":
                letter_option = conexion.recv(1024).decode("utf-8")
                mouse_move(letter_option)
            elif data_client == "exit" or   data_client == "x" or data_client == "3" or data_client == "close":
                
                break
            elif data_client == "ihere":
                    conexion.send(b'ihere')


