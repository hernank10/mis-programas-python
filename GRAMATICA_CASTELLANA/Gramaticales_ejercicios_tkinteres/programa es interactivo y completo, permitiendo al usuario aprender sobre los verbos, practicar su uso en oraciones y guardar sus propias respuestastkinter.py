import json
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

def guardar_ejemplo(user_text, file="ejemplos.json"):
    try:
        with open(file, "r") as f:
            ejemplos = json.load(f)
    except FileNotFoundError:
        ejemplos = []
    
    if len(ejemplos) < 100:
        ejemplos.append(user_text)
        with open(file, "w") as f:
            json.dump(ejemplos, f, indent=4)
        messagebox.showinfo("Guardado", "✅ Ejemplo guardado!")
    else:
        messagebox.showwarning("Límite alcanzado", "⚠️ Límite de 100 ejemplos alcanzado.")

def mostrar_teoria():
    teoria_text.delete("1.0", tk.END)
    teoria = """
    === TEORÍA: USO DE LOS VERBOS ===
    Los verbos 'decir', 'explicar', 'comentar', 'afirmar', 'negar' y 'prometer' pueden utilizarse en diversas estructuras:
    - Proposiciones subordinadas sustantivas (Ej: "Juan dijo que vendría").
    - Oraciones coordinadas mediante conjunciones (Ej: "Juan dijo que vendría y que traería café").
    """
    teoria_text.insert(tk.END, teoria)

def ejercicio_completacion():
    ejercicios = [
        ("María ____ que no tenía tiempo.", "dijo"),
        ("Pedro explicó que estudiaría ___ que se esforzaría más.", "y"),
        ("El maestro comentó que revisáramos la tarea ___ que la entregáramos.", "y"),
        ("Juan afirmó que vendría temprano ___ que traería café.", "y"),
        ("Mi madre prometió que cocinaría arroz ___ que prepararía sopa.", "y")
    ]
    
    puntuacion = 0
    for i, (oracion, respuesta) in enumerate(ejercicios, 1):
        user_resp = simpledialog.askstring("Ejercicio de completación", f"{i}. {oracion}").strip().lower()
        if user_resp == respuesta:
            messagebox.showinfo("Correcto", "✅ Respuesta correcta!")
            puntuacion += 10
        else:
            messagebox.showerror("Incorrecto", "❌ Respuesta incorrecta. Inténtalo de nuevo.")
    
    messagebox.showinfo("Puntuación", f"🎯 Puntuación final: {puntuacion}/50")

def ejercicio_redaccion():
    user_input = simpledialog.askstring("Ejercicio de redacción", "Escribe una oración usando uno de los verbos:")
    if user_input:
        guardar_ejemplo(user_input)

def menu():
    global root, teoria_text
    root = tk.Tk()
    root.title("Ejercicios de Verbos")
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()
    
    tk.Label(frame, text="Ejercicios de Verbos", font=("Arial", 14, "bold")).pack()
    
    teoria_text = scrolledtext.ScrolledText(frame, width=60, height=10)
    teoria_text.pack()
    
    btn_teoria = tk.Button(frame, text="Ver teoría", command=mostrar_teoria)
    btn_teoria.pack()
    
    btn_completacion = tk.Button(frame, text="Ejercicios de completación", command=ejercicio_completacion)
    btn_completacion.pack()
    
    btn_redaccion = tk.Button(frame, text="Ejercicio de redacción", command=ejercicio_redaccion)
    btn_redaccion.pack()
    
    btn_salir = tk.Button(frame, text="Salir", command=root.quit)
    btn_salir.pack()
    
    root.mainloop()

if __name__ == "__main__":
    menu()
