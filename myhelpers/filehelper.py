# fonction de lecture d'un fichier texte


def lecture_fichier_texte(chemin:str) -> str:
    try:
        with open(chemin,'r', encoding='utf-8') as flux:
            contenu = flux.read()

        return contenu

    except:
        raise Exception('Chemin invalide...........')

# fonction d'écriture dans un fichier 

def ecriture_fichier_texte(chemin:str, contenu:str, mode_ajout:bool=False):

    mode = 'w'
    if mode_ajout:
        mode = 'a'
        contenu = '\n'+contenu
    try:
        with open(chemin,mode, encoding='utf-8') as flux:
            flux.write(contenu)


    except:
        raise Exception('Chemin invalide...........')
    
import os

def check_permission(chemin:str):
    if os.access(chemin, os.R_OK):
        print('Lecture OK')

    if os.access(chemin, os.W_OK):
        print('écriture OK')

    if os.access(chemin, os.X_OK):
        print('fichier exécutable')

    if os.access(chemin, os.F_OK):
        print('fichier existe')
        