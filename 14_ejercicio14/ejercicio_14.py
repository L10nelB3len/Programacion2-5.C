from PIL import Image
import numpy as np

#1 Cargamos la imagen
imagen = Image.open('imagen/gojo.jpg')

#2 Convertimos a escala de grises
imagen_gris = imagen.convert('L')

#3 Convertir a matriz NumPy
matriz = np.array(imagen_gris)

#4 Voltear horizontalmente (invertir columnas)
matriz_volteada = np.fliplr(matriz)

#5 Convertir la matriz volteada a imagen
imagen_volteada = Image.fromarray(matriz_volteada)

#6 Mostrar imagen volteada
imagen_volteada.show()
