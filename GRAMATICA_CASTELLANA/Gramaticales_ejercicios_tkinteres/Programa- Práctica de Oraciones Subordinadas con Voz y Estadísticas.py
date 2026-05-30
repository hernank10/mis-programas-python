import tkinter as tk
from tkinter import messagebox, simpledialog
import pyttsx3
import speech_recognition as sr
import random

# Configuración de pyttsx3 para síntesis de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de la voz

# Configuración de speech_recognition para reconocimiento de voz
recognizer = sr.Recognizer()

# Oraciones subordinadas en español e inglés
oraciones_subordinadas = [
    {"idioma": "español", "tipo": "causal", "oracion": "Como estaba lloviendo, nos quedamos en casa.", "subordinada": "Como estaba lloviendo"},
    {"idioma": "español", "tipo": "temporal", "oracion": "Cuando llegues, avísame.", "subordinada": "Cuando llegues"},
    {"idioma": "español", "tipo": "condicional", "oracion": "Si estudias, aprobarás el examen.", "subordinada": "Si estudias"},
    {"idioma": "inglés", "tipo": "causal", "oracion": "Because it was raining, we stayed home.", "subordinada": "Because it was raining"},
    {"idioma": "inglés", "tipo": "temporal", "oracion": "When you arrive, let me know.", "subordinada": "When you arrive"},
    {"idioma": "inglés", "tipo": "condicional", "oracion": "If you study, you will pass the exam.", "subordinada": "If you study"}
]

# Estadísticas del usuario
estadisticas = {"correctas": 0, "incorrectas": 0}

# Función para reproducir voz
def reproducir_voz(texto, idioma='es'):
    engine.setProperty('voice', 'spanish' if idioma == 'español' else 'english')
    engine.say(texto)
    engine.runAndWait()

# Función para reconocer voz
def reconocer_voz():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES" if estadisticas["idioma"] == "español" else "en-US")
            print(f"Has dicho: {texto}")
            return texto
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
            return None
        except sr.RequestError:
            print("Error al conectar con el servicio de reconocimiento de voz.")
            return None

# Función para practicar oraciones subordinadas
def practicar_subordinadas():
    oracion = random.choice([o for o in oraciones_subordinadas if o["idioma"] == estadisticas["idioma"]])
    reproducir_voz(f"Escucha la oración: {oracion['oracion']}", oracion["idioma"])
    respuesta = simpledialog.askstring("Práctica", f"Escribe la oración subordinada en la siguiente oración:\n{oracion['oracion']}")

    if respuesta == oracion["subordinada"]:
        messagebox.showinfo("Resultado", "¡Correcto! Has identificado la oración subordinada.")
        estadisticas["correctas"] += 1
    else:
        messagebox.showinfo("Resultado", f"Incorrecto. La oración subordinada es: {oracion['subordinada']}")
        estadisticas["incorrectas"] += 1

# Función para mostrar estadísticas
def mostrar_estadisticas():
    messagebox.showinfo("Estadísticas", f"Respuestas correctas: {estadisticas['correctas']}\nRespuestas incorrectas: {estadisticas['incorrectas']}")

# Función para cambiar el idioma
def cambiar_idioma():
    estadisticas["idioma"] = "inglés" if estadisticas["idioma"] == "español" else "español"
    messagebox.showinfo("Idioma Cambiado", f"Ahora practicarás en {estadisticas['idioma']}.")

# Interfaz gráfica con Tkinter
def crear_interfaz_grafica():
    ventana = tk.Tk()
    ventana.title("Práctica de Oraciones Subordinadas")

    # Botones de la interfaz
    btn_practicar = tk.Button(ventana, text="Practicar", command=practicar_subordinadas)
    btn_practicar.pack(pady=10)

    btn_estadisticas = tk.Button(ventana, text="Ver Estadísticas", command=mostrar_estadisticas)
    btn_estadisticas.pack(pady=10)

    btn_cambiar_idioma = tk.Button(ventana, text="Cambiar Idioma", command=cambiar_idioma)
    btn_cambiar_idioma.pack(pady=10)

    btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
    btn_salir.pack(pady=10)

    ventana.mainloop()

# Función principal
def main():
    estadisticas["idioma"] = "español"  # Idioma predeterminado
    crear_interfaz_grafica()

if __name__ == "__main__":
    main()
