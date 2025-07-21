#list: est une collection ordonnée avec doublons autorisés

# liste vide:
l = []
l1 = list()

# Il n'y a aucune restriction sur le type des éléments.

my_list = [10,11.5,'test',True,[15,45]]

notes = [2,6,7,9]
print(notes)

# Ajouts:

notes.append(9)
print(notes)

notes.insert(0,9)
print(notes)

print(notes.count(9))
print(notes.index(9))

# Modifications:
notes[0] = 11
print(notes)

# Suppressions

notes.remove(9)
print(notes)

notes.pop() # par défaut supprime le dernier élémnet
print(notes)

print('___________Atteindre un élément dans une liste:')
notes = [2,6,7,9]

print(f'Première note: {notes[0]}')
print(f'Dernière note: {notes[len(notes) - 1]}')

# Python autorise les indexs négatifs
print(f'Dernière note : {notes[-1]}')

print('__________ Parcourir une liste')

print('>>> For:')

for n in notes:
    print(n)

print('>>>> while:')

indexe = 0
taille = len(notes)

while indexe < taille:
    print(notes[indexe])
    indexe += 1

print('>>>>> For avec index:')

for indexe in range(len(notes)):
    print(notes[indexe])

print('_____________Slicing:')

# Slicing: mécanisme permettant de créer des sous listes à partir de listes existantes

prenoms = ['Jean', 'Marie', 'Mark', 'Nadine']

list1 = prenoms[0:3] # de index 0 à n-1
print(list1)

list2 = prenoms[:3] # du début jusqu'à n-1
print(list2)

list3 = prenoms[:] # du début jusqu'à la fin -> copie
print(list3)

list4 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list4)

# affichez les 3 premiers prénoms:
print(prenoms[:3])

# affichez les 3 derniers prénoms:
print(prenoms[-1:-4:-1])
print(prenoms[-3:])

print('________________ Comprehension List:')

# mécanisme permettant de créer de nouvelles listes à partir de listes existantes en modifiant les éléments 
# des listes de départ.

nombres = range(10)

# nouvelle liste ne contenant que les nombres pairs:
# syntaxe classique:

nombres_pairs = []
for e in nombres:
    if e % 2 == 0:
        nombres_pairs.append(e)

# syntaxe comprehension list:

nombres_pairs_new = [e for e in nombres if e % 2 == 0]

# nouvelle liste en convertissant tous les éléments en str

nombres_str = [str(e) for e in nombres]

#print(list(filter(lambda x: x%2==0, nombres)))

print('________ Multiples conditions:')

nombres = range(10)

# nouvelle liste ne contenant que les nombres pairs supérieurs à 4

sol1 = [e for e in nombres if e % 2 == 0 and e > 4] # utilisation des opérateurs logiques
print(sol1)

sol2 = [e for e in nombres if e % 2 == 0 if e > 4] # aucune limite sur le nbre de if
print(sol2)

print(">>>>>>> random pour les listes:")

from random import choice, choices, shuffle

cartes = [x for x in range(1,11)]

print('__choice: élément aléatoire:')

print(choice(cartes))

print('__choices: sous ensemble aléatoire:')
print(choices(cartes,k=5))

print("__shuffle: mélanger les éléments d'une liste")

shuffle(cartes)
print(cartes)