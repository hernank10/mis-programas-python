import json
import tkinter as tk
from tkinter import messagebox, simpledialog

DATA_FILE = "oraciones_apex_dd.json"

TEORIA = """
Las aposiciones explicativas se emplean para añadir información adicional sobre un sustantivo ya mencionado. 
Ejemplo: Gabriel García Márquez, el autor colombiano, escribió Cien años de soledad.

Las dislocaciones a la derecha (DD) consisten en la presencia de un pronombre en la oración principal 
y un sintagma nominal independiente al final, el cual reitera la referencia.
Ejemplo: Me pareció verlo ayer, a tu hermano.

Ejemplo combinado de Apex y DD:
En la reunión estaba él, el director de la empresa, con su asistente.
"""

def cargar_oraciones():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_oraciones(oraciones):
    with open(DATA_FILE, "w") as file:
        json.dump(oraciones, file, indent=4)

def mostrar_teoria():
    messagebox.showinfo("Teoría sobre Apex y DD", TEORIA)

def completar_apex():
    respuesta = simpledialog.askstring("Aposición Explicativa", "Completa: Gabriel García Márquez, ____________, escribió Cien años de soledad.")
    if respuesta:
        messagebox.showinfo("Resultado", f"Gabriel García Márquez, {respuesta}, escribió Cien años de soledad.")

def completar_dd():
    respuesta = simpledialog.askstring("Dislocación a la Derecha", "Completa: La vi en el concierto, ____________.")
    if respuesta:
        messagebox.showinfo("Resultado", f"La vi en el concierto, {respuesta}.")

def combinar_apex_dd():
    respuesta1 = simpledialog.askstring("Aposición Explicativa", "Completa la primera aposición explicativa:")
    respuesta2 = simpledialog.askstring("Dislocación a la Derecha", "Completa la dislocación a la derecha:")
    if respuesta1 and respuesta2:
        messagebox.showinfo("Resultado", f"En la reunión estaba él, {respuesta1}, {respuesta2}.")

def reescribir_dd():
    respuesta = simpledialog.askstring("Reescribir con DD", "Reescribe: El chef preparó el plato más exquisito.")
    if respuesta:
        messagebox.showinfo("Resultado", f"{respuesta}, el chef preparó el plato más exquisito.")

def crear_apex():
    respuesta = simpledialog.askstring("Aposición Explicativa", "Completa: El Taj Mahal, ____________, es una maravilla arquitectónica.")
    if respuesta:
        messagebox.showinfo("Resultado", f"El Taj Mahal, {respuesta}, es una maravilla arquitectónica.")

def escribir_nuevas_oraciones():
    oraciones = cargar_oraciones()
    if len(oraciones) >= 100:
        messagebox.showwarning("Límite alcanzado", "Se ha alcanzado el límite de 100 oraciones.")
        return
    
    nueva_oracion = simpledialog.askstring("Nueva Oración", "Escribe una nueva oración con Apex o DD:")
    if nueva_oracion:
        oraciones.append(nueva_oracion)
        guardar_oraciones(oraciones)
        messagebox.showinfo("Guardado", "Oración guardada exitosamente.")

def practicar_oraciones():
    oraciones = cargar_oraciones()
    if not oraciones:
        messagebox.showwarning("Sin oraciones", "No hay oraciones guardadas para practicar. Agrega algunas primero.")
        return
    
    for oracion in oraciones:
        respuesta = simpledialog.askstring("Práctica", f"Reescribe: {oracion}")
    messagebox.showinfo("Práctica", "Práctica completada.")

def crear_interfaz():
    root = tk.Tk()
    root.title("Práctica de Apex y DD")
    root.geometry("450x550")
    
    tk.Label(root, text="Menú de Práctica", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(root, text="1. Ver Teoría", command=mostrar_teoria, width=40).pack(pady=5)
    tk.Button(root, text="2. Completar Aposición Explicativa", command=completar_apex, width=40).pack(pady=5)
    tk.Button(root, text="3. Completar Dislocación a la Derecha", command=completar_dd, width=40).pack(pady=5)
    tk.Button(root, text="4. Combinar Apex y DD", command=combinar_apex_dd, width=40).pack(pady=5)
    tk.Button(root, text="5. Reescribir con DD", command=reescribir_dd, width=40).pack(pady=5)
    tk.Button(root, text="6. Crear Aposición Explicativa", command=crear_apex, width=40).pack(pady=5)
    tk.Button(root, text="7. Escribir Nuevas Oraciones", command=escribir_nuevas_oraciones, width=40).pack(pady=5)
    tk.Button(root, text="8. Practicar Oraciones", command=practicar_oraciones, width=40).pack(pady=5)
    tk.Button(root, text="9. Salir", command=root.quit, width=40).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()
