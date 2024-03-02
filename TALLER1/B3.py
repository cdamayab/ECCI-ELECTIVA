# Realice un programa para el cálculo de volúmenes (Prisma, Pirámide,
# Cono truncado, Cilindro) donde el usuario pueda seleccionar el sólido
# y los parámetros de cada volumen.

import math

def calcular_volumen_prisma(base, altura):
    return base * altura

def calcular_volumen_piramide(base, altura):
    return (1/3) * base * altura

def calcular_volumen_cono_truncado(base_mayor, base_menor, altura):
    return (math.pi * altura / 3) * (base_mayor**2 + base_mayor * base_menor + base_menor**2)

def calcular_volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

# Menú de opciones
print("Seleccione el sólido para calcular su volumen:")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("Ingrese el número correspondiente al sólido: "))

# Calcular el volumen según la opción seleccionada
if opcion == 1:
    base = float(input("Ingrese la medida de la base del prisma en metros: "))
    altura = float(input("Ingrese la altura del prisma en metros: "))
    volumen = calcular_volumen_prisma(base, altura)
    solido = "prisma"
elif opcion == 2:
    base = float(input("Ingrese la medida de la base de la pirámide en metros: "))
    altura = float(input("Ingrese la altura de la pirámide en metros: "))
    volumen = calcular_volumen_piramide(base, altura)
    solido = "pirámide"
elif opcion == 3:
    base_mayor = float(input("Ingrese la medida de la base mayor del cono truncado en metros: "))
    base_menor = float(input("Ingrese la medida de la base menor del cono truncado en metros: "))
    altura = float(input("Ingrese la altura del cono truncado en metros: "))
    volumen = calcular_volumen_cono_truncado(base_mayor, base_menor, altura)
    solido = "cono truncado"
elif opcion == 4:
    radio = float(input("Ingrese el radio del cilindro en metros: "))
    altura = float(input("Ingrese la altura del cilindro en metros: "))
    volumen = calcular_volumen_cilindro(radio, altura)
    solido = "cilindro"
else:
    print("Opción no válida")
    exit()

print("El volumen del", solido, "es:", volumen, " metros cúbicos.")