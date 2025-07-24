"""
Ce module est une bibliothèque de focntions.....
Le module documentation contient des fcts.........
"""

print(__doc__)


def fct():
    """
    Une fct à titre d'exemple
    On peut documenter nos focntions comme ceci
    """

    print('>>>> fct.....')

print(fct.__doc__)
    


import math


print(dir(math))

print('>>>>>>>>>>>>>>>>>>>> __doc__ et help:')

print(math.__doc__) # doc du module
print(help(math))

print(math.sqrt.__doc__) # doc d'une fct
print(help(math.sqrt))

# Il existe 3 syntaxes pour la docstring

"""
DocString de type EpyText
@param param1: décrire param1
@param param2: décrire param1
@return: décrire ce qui retourné
"""


"""
DocString de type reST
:param param1: décrire param1
:param param2: décrire param1
:return: décrire ce qui retourné
"""


"""
DocString de type Google - recommandée car plus lisible

Args:
    param1: décrire param1
    param2: décrire param1

Returns:
    décrire ce qui retourné
"""

# Dans Vs Code, installez l'extension autoDocstring

def addition(x:int, y:int) -> int:
    """Fonction qui additionne 2 entiers

    Args:
        x (int): est un entier
        y (int): est un entier

    Returns:
        int: somme de x et y
    """
    return x+y

# Testez le module pydoc de Python
# Dans le terminal, tapez la commande: python -m pydoc

# pip install pdoc
# commande pour générer la doc html:
# pdoc 30_Documentation//documentation.py -o docs

# Command-line interface
# pdoc includes a feature-rich "binary" program for producing HTML and plain text documentation of your modules. 
# For example, to produce HTML documentation of your whole package in subdirectory 'build' of the current directory,
#  using the default HTML template, run:

# pdoc --html --output-dir build my_package
# If you want to omit the source code preview, run:

# $ pdoc --html --config show_source_code=False my_package