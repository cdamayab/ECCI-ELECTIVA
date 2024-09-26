# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
        self.centralwidget.setObjectName("centralwidget")
        
        # Layout principal vertical   
        main_layout = QVBoxLayout(self.centralwidget)    
        
        # Título
        self.label = QtWidgets.QLabel(self.centralwidget)  
        font = QtGui.QFont() 
        font.setPointSize(18) 
        self.label.setFont(font)  
        self.label.setObjectName("label")
        main_layout.addWidget(self.label)

        # Layout para los campos de entrada A y B
        input_layout = QHBoxLayout()

        # Etiqueta y campo de texto para num A
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        input_layout.addWidget(self.label_2)

        self.textEdit = QLineEdit(self.centralwidget)  
        self.textEdit.setFixedSize(100, 30)
        self.textEdit.setObjectName("textEdit")
        input_layout.addWidget(self.textEdit)   

        # Espaciado entre los campos
        input_layout.addStretch(1)

        # Etiqueta y campo de texto para num B
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        input_layout.addWidget(self.label_3)

        self.textEdit_2 = QLineEdit(self.centralwidget)     
        self.textEdit_2.setFixedSize(100, 30)
        self.textEdit_2.setObjectName("textEdit_2")  
        input_layout.addWidget(self.textEdit_2)   

        main_layout.addLayout(input_layout)

        # Layout para operaciones 
        button_layout = QVBoxLayout()

        # # Botones de funciones matematicas
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)    
        self.pushButton.setObjectName("pushButton")   
        button_layout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")  
        button_layout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")    
        button_layout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        button_layout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        button_layout.addWidget(self.pushButton_5)

        # Botones de funciones trigonometricas
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        button_layout.addWidget(self.pushButton_6)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        button_layout.addWidget(self.pushButton_7)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        button_layout.addWidget(self.pushButton_8)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        button_layout.addWidget(self.pushButton_9)

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        button_layout.addWidget(self.pushButton_10)

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName("pushButton_11")
        button_layout.addWidget(self.pushButton_11)

        main_layout.addLayout(button_layout)

        # Resultado
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setLineWidth(0)
        self.label_4.setObjectName("label_4")
        main_layout.addWidget(self.label_4)

        # Footer con nombres y logo
        footer_layout = QHBoxLayout()
        names_layout = QVBoxLayout()

        self.label1 = QLabel('Cristhian Amaya', self.centralwidget)
        self.label2 = QLabel('Diego Ariztizabal', self.centralwidget)
        self.label3 = QLabel('Daniel Cardenas', self.centralwidget)
        self.label4 = QLabel('Nicolas Gonzalez', self.centralwidget)

        names_layout.addWidget(self.label1)
        names_layout.addWidget(self.label2)
        names_layout.addWidget(self.label3)
        names_layout.addWidget(self.label4)

        # Añadir logo de la universidad
        image_label_logo = QLabel(self.centralwidget)
        pixmap = QPixmap('./ecci.jpg')
        image_label_logo.setPixmap(pixmap)
        image_label_logo.setScaledContents(True)
        image_label_logo.setFixedSize(150, 150)

        # Añadir nombres y logo al footer_layout
        footer_layout.addLayout(names_layout)
        footer_layout.addWidget(image_label_logo)

        main_layout.addLayout(footer_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Acciones al presionar los botones
        self.pushButton.clicked.connect(self.suma)
        self.pushButton_2.clicked.connect(self.resta)
        self.pushButton_3.clicked.connect(self.multiplicacion)
        self.pushButton_4.clicked.connect(self.division)
        self.pushButton_5.clicked.connect(self.residuo)
        self.pushButton_6.clicked.connect(self.seno)
        self.pushButton_7.clicked.connect(self.coseno)
        self.pushButton_8.clicked.connect(self.tangente)
        self.pushButton_9.clicked.connect(self.cotangente)
        self.pushButton_10.clicked.connect(self.secante)
        self.pushButton_11.clicked.connect(self.cosecante)

    # Función para validar que los campos sean numéricos
    def validar_numericos(self):
        try:
            a = float(self.textEdit.text())
            b = float(self.textEdit_2.text())
            return a, b
        except ValueError:
            self.label_4.setText("Error: Ingrese campos numéricos")
            return None, None

    # Funciones de operacion matematicas
    def suma(self):
        a, b = self.validar_numericos()
        if a is not None and b is not None:
            c = a + b
            self.label_4.setText(f"Resultado: {c}")

    def resta(self):
        a, b = self.validar_numericos()
        if a is not None and b is not None:
            c = a - b
            self.label_4.setText(f"Resultado: {c}")

    def multiplicacion(self):
        a, b = self.validar_numericos()
        if a is not None and b is not None:
            c = a * b
            self.label_4.setText(f"Resultado: {c}")

    def division(self):
        a, b = self.validar_numericos()
        if a is not None and b is not None:
            if b != 0:
                c = a / b
                self.label_4.setText(f"Resultado: {c}")
            else:
                self.label_4.setText("Error: División entre 0")

    def residuo(self):
        a, b = self.validar_numericos()
        if a is not None and b is not None:
            if b != 0:
                c = a % b
                self.label_4.setText(f"Resultado: {c}")
            else:
                self.label_4.setText("Error: División entre 0")

    # Funciones de operaciones trigonometricas
    def seno(self):
        a, _ = self.validar_numericos()
        if a is not None:
            valor = math.radians(a)
            resultado = round(math.sin(valor), 10)
            self.label_4.setText(f"Resultado: {resultado}")

    def coseno(self):
        a, _ = self.validar_numericos()
        if a is not None:
            valor = math.radians(a)
            resultado = round(math.cos(valor), 10)
            self.label_4.setText(f"Resultado: {resultado}")

    def tangente(self):
        a, _ = self.validar_numericos()
        if a is not None:
            valor = math.radians(a)
            resultado = math.tan(valor)
            if abs(resultado) > 1e10:
                self.label_4.setText("Resultado: INF")
            else:
                self.label_4.setText(f"Resultado: {round(resultado, 10)}")

    def cotangente(self):
        a, _ = self.validar_numericos()
        if a is not None:
            valor = math.radians(a)
            tangente = math.tan(valor)
            if tangente != 0:
                resultado = round(1 / tangente, 10)
                self.label_4.setText(f"Resultado: {resultado}")
            else:
                self.label_4.setText("Resultado: Indefinido")

    def secante(self):
        a, _ = self.validar_numericos()
        if a is not None:
            valor = math.radians(a)
            coseno = math.cos(valor)
            if coseno != 0:
                resultado = 1 / coseno
                if abs(resultado) > 1e10:
                    self.label_4.setText("Resultado: INF")
                else:
                    self.label_4.setText(f"Resultado: {round(resultado, 10)}")
            else:
                self.label_4.setText("Resultado: INF")

    def cosecante(self):
        a, _ = self.validar_numericos()
        if a is not None:
            valor = math.radians(a)
            seno = math.sin(valor)
            if seno != 0:
                resultado = round(1 / seno, 10)
                self.label_4.setText(f"Resultado: {resultado}")
            else:
                self.label_4.setText("Resultado: Indefinido")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.label.setText(_translate("MainWindow", "CALCULADORA"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.pushButton_4.setText(_translate("MainWindow", "/"))
        self.pushButton_5.setText(_translate("MainWindow", "%"))
        self.pushButton_6.setText(_translate("MainWindow", "SEN"))
        self.pushButton_7.setText(_translate("MainWindow", "COS"))
        self.pushButton_8.setText(_translate("MainWindow", "TAN"))
        self.pushButton_9.setText(_translate("MainWindow", "COTAN"))
        self.pushButton_10.setText(_translate("MainWindow", "SEC"))
        self.pushButton_11.setText(_translate("MainWindow", "COSEC"))
        self.label_4.setText(_translate("MainWindow", "Resultado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

