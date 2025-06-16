# Bloc conditionnel: est un ensemble d'instructions qui ne s'exécute que si une condition 
# est vérifiée

age = 15

if age < 18:
    print('mineur')
    print('toujours mineur')

print('fin du if...........')

# les : représentent le début d'un bloc d'instructions. Tant que les instructions
# sont indentées de la mm façon, on est toujours dans le bloc

# IF/ELSE

if age < 18:
    print('mineur')
else:
    print('majeur')


# Possibilité de vérifier plusieurs conditions: via le elif
if age < 18:
    print('mineur')
elif age <= 25:
    print('Jeune adulte')
else:
    print('majeur')

# On peut aussi combiner des conditions en utilisant les opérateurs logiques:

if age >= 18 and age <= 25:
    print('Entre 18 et 25')

# Syntaxe simplifiée pour le and

if 18 <= age <= 25:
    print('Entre 18 et 25')

derogation = True

if age >= 18 or derogation == True:
    print('Age 18 ou avoir une dérogation....')

# Un bloc vide n'est pas valide syntaxiquement.
# Néaumoin, on peut définir un bloc vide en utilisant le mot pass
if age > 18:
    pass

print('suite du script.....')

# Opérateur ternaire: syntaxe simplifiée du if/else classique

if age < 18:
    print('mineur')
else:
    print('majeur')

# Syntaxe ternaire:

print('mineur') if age < 18 else print('majeur')

# Depuis Python 3.10, ajout du match/case: syntaxe simplifiée du elif

note = 8

match note:

    case 0|1|2|3|4|5|6|7|8|9:
        print('En dessous de la moyenne...')

    case 10|11|12|13:
        print('Juste la moyenne....')

    # Pour les autres cas: 2 syntaxes - case other: ou case _:

    case other:
        print('Good job.....')

    # case _:
    #     print('Good job........')

# Exo1: Demandez la saisie d'un nombre. Affichez si le nombre saisi est pair ou impair

nb = int(input('Votre nombre: '))

if nb % 2 == 0:
    print(f'{nb} est pair')
else:
    print(f'{nb} est impair')

# Exo2: Demandez la saisie d'un mot. Affichez si le mot saisi contient ou pas la lettre e

mot = input('Votre mot: ')

if 'e' in mot:
    print(f'{mot} contient e')
else:
    print(f'{mot} ne contient pas e')