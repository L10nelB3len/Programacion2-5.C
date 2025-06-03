while True:
    try:  
        caramelos = int(input("¿Cuántos caramelos se van a repartir? "))

        estudiantes = int(input("¿Entre cuántos estudiantes se van a repartir? "))

        if estudiantes == 0:
            print("No es posible repartir caramelos entre 0 estudiantes.")
        elif caramelos == 0:
            print("Parece que no hay caramelos que repartir (gil)")
        else:
            caramelos_por_estudiante = caramelos // estudiantes
            sobrantes = caramelos % estudiantes


            print(f"Cada estudiante recibirá {caramelos_por_estudiante} caramelos.")

        if sobrantes > 0:
           print(f"Sobran {sobrantes} caramelos en la bolsa.")
        else:
           print("No sobran caramelos.")
           
        #break
    except ValueError:
            print("Solo puedes ingresar números enteros. Intenta de nuevo.")