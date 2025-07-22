# tous les collections Python sont des itérables
# 2 types d'itérables: ordonnés (list,tuple,str) et non ordonnés

print('______________ fonction enumerate:')

# fonction qu'avec les itérables ordonnés
chaine = 'test'

for e in enumerate(chaine):
    print(e) # e est un tuple(index,caractère associé)

# unpacking du tuple
for index,lettre in enumerate(chaine):
    print(index,lettre)


print('______________ Fonctions: all, any')

iterable1 = [0,1,0,1]
iterable2 = [0,0,0,0]
iterable3 = [1,1,1,1]
iterable4 = [0,1,2,3]
iterable5 = ['a','b','c','d']

print('_____all:')
# Vérifier que toutes les valeurs sont vraies
print(all(iterable1)) # False
print(all(iterable2)) # False
print(all(iterable3)) # True
print(all(iterable4)) # False
print(all(iterable5)) # True

print('_____any:')
# Vérifier qu'au moins une valeur est vraie
print(any(iterable1))
print(any(iterable2))
print(any(iterable3))
print(any(iterable4))
print(any(iterable5))

# Pour un dictionnaire all et any renvoient tout le temps True
# Pour un dict vide: any renvoie False
# Démarche:
# Extraire les clés dans une liste: d.keys() -> ensuite any et all
# Extraire les valeurs dans une liste: d.values() -> ensuite any et all

# Autres fonctions natives:
print(len(iterable1))
print(sum(iterable1))
print(min(iterable1))
print(max(iterable1))

print('______ fonction (class) zip:')

# zip est une fonction permettant de combiner des itérables
# combiner 2 listes:

list1 = [1,2,3]
list2 = ['a', 'b', 'c']

resultat = zip(list1,list2)
print(resultat)
print(type(resultat))
print(list(resultat))

# combinaison de 2 listes en dict
keys = ['a', 'b', 'd']
values = [1,2,3]

d = dict(zip(keys,values))
print(d)

# combinaison de 2 listes en plusieurs dicts

dicts = []

for k,v in zip(keys,values):
    d = {'cle': k, 'valeur': v}
    dicts.append(d)

print(dicts)

# parcourir 2 listes au même temps

list1 = [1,2,3]
list2 = ['a', 'b', 'c']

for element1,element2 in zip(list1,list2):
    print(element1,element2)

print('___________________ Iterator:')
# est un objet permettant de faire des itérations sur une collection

my_tuple = ('pomme', 'banane', 'poire')
my_iterator = iter(my_tuple)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

print('_____________ module itertools:')

# module de python qui propose un certain nombre de fonctions rapides et efficaces en mémoire
# qui peuvent être utilisées individuellement ou en les combinant

print('__________ itérateurs infinis:')

from itertools import count, repeat, cycle

my_count = count(5)
print(my_count)
print(next(my_count))
print(next(my_count))
print(next(my_count))
print(next(my_count))
print(next(my_count))

my_repeat = repeat(10)
print(my_repeat)
print(next(my_repeat))
print(next(my_repeat))
print(next(my_repeat))
print(next(my_repeat))

my_cycle = cycle('AB')
print(my_cycle)
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))

print('______________ Itérateurs finis:')

from itertools import accumulate,chain,compress,dropwhile,takewhile,filterfalse,islice

# Itérateurs se terminant par la séquence d'entrée la plus courte

print('\t__accumulate:')
my_accumulate = accumulate([1,2,3]) # e0, e0+e1, e0+e1+e2

print(next(my_accumulate))
print(next(my_accumulate))
print(next(my_accumulate))
#print(next(my_accumulate)) -> exception


print('\t__chain:')
my_chain = chain('ABC', 'DEF') # permet de charger le contenu de plusieurs de plusieurs sources de données avec un yield

print(next(my_chain))
print(next(my_chain))
print(next(my_chain))
print(next(my_chain))
print(next(my_chain))
print(next(my_chain))
#print(next(my_chain))

print('\t__compress:')

my_compress = compress('ABCDEF', [1,0,1,0,1,1]) # ((e[0] if s[1]), (e[1], s[0]))

print(my_compress) # A C E F
print(next(my_compress))
print(next(my_compress))
print(next(my_compress))
print(next(my_compress))

print('\t__dropwhile:')

my_dropwhile = dropwhile(lambda x: x < 5, [1,4,6,4,1]) # 6 4 1 -> fais un break dès que qu'un élément est sup. à 5 (condition est fausse)

print(next(my_dropwhile))
print(next(my_dropwhile))
print(next(my_dropwhile))
#print(next(my_dropwhile))

print('\t__takewhile:')

my_takewhile = takewhile(lambda x: x < 5, [1,4,6,4,1]) # 1 4
print(next(my_takewhile))
print(next(my_takewhile))

print('\t__filterfalse:')

my_filterfalse = filterfalse(lambda x : x % 2, range(10))
print(next(my_filterfalse))
print(next(my_filterfalse))
print(next(my_filterfalse))
print(next(my_filterfalse))
print(next(my_filterfalse))

print('\t__islice:')

my_islice = islice('ABCDEFG',2,None) # CDEFG

print(next(my_islice))
print(next(my_islice))
print(next(my_islice))
print(next(my_islice))
print(next(my_islice))

print('______________ Itérateurs combinatoires:')

from itertools import product, permutations, combinations, combinations_with_replacement

print('\t__product:')
my_product = product('ABCD', repeat=2) # produit cartésien

print(next(my_product))
print(next(my_product))
print(next(my_product))

print('\t__permutations')

my_permutation = permutations('ABCD', 2) # tous les ré-arrangements possibles, sans répétitions d'éléments

print(next(my_permutation))
print(next(my_permutation))
print(next(my_permutation))
print(next(my_permutation))
print(next(my_permutation))
print(next(my_permutation))

print('\t__combinaisons:')

my_combinaison = combinations('ABC', 2) # ordonnées, sans répétitions et sans combinaisons

print(next(my_combinaison))
print(next(my_combinaison))
print(next(my_combinaison))

print('\t__combinaisons with remplacement:')

my_combinations_with_replacement = combinations_with_replacement('ABC', 2) # ordonnées, avec répétitions et sans combinaisons

print(next(my_combinations_with_replacement))
print(next(my_combinations_with_replacement))
print(next(my_combinations_with_replacement))
print(next(my_combinations_with_replacement))
print(next(my_combinations_with_replacement))


