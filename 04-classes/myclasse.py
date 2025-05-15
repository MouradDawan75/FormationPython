# approche procédurale: repose sur l'utilisation des paramètres et des fonctions
# approche objets: repose sur l'utilisation de classes et d'objets

# Une classe est un type de données. Sa tâche principale est de décrire la structure d'un objet.
# Elle définie une sorte à partir duquel on crée nos objets.

# Elle principalement 3 choses:
# - Attributs - propriétés
# - fonctions
# - fonction spéciale appelée construteur (initialisateur) qui porte le nom de la classe permettant d'instancier la classe

class User:

    # attribut de classe: partagé par l'ensemble des objets

    profil = 'admin'

    # attributs d'instance: spécifiques à chaque
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        print('*********')
        # self: mot clé qui pointe vers la variable en cours d'utilisation

    # fonction d'instance: est une fonction qui concerne une instance particulière
    def afficher_nom(self):
        print(self.nom)

    @classmethod
    def modifier_profil(cls, nom_profil):
        cls.profil = nom_profil



# Code exécuté par Python:
#u1 = User.__init__(u1, 'DUPONT', 'Jean')

u = User('DUPONT', 'Jean')
u.afficher_nom()

print(u.prenom)

print(User.profil)


User.modifier_profil('manager')


# Conventions de nommage:

# variables et méthode: snake_case
# classes: PascalCase: CompteBancaire

class CompteBancaire:

    # attribut de classe
    banque = 'BNP'

    def __init__(self, numero, solde):
        self.numero = numero
        self.solde = solde

    def depot(self, montant):
        self.solde += montant


    def retrait(self, montant):
        self.solde -= montant

    @classmethod
    def modifier_banque(cls, nom_banque):
        cls.banque = nom_banque



cpt = CompteBancaire('1258dsf', 1500)
cpt1 = CompteBancaire('sdqs458', 4500)

print(cpt.banque)
print(cpt1.banque)

CompteBancaire.modifier_banque('LCL')

print(cpt.banque)
print(cpt1.banque)