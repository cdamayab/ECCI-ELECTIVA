import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import time

# Definir entorno local o raspberry
ENTORNO_LOCAL = True

if not ENTORNO_LOCAL:
    import smbus
    # Configuración I2C
    bus = smbus.SMBus(1)  # Bus I2C en Raspberry Pi
    i2c_address = 0x48  # Dirección del sensor (por ejemplo, para un TMP102)

    def leer_sensor_i2c():
        # Leer dos bytes del sensor (ejemplo TMP102)
        raw = bus.read_word_data(i2c_address, 0)
        temp = ((raw & 0xff) << 8) | (raw >> 8)
        temp = temp >> 4  # TMP102 tiene 12 bits de precisión
        return temp * 0.0625  # Convertir a grados Celsius

else:
    # Simulacion en entorno local
    def leer_sensor_i2c():
        return 25.0  # Simula una lectura de temperatura de 25.0 grados Celsius

class I2CReadApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mostrar_lectura)

    def initUI(self):
        self.setWindowTitle("Lectura de Sensor I2C")
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Campo de texto para ingresar el tiempo de lectura
        self.time_input = QLineEdit(self)
        self.time_input.setPlaceholderText("Introduce el tiempo en segundos")
        layout.addWidget(self.time_input)

        # Botón para comenzar la lectura del sensor
        self.start_button = QPushButton('Iniciar Lectura', self)
        self.start_button.clicked.connect(self.iniciar_lectura)
        layout.addWidget(self.start_button)

        # Static Text para mostrar la lectura del sensor
        self.lectura_label = QLabel('Lectura: -', self)
        layout.addWidget(self.lectura_label)

        # Footer con nombres y logo
        footer_layout = QHBoxLayout()

        # Nombres
        names_layout = QVBoxLayout()
        self.label1 = QLabel('Cristhian Amaya', self)
        self.label2 = QLabel('Diego Ariztizabal', self)
        self.label3 = QLabel('Daniel Cardenas', self)
        self.label4 = QLabel('Nicolas Gonzalez', self)

        names_layout.addWidget(self.label1)
        names_layout.addWidget(self.label2)
        names_layout.addWidget(self.label3)
        names_layout.addWidget(self.label4)

        # Logo de la universidad
        image_label_logo = QLabel(self)
        pixmap = QPixmap('ecci.jpg')
        image_label_logo.setPixmap(pixmap)
        image_label_logo.setScaledContents(True)
        image_label_logo.setFixedSize(150, 150)

        # Añadir nombres y logo al layout de footer
        footer_layout.addLayout(names_layout)
        footer_layout.addWidget(image_label_logo)

        # Añadir footer al layout principal
        layout.addLayout(footer_layout)

        self.show()

    def iniciar_lectura(self):
        try:
            tiempo = int(float(self.time_input.text()) * 1000)  # Convertir a milisegundos y asegurar que sea entero
            self.timer.start(tiempo)
        except ValueError:
            print("Por favor, introduce un número válido para el tiempo.")

    def mostrar_lectura(self):
        # Leer y mostrar datos del sensor I2C
        lectura = leer_sensor_i2c()
        self.lectura_label.setText(f"Lectura: {lectura:.2f}")

def main():
    app = QApplication(sys.argv)
    mainWindow = I2CReadApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

