import tkinter as tk
from tkinter import messagebox
import random

def mostrar_teoria():
    teoria = ("Los demostrativos en español pueden aparecer en posición prenominal (antes del sustantivo) "
              "y en posición posnominal (después del sustantivo), sin cambiar su significado.\n"
              "Ejemplo:\n - Este libro (prenominal)\n - El libro este (posnominal)\n\n"
              "En posición posnominal, el demostrativo requiere un determinante, por ejemplo: 'el libro este'.")
    messagebox.showinfo("Teoría sobre demostrativos", teoria)

def verificar_respuesta(entry, respuesta_correcta):
    respuesta_usuario = entry.get().strip().lower()
    if respuesta_usuario == respuesta_correcta:
        messagebox.showinfo("Resultado", "¡Correcto!")
    else:
        messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")

def practicar_ejercicios():
    ejercicios = [
        {"pregunta": "Completa la frase: 'Me gusta ____ coche rojo'", "respuesta": "este"},
        {"pregunta": "Completa la frase: 'No entiendo por qué compraste ____ zapatos'", "respuesta": "esos"},
        {"pregunta": "Transforma en posnominal: 'Esa casa'", "respuesta": "la casa esa"},
        {"pregunta": "Transforma en prenominal: 'El perro aquel'", "respuesta": "aquel perro"}
    ]
    random.shuffle(ejercicios)
    ejercicio_actual = ejercicios[0]
    
    ejercicio_window = tk.Toplevel()
    ejercicio_window.title("Ejercicio")
    tk.Label(ejercicio_window, text=ejercicio_actual['pregunta']).pack()
    entry = tk.Entry(ejercicio_window)
    entry.pack()
    tk.Button(ejercicio_window, text="Verificar", command=lambda: verificar_respuesta(entry, ejercicio_actual['respuesta'])).pack()

def menu():
    root = tk.Tk()
    root.title("Práctica de Demostrativos")
    
    tk.Label(root, text="Menú de Práctica", font=("Arial", 14)).pack()
    tk.Button(root, text="Leer teoría sobre demostrativos", command=mostrar_teoria).pack()
    tk.Button(root, text="Realizar ejercicios", command=practicar_ejercicios).pack()
    tk.Button(root, text="Salir", command=root.quit).pack()
    
    root.mainloop()

if __name__ == "__main__":
    menu()
