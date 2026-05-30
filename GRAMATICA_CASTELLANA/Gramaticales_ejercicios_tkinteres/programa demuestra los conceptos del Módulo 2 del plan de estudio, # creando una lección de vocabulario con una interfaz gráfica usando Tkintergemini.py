# Este programa demuestra los conceptos del Módulo 2 del plan de estudio,
# creando una lección de vocabulario con una interfaz gráfica usando Tkinter.

import tkinter as tk
from tkinter import messagebox

# --- Contenido de la lección ---
# Diccionario para almacenar las palabras, igual que en el módulo 1.
vocabulario_animales = {
    "perro": "dog",
    "gato": "cat",
    "pato": "duck"
}

# --- Variables de estado de la aplicación ---
lista_palabras = list(vocabulario_animales.keys())
palabra_actual = ""
puntaje = 0
indice_pregunta = 0

# --- Funciones de la lección ---
def iniciar_leccion():
    """Reinicia la lección y muestra la primera palabra."""
    global indice_pregunta, puntaje
    indice_pregunta = 0
    puntaje = 0
    siguiente_pregunta()

def siguiente_pregunta():
    """Muestra la siguiente palabra y actualiza la interfaz."""
    global palabra_actual, indice_pregunta

    # Si ya respondimos todas las preguntas, mostramos el resultado final.
    if indice_pregunta >= len(lista_palabras):
        mostrar_resultados()
        return

    palabra_actual = lista_palabras[indice_pregunta]
    label_pregunta.config(text=f"¿Cómo se dice '{palabra_actual}' en inglés?")
    entry_respuesta.delete(0, tk.END)  # Limpiamos el campo de texto
    
    indice_pregunta += 1

def verificar_respuesta():
    """Verifica la respuesta del usuario y da feedback."""
    global puntaje
    respuesta_usuario = entry_respuesta.get().strip().lower()
    respuesta_correcta = vocabulario_animales[palabra_actual]

    if respuesta_usuario == respuesta_correcta:
        puntaje += 1
        messagebox.showinfo("¡Correcto!", "¡Respuesta correcta! ✅")
    else:
        messagebox.showerror("Incorrecto", f"Respuesta incorrecta. La respuesta es '{respuesta_correcta}'. ❌")

    # Pasar a la siguiente pregunta después de la verificación.
    siguiente_pregunta()

def mostrar_resultados():
    """Muestra los resultados finales de la lección."""
    mensaje = f"¡Lección terminada!\nTu puntaje final es: {puntaje} de {len(lista_palabras)}."
    messagebox.showinfo("Resultados", mensaje)

# --- Configuración de la ventana principal ---
ventana = tk.Tk()
ventana.title("Lección de Vocabulario con Tkinter")
ventana.geometry("400x250")
ventana.configure(bg="#F0F0F0")

# --- Creación de los widgets ---
# Título
titulo = tk.Label(ventana, text="Lección de Vocabulario", font=("Helvetica", 24, "bold"), bg="#F0F0F0")
titulo.pack(pady=10)

# Etiqueta para la pregunta
label_pregunta = tk.Label(ventana, text="", font=("Helvetica", 16), bg="#F0F0F0")
label_pregunta.pack(pady=10)

# Campo de entrada de texto
entry_respuesta = tk.Entry(ventana, font=("Helvetica", 14), width=30)
entry_respuesta.pack(pady=5)

# Botón para verificar la respuesta
boton_verificar = tk.Button(ventana, text="Verificar", font=("Helvetica", 14), command=verificar_respuesta)
boton_verificar.pack(pady=10)

# Botón para empezar la lección
boton_iniciar = tk.Button(ventana, text="Empezar Lección", font=("Helvetica", 14), command=iniciar_leccion)
boton_iniciar.pack(pady=10)

# Iniciar la lección automáticamente
iniciar_leccion()

# Bucle principal de la aplicación
ventana.mainloop()
