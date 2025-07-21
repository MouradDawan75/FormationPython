# For:
# - Permet de gérer un traitement répététif dont le nombre d'itérations est connu d'avance
# - Permet de parcourir tous les éléments d'une collection

# While: boucle conditionnelle
# - Permet de gérer les traitements répététtifs dont le nbre d'itérations n'est pas connu, mais
# qui dépendent d'une condition

print('>>>>> For:')

nombres = range(10) # de 0 à 
print(type(nombres)) # est objet de type range

for i in nombres:
    print(i)

# Affichez hello 5 fois

for e in range(5):
    print('hello')

print('>>>> while:')

n = 0

while n < 5:
    print('bonjour')
    n += 1

# Demandez la saisie d'un nombre compris entre 1 (inclus) et 10 (inclus)

# while finie
i = 0
while not(1 <= i <= 10):
    i = int(input('Nombre entre 1 et 10: '))

# while infinie
while True:
    i = int(input('Nombre entre 1 et 10: '))
    if 1 <= i <= 10:
        break

chaine = 'texte'

for c in chaine:
    print(c)

print('>>>>>>>> break et continue')

prenom = 'sylvain'

for lettre in prenom:

    if lettre == 'y':
        continue # force le passage à 'itération suivante

    if lettre == 'i':
        break

    print(lettre) # slva

lst = [10,20,30]
taille = len(lst)
index = 0

while index < taille:
    print(lst[index])
    index += 1