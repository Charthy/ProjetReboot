import sys, platform
import socket
import smtplib
sock_name = socket.gethostname()

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

Fromadd = "yarez.leroy@gmail.com "
Toadd = "yarez@outlook.com"
message = MIMEMultipart()
message['From'] = Fromadd
message['To'] = Toadd
message['Subject'] = sock_name + " , reboot"
msg = "Le serveur " + sock_name + " va rebooter"
message.attach(MIMEText (msg.encode('utf-8'), 'plain', 'utf-8'))

serveur = smtplib.SMTP('smtp.gmail.com:587')
serveur.starttls()
password = "Nathan0208*Raphael"
serveur.login(Fromadd, password)
texte = message.as_string().encode('utf-8')
Toadds = [Toadd]
serveur.sendmail(Fromadd, Toadds, texte)
serveur.quit()

