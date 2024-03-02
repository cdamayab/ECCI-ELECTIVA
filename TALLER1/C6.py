import cv2

# Cargar la imagen original
imagen_original = cv2.imread('logo2.jpg')
imagen_original = cv2.resize(imagen_original, None, fx=0.5, fy=0.5)  # Redimensionar a la mitad

gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)    # Convertir a escala de grises
blanco_negro = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)  # Aplicar umbral adaptativo
blanco_negro = cv2.medianBlur(blanco_negro, 5)  # Aplicar filtro de suavizado para eliminar el ruido
contornos, _ = cv2.findContours(blanco_negro, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Encontrar contornos en la imagen en blanco y negro

# Dibujar los contornos en la imagen original
imagen_contornos = imagen_original.copy()
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Crear un mosaico con todas las imágenes
mosaico = cv2.hconcat([imagen_original, imagen_contornos])
print(mosaico)

# Mostrar el mosaico
cv2.imshow('Mosaico', mosaico)
cv2.waitKey(0)
cv2.destroyAllWindows()
