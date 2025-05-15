import os
import json

# Contrairement à un fichier texte, un fichier json en plus du texte, 
# contient des données (tableaux, listes, valeurs numériques...)

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier, 'users.json')

# Lecture d'un json:

with open(chemin_json,'r', encoding='utf-8') as flux:
    contenu = json.load(flux)

# print(contenu) -> il s'agit d'une liste de dictionnaires

for user in contenu:
    print('Name:',user.get('name'), 'Latitude:', user.get('address').get('geo').get('lat'))


# Ecriture dans un fichier json:
chemin_sortie = os.path.join(chemin_dossier,'sortie.json')

with open(chemin_sortie, 'w', encoding='utf-8') as flux:
    # contenu: soit une liset de dict - soit 1 seul dict
    data = {
        'nom': 'DUPONT',
        'prenom': 'David'
    }

    json.dump(data,flux, indent=4, ensure_ascii=False) # ensure_ascii = True: tous les char non ascii seront ignorés

# load() et dump(): pour manipuer les fichiers json

print(">>>>>>>>>>>>> loads() et dumps(): pour les chaines json")

# Le format json, utilise les doubles côtes pour les chaines de caractères

employe = '{"first_name:":"DUPONT", "last_name": "Jean"}'

print(type(employe))

#loads(): permet de convertir une chaine en dict
employe_dict = json.loads(employe)

print(type(employe_dict))

# Ajouter une clé
employe_dict['age'] = 65

print(employe_dict)

# MAJ une clé
employe_dict['last_name'] = 'David'
print(employe_dict)

# dumps(): permet de convertir un dict en chaine

chaine = json.dumps(employe_dict)

print(chaine)