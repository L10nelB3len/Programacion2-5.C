import customtkinter as ctk
import tkinter as tk
from tkinter import font
import random
import pygame
import os

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")


# Variables globales
secreto = random.randint(1, 20)
intentos = 6

# Música
pygame.init()
pygame.mixer.music.load("sound2.mp3")  #pista de audio
pygame.mixer.music.play(-1) #loop

# Ventana principal
ventana = ctk.CTk()
ventana.geometry("450x400") #dimension de la ventana
ventana.title("🎮 Adivina el numero") #nombre del programa
ventana.bind("<Return>", lambda event: verificar())
fondo = ctk.CTkFrame(master=ventana, fg_color="#000000") #color solido de fondo
fondo.pack(fill="both", expand=True) #se ajusta a la ventana


#Fuente personalizada 
fuente_nombre = "MonsterFriendBack"
fuente_personalizada = ctk.CTkFont(family=fuente_nombre, size=12)

#Metodo para verificar lo ingresado por los usarios
def verificar():
    global intentos
    entrada = entry.get()
    if not entrada.isdigit():
        mensaje.configure(text="Solo puedes ingresar numeros enteros")
        return

    num = int(entrada)
    intentos -= 1
    
    if num == secreto:
        mensaje.configure(text=f"¡Adivinaste! El numero era: {secreto}")
        boton_intentar.configure(state="disabled")
        frame_boton_reiniciar.place(relx=0.5, rely=0.85, anchor="center")
    elif intentos == 0:
        mensaje.configure(text=f"Se acabaron los intentos \nEl numero secreto era: {secreto}")
        boton_intentar.configure(state="disabled")
        frame_boton_reiniciar.place(relx=0.5, rely=0.85, anchor="center")
    else:
        pista = "alto" if num > secreto else "bajo"
        mensaje.configure(text=f"Tu numero es muy {pista} \nIntentos restantes: {intentos}")


#Metodo para el boton de reiniciar
def reiniciar():
    global secreto, intentos
    secreto = random.randint(1, 20)
    intentos = 6
    entry.delete(0, tk.END)
    mensaje.configure(text="")
    boton_intentar.configure(state="normal")
    frame_boton_reiniciar.place_forget() 


# Título
ctk.CTkLabel(fondo, text="Adivina un numero entre 1 y 20", font=ctk.CTkFont(family=fuente_nombre, size=16)).pack(pady=10)

# Entrada
entry = ctk.CTkEntry(fondo, font=ctk.CTkFont(family=fuente_nombre, size=14), width=200)
entry.pack(pady=5)


# Frame externo blanco para Caja de diálogo 
frame_borde = tk.Frame(fondo, bg="white", bd=0)
frame_borde.pack(pady=10)

# Caja de diálogo 
mensaje = ctk.CTkLabel(
    master=frame_borde,
    text="",
    font=ctk.CTkFont(family="MonsterFriendBack", size=12),
    width=296,
    height=56,
    corner_radius=0,
    fg_color="#000000",
    text_color="#FFFFFF",
    wraplength=280,
    justify="center"
)
mensaje.pack(padx=2, pady=2)

# Frame externo naranja para el botón Adivinar
frame_boton = tk.Frame(fondo, bg="orange", bd=0)
frame_boton.pack(pady=10)

# Botón adivinar
boton_intentar = ctk.CTkButton(
    master=frame_boton,
    text="ADIVINAR",
    command=verificar,
    font=ctk.CTkFont(family="MonsterFriendBack", size=18),
    width=296,
    height=56,
    corner_radius=0,
    fg_color="#000000",
    text_color="#ff9f40"
    
)
boton_intentar.pack(padx=2, pady=2)


# Frame externo naranja para el botón Reiniciar 
frame_boton_reiniciar = tk.Frame(ventana, bg="orange", bd=0)

# Botón Reiniciar 
boton_reiniciar = ctk.CTkButton(
    master=frame_boton_reiniciar,
    text="REINICIAR",
    command=reiniciar,
    font=ctk.CTkFont(family="MonsterFriendBack", size=18),
    width=296,
    height=56,
    corner_radius=0,
    fg_color="#000000",
    text_color="#ff9f40"
)
boton_reiniciar.pack(padx=2, pady=2)
frame_boton_reiniciar.place_forget() 

ventana.mainloop()
