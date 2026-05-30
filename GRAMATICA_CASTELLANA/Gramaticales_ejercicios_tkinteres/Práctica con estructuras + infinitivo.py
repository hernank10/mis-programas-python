import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Diccionario con teoría y ejemplos
estructuras = {
    "Con": "Expresa una acción acompañada de otra.\nEjemplo: Con estudiar todos los días, mejorarás tu comprensión.",
    "Después de": "Indica una acción posterior.\nEjemplo: Después de comer, salimos a caminar.",
    "Antes de": "Expresa una acción previa.\nEjemplo: Antes de dormir, lee un libro.",
    "Al": "Expresa simultaneidad o causa.\nEjemplo: Al llegar a casa, encendí la luz.",
    "Por": "Puede indicar causa o motivo.\nEjemplo: Por no estudiar, suspendió el examen."
}

ejemplos_guardados = []

def mostrar_teoria():
    estructura = simpledialog.askstring("Teoría", "Escribe una estructura (Con, Después de, Antes de, Al, Por):")
    if estructura in estructuras:
        messagebox.showinfo("Teoría", estructuras[estructura])
    else:
        messagebox.showerror("Error", "Estructura no reconocida.")

def completar_oracion():
    estructura = random.choice(list(estructuras.keys()))
    ejemplo = estructuras[estructura].split("\nEjemplo: ")[1]
    oracion_incompleta = ejemplo.split(",")[0] + ", ..."
    respuesta = simpledialog.askstring("Completar oración", f"Completa la oración:\n{oracion_incompleta}")
    
    if respuesta and respuesta in ejemplo:
        messagebox.showinfo("Correcto", "¡Bien hecho!")
    else:
        messagebox.showerror("Incorrecto", f"La respuesta correcta era:\n{ejemplo}")

def crear_oracion():
    estructura = simpledialog.askstring("Crear oración", "Escribe una estructura (Con, Después de, Antes de, Al, Por):")
    if estructura not in estructuras:
        messagebox.showerror("Error", "Estructura no reconocida.")
        return
    
    verbo = simpledialog.askstring("Crear oración", "Escribe un verbo en infinitivo:")
    complemento = simpledialog.askstring("Crear oración", "Escribe un complemento para la oración:")
    
    if verbo and complemento:
        oracion = f"{estructura} {verbo} {complemento}."
        ejemplos_guardados.append(oracion)
        messagebox.showinfo("Oración creada", oracion)
        
        # Repetir la oración
        respuesta = simpledialog.askstring("Repite la oración", f"Escríbela nuevamente:\n{oracion}")
        if respuesta == oracion:
            messagebox.showinfo("Correcto", "¡Bien hecho!")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era:\n{oracion}")

def iniciar_interfaz():
    root = tk.Tk()
    root.title("Práctica con estructuras + infinitivo")
    root.geometry("400x350")
    
    tk.Label(root, text="Práctica con estructuras + infinitivo", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Leer teoría", command=mostrar_teoria).pack(pady=5)
    tk.Button(root, text="Practicar completación de oraciones", command=completar_oracion).pack(pady=5)
    tk.Button(root, text="Crear nuevas oraciones", command=crear_oracion).pack(pady=5)
    tk.Button(root, text="Salir", command=root.quit).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()
