API de Données EgaPro
Ce dépôt contient une API simple basée sur Flask pour accéder aux données d'un fichier CSV contenant des informations sur les indices d'égalité professionnelle entre les femmes et les hommes pour différentes entreprises. Les données sont chargées en mémoire et servies via plusieurs points de terminaison API.

Prise en Main
Prérequis
Pour exécuter ce projet, vous aurez besoin de :

Python 3.x
Bibliothèque Flask
Installation
Clonez le dépôt sur votre machine locale :

bash
Copier le code
git clone <url-du-depot>
cd <repertoire-du-depot>
Installez les packages Python requis :

bash
Copier le code
pip install Flask
Assurez-vous que le fichier de données CSV (index-egalite-fh-utf8.csv) est présent dans le répertoire du projet.

Lancer l'Application
Pour démarrer l'application Flask, exécutez la commande suivante :

bash
Copier le code
python app.py
L'application sera disponible à l'adresse http://127.0.0.1:5000.

Points de Terminaison de l'API
Obtenir les Données par SIREN
Requête
GET /api/siren/<siren>

Paramètres
siren (string) : Le numéro SIREN de l'entreprise.
Réponse
200 OK : Retourne les données pour le SIREN spécifié au format JSON.
404 Not Found : Si le SIREN n'est pas trouvé, retourne un message d'erreur.
Exemple
bash
Copier le code
curl http://127.0.0.1:5000/api/siren/123456789
Obtenir Tous les SIREN
Requête
GET /api/sirens

Réponse
200 OK : Retourne une liste de tous les numéros SIREN disponibles au format JSON.
Exemple
bash
Copier le code
curl http://127.0.0.1:5000/api/sirens
Obtenir Toutes les Données
Requête
GET /api/data

Réponse
200 OK : Retourne toutes les données au format JSON.
Exemple
bash
Copier le code
curl http://127.0.0.1:5000/api/data
Aperçu du Code
Chargement des Données : Le fichier CSV index-egalite-fh-utf8.csv est lu, et les données sont stockées dans le dictionnaire egapro_data, indexé par les numéros SIREN. Seules les données les plus récentes pour chaque SIREN sont conservées.
Application Flask : L'application Flask fournit trois points de terminaison pour accéder aux données.
Structure des Fichiers
app.py : L'application Flask principale.
index-egalite-fh-utf8.csv : Le fichier de données CSV (non inclus dans le dépôt).
