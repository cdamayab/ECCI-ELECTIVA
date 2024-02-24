# Realice un programa que le permita al usuario ingresar los coeficientes
# de una función de transferencia de segundo orden y graficar su comportamiento,
# además se debe mostrar que tipo de sistema es: subamortiguado, criticamente
# amortiguado y sobreamortiguado.

import numpy as np
import matplotlib.pyplot as plt

# Ejemplo de cómo ingresar los coeficientes:
# Si la función de transferencia es de la forma K / (s^2 + 2*zeta*wn*s + wn^2),
# el usuario ingresaría los coeficientes como sigue:
# Ingrese el coeficiente de ganancia K: 1
# Ingrese la frecuencia natural wn: 2
# Ingrese el coeficiente de amortiguamiento zeta: 0.5

# Solicitar al usuario que ingrese los coeficientes de la función de transferencia
K = float(input("Ingrese el coeficiente de ganancia K: "))
wn = float(input("Ingrese la frecuencia natural wn: "))
zeta = float(input("Ingrese el coeficiente de amortiguamiento zeta: "))

# Calcular los polos de la función de transferencia
s1 = -wn * (zeta + np.sqrt(zeta**2 - 1))
s2 = -wn * (zeta - np.sqrt(zeta**2 - 1))

# Graficar la respuesta al escalón unitario
t = np.linspace(0, 10, 1000)
y = K * (1 - (np.exp(-zeta * wn * t) * (np.cos(np.sqrt(1 - zeta**2) * wn * t) + (zeta / np.sqrt(1 - zeta**2)) * np.sin(np.sqrt(1 - zeta**2) * wn * t))))

plt.plot(t, y)
plt.title('Respuesta al escalón unitario')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

# Determinar el tipo de sistema
if zeta < 1:
    print("El sistema es subamortiguado.")
elif zeta == 1:
    print("El sistema es críticamente amortiguado.")
else:
    print("El sistema es sobreamortiguado.")
