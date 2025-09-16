from PIL import Image
import numpy as np


#metodo para rotar la matriz 180°
def rotar_180(matriz):
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

#metodo para rotar la matriz 90° a la derecha
def rotar_90_derecha(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_rotada = []

    # Inicializar matriz vacía con dimensiones invertidas
    for i in range(columnas):
        fila = [0] * filas
        matriz_rotada.append(fila)

    # Reorganización de elementos: las filas se convierten en columnas
    for i in range(filas):
        for j in range(columnas):
            matriz_rotada[j][filas - 1 - i] = matriz[i][j] 
    return matriz_rotada

#metodo para rotar la matriz 90° a la izquierda
def rotar_90_izquierda(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_rotada = []

    # Inicializar matriz vacía con dimensiones invertidas
    for i in range(columnas):
        fila = [0] * filas
        matriz_rotada.append(fila)

    # Reorganización de elementos: las filas se convierten en columnas
    for i in range(filas):
        for j in range(columnas):
            matriz_rotada[columnas - 1 - j][i] = matriz[i][j] 
    return matriz_rotada


#inicio
imagen = Image.open('imagen/ludopata.jpeg')
matriz =  np.array(imagen)

while True:
    opcion = input(
    "¿Cómo te gustaría rotar la imagen?\n"
    "1. 90° a la derecha\n"
    "2. 90° a la izquierda\n"
    "3. 180°\n"
    "4. Salir\n"
    "👉 Ingresa una de las opciónes: "
)

    if opcion == "1":
        matriz = rotar_90_derecha(matriz)
    elif opcion == "2":
        matriz = rotar_90_izquierda(matriz)
    elif opcion == "3":
        matriz = rotar_180(matriz)
    elif opcion == "4":
        print("¡Programa Finalizado!")
        break
    else:
        print("Opción no válida.")
        continue

    Image.fromarray(np.array(matriz)).show()
    imagen.show()
    

    
    