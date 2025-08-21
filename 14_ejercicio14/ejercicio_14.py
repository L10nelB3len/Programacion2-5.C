from PIL import Image
import numpy as np

#metodo para invertir la matriz
def invertir_columnas(matriz):
    filas = len(matriz)  
    columnas = len(matriz[0])
    matriz_invertida = []

    #Inicialización de matriz vacía con ceros
    for i in range(filas):
        fila = [0] * columnas       
        matriz_invertida.append(fila)

    #Inversión horizontal: copiar columnas en orden inverso
    for i in range(filas):
        for j in range(columnas):
            matriz_invertida[i][j] = matriz[i][columnas - 1 - j]
    return matriz_invertida

#1 Cargamos la imagen
imagen = Image.open('imagen/gojo.jpg')

#2 Convertimos a escala de grises
imagen_gris = imagen.convert('L')

#3 Convertir a matriz NumPy
matriz = np.array(imagen_gris)

print(matriz)
#4 Voltear horizontalmente (invertir columnas)
matriz_invertida = invertir_columnas(matriz)
        
#5 Convertir la matriz volteada a imagen
imagen_volteada = Image.fromarray(np.array(matriz_invertida))

#6 Mostrar imagen volteada
imagen_volteada.show()
