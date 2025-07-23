# Une classe abstraite est une classe non instanciable

class Homme:

    def __init__(self, nom,prenom):
        self.nom = nom
        self.prenom = prenom



class Femme:

    def __init__(self, nom,prenom):
        self.nom = nom
        self.prenom = prenom


from abc import ABC, abstractmethod # ABC: Abstract Base Class

class  Personne(ABC):

    def __init__(self, nom,prenom):
        self.nom = nom
        self.prenom = prenom

    @abstractmethod
    def identite(self):
        raise NotImplemented('..........')


class Homme(Personne):
    
    def identite(self):
        print('Homme.......')


class Femme(Personne):
    
    def identite(self):
        return super().identite()


p = Homme('n', 'p')


