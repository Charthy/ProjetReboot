import os
import sys
import ctypes
import socket
import smtplib
sock_name = socket.gethostname()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
Fromadd = "yarez.leroy@gmail.com "
Toadd = "yarez@outlook.com"
message = MIMEMultipart()
message['From'] = Fromadd
message['To'] = Toadd
message['Subject'] = sock_name + " , reboot"
msg = "Le serveur " + sock_name + " va redemarrer"
message.attach(MIMEText (msg.encode('utf-8'), 'plain', 'utf-8'))
serveur = smtplib.SMTP('smtp.gmail.com', 587)
serveur.starttls()
serveur.login(Fromadd, "Nathan0208*Raphael")
texte = message.as_string().encode('utf-8')
Toadds = [Toadd]
serveur.sendmail(Fromadd, Toadds, texte)
serveur.quit()
user32 = ctypes.WinDLL('user32')
user32.ExitWindowsEx(0x00000002, 0x00000001)