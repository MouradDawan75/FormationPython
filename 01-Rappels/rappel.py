# Connaitre la syntaxe
# Connaitre les types de données: int, float, str, bool, tuple, list, dict, set
# Savoir faire des contrôles: if/else - match/case
note = 10

match note:
    case 0|1|2|3|4|5:
        print('note entre 0 et 5')

    case 6|7|8|9|10:
        print('note entre 6 et 10')

    # 2 syntaxes pour les autres cas:
    case other:
        print('autre note')

    # case _:
    #     print('autre note')

# Savoir les traitements répététifs:
# Utilisation des boucles:
# For:
# ---- permet de parcourir tous les éléments d'une collection

# afficher hello 5 fois

for i in range(5):
    print('hello')

# While: boucle conditionnelle

n = 5

while n < 10:
    print('test')
    n = n +1

# Savoir manipuler les collections

# list: est une collection ordonnée avec doublons autorisés
lst = []


# tuple: collection ordonnée avec doublons autorisés: il s'agit d'une liste en lecture seule
t = ()


# dict: collection non ordonnée qui fonctionne par association clé:valeur
d = {
    'nom': 'DUPONT',
    'prenom': 'Jean'
}

# set: est une collection non ordonnée sans doublons
s = set()

import math,statistics

# on peut importer des éléments spécifiques

from math import sqrt

from mymodule import add

print(add(5,10))



# Les modules visibles par python, sont listés dans sys.path

import sys

print(sys.path)

# Solution: ajouter le chemin du module2 dans sys.path

import os

print(__file__)# c:\.....\rappel.py

chemin_dossier_en_cours = os.path.dirname(__file__) # c:\...\01-Rappels
chemin_dossier_principal = os.path.dirname(chemin_dossier_en_cours) # c:\....\FormationPython

# ajout du chemin principal dans sys.path

sys.path.append(chemin_dossier_principal)

from module2 import soustraction

print(soustraction(10,5))


# pour récupérer le chemin du dossier principal:
print(os.getcwd())

# Environnement virtuel: il s'agit d'une copie de Python
# Pour créer des envi. virtuels, on utilise le module venv#####

############# Bonnes pratiques:

#### Etapes à mettre en place au début d'un projet

# - créer un env. virtuel
# - installer les modules externes nécessaires au projets

# 1- Commande à exécuter dans le terminal:
# python -m venv nom_environnement

# 2- Activer l'env. virtuel
# dans le terminal: .\myenv\Scripts\activate
# Vérifiez que l'env. virtuel est sélectionné dans Vs Code

# pip: est le gestionnaire de modules externes python

# pip list
# pip install nom_module_externe
# pip uninstall nom_module_externe

######### Etapes à mettre en place à la fin d'un projet:

# générer un fichier contenant la liste des modules externes utilisés dans le projet
# commande à exécuter dans le terminal:

# pip freeze --local > requirements.txt

# Pour intaller les modules listés dans requirements.txt:
# commande: pip intall -r requirements.txt
