# Realice un programa que sume, reste, multiplique (producto punto y
# producto cruz) y divida dos matrices previamente inicializadas.

import numpy as np 

# Matrices a operar
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

suma = matriz1 + matriz2
resta = matriz1 - matriz2
producto_punto = np.sum(matriz1 * matriz2   )# Para matrices, el producto punto se define como la suma de los productos de los elementos correspondientes.
producto_cruz = None    # El producto cruz no está definido para matrices 
division = matriz1 / matriz2    # No definida - Se realiza operacion elemento por elemento

# Imprimimos los resultados
print("Suma de matrices:\n", suma)
print("\nResta de matrices:\n", resta)
print("\nProducto punto:", producto_punto)
print("\nProducto cruz:", producto_cruz)
print("\nDivisión de matrices:\n", division)
