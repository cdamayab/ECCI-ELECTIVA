# Realice un programa que calcule la fuerza de avance y retroceso
# de un cilindro neumático de doble efecto. Debe establecer previamente
# los valores de presión, así como las dimensiones físicas del cilindro
# para realizar el cálculo.

import math

# Valores de entrada
presion = 100  # Presión aplicada en psi
diametro_embolo = 2  # Diámetro del émbolo en pulgadas
diametro_vastago = 1  # Diámetro del vástago en pulgadas


area_efectiva_avance = math.pi * (diametro_embolo / 2) ** 2
fuerza_avance = presion * area_efectiva_avance  # Calcular la fuerza de avance (F = P * A)
    

area_efectiva_retroceso = math.pi * ((diametro_embolo / 2) ** 2 - (diametro_vastago / 2) ** 2)
fuerza_retroceso = presion * area_efectiva_retroceso    # Calcular la fuerza de retroceso (F = P * A)
    

# Mostrar resultados
print("Fuerza de avance:", fuerza_avance, "libras")
print("Fuerza de retroceso:", fuerza_retroceso, "libras")