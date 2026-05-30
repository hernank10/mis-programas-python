import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import os
import random

# Inicializar el motor de voz
tts_engine = pyttsx3.init()

# Ruta de guardado
AUDIO_DIR = "audios_usuario"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Diccionario de ejemplos con AFI (representación simplificada)
ejemplos_con_voz = {
    "Fonológico y ortográfico": [
        {
            "texto": "zapato",
            "descripcion": "Fonema /s/ representado con 'z'.",
            "traduccion": "shoe",
            "afi": "saˈpato"
        },
        {
            "texto": "gente",
            "descripcion": "Fonema /x/ representado con 'g' ante 'e'.",
            "traduccion": "people",
            "afi": "ˈxente"
        }
    ]
}

# Funciones
def leer_texto(texto):
    tts_engine.say(texto)
    tts_engine.runAndWait()

def grabar_audio(nombre_archivo, duracion=5):
    fs = 44100  # Hz
    messagebox.showinfo("Grabación", f"🎙 Comienza a hablar. Grabación de {duracion} segundos...")
    grabacion = sd.rec(int(duracion * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(nombre_archivo, fs, grabacion)
    messagebox.showinfo("Grabado", f"✅ Audio guardado como {nombre_archivo}")

def reproducir_audio(nombre_archivo):
    try:
        fs, data = wav.read(nombre_archivo)
        sd.play(data, fs)
        sd.wait()
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo de audio.")

def mostrar_ejemplos():
    salida = ""
    for nivel, lista in ejemplos_con_voz.items():
        salida += f"\n=== {nivel} ===\n"
        for ej in lista:
            salida += f"{ej['texto']} | {ej['descripcion']} | EN: {ej['traduccion']} | AFI: /{ej['afi']}/\n"
    mostrar_ventana_texto("Ejemplos con Voz y AFI", salida)

def escuchar_ejemplo():
    nivel = "Fonológico y ortográfico"
    ejemplos = ejemplos_con_voz[nivel]
    ejemplo = random.choice(ejemplos)
    leer_texto(ejemplo["texto"])
    mensaje = f"Texto: {ejemplo['texto']}\nDescripción: {ejemplo['descripcion']}\nTraducción: {ejemplo['traduccion']}\nAFI: /{ejemplo['afi']}/"
    messagebox.showinfo("Ejemplo con Voz", mensaje)

def grabar_ejemplo_usuario():
    palabra = simpledialog.askstring("Grabación", "Palabra u oración que vas a decir:")
    if not palabra:
        return
    nombre_archivo = os.path.join(AUDIO_DIR, palabra.replace(" ", "_") + ".wav")
    grabar_audio(nombre_archivo)

def escuchar_ejemplo_usuario():
    palabra = simpledialog.askstring("Escuchar", "Palabra u oración grabada:")
    if not palabra:
        return
    nombre_archivo = os.path.join(AUDIO_DIR, palabra.replace(" ", "_") + ".wav")
    reproducir_audio(nombre_archivo)

def mostrar_ventana_texto(titulo, contenido):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    text = tk.Text(ventana, wrap="word", width=80, height=30)
    text.insert("1.0", contenido)
    text.config(state="disabled")
    text.pack(padx=10, pady=10)

# GUI principal
ventana = tk.Tk()
ventana.title("Aprendizaje Fonológico con Voz y AFI")

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill='both')

# Pestañas y funciones
funciones = {
    "Ver Ejemplos + AFI": mostrar_ejemplos,
    "Escuchar Ejemplo": escuchar_ejemplo,
    "Grabar mi Voz": grabar_ejemplo_usuario,
    "Escuchar mi Grabación": escuchar_ejemplo_usuario,
}

for nombre, funcion in funciones.items():
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=nombre)
    boton = tk.Button(frame, text=nombre, command=funcion, font=("Arial", 14), padx=10, pady=10)
    boton.pack(pady=30)

ventana.mainloop()
