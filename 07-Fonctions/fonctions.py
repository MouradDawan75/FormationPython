# Fonction: est un ensemble d'instructions réutilisable
# 2 types de fonctions:
# Fonction qui ne renvoie aucun résultat: ex: print()
# Fonction qui renvoie un résultat. Ex: input()

# Syntaxe pour créer une fonction: def nom_fonction(paramètres): instructions

# Exemple d'une fonction

def fonction1():
    print('texte de fct1..........')

fonction1()

print(fonction1) # sans les parenthèses, il s'agit d'une variable contenant l'id de la fct

f = fonction1
f()

# Exemple d'une fct avec des params:

def repeter(message, nombre_de_fois):
    # for i in range(nombre_de_fois):
    #     print(message)

    v = 10

    compteur = 0
    while compteur < nombre_de_fois:
        print(message)
        compteur += 1

repeter('hello', 5)

# Exemple qui renvoie un résultat:

def carre(nombre):
    return nombre ** 2


r = carre(5)
print(r)

# Annotations de type: permet aux dév. de spécifier le type de params attendus
# par une fonction

x:int = 10
s:str = 'test'

x = 'test'
print(x)

# Le fait de pratiquer les annotations de types, ne change pas le caractère dynamique
# du langage

def somme(x:int, y:int) -> int:
    return x+y

print(">>>>>>>>>>>>> Fonctions avec des params optionnels:")

def fct(x,alpha=10,beta=11):
    print(x,alpha,beta)

fct(99) # la fct utilise les valeurs initiales de alpha et beta

fct(99,55,66) # en cas de besoin, on peut modifier les valeurs de alpha et beta

# Les params optionnels possèdent une valeur par défaut et sont définis à la suite des
# params obligatoires

# Appel d'une fonction avec des paramètres nommés sans tenir compte de leur position

fct(2,beta=11)
fct(beta=55,x=88)

print('test1', end=' ')
print('test2')

print(">>>>>>>>>>> Fonction avec un nombre variable de paramètres: ")

print(10,True,'test',10.5)

def somme_variable(*entiers: int):
    #print(type(entiers)) # tuple: liste en lecture seule
    s = 0
    for e in entiers:
        s += e

    return s

print(somme_variable(10,20,30))
print(somme_variable(10,20,30,40))
print(somme_variable(10,20,30,40,50))

print(">>>>>> Fonction qui renvoie plusieurs résutats:")
def calculs(x:int, y:int):
    s = x + y
    p = x * y
    return s,p

resultat = calculs(10,5)
print(type(resultat)) # tuple
print(resultat)

# Deballage (unpacking) d'un tuple:

sm,pr = resultat
print(f'somme = {sm} - produit = {pr}')

print(">>>>>>> Variable locale - variable globale:")

# b et c sont globales: visibles dans tout le script

b = 10
c = 10

def modifier():
    global b # demande explicite de manipulation du b global
    b = 15
    c = 15
    v = 11
    print("===============================================")
    print(locals())
    print("===============================================")

modifier()

print(f'b = {b}')
print(f'c = {c}')

print(globals())

print(">>>>>>>>>> Quelques fonctions natives de Python:")

lst = [10,20,30]
print(sum(lst))
print(min(lst))
print(max(lst))
print(len(lst)) # len(): renvoie la taille d'une collection
print(len('chaine'))
print(round(10.5111, 2))

print(">>>>>>>>>>>> Fonction qui prend en params une autre fonction:")

def add(x,y):
    return x+y

def soustraction(x,y):
    return x-y

def traitement(fct,x,y):
    return fct(x,y)

print(traitement(add,10,5))
print(traitement(soustraction,10,5))

my_list = [10,5,3,8,7,11]

def sup_a_5(x):
    return x > 5

print(list(filter(sup_a_5,my_list)))