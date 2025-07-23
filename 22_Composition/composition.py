
class Adresse:

    def __init__(self,num,street):
        self.num = num
        self.street = street


class Client:

    def __init__(self,nom:str, adresse:Adresse):
        self.nom = nom
        self.adresse = adresse

    def test(self):
        pass

    def test(self, a):
        pass


# Composition (association): un objet de type Adresse qui fait partie des attributs d'un objet de type Client
c = Client('Carrefour', Adresse('10', 'rue Machin 75015 Paris'))

# Composition: utilisée pour réduire la dépendance entre les objets.
# Remplacer l'héritage par une composition
