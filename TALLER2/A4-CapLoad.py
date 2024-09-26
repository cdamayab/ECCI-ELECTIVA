import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap

class CapSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simulador Circuito RC")
        self.setGeometry(100, 100, 800, 800)

        # Definir layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Crear sliders
        self.slider_resistance = QSlider(Qt.Horizontal, self)
        self.slider_resistance.setRange(1, 1000)
        self.slider_resistance.setValue(100)
        self.slider_resistance.valueChanged.connect(self.update_plot)

        self.slider_capacitance = QSlider(Qt.Horizontal, self)
        self.slider_capacitance.setRange(1, 100)
        self.slider_capacitance.setValue(10)
        self.slider_capacitance.valueChanged.connect(self.update_plot)

        self.slider_voltage = QSlider(Qt.Horizontal, self)
        self.slider_voltage.setRange(1, 10)
        self.slider_voltage.setValue(5)
        self.slider_voltage.valueChanged.connect(self.update_plot)

        # Etiquetas para sliders
        self.label_resistance = QLabel(f"Resistencia (Ω): {self.slider_resistance.value()}", self)
        self.label_capacitance = QLabel(f"Capacitancia (μF): {self.slider_capacitance.value()}", self)
        self.label_voltage = QLabel(f"Voltaje (V): {self.slider_voltage.value()}", self)

        # Añadir widgets al layout
        layout.addWidget(self.label_resistance)
        layout.addWidget(self.slider_resistance)
        layout.addWidget(self.label_capacitance)
        layout.addWidget(self.slider_capacitance)
        layout.addWidget(self.label_voltage)
        layout.addWidget(self.slider_voltage)

        # Crear area para la grafica
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
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
        image_label = QLabel(self)
        pixmap = QPixmap('ecci.jpg') 
        image_label.setPixmap(pixmap)  
        image_label.setScaledContents(True)
        image_label.setFixedSize(150, 150)  

        # Añadir nombres y logo al footer_layout
        footer_layout.addLayout(names_layout)  
        footer_layout.addWidget(image_label) 

        # Añadir footer al layout principal  
        layout.addLayout(footer_layout) 

        # Inicializar gráfico
        self.time = np.linspace(0, 10, 1000)  # Tiempo en segundos  
        self.update_plot()  

        self.show()

    def update_plot(self):
        # Obtener valores de los sliders  
        R = self.slider_resistance.value()  
        C = self.slider_capacitance.value() / 1000  # Convertir a Faradios (μF -> F)
        V = self.slider_voltage.value()    

        # Actualizar etiquetas
        self.label_resistance.setText(f"Resistencia (Ω): {R}")  
        self.label_capacitance.setText(f"Capacitancia (μF): {self.slider_capacitance.value()}")
        self.label_voltage.setText(f"Voltaje (V): {V}") 

        # Ecuaciones de carga y descarga de un condensador
        tau = R * C  # Constante de tiempo  
        charge = V * (1 - np.exp(-self.time / tau))  # Ecuación de carga
        discharge = V * np.exp(-self.time / tau)      # Ecuación de descarga

        # Limpiar la grafica anterior
        self.ax.clear() 

        # Graficar carga y descarga
        self.ax.plot(self.time, charge, label='Carga')  
        self.ax.plot(self.time, discharge, label='Descarga')
        self.ax.set_xlabel('Tiempo (s)') 
        self.ax.set_ylabel('Voltaje (V)') 
        self.ax.set_title('Carga y Descarga del Condensador') 
        self.ax.legend()

        # Refrescar la grafica
        self.canvas.draw()

def main():
    app = QApplication(sys.argv) 
    mainWindow = CapSimulator()  
    sys.exit(app.exec_()) 

if __name__ == '__main__':
    main()

