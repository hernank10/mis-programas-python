import tkinter as tk
from tkinter import messagebox
import random

def mostrar_teoria():
    teoria = ("Las nominalizaciones con 'lo' permiten convertir adjetivos en sustantivos abstractos. \n"
              "Ejemplo: \n - Lo bueno de Juan (expresión neutra sobre una cualidad)\n"
              " - La bondad de Juan (sustantivo abstracto que denota la cualidad como entidad)")
    messagebox.showinfo("Teoría sobre nominalizaciones", teoria)

def verificar_respuesta(entry, respuesta_correcta):
    respuesta_usuario = entry.get().strip().lower()
    if respuesta_usuario == respuesta_correcta:
        messagebox.showinfo("Resultado", "¡Correcto!")
    else:
        messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")

def practicar_ejercicios():
    ejercicios = [
        {"pregunta": "Transforma en nominalización con 'lo': 'La generosidad de María'", "respuesta": "lo generoso de maria"},
        {"pregunta": "Transforma en nominalización con sustantivo: 'Lo bello del paisaje'", "respuesta": "la belleza del paisaje"},
        {"pregunta": "Completa: ____ honesto de Luis es admirable.", "respuesta": "lo"},
        {"pregunta": "¿Qué forma es correcta? 'Lo inteligente de Pedro' o 'La inteligencia de Pedro'?", "respuesta": "la inteligencia de pedro"}
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
    root.title("Práctica de Nominalizaciones")
    
    tk.Label(root, text="Menú de Práctica", font=("Arial", 14)).pack()
    tk.Button(root, text="Leer teoría sobre nominalizaciones", command=mostrar_teoria).pack()
    tk.Button(root, text="Realizar ejercicios", command=practicar_ejercicios).pack()
    tk.Button(root, text="Salir", command=root.quit).pack()
    
    root.mainloop()

if __name__ == "__main__":
    menu()
