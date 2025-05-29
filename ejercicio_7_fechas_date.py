from datetime import datetime, date
from datetime import timedelta

# Método A: Edad total en días
def calcular_edad_en_dias(fecha_nacimiento):
    hoy = date.today()
    diferencia = hoy - fecha_nacimiento
    edad_timedelta = timedelta(days=diferencia.days)
    return edad_timedelta.days

# Método B: Edad en años, meses y días
def calcular_edad_ymd(fecha_nacimiento):
    hoy = date.today()
    años = hoy.year - fecha_nacimiento.year     
    meses = hoy.month - fecha_nacimiento.month
    dias = hoy.day - fecha_nacimiento.day 

    if dias < 0: # si los días resultan valores negativos
       meses -= 1 #reducimos el mes en 1
       dias += 31  # sumamos 31 días para ajustar valores negativos

    if meses < 0: # si los meses resultan valores negativos
        años -= 1 # reducimos el año en 1
        meses += 12 # sumamos 12 meses para ajustar valores negativos
    return años, meses, dias 
    
# Metodo para validar datos   
def validar_datos(año,mes,dia): 
    hoy = date.today()
    
    #al usar "if not" verificamos que las variables (año, mes y dia) no esten dentro de los rangos
    if not (1900 <= año <= hoy.year): #si el año ingresado (variable año) es menor que 1900 o mayor que el año actual, entonces la condición es verdadera
        return False, f"Año inválido. Debe ingresar un valor entre 1900 y {hoy.year}."
    if not (1 <= mes <= 12): #si el mes ingresado (variable mes) es menor que 1 o mayor que 12, entonces la condición es verdadera
        return False, "Mes inválido. Debe ingresar un valor entre 1 y 12."
    if not (1 <= dia <= 31): #si el dia ingresado (variable dia) es menor que 1 o mayor que 31, entonces la condición es verdadera
        return False, f"Día inválido. Debe ingresar un valor entre 1 y 31."
    return True, None
    
# Metodo Epoch\timestamp   
def calcular_timestamp (fecha_timestamp):
    hoy = datetime.now()
    timestamp_nacimiento = datetime.timestamp(fecha_timestamp)
    timestamp_actual = datetime.timestamp(hoy)
    return timestamp_nacimiento, timestamp_actual

while True:
    try:
        # Pedir los datos
        año = int(input("Introduce tu año de nacimiento "))
        mes = int(input("Introduce tu mes de nacimiento "))
        dia = int(input("Introduce tu día de nacimiento "))        
                
        valido, mensaje_error = validar_datos(año, mes, dia)
        
        if valido: 
            fecha_nacimiento = date(año, mes, dia) # formato date: YYYY-MM-año-mes-día)
            fecha_timestamp = datetime(año, mes, dia) # formato datetime: YYYY-MM-DD HH:MM:SS.microsegundos (incluye horario con precisión)
        
            # Calcular edades
            edad_dias = calcular_edad_en_dias(fecha_nacimiento)
            años, meses, dias = calcular_edad_ymd(fecha_nacimiento)
            
            # Timestamp
            seg_nacimiento_timestamp, seg_actual_timestamp = calcular_timestamp(fecha_timestamp)
            
            # Mostrar resultados
            print(f"Tu fecha de nacimiento es {fecha_nacimiento}")
            print(f"\nA) Has vivido aproximadamente: {edad_dias} días.")
            print(f"B) Tu edad es: {años} años, {meses} meses y {dias} días.")
            print(f"Segundos hasta la fecha de nacimiento {seg_nacimiento_timestamp}")
            print(f"Segundos hasta la fecha actual {seg_actual_timestamp}")
            #break
            
        else:
            print(f"Error: {mensaje_error} Por favor, intenta de nuevo.\n")
    except ValueError:
        print("Error: Solo puedes ingresar números enteros")