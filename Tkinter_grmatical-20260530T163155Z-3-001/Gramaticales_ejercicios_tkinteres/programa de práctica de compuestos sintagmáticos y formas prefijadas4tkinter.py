import json
import tkinter as tk
from tkinter import messagebox

# Archivo donde se guardarán los ejemplos del usuario
FILE_NAME = "ejemplos_usuario.json"

# Teoría sobre los compuestos sintagmáticos y formas prefijadas
TEORIA = """
Los compuestos sintagmáticos y algunas formas prefijadas pueden escribirse de distintas maneras. 
Algunos se escriben en una sola palabra (ej. "mediodía"), mientras que otros deben mantenerse en dos palabras (ej. "medio ambiente").

Ejemplos:
- "Medio día" (incorrecto) → "Mediodía" (correcto)
- "Centro derecha" (incorrecto) → "Centroderecha" (correcto)
- "Sin techo" (correcto) → "Sintecho" (correcto en algunos casos, dependiendo del uso)
"""

# Lista de ejercicios de completación
EJERCICIOS_COMPLETACION = [
    {"oracion": "Cuidamos el ____ ambiente.", "respuesta": "medioambiente"},
    {"oracion": "Se reunieron los líderes de ____ derecha.", "respuesta": "centroderecha"},
    {"oracion": "Salimos a caminar al ____ día.", "respuesta": "mediodía"},
    {"oracion": "Vive en la calle, es un ____ techo.", "respuesta": "sintecho"},
    {"oracion": "El futbolista juega en el ____ campo.", "respuesta": "mediocampo"}
]

# Cargar ejemplos del usuario si existen
def cargar_ejemplos():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guardar ejemplos del usuario
def guardar_ejemplos(ejemplo):
    ejemplos = cargar_ejemplos()
    if len(ejemplos) < 100:
        ejemplos.append(ejemplo)
        with open(FILE_NAME, "w") as file:
            json.dump(ejemplos, file, indent=4)
    else:
        messagebox.showwarning("Límite alcanzado", "Has alcanzado el límite de 100 ejemplos guardados.")

# Función para los ejercicios de completación
def ejercicios_completacion():
    def verificar_respuesta():
        respuesta = entrada.get().strip().lower()
        if respuesta == ejercicio["respuesta"]:
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        else:
            messagebox.showerror("Incorrecto", f"Respuesta incorrecta. La correcta es: {ejercicio['respuesta']}")
    
    ventana = tk.Toplevel()
    ventana.title("Ejercicios de Completación")
    
    ejercicio = EJERCICIOS_COMPLETACION[0]
    tk.Label(ventana, text=ejercicio["oracion"], font=("Arial", 12)).pack(pady=10)
    entrada = tk.Entry(ventana, font=("Arial", 12))
    entrada.pack(pady=5)
    tk.Button(ventana, text="Verificar", command=verificar_respuesta).pack(pady=10)

# Función para los ejercicios de redacción
def ejercicios_redaccion():
    def guardar_oracion():
        oracion = entrada.get()
        guardar_ejemplos(oracion)
        messagebox.showinfo("Guardado", "Tu oración ha sido guardada.")
    
    ventana = tk.Toplevel()
    ventana.title("Ejercicios de Redacción")
    
    tk.Label(ventana, text="Escribe una oración con una de las siguientes palabras:", font=("Arial", 12)).pack(pady=10)
    tk.Label(ventana, text=", ".join([e["respuesta"] for e in EJERCICIOS_COMPLETACION]), wraplength=400, font=("Arial", 10)).pack(pady=5)
    entrada = tk.Entry(ventana, font=("Arial", 12), width=50)
    entrada.pack(pady=5)
    tk.Button(ventana, text="Guardar", command=guardar_oracion).pack(pady=10)

# Función principal
def main():
    root = tk.Tk()
    root.title("Práctica de Compuestos Sintagmáticos")
    root.geometry("500x400")
    
    tk.Label(root, text="Práctica de Compuestos Sintagmáticos", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(root, text=TEORIA, wraplength=450, justify="left", font=("Arial", 10)).pack(pady=10)
    
    tk.Button(root, text="Ejercicios de Completación", command=ejercicios_completacion, width=30).pack(pady=5)
    tk.Button(root, text="Ejercicios de Redacción", command=ejercicios_redaccion, width=30).pack(pady=5)
    
    root.mainloop()

# Ejecutar el programa
if __name__ == "__main__":
    main()
