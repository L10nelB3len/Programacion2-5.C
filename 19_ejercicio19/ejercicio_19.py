import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import CTkFont
import tkinter.font as tkFont
from PIL import Image, ImageFont, ImageTk
import os, sys
import pygame

# Configuración global de estilo
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")  

# Ruta segura para recursos 
def ruta_recurso(rel_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, rel_path)

# Música
pygame.mixer.init()
pygame.mixer.music.load(ruta_recurso("recursos/Otonoke.mp3")) #pista de audio
pygame.mixer.music.play(-1)  # Reproduce en loop

# Cargar íconos
icon_lock = ctk.CTkImage(Image.open(ruta_recurso("recursos/lock.png")), size=(12, 12))
icon_unlock = ctk.CTkImage(Image.open(ruta_recurso("recursos/unlock.png")), size=(12, 12))


# Función de cifrado César
def cifrado_cesar(texto: str, desplazamiento: int) -> str:
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado

# Función principal de encriptar
def encriptar():
    texto_original = entrada.get()
    desp = entrada_desp.get()

    if not texto_original:
        messagebox.showerror("Error", "Por favor escribe un mensaje")
        return

    try:
        desplazamiento = int(desp)
    except ValueError:
        messagebox.showerror("Error", "Por favor introduce un desplazamiento entero válido (puede ser negativo)")
        return

    texto_cifrado = cifrado_cesar(texto_original, desplazamiento)

    # Ventana secundaria
    ventana.withdraw()
    sec = ctk.CTkToplevel()
    sec.title("Desencriptar Mensaje")
    sec.geometry("500x360")
    sec.configure(fg_color="black")

  
    ctk.CTkLabel(sec, text="Mensaje encriptado", text_color="white", font=titulo).pack(pady=(10, 2))
    ctk.CTkLabel(sec, text=texto_cifrado, text_color="skyblue", font=fuente_personalizada).pack(pady=(0, 10))

    resultado_lbl = ctk.CTkLabel(sec, text="", text_color="lightgreen", font=fuente_personalizada)
    resultado_lbl.pack(pady=10)

    # Función que descifra el mensaje cifrado aplicando el desplazamiento inverso
    def desencriptar():
        texto_descifrado = cifrado_cesar(texto_cifrado, -desplazamiento)
        resultado_lbl.configure(
            text=f"Desplazamiento utilizado: {desplazamiento}\nMensaje desencriptado: {texto_descifrado}"
        )
    
     # Función que cierra la ventana secundaria y reinicia los campos de entrada en la ventana principal
    def regresar():
        sec.destroy()
        ventana.deiconify()
        entrada.delete(0, tk.END)
        entrada_desp.delete(0, tk.END)

    ctk.CTkButton(sec, text="DESENCRIPTAR", image=icon_unlock, compound="right", command=desencriptar, font=(fuente_personalizada, 12), corner_radius=15).pack(pady=5)
    ctk.CTkButton(sec, text="Cerrar", command=sec.destroy, font=(fuente_personalizada, 12), corner_radius=15).pack(pady=5)
    ctk.CTkButton(sec, text="Nuevo mensaje", command=regresar, font=(fuente_personalizada, 12), corner_radius=15).pack(pady=5)


# Ventana principal
ventana = ctk.CTk()
ventana.title("Cifrado César")
ventana.geometry("450x280")
ventana.configure(fg_color="black")

# Fuente personalizada 
fuente_personalizada = CTkFont(family="Techbit DEMO", size=20)
titulo = CTkFont(family="Techbit DEMO", size=30)

ctk.CTkLabel(ventana, text="Escribe tu mensaje", text_color="white", font=titulo).pack(pady=(15, 5))
entrada = ctk.CTkEntry(ventana, width=300, text_color="white", fg_color="#222", border_color="#444", border_width=1)
entrada.pack(pady=5)

ctk.CTkLabel(ventana, text="Aplica un desplazamiento", text_color="white", font=fuente_personalizada).pack(pady=(10, 5))
entrada_desp = ctk.CTkEntry(ventana, width=100, justify="center", text_color="white", fg_color="#222", border_color="#444", border_width=1)
entrada_desp.pack(pady=5)

ctk.CTkButton(ventana, text="ENCRIPTAR", image=icon_lock, compound="right", command=encriptar, corner_radius=20, font=(fuente_personalizada, 12)).pack(pady=20)

ventana.mainloop()
