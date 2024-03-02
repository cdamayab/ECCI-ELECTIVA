# Realice un programa que le permita al usuario escoger entre robot
# Cilíndrico, Cartesiano y esférico, donde como respuesta a la selección
# conteste con el tipo y número de articulaciones que posee.

# Menú de opciones
print("Seleccione el tipo de robot:")
print("1. Cilíndrico")
print("2. Cartesiano")
print("3. Esférico")

# Opcion del usuario
opcion = int(input("Ingrese el número correspondiente al tipo de robot: "))

if opcion == 1:
    tipo_robot = "Cilíndrico"
    tipo_articulaciones = "1 articulación rotacional y dos prismáticas prismáticas"
    numero_articulaciones = "2"
elif opcion == 2:
    tipo_robot = "Cartesiano"
    tipo_articulaciones = "3 articulaciones prismáticas"
    numero_articulaciones = "3"
elif opcion == 3:
    tipo_robot = "Esférico"
    tipo_articulaciones = "2 articulaciones rotacionales y 1 prismáticas"
    numero_articulaciones = "3"
else:
    print("Opción no válida")
    exit()

print("El robot", tipo_robot, "posee ", tipo_articulaciones, ", tiene", numero_articulaciones, "articulaciones.")
