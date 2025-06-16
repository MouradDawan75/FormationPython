age = 50
prenom = 'Marie'

# Affichage attendu: Prénom: Marie Age: 50

# Concaténation:

print('Prénom: '+prenom+' Age: '+str(age))

# Utiliser la virgule comme séparateur:
# Pas besoin de faire des conversions en str, de plus, la virgule génère un espace

print('Prénom:',prenom,'Age:',age)

# A partir de Python 3: ajout de la fonction de format

print("Prénom: {} Age: {}".format(prenom,age))

# A partir de Python 3.6: ajout fstring -> syntaxe simplifiée de la fonction format

print(f"Prénom: {prenom} Age: {age}")
# Entre accoldes:
# On peut soit insérer des variables, soit des expressions

print(f"{3 + 5}") # exemple d'une expression
print(f"{int(12.99)}") # autre expression

# Caractères d'echappement:
# \n: retour à la ligne -> new ligne
# \r: retour à la ligne -> return
# \t: tabulation
# \s: space
# \b: back space
# \\: ignorer le back slash
# \": ignorer les "

print('\tceci est une\nchaine sur plusieurs\nlignes.')

chemin = 'c:\\test\\notes.txt'

print(chemin)

chaine = "ceci est un \"exemple\" de texte"
print(chaine)

print(">>>>> Chaine multilignes:")

# chaine verbatime:

print("""
    Ceci est une
chaine sur plusieurs
lignes.
""")