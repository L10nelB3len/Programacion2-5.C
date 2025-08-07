#ejercicio 12
import string

# Método 1: Cifrado César utilizando tablas de traducción con str.translate() y str.maketrans().
def aplicar_cifrado_cesar(mensaje: str, desplazamiento: int, descifrado: bool = False):
    if descifrado:
        desplazamiento = -desplazamiento

    alfabeto = string.ascii_lowercase 
    alfabeto_desplazadas = alfabeto[desplazamiento:] + alfabeto[:desplazamiento]
    tabla_traduccion = str.maketrans(
        alfabeto + alfabeto.upper(),
        alfabeto_desplazadas + alfabeto_desplazadas.upper()
       )

    texto_convertido = mensaje.translate(tabla_traduccion)
    return texto_convertido

mensaje_original = "Sister Hong"
mensaje_cifrado = aplicar_cifrado_cesar(mensaje_original, 3)
mensaje_descifrado = aplicar_cifrado_cesar(mensaje_cifrado, 3, descifrado=True)

print("Cifrado:", mensaje_cifrado)
print("Descifrado:", mensaje_descifrado)



# Método 2: Cifrado César mediante manipulación directa de códigos Unicode con ord() y chr()
mensaje= "Sister Hong"
def aplicar_cifrado_cesar(mensaje, desplazamiento):
        cifrado = ""
        for letra in mensaje:
            if letra.isalpha(): #solo letras
                if letra.islower(): #comprueba si es minuscula
                    base = ord('a') #a = 97
                else:
                    base = ord('A') #A = 65
                nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)
                cifrado += nueva_letra #concatena la nueva letra al contenido actual de la variable cifrado (esta comienza como una cadena vacia)
            else:
                cifrado += letra #conserva espacios y signos y los concatena a la variable cifrado
        return  cifrado
    
mensaje_cifrado = aplicar_cifrado_cesar(mensaje, 3)
mensaje_descifrado = aplicar_cifrado_cesar(mensaje_cifrado, -3)

print("Cifrado:", mensaje_cifrado)
print("Descifrado:", mensaje_descifrado)

