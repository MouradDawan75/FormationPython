# Un env. virtuel est une copie de Python

# Bonnes Pratiques:

# Au début d'un projet, on créer un env. virtuel contenant les modules externes nécessaires au projet

# 1- Pour créer un env. virtuel, on utilise le module venv de Python
# Commande: python -m venv nom_env_virtuel

# 2- Activer l'env. virtuel:
# commande: .\myenv\Scripts\activate

# Si power shell bloque l'activation:
# - Démarrer Power Shell en tant qu'admin
# - commande dans Power Shell: Set-ExecutionPolicy RemoteSigned -> répondre par o (oui)
# - réactiver l'env. virtuel
# - Dans VS Code choisir l'interpréteur de l'env. virtuel

# Pour installer des modules externes, on utilise le pip
# pip list
# pip install nom_module_externe
# pip uninstall nom_module_externe

# Une fois l'env. virtuel activé:
# Installez les modules externes nécessaires au projet


# A la fin du projet, on génère un fichier (requirements.txt) contenant la liste des modules installés
# commande: pip freeze --local > requirements.txt

# Pour installer les modules listés dans requirements:
# commande: pip install -r requirements.txt

# requests module nécessaire pour faire appelle à des api rest

# Api Rest (web service rest): une application web sans IHM qui renvoie du contenu json
# REST: Respresentation State Transfert - est un style d'architecture
# Api Rest: n'est pas limitée au format json: elle peut renvoyée du texte, xml, binaire.....

# Une Api Rest est un ensemble de ressources (images, article d'un journal..), où chaque ressource possède un ID
# URI (Uniform Resource Identifier-appelé end point), une méthode d'accès (GET,POST,DELETE,PUT) et elle peut être
# publique ou privée

# Toutes ces infos sont fournies dans la doc de l'api

import requests

END_POINT = 'https://restcountries.com/v3.1/name/'

pays = input('Votre pays: ')

reponse = requests.get(END_POINT+pays).json()

if reponse[0].get('name').get('common') == pays:

    print(f'Nom: {reponse[0].get('name').get('common')} - Capitale: {reponse[0].get('capital')} - Population {reponse[0].get('population')}')
    print('______Pays limitrophes:______')
    print(reponse[0].get('borders'))
    for code in reponse[0].get('borders'):
        rep = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        print(f'Nom: {rep[0].get('name').get('common')}')
else:
    print('Pays introuvable............')