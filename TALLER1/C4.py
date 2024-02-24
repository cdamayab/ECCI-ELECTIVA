# Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un
# vector con coordenadas ingresadas por el usuario.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Solicitar al usuario que ingrese las coordenadas del vector
x = float(input("Ingrese la coordenada x del vector: "))
y = float(input("Ingrese la coordenada y del vector: "))
z = float(input("Ingrese la coordenada z del vector: "))

# Crear la figura y el sistema de coordenadas 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el sistema de coordenadas X, Y, Z
ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')

# Dibujar el vector ingresado por el usuario
ax.quiver(0, 0, 0, x, y, z, color='m', label='Vector')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sistema de coordenadas 3D')

# Ajustar los límites del gráfico para que se muestren todos los ejes
max_range = np.array([x, y, z]).max()
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])
ax.legend()
plt.show()
