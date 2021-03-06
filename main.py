# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from funciones import *
import funciones.funciones as func


class Ui_Game(object):
    numeroAleatorio = func.generadorNumero()

    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.resize(613, 157)
        Game.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.centralwidget = QtWidgets.QWidget(Game)
        self.centralwidget.setMinimumSize(QtCore.QSize(628, 157))
        self.centralwidget.setMaximumSize(QtCore.QSize(628, 157))
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(410, 27, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text2.setFont(font)
        self.text2.setStyleSheet("color: #323643;")
        self.text2.setObjectName("text2")
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(20, 80, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text1.setFont(font)
        self.text1.setStyleSheet("color: #323643;")
        self.text1.setObjectName("text1")
        self.txt2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt2.setGeometry(QtCore.QRect(530, 20, 41, 20))
        self.txt2.setStyleSheet(" border-width: 1px;\n"
                                " border-style: solid;\n"
                                " border-color:  #0E3EDA;\n"
                                "border-top-style:none; \n"
                                "border-left: none;\n"
                                "border-right: none;\n"
                                "")
        self.txt2.setText("")
        self.txt2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt2.setObjectName("txt2")
        self.txt1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt1.setGeometry(QtCore.QRect(20, 110, 51, 21))
        self.txt1.setStyleSheet(" border-width: 1px;\n"
                                " border-style: solid;\n"
                                " border-color:  #0E3EDA;\n"
                                "border-top-style:none; \n"
                                "border-left: none;\n"
                                "border-right: none;\n"
                                "\n"
                                "")
        self.txt1.setText("")
        self.txt1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt1.setReadOnly(True)
        self.txt1.setObjectName("txt1")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(410, 60, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setStyleSheet("QPushButton {\n"
                                "    color: white;\n"
                                "    background-color: #015ECB;;\n"
                                "    border-radius: 5px;\n"
                                "    padding: 5px;\n"
                                "\n"
                                "}\n"
                                "\n"
                                "/*QPushButton:hover {\n"
                                "    background-color: #0093e8;;\n"
                                "    color: white;\n"
                                "}\n"
                                "*/\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                " background-color:#004da5;\n"
                                "color: white;\n"
                                "}")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(410, 100, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setStyleSheet("QPushButton {\n"
                                "    color: #015ECB;\n"
                                "    border: 1px solid;\n"
                                "    border-color: #015ECB;\n"
                                "    border-radius: 5px;\n"
                                "    padding: 5px;\n"
                                "}\n"
                                "\n"
                                "/*QPushButton:hover {\n"
                                "    background-color: #d8d8d8;\n"
                                "    color: white;\n"
                                "}\n"
                                "*/\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "     background-color:#f4f4f4;\n"
                                "    color: #015ECB;\n"
                                "}\n"
                                "")
        self.btn2.setObjectName("btn2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 10, 221, 130))
        self.plainTextEdit.setStyleSheet(" border-width: 1px;\n"
                                         " border-style: solid;\n"
                                         "border-color: rgb(218, 196, 255);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.cmb1 = QtWidgets.QComboBox(self.centralwidget)
        self.cmb1.setGeometry(QtCore.QRect(20, 40, 101, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb1.setFont(font)
        self.cmb1.setStyleSheet("    color: blue;\n"
                                "    background-color: white;;\n"
                                "    border: 1px solid blue;\n"
                                "")
        self.cmb1.setObjectName("cmb1")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.text3 = QtWidgets.QLabel(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(20, 10, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.text3.setFont(font)
        self.text3.setStyleSheet("color: #323643;")
        self.text3.setObjectName("text3")
        Game.setCentralWidget(self.centralwidget)

        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate(
            "Game", "  ??Intenta adivinar el numero!"))
        Game.setWindowIcon(QtGui.QIcon('./assets/rocket.png'))
        self.text2.setText(_translate("Game", "Ingresa un n??mero:"))
        self.text1.setText(_translate("Game", "Intentos disponibles:"))
        self.btn1.setText(_translate("Game", "Probar numero"))
        self.btn2.setText(_translate("Game", "Reiniciar Juego"))
        self.plainTextEdit.setToolTip(_translate(
            "Game", "<html><head/><body><p><br/></p></body></html>"))
        self.cmb1.setItemText(0, _translate("Game", "Facil"))
        self.cmb1.setItemText(1, _translate("Game", "Intermedio"))
        self.cmb1.setItemText(2, _translate("Game", "Dificil"))
        self.cmb1.setItemText(3, _translate("Game", "Demencial"))
        self.text3.setText(_translate("Game", "Nivel de dificultad:"))
        self.txt1.setText(_translate("Game", "5"))

        self.btn1.clicked.connect(self.playGame)
        self.btn2.clicked.connect(self.reset)

    def playGame(self):
        try:
            intentos = int(self.txt1.text())
            if intentos != 0:
                intento = func.adivinarNumero(
                    self.numeroAleatorio, self.txt2.text())
                if intento[0]:
                    intentos = intentos - 1
                    self.txt1.setText(str(intentos))
                    if(intentos != 0):
                        self.plainTextEdit.setPlainText(
                            intento[1])
                    elif(intentos == 0):
                        self.plainTextEdit.setPlainText(
                            "Perdiste :( , suerte en la proxima")
                        self.txt2.setFocus()
                elif intento[0] == False:
                    intentos = intentos - 1
                    self.txt1.setText(str(intentos))
                    if(intentos != 0):
                        self.plainTextEdit.setPlainText(
                            intento[1])
                    elif(intentos == 0):
                        self.plainTextEdit.setPlainText(
                            "Perdiste :( , suerte en la proxima")
                        self.txt2.setFocus()
        except:
            self.plainTextEdit.setPlainText(
                            "Parece que algo salio mal al intentar con ese numero ")

    def reset(self):
        self.txt1.setText("5")
        self.txt2.setText("")
        self.plainTextEdit.setPlainText("")
        self.txt2.setFocus()
        self.numeroAleatorio = func.generadorNumero()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QMainWindow()
    ui = Ui_Game()
    ui.setupUi(Game)
    Game.show()
    sys.exit(app.exec_())
