# Variable: zone mémoire contenant une valeur typée
# Types de données:

# types de bases: immuables
# numériques: int, float, complex
# type textuel: str
# type boolean: bool

# types complèxes: muables

# types séquences: list, tuple, range
# type mapping: dict
# types ensembles: set, frozenset
# type octets: bytes

# Python utilise le typage dynamique.
# nom_variable = valeur
# Python utilise la convention:
# PascalCase: MaVariable -> classes
# camelCase: maVariable
# snake_case: ma_variable -> convention utilisée par Python -> variables et fonctions

# Le nom d'une variable, peut contenir des lettres, des chiffres et underscore. Pas de tiret (-) et pas d'espaces
# Le nom peut commencer soit par une lettre ou un underscore

entier = 15
floattant = 10.5
complexe = 4 + 2j # j est le nombre imaginaire

z = complex(1,2)
print(z)
print(z.real)
print(z.imag)

# Il faut importé le module cmath pour manipuler les nombres complèxes

import cmath
cmath.phase(complexe)
cmath.polar(complexe)

chaine = "ceci est une chaine"
chaine1 = 'autre chaine'

# Constante: c'est une notion qui n'existe pas réellement en Python, c'est plus une convention de nommage

PSEUDO_CONSTANTE = 10
PSEUDO_CONSTANTE = 'texte'

# Variables nulles: None
x = None
print(x)

# On a une certaine liberté dans l'écriture des nombres flottants

i = 0.99
i = .99
i = 00.99

# Pour les entiers longs: les rendre pus lisibles

e = 123_456_789

print(">>>>> type des variables:")

print(type(entier))
print(type(chaine))

# En Python, tout est objet.

print('>>>>>> ID des variables:')

x = 10

print(id(x))

y = x

print(id(y))

y = 15

print(id(y))

print(">>>>>> Conversions de types:")

x = 15

f = float(x)

b = 12.55
c = int(b)

# syntaxe: type(contenu à convertir)
# str(), int(), bool().......

nb1 = int(input('Premier nombre: '))
nb2 = int(input('Second nombre: '))
s = nb1 + nb2
print("Somme = "+str(s))

print(">>>>>> Valeurs dites vraies:")

print(bool(1))
print(bool(-1))
print(bool("chaine non vide"))
print(bool([12])) # collection non vide
print(bool(True))

print(">>>>>>>> Valeurs dites fausses:")

print(bool(0))
print(bool(None))
print(bool('')) # chaine vide
print(bool([])) # collection vide
print(bool(False))

saisie = input('Tapez quelque chose: ')

if saisie:
    print('OK!')
else:
    print('Aucune saisie.....')

print(">>>>>>>>> Taille des variables:")

import sys

# Dans Python 3, aucune limite de taille pour les types numériques. Tant que vous avez de la RAM

print(sys.maxsize) # limite virtuelle du int
print(type(sys.maxsize)) # int
print(sys.maxsize == 2**63 - 1) # True

# les flottants sont infinis en Python 3
print(sys.float_info)

# limite virtuelle: max=1.7976931348623157e+308 -> veut dire 1.79... multiplié par 10 puissane 308
# Toute valeur supérieure à cette limite virtuelle est considerée comme étant infinie

e = 1.8e+308
print(e) # inf: infinie

print('>>>>>>>> valeurs aléatoires:')

import random

aleatoire = random.randint(1,10)
print(aleatoire)

import os

print(os.environ.get('PYTHON_VARIABLE'))
print(os.getenv('PYTHON_VARIABLE'))