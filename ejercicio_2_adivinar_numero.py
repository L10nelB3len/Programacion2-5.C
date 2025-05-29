import random
secreto = random.randint(1, 20)
intento = 1
apuntador = 0

#print(f"{secreto}")
print("¡Bienvenido! Se ha generado un número secreto entre 1 y 20. Tienes 6 intentos para adivinarlo. ¡Buena suerte!")


while apuntador<6:
    intento = 6-apuntador
    try:
        num = int(input("Ingrese un numero para comenzar a jugar "))

        if num > secreto:
            print(f"¡Casi! Pero tu número es demasiado alto. Intenta algo más pequeño")
            print(f"Te quedan {intento} intentos restantes")
            print("")
            apuntador += 1
            
        elif num < secreto:
            print(f"Uh-oh, tu número es demasiado bajo. ¡Piensa más grande! Intenta otra vez")
            print(f"Te quedan {intento} intentos restantes")
            print("")
            apuntador += 1
            
        else:
            print(f"Increíble! Adivinaste el número secreto, el numero secreto era: {secreto}.")
            print("")
            break
        
    except ValueError:
        print("Solo puedes ingresar números enteros. Intenta de nuevo.")
        
if apuntador == 6:
    print(f"¡Qué lástima! Se terminaron los intentos. El número secreto era: {secreto}. ¿Quieres intentarlo de nuevo?")
        