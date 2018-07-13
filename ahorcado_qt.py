# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ahorcado_equipo2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ahorcado_Qt(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 590)
        MainWindow.setStyleSheet("QLineEdit{\n"
"    border: 1px solid gray;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.letra_a = QtWidgets.QPushButton(self.centralwidget)
        self.letra_a.setGeometry(QtCore.QRect(0, 460, 41, 41))
        self.letra_a.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_a.setObjectName("letra_a")
        self.letra_b = QtWidgets.QPushButton(self.centralwidget)
        self.letra_b.setGeometry(QtCore.QRect(40, 460, 41, 41))
        self.letra_b.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_b.setObjectName("letra_b")
        self.letra_d = QtWidgets.QPushButton(self.centralwidget)
        self.letra_d.setGeometry(QtCore.QRect(120, 460, 41, 41))
        self.letra_d.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_d.setObjectName("letra_d")
        self.letra_c = QtWidgets.QPushButton(self.centralwidget)
        self.letra_c.setGeometry(QtCore.QRect(80, 460, 41, 41))
        self.letra_c.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_c.setObjectName("letra_c")
        self.letra_e = QtWidgets.QPushButton(self.centralwidget)
        self.letra_e.setGeometry(QtCore.QRect(160, 460, 41, 41))
        self.letra_e.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_e.setObjectName("letra_e")
        self.letra_h = QtWidgets.QPushButton(self.centralwidget)
        self.letra_h.setGeometry(QtCore.QRect(280, 460, 41, 41))
        self.letra_h.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_h.setObjectName("letra_h")
        self.letra_g = QtWidgets.QPushButton(self.centralwidget)
        self.letra_g.setGeometry(QtCore.QRect(240, 460, 41, 41))
        self.letra_g.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_g.setObjectName("letra_g")
        self.letra_i = QtWidgets.QPushButton(self.centralwidget)
        self.letra_i.setEnabled(True)
        self.letra_i.setGeometry(QtCore.QRect(320, 460, 41, 41))
        self.letra_i.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_i.setObjectName("letra_i")
        self.letra_j = QtWidgets.QPushButton(self.centralwidget)
        self.letra_j.setGeometry(QtCore.QRect(0, 500, 41, 41))
        self.letra_j.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_j.setObjectName("letra_j")
        self.letra_f = QtWidgets.QPushButton(self.centralwidget)
        self.letra_f.setGeometry(QtCore.QRect(200, 460, 41, 41))
        self.letra_f.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_f.setObjectName("letra_f")
        self.letra_m = QtWidgets.QPushButton(self.centralwidget)
        self.letra_m.setGeometry(QtCore.QRect(120, 500, 41, 41))
        self.letra_m.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_m.setObjectName("letra_m")
        self.letra_l = QtWidgets.QPushButton(self.centralwidget)
        self.letra_l.setGeometry(QtCore.QRect(80, 500, 41, 41))
        self.letra_l.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_l.setObjectName("letra_l")
        self.letra_n = QtWidgets.QPushButton(self.centralwidget)
        self.letra_n.setGeometry(QtCore.QRect(160, 500, 41, 41))
        self.letra_n.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_n.setObjectName("letra_n")
        self.letra_enie = QtWidgets.QPushButton(self.centralwidget)
        self.letra_enie.setGeometry(QtCore.QRect(200, 500, 41, 41))
        self.letra_enie.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_enie.setObjectName("letra_enie")
        self.letra_k = QtWidgets.QPushButton(self.centralwidget)
        self.letra_k.setGeometry(QtCore.QRect(40, 500, 41, 41))
        self.letra_k.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_k.setObjectName("letra_k")
        self.letra_q = QtWidgets.QPushButton(self.centralwidget)
        self.letra_q.setGeometry(QtCore.QRect(320, 500, 41, 41))
        self.letra_q.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_q.setObjectName("letra_q")
        self.letra_p = QtWidgets.QPushButton(self.centralwidget)
        self.letra_p.setGeometry(QtCore.QRect(280, 500, 41, 41))
        self.letra_p.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_p.setObjectName("letra_p")
        self.letra_r = QtWidgets.QPushButton(self.centralwidget)
        self.letra_r.setGeometry(QtCore.QRect(0, 540, 41, 41))
        self.letra_r.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_r.setObjectName("letra_r")
        self.letra_s = QtWidgets.QPushButton(self.centralwidget)
        self.letra_s.setGeometry(QtCore.QRect(40, 540, 41, 41))
        self.letra_s.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_s.setObjectName("letra_s")
        self.letra_o = QtWidgets.QPushButton(self.centralwidget)
        self.letra_o.setGeometry(QtCore.QRect(240, 500, 41, 41))
        self.letra_o.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_o.setObjectName("letra_o")
        self.letra_x = QtWidgets.QPushButton(self.centralwidget)
        self.letra_x.setGeometry(QtCore.QRect(240, 540, 41, 41))
        self.letra_x.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_x.setObjectName("letra_x")
        self.letra_t = QtWidgets.QPushButton(self.centralwidget)
        self.letra_t.setGeometry(QtCore.QRect(80, 540, 41, 41))
        self.letra_t.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_t.setObjectName("letra_t")
        self.letra_u = QtWidgets.QPushButton(self.centralwidget)
        self.letra_u.setGeometry(QtCore.QRect(120, 540, 41, 41))
        self.letra_u.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_u.setObjectName("letra_u")
        self.letra_v = QtWidgets.QPushButton(self.centralwidget)
        self.letra_v.setGeometry(QtCore.QRect(160, 540, 41, 41))
        self.letra_v.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_v.setObjectName("letra_v")
        self.letra_w = QtWidgets.QPushButton(self.centralwidget)
        self.letra_w.setGeometry(QtCore.QRect(200, 540, 41, 41))
        self.letra_w.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_w.setObjectName("letra_w")
        self.letra_y = QtWidgets.QPushButton(self.centralwidget)
        self.letra_y.setGeometry(QtCore.QRect(280, 540, 41, 41))
        self.letra_y.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_y.setObjectName("letra_y")
        self.letra_z = QtWidgets.QPushButton(self.centralwidget)
        self.letra_z.setGeometry(QtCore.QRect(320, 540, 41, 41))
        self.letra_z.setStyleSheet("/* Letras Abcedario*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Letras Abcedario */")
        self.letra_z.setObjectName("letra_z")
        self.entrada_arriesgar = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_arriesgar.setGeometry(QtCore.QRect(390, 540, 181, 41))
        self.entrada_arriesgar.setStyleSheet("")
        self.entrada_arriesgar.setObjectName("entrada_arriesgar")
        self.boton_arriesgar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_arriesgar.setGeometry(QtCore.QRect(590, 540, 81, 41))
        self.boton_arriesgar.setStyleSheet("/* Boton Arriesgar*/\n"
"QPushButton {\n"
"   border: 1px solid gray;\n"
"   background-color: rgb(255, 151, 57);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"/* Fin Boton Arriesgar */")
        self.boton_arriesgar.setObjectName("boton_arriesgar")
        self.etiqueta_incognita = QtWidgets.QLabel(self.centralwidget)
        self.etiqueta_incognita.setGeometry(QtCore.QRect(0, 20, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etiqueta_incognita.setFont(font)
        self.etiqueta_incognita.setObjectName("etiqueta_incognita")
        self.boton_pista = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pista.setGeometry(QtCore.QRect(360, 20, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.boton_pista.setFont(font)
        self.boton_pista.setStatusTip("")
        self.boton_pista.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 1px solid gray;\n"
"    border-radius: 25px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.boton_pista.setObjectName("boton_pista")
        self.etiqueta_imagen = QtWidgets.QLabel(self.centralwidget)
        self.etiqueta_imagen.setGeometry(QtCore.QRect(360, 100, 351, 291))
        self.etiqueta_imagen.setStyleSheet("border-image: url(:/1/1.jpg);")
        imagen = QPixmap("1.jpg")
        self.etiqueta_imagen.setPixmap(imagen)
        self.etiqueta_imagen.setText("")
        self.etiqueta_imagen.setObjectName("etiqueta_imagen")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(550, 0, 113, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("QLabel{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.etiqueta_pista = QtWidgets.QLabel(self.layoutWidget)
        self.etiqueta_pista.setStyleSheet("QLabel{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color:red;\n"
"}")
        self.etiqueta_pista.setObjectName("etiqueta_pista")
        self.gridLayout.addWidget(self.etiqueta_pista, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("QLabel{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.etiqueta_puntuacion = QtWidgets.QLabel(self.layoutWidget)
        self.etiqueta_puntuacion.setStyleSheet("QLabel{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.etiqueta_puntuacion.setObjectName("etiqueta_puntuacion")
        self.gridLayout.addWidget(self.etiqueta_puntuacion, 1, 2, 1, 1)
        self.layoutWidget.raise_()
        self.letra_a.raise_()
        self.letra_b.raise_()
        self.letra_d.raise_()
        self.letra_c.raise_()
        self.letra_e.raise_()
        self.letra_h.raise_()
        self.letra_g.raise_()
        self.letra_i.raise_()
        self.letra_j.raise_()
        self.letra_f.raise_()
        self.letra_m.raise_()
        self.letra_l.raise_()
        self.letra_n.raise_()
        self.letra_enie.raise_()
        self.letra_k.raise_()
        self.letra_q.raise_()
        self.letra_p.raise_()
        self.letra_r.raise_()
        self.letra_s.raise_()
        self.letra_o.raise_()
        self.letra_x.raise_()
        self.letra_t.raise_()
        self.letra_u.raise_()
        self.letra_v.raise_()
        self.letra_w.raise_()
        self.letra_y.raise_()
        self.letra_z.raise_()
        self.entrada_arriesgar.raise_()
        self.boton_arriesgar.raise_()
        self.etiqueta_incognita.raise_()
        self.boton_pista.raise_()
        self.etiqueta_imagen.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.letra_a.setText(_translate("MainWindow", "A"))
        self.letra_b.setText(_translate("MainWindow", "B"))
        self.letra_d.setText(_translate("MainWindow", "D"))
        self.letra_c.setText(_translate("MainWindow", "C"))
        self.letra_e.setText(_translate("MainWindow", "E"))
        self.letra_h.setText(_translate("MainWindow", "H"))
        self.letra_g.setText(_translate("MainWindow", "G"))
        self.letra_i.setText(_translate("MainWindow", "I"))
        self.letra_j.setText(_translate("MainWindow", "J"))
        self.letra_f.setText(_translate("MainWindow", "F"))
        self.letra_m.setText(_translate("MainWindow", "M"))
        self.letra_l.setText(_translate("MainWindow", "L"))
        self.letra_n.setText(_translate("MainWindow", "N"))
        self.letra_enie.setText(_translate("MainWindow", "Ñ"))
        self.letra_k.setText(_translate("MainWindow", "K"))
        self.letra_q.setText(_translate("MainWindow", "Q"))
        self.letra_p.setText(_translate("MainWindow", "P"))
        self.letra_r.setText(_translate("MainWindow", "R"))
        self.letra_s.setText(_translate("MainWindow", "S"))
        self.letra_o.setText(_translate("MainWindow", "O"))
        self.letra_x.setText(_translate("MainWindow", "X"))
        self.letra_t.setText(_translate("MainWindow", "T"))
        self.letra_u.setText(_translate("MainWindow", "U"))
        self.letra_v.setText(_translate("MainWindow", "V"))
        self.letra_w.setText(_translate("MainWindow", "W"))
        self.letra_y.setText(_translate("MainWindow", "Y"))
        self.letra_z.setText(_translate("MainWindow", "Z"))
        self.boton_arriesgar.setText(_translate("MainWindow", "Arriesgar"))
        self.boton_pista.setText(_translate("MainWindow", "Pista"))
        self.label_4.setText(_translate("MainWindow", "Vidas:"))
        self.etiqueta_pista.setText(_translate("MainWindow", "❤❤❤"))
        self.label_2.setText(_translate("MainWindow", "Puntuación:"))
        self.etiqueta_puntuacion.setText(_translate("MainWindow", "0"))

