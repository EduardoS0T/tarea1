import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración
correo_emisor = 'soteloeliasg@gmail.com'
password = ' #### '
correo_destinatario = 'angel.brito@fi.unam.edu'

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = correo_emisor
mensaje['To'] = correo_destinatario
mensaje['Subject'] = 'Correo de prueba desde Python'

# Cuerpo del mensaje
cuerpo = 'Hola, este es un correo de prueba enviado mediante Python usando SMTP desde Gmail.'
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Conexión al servidor SMTP de Gmail
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()  # Iniciar conexión segura
    servidor.login(correo_emisor, password)
    texto_del_mensaje = mensaje.as_string()

    # Enviar correo
    servidor.sendmail(correo_emisor, correo_destinatario, texto_del_mensaje)
    print('Correo enviado exitosamente.')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    servidor.quit()
