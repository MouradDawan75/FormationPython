# approche procédurale: repose sur l'utilisation de params de fonctions
# approche objets: repose sur l'utilisation de classes et d'objets

# Une classe est un type de données. Elle définie une sorte de template à partir duquel on crée nos objets.
# Sa tâche principale est de décrire a structure d'un objet.
# Elle contient généralement 3 chose:
# - Les attributs de l'objet
# - Des fonctions
# - Fonction spéciale qui porte le nom de la classe appelée constructeur (initialisateur).
# Méthode permettant d'instancier une classe

class User:

    #attributs de classe: attributs partagés par toutes les instances
    profil = 'ADMIN'

    # attributs d'instance
    def __init__(self, nom,prenom):
        #self: mot clé qui pointe vers l'objet en cours d'utilisation
        self.nom = nom
        self.prenom = prenom 
        print('___________init_______________')

    # fonction d'instance
    def full_name(self):
        print(self.nom+" "+self.prenom)

    @classmethod
    def modifier_profil(cls, nom_profil):
        cls.profil = nom_profil

    @staticmethod
    def test():
        print('static méthode...........')

#code exécuté par Python en arrière plan
#User.__init__(u1, 'DUPONT', 'Jean')
u1 = User('DUPONT', 'Jean')
u1.full_name()

u2 = User('FEDERER', 'Roger')

print(u1.profil)
print(u2.profil)

print(User.profil)

User.modifier_profil('MANAGER')

print(u1.profil)
print(u2.profil)

User.test()

class GestionUser:

    @staticmethod
    def insert(u:User):
        print('user inséré en BD.........')


GestionUser.insert(u1)
GestionUser.insert(u2)

# Le principe de la décoration en Python est d'appliquer un décorateur à une fct afin de retourner un nouvel (une fct généralement)
# Un decorator est une fct qui prend en params une autre fct et qui renvoie une nouvelle



def decorator(f):
    print('Nom de la fonction:',f.__name__)
    return f

@decorator
def add(x,y):
    return x+y

print(add(10,5))

def print_decorator(func):

    def new_function(a,b):
        print(f'Addition des nombres {a} et {b}')
        result = func(a,b)
        print(f'Retour: {result}')
        return result
    
    return new_function # un decorator renvoie toujours une fonction

@print_decorator
def somme(x,y):
    return x+y

print(somme(10,15))

def generic_decorator(func):

    def new_function(*args, **kwargs):
        print(f'Appel de la fonction {func.__name__} avec agrs = {args} et kwargs = {kwargs}')
        result = func(*args, **kwargs)
        print(f'Retour: {result}')
        return result
    
    return new_function

@generic_decorator
def test(x,y,z,w):
    pass

test(15,12,z=11,w=55)

class CompteBancaire:

    banque = "BNP"

    def __init__(self,numero,solde):
        self.numero = numero
        self.solde = solde

    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            raise Exception('Solde insuffisant........')
        
    def depot(self, montant):
        self.solde += montant

    @classmethod
    def changer_banque(cls, nom_banque):
        cls.banque = nom_banque

    # __str__: permet de personnaliser l'affichage - choisir attributs à afficher
    def __str__(self):
        return f'Numéro: {self.numero} - Solde: {self.solde}'
    
    def __eq__(self,other):
        return self.numero == other.numero
    
    def __gt__(self,other): pass # > Greater Than
    def __ge__(self,other): pass # >= Greater equal
    def __lt__(self,other): pass # < less than 
    def __le__(self,other): pass # <= less equal
    def __ne__(self,other): pass # != not equal

    #destructeur: focntion appelée lors du passage du Garbage Collector
    def __del__(self):
        print('>>>>>>>> destructeur......')



c1 = CompteBancaire('qsds145', 500)
c1.depot(1000)
c1.retrait(150)

print(c1)

c2 = CompteBancaire('145fgt', 1500)
c3 = CompteBancaire('145fgt', 999)

print(c2 == c3)
print(c2 is c3)
print(id(c2))
print(id(c3))

print(c2.__dict__)
print(c2.__class__)

# 2 syntaxes pour détruire un objet en mémoire
del c1
c2 = None

# Concepts Objets: Encapsulation - Héritage - Polymorphisme - Abstraction - Composition (Association)






