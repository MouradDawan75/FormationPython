#dict: est une collection non ordonnée qui fonctionne par association clé:valeur
# Dans un dictionnaire physique, le mot est la clé, sa définition est la valeur.
# Les clés sont uniques dans un dictionnaire.

# 2 Syntaxes pour créer un dict vide:

d1 = {}
d2 = dict()

# Le type dict sert générelement à regrouper les caractéristiques d'un objet

user = {
    'nom' : 'DUPONT',
    'prenom': 'Jean',
    'age': 65
}

# Afficher le nom:
print(user['nom'])
#print(user['Nom']) -> si clé introuvable -> exception

print(user.get('nom'))
print(user.get('Nom')) # si clé introuvable -> renvoie None

# On peut ajouter des clés dans un dict

user['contrat'] = 'CDD'

print(user)

user['contrat'] = 'CDI' # si la clé existe: la valeur associée est écrasée
print(user)

# On peut aussi avoir des dicts complèxes:

utilisateur = {
    'nom' : 'DUPONT',
    'prenom': 'Jean',
    'age': 65,
    'telephones': ['06060606','07070707'],
    'adresse': {
        'rue': '10 rue Machin',
        'code_postal': 77000
    }
}

# Affichez chaque num. de tél.:
for t in utilisateur.get('telephones'):
    print(t)

# Affichez la rue:
print(utilisateur.get('adresse').get('rue'))

print(">>>>>>>>>>>Appel d'une API Rest")

# Il faut installer le module requests
# pip est le gestionnaire de modules externes
# pip install nom_module
# pip uninstall nom_module
# pip list: afficher la liste des modules installés

# import requests

# URI='https://api.restful-api.dev/objects'

# reponse = requests.get(URI).json() # json(): conversion du contenu en dict

# #print(reponse.content) - c'est une liste de dict

# id = input('Id du produit: ')

# for produit in reponse:
#     if produit.get('id') == id:
#         print(f"Id: {produit.get('id')} - Name: {produit.get('name')}")

print(">>>>>>>>>>> Parcourir un dict:")

d = {
'a':1,
'b':2
}

# For par défaut revoi uniquement les clés:
for element in d:
    print(element)

# for explicite sur les clés
for cle in d.keys():
    print(f'Clé: {cle} - Valeur: {d.get(cle)}')


# for explicite sur les valeurs
for v in d.values():
    print(v)

# for sur les items (clé,valeur) du dict
for item in d.items():
    print(item) # item est un tuple(clé,valeur)

# Exo:
# Demandez la saisie d'un mot. Affichez un dictionnaire dont les clés sont les lettres 
# qui composent le mot et les valeurs sont le nombre de chaque lettre dans le mot
# Ex: test -> {'t': 2, 'e': 1, 's': 1}


mot = input('Votre mot: ')

d = {}

for lettre in mot:
    d[lettre] = mot.count(lettre)

print(d)
