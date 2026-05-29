import tkinter as tk
import pyttsx3
from playsound import playsound
import random
import os

# Configuración del lector de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de la voz
engine.setProperty('volume', 0.9)  # Volumen

# Carpeta para archivos de audio de fonemas
audio_folder = "./audios_fonemas"  # Cambia la ruta si necesitas una ubicación diferente.

# Diccionario con fonemas y sus descripciones
fonemas_es = {
    "/a/": "Vocal abierta, anterior, como en 'amar'.",
    "/e/": "Vocal cerrada, anterior, como en 'peso'.",
}
fonemas_en = {
    "/æ/": "Vocal abierta, como en 'cat'.",
    "/i:/": "Vocal larga, como en 'see'.",
}

# Función para leer texto en voz alta
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para reproducir audio de fonema
def play_audio(fonema):
    filepath = os.path.join(audio_folder, f"{fonema}.mp3")
    if os.path.exists(filepath):
        playsound(filepath)
    else:
        print(f"Audio para {fonema} no encontrado.")
        speak(f"Audio for {fonema} not found.")

# Función para mostrar la teoría fonética
def teoria_fonetica(fonemas, idioma):
    teoria_window = tk.Toplevel()
    teoria_window.title(f"Teoría Fonética ({idioma})")

    text_area = tk.Text(teoria_window, height=15, width=50)
    text_area.pack()

    for fonema, descripcion in fonemas.items():
        text_area.insert(tk.END, f"{fonema}: {descripcion}\n")
        speak(f"Fonema {fonema}: {descripcion}")
        play_audio(fonema)

    text_area.insert(tk.END, "\nPresiona cualquier tecla para regresar al menú principal.")
    text_area.bind("<KeyPress>", lambda event: teoria_window.destroy())  # Cierra la ventana al presionar una tecla

# Función para el cuestionario interactivo
def cuestionarios_interactivos():
    cuestionario_window = tk.Toplevel()
    cuestionario_window.title("Cuestionario Interactivo")

    pregunta_label = tk.Label(cuestionario_window, text="¿Qué fonema corresponde a la descripción?", font=("Arial", 14))
    pregunta_label.pack()

    fonema, descripcion = random.choice(list(fonemas_es.items()))
    pregunta_label.config(text=f"Descripción: {descripcion}")
    
    respuesta_entry = tk.Entry(cuestionario_window, font=("Arial", 14))
    respuesta_entry.pack()

    def verificar_respuesta():
        respuesta = respuesta_entry.get().strip()
        if respuesta == fonema:
            resultado_label.config(text="¡Correcto!", fg="green")
            speak("Correcto.")
        else:
            resultado_label.config(text=f"Incorrecto. La respuesta era {fonema}.", fg="red")
            speak(f"Incorrecto. La respuesta correcta era {fonema}.")

    resultado_label = tk.Label(cuestionario_window, font=("Arial", 14))
    resultado_label.pack()

    verificar_btn = tk.Button(cuestionario_window, text="Verificar Respuesta", font=("Arial", 14), command=verificar_respuesta)
    verificar_btn.pack()

# Función principal con el menú
def menu_principal():
    root = tk.Tk()
    root.title("Programa de Fonología y Gramática")

    # Crear botones del menú
    teoria_btn = tk.Button(root, text="Estudiar Teoría Fonética (Español)", font=("Arial", 14), command=lambda: teoria_fonetica(fonemas_es, "Español"))
    teoria_btn.pack(pady=10)

    teoria_btn_en = tk.Button(root, text="Estudiar Teoría Fonética (Inglés)", font=("Arial", 14), command=lambda: teoria_fonetica(fonemas_en, "Inglés"))
    teoria_btn_en.pack(pady=10)

    cuestionario_btn = tk.Button(root, text="Cuestionarios Interactivos", font=("Arial", 14), command=cuestionarios_interactivos)
    cuestionario_btn.pack(pady=10)

    salir_btn = tk.Button(root, text="Salir", font=("Arial", 14), command=root.quit)
    salir_btn.pack(pady=10)

    # Ejecutar la interfaz gráfica
    root.mainloop()

# Ejecutar el programa
menu_principal()
