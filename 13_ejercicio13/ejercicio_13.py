#Ejercicio 13

# Metodo para crear la matriz
def crear_matriz(n):
    matriz_generada = []
    contador = 1
    for filas in range(dimension):
        fila = []
        for columnas in range(dimension):
            fila.append(contador)
            contador += 1
        matriz_generada.append(fila)
    return matriz_generada

# Metodo para imprimir en forma de cuadricula 
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:3}", end= " ")  
        print()  

# Metodo para sumar las diagonales principal(1, 6, 11, 16) contra diagonal(4, 7, 10, 13)
def suma_diagonales(matriz):
    suma_principal = 0
    suma_contra = 0
    for i in range(dimension):
        suma_principal += matriz[i][i] # (0,0) (1,1)  (2,2) (3,3)
        suma_contra += matriz[i][dimension - 1 - i] # (0,3) (1,2) (2,1) (3,0)
    return suma_principal, suma_contra

# Metodo para multiplicar las diagonales principal(1, 6, 11, 16) contra diagonal(4, 7, 10, 13)
def producto_diagonales(matriz):
    mul_principal = 1
    mul_contra = 1
    for i in range(dimension):
        mul_principal *= matriz[i][i] 
        mul_contra *= matriz[i][dimension - 1 - i]
    return mul_principal, mul_contra

# inicio
dimension = 4
matriz = crear_matriz(dimension)

#imprimimos la matriz
print(matriz)
print()

#imprimimos la matriz en forma de cuadricula
imprimir_matriz(matriz)
print()

# Calcular y mostrar sumas de diagonales
suma_principal, suma_contra = suma_diagonales(matriz)
print("➕ Suma de diagonales:")
print("↘ Diagonal principal:",suma_principal)
print("↙ Contra Diagonal:",suma_contra)
print()

# Calcular y mostrar productos de diagonales
producto_principal, producto_contra = producto_diagonales(matriz)
print("✖️ Producto de diagonales:")
print("↘ Diagonal principal:",producto_principal)
print("↙ Contra Diagonal:",producto_contra)


