import time
import re
import json
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyttsx3

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Diccionario de reglas de tipos de frases y listas de frases con niveles de dificultad
reglas_frases = {
    "Frases declarativas": {
        "principiante": [
            "El perro corre.",
            "La casa es grande.",
            "Los niños juegan.",
            "El profesor explica.",
            "María lee un libro."
        ],
        "intermedio": [
            "El perro corre en el parque.",
            "La casa es grande y cómoda.",
            "Los niños juegan en el jardín.",
            "El profesor explica la lección.",
            "María lee un libro interesante."
        ],
        "avanzado": [
            "El perro corre rápidamente en el parque grande.",
            "La casa, que es grande y cómoda, está en la colina.",
            "Los niños, que son muy felices, juegan en el jardín.",
            "El profesor, con mucha paciencia, explica la lección.",
            "María lee un libro interesante sobre la historia."
        ]
    },
    "Frases interrogativas": {
        "principiante": [
            "¿El perro corre?",
            "¿La casa es grande?",
            "¿Los niños juegan?",
            "¿El profesor explica?",
            "¿María lee un libro?"
        ],
        "intermedio": [
            "¿El perro corre en el parque?",
            "¿La casa es grande y cómoda?",
            "¿Los niños juegan en el jardín?",
            "¿El profesor explica la lección?",
            "¿María lee un libro interesante?"
        ],
        "avanzado": [
            "¿El perro corre rápidamente en el parque grande?",
            "¿La casa, que es grande y cómoda, está en la colina?",
            "¿Los niños, que son muy felices, juegan en el jardín?",
            "¿El profesor, con mucha paciencia, explica la lección?",
            "¿María lee un libro interesante sobre la historia?"
        ]
    },
    "Frases exclamativas": {
        "principiante": [
            "¡El perro corre!",
            "¡La casa es grande!",
            "¡Los niños juegan!",
            "¡El profesor explica!",
            "¡María lee un libro!"
        ],
        "intermedio": [
            "¡El perro corre en el parque!",
            "¡La casa es grande y cómoda!",
            "¡Los niños juegan en el jardín!",
            "¡El profesor explica la lección!",
            "¡María lee un libro interesante!"
        ],
        "avanzado": [
            "¡El perro corre rápidamente en el parque grande!",
            "¡La casa, que es grande y cómoda, está en la colina!",
            "¡Los niños, que son muy felices, juegan en el jardín!",
            "¡El profesor, con mucha paciencia, explica la lección!",
            "¡María lee un libro interesante sobre la historia!"
        ]
    }
}

# Variables globales
puntaje_acumulativo = 0
tabla_clasificacion = []

# Cargar la tabla de clasificación desde un archivo JSON
try:
    with open("tabla_clasificacion.json", "r") as archivo:
        tabla_clasificacion = json.load(archivo)
except FileNotFoundError:
    tabla_clasificacion = []

def guardar_tabla_clasificacion():
    """Guarda la tabla de clasificación en un archivo JSON."""
    with open("tabla_clasificacion.json", "w") as archivo:
        json.dump(tabla_clasificacion, archivo)

def leer_texto(texto):
    """Lee el texto en voz alta."""
    engine.say(texto)
    engine.runAndWait()

def evaluar_estructura(oracion_correcta, oracion_usuario):
    """
    Evalúa si la estructura de la oración escrita por el usuario es correcta.
    """
    # Normaliza las oraciones para compararlas
    oracion_correcta = re.sub(r'[^\w\s]', '', oracion_correcta.lower())
    oracion_usuario = re.sub(r'[^\w\s]', '', oracion_usuario.lower())
    return oracion_correcta == oracion_usuario

def realizar_ejercicio(regla, nivel):
    global puntaje_acumulativo
    frases = reglas_frases[regla][nivel]
    inicio = time.time()
    correctas_frases = 0

    for i, frase in enumerate(frases):
        leer_texto(frase)  # Lee la frase en voz alta
        respuesta = simpledialog.askstring("Ejercicio", f"Escribe la frase {i+1}:\n{frase}")
        if respuesta is None:  # Si el usuario cancela
            return
        if evaluar_estructura(frase, respuesta):
            correctas_frases += 1

    fin = time.time()
    tiempo_transcurrido = fin - inicio
    precision_frases = (correctas_frases / len(frases)) * 100
    puntaje = precision_frases * (1 - tiempo_transcurrido / 60)  # Puntaje basado en precisión y tiempo
    puntaje_acumulativo += puntaje

    # Mostrar resultados
    messagebox.showinfo(
        "Resultados",
        f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n"
        f"Precisión en frases: {precision_frases:.2f}%\n"
        f"Puntaje obtenido: {puntaje:.2f}\n"
        f"Puntaje acumulativo: {puntaje_acumulativo:.2f}"
    )

def mostrar_tabla_clasificacion():
    """Muestra la tabla de clasificación."""
    if not tabla_clasificacion:
        messagebox.showinfo("Tabla de Clasificación", "Aún no hay registros en la tabla de clasificación.")
        return

    tabla_str = "Tabla de Clasificación:\n\n"
    for i, (nombre, puntaje) in enumerate(sorted(tabla_clasificacion, key=lambda x: x[1], reverse=True), 1):
        tabla_str += f"{i}. {nombre}: {puntaje:.2f} puntos\n"

    messagebox.showinfo("Tabla de Clasificación", tabla_str)

def guardar_puntaje():
    """Guarda el puntaje del usuario en la tabla de clasificación."""
    global puntaje_acumulativo, tabla_clasificacion
    nombre = simpledialog.askstring("Guardar Puntaje", "Ingresa tu nombre:")
    if nombre:
        tabla_clasificacion.append((nombre, puntaje_acumulativo))
        guardar_tabla_clasificacion()
        messagebox.showinfo("Guardar Puntaje", f"Puntaje de {nombre} guardado exitosamente.")
        puntaje_acumulativo = 0  # Reiniciar el puntaje acumulativo

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Práctica de Frases en Español")
    ventana.geometry("400x300")

    def seleccionar_ejercicio(regla):
        nivel = simpledialog.askstring("Nivel de Dificultad", "Selecciona un nivel (principiante, intermedio, avanzado):")
        if nivel and nivel.lower() in ["principiante", "intermedio", "avanzado"]:
            realizar_ejercicio(regla, nivel.lower())
        else:
            messagebox.showerror("Error", "Nivel no válido. Intenta de nuevo.")

    # Botones para seleccionar el tipo de frase
    tk.Label(ventana, text="Selecciona un tipo de frase:").pack(pady=10)
    for regla in reglas_frases.keys():
        tk.Button(ventana, text=regla, command=lambda r=regla: seleccionar_ejercicio(r)).pack(pady=5)

    # Botones adicionales
    tk.Button(ventana, text="Ver Tabla de Clasificación", command=mostrar_tabla_clasificacion).pack(pady=10)
    tk.Button(ventana, text="Guardar Puntaje", command=guardar_puntaje).pack(pady=5)
    tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()
