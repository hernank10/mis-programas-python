import tkinter as tk
from tkinter import messagebox
import random

# Teoría detallada sobre la combinatoria léxica
def mostrar_teoria():
    teoria = """
    Teoría de la combinatoria léxica:

    La combinatoria léxica estudia cómo los verbos se combinan con ciertos sustantivos para formar expresiones semánticamente aceptables.
    Esta teoría se basa en las restricciones semánticas y sintácticas de cada verbo.
    
    Ejemplos de combinaciones válidas:
    - Caer: caen las bombas, caímos en la trampa.
    - Subir: sube el precio, suben las escaleras.
    - Bajar: bajaron los precios, bajamos la persiana.
    - Alzar: alzar la bandera, alzaron la voz.
    - Levantar: levantar el ánimo, levantaron el peso.
    """
    messagebox.showinfo("Teoría de la combinatoria léxica", teoria)

# Función para verificar combinaciones léxicas
def verificar_combinacion(verbo, sustantivo):
    combinaciones_validas = {
        "caer": ["bomba", "imperio", "enfermo"],
        "arriar": ["velas", "bandera"],
        "subir": ["compra", "precio", "escaleras"],
        "izar": ["bandera"],
        "bajar": ["persiana", "precio"],
        "alzar": ["mano", "bandera"],
        "levantar": ["ánimo", "peso"],
        "levar": ["ancla"]
    }
    
    return sustantivo in combinaciones_validas.get(verbo, [])

# Ejercicios de completación de oraciones
def ejercicio_completacion():
    oraciones = [
        "El imperio comenzó a _______ después de años de prosperidad.",
        "Ellos decidieron _______ la bandera en lo alto del edificio.",
        "Para bajar la temperatura, se puede _______ el aire acondicionado.",
        "Después de la tormenta, la gente comenzó a _______ las velas.",
        "Nosotros queremos _______ el ánimo de los trabajadores."
    ]
    
    respuestas_correctas = ["caer", "izar", "bajar", "arriar", "levantar"]
    
    def completar_oracion(index):
        respuesta = entry_respuesta.get().strip().lower()
        if respuesta == respuestas_correctas[index]:
            messagebox.showinfo("¡Correcto!", "¡La respuesta es correcta!")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era '{respuestas_correctas[index]}'.")
        
        # Limpiar la entrada para la siguiente pregunta
        entry_respuesta.delete(0, tk.END)
        
        # Avanzar al siguiente ejercicio
        if index < len(oraciones) - 1:
            label_oracion.config(text=oraciones[index + 1])
            button_completar.config(command=lambda: completar_oracion(index + 1))
        else:
            messagebox.showinfo("¡Has completado todos los ejercicios!", "¡Excelente trabajo!")

    # Mostrar la primera oración
    window_ejercicio = tk.Toplevel()
    window_ejercicio.title("Ejercicio de completación")
    label_oracion = tk.Label(window_ejercicio, text=oraciones[0], font=("Arial", 14))
    label_oracion.pack(pady=20)
    
    entry_respuesta = tk.Entry(window_ejercicio, font=("Arial", 14))
    entry_respuesta.pack(pady=10)
    
    button_completar = tk.Button(window_ejercicio, text="Completado", font=("Arial", 14), command=lambda: completar_oracion(0))
    button_completar.pack(pady=20)

# Ejercicios de conversión de oraciones simples a compuestas
def ejercicio_conversion():
    oraciones_simples = [
        "El perro corre.",
        "El sol brilla.",
        "Nosotros comemos pizza.",
        "Juan lee un libro."
    ]
    
    oraciones_compuestas = [
        "El perro corre y la gata duerme.",
        "El sol brilla y las aves cantan.",
        "Nosotros comemos pizza y bebemos refrescos.",
        "Juan lee un libro y su hermano estudia."
    ]
    
    def convertir_oracion(index):
        respuesta = entry_respuesta.get().strip()
        if respuesta == oraciones_compuestas[index]:
            messagebox.showinfo("¡Correcto!", "¡La respuesta es correcta!")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era '{oraciones_compuestas[index]}'.")
        
        # Limpiar la entrada para la siguiente pregunta
        entry_respuesta.delete(0, tk.END)
        
        # Avanzar al siguiente ejercicio
        if index < len(oraciones_simples) - 1:
            label_oracion.config(text=oraciones_simples[index + 1])
            button_convertir.config(command=lambda: convertir_oracion(index + 1))
        else:
            messagebox.showinfo("¡Has completado todos los ejercicios!", "¡Excelente trabajo!")

    # Mostrar la primera oración
    window_ejercicio = tk.Toplevel()
    window_ejercicio.title("Ejercicio de conversión")
    label_oracion = tk.Label(window_ejercicio, text=oraciones_simples[0], font=("Arial", 14))
    label_oracion.pack(pady=20)
    
    entry_respuesta = tk.Entry(window_ejercicio, font=("Arial", 14))
    entry_respuesta.pack(pady=10)
    
    button_convertir = tk.Button(window_ejercicio, text="Convertir", font=("Arial", 14), command=lambda: convertir_oracion(0))
    button_convertir.pack(pady=20)

# Ejercicios de redacción con almacenamiento de ejemplos
def ejercicio_redaccion():
    ejemplos_guardados = []
    
    def guardar_oracion():
        if len(ejemplos_guardados) < 100:
            oracion = entry_redaccion.get().strip()
            if oracion:
                ejemplos_guardados.append(oracion)
                messagebox.showinfo("¡Oración guardada!", "Tu oración ha sido guardada correctamente.")
                entry_redaccion.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Por favor, escribe una oración.")
        else:
            messagebox.showinfo("Límite alcanzado", "¡Has alcanzado el límite de 100 ejemplos guardados!")

    window_redaccion = tk.Toplevel()
    window_redaccion.title("Ejercicio de redacción")
    
    label_instruccion = tk.Label(window_redaccion, text="Escribe una oración con los siguientes verbos: 'caer', 'subir', 'bajar', 'levantar', 'alzar', 'izar'", font=("Arial", 14))
    label_instruccion.pack(pady=20)
    
    entry_redaccion = tk.Entry(window_redaccion, font=("Arial", 14))
    entry_redaccion.pack(pady=10)
    
    button_guardar = tk.Button(window_redaccion, text="Guardar Oración", font=("Arial", 14), command=guardar_oracion)
    button_guardar.pack(pady=20)

# Función principal para mostrar el menú
def menu():
    window = tk.Tk()
    window.title("Programa de Teoría y Ejercicios Lingüísticos")
    
    # Botones del menú
    button_teoria = tk.Button(window, text="Teoría de la combinatoria léxica", font=("Arial", 14), command=mostrar_teoria)
    button_teoria.pack(pady=20)
    
    button_completacion = tk.Button(window, text="Ejercicio de completación de oraciones", font=("Arial", 14), command=ejercicio_completacion)
    button_completacion.pack(pady=20)
    
    button_conversion = tk.Button(window, text="Ejercicio de conversión de oraciones", font=("Arial", 14), command=ejercicio_conversion)
    button_conversion.pack(pady=20)
    
    button_redaccion = tk.Button(window, text="Ejercicio de redacción (guardar hasta 100 ejemplos)", font=("Arial", 14), command=ejercicio_redaccion)
    button_redaccion.pack(pady=20)
    
    button_salir = tk.Button(window, text="Salir", font=("Arial", 14), command=window.quit)
    button_salir.pack(pady=20)
    
    window.mainloop()

if __name__ == "__main__":
    menu()
