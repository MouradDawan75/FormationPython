
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

# Créer des répertoires:

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

chemin_new = os.path.join(chemin_dossier, 'new.txt')
contenu_final = ''

for f in os.listdir(chemin_dossier):

    if f.endswith('.txt'):
        chemin = os.path.join(chemin_dossier, f)
        contenu_final += '>>>>>>> Fichier: '+f+'\n'+lecture_fichier_texte(chemin)+'\n'

if contenu_final:
    ecriture_fichier_texte(chemin_new, contenu_final)
else:
    print('Aucun fichier trouvé...............')


from myhelpers.filehelper import check_permission

check_permission(chemin_new)

print(">>>>>>>>>> module pathlib:")

from pathlib import Path

dossier_utilisateur = Path.home()
print(dossier_utilisateur)

print(Path.cwd()) # dossier projet

documents = Path('/Users/oem/Documents')

print(documents)

print('>>>>>> join:')

# 2 syntaxes pour le join

home = Path.home()
documents = home / 'Documents'

home.joinpath('Documents')

print('>>>>>>>> infos fichiers:')

fichier = Path('/Users/oem/Documents/path.txt')

print(fichier.name)
print(fichier.parent)
print(fichier.suffix) # extension
print(fichier.parts)
print(fichier.stem) # nom sans extension

print(fichier.exists())
print(fichier.is_dir())
print(fichier.is_file())

print('>>>>>>>>>>>>> lecture et écriture avec pathlib:')

fichier = Path('/Users/oem/Documents/test.txt')
fichier.write_text('contenu du fichier........')


print(fichier.read_text())

print('>>>>>>>>>>>>> Parcourir un rép:')

rep = Path('/Users/oem/Documents')

for f in rep.iterdir():
    print(f.name)

# ajout d'un filtre
# fichier .txt

print('>>>>>>>> glob: pour filtrer')

for f in rep.glob('*.txt'):
    print(f.name)

print('>>>>>>>> rglob: ')

# scanner de façon récursive un rep

for f in rep.rglob('*.txt'):
    print(f.name)


print(">>>>>>>>>>>>>>> lecture binaire:")

with open(os.path.join(chemin_dossier, 'exemple.bin'), 'rb') as flux:
    data = flux.read()

print(data)

print(data.decode('utf-8'))

# lecture image

with open(os.path.join(chemin_dossier, 'dawan.png'), 'rb') as flux:
    data = flux.read()


print(data[:100])

# pip install pillow

from PIL import Image
import io

with open(os.path.join(chemin_dossier, 'dawan.png'), 'rb') as flux:
    image_data = flux.read()


image = Image.open(io.BytesIO(image_data))

image.show()



