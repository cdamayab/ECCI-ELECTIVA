# Escribir un programa que realice la pregunta ¿Desea continuar Si/No?
# y que no deje de hacerla hasta que el usuario teclee No.

while True:
    respuesta = input("¿Desea continuar? (Si/No): ")
    if respuesta.lower() == "no":
        print("¡Hasta luego!")
        break
