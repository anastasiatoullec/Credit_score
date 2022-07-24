# Credit score
L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.

Nous avons choisi la base de donée "Credit score" sur le site kaggle: https://www.kaggle.com/datasets.
Cette base de données(BDD) est une BDD SQL avec de pouvoir traiter des données tabulaire. Pour le choix SQL, nous avons regardé le format le plus pertinent afin de la traiter. Si on peut se demander si une BDD orientée document est adapté, non, car nous avons aucune colonne correspondant réellement à des documents: du texte long ni des données dont le type semble être assez libre i.e non déjà fixé au préalable. Nous avons itéré le même raisonnement pour les BDD orientées graphe. 

Pour lancer ce projet vous avez besoin simplement de démarrer Docker compose avec la commende suivante: docker-compose up.
Il va exécuter tous les scripts nécessaires pour que vous puissiez voir API sur l'adresse http://127.0.0.1:8000/docs ou http://localhost:8000/docs.
