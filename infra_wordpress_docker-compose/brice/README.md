Au départ, voici le travail à effectuer:
![alt text](https://github.com/BrissouAdmin/nov23_bootcamp_devops_services-web/blob/brice/projet_base/images/Architecture_mono_wordpress.png)



Image Infra mono

Vous êtes recruté comme administrateur sysops au sein d’une société de service spécialisé dans l'IT et vous êtes chargé de déployer et gérer l’infrastructure de production pour le site internet avec les spécificités suivantes : Serveur web Nginx avec le CMS Wordpress et une base de données MariaDB, le tout sur une seule machine.



Première Amélioration du Projet:
Image Infra haute dispo

![alt_text](https://github.com/BrissouAdmin/nov23_bootcamp_devops_services-web/blob/brice/projet_base/images/Infra_Projet_Fil_rouge-Services_Web-Projet_base.jpeg)

Quelques mois plus tard, l’entreprise a massivement investi dans diverses campagnes publicitaires, le site rencontre un succès sans précédent et de plus en plus de personnes se connectent sur le serveur, entrainant ainsi une augmentation de la charge de plus en plus élevé. Il faudra donc trouver un moyen de rendre l’infrastructure hautement disponible et ceci en ajoutant des serveurs supplémentaires de sorte que la charge puisse être gérée facilement grâce à l’ajout de ces ressources supplémentaires. Il s'agit en fait d'un scaling horizontale
Vous devrez :
    • Ajouter 3 nouveaux serveurs à l’infrastructure. Il faudra donc avoir un serveur qui sera chargé de gérer uniquement la base de données. Vous déplacerez donc votre instance de MariaDB sur ce serveur. Un autre serveur sera une instance supplémentaire de Wordpress. Le dernier serveur sera une instance d’Nginx qui servira d’équilibreur de charge afin de distribuer le trafic sur les deux serveurs Wordpress.
    • Comme Wordpress est une application avec session, vous devez choisir l’algorithme d’équilibrage de charge adéquat pour votre solution.
    • Enfin, vous devez enregistrer l’adresse du serveur qui fera office d’équilibreur à votre sous-domaine et reconfigurer Let’s Encrypt pour obtention de nouveaux certificats.


