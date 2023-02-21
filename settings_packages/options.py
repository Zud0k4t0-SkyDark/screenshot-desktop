# Aqui estara la tralla por una parte el screenshot  y por otra el envío del correo.
# Enviar el correo de la otra forma para que haya mas seguridad en el envío de este.
import smtplib, pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import subprocess
from datetime import datetime

# Ruta del path
path = subprocess.run("powershell $env:tmp", stdout=subprocess.PIPE, universal_newlines=True, shell=True)
path = path.stdout
# Estanciamos los objetos a usarem = EmailMessage()

msg = MIMEMultipart()


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

# Code HTML SEND

html = """
<!DOCTYPE html>
<html>
<head>
	<title>Simple Email</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			background-color: #f4f4f4;
		}
		.container {
			max-width: 600px;
			margin: 0 auto;
			padding: 20px;
			background-color: #fff;
			border-radius: 5px;
			box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
		}
		h1 {
			font-size: 28px;
			color: #333;
			margin-top: 0;
		}
		p {
			font-size: 18px;
			line-height: 1.5;
			color: #666;
		}
		.button {
			display: inline-block;
			padding: 10px 20px;
			background-color: #009688;
			color: #fff;
			border-radius: 5px;
			text-decoration: none;
			margin-top: 20px;
		}
		.button:hover {
			background-color: #00796b;
		}
        a {
        text-decoration: none;
        }
        strong {
        text-color: black;
        }
	</style>
</head>
<body>
	<div class="container">
		<h1>¡Take your Image!</h1>
		<p>Buena Image 🤑👍</p>
		<p>Email send by <strong>Zud0k4t0</strong></p>
		<ul>
            <li><strong>Correo electrónico:</strong></br> 
            <a href="mailto:juanmapipa4@gmail.com">juanmapipa4@gmail.com</a></li>
            <li><strong>Whatsapp</strong>
            <a href="wa.me//14094024271"></br>
            Send Message </a>
            </li>
            <li><strong>Teléfono:</strong></br>
            +1 (409) 402-4271</li>
		</ul>
		<p>¡Gracias por tu espera!</p>
        <img src="cid:image1" width="500px">
		<a href="https://github.com/Zud0k4t0-SkyDark/screenshot-desktop/" class="button">Ir al Proyecto</a>
	</div>
</body>
</html>
"""

#msg_text = MIMEText(html, 'html')
#msg.attach(msg_text)

def send_image(path_image, email="juanmapipa4@gmail.com", name_image="patata.jpg"):

    print ("Path image ==> ",path_image)
    print ("El correo va para => {}".format(email))


    with open(path_image, 'rb') as f:
        img_data = f.read()

    # Para poder poner un nombre a la imagen
    #img = MIMEImage(img_data, name="hola.jpg")
    img = MIMEImage(img_data, name="imagen.jpg")
 #   img.add_header('Content-ID', '<image1>')
    msg.attach(img)

    msg['Subject'] = 'Capture Image'
    msg['From'] = 'monolopepe5@gmail.com'
    msg['To'] = email
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('monolopepe5@gmail.com', 'rqkvlzrtfbvdcgsu')
    smtp.sendmail('monolopepe5@gmail.com', email, msg.as_string())
    smtp.quit()

