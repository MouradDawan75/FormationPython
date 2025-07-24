import os
import json

# Contrairement à un fichier texte, un fichier json en plus du texte, contient des données (listes, numériques....)

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier, 'users.json')

with open(chemin_json, 'r', encoding='utf-8') as flux:
    contenu =json.load(flux)


# print(contenu) -> contenu est une liste de dicts

for user in contenu:
    print(f'Name: {user.get('name')} - Latitude: {user.get('address').get('geo').get('lat')}')

# Ecriture json:

chemin_ecriture = os.path.join(chemin_dossier, 'sortie.json')

with open(chemin_ecriture, 'w', encoding='utf-8') as flux:

    # contenu: soit 1 dict ou une liste de dict
    data = {
        'python' : 'Langage de programmation £',
        'version' : 3.13
    }

    json.dump(data,flux,indent=4, ensure_ascii=False) # ensure_ascii=True -> tous les char non ASCII seront ignorés


print('>>>>>>>>>>>>>>> loads() et dumps()')

player_str = '{"nom" : "FEDERER", "prenom": "Roger", "sport" : "Football"}'
print(type(player_str))

# Conversion en dict: déserialisation

player_dict = json.loads(player_str)
print(type(player_dict))
print(player_dict)

# Ajouter des clés:

player_dict['age'] = 39

# Modifier une clé
player_dict['sport'] = 'Tennis'

# Supprimer une clé

del player_dict['prenom']

#player_dict.pop('prenom') -> autre façon de supprimer une clé

print(player_dict)

# Conversion en string: sérialisation

result_str = json.dumps(player_dict, indent=2)

print(result_str)

