
class Animal:

    def __init__(self,nom,age):
        self.nom = nom
        self.age = age

    def emettre_son(self):
        print("Son de l'animal")


class Chat(Animal):
    
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur

    def dormir(self):
        print('Dormir chat............')

    # Overload: surcharge de fonction

    def emettre_son(self):
        print('Miauller..........')


class Chien(Animal):

    def emettre_son(self):
        print('Aboyer............')

a = Animal('a', 5)
a.emettre_son()

c = Chat('chat', 3, 'gris')
c.emettre_son()

# Une classe enfant, via l'héritage récupère tous les membres de la classe mère
# Une classe fille, en plus des attributs définis dans la classe mère, elle peut avoir des attributs qui lui sont spécifiques
# Une classe fille, en plus des fonctions définies dans la classe mère, elle peut avoir des fonctions qui lui sont spécifiques
# Une classe fille, en cas de besoin peut modifier les fcts définies dans la classe mère

chien =Chien('chien', 4)
chien.emettre_son()

# Polymorphisme: un objet peut prendre plusieurs formes
# C'est conséquence de l'héritage, c'est le fait que l'objet puisse prendre la forme de tous les objets enfants

print(isinstance(a, Animal))
print(isinstance(a, Chat))
print(isinstance(c, Chat))
print(isinstance(c, Animal))

# Collection polymorphique:

animaux:list[Animal] = []

animaux.append(a)
animaux.append(c)
animaux.append(chien)

# Fonction polymorphique

# Polymorphique par sous typage
def test(a:Animal):
    a.emettre_son()


# Polymorphisme AD-HOC
def test2(a):
    if a is Animal:
        a = Animal(a)
        a.emettre_son()


test(a)
test(c)
test(chien)

class Giraffe(Animal):
    pass


animaux.append(Giraffe('g', 6))
test(Giraffe('g', 5))

print('>>>>>>>>>>>>>>>> Héritage multiple:')

class Cat:

    def meow(self):
        print('Weoh....')

class Talker:

    def say(self, text):
        print(text)


class TalkerCat(Cat,Talker):
    pass

tc = TalkerCat()
tc.meow()
tc.say('miaou..........')

print('******************************************************************')

class Cat:

    def __init__(self,name):
        self.name = name+ ' Cat'

    def parler(self):
        print('miaou............')


class Talker:

    def __init__(self, name):
        self.name = name +' Talker'

    def parler(self):
        print('miauller..........')


class TalkingCat(Cat,Talker):

    def __init__(self, name):
        #super().__init__(name) # super(): réference la plus a gauche par défaut
        Talker.__init__(self,name)

    def parler(self):
        #super().parler() # super(): réference la plus a gauche par défaut
        Talker.parler(self) # MRO: Method Resolution Order


print('MRO:', TalkingCat.__mro__)

tc = TalkingCat('name')
print(tc.name)
tc.parler()