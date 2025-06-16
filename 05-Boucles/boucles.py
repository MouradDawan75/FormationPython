# for:
# 1- Permet de parcourir tous les éléments d'une collection
# 2- Permet de gérer les traitements répétetifs dont le nombre d'itérations 
# est connu d'avance

print(">>>>>>>>>>>> Boucle for:")

# Parcourir tous les éléments d'une collection

nombres = range(10) # séquence de nombres de 0 à n - 1

for e in nombres:

    #Sortir de la boucle for si e == 5
    if e == 5:
        break
    print(e)

prenom = 'Julie'

for lettre in prenom:
    print(lettre)

# Gestion d'un traitement répétetif dont le nombre d'itérations est connu

# Affichez hello 5 fois

for i in range(5):
    print('hello')


print('>>>>>>>>>> Boucle while:')
# while: boucle conditionnelle -> permet de gérer les traitements répétetifs dont
# le nombre d'itérations n'est pas connu mais qui dépendent de conditions

x = 0

# Affichez hello tnat que x < 5

while x < 5:
    print('hello')
    x += 1

# Demandez le saisie un nombre compris entre 1 et 10. Tant que le nombre n'est pas valide
# redemandez la saisie d'un autre

# Sol1: Boucle while infinie

print('>>>>> while infinie:')

while True:

    nb = int(input('Nombre entre 1 et 10'))
    if nb >= 1 and nb <= 10:
        break


# Sol2: Boucle while finie
print('>>>>> while finie:')
i = 55

while not (i >= 1 and i <= 10):
    i = int(input('Nombre entre 1 et 10'))

print('>>>>>>>>>>> break et continue:')

prenom = "sylvain"

for lettre in prenom:

    if lettre == 'y':
        continue # force le passage à l'itération suivante -> la suite de la boucle ne sera 
                 # pas exécutée   

    if lettre == 'i':
        break

    print(lettre) #  slva

