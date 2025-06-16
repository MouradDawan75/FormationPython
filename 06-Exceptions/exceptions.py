# Il existe 3 types d'erreurs possibles dans un code:
# - Erreur de compilation (syntaxe): sont détectées automiquement par l'IDE
# - Exceptions: sont des erreurs qui provoquent l'arrêt de l'application
# - Code fonctionnel, qui renvoi un résultat inattendu

# Pour éviter l'arrêt de l'application, une exception doit être gérée
# Pour gérer une exception, on utilise le bloc try/except

# Il existe plusieurs types d'eceptions possibes, chacune d'elle porte le nom de l'erreur 
# qu'elle.
# Il existe aussi un type anonyme (générique) Exception

nb = 10


try:
    concatenation = 'chaine' + 5
    print(nb / 0)
    

except ZeroDivisionError:
    print('exception gérée........')
    # garder une trace dans un fichier  de logs

except TypeError:
    print('Exception concaténation gérée......')

print('suite du script...')

print('>>>>>>>>>>>>>> Type Exception générique:')

# Obligation: une ressource (fichier, base de données...) doit être libérée
# à la fin de son utilisation

# Bonne pratique: prévoir un try/except lors de la manipulation de ressources

nb = 10


try:
    print(nb / 2)
    concatenation = 'chaine' + '5'
    # Ouverture d'un fichier 

    

    
    
# Syntaxe simplifiée de:  except Exception as e:  
except:
    print('>>>>>>>>>>>> except..............') 
      

# except Exception as e:
#     print('exception générique........')
#     # garder une trace dans un fichier  de logs
#     print(e)

else:
    # bloc optionnel qui s'exécute seulement si aucune n'est générée dans le try
    print('>>> else')

finally:
    # bloc optionnel qui s'exécute tout le temps: exception ou pas
    print('>>> finally......')
    # Fermeture du fichier
    # Ce bloc, sert dans la pratique à fermer les ressources utilisées dans le try.

# Demandez la saisie d'un nombre valide
while True:
    nombre = input('Votre nombre: ')

    try:
        nombre = int(nombre)
        break

    except:
        print('Nombre invalide..........')

    # else:
    #     break 


print(nombre)