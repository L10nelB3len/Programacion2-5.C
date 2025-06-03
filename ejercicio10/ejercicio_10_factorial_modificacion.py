def factorial(num):
    
    if num < 0 :
        return False, f"No factorizo numeros negativos, intenta de nuevo", None
    elif num == 0 or num == 1:
        return True, None, 1
    else:
        factorial = 1
        for i in range (1, num+1):
            factorial *= i
        return True, None, factorial

       
def proceso(num):
    if  num == 0 or num == 1:
        return "1" 
    else:
        # Construimos la lista de strings(cadena de texto) con los números
        lista_numeros = [str(i) for i in range(1, num + 1)] # []creamos la lista, str(i) Toma el valor actual de i y lo convierte a una cadena de texto
        # Unimos la lista con " x " y retornamos el resultado
        return " x ".join(lista_numeros) #.join() es un método de las cadenas, nos permite concatenar (unir) los elementos de una secuencia (lista_numeros)
           # "x" sera el elemento (separador) que une a los elementos de la lista ej: lista_numeros es [1, 2 ,3] el resultado usando .join() sera "1 x 2 x 3"
while True:
    
    try:
        
        num=int(input("ingrese el numero para factorisar "))
        
        # Llama a la función factorial para validar y calcular.
        validar, mensaje_error, resultado = factorial(num)
        # Llama a la función proceso para obtener la cadena de pasos.
        proceso_cadena = proceso(num)
        
        
         # Si el número es válido y el factorial se calculó, muestra los resultados.
        if validar:
            print(f"\nEl factorial de {num} es: {resultado}")
            print(f"{num}! = {resultado}")
            
            print("\nEl proceso es el siguiente:")
            print(f"{num}! = {proceso_cadena}")
        else:
            print (f"{mensaje_error}")
        
    except ValueError:
        print("Error: Solo puedes ingresar números enteros")
