#Modulos que usamos para el envío para de Imagenes.

#MIMEImage ==> from email.MIMEImage import MIMEImage
#msg = MIMEMultipart() ==> from email.MIMEMultipart import MIMEMultipart

import ssl, smtplib
import mimetypes
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEImage import MIMEImage
from email.mime.image import MIMEImage
import subprocess


path = subprocess.run("powershell $env:tmp", stdout=subprocess.PIPE, universal_newlines=True, shell=True)
path = path.stdout
path_image = path.strip()+"\otra.png"
print (path_image)

def send_email(path_image):
    #message = "<br>Hola ,<br><br> Se ha detectado una alerta de seguridad <br><br> "
    #em = MIMEText(message, "html", _charset = "uft-8")
    em = EmailMessage()
    context = ssl.create_default_context()

    # Send Email

    em['From'] = 'caca@gmailcom'
    em['To'] = 'juanmapipa4@gmail.com'
    em['Subject'] = 'Capture Image'


    em.set_content("Capture Image:")

    # Adjuntamos Imagen
    file = open(path_image, "rb")
    attach_image = MIMEImage(file.read())
    #attach_image.add_header('Content-Disposition', 'attachment; filename = "Alarma"')
    em.add_attachment(attach_image)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login('monolocacapop', 'ngkdwjlpolfrzyop')
        smtp.sendmail('monolocacapop', 'juanmapipa4@gmail.com', em.as_string())
    #...
    #(235, b'2.7.0 Accepted')
    #{}
send_email(path_image)