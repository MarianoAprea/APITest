import smtplib
from email.mime.text import MIMEText

# Configuración del correo electrónico
remitente = "apreamariano@gmail.com"
destinatario = "marianoaprea@hotmail.com"
asunto = "Asunto del correo desde PYTHON"
cuerpo = "Este es el cuerpo del correo electrónico , envio desde python"

# Crea el mensaje
mensaje = MIMEText(cuerpo)
mensaje['Subject'] = asunto
mensaje['From'] = remitente
mensaje['To'] = destinatario

# Configura el servidor SMTP
servidor_smtp = "smtp.gmail.com"
puerto_smtp = 587  # O 465 para conexiones SSL
usuario_smtp = "apreamariano@gmail.com"
contrasena_smtp = ""

try:
    # Inicia la conexión SMTP
    with smtplib.SMTP(servidor_smtp, puerto_smtp) as server:
        server.starttls()  # Opcional, si el servidor requiere TLS
        server.login(usuario_smtp, contrasena_smtp)
        server.sendmail(remitente, destinatario, mensaje.as_string())
        print("Correo electrónico enviado con éxito.")

except Exception as e:
    print(f"Error al enviar el correo electrónico: {e}")

    