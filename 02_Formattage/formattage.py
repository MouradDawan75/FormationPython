age = 60
prenom = 'Marie'

# Chaine a construire: Prénom: Marie Age: 60

print(">>>>>>Concaténation:")

print('Prénom: '+prenom+" Age: "+str(age))

print(">>>>>> Utiliser la virgule comme séparateur:")

print('Prénom:',prenom,'Age:',age) # pas besoin de conversion en str, de plus la virgule génère un éspace

# A partir de Python 3, ajout de la fonction format:

print('Prénom: {} Age: {}'.format(prenom,age))

# A partir de Python 3.6: ajout de fstring -> syntaxe simpifiée de la fct format

print(f'Prénom: {prenom} Age: {age}')

print(f'{3 + 5}') # exemple d'une expression
print(f'{3 + 5 = }') # exemple d'une expression avec égale

print(">>>>>>>>> Caractères d'echappement")

# \n: retour à la ligne
# \t: tabulation
# \s: space
# \b: back space

print("\tCeci est une chaine\nsur plusieurs\nlignes.")

chemin = "c:\\test\\notes.txt"
chemin2 = r"c:\test\notes.txt" # raw string - chaine brute

print(chemin2)

print('>>>>> DocString:')

# pratique pour les chaines multilignes

print("""
    Ceci est une
chaine sur plusieurs
lignes.
""")