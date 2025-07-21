#set: est une collection non ordonnée sans doublons. De plus, le type set supporte les opérations
# sur les ensembles, telles que l'union, l'intersection, la différence et la différence symétrique

# ensemble vide:

e = set()

panier = {'pomme', 'banane', 'Pomme', 'poire','pomme'} # Python est sensible à la casse
print(panier)

a = set('abracadabra') # conversion d'une chaine en set
b = set('alacazam')

print(a)
print(b)

print('__Union:')
# lettres dans a ou dans b ou dans les 2
# 2 syntaxes:
print(a | b)
print(a.union(b))

print('__Intersection:')
# lettres dans a et dans b
# 2 syntaxes:
print(a & b)
print(a.intersection(b))

print('__Différence:')
# lettres dans a mais pas dans b
# 2 syntaxes:
print(a - b)
print(a.difference(b))

print('__Différence symétrique:')
# lettres dans a ou dans b mais pas dans les 2
# 2 syntaxe:
print(a ^ b)
print(a.symmetric_difference(b))

# Les ensembles supportent la syntaxe comprehension set:
ensemble = set('abracadabra')

# nouveau set ne contenant que les lettres différentes de a,b et c

resultat = {lettre for lettre in ensemble if lettre not in 'abc'}
print(resultat) 

print('>>>>>>>>>>> frozenset:')

# est un set immuable (en lecture seule)

a = frozenset([1,2,3,4])
b = frozenset([3,4,5,6])

c = a.copy()

print(a.union(b))
print(a.intersection(b))

e = frozenset([5,6])
print(a.isdisjoint(e)) # True

print(e.issubset(b)) # True

print(b.issuperset(e)) # True

