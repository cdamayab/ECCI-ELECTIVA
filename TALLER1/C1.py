# Realice un programa que grafique el comportamiento de un sensor
# PT100 desde -200°C a 200°C.

import matplotlib.pyplot as plt
import numpy as np

# Definir el rango de temperaturas
temperaturas = np.linspace(-200, 200, 1000)

# Calcular la resistencia para cada temperatura utilizando la ecuación de Callendar-Van Dusen
R0 = 100  # Resistencia nominal de la PT100 a 0°C (100 ohmios)
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

def resistencia_pt100(temperatura):
    return R0 * (1 + A * temperatura + B * temperatura**2 + C * (temperatura - 100) * temperatura**3)

# Calcular la resistencia para cada temperatura en el rango especificado
resistencias = resistencia_pt100(temperaturas)

# Graficar el comportamiento de la PT100
plt.plot(temperaturas, resistencias, color='blue')
plt.title('Comportamiento de un sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (ohmios)')
plt.grid(True)
plt.show()