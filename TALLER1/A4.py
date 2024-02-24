# Realice un programa para el cálculo de la resistencia de una RTD de
# platino (PT100) en función de la temperatura.

# La ecuación de Callendar-Van Dusen se expresa como:
#
# R(t)=R(0)(1+A*t+B*t^{2})
#
# Donde:
# 
#     R(T) es la resistencia de la RTD a una temperatura T (en ohmios).
#     R0 es la resistencia nominal de la RTD a 0 °C (100 ohmios para una PT100).
#     A, B y C son coeficientes de la ecuación de Callendar-Van Dusen.
# 
# Los valores típicos de los coeficientes A, B y C para una PT100 son:
# 
#     A = 3.9083e-3 °C^-1
#     B = -5.775e-7 °C^-2
#     C = -4.183e-12 °C^-4

def calcular_resistencia_PT100(temperatura):
    R0 = 100  # Resistencia nominal de la PT100 a 0 °C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12
    
    T = temperatura
    
    R = R0 * (1 + A * T + B * T**2 + C * (T - 100) * T**3)
    return R

temperatura = 25  # Temperatura en grados Celsius
resistencia = calcular_resistencia_PT100(temperatura)
print("Resistencia a", temperatura, "°C:", resistencia, "ohmios")