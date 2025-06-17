#set: est une collection non ordonnée et sans doublons. De plus, le type set supporte
# les opérations sur les ensembles, telles que l'union, l'intersection, la différence et
# différence symétrique

# syntaxe pour un set vide:

ensemble_vide = set()

panier = {'pomme', 'orange', 'Pomme', 'poire', 'pomme'}
print(panier) # Python est sensible à la casse


a = set('abracadabra') # chaine convertie en set
b = set('alakazam')

print(a)
print(b)

print('__Union:')
# 2 syntaxes: lettres dans a ou dans b ou dans les 2
print(a | b)
print(a.union(b))

print('__Intersection:')
# 2 syntaxes: lettres dans a et dans b
print(a & b)
print(a.intersection(b))

print('__Différence:')
# 2 syntaxes: lettres dans a mais pas dans b
print(a - b)
print(a.difference(b))

print('__Différence symétrique:')
# 2 syntaxes: lettres dans a ou dans b mais pas dans les 2
print(a ^ b)
print(a.symmetric_difference(b))


# Le type supporte la syntaxe Comprehension Set

ensemble = set('abracadabra')

# construire un nouveau set ne contenant que lettres différentes de a,b et c

resultat = {lettre for lettre in ensemble if lettre not in 'abc'}

print(resultat)

lst = [1,1,2,2,3,3]

# Suppression des doublons dans une liste

lst = set(lst)
lst = list(lst)

print(lst)
