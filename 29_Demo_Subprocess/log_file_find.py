
from argparse import ArgumentParser
import os

chemin_dossier = os.path.dirname(__file__)


def find_lines_in_log_file():

    print(chemin_dossier)

    

    try:
        parser = ArgumentParser()
        parser.add_argument('chemin_fichier_logs', type=str)
        parser.add_argument('chemin_fichier_sortie', type=str)
        parser.add_argument('mot_recherche', type=str)

        params = parser.parse_args()
        mot_recherche = params.mot_recherche
        chemin_fichier_logs = params.chemin_fichier_logs
        chemin_fichier_sortie = params.chemin_fichier_sortie

        mot_recherche = mot_recherche.upper()
        liste_lignes = []
        with open(os.path.join(chemin_dossier, chemin_fichier_logs),'r', encoding='utf-8') as flux:
            lignes = flux.readlines()
            for ligne in lignes:
                index = ligne.find(mot_recherche)
                if index != -1:
                    liste_lignes.append(ligne)

        if liste_lignes:
            with open(os.path.join(chemin_dossier, chemin_fichier_sortie), 'w', encoding='utf-8') as flux:
                flux.writelines(liste_lignes)

        else:
            print(f'Le mot {mot_recherche} non trouvé.........')



    except:
        raise Exception('Chemin invalide ou paramètres invalides.........')
    

if __name__ == '__main__':
    find_lines_in_log_file()