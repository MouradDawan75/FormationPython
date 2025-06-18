# Etape1: construction du chemin

# chemin_fichier = 'c:\......'

import os

print(__file__) # chemin du fichier en cours: c:\....\txt_files.py

chemin_dossier_en_cours = os.path.dirname(__file__) # Directry Name: c:\...\16-txt_files

#chemin_fichier = chemin_dossier_en_cours +"\demo.txt"

# join: génère un chemin valide selon l'os utilisé: Windows, Mac, Linux
chemin_fichier = os.path.join(chemin_dossier_en_cours, 'demo.txt') 

# Etape2: appel de la fonction open()
# La fonction open prends plusieurs params:
# - chemin du fichier
# - mode d'accès: r: read, w: write, a: append 
#   (en mode w et a) si le fichier n'existe pas, il sera crée par la fonction
# - encoding: utf-8

flux = open(chemin_fichier, 'a', encoding='utf-8')
flux.write('\ncontenu du fichier.....')
flux.close()

flux = open(chemin_fichier,'r', encoding='utf-8')
contenu = flux.read()
flux.close()

print(contenu)

print('---------Module os:')

print(os.path.exists(chemin_fichier))
print(os.getcwd()) # Get Current Working Directory

# Créer un répertoire:
chemin_dossier = os.path.join(chemin_dossier_en_cours, 'rep')

if os.path.exists(chemin_dossier):
    print('Dossier existant')
else:
    os.mkdir(chemin_dossier) # Make Directory

# Lister le contenu d'un répertoire:

for f in os.listdir(chemin_dossier_en_cours):
    print(f)