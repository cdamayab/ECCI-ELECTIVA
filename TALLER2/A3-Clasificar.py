# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("ROBOTS Y SUS ARTICULACIONES")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout principal
        layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Titulo
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("ROBOTS Y SUS ARTICULACIONES")
        layout.addWidget(self.label)

        # ComboBox para seleccionar el tipo de robot
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItem("cartesiano")
        self.comboBox.addItem("esferico")
        self.comboBox.addItem("cilindrico")
        layout.addWidget(self.comboBox)

        # Label para mostrar la desc de las articulaciones
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font.setBold(True)
        self.label_2.setFont(font)
        layout.addWidget(self.label_2)

        # Label para mostrar la imagen del robot
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFixedSize(400, 300)
        layout.addWidget(self.label_3)

        # Dic que asocia cada opcion con un texto específico
        self.text_dict = {
            "cartesiano": "Este es un robot cartesiano y cuenta con 3 articulaciones prismaticas",
            "esferico": "Este es un robot esférico y cuenta con 2 articulaciones rotacionales y una prismatica",
            "cilindrico": "Este es un robot cilíndrico y cuenta con 3 articulaciones rotacionales"
        }

        # Dic que asocia cada opción con la imagen correspondiente
        self.image_dict = {
            "cartesiano": "./cartesiano.jpg",
            "esferico": "./esferico.jpg",
            "cilindrico": "./cilindrico.jpg"
        }

        # Conectar señal de cambio en comboBox con los métodos que actualizan los labels
        self.comboBox.currentIndexChanged.connect(self.update_label_2)
        self.comboBox.currentIndexChanged.connect(self.update_label_3)

        # Layout secundario para los nombres y el logo
        footer_layout = QHBoxLayout()

        # Añadir etiquetas con los nombres
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
        pixmap = QPixmap('./ecci.jpg')  # Asegúrate de que la imagen esté en el mismo directorio
        image_label_logo.setPixmap(pixmap)
        image_label_logo.setScaledContents(True)
        image_label_logo.setFixedSize(150, 150)

        # Añadir nombres y logo al footer_layout
        footer_layout.addLayout(names_layout)
        footer_layout.addWidget(image_label_logo)

        # Añadir footer al layout principal
        layout.addLayout(footer_layout)

        MainWindow.setCentralWidget(self.centralwidget)

    def update_label_2(self):
        """Actualiza el texto de label_2 según la opción seleccionada en comboBox"""
        selected_text = self.comboBox.currentText()  # Obtener el texto seleccionado
        # Actualizar label_2 con el texto del diccionario
        self.label_2.setText(self.text_dict.get(selected_text, "Texto no definido"))

    def update_label_3(self):
        """Actualiza el label_3 con la imagen del robot según la opción seleccionada"""
        selected_text = self.comboBox.currentText()  # Obtener el texto seleccionado
        image_path = self.image_dict.get(selected_text, "")  # Obtener la ruta de la imagen
        
        if image_path:  # Si hay una imagen definida para la opción seleccionada
            pixmap = QtGui.QPixmap(image_path)
            self.label_3.setPixmap(pixmap.scaled(self.label_3.size(), QtCore.Qt.KeepAspectRatio))
        else:
            self.label_3.clear()  # Limpiar el label si no hay imagen disponible


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

