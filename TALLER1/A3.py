# Realice un programa que convierta coordenadas rectangulares a
# cilíndricas y esféricas, para lo cual deben consultar sobre el uso
# de funciones trigonométricas en Python.

import numpy as np

def cartesianas_a_cilindricas(x, y, z):
    r = np.sqrt(x**2 + y**2)  
    theta = np.arctan2(y, x)  
    return r, theta, z  

def cartesianas_a_esfericas(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2) 
    theta = np.arctan2(y, x)  
    phi = np.arccos(z / r) 
    return r, theta, phi 

# Coordenadas rectangulares
x = 1
y = 1
z = 1

r_cyl, theta_cyl, z_cyl = cartesianas_a_cilindricas(x, y, z)
print("Coordenadas cilíndricas:", r_cyl, theta_cyl, z_cyl)

r_sph, theta_sph, phi_sph = cartesianas_a_esfericas(x, y, z)
print("Coordenadas esféricas:", r_sph, theta_sph, phi_sph)
