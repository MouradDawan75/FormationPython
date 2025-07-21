# Bloc conditionnel: est une ensemble d'instructions qui ne s'exécute que si une condition est vérifiée

age = 26

if age < 18:
   print('Mineur')
   print('Toujours mineur')

print('Tout âge')

if age < 18:
   print('mineur')
elif age <= 25:
   print('jeune adulte')
else:
   print('adulte')

# On peut aussi combiner des conditions en utilisant les opérateurs

if age >= 18 and age <= 25:
   print('Vous avez entre 18 et 25 ans')

# Syntaxe simplifiée pour 1 seul and:

if 18 <= age <= 25:
   print('jeune adulte')

# Un bloc vide n'est pas valide syntaxiquement:
# Le mot clé pass permet de définir un bloc vide valide syntaxiquement

if True:
   pass
   
print('suite........')

# Opérateur ternaire: syntaxe simplifiée d'un if/else classique

if age < 18:
   print('mineur')
else:
   print('majeur')

print('mineur') if age < 18 else print('majeur')

# On peut aussi l'utiliser pour faire une affectation conditionnelle

resultat = 'mineur' if age < 18 else 'majeur'

# Depuis Python 3.10, ajout du bloc match/case

note = 3

match note:
   
   case 0|1|2|3|4|5|6|7|8|9:
      print('En dessous de la moyenne')
   case 10|11|12|13:
      print('Juste la moyenne')

    # pour les autres cas: 2 syntaxes

   case other:
      print('Good job')

#    case _:
#       print('Good job....')

chaine_saisie = input('Entrez une valeur: ')

value = eval(chaine_saisie)

match value:
   
   case int():
      print('Valeur entière')
   case float():
      print('Valeur flottante')
   case complex():
      print('Valeur complèxe')
   case _:
      print('Valeur non numérique')

