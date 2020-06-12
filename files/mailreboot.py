#!/usr/bin/python
########################################################################## 
# Ce script python est utilise pour envoyer un mail de confirmation après redémarrage de
# serveurs selon la plateforme (Windows ou Linux) de l'OS sur lequel il se joue.
# ce script est lancé via un modul ansible qui le joue sur le groupe de serveur du playbook 
# utilisé. 
# 
# Testé avec Python 2.7.18
# Script Revision: 1.0
#
##########################################################################
#
# Importation des librairies Python nécessaires
import os
import sys
import socket
import smtplib
# Declaration de la variable 'sock_name' afin de recuperer le hostname 
# par la fonction socket.gethosname()
sock_name = socket.gethostname()
# Preparation de l'email à envoyé en utilisant la bibliothèque smtplib intégré à Python
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
message['Subject'] = sock_name + " : " + socket.gethostbyname(sock_name) +  " ,  reboot"
msg = "Le serveur " + sock_name + " ( " + socket.gethostbyname(sock_name) + " ) " + " vient de redemarrer avec succes"
message.attach(MIMEText (msg.encode('utf-8'), 'plain', 'utf-8'))
# Connexion au serveur sortant, On utilise ici le serveur SMTP de Google (Gmail)(en précisant son nom et son port)
serveur = smtplib.SMTP('smtp.gmail.com:587')
serveur.starttls()
password = "secret_passwd"
serveur.login(Fromadd, password)
texte = message.as_string().encode('utf-8')
Toadds = [Toadd]
# Envoie du mail
serveur.sendmail(Fromadd, Toadds, texte)
serveur.quit() ## on ferme et quite la fonction serveur. 

