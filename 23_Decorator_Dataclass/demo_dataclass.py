# syntaxe de base

class Foo:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


f = Foo(1,'b', True)
f1 = Foo(1,'b', True)

print(f.__dict__)
print(f) # pas de fct __str__
print(f == f1) # pas de fct __eq__

print('>>>>>>>>>>>>>>> dataclass decorator:')

from dataclasses import dataclass

@dataclass
class Post:
    a: int
    b: str
    c: bool

    # possibilité de surcharger __str__ et __eq__

p1 = Post(1,'b', True)
p2 = Post(1,'b', True)

print(p1.__dict__)
print(p1)
print(p1 == p2)

# @dataclass: __init_, __str__ et __eq__ implémentés

print('>>>>>>>>>>>>> Ajout de paramètres au décorateur:')

#order: permte d'ajouter les autres fcts de comparaison: __lt__, __gt__, __le__, __ge__, __ne__

@dataclass(order=True)
class Blog:
    a: int
    b: str

b1 = Blog(1, 'a')
b2 = Blog(1, 'b')

print(b1 > b2)
print(b1 >= b2)
print(b1 < b2)
print(b1 <= b2)
print(b1 != b2)

# frozen: True -> permet de créer des instances immaubles -> attributs non modifiables

print('>>>>>>>>>>>>> configuration des attributs:')

from dataclasses import field, fields

@dataclass
class Test:

    a: int = field(repr=False)
    b: str

t = Test(5, 'b')

print(t)

print(fields(t))

print('>>>>>>>>>>>>> Les attributs de classe:')

from typing import ClassVar

@dataclass
class Prod:
   
    a:int
    b:str
    c:ClassVar[bool] = False
    d: bool = field(init=False)

    def __post_init__(self):
        print('___post_init')
        self.d = len(self.b) > self.a


p1 = Prod(1, 'p1')
p2 = Prod(2, 'p2')

print(p1.c)
print(p2.c)

print(Prod.c)

Prod.c = True

print(p1.c)
print(p2.c)