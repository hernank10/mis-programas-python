import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import speech_recognition as sr
from gtts import gTTS
import os
import pygame

# Datos de ejemplo
easociacion = {"sol": "sol.png", "casa": "casa.png", "perro": "perro.png"}
ord_palabras = ["El perro juega en el parque", "Mi casa es grande y bonita"]
relleno = ["El ___ brilla en el cielo", "Mi ___ es alta y fuerte"]

def ejercicio_asociacion():
    palabra = random.choice(list(easociacion.keys()))
    respuesta = simpledialog.askstring("Ejercicio de Asociación", f"¿Qué palabra corresponde a la imagen mostrada? ({easociacion[palabra]})")
    if respuesta.lower() == palabra:
        messagebox.showinfo("Correcto", "¡Bien hecho!")
    else:
        messagebox.showerror("Incorrecto", f"La respuesta correcta era {palabra}")

def dictado():
    oracion = "Hoy es un hermoso día para aprender"
    tts = gTTS(text=oracion, lang='es')
    tts.save("dictado.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("dictado.mp3")
    pygame.mixer.music.play()
    respuesta = simpledialog.askstring("Dictado", "Escribe la oración que escuchaste:")
    if respuesta.lower() == oracion.lower():
        messagebox.showinfo("Correcto", "¡Buena ortografía!")
    else:
        messagebox.showerror("Incorrecto", f"La respuesta correcta era: {oracion}")

def ordenar_palabras():
    oracion = random.choice(ord_palabras)
    palabras = oracion.split()
    random.shuffle(palabras)
    respuesta = simpledialog.askstring("Ordenar palabras", f"Ordena estas palabras: {' '.join(palabras)}")
    if respuesta.lower() == oracion.lower():
        messagebox.showinfo("Correcto", "¡Bien hecho!")
    else:
        messagebox.showerror("Incorrecto", f"La respuesta correcta era: {oracion}")

def rellenar_espacios():
    oracion = random.choice(relleno)
    respuesta = simpledialog.askstring("Rellenar espacios", f"{oracion}")
    if "sol" in oracion and respuesta.lower() == "sol":
        messagebox.showinfo("Correcto", "¡Bien hecho!")
    elif "casa" in oracion and respuesta.lower() == "casa":
        messagebox.showinfo("Correcto", "¡Bien hecho!")
    else:
        messagebox.showerror("Incorrecto", "Inténtalo de nuevo")

def lectura_en_voz_alta():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Lectura en voz alta", "Lee en voz alta: 'Hola, estoy aprendiendo a leer' y presiona Aceptar")
        try:
            audio = recognizer.listen(source)
            texto = recognizer.recognize_google(audio, language='es-ES')
            if "hola estoy aprendiendo a leer" in texto.lower():
                messagebox.showinfo("Correcto", "¡Buena pronunciación!")
            else:
                messagebox.showerror("Incorrecto", "Inténtalo nuevamente")
        except:
            messagebox.showerror("Error", "No se pudo reconocer tu voz")

# Interfaz Gráfica
tk_root = tk.Tk()
tk_root.title("Aprender a Leer y Escribir")
tk.Button(tk_root, text="Ejercicio de Asociación", command=ejercicio_asociacion).pack(pady=5)
tk.Button(tk_root, text="Dictado Interactivo", command=dictado).pack(pady=5)
tk.Button(tk_root, text="Ordenar Palabras", command=ordenar_palabras).pack(pady=5)
tk.Button(tk_root, text="Rellenar Espacios", command=rellenar_espacios).pack(pady=5)
tk.Button(tk_root, text="Lectura en Voz Alta", command=lectura_en_voz_alta).pack(pady=5)
tk_root.mainloop()
