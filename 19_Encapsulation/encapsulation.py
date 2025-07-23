
# En procédural:

def surface(hauteur,largeur):
    return hauteur * largeur

h = 10
l = 15

r = surface(h,l)

# Encapsulation:
# 1- Regrouper dans une seule et mm classe tous les params et toutes les fcts qui concernent le mm sujet
# 2- Pas d'accès publique aux attributs d'une classe. L'accès passe forcément par les accésseurs (get/set)


class Rectangle:

    def __init__(self, hauteur, largeur):
        #self.set_hauteur(hauteur) #self.__hauteur = hauteur
        #self.set_largeur(largeur)#self.__largeur = largeur
        self.hauteur = hauteur
        self.largeur = largeur

    def __get_hauteur(self):
        return self.__hauteur
    
    def __set_hauteur(self,value):
        if value <= 0:
            raise ValueError('Hauteur doit être positive.......')
        self.__hauteur = value

    def __get_largeur(self):
        return self.__largeur
    
    def __set_largeur(self,value):
        self.__largeur = value

    hauteur = property(__get_hauteur, __set_hauteur,None, """""")
    largeur = property(__get_largeur,__set_largeur, None, """""")

    def surface(self):
        return self.hauteur * self.largeur
    

rec = Rectangle(10,15)

print('>>>>>>>>>>>>>>>>>> Syntaxe simplifiée..............')

class NewRectangle:

    

    def __init__(self, hauteur,largeur):
        self.hauteur = hauteur
        self.largeur = largeur

    @property # par défaut c'est le getter
    def hauteur(self):
        return self.__hauteur
    
    @hauteur.setter
    def hauteur(self, value):
        if value <= 0:
            raise ValueError('Hauteur positive............')
        self.__hauteur = value

    @hauteur.deleter
    def hauteur(self):
        del self.__hauteur

    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self,value):
        self.__largeur = value


rec2 = NewRectangle(10,15)

print(rec2.hauteur)

del rec2.hauteur

print(rec2.largeur)
print(rec2.hauteur)



