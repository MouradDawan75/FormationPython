#1) somme liste
def somme_liste(entiers):

    s = 0
    for e in entiers:
        s += e

    return s

print(somme_liste([10,15,20]))

#2) moyenne liste

def moyenne_liste(entiers):
    s = somme_liste(entiers) # len(entiers)
    compteur = 0
    for e in entiers:
        compteur += 1

    return s / compteur

#3) min liste

def min_liste(entiers):
    
    m = entiers[0] # les éléments d'une liste sont indéxés. Le premier commence à l'index 0
    for e in entiers:
        if e < m:
            m = e

    return m

#4)
def table_multiplication(nombre,premier_multipe,dernier_multiple):
    for i in range(premier_multipe, dernier_multiple + 1):
        print(f'{nombre} x {i} = {nombre * i}')

#5)

while True:

    choix = input("""
1- Convertir heures en minutes
2- Convertir minutes en heures
3- Quitter

""")
    
    if choix == '3':
        print('Fin du programme....')
        break

    if choix == '1':
        heures = int(input('Heures à convertir: '))
        print(f'{heures}h = {heures * 60}m')

    if choix == '2':
        minutes = int(input('Minutes à convertir: '))
        print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')

# Code optimisé:

def menu():
        choix = input("""
1- Convertir heures en minutes
2- Convertir minutes en heures
3- Quitter

""")
        return choix


from mesfonctions import choix1, choix2

while True:

    choix = menu()
    if choix == '3':
        break

    if choix == '1':
        choix1()

    if choix == '2':
        choix2()

