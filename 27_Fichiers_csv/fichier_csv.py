import os
import csv

chemin_csv = os.path.join(os.path.dirname(__file__), 'demo_file.csv')

# Lecture csv

contenus = []

with open(chemin_csv, 'r', encoding='utf-8') as flux:
    curseur = csv.reader(flux,delimiter=',')

    for ligne in curseur:
        contenus.append(ligne)

#print(contenus[0]) -> est une liste de listes, où chaque liste est une ligne du csv

# Ecriture csv

chemin_copie = os.path.join(os.path.dirname(__file__), 'copie.csv')

with open(chemin_copie, 'w', encoding='utf-8') as flux:
    curseur = csv.writer(flux,delimiter=';',lineterminator='\n')
    # contenu à fournir: soit 1 liste soit une liste de listes

    for ligne in contenus:
        curseur.writerow(ligne)