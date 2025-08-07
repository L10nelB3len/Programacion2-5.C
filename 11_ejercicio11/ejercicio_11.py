#Ejercicio 11
import random

#Lista de estudiantes
lista_estudiantes = ["Sofía", "Lionel", "Valentina", "Martín", "Camila",
    "Julián", "Florencia", "Mateo", "Carla", "Alan"]

#Nueva lista con orden aleatorio
orden_exposicion = []
#La función random.sample() genera un orden aleatorio de estudiantes sin modificar la lista original
for estudiante in random.sample(lista_estudiantes, len(lista_estudiantes)):
    orden_exposicion.append(estudiante)

print("🗣🔥🔥 Orden de exposición:")
#La función enumerate() toma la lista 'orden_exposicion' y devuelve un iterador que produce pares (índice, nombre)
for i, nombre in enumerate(orden_exposicion, start=1):
    print(f"{i}. {nombre}")

"""
                                                    -Lista de metodos que se usan en el codigo-
len(): Devuelve la cantidad de elementos en una lista
random,sample(): Devuelve una nueva lista con elementos aleatorios sin repetir
append(): Agrega un elemento al final de una lista
enumerate(): Devuelve un iterador que produce pares de valores: el índice y el elemento

"""



   
