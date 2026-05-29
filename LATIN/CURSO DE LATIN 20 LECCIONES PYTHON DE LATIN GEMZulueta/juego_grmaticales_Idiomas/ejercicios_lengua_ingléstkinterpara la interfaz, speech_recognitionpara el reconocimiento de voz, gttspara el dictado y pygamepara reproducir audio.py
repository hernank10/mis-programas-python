import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import speech_recognition as sr
from gtts import gTTS
import os
import pygame

# Datos de ejemplo
easociacion = {"sun": "sun.png", "house": "house.png", "dog": "dog.png"}
ord_palabras = ["The dog plays in the park", "My house is big and beautiful"]
relleno = ["The ___ shines in the sky", "My ___ is tall and strong"]

def ejercicio_asociacion():
    palabra = random.choice(list(easociacion.keys()))
    respuesta = simpledialog.askstring("Association Exercise", f"What word corresponds to the displayed image? ({easociacion[palabra]})")
    if respuesta.lower() == palabra:
        messagebox.showinfo("Correct", "Well done!")
    else:
        messagebox.showerror("Incorrect", f"The correct answer was {palabra}")

def dictado():
    oracion = "Today is a beautiful day to learn"
    tts = gTTS(text=oracion, lang='en')
    tts.save("dictation.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("dictation.mp3")
    pygame.mixer.music.play()
    respuesta = simpledialog.askstring("Dictation", "Type the sentence you heard:")
    if respuesta.lower() == oracion.lower():
        messagebox.showinfo("Correct", "Great spelling!")
    else:
        messagebox.showerror("Incorrect", f"The correct answer was: {oracion}")

def ordenar_palabras():
    oracion = random.choice(ord_palabras)
    palabras = oracion.split()
    random.shuffle(palabras)
    respuesta = simpledialog.askstring("Order Words", f"Arrange these words: {' '.join(palabras)}")
    if respuesta.lower() == oracion.lower():
        messagebox.showinfo("Correct", "Well done!")
    else:
        messagebox.showerror("Incorrect", f"The correct answer was: {oracion}")

def rellenar_espacios():
    oracion = random.choice(relleno)
    respuesta = simpledialog.askstring("Fill in the Blanks", f"{oracion}")
    if "sun" in oracion and respuesta.lower() == "sun":
        messagebox.showinfo("Correct", "Well done!")
    elif "house" in oracion and respuesta.lower() == "house":
        messagebox.showinfo("Correct", "Well done!")
    else:
        messagebox.showerror("Incorrect", "Try again")

def lectura_en_voz_alta():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Reading Aloud", "Read aloud: 'Hello, I am learning to read' and press OK")
        try:
            audio = recognizer.listen(source)
            texto = recognizer.recognize_google(audio, language='en-US')
            if "hello i am learning to read" in texto.lower():
                messagebox.showinfo("Correct", "Good pronunciation!")
            else:
                messagebox.showerror("Incorrect", "Try again")
        except:
            messagebox.showerror("Error", "Could not recognize your voice")

# Interfaz Gráfica
tk_root = tk.Tk()
tk_root.title("Learn to Read and Write")
tk.Button(tk_root, text="Association Exercise", command=ejercicio_asociacion).pack(pady=5)
tk.Button(tk_root, text="Interactive Dictation", command=dictado).pack(pady=5)
tk.Button(tk_root, text="Order Words", command=ordenar_palabras).pack(pady=5)
tk.Button(tk_root, text="Fill in the Blanks", command=rellenar_espacios).pack(pady=5)
tk.Button(tk_root, text="Reading Aloud", command=lectura_en_voz_alta).pack(pady=5)
tk_root.mainloop()
