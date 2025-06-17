# list: est une collection ordonnée avec doublons autorisés
# 
# 2 Syntaxes pour créer une liste vide:

l1 = []
l2 = list() 

lst = [10,True,'test', [10,20]]

# Aucune restriction sur le type des éléments d'une liste

notes = [2,6,7,9]

# Ajouts:

notes.append(9)
print(notes)

notes.insert(0,9)
print(notes)

# Modifications:

notes[0] = 10
print(notes)

# Suppressions

notes.remove(9)
print(notes)

notes.pop()
print(notes)
print(notes.index(2)) # index commence à 0
print(notes.count(2))
print(len(notes)) # nombre d'éléments

print(">>>>>>>>> Atteindre un élément:")

notes = [2,6,7,9]

taille = len(notes)

print(f'Première note: {notes[0]}')
print(f'Dernière note: {notes[taille - 1]}')

# Python autorise les indexs négatifs:

print(f'Dernière note: {notes[-1]}')

print(">>>>>>>>>>> Parcourir une liste:")

print('___For:')

for n in notes:
    print(n)

print('___While:')

taille = len(notes)
compteur = 0

while compteur < taille:
    print(notes[compteur])
    compteur += 1

print(">>>>>>>>>> Slicing:")

# Slicing: mécanisme permettant de créer des sous listes à partir de listes existantes

prenoms = ['Lua','Francis','Aminata','Candice','Pierre']


list1 = prenoms[0:3] # de index 0 à index n - 1
print(list1)

list2 = prenoms[:3] # de début jusqu'à n - 1
print(list2)

list3 = prenoms[:] # du début jusqu'à la fin -> une copie
print(list3)

list4 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list4)

# Affichez les 3 premiers éléments
print(prenoms[0:3])

# Affichez les 3 derniers éléments 
print(prenoms[-3:])

print(">>>>>>>>>>>>>>> Comprehension List:")

# Comprehension List: mécanisme permettant de créer de nouvelles listes à partir 
# de listes existantes en modifiant les éléments des listes de départ

nombres = range(10)

# Créez une nouvelle liste en doublant tous les nombres

# Syntaxe classique:

nombres_doubles = []

for e in nombres:
    nombres_doubles.append(e * 2)

# Syntaxe comprehension list:

nombres_doubles_new = [e * 2 for e in nombres]

nombres = range(10)

# Nouvelle liste ne contenant que les nombres impairs:

nombres_impairs = [e for e in nombres if e % 2 != 0]
print(nombres_impairs)

# Multiples conditions: nombres pairs supérieurs

nombres_pairs = [e for e in nombres if e % 2 == 0 and e > 2]
nombres_pairs_new = [e for e in nombres if e % 2 == 0 if e > 2] # aucune limite sur le nombre de if

# On peut utiliser des fcts dans comprehension list

def carre(n):
    return n ** 2

nombres_carres = [carre(e) for e in nombres]

print(nombres_carres)

