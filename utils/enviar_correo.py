from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTP
from os import environ, getcwd, path

def enviar_correo(destinatario, titulo, cuerpo):
    cuerpo_html = '  '
    mensaje= MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    password_email_emisor = 'wvfihqhlbylrghjq' # environ.get('PASSWORD_SENDER')
    # print(environ.get('PASSWORD_SENDER') is None)

    mensaje['Subject'] = titulo

    mensaje.attach(MIMEText(cuerpo))

    mensaje.attach(MIMEText(cuerpo_html, 'html'))

    #                   SERVIDOR      | PUERTO
    # outlook > outlook.office365.com | 587
    # hotmail > smtp.live.com         | 587
    # gmail >   smtp.gmail.com        | 587
    # icloud >  smtp.mail.me.com      | 587
    # yahoo >   smtp.mail.yahoo.com   | 587

    emisor = SMTP('smtp.gmail.com', 587)

    emisor.starttls()

    emisor.login(user= email_emisor, password= password_email_emisor)
    emisor.sendmail(from_addr=email_emisor, to_addrs=destinatario, msg=mensaje.as_string())

    # cerrar la conexion con mi servidor de correos

    emisor.quit()


def enviar_correo_adjuntos(destinatarios, titulo):
    
    cuerpo = 'Por favor revisa adjuntos'
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    pasword_email_emisor = 'wvfihqhlbylrghjq'

    mensaje['subject'] = titulo

    mensaje.attach(MIMEText(cuerpo))
    ruta= getcwd()
            
    ruta_definitiva = path.join(ruta, 'utils', 'lapiceros.jpg')
    # print(getcwd())
    
    with open(ruta_definitiva, 'rb') as archivo:
          print(archivo)
          archivo = MIMEApplication(archivo.read(), Name='lapiceros.jpg')

    archivo['Content-Disposition'] = 'attachment; filename="lapiceros.jpg"';
    mensaje.attach(archivo)      

    emisor = SMTP('smtp.gmail.com', 587)

    emisor.starttls()

    emisor.login(user= email_emisor, password= pasword_email_emisor)
    
    emisor.sendmail(from_addr=email_emisor, to_addrs=destinatarios, msg=mensaje.as_string()) 

    emisor.quit()