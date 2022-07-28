# Credit score
L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.

Nous avons choisi la base de donée "Credit score" sur le site kaggle: https://www.kaggle.com/datasets.
Cette base de données(BDD) est une BDD SQL avec de pouvoir traiter des données tabulaire. Pour le choix SQL, nous avons regardé le format le plus pertinent afin de la traiter. Si on peut se demander si une BDD orientée document est adapté, non, car nous avons aucune colonne correspondant réellement à des documents: du texte long ni des données dont le type semble être assez libre i.e non déjà fixé au préalable. Nous avons itéré le même raisonnement pour les BDD orientées graphe. 

Pour lancer ce projet vous pouvez lancer le fichier setup.sh, qui se chargera de télécharger deux images de DockerHub et lancera les containers avec API et Batabase via docker-compose.yaml.Vous pouvez tester l'API sur l'adresses suivantes http://127.0.0.1:8000/docs ou http://localhost:8000/docs.
