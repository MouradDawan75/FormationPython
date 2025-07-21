# dict: est une collection non ordonnée qui fonctionne par association clé:valeur
# Dans un dictionnaire physique, le mot est la clé, sa définition est la valeur.
# Dans un dict, les clés sont uniques

# Dans la pratique, le type dict est utilisé pour regrouper les caractéristiques d'un objet

user = {
    'nom' : 'DUPONT',
    'prenom' : 'Paul',
    'age' : 65
}

print(user['nom'])
# print(user['Nom']) -> si clé inexistante -> exception

print(user.get('nom'))
print(user.get('Nom')) # renvoie None si clé introuvable

# Ajouter des clés:
user['contrat'] = 'CDD'
print(user)

user['contrat'] = 'CDI'
print(user)

user.update({'nom' : 'DURAND', 'taille': 1.8})

print(user)

# On peut aussi avoir des dict complèxes:
utilisateur = {
    'nom' : 'DUPONT',
    'prenom' : 'Paul',
    'age' : 65,
    'telephones' : ['06060606', '0707070707'],
    'adresse' : {
        'rue' : '10 rue Machin',
        'code_postal' : 75001
    }
}

# Affichez chaque num. de tél.:
for t in utilisateur.get('telephones'):
    print(t)

# Affichez la rue:
print(utilisateur.get('adresse').get('rue'))
print(utilisateur['adresse']['rue'])

print('______ Parcourir un dict:')

d = {
    'a' : 1,
    'b' : 2
}

print('__for:')
# for par défaut renvoie uniquement les clés

for e in d:
    print(e) 


print('__ for sur les clés:')

for k in d.keys():
    print(f'clé: {k} - valeur: {d.get(k)}')

print('___ for sur les valeurs:')

for v in d.values():
    print(v)

print('___ for sur les items du dict:')

for item in d.items():
    print(item) # item est un tuple (clé,valeur)

# unpacking (deballage d'un tuple)
for k,v in d.items():
    print(k,v)


print('___________ Dictionary comprehension:')

d = {
    'a' : 1,
    'b' : 2
}

# Inverser le dict d

result = {v:k for k,v in d.items()}
print(result)

my_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5
}

# nouveau dict en doubant les valeurs de my_dict

dict_doubles = {k:v*2 for k,v in my_dict.items()}
print(dict_doubles)

print('____multiples conditions:')


my_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5
}

# uniquement les valeurs paires et supérieures à 2

resultat = {k:v for k,v in my_dict.items() if v % 2 == 0 if v > 2}
print(resultat)


