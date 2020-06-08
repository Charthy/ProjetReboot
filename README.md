# ProjetReboot
Introduction

Mettre en place une solution de reboot de serveurs basés sur Linux et Windows en utilisant des modules « playbook » Ansible que j’édite en « Python » afin d’exécuter cette tâche. Cette approche est utile car il suffit de renseigner les hosts cibles dans le fichier host d’Ansible pour ensuite de manière automatisée, envoyer des commandes ou des scripts d’exécutions de certaines tâches répétitives aux hosts désignés sans avoir à le faire poste par poste manuellement. La tâches de reboot de serveur pouvant s’avérer être chronophage et très répétitive et Ansible pour gérer de façon centralisé et automatiser l’exécution de ces tâches sur des groupes d’hôtes reste pour ma part bien adapté. 

Ressources exploitables

La solution proposée est étudiée pour une infrastructure de test émulant une infrastructure de production. 
  - Un serveur Ansible que je nomme « nodemng » sous Debian10 
  -	Un serveur Windows2016
  -	Un serveur de base de données sous Debian10

Pour ma part j’utilise ansible2.7.10 / ansible2.9.10 et Python2.7.18 
Les hôtes à manager sont organisés en deux groupes :
  -	[Linux] pour les hôtes dont l’OS est Linux et 
  -	[Windows] pour les hôtes dont l’OS est Windows

Livrables
Mettre à disposition l’URL du répertoire GitHub public hébergeant le code et la documentation du module et script à mettre en place.
Le principe sera simple, il faudra à une heure définie, que le module Ansible puisse s’exécuter et jouer les tâches définit afin de lancer et exécuter le script sur les cibles définit et renvoyer une alerte via email à l’admnistrateur, puis marquer un temps d’attente durant l’exécution du redémarrage des serveurs concernés. Puis, renvoyer un deuxième mail de confirmation une fois le serveur redémarré et opérationnel. 

Planification du reboot

La planification peut être sous 4 catégories :
  -	Un fois par semaine (WEEKLY)
  -	Une fois le mois (MONTHLY)
  -	Un jour défini du mois (DAY OF MONTH)
  -	Chaque jour (EVERYDAY)

Pour ma part et dans le cadre de ces modules, j’ai choisi l’exécution d’une tâche « cron » marquant le temps de réitération du module sur le groupe des serveurs définit.

Le référentiel ou groupe d’hôtes

Le fichier référentiel « /etc/ansibles/hotes » listera les serveurs à rebooter, ainsi, si dans l’évolution de la tâche, on vient à rajouter un serveur à redémarrer, le script sera lancé sur ce dernier. Cela s’applique aussi dans le cas où, on vient à lister une nouvelle tâche d’administration de serveur, il sera ainsi plus simple de juste l’ajouter au playbook pour l’exécuter sur un groupe de serveurs.

Contraintes 

On se doit de mettre en place une solution gratuite et libre qui va : 
  -	Permettre le redémarrage des serveurs basés sur Linux
  -	Permettre l’arrêt des bases de données MySQL par l’arrêt du service « MySQLd » avant l’arrêt du serveur (cela pour le serveur de base de données)
  -	Permettre le redémarrage des serveurs Windows
  -	Renvoyer des alertes avant le redémarrage et après le redémarrage des serveurs.

Les étapes de l’exécution du module Ansible 

Une fois exécuté, selon qu’on aura exécuté le module exécutable sur le groupe des serveurs Linux ou Windows, le système doit :
  -	Contrôler sur le référentiel « /etc/ansible/hosts », tous les serveurs renseignés sous le groupe de serveur que j’ai nommé : Linux ou Windows 
      o	Vérifier qu’ils sont up
  -	 Démarrer la première tâche du module (Playbook) ici c’est la tâche « Reboot des serveurs »
      o	Faire appel au module ansible à utiliser ici c’est le module « script » 
          	On fait appel à un script édité en Python sous « /etc/ansible/files/script.py » :
          	Exécution du script sur les serveurs concernés
              •	Envoie d’une alerte informant que le serveur « hostname » va redémarrer »
              •	Puis redémarrage du serveur en choisissant les arguments « reboot » et comme raison, l’argument « maintenance ».
  -	Démarrer un module « wait_for_connection » durant le temps de redémarrage des hosts concernés et cela suite à l’éxécution du script Python. 
  -	Lancement de la 3e tâche qui est une tâche d’envoi de mail après reboot des serveurs concernés. 
      o	Ici le script lancé sert simplement à confirmer que le serveur a bien redémarré en exécutant le script « mailreboot.py ». 



