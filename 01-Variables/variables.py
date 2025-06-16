# Variable: zone mémoire (RAM) contenant une valeur typée

# Types numériques: entiers (int), réels (float), complex
# Type textuel: str (String)
# Type boolean: True / False
# Collections:
# Listes: range, list, tuple
# Ensemble: set
# Dictionnaire: dict

# Syntaxe pour créer des variables:
# Python utilise le typage dynamique:
# Java utilise le typage statique: int  x = 10

my_int = 10
my_float = 10.5

# 2 syntaxes pour le type textuel
my_chaine1 = 'ceci est une chaine'
my_chaine2 = "autre chaine"
my_complex = 4 + 5j # j est nombre imaginaire
my_bool = True

# Convetion de nommage des variables:
# PascalCase: MyInt
# camelCase: myInt
# snake_case: my_int -> convention utilisée par Python

# Le nom d'une variable ne peut contenir que des lettres, chiffres et undescore
# pas d'espaces, pas de caractère spacial et pas de tiret (-)
# e nom d'une variable peut commancé soit par une lettre ou undescore
_x = 10

print(my_int)
print(my_complex.real)
print(my_complex.imag)

# Constante: est une variable dont le contenu ne peut pas être modifié
# Le nom d'une constante doit être en majuscule

# La notion de constante n'existe pas réellement en python, c'est juste
# une convention de nommage

MA_CONSTANTE = 15
MA_CONSTANTE = 'texte'

print(MA_CONSTANTE)

# Variable nulle: None

x = None
print(x)

# Pour les nombres long, on peut pratiquer la syntaxe suivante pour les rendre
# plus lisibes:

n = 1_158_699
print(n)

# Pour les nombres réels, on peut faire:

# ces 3 syntaxes sont équivalentes
z = 0.99
z = 00.99
z = .99

print(">>>>>> type d'une variable:")

print(type(my_int))
print(type(my_chaine1))
print(type(my_bool))

print(">>>>> Conversions de types:")

f = 11.8
i = int(f)

print(i)

f = float(i)
s = str(f)

# bool(variable a convertir)
# int(variable a convertir)
# str(variable a convertir)
# float(variable a convertir)

nb1 = int(input('Premier nombre: '))
nb2 = int(input('Second nombre: '))

somme = nb1 + nb2

print("Somme = " + str(somme))

# Python ne permet de concaténer que des str

print('>>>>>>>>> ID des variables:')

x = 5

print(id(x))

y = x
print(id(y))

print(">>>>>>>>>> module random")

# module permettant de générer des valeurs aléatoires

import random

aleatoire = random.randint(1,10)

print(aleatoire)

#Raccourcis claviers:

# copier/coller: ctr + c - ctr + v
# commenter des lignes sélectionnées: ctr + k + c
# décommenter des lignes sélectionnées: ctr + k + u