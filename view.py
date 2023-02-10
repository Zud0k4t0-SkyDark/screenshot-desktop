import socket
from pynput import mouse,keyboard
import subprocess
import threading
import signal, sys
from rich import print

def def_handler(sig, frame):
    print ("\n Saliendo del Programa....")
    sys.exit(1)
signal.signal(signal.SIGINT, def_handler)


# Proceso Aparte Corriendo en un Hilo

def image():
    data = subprocess.run("powershell [void][reflection.assembly]::loadwithpartialname('system.windows.forms'); $MyScreenshot = [System.Windows.Forms.SystemInformation]::VirtualScreen; $WID = $MyScreenshot.Width; $HEI = $MyScreenshot.Height; $LEFT = $MyScreenshot.Left; $TOP = $MyScreenshot.Top; $MyBitmap = New-Object System.Drawing.Bitmap $WID, $HEI ;$MyDrawing = [System.Drawing.Graphics]::FromImage($MyBitmap); $MyDrawing.CopyFromScreen($LEFT, $TOP, 0, 0, $MyBitmap.Size); $MyFile = $env:TMP+'\{}.png' ; $MyBitmap.Save($MyFile) ".format("caca"))

def key_press(key):
    if key == keyboard.Key.ctrl_l:
        image()
def listen_keyboard():
    with keyboard.Listener(on_press=key_press) as listener:
        listener.join()
tarea = threading.Thread(target=listen_keyboard, name="listen_keyboard")
tarea.start()

host = "127.0.0.1"

# Servidor
print ("[red]######################[/red][yellow]~~[/yellow]Inciado el Servidor[yellow]~~[/yellow][green]@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[/green]")
print ('''[cyan]
                            _ ___                /^^\ /^\  /^^\_
            _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
        _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
        / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
        ( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
        ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
        _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
        < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
        \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
        `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
[/cyan]''')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, 4444))
        s.listen(3)
        conexion, addr = s.accept()
        conexion.sendall(b'################~~~Conectado con El Servidor~~~##################')
        print ("\n[red][!][/red][yellow]Conexion Realizada con el Cliente[/yellow]\n\n")
        while True:
            #data = input("~# ")
            #conexion.send(data.encode("utf-8"))
            data_client = conexion.recv(1024).decode("utf-8")
            if  data_client == "menu" or data_client == "m":
                conexion.send(b'''
                            ################ MENU @@@@@@@@@@@@@@@
                            1) Sacar Captura del Ordenador
                            2) Enviar Data (Posicion del Mouse)
                            3) Cerrar la Script
                ''')
            elif data_client == "exit" or   data_client == "x":
                sys.exit(1)
            elif data_client == "1":
                conexion.send(b"Menu about Image:")
                imagen_name = conexion.recv(1024).decode("utf-8")
                data = subprocess.run("powershell [void][reflection.assembly]::loadwithpartialname('system.windows.forms'); $MyScreenshot = [System.Windows.Forms.SystemInformation]::VirtualScreen; $WID = $MyScreenshot.Width; $HEI = $MyScreenshot.Height; $LEFT = $MyScreenshot.Left; $TOP = $MyScreenshot.Top; $MyBitmap = New-Object System.Drawing.Bitmap $WID, $HEI ;$MyDrawing = [System.Drawing.Graphics]::FromImage($MyBitmap); $MyDrawing.CopyFromScreen($LEFT, $TOP, 0, 0, $MyBitmap.Size); $MyFile = $env:TMP+'\{}.png' ; $MyBitmap.Save($MyFile) ".format(imagen_name))
                conexion.send(b"Captura Sacada...")
                data_client = " "

            elif data_client == "2":
                conexion.send(b'''
                            ######################################
                            Tenes las posiciones a,b,c,d
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                ''')
            elif data_client == "3" or data_client == "close" or data_client == "exit":
                conexion.send(b'''
                            Cerrando Script
                ''')
                sys.exit(1)

