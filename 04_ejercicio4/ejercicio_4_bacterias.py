while True:
    try:    
        tiempo = int(input(f"ingrese cuanto tiempo dejara reproducciendose las bacterias "))
        bacterias_total =  pow(2, tiempo)
        
        print(f"Pasaron {tiempo} horas, La cantidad de bacterias actualmente es de : {bacterias_total}")
        break

    except ValueError:
            print("Solo puedes ingresar números enteros. Intenta de nuevo.")