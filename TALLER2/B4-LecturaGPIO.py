import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPixmap

# Definir entorno local o raspberry
ENTORNO_LOCAL = False

if not ENTORNO_LOCAL:
    import RPi.GPIO as GPIO
    # Configuracion de pin de lectura
    GPIO.setmode(GPIO.BOARD)
    input_pin = 11  # pin de entrada digital
    GPIO.setup(input_pin, GPIO.IN)

else:
    # Simulacion en entorno local
    class GPIO:
        @staticmethod
        def setup(pin, mode):
            pass

        @staticmethod
        def input(pin):
            return 0  # Simula estado bajo

# Colores para los estados alto y bajo
COLOR_ALTO = QColor(255, 0, 0)  # Rojo para estado alto
COLOR_BAJO = QColor(0, 0, 255)  # Azul para estado bajo

class PinReadApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_pin)
        self.timer.start(500)  # Lectura cada 500 ms

    def initUI(self):
        self.setWindowTitle("Lectura de Puerto Digital")
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Static Text para mostrar estado del pin
        self.state_label = QLabel('Estado: Desconocido', self)
        layout.addWidget(self.state_label)

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

    def read_pin(self):
        # Leer estado del pin digital
        if not ENTORNO_LOCAL:
            pin_state = GPIO.input(input_pin)
        else:
            pin_state = 0  # Simula estado bajo en local

        # Actualizar color y texto segun estado
        if pin_state == 1:
            self.state_label.setText("Estado: Alto")
            self.state_label.setStyleSheet(f"color: {COLOR_ALTO.name()}")
        else:
            self.state_label.setText("Estado: Bajo")
            self.state_label.setStyleSheet(f"color: {COLOR_BAJO.name()}")

def main():
    app = QApplication(sys.argv)
    mainWindow = PinReadApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if not ENTORNO_LOCAL:
            GPIO.cleanup()

