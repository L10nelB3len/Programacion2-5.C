
# Metodo para calcular el iva
def calcular_factura(monto_factura, tasa_iva):
    
    #Si porcentaje_iva no es None y tampoco es una cadena vacía
    if  tasa_iva is not None and tasa_iva != "": #"is not None" se entiende como: la variable tiene algún valor diferente a None
        tasa_iva_aplicada = tasa_iva / 100 #ej: iva del 10% = 0.1
    else:
        tasa_iva_aplicada = 21 / 100 #0.21
        
    iva_calculado = monto_factura * tasa_iva_aplicada   #ej: 3000 * 0.1(iva del 10%) = 300
    importe_final = monto_factura + iva_calculado #ej: 3000 + 300
    return importe_final

while True:
    try:
        
        monto_factura = float(input("Ingrese el monto de la factura que desea calcular el IVA: "))
        
        iva_ingresado_str = input("Ingrese el IVA a aplicar (21% si no ingresa nada) ")  

        # Verificar si la cadena ingresada no está vacía o solo tiene espacios 
        if iva_ingresado_str.strip(): #.strip() elimina los espacios en blancos, luego se verifica la condicion
            tasa_iva = float(iva_ingresado_str)  # Convertir a número decimal
        else:
            tasa_iva = None  # Asignar None si la entrada está vacía

        
        monto_con_iva = calcular_factura(monto_factura, tasa_iva)
        
        print("")
        print(f"El monto de la factura ingresada es: ${monto_factura} sin I.V.A")
        if tasa_iva is None:
            print("Se aplicará un IVA del 21% por defecto")
        else:
            print(f"Se aplicará un I.V.A del : {int(tasa_iva)}%")
        print(f"El total a pagar con IVA es: ${monto_con_iva:.2f}")
        #break
        
    except ValueError:
        print("Error: Por favor, ingrese solo números para el importe y el IVA.") 
    """except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")"""