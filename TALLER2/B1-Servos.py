import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QDial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# Definir entorno local o raspberry
ENTORNO_LOCAL = False

if not ENTORNO_LOCAL:
    import RPi.GPIO as GPIO
    # Configuración de pines GPIO para servos
    GPIO.setmode(GPIO.BOARD)

    # Pines Servo 1 (VCC, GND, PWM)
    servo1_pwm  = 11  # pin PWM
    #servo1_vcc = 2   # pin VCC definido por placa
    #servo1_gnd = 6   # pin GND definido por placa

    # Pines Servo 2 (VCC, GND, PWM)
    servo2_pwm  = 12  # pin PWM
    #servo2_vcc = 4   # pin VCC definido por placa
    #servo2_gnd = 9   # pin GND definido por placa

    # Configuracion de pines PWM 
    GPIO.setup(servo1_pwm, GPIO.OUT)
    GPIO.setup(servo2_pwm, GPIO.OUT)

    # Configuracion de PWM para servos (frecuencia de 50 Hz)
    servo1 = GPIO.PWM(servo1_pwm, 50)
    servo2 = GPIO.PWM(servo2_pwm, 50)

    # Iniciar PWM con duty cycle 0 - posicion inicial
    servo1.start(0)
    servo2.start(0)
else:
    # Si entorno = local, se definen funciones vacias
    class GPIO:
        BCM = None
        OUT = None

        @staticmethod
        def setmode(mode):
            pass

        @staticmethod
        def setup(pin, mode):
            pass

        @staticmethod
        def PWM(pin, freq):
            return DummyPWM()

    class DummyPWM:
        def start(self, value):
            pass

        def ChangeDutyCycle(self, value):
            pass

        def stop(self):
            pass

class ServoControlApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Control de Servomotores con Sliders")
        self.setGeometry(100, 100, 400, 400)

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Textbox para seleccion del servomotor
        self.servo_input = QLineEdit(self)
        self.servo_input.setPlaceholderText("Selecciona servo (1 o 2)")
        layout.addWidget(self.servo_input)

        # Slider para el angulo
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)
        self.slider.valueChanged.connect(lambda: self.update_servo('slider'))
        layout.addWidget(self.slider)

        # Label angulo actual
        self.angle_label = QLabel('Ángulo: 0°', self)
        layout.addWidget(self.angle_label)

        # Dial para visualizar el angulo 
        self.dial = QDial(self)
        self.dial.setMinimum(0)
        self.dial.setMaximum(180)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(lambda: self.update_servo('dial'))
        layout.addWidget(self.dial)

        # Footer para nombres y logo
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

    def update_servo(self, source): # Actualiza angulo y controles (slider,dial).onChange
    
        # Obtener el angulo actual
        if source == 'slider':
            angle = self.slider.value()
            self.dial.setValue(angle)  # Sincroniza el dial con el slider
        elif source == 'dial':
            angle = self.dial.value()
            self.slider.setValue(angle)  # Sincroniza el slider con el dial 
        
        angle = self.slider.value()
        self.angle_label.setText(f'Ángulo: {angle}°')
        self.dial.setValue(angle)

        # Obtener el número del servomotor
        servo_num = self.servo_input.text()

        # Convertir el ángulo a ciclo de trabajo de PWM
        duty_cycle = angle / 18 + 2

        if servo_num == '1':
            if not ENTORNO_LOCAL:
                servo1.ChangeDutyCycle(duty_cycle)
        elif servo_num == '2':
            if not ENTORNO_LOCAL:
                servo2.ChangeDutyCycle(duty_cycle)
        else:
            # Mostrar error en label si servo no es válido
            self.angle_label.setText("Servo no encontrado, digite un número 1 o 2.")
            
def main():
    app = QApplication(sys.argv)
    mainWindow = ServoControlApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if not ENTORNO_LOCAL:
            servo1.stop()
            servo2.stop()
            GPIO.cleanup()

