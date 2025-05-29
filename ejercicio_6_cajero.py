while True:
    try:  
        extraccion = int(input("Ingresa la cantidad que desea extraer "))

        print("IMPORTANTE! Las extracciones solo se realizan en Billetes de $200 y $1000")

        billetes_1000 = extraccion // 1000


        print(f"El monto que desea extraer es de {extraccion}")

        billetes_200 =  extraccion % 1000 // 200
        saldo_sin_extraer = extraccion % 1000 % 200

       
        print(f"la cantidad en billetes de $1000 es {billetes_1000}")
        print(f"la cantidad en billetes de $200 es {billetes_200}")

        if saldo_sin_extraer  > 0:
            print(f"Por falta de billetes no fue posible extraer el monto completo")
            print (f"La cantidad de saldo sin extraer es de ${saldo_sin_extraer}")
            
        #break
    except ValueError:
        print("Solo puedes ingresar números enteros. Intenta de nuevo.")