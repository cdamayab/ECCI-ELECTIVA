# Implemente la ecuación de carga y descarga para un circuito RC. El
# usuario ingresa por teclado el valor de voltaje (V), capacitancia (μF) y
# resistencia (Ω). Posteriormente realice en Python la gráfica.

import numpy as np
import matplotlib.pyplot as plt

# Solicitar los valores al usuario
V0 = float(input("Ingrese el voltaje inicial (V): "))
C = float(input("Ingrese la capacitancia (μF): "))
R = float(input("Ingrese la resistencia (Ω): "))

tau = R * C*1e-6     # Constante de tiempo (RC)
t = np.linspace(0, 5 * tau, 1000) # Rango de tiempo para la gráfica

# Calcular el voltaje para carga y descarga
V_carga = V0 * (1 - np.exp(-t / tau))
V_descarga = V0 * np.exp(-t / tau)

plt.plot(t, V_carga, label='Carga del capacitor')
plt.plot(t, V_descarga, label='Descarga del capacitor')
plt.title('Carga y descarga de un capacitor en un circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.show()
