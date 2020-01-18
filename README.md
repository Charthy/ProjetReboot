# ProjetReboot
Introduction

Mettre en place une solution d’arrêt et de reboot de serveurs basés sur Linux et Windows afin d’en faciliter les nombreuses opérations de contrôles des services avant l’arrêt, opérations qui peuvent s’avérer être répétitives. 

Livrables
Mettre à disposition l’URL du répertoire GitHub public hébergeant le code et la documentation du script à mettre en place.
Le principe sera simple, il faudra à une heure définie, que le script puisse se lancer et vérifier durant un temps défini aussi (une heure), sur un référentiel, quel serveur doit être redémarrer.

Planification du reboot

La planification peut être sous 4 catégories :
-	Un fois par semaine (WEEKLY)
-	Une fois le mois (MONTHLY)
-	Un jour défini du mois (DAY OF MONTH)
-	Chaque jour (EVERYDAY)

Le référentiel

Le fichier référentiel listera les serveurs à rebooter, ainsi, si dans l’évolution de la tâche, on vient à rajouter un serveur à redémarrer, le script pourra le retrouver facilement sur le référentiel. Ce fichier devra être logé dans un répertoire défini. 

-	Les variables du réfentiel pourraient être : <OS>,<Hostname>,<Hours>,<Frequence>,<Action>,<Commentaires>

o	<OS> : sera obligatoire pour spécifier le type de systèmes utilisé par le serveur concerné
	Nomenclature à utiliser :
•	DEB(x) avec (x) représentant la version de l’OS
•	W2K(x)
o	<Hour> : obligatoire, cette variable va déterminer l’heure à laquelle le script va être exécuter pour le serveur concerné
o	<Frequence> : obligatoire, c’est la fréquence à laquelle le script sera exécuté pour le serveur concerné (référence aux catégories, variable à définir)
o	<Action> : Optionnel, ici l’action pourrait être :
	Soit un reboot (E : pour exécuter)
	Soit : un arrêt (S : pour stop)
o	<Comment> : optionnel, servira à renseigner un commentaire quand aux actions à prévoir pour le serveur concerné.

Contraintes 

On se doit de mettre en place une solution gratuite et libre qui va : 
-	Permettre l’arrêt des serveurs basés sur Linux
-	Permettre l’arrêt des bases de données MySQL avant l’arrêt du serveur
-	Déconnecter les utilisateurs connectés aux bases de données 
-	Faire un Dump des bases de données
-	Envoyer les logs de contrôles à chaque étape de l’exécution du script
-	Veiller à ce que le script puisse être exécutable sur les systèmes basés sur Linux et Windows
Les étapes du script

Une fois exécuté, le système doit :
-	Contrôler sur le « référentiel », tous les serveurs renseignés et correspondant à la planification définie
o	Génération d’un premier log (point de contrôle) : liste les serveurs (Linux) qui vont être rebootés (Serveurs satisfaisant aux conditions des variables du fichier du référentiel)
-	 Vérification de liste générée si les serveurs (Linux ou Windows) concernés sont UP ou DOWN
o	Extraction des serveurs Linux_U (U : pour UP) 
o	Extraction des serveurs Linux_D (D : pour DOWN)
	Si serveur Windows concernés :
o	Extraction des serveurs Windows_U 
o	Extraction des serveurs Windows_D 
	Sinon
o	Génération de la liste de serveurs nécessitant un arrêt de service_S
o	Génération de la liste de serveurs nécessitant un arrêt de MySQL_S

-	Reboot des serveurs
o	Le reboot va se baser sur la liste extraite 
	Linux_U ou Windows_U
o	Génération de liste des serveurs Linux_R (R : restart)
o	Génération de la liste des serveurs Windows_R
o	Liste des serveurs Windows_Linux_R

-	Envoie des commandes d’arrêt de services et des bases de données
o	Se base sur les listes générées 
	Service_S et MySQL_S
o	Génération des Services.log (à placer dans le dossier des log)
o	Génération des MySQL_log (à placer dans le dossier des logs)

