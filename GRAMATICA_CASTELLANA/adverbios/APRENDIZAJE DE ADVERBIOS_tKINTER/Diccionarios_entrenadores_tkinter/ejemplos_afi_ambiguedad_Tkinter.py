import tkinter as tk
from tkinter import messagebox, ttk
import csv

# Leer los datos desde el archivo CSV
def cargar_ejemplos():
    ejemplos = []
    with open("/mnt/data/ejemplos_afi_ambiguedad.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            ejemplos.append(fila)
    return ejemplos

# Verificar la respuesta del usuario
def verificar_respuesta():
    respuesta = entrada_afi.get().strip()
    correcto = ejemplos[indice_actual[0]]["AFI"].strip()
    if respuesta == correcto:
        messagebox.showinfo("¡Correcto!", "¡Has escrito correctamente la transcripción AFI!")
        siguiente_ejemplo()
    else:
        messagebox.showerror("Incorrecto", f"La transcripción correcta era: {correcto}")

# Mostrar el siguiente ejemplo
def siguiente_ejemplo():
    if indice_actual[0] < len(ejemplos) - 1:
        indice_actual[0] += 1
        mostrar_ejemplo()
    else:
        messagebox.showinfo("Fin", "¡Has completado todos los ejemplos!")
        ventana.quit()

# Mostrar el ejemplo actual en la interfaz
def mostrar_ejemplo():
    ejemplo = ejemplos[indice_actual[0]]
    texto_ejemplo.set(f"Ejemplo {indice_actual[0]+1}: {ejemplo['Ejemplo']}\nInterpretación: {ejemplo['Interpretación']}\nClasificación: {ejemplo['Clasificación']}")

# Inicialización de la ventana
ventana = tk.Tk()
ventana.title("Práctica de transcripción AFI")
ventana.geometry("600x400")

ejemplos = cargar_ejemplos()
indice_actual = [0]

texto_ejemplo = tk.StringVar()
mostrar_ejemplo()

etiqueta = ttk.Label(ventana, textvariable=texto_ejemplo, wraplength=550)
etiqueta.pack(pady=20)

entrada_afi = ttk.Entry(ventana, width=50)
entrada_afi.pack(pady=10)

boton_verificar = ttk.Button(ventana, text="Verificar", command=verificar_respuesta)
boton_verificar.pack(pady=5)

boton_siguiente = ttk.Button(ventana, text="Siguiente", command=siguiente_ejemplo)
boton_siguiente.pack(pady=5)

ventana.mainloop()
