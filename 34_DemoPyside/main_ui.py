# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(873, 709)
        self.lineEdNombre1 = QLineEdit(Form)
        self.lineEdNombre1.setObjectName(u"lineEdNombre1")
        self.lineEdNombre1.setGeometry(QRect(390, 170, 113, 22))
        self.lineEdNombre2 = QLineEdit(Form)
        self.lineEdNombre2.setObjectName(u"lineEdNombre2")
        self.lineEdNombre2.setGeometry(QRect(390, 210, 113, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 180, 49, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 210, 49, 16))
        self.btnValider = QPushButton(Form)
        self.btnValider.setObjectName(u"btnValider")
        self.btnValider.setGeometry(QRect(410, 260, 75, 24))
        self.lblResultat = QLabel(Form)
        self.lblResultat.setObjectName(u"lblResultat")
        self.lblResultat.setGeometry(QRect(380, 320, 161, 16))
        self.champsMultiLignes = QPlainTextEdit(Form)
        self.champsMultiLignes.setObjectName(u"champsMultiLignes")
        self.champsMultiLignes.setGeometry(QRect(240, 350, 441, 221))
        self.btnLecture = QPushButton(Form)
        self.btnLecture.setObjectName(u"btnLecture")
        self.btnLecture.setGeometry(QRect(240, 590, 141, 24))
        self.btnEcriture = QPushButton(Form)
        self.btnEcriture.setObjectName(u"btnEcriture")
        self.btnEcriture.setGeometry(QRect(570, 590, 111, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre1:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre2:", None))
        self.btnValider.setText(QCoreApplication.translate("Form", u"Valider", None))
        self.lblResultat.setText(QCoreApplication.translate("Form", u"Somme =", None))
        self.btnLecture.setText(QCoreApplication.translate("Form", u"Lecture Fichier", None))
        self.btnEcriture.setText(QCoreApplication.translate("Form", u"Ecriture Fichier", None))
    # retranslateUi

