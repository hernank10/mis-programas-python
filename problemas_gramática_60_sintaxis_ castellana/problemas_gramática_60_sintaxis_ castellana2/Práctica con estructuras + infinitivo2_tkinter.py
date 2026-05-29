import random
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

FILENAME = "ejemplos_guardados.txt"

def cargar_ejemplos():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r", encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except OSError:
            messagebox.showerror("Error", "No se pudo leer el archivo de ejemplos.")
            return []
    return []

def guardar_ejemplos(nuevos_ejemplos):
    try:
        with open(FILENAME, "a", encoding="utf-8") as file:
            for ejemplo in nuevos_ejemplos:
                file.write(ejemplo + "\n")
    except OSError:
        messagebox.showerror("Error", "No se pudo guardar los ejemplos.")

ejemplos = cargar_ejemplos()

def teoria():
    estructuras = [
        ("Con", "Expresa una acción acompañada de otra. Ej: Con estudiar todos los días, mejorarás tu comprensión."),
        ("Después de", "Indica una acción posterior. Ej: Después de comer, salimos a caminar."),
        ("Antes de", "Expresa una acción previa. Ej: Antes de dormir, lee un libro."),
        ("Al", "Expresa simultaneidad o causa. Ej: Al llegar a casa, encendí la luz."),
        ("Por", "Puede indicar causa o motivo. Ej: Por no estudiar, suspendió el examen.")
    ]
    teoria_texto = "Teoría sobre estructuras + infinitivo:\n\n" + "\n".join([f"- '{estructura}' + infinitivo: {explicacion}" for estructura, explicacion in estructuras])
    messagebox.showinfo("Teoría", teoria_texto)

def ver_oraciones():
    if not ejemplos:
        messagebox.showinfo("Oraciones", "No hay ejemplos guardados.")
    else:
        messagebox.showinfo("Oraciones guardadas", "\n".join(ejemplos))

def practicar_memoria():
    if not ejemplos:
        messagebox.showinfo("Practicar Memoria", "No hay ejemplos guardados para practicar.")
        return
    
    oracion = random.choice(ejemplos)
    respuesta = simpledialog.askstring("Práctica de Memoria", f"Escribe nuevamente esta oración de memoria:\n{oracion}")
    
    if respuesta and respuesta.strip() == oracion:
        messagebox.showinfo("Resultado", "¡Correcto!")
    else:
        messagebox.showerror("Resultado", f"Incorrecto. La respuesta correcta era:\n{oracion}")

def crear_oracion():
    oraciones_creadas = []
    while len(ejemplos) + len(oraciones_creadas) < 100:
        verbo = simpledialog.askstring("Nueva Oración", "Escribe un verbo en infinitivo (o 'fin' para terminar):")
        if not verbo or verbo.lower() == 'fin':
            break
        
        complemento = simpledialog.askstring("Nueva Oración", "Escribe un complemento para la oración:")
        if not complemento:
            continue
        
        simple = f"Con {verbo} {complemento}."
        compuesta = f"Con {verbo} {complemento}, lograrás el objetivo."
        
        oraciones_creadas.extend([simple, compuesta])
    
    if oraciones_creadas:
        guardar_ejemplos(oraciones_creadas)
        ejemplos.extend(oraciones_creadas)
        
        for oracion in oraciones_creadas:
            respuesta = simpledialog.askstring("Repetición", f"Escríbela nuevamente: {oracion}")
            if respuesta and respuesta.strip() == oracion:
                messagebox.showinfo("Verificación", "¡Correcto!")
            else:
                messagebox.showerror("Verificación", f"Incorrecto. La respuesta correcta era: {oracion}")
    else:
        messagebox.showinfo("Creación", "No se crearon nuevas oraciones.")

def iniciar_interfaz():
    root = tk.Tk()
    root.title("Práctica de estructuras + infinitivo")
    root.geometry("400x300")
    
    tk.Label(root, text="Práctica de estructuras + infinitivo", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Leer teoría", command=teoria).pack(fill="x", padx=20, pady=5)
    tk.Button(root, text="Ver oraciones guardadas", command=ver_oraciones).pack(fill="x", padx=20, pady=5)
    tk.Button(root, text="Practicar escritura de memoria", command=practicar_memoria).pack(fill="x", padx=20, pady=5)
    tk.Button(root, text="Crear nuevas oraciones", command=crear_oracion).pack(fill="x", padx=20, pady=5)
    tk.Button(root, text="Salir", command=root.quit).pack(fill="x", padx=20, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()
