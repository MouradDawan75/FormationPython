import math

math.sqrt(25)

# On peut aussi modifier le nom du module importé: définir un alias

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques d'un module

from math import sqrt,cos

# On peut aussi modifier le nom de l'élément spécifique

from math import sqrt as racine_carree

racine_carree(25)

from math import * # on doit connaitre toutes les fonctions du module

# Un module est un fichier (.py) qui contient généralement des fonctions, des classes 
# ou des constantes

# Un package est un dossier contenant des modules.
# Pour convertir un répertoire en package Python, ce dernier doit contenir le fichier
# __init__.py qu'on peut laisser vide

# Pour Python < 3.3: __init__py est nécessaire pour un package
# Pour Python >= 3.3: __init__.py n'est pas nécessaire pour un package mais il recommandé
# de le générer comme même pour des questions de compatibilité

# Contrainte: le nom d'un module (ou package), doit être en miniscules, sans éspaces 
# ni underscore et doit commencé par une lettre

#import mypackage.myfunctions # importer tout le module
from mypackage.myfunctions import fonction1 # importer un élément spécifique

fonction1()


