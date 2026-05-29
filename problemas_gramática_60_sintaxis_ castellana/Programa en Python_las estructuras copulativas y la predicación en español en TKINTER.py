import tkinter as tk
from tkinter import messagebox
import random

def mostrar_teoria():
    teoria = ("Las oraciones copulativas agentivas permiten la combinación con adverbios de habitualidad, "  
              "el progresivo y los adverbiales agentivos cuando el adjetivo denota un comportamiento voluntario.\n\n"
              "Ejemplo:\n"
              " - *Juan es alto habitualmente* (incorrecto)\n"
              " - *Juan es atento habitualmente* (correcto)\n")
    messagebox.showinfo("Teoría sobre estructuras copulativas", teoria)

def verificar_respuesta(entry, respuesta_correcta):
    respuesta_usuario = entry.get().strip().lower()
    if respuesta_usuario == respuesta_correcta:
        messagebox.showinfo("Resultado", "¡Correcto!")
    else:
        messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")

def practicar_ejercicios():
    ejercicios = [
        {"pregunta": "¿Cuál de estas oraciones es correcta?\n\nA) Juan es amable habitualmente.\nB) Juan es alto habitualmente.", "respuesta": "a"},
        {"pregunta": "¿Cuál es la forma correcta?\n\nA) Juan está siendo cruel.\nB) Juan está siendo alto.", "respuesta": "a"},
        {"pregunta": "Completa: ____ amable con los demás a propósito.", "respuesta": "es"},
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
    root.title("Práctica de Estructuras Copulativas")
    
    tk.Label(root, text="Menú de Práctica", font=("Arial", 14)).pack()
    tk.Button(root, text="Leer teoría sobre estructuras copulativas", command=mostrar_teoria).pack()
    tk.Button(root, text="Realizar ejercicios", command=practicar_ejercicios).pack()
    tk.Button(root, text="Salir", command=root.quit).pack()
    
    root.mainloop()

if __name__ == "__main__":
    menu()
