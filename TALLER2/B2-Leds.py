import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap

# Definir entorno local o raspberry
ENTORNO_LOCAL = False

if not ENTORNO_LOCAL:
    import RPi.GPIO as GPIO
    # Configuracion de pines para leds
    GPIO.setmode(GPIO.BOARD)

    # Pines para LED1 y LED2 (encendido/apagado)
    led1_signal = 17  # pin LED1
    led1_gnd = 18     # pin GND
    led2_signal = 22  # pin LED2
    led2_gnd = 23     # pin GND

    # Pines para LED3 y LED4 (brillo por sliders)
    led3_signal = 11  # pin LED3
    led3_gnd    = 6   # pin GND definido por placa
    led4_signal = 12  # pin LED4
    led4_gnd    = 9   # pin GND definido por placa

    # Configuracion de pines de salida
    GPIO.setup(led1_signal, GPIO.OUT)
    GPIO.setup(led2_signal, GPIO.OUT)
    GPIO.setup(led3_signal, GPIO.OUT)
    GPIO.setup(led4_signal, GPIO.OUT)

    # PWM para controlar brillo de leds 3 y 4
    led3_pwm = GPIO.PWM(led3_signal, 100)
    led4_pwm = GPIO.PWM(led4_signal, 100)

    led3_pwm.start(0)
    led4_pwm.start(0)

else:
    # Si entorno = local, se definen funciones vacias
    class GPIO:
        @staticmethod
        def setup(pin, mode):
            pass

        @staticmethod
        def output(pin, state):
            pass

        class PWM:
            def __init__(self, pin, freq):
                pass

            def start(self, value):
                pass

            def ChangeDutyCycle(self, value):
                pass

# Variables para color de leds 1 y 2
LED1_COLOR_ON = QColor(0, 255, 0)  # olor LED 1
LED2_COLOR_ON = QColor(0, 0, 255)  # Color LED 2

class LEDControlApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Estados iniciales para los LEDs
        self.led1_on = False
        self.led2_on = False

    def initUI(self):
        self.setWindowTitle("Control de LEDs con Botones y Brillo con Sliders")
        self.setGeometry(100, 100, 400, 400)

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Botones para controlar encendido/apagado
        self.button_led1 = QPushButton('LED 1', self)
        self.button_led1.clicked.connect(lambda: self.toggle_led(self.button_led1, 'led1'))
        layout.addWidget(self.button_led1)

        self.button_led2 = QPushButton('LED 2', self)
        self.button_led2.clicked.connect(lambda: self.toggle_led(self.button_led2, 'led2'))
        layout.addWidget(self.button_led2)

        # Sliders para controlar el brillo
        self.slider_led3 = QSlider(Qt.Horizontal, self)
        self.slider_led3.setMinimum(0)
        self.slider_led3.setMaximum(100)
        self.slider_led3.valueChanged.connect(lambda: self.update_brightness('led3', self.slider_led3.value()))
        layout.addWidget(self.slider_led3)

        self.slider_led4 = QSlider(Qt.Horizontal, self)
        self.slider_led4.setMinimum(0)
        self.slider_led4.setMaximum(100)
        self.slider_led4.valueChanged.connect(lambda: self.update_brightness('led4', self.slider_led4.value()))
        layout.addWidget(self.slider_led4)

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

    def toggle_led(self, button, led_name):
        if led_name == 'led1':
            self.led1_on = not self.led1_on
            if not ENTORNO_LOCAL:
                GPIO.output(led1_signal, self.led1_on)
            button.setStyleSheet(f"background-color: {LED1_COLOR_ON.name()}" if self.led1_on else "")

        elif led_name == 'led2':
            self.led2_on = not self.led2_on
            if not ENTORNO_LOCAL:
                GPIO.output(led2_signal, self.led2_on)
            button.setStyleSheet(f"background-color: {LED2_COLOR_ON.name()}" if self.led2_on else "")

    def update_brightness(self, led_name, value):
        if led_name == 'led3':
            if not ENTORNO_LOCAL:
                led3_pwm.ChangeDutyCycle(value)
        elif led_name == 'led4':
            if not ENTORNO_LOCAL:
                led4_pwm.ChangeDutyCycle(value)

def main():
    app = QApplication(sys.argv)
    mainWindow = LEDControlApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if not ENTORNO_LOCAL:
            GPIO.cleanup()

