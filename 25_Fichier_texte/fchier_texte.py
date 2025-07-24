
# Etape1: construction du chemin

import os

print(__file__) # revoie le chemin du fichier en cours

chemin_dossier = os.path.dirname(__file__) # c:\.....\25_Fichier_Texte
chemin_fichier = os.path.join(chemin_dossier, 'demo.txt')


# Etape2: Appel de la fct open
# open()prend plusieurs params:
# - chemin du fichier
# - mode d'accés: r: read, w:write, a: append
# - encoding: 'utf-8'

flux = open(chemin_fichier, 'a', encoding='utf-8')
flux.write('\nContenu du fichier')
flux.close()


flux = open(chemin_fichier, 'r', encoding='utf-8')
contenu = flux.read()
flux.close()

print(contenu)

print(">>>>>>>>>>> Context Manager:")
# s'occupe de libérer les ressources à la fin du boc with

with open(chemin_fichier, 'r', encoding='utf-8') as flux:
    print(flux.read()) # vous arrivez à la fin du fichier
    #flux.close() -> plus nécessaire
    flux.seek(0)
    # whence = 0: partir du début du fichier
    # whence = 1: partir de la position actuelle du curseur
    # whence = 2: partir de la fin du fichier
    print('==================================')
    print(flux.read())
    print('==================================')
        

#print(flux.read()) 

print('>>>>>>>>>>>>> Test des fcts de lecture et écriture:')

import sys

# getcwd(): renvoie le chemin du dossier projet
chemin_projet = os.getcwd()
sys.path.append(chemin_projet)

from myhelpers.filehelper import lecture_fichier_texte,ecriture_fichier_texte

chemin_test = os.path.join(chemin_dossier, 'test.txt')

ecriture_fichier_texte(chemin_test, 'contenu du fichier', mode_ajout=True)
print(lecture_fichier_texte(chemin_test))

print(">>>>>>>>>>>>>> Module os:")

print(os.getcwd())

# Créer des répertoire:

chemin_rep = os.path.join(chemin_dossier, 'rep')

if os.path.exists(chemin_rep):
    print('dossier existe déjà........')
else:
    os.mkdir(chemin_rep)
    print('Dossier crée......')

print('>>>>>> Parcourir un rép:')

for f in os.listdir(chemin_dossier):
    print(f)

# Exo: lire tous les fichiers .txt du dossier en cours et extraire le contenu pour l'insérer dans new.txt
# Résultat attendu: contenu de new.txt
# >>>>>>>>>> nom du fichier lu
# contenu
# >>>>>>>>>> nom du fichier lu
# contenu