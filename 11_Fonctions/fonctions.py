# fonction: est un ensemble d'instructions réutilisable
# fonction qui renvoie un résultat: input()
# fonction qui ne revoie aucun résultat: print()

# syntaxe:
# def nom_fonction(params):
#   instrcution1
#   instrcution2

# exemple d'un fonction:

def fonction1():
    print('fonction1..........')

fonction1()

# sans les 2 parenthèses: il s'agit d'une variable contenant l'id de la fct en mémoire
print(fonction1)

f = fonction1
f()

# exemple d'une fct avec params:

def repeter(texte, nombre_repetitions):
    for i in range(nombre_repetitions):
        print(texte)

repeter('hello', 5)

# exemple d'une fct qui renvoie un résultat

def carre(nombre):
    return nombre ** 2

r = carre(5)
print(r)

#print(carre('chaine'))

# Annotations de types depuis Python 3.5: mécanisme permettant de spécifier le type de params attendus par une fonction

i:int = 5
s:str = 'test'

i = 'test'
print(i)

# Le typage reste dynamique mm en pratiquant les annotations de types

# Bonne pratique: utiliser les annotations de types dans les fcts

def somme(a:int, b:int) -> int:
    return a+b

print('_____________ fonction avec des params optionnels:')

def fct(x, alpha=10,beta=11):
    print(x,alpha,beta)

fct(55) # la fct utilise les valeurs initiales de alpha et beta
fct(99,33,44) # en cas de besoin, on peut modifier les valeurs de alpha et beta

# les params optionnels, possèdent une valeur par défaut et sont définis à la suite des params recquis

# Appelle d'une fct avec des params nommés sont tenir compte de leur position

fct(beta=77,x=2)

def prix_ttc(prix_ht:float, tva:float = 0.2) -> float:
    return prix_ht * (1 + tva)

print(prix_ttc(80))
print(prix_ttc(80, tva=0.35))

print('test1', end=' ')
print('test2')

print('_____________ fonction qui renvoie plusieurs résultats:')

def calculs(a:int, b:int) :
    somme = a + b
    produit = a * b
    return somme,produit

result = calculs(10,15)
print(result)
print(type(result))

# unpacking du tuple
s,p = result
print('Somme =', s)
print('Produit =', p)

print('_____________ Fonction avec un nombre variable de params:')

print(10,'test',True)

def somme_variable(*entiers:int):
    #print(type(entiers)) -> entiers: est un tuple
    s = 0
    for e in entiers:
        s += e
    
    return s

somme_variable(10,12)

def my_func(*args, **kwargs):
    print(args) # args: tuple
    print(kwargs) # kwargs: dict
    

# le tuple contient les params anonymes
# le dict contient les params nommés
my_func(10,5,True, x=10,z=55)

def generate_dict(**kvargs):
    return kvargs

d = generate_dict(nom='DUPONT', prenom='Jean')
print(d)

def generate_list(*elements):
    return list(elements)
    
print(generate_list(15,48,75))

# Bonnes pratiques: langages objets
# 5 principes SOLID
# Single of responsablity
# Open/close: code ouvert à l'extenson mais fermé
# Liskov Subtitution: les objets enfants sont substituables aux objets parents
# Interfaces segrégation
# Dependency Inversion

print('>>>>>>>>>>>> variables locales - variables globales:')

b = 10
c = 10

def modifier():
    global b
    b = 15
    c = 15
    v = 12
    print('***************************************************')
    print(locals())
    print('***************************************************')

modifier()

print(f'b = {b} - c = {c}')

print(globals())

print("____________________ fonction en paramètre d'une autre fonction")

def add(x,y):
    return x+y

def soustraction(x,y):
    return x-y

def my_calculs(func,x,y):
    return func(x,y)

print(my_calculs(add,10,5))
print(my_calculs(soustraction,10,5))

# Expression Lambda: fonction anonyme: param1,param2 : instruction
# appelée aussi fonction à 1 seule instruction avec un return implicite

# A utiliser avec des fcts prenant en params d'autres fcts

print(my_calculs(lambda x,y : x*y, 10,5))

print('________________ fonctions natives de Python:')

# print()
# input()
# quit()

lst = [10,5,2,4,13]

print(len(lst))
print(sum(lst))
print(min(lst))
print(max(lst))
print(round(2.5897, 2))


def tri(x):
    return x >= 5

print("fonction explicite:",list(filter(tri, lst)))
print("expression lambda:",list(filter(lambda x : x >= 5,lst)))

result = sorted(range(-5,6), key=lambda x: x**2)
print(result)

e = (1,)
print(type(e))

print('__________________ yield:')

# Le mot clé yield est un outil puissant qui permet de créer des générateurs facilitant la gestion de grandes quantités
# sans surcharger la mémoire.
# Contrairement à return, le yield ne términe la fonction, il suspend son exécution et reprend là où elle s'était
# arrêtée.

def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1


counter = count_up_to(5) # avec un return dans fct, 5 objets sont déjà chargé en mémoire
# for v in counter:
#     print(v)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# sans boucle
def simple_generateur():
    yield 'première valeur'
    yield 'deuxiéme valeur'
    yield 'troisième valeur'

gen = simple_generateur()

print(next(gen))
print(next(gen))
print(next(gen))

# Quand utiliser yield au lien de return:
# A utiliser lorsqu'on traite des quantité importantes de données.
# Permet principalement d'économiser la mémoire

# Cas pratique: lecture d'un fichier volumineux ligne par ligne

def read_large_file(path):
    with open(path, 'r') as flux:
        #return flux.readlines() -> remplacer le return par yield -> 1 seule ligne à la fois
        for line in flux:
            yield line.strip()


line = read_large_file('11_Fonctions\\demo.txt')

print(next(line))
print(next(line))
print(next(line))
print(next(line))


for ligne in read_large_file('11_Fonctions\\demo.txt'):
    print(ligne)
