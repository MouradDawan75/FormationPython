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



