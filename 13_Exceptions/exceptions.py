# il existe 3 types d'erreurs possibles:
# - erreurs de compilation: détectées automatiquement par l'IDE
# - exception: erreur qui provoque l'arrêt de l'application
# - code fonctionnel qui renvoi un résutlat inattendu -> faire debbugage

# pour éviter l'arrêt de l'application, un exception doit être gérée
# pour gérer une exception on utilise le bloc try-except

# Il existe plusieurs types d'exceptions, chacune d'elle porte le nom de l'erreur qu'elle génère.
# Il aussi un type anonyme (générique) appelé Exception

x = 10

try:
    s = 's' + 5
    print(x / 0)
    
except ZeroDivisionError:
    print('exception gérée........')

except TypeError:
    print('exception concaténation gérée.........')

print('suite du script............')

print('>>>>>>>>>>>>>>>>>>> Exception générique:')

x = 10

# Obligation: une ressource (fichier, BD....) doit être fermée à la fin de son utilisation 

# Bonne pratique: prévoir un try/except lors de manipulation de ressources

try:
    s = 's' + '5'
    print(x / 2)
    # ouvertue d'un fichier
    

# syntaxe simplifiée except Exception:
except:
    print('exception générique..............')

else:
    # bloc optionnel qui s'exécute si aucune erreur dans le try
    print('bloc else..........;')

finally:
    # bloc optionnel qui s'exécute tout le temps
    print('>>>>>>>> bloc finally...........')
    # fermeture du fichier
    # sert dans la pratique à libérer les ressources utilisées dans le try
     
    
# except Exception as e:
#     print('exception générique..............')
#     print(e)

def division(x):
    """ Fonction qui génère une exception si x = 0  """
    #option1: la fct gère sa propre exception
    # try:
    #     print(10/x)
    # except:
    #     print('exception gérée par la fct...........')

    # option2: faire une remontée d'exception - les appelants doivent gérer l'exception
    if x != 0:
        print(10/x)
    else:
        raise Exception('Attention, tentative de division par 0')
    

try:
    division(0)
except Exception as e:
    print(e)


print("_________________ test de l'exception perso:")

from mes_exceptions import AucunChiffreException

def conversion(s):

    if not s.isdigit():
        raise AucunChiffreException(s,"conversion")
    
    return int(s)

try:
    s = '123a'
    i = conversion(s)
except Exception as e:
    print(e)

print('_______________ ExceptionGroup')

# Depuis Python 3.11, ajout de ExceptionGroup

try:
    raise ExceptionGroup('Exception group pour de multiples erreurs', (
        ValueError('value error'),
        TypeError('TypeError'),
        KeyError('KeyError')
        
        ))
except KeyError as e:
    raise e
except (ValueError, TypeError) as err:
    raise err

def write_to_file(exceptions, file_name) :
    with open(file_name, 'w') as flux:
        for exception in exceptions:
            flux.write(exception)

# openAI: pip install openai
# gpt: pout le traitement de texte
# dalle-e: traitement d'image
# whisper: traitement de la voix 




