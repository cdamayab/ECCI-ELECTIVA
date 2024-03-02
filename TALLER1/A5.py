# Realice en funciones las rotaciones en X, Y y Z, donde se tenga
# un parámetro de entrada (ángulo) y un parámetro de salida (matriz).

import numpy as np

def rotacion_x(angulo):
    angulo_rad = np.radians(angulo) # Convertir el ángulo a radianes
    return  np.array([[1, 0, 0],
                        [0, np.cos(angulo_rad), -np.sin(angulo_rad)],
                        [0, np.sin(angulo_rad), np.cos(angulo_rad)]])


def rotacion_y(angulo):
    angulo_rad = np.radians(angulo) # Convertir el ángulo a radianes
    return np.array([[np.cos(angulo_rad), 0, np.sin(angulo_rad)],
                        [0, 1, 0],
                        [-np.sin(angulo_rad), 0, np.cos(angulo_rad)]])

def rotacion_z(angulo):
    angulo_rad = np.radians(angulo) # Convertir el ángulo a radianes
    return np.array([[np.cos(angulo_rad), -np.sin(angulo_rad), 0],
                        [np.sin(angulo_rad), np.cos(angulo_rad), 0],
                        [0, 0, 1]])

angulo = 45  # Ángulo de rotación en grados

print("Matriz de rotación en el eje X:\n", rotacion_x(angulo))
print("\nMatriz de rotación en el eje Y:\n",  rotacion_y(angulo))
print("\nMatriz de rotación en el eje Z:\n", rotacion_z(angulo))