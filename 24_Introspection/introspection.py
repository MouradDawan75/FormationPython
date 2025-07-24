print('>>>vérification du type:')

data = "chaine"
print(isinstance(data, str))
print(issubclass(str, object))
print(issubclass(str, int))
print(type(data))

print(">>>Attributs d'un objet:")

print(hasattr(data,"upper"))
print(hasattr(data,"manger"))
print(getattr(data,"upper"))

class Foo:

    def __init__(self,a,b):
        self.a = a
        self.b = b

f = Foo(1, 'b')

print(hasattr(f, 'a'))
print(getattr(f, 'a'))

print(f.__dict__)
print(vars(f)) # equivalent de f.__dict__

import sys

print(sys.getsizeof(f))

import inspect

# Fonctions pour le type

# inspect.ismodule()
# inspect.ismethod()
# inspect.isfunction()
# inspect.isgenerator()
# inspect.isbuiltin()
# inspect.isclass()

data = 'test'

# Fonction pour les objets:
# inspect.getmembers()
inspect.getmembers(data, inspect.ismethod)
# inspect.getmembers_static() -> attributs de classe

# Fonction pour la doc:

print(inspect.getdoc(data))
# inspect.getcomments()
# inspect.getdoc()
# inspect.getsource()