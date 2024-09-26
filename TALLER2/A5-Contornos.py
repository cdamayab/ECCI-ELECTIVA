import sys
import numpy as np
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap, QImage

class ImageContourApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Identificación de Contornos de Imagen")
        self.setGeometry(100, 100, 800, 800)

        # Definir layout principal  
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)   
        layout = QVBoxLayout(central_widget)  

        # Botón para cargar la imagen
        self.load_button = QPushButton('Cargar Imagen', self)  
        self.load_button.clicked.connect(self.load_image)  
        layout.addWidget(self.load_button)

        # Etiqueta para mostrar la imagen cargada 
        self.image_label = QLabel(self)
        layout.addWidget(self.image_label) 
 
        # Layout secundario para los nombres y el logo 
        footer_layout = QHBoxLayout() 

        # Añadir etiquetas con los nombres 
        names_layout = QVBoxLayout()
        self.label1 = QLabel('Cristhian Amaya', self) 
        self.label2 = QLabel('Diego Ariztizabal', self)  
        self.label3 = QLabel('Daniel Cardenas', self) 
        self.label4 = QLabel('Nicolas Gonzalez', self)

        names_layout.addWidget(self.label1) 
        names_layout.addWidget(self.label2)  
        names_layout.addWidget(self.label3)   
        names_layout.addWidget(self.label4) 

        # Añadir logo de la universidad
        image_label_logo = QLabel(self)
        pixmap = QPixmap('ecci.jpg') 
        image_label_logo.setPixmap(pixmap)
        image_label_logo.setScaledContents(True)  
        image_label_logo.setFixedSize(150, 150) 

        # Añadir nombres y logo al footer_layout
        footer_layout.addLayout(names_layout)
        footer_layout.addWidget(image_label_logo)  

        # Añadir footer al layout principal 
        layout.addLayout(footer_layout)   

        self.show()

    def load_image(self):
        # Abrir un cuadro de diálogo para seleccionar la imagen
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Archivos de Imagen (*.png *.jpg *.bmp)", options=options)
        if file_name:
            # Cargar la imagen con OpenCV
            self.process_image(file_name)

    def process_image(self, file_name):
        # Cargar la imagen original
        imagen_original = cv2.imread(file_name)
        if imagen_original is None: 
            return

        # Redimensionar imagen
        imagen_original = cv2.resize(imagen_original, None, fx=0.5, fy=0.5) 

        # Convertir a escala de grises 
        gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY) 

        # Aplicar umbral adaptativo
        blanco_negro = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

        # Aplicar filtro de suavizado para eliminar el ruido
        blanco_negro = cv2.medianBlur(blanco_negro, 5)

        # Encontrar contornos en la imagen en blanco y negro
        contornos, _ = cv2.findContours(blanco_negro, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Dibujar los contornos en la imagen original
        imagen_contornos = imagen_original.copy()
        cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

        # Crear un mosaico con la imagen original y la imagen con contornos
        mosaico = cv2.hconcat([imagen_original, imagen_contornos])

        # Convertir la imagen de mosaico de OpenCV a un formato que PyQt5 pueda mostrar
        height, width, channel = mosaico.shape  
        bytes_per_line = 3 * width  
        qimg = QImage(mosaico.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped() 

        # Mostrar la imagen en el QLabel 
        self.image_label.setPixmap(QPixmap.fromImage(qimg))  
        self.image_label.setScaledContents(True) 
        self.image_label.setFixedSize(600, 300)    

def main():
    app = QApplication(sys.argv) 
    mainWindow = ImageContourApp()     
    sys.exit(app.exec_())   

if __name__ == '__main__':
    main()  

