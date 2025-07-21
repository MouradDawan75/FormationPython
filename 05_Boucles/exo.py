#1)
# sol1:
for i in range(15):
    print(i+1)

#sol2:
for i in range(16):
    if i != 0:
        print(i)

# sol3:
for i in range(1,16):
    print(i)

#2)
# sol1:
for i in range(1,16):
    if i % 2 != 0:
        print(i)

# sol2:
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

    """)

    #gestion de la boucle infinie: break
    if choix == 'q':
        print('Fin du programme.......')
        break

    #gestion choix invalide
    if choix not in 'asmd':
        print('Choix invalide.....')
        continue

    nb1 = float(input('nb1: '))
    nb2 = float(input('nb2: '))

    #gestion de la division par 0

    if choix == 'd' and nb2 == 0:
        while True:
            print('nb2 doit être différent de 0')
            nb2 = float(input('nb2: '))
            if nb2 != 0:
                break


    match choix:
        case 'a':
            print(f'{nb1 + nb2 = }')

        case 'm':
            print(f'{nb1 * nb2 = }')

        case 's':
            print(f'{nb1 - nb2 = }')

        case 'd':
            print(f'{nb1 / nb2 = }')