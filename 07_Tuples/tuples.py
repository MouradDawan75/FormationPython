# tuple: est collection ordonnée avec doublons autorisés. Il s'agit d'une liste en lecture seule (liste constante)
# 
# tuple vide:
t1 = ()
t2 = tuple()

prenoms = ('Jean','Marie','Mark')
print(prenoms.count('Jean'))
print(prenoms.index('Jean'))

#prenoms[0] = 'Dawan'

# unpacking (deballage d'un tuple):

p1,p2,p3 = prenoms
print(p1)
print(p2)
print(p3)

# Modification d'un tuple

# conversion en list
prenoms = list(prenoms)

# application des modifs:
prenoms.pop()
prenoms.append('Paris')
prenoms[0] = 'Dawan'

# conversion en tuple
prenoms = tuple(prenoms)

print(prenoms)
