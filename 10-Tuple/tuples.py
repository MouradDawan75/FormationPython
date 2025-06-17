#tuple: collection ordonnée avec doublons autorisés. Il s'agit d'une liste en lecture seule
# une sorte de liste constante

# 2 syntaxes pour créer des tupes vides:
t1 = ()
t2 = tuple()

prenoms = ('Jean', 'Marie', 'Marc')

prenoms.count('Jean')
prenoms.index('Jean')

# Deballage (unpacking)
p1,p2,p3 = prenoms
print(p1)
print(p2)
print(p3)

# Modification d'un tuple:

# 1- Conversion en liste
prenoms = list(prenoms)

# 2- Application des modifications
prenoms.remove('Jean')
prenoms.append('Paris')

# 3- Conversion en tuple
prenoms = tuple(prenoms)

print(prenoms)