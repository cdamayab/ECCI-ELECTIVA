# Realice un programa que calcule X números aleatorios en un rango
# determinado por el usuario.

import random

# Solicitar al usuario los datos
inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))
cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))

numeros_aleatorios = [random.randint(inicio, fin) for _ in range(cantidad)]

print("Números aleatorios generados:")
for numero in numeros_aleatorios:
    print(numero)