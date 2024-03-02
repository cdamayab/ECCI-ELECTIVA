import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Solicitar los datos
K = float(input("Ingrese el coeficiente de ganancia K: "))
wn = float(input("Ingrese la frecuencia natural wn: "))
zeta = float(input("Ingrese el coeficiente de amortiguamiento zeta: "))

# Crear la función de transferencia
num = [K * wn**2]
den = [1, 2 * zeta * wn, wn**2]
sys = ctl.TransferFunction(num, den)

# Determinar el tipo de sistema
damping_ratio = zeta
if damping_ratio < 1:
    print("El sistema es subamortiguado.")
elif damping_ratio == 1:
    print("El sistema es críticamente amortiguado.")
else:
    print("El sistema es sobreamortiguado.")
    
# Graficar la respuesta al escalón unitario
t, y = ctl.step_response(sys)
plt.plot(t, y)
plt.title('Respuesta al escalón unitario')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()


