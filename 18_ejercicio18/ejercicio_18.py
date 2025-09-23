import tkinter as tk
import random

# Inicialización
secreto = random.randint(1, 20)
intentos = 6

def verificar():
    global intentos
    try:
        num = int(entry.get())
        intentos -= 1

        if num > secreto:
            mensaje.set(f"Tu número es muy alto.\nIntentos restantes: {intentos}")
        elif num < secreto:
            mensaje.set(f"Tu número es demasiado bajo.\nIntentos restantes: {intentos}")
        else:
            mensaje.set(f"🎉¡Adivinaste! el número secreto: {secreto}")
            boton.config(state="disabled")
            return

        if intentos == 0 and num != secreto:
            mensaje.set(f"😢 Se acabaron los intentos.\nEl número secreto era: {secreto}")
            boton.config(state="disabled")

    except ValueError:
        mensaje.set("Solo puedes ingresar números enteros.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Juego: Adivina el número")

tk.Label(ventana, text="Adivina un número entre 1 y 20").pack()

entry = tk.Entry(ventana)
entry.pack()

boton = tk.Button(ventana, text="Intentar", command=verificar)
boton.pack()

mensaje = tk.StringVar()
tk.Label(ventana, textvariable=mensaje, wraplength=300).pack()

ventana.mainloop()
