import os
import sys
import socket
import smtplib
sock_name = socket.gethostname()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
Fromadd = "mail_expediteur "
Toadd = "mail_destinataire"
message = MIMEMultipart()
message['From'] = Fromadd
message['To'] = Toadd
message['Subject'] = sock_name + " : " + socket.gethostbyname(sock_name) +  " ,  reboot"
msg = "Le serveur " + sock_name + " ( " + socket.gethostbyname(sock_name) + " ) " + " vient de redemarrer avec succes"
message.attach(MIMEText (msg.encode('utf-8'), 'plain', 'utf-8'))
serveur = smtplib.SMTP('smtp.gmail.com', 587)
serveur.starttls()
password = "secret_passwd"
serveur.login(Fromadd, password)
texte = message.as_string().encode('utf-8')
Toadds = [Toadd]
serveur.sendmail(Fromadd, Toadds, texte)
serveur.quit()

