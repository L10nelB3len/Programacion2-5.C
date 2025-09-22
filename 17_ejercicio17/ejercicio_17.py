from PIL import Image
import numpy as np

# Filtro gaussiano 3x3 simple
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) / 16

# Método para aplicar filtro gaussiano
def desenfoque(matriz):
    height, width, _ = matriz.shape
    output = np.zeros_like(matriz)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for c in range(3):  # Para cada canal de color (RGB)
                suma = 0
                for ki in range(-1, 2):
                    for kj in range(-1, 2):
                        suma += matriz[i + ki][j + kj][c] * kernel[ki + 1][kj + 1]
                output[i][j][c] = int(suma)
    return output

# Inicio
imagen = Image.open('imagen/imagen.jpg')
matriz = np.array(imagen)

matriz_desenfocada = desenfoque(matriz)
imagen_desenfocada = Image.fromarray(matriz_desenfocada.astype(np.uint8))

imagen_desenfocada.show()
