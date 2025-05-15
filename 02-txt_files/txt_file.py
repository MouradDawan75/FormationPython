# Etape1: construire le chemin du fichier

# chemin_fichier= 'c:\.......'

import os # nécessaire pour la gestion des paths
chemin_dossier = os.path.dirname(__file__) # c:\...\02-txt_files

# chemin_fichier = chemin_dossier +"/demo.txt"

chemin_fichier = os.path.join(chemin_dossier, 'demo.txt') # join: génère un path valide selon l'os utilisé

# Etape2: appeler la fonction open qui prend plusieurs paramètres
#  - chemin du fichier
#  - mode d'accès: r: read
#                 w: write
#                 a: append  
#    En mode écriture (w,a): si le fichier inexistant - il est crée par a fonction open
# - Encodage des caractères: utf-8

# Obligation: une ressource (fichier, BD) doit être libérée à la fin de son utilisation

# Stream (flux): est une sorte de canal intermédiaire entre une source et une destination

# Ecriture dans un fichier

flux = open(chemin_fichier,'w', encoding='utf-8')
flux.write('contenu du fichier')
flux.close()

# Lecture d'un fichier

flux = open(chemin_fichier,'r', encoding='utf-8')
contenu = flux.read()
flux.close()

print(contenu)

print(">>>>>>>>>>>>>>> Context Manager <<<<<<<<<<<<<<<<<<<<<")
# Context Manager (with resource): s'occupe de libérer la ressource à la fin de son  utilisation

with open(chemin_fichier,'r', encoding='utf-8') as fichier:
    print(fichier.read()) # vous arrivez à la fin du fichier. La prochaine lecture n'aura aucun caractère à lire
    # fichier.close() -> ligne exécutée par le with
    fichier.seek(0) # remettre le curseur au début du fichier
    # fichier.seek(5) -> renvoie le 6ème caractère -> index commence à 0
    # whence: 0 -> partir du début du fichier
    # whence: 1 -> partir de la fin du fichier
    # whence: 2 partir  de la position actuelle du curseur 
    print(">>>>>>>>>>>>>>>>>>>>>>>>")
    print(fichier.read())
    print(">>>>>>>>>>>>>>>>>>>>>>>>")

#print(fichier.read())

import threading
import time

def tache(name):
    # simuler une tâche lente
    time.sleep(2)
    print('Thread:',name,'Thread name:',threading.current_thread().name, 'Processus ID', os.getpid())

x = (1,)

t1 = threading.Thread(target=tache, args=('tache1',))
t2 = threading.Thread(target=tache, args=('tache2',))

t1.start()
t2.start()

t1.join() # join mets en attente le thread principal
t2.join()

print('tâche principale.........', threading.current_thread().name, 'Processus ID', os.getpid())