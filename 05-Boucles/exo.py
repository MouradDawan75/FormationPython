#1)Affichez tous les nombres de 1 (inclus) à 10 (inclus) -> range()

for i in range(11):
    if i != 0:
        print(i)

for i in range(10):
    print(i+1)

# on peut modifier l'index de départ de la focntion range
for i in range(1,11):
    print(i)

#2)Affichez tous les nombres impairs de 1 (inclus) à 15 (inclus)

for i in range(1,16):
    if i % 2 != 0:
        print(i)

# on peut modifier le pas de la fonction range
for i in range(1,16,2):
    print(i)

#3)

while True:
    choix = input("""

    - Addition: tapez a
    - Soustraction: tapez s
    - Multiplication: tapez m
    - Division: tapez d
    - Quitter: tapez q

    Votre choix: 

    """)

    # Gestion du break

    if choix == 'q':
        print('fin du programme....')
        break

    # Gestion d'un choix invalide

    if choix not in ['a','s','m','d']:
        print('Choix invalide....')
        continue

    # Demandez la saisie de 2 floats
    nb1 = float(input('Premier nombre: '))
    nb2 = float(input('Second nombre: '))

    # Gestion de la division par 0

    if choix == 'd' and nb2 == 0:
        while nb2 == 0:
            nb2 = float(input('Second nombre différent de 0: '))

    # Affichez le résultat

    match choix:

        case 'a':
            print(f'{nb1} + {nb2} = {nb1 + nb2}')

        case 's':
            print(f'{nb1} - {nb2} = {nb1 - nb2}')

        case 'm':
            print(f'{nb1} x {nb2} = {nb1 * nb2}')

        case 'd':
            print(f'{nb1} / {nb2} = {nb1 / nb2}')

        


        
        