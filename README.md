API SOAP EgaPro
Ce projet est une API SOAP construite à l'aide de Flask et Spyne, servant les données EgaPro depuis un fichier CSV via des points d'accès SOAP.

Table des matières
Installation
Utilisation
Points d'accès de l'API
Format des données CSV
Contribuer
Licence
Installation
Pour exécuter ce projet, vous devez avoir Python installé. Suivez les étapes ci-dessous pour configurer l'environnement et exécuter l'application :

Clonez le dépôt :

sh
Copier le code
git clone https://github.com/your-username/egapro-soap-api.git
cd egapro-soap-api
Créez et activez un environnement virtuel :

sh
Copier le code
python -m venv venv
source venv/bin/activate   # Sous Windows : venv\Scripts\activate
Installez les dépendances :

sh
Copier le code
pip install flask spyne
Placez votre fichier CSV :
Assurez-vous que votre fichier CSV est nommé index-egalite-fh-utf8.csv et est situé dans le même répertoire que l'application.

Exécutez l'application :

sh
Copier le code
python app.py
Utilisation
Après avoir exécuté l'application, l'API SOAP sera disponible à http://localhost:5000/soap.

Exemple de requête SOAP
Vous pouvez utiliser un outil comme SOAP UI ou Postman pour envoyer des requêtes SOAP. Voici un exemple de requête SOAP pour récupérer des données par SIREN :

xml
Copier le code
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.flask">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:get_data_by_siren>
         <spy:siren>123456789</spy:siren>
      </spy:get_data_by_siren>
   </soapenv:Body>
</soapenv:Envelope>
