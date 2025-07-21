print('______________Opérateurs arithmétiques:')

print('>>> Addition:')

a = 7
b = 3
c = a + b
c += 2 # c = c + 2

print(f'c = {c}')

print('>>> Soustraction:')

a = 7
b = 3
c = a - b
c -= 2 # c = c - 2

print(f'c = {c}')

print('>>> Multiplication:')

a = 7
b = 3
c = a * b
c *= 2 # c = c * 2

print(f'c = {c}')

print('>>> Division:')

a = 7
b = 3
c = a / b
c /= 2 # c = c / 2

print(f'c = {c}')

print('>>> Division entière:')

a = 7
b = 3
c = a // b
c //= 2 # c = c // 2

print(f'c = {c}')

print('>>> Puissance:')

a = 7
b = 3
c = a ** b
c **= 2 # c = c ** 2

print(f'c = {c}')

print('>>> Reste de la division entière: modulo:')

a = 7
b = 3
c = a % b
c %= 2 # c = c % 2

print(f'c = {c}')

print('_________________Opérateurs de comparaison:')

# > >= < <= ==(égalité) != (différent)

print('_________________Opérateurs logiques:')

# and, or et not

print('_________________Affectations multiples:')

# si des variables sont du mm type et possèdent la mm vaeur, on peut faire:
v1=v2=v3=10

# si des variables ne sont pas du mm type, on peut faire:

var1,var2,var3 = 10,True,'Test'

print('_____________ Opérateurs: is et in:')

# in permet de vérifier si un element fait partie ou pas d'une collection

chaine = 'test'

print('e' in chaine)

list1 = [1,2,3]
list2 = [1,2,3]

print(1 in list1)
print(2 in list2)

print(list1 == list2) # True: mm contenu
print(list1 is list2) # False: car 2 objets (id) différents en mémoire

print('______ Opérateur walrus:')

# opérateur permettant d'assigner une valeur à une variable et de l'utiliser dans un calcul

print((x:=5) + 8)

(l:=[]).append(5)

# Pour faire des calculs complèxes, on utiliser les modules math et statistics

import math,statistics

math.sqrt(25)
math.exp(2)
math.factorial(5)
math.isinf(30)
math.pow(5,2)

statistics.mean(list1) # moyenne d'une liste

print(dir(math))
print(help(math.pow))