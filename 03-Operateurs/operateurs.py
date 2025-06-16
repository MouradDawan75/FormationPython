print(">>>>>>>>>>>>> Opérateurs arithmétiques:")

print('__Addition:')

a = 7
b = 3
c = a + b
c += 2 # c = c + 2 -> syntaxe simpifiée

print(f'c = {c}')

print('__Soustraction:')

a = 7
b = 3
c = a - b
c -= 2 # c = c - 2 -> syntaxe simpifiée

print(f'c = {c}')

print('__Multiplication:')

a = 7
b = 3
c = a * b
c *= 2 # c = c * 2 -> syntaxe simpifiée

print(f'c = {c}')

print('__Division:')

a = 7
b = 3
c = a / b
c /= 2 # c = c / 2 -> syntaxe simpifiée

print(f'c = {c}')

print('__Puissance:')

a = 7
b = 3
c = a ** b # a puissance b
c **= 2 # c = c ** 2 -> syntaxe simpifiée

print(f'c = {c}')

print('__Division entière:')

a = 7
b = 3
c = a // b
c //= 2 # c = c // 2 -> syntaxe simpifiée

print(f'c = {c}')

print('__Reste de le division entière: modulo')

a = 7
b = 3
c = a % b
c %= 2 # c = c // 2 -> syntaxe simpifiée

print(f'c = {c}')

print('__Opérateurs de comparaison:')
# > >= < <= ==(égalité) !=(différent): renvoient un boolean

n1 = 5
n2 = 7

print(n1 > n2) # False
print(n1 < n2) # True

print('__Operateurs logiques:')

# and, or et not: renvoient un boolean
# Table logique:
# A     B   A and B     A or B
# v     v      v          v
# v     f      f          v
# f     f      f          f
# 
print((n1 > 0) and (n1 > n2)) # False
print(not(n1 > 0)) # False   

print('>>>>>> Affectations multiples:')

# si des variables sont du mm type et possèdent la mm valeur, on peut faire:

v1=v2=v3=10
print(id(v1))
print(id(v2))
print(id(v3))

v1 = 5
print(id(v1))

# si des variables ne sont pas du mm type, on peut faire:
# Syntaxe non recommandée en pratique

var1,var2,var3=10,True,'test'

print('____ Opérateurs: is et in')

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2) # True: car le mm contenu
print(list1 is list2) # False: car 2 objets différents en mémoire (2 id différnets)

# in: permet de vérifier si un élément fait partie d'une collection

print(1 in list1)
print(5 in list2)

chaine = 'ceci est une chaine'

print('e' in chaine)
print('une' in chaine)


# Pour des calculs complèxes, on peut utiliser les modules: math et statistics

import math,statistics

math.sqrt(25)
math.pow(2,3) # 2 puissance

print(statistics.mean(list1)) # moyenne d'une liste