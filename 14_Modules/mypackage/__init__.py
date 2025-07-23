print('___________________init.py')

# import os

# SERVER = os.environ.get('SERVER_IP')
# USER = os.environ.get('USER')
# PASSWORD = os.environ.get('PASSWORD')
# PORT = os.environ.get('PORT')

# permet de gérer l'initialisation d'un package 
PACKAGE_VESRION = '1.0'

# Appelle d'une fonction d'initialisation d'une connexion à une BD
from .module1 import fonction1

fonction1()

# La gestion des imports: modules et fonctions

from .module2 import fonction3
__all__ = ['module1', 'fonction3'] # niveau package -> liste des modules et fcts exportables via from mypackage import *


