# Realice un programa que calcule la potencia que consume un
# circuito ingresando por teclado el valor de corriente y voltaje.

# Solicitar al usuario que ingrese los valores de voltaje y corriente
voltaje = float(input("Ingrese el voltaje (en voltios): "))
corriente = float(input("Ingrese la corriente (en amperios): "))

potencia = voltaje * corriente

print("La potencia consumida es:", potencia, "Watts")