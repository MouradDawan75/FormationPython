# pip install pyside6

# module Python permettant d'utiliser le frameworg Qt pour créer des interfaces graphiques

# 2 classes principales dans PySide6:
# QApplication: pour créer l'appication
# QWidget: classe mère de tous les Widgets

# Possibilité d'utiliser Qt Designer pour créer des interfaces qui se trouve dans le dossier PySide6

# Dans Vs Code, installer l'extension Qt for Python

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QTranslator, QLocale
from PySide6 import QtCore
from main_ui import Ui_Form

import sys,os

sys.path.append(os.getcwd())

from myhelpers.filehelper import lecture_fichier_texte, ecriture_fichier_texte



class FenetrePrincipale(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()

        transtate =QTranslator()
        transtate.load('34_Demo_Pyside/words.txt')
        app.installTranslator(transtate)
        

        # application du design généré
        self.setupUi(self)

        # connecter le bouton valider à la fct somme
        self.btnValider.clicked.connect(self.somme)

        # gestion du btnEcriture
        self.btnEcriture.clicked.connect(self.ecriture_fichier)

        # gestion du btnLecture
        self.btnLecture.clicked.connect(self.lecture_fichier)

    
    #définir une fonction pour chaque besoin fonctionnel
    def somme(self):
        nb1 = float(self.lineEdNombre1.text())
        nb2 = float(self.lineEdNombre2.text())
        somme = nb1 + nb2

        self.lblResultat.setText('Somme = '+str(somme))

    def ecriture_fichier(self):
        contenu = self.champsMultiLignes.toPlainText()
        dialog = QFileDialog()
        dialog.setNameFilters(['Fichiers texte (*.txt)', 'Tous les fichiers (*.*)'])
        resultat = dialog.exec() # renvoie 1: si fichier sélectionné sinon 0

        messageDialog = QMessageBox()
        messageDialog.setIcon(QMessageBox.Icon.Information)
        messageDialog.setWindowTitle('Sauvegarde')

        if resultat:
            chemin = dialog.selectedFiles()[0]
            ecriture_fichier_texte(chemin,contenu)
            messageDialog.setText(f'Fichier sauvegardé dans {chemin}')
            messageDialog.exec()
        else:
            messageDialog.setText('Sauvegarde annulée')
            messageDialog.exec()

    def lecture_fichier(self):

        dialog = QFileDialog()
        dialog.setNameFilters(['Fichiers texte (*.txt)', 'Tous les fichiers (*.*)'])
        resultat = dialog.exec()

        
        if resultat:
            chemin = dialog.selectedFiles()[0]
            contenu = lecture_fichier_texte(chemin)
            self.champsMultiLignes.setPlainText(contenu)
        else:
            messageDialog = QMessageBox()
            messageDialog.setIcon(QMessageBox.Icon.Information)
            messageDialog.setWindowTitle('Lecture fichier texte')
            messageDialog.setText('Aucun fichier sélectionné.......')
            messageDialog.exec()

            

    



app = QApplication()

theme = os.path.join(os.path.dirname(__file__), 'Adaptic.qss')
style_file = QtCore.QFile(theme)

style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)

style = style_file.readAll()

app.setStyleSheet(str(style, encoding='utf-8'))

# fenetre = QWidget()

# fenetre.show()
locale = QLocale('en')
QLocale.setDefault(locale)

f = FenetrePrincipale()

f.show()


app.exec()

# Internationalisation: I18N -> https://geekscoders.com/internationalization-in-python-pyqt6/

# Thèmes QT: https://qss-stock.devsecstudio.com/templates.php


