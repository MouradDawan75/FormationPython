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