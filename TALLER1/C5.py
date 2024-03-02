# Dibuje el nombre de cada uno de los integrantes del grupo en un plot
# en 2D, teniendo en cuenta líneas rectas y/o curvas.

import matplotlib.pyplot as plt
import numpy as np

# Arreglos con las coordenadas para cada letra
coordenadas = {
    "c": np.array([[10, 0 ], [0, 0 ], [ 0, 10], [10, 10]]),
    "r": np.array([[ 5, 0 ], [5, 10], [ 5, 8 ], [ 8,  9]]),
    "i": np.array([[ 5, 0 ], [5, 10]]),
    "s": np.array([[ 0, 0 ], [5, 0 ], [ 5, 5], [ 0, 5], [ 0, 10], [ 5, 10]]),
    "t": np.array([[ 5, 0 ], [5, 10], [ 0, 10],[10, 10]]),
    "h": np.array([[ 5, 0 ], [5, 10], [ 5, 5], [10, 5], [10, 0], [10, 10], [10, 5]]),
    "I": np.array([[ 5, 0 ], [5, 10]]),
    "a": np.array([[ 0, 0 ], [5, 10], [10, 0], [7.5, 5], [2.5, 5]]),
    "n": np.array([[ 5, 0 ], [5, 10], [15, 0], [15, 10]]),
    "e": np.array([[10, 0 ], [0, 0 ], [ 0, 10], [10, 10],[0, 10],[0, 5],[10, 5]]),
    "l": np.array([[10, 0 ], [0, 0 ], [ 0, 10]]),
    "u": np.array([[ 0, 10], [0, 0 ], [10,  0], [10,  10]]),
    "d": np.array([[ 0, 0 ], [0, 10], [10,  5], [ 0,   0]]),
    "g": np.array([[10, 10], [0, 10], [ 0,  0], [10,   0], [10, 5], [0, 5]]),
    "o": np.array([[ 0,  0], [0, 10], [10, 10], [10,   0], [ 0, 0 ]]),
}

# Función para dibujar una letra en una posición específica
def dibujar_letra(ax, letra, x, y):
    coords = coordenadas[letra]
    ax.plot(coords[:, 0]+x, coords[:, 1]+y)

fig, ax = plt.subplots()

#Nombre1
dibujar_letra(ax, "c", 0, 0)
dibujar_letra(ax, "r",10, 0)
dibujar_letra(ax, "i",20, 0)
dibujar_letra(ax, "s",30, 0)
dibujar_letra(ax, "t",40, 0)
dibujar_letra(ax, "h",50, 0)
dibujar_letra(ax, "I",60, 0)
dibujar_letra(ax, "a",70, 0)
dibujar_letra(ax, "n",80, 0)
#Nombre2
dibujar_letra(ax, "c", 0, -15)
dibujar_letra(ax, "e",12, -15)
dibujar_letra(ax, "s",24, -15)
dibujar_letra(ax, "a",30, -15)
dibujar_letra(ax, "r",40, -15)
#Nombre3
dibujar_letra(ax, "l", 0, -30)
dibujar_letra(ax, "u",12, -30)
dibujar_letra(ax, "i",20, -30)
dibujar_letra(ax, "s",30, -30)
#Nombre4
dibujar_letra(ax, "d", 0, -45)
dibujar_letra(ax, "i",10, -45)
dibujar_letra(ax, "e",18, -45)
dibujar_letra(ax, "g",29, -45)
dibujar_letra(ax, "o",40, -45)

ax.set_xlim([-5, 100])
ax.set_ylim([-50, 15])
ax.set_aspect("equal")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Nombre 'Cristhian'")
plt.show()