import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

# Definir entorno local o raspberry
ENTORNO_LOCAL = True

if not ENTORNO_LOCAL:
    import RPi.GPIO as GPIO
    from time import sleep
    # Configuración de pines para el motor paso a paso
    GPIO.setmode(GPIO.BCM)
    
    coil_A_1_pin = 17  # Pin 1 de la bobina A
    coil_A_2_pin = 18  # Pin 2 de la bobina A
    coil_B_1_pin = 22  # Pin 1 de la bobina B
    coil_B_2_pin = 23  # Pin 2 de la bobina B
    
    GPIO.setup(coil_A_1_pin, GPIO.OUT)
    GPIO.setup(coil_A_2_pin, GPIO.OUT)
    GPIO.setup(coil_B_1_pin, GPIO.OUT)
    GPIO.setup(coil_B_2_pin, GPIO.OUT)

    def setStep(w1, w2, w3, w4):
        GPIO.output(coil_A_1_pin, w1)
        GPIO.output(coil_A_2_pin, w2)
        GPIO.output(coil_B_1_pin, w3)
        GPIO.output(coil_B_2_pin, w4)

    def move_stepper(steps, delay=0.005):
        for i in range(steps):
            setStep(1, 0, 1, 0)
            sleep(delay)
            setStep(0, 1, 1, 0)
            sleep(delay)
            setStep(0, 1, 0, 1)
            sleep(delay)
            setStep(1, 0, 0, 1)
            sleep(delay)

else:
    # Simulacion en entorno local
    def move_stepper(steps, delay=0.005):
        print(f"Simulacion: Motor movido {steps} pasos.")

class StepperMotorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Control de Motor Paso a Paso")
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Campo de texto para ingresar el número de vueltas
        self.turns_input = QLineEdit(self)
        self.turns_input.setPlaceholderText("Introduce el numero de vueltas")
        layout.addWidget(self.turns_input)

        # Botón para accionar el movimiento
        self.move_button = QPushButton('Mover Motor', self)
        self.move_button.clicked.connect(self.start_motor)
        layout.addWidget(self.move_button)

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

    def start_motor(self):
        try:
            vueltas = float(self.turns_input.text())  # Convertir las vueltas a float
            steps_per_rev = 200  # Número de pasos por vuelta del motor
            total_steps = int(vueltas * steps_per_rev)  # Convertir vueltas a pasos

            # Mover el motor el número de pasos calculado
            move_stepper(total_steps)
        except ValueError:
            print("Por favor, introduce un número válido de vueltas.")

def main():
    app = QApplication(sys.argv)
    mainWindow = StepperMotorApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if not ENTORNO_LOCAL:
            GPIO.cleanup()

