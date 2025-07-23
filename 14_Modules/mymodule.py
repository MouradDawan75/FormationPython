import random

random.randint(1,10)

# On peut aussi modifier le nom du module importé (définir un alias)

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques

from math import sqrt

sqrt(25)

# On peut aussi modifier le nom de 'élément importé

from math import sqrt as racine_carree

racine_carree(25)

# On peut aussi importé tous les éléments d'un module

from math import * # il faut connaitre le nom de tous les éléments du module 

# Un module est un fichier Python (.py) qui contient généralement, des fonctions, des classes ou des constantes.
# Un package est un répertoire contenant des modules
# Contrainte: le nom d'un package (module), doit être en miniscule, sans éspaces et sans undescore et doit commencer
# par une lettre.

# Pour convertir un répertoire en package Python, ce dernier doit contenir le fichier __init__.py 
# qu'on peut laisser vide

# Python < 3.3: __init__.py obligatoire
# Python >= 3.3: __init__.py n'est pas nécessaire. Mais il est recommandé de le générer pour des raisons de compatibilté

#import mypackage.module1 as md1
#from mypackage.module1 import fonction1

# Un module importé est toujours exécuté

#fonction1()

# Pour un module exécuté: __name__ == '__main__'
# Pour un module importé: __name__ == 'nom_module_importé'

# vérification de la conf. du init.py
from mypackage import *


fonction3()
module1.fonction1()

# from monpackage.mesfonctions import f1
# Les chemins visibles par Python, sont listés dans sys.path

import sys

print(sys.path) # Par défaut, seul le dossier en cours est visible
# solution: ajouter le chemin du dossier principal (du projet) dans sys.path

#chemin_dossier_principal = 'c:\.........'

import os

print(__file__) # c:\.......\mymodule.py

chemin_dossier_en_cours = os.path.dirname(__file__)
chemin_dossier_projet = os.path.dirname(chemin_dossier_en_cours)

sys.path.append(chemin_dossier_projet)

from monpackage.mesfonctions import f1

f1()


