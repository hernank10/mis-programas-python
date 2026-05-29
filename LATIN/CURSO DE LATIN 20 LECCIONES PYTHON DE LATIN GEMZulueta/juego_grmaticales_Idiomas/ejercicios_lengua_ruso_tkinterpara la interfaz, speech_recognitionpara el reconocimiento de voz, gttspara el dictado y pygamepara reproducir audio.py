import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import speech_recognition as sr
from gtts import gTTS
import os
import pygame

# Datos de ejemplo
easociacion = {"\u0441\u043e\u043b\u043d\u0446\u0435": "sun.png", "\u0434\u043e\u043c": "house.png", "\u0441\u043e\u0431\u0430\u043a\u0430": "dog.png"}
ord_palabras = ["\u0421\u043e\u0431\u0430\u043a\u0430 \u0438\u0433\u0440\u0430\u0435\u0442 \u0432 \u043f\u0430\u0440\u043a\u0435", "\u041c\u043e\u0439 \u0434\u043e\u043c \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u0438 \u043a\u0440\u0430\u0441\u0438\u0432\u044b\u0439"]
relleno = ["\u0412 \u043d\u0435\u0431\u0435 \u0441\u0432\u0435\u0442\u0438\u0442 ___", "\u041c\u043e\u0439 ___ \u0432\u044b\u0441\u043e\u043a\u0438\u0439 \u0438 \u043a\u0440\u0435\u043f\u043a\u0438\u0439"]

def ejercicio_asociacion():
    palabra = random.choice(list(easociacion.keys()))
    respuesta = simpledialog.askstring("\u0423\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u0435 \u043f\u043e \u0430\u0441\u0441\u043e\u0446\u0438\u0430\u0446\u0438\u044f\u043c", f"\u041a\u0430\u043a\u043e\u0435 \u0441\u043b\u043e\u0432\u043e \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044e? ({easociacion[palabra]})")
    if respuesta.lower() == palabra:
        messagebox.showinfo("\u0412\u0435\u0440\u043d\u043e", "\u041c\u043e\u043b\u043e\u0434\u0435\u0446!")
    else:
        messagebox.showerror("\u041d\u0435\u0432\u0435\u0440\u043d\u043e", f"\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442: {palabra}")

def dictado():
    oracion = "\u0421\u0435\u0433\u043e\u0434\u043d\u044f \u043f\u0440\u0435\u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0434\u0435\u043d\u044c \u0434\u043b\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f"
    tts = gTTS(text=oracion, lang='ru')
    tts.save("dictation.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("dictation.mp3")
    pygame.mixer.music.play()
    respuesta = simpledialog.askstring("\u0414\u0438\u043a\u0442\u0430\u043d\u0442", "\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435:")
    if respuesta.lower() == oracion.lower():
        messagebox.showinfo("\u0412\u0435\u0440\u043d\u043e", "\u041e\u0442\u043b\u0438\u0447\u043d\u043e!")
    else:
        messagebox.showerror("\u041d\u0435\u0432\u0435\u0440\u043d\u043e", f"\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442: {oracion}")

def lectura_en_voz_alta():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("\u0427\u0442\u0435\u043d\u0438\u0435 \u0432\u0441\u043b\u0443\u0445", "\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0439\u0442\u0435 \u0432\u0441\u043b\u0443\u0445: 'Здравствуйте, я учусь читать' и нажмите OK")
        try:
            audio = recognizer.listen(source)
            texto = recognizer.recognize_google(audio, language='ru-RU')
            if "здравствуйте я учусь читать" in texto.lower():
                messagebox.showinfo("\u0412\u0435\u0440\u043d\u043e", "\u0425\u043e\u0440\u043e\u0448\u0430\u044f \u043f\u0440\u043e\u043d\u043e\u0448\u0435\u043d\u0438\u0435!")
            else:
                messagebox.showerror("\u041d\u0435\u0432\u0435\u0440\u043d\u043e", "\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0435\u0449\u0435 \u0440\u0430\u0437")
        except:
            messagebox.showerror("\u041e\u0448\u0438\u0431\u043a\u0430", "\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0442\u044c \u0432\u0430\u0448 \u0433\u043e\u043b\u043e\u0441")
