while True:
    try:
        n_dec = int(input(f"ingrese un numero "))
               
        n_bin = bin(n_dec)
        n_hex = hex(n_dec)

        print(f"Usando el sistema decimal, su numero ingresado {n_dec} es = {n_dec}")
        print(f"Usando el sistema binario, su numero ingresado {n_dec} es = {n_bin}")
        print(f"Usando el sistema hexadecimal, su numero ingresado {n_dec} es = {n_hex}")
        break
        
    except ValueError:
            print("Solo puedes ingresar números enteros. Intenta de nuevo.")