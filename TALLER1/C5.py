# Dibuje el nombre de cada uno de los integrantes del grupo en un plot
# en 2D, teniendo en cuenta líneas rectas y/o curvas.

import matplotlib.pyplot as plt
import numpy as np

# Arreglos con las coordenadas para cada letra
coordenadas = {
    "C": np.array([[10, 0], [0, 0], [0, 10], [10, 10]]),
    "r": np.array([[15, 0], [15, 10], [15, 8], [18, 9]]),
    "i": np.array([[25, 0], [25, 10]]),
    "s": np.array([[30, 0], [35, 0], [35, 5], [30, 5], [30, 10], [35, 10]]),
    "t": np.array([[45, 0], [45, 10], [40, 10], [50, 10]]),
    "h": np.array([[55, 0], [55, 10], [55, 5], [60, 5], [60, 0], [60, 10], [60, 5]]),
    "I": np.array([[65, 0], [65, 10]]),
    "a": np.array([[70, 0], [75, 10], [80, 0], [77.5, 5], [72.5, 5]]),
    "n": np.array([[85, 0], [85, 10], [95, 0], [95, 10]])
}

fig, ax = plt.subplots()

# Se dibuja cada letra 
for letra, coords in coordenadas.items():
    ax.plot(coords[:, 0], coords[:, 1])

ax.set_xlim([-5, 100])
ax.set_ylim([-5, 15])
ax.set_aspect("equal")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Nombre 'Cristhian'")
plt.show()