# Realice un programa que sume, reste, multiplique (producto punto y
# producto cruz) y divida dos vectores previamente inicializados.

import numpy as np  

# Vectores a operar
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

suma = vector1 + vector2
resta = vector1 - vector2
producto_punto = np.dot(vector1, vector2)
producto_cruz = np.cross(vector1, vector2)
division = vector1 / vector2  # No definida - Se realiza operacion elemento por elemento

# Imprimimos los resultados
print("Suma de vectores:", suma)
print("Resta de vectores:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("Division de vectores:", division)