#!/usr/bin/python
########################################################################## 
# Ce script python est utilise pour rebooter des serveurs Linux et Windows
# en envoyant en premier un message d'alerte a l'administrateur une fois le script lancé
# puis en redémarrant le serveur selon la plateforme (Windows ou Linux) de l'OS.
# ce script est lancé via un modul ansible qui le joue sur le groupe de serveur du playbook 
# utilisé. 
# 
# Testé avec Python 2.7.18
#
##########################################################################
#
# Importation des librairies Python nécessaires
import sys, platform
import socket
import smtplib

# Declaration de la variable 'sock_name' afin de recuperer le hostname 
# par la fonction socket.gethosname()
sock_name = socket.gethostname()

# Envoie d'email d'alerte en text plein via Python en utilisant le serveur 
# SMTP de Google -  'gmail' d'où l'mportation du module 'smtplib' natif de Python. 
# Ici nous faison appel aux modules permettant de définir l'expediteur, les destinataires
# ainsi que l'objet.
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

Fromadd = "mail_expediteur "
Toadd = "mail_destinataire"
# creation de l'objet message 
message = MIMEMultipart()
message['From'] = Fromadd
message['To'] = Toadd
# Specification de l'objet du mail en faisant appel à la fonction 'socket.gethostbyname()' 
# Afin de récupérer l'IP de l'hote concerné
message['Subject'] = sock_name + " : " + socket.gethostbyname(sock_name) + " , reboot"
# Specification du message a envoyer
msg = "Le serveur " + sock_name + " ( " + socket.gethostbyname(sock_name) + " ) " + " va rebooter"
message.attach(MIMEText (msg.encode('utf-8'), 'plain', 'utf-8'))

# Connexion au serveur sortant (en précisant son nom et son port)
serveur = smtplib.SMTP('smtp.gmail.com:587')
serveur.starttls()
password = "secret_passwd"
serveur.login(Fromadd, password)
texte = message.as_string().encode('utf-8')
Toadds = [Toadd]
# Envoie du mail 
serveur.sendmail(Fromadd, Toadds, texte)
serveur.quit()

# Instruction de redemarrage du serveur selon la platforme de l'OS
# Pour Windows, ici on importe la bibliothèque 'ctypes' afin d'utiliser la fonction 
# ExitWindowsEx() et transmettre les arguments qui permettent de redémarrer l'ordinateur
# Avec comme argument justificatif 'une maintenance planifiée'
if sys.platform == 'win32':
  import ctypes
  user32 = ctypes.WinDLL('user32')
  user32.ExitWindowsEx(0x00000002, 0x00000001)

# Pour Linux ce script ne s'appliquant pour l'instant qu'au serveur de base de donnees
# Mysql, il sera juste question d'arrêter le service MySQLd puis de lancer un reboot.
else:
  import os
  os.system("systemctl stop mysqld")
  os.system("shutdown -r now")
