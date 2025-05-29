import math

#metodo para calcular el radio
def calcular_area_circulo(radio):
    
    if radio < 0: 
        return False, f"Radio: no puede ser un valor negativo", None
    else:
        area = math.pi * (radio ** 2)
        return True, None, area
    
#metodo para calcular el volumen   
def calcular_volumen_cilindro(area_base_calculada, altura_ingresada):
    if altura_ingresada < 0:
        return False, f"Altura: no puede ser un valor negativo", None
    else:
        volumen = area_base_calculada * altura_ingresada
        return True, None, volumen
    
while True:
    try:
        
        # 1. Pedir el radio para calcular el área de la base
        radio_ingresado = float(input("Ingrese el valor del radio de la base (para área y volumen): "))
        
         # 2. Calcular el área de la base
        valido_area, error_area, area_base_calculada = calcular_area_circulo(radio_ingresado)

        if valido_area:
            print(f"El área de la base (círculo) es: {area_base_calculada:.2f}\n")

            # 3. Pedir la altura para el cilindro
            altura_ingresada = float(input("Ingrese el valor de la altura del cilindro: "))

            # 4. Calcular el volumen del cilindro usando el área de la base calculada
            valido_volumen, error_volumen, volumen_final = calcular_volumen_cilindro(area_base_calculada, altura_ingresada)

            if valido_volumen:
                print(f"El volumen del cilindro es: {volumen_final:.2f}\n")
                break # Si todo esta correcto, salimos del bucle
            else:
                print(f"{error_volumen} Por favor, intente de nuevo.\n")
        else:
            print(f"{error_area} Por favor, intente de nuevo.\n")
            
    except ValueError:
        print("Error: Por favor, ingrese solo números") 