import random

aleatoire = random.randint(1,100)

for i in range(6):
    print(f'{i+1} tentative')
    nombre = input('Votre nombre: ')
    try:
        nombre = int(nombre)
        if nombre == aleatoire:
            print(f'Trouvé en {i+1} tentatives. Aléatoire = {aleatoire}')
            break

        if aleatoire > nombre:
            print('Plus grand')

        if aleatoire < nombre:
            print('Pkus petit')


    except:
        print('Nombre invalide.....')


if nombre != aleatoire:
    print(f'Perdu! aleatoire = {aleatoire}')

print('>>>>>>>>>>> while finie:')

compteur = 0

while compteur < 6:
    nombre = input('Votre nombre: ')
    compteur += 1
    try:
        nombre = int(nombre)
        if nombre == aleatoire:
            print(f'Trouvé en {compteur} tentatives. Aléatoire = {aleatoire}')
            break

        if aleatoire > nombre:
            print('Plus grand')

        if aleatoire < nombre:
            print('Pkus petit')


    except:
        print('Nombre invalide.....')
