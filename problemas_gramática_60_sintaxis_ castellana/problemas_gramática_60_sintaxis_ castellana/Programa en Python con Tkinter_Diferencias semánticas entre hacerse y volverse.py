import tkinter as tk
from tkinter import messagebox
import random

def mostrar_teoria():
    teoria = ("Los verbos 'hacerse' y 'volverse' expresan cambios, pero con diferencias: \n"
              "- 'Hacerse' indica un cambio gradual, muchas veces voluntario o por influencia externa.\n"
              "  Ejemplo: 'Se hizo médico tras años de estudio.'\n"
              "- 'Volverse' indica un cambio más radical e involuntario.\n"
              "  Ejemplo: 'Se volvió muy desconfiado después del accidente.'")
    messagebox.showinfo("Teoría sobre 'hacerse' y 'volverse'", teoria)

def verificar_respuesta(entry, respuesta_correcta):
    respuesta_usuario = entry.get().strip().lower()
    if respuesta_usuario == respuesta_correcta:
        messagebox.showinfo("Resultado", "¡Correcto!")
    else:
        messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")

def practicar_ejercicios():
    ejercicios = [
        {"pregunta": "Completa la oración: Se ____ millonario con el tiempo.", "respuesta": "hizo"},
        {"pregunta": "Completa la oración: Tras la tragedia, se ____ muy frío emocionalmente.", "respuesta": "volvió"},
        {"pregunta": "El clima en la ciudad se ____ más cálido con los años.", "respuesta": "ha hecho"},
        {"pregunta": "Desde que cambió de trabajo, se ____ una persona más feliz.", "respuesta": "ha vuelto"}
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
    root.title("Práctica sobre 'hacerse' y 'volverse'")
    
    tk.Label(root, text="Menú de Práctica", font=("Arial", 14)).pack()
    tk.Button(root, text="Leer teoría sobre 'hacerse' y 'volverse'", command=mostrar_teoria).pack()
    tk.Button(root, text="Realizar ejercicios", command=practicar_ejercicios).pack()
    tk.Button(root, text="Salir", command=root.quit).pack()
    
    root.mainloop()

if __name__ == "__main__":
    menu()
