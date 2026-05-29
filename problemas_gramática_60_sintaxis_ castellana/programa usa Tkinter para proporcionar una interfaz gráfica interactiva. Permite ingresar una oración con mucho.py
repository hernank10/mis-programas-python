import tkinter as tk
from tkinter import messagebox

def analizar_oracion():
    oracion = entrada_oracion.get()
    interpretacion = opcion_seleccionada.get()
    
    if not oracion:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una oración.")
        return
    
    resultado = f"Oración: {oracion}\nInterpretación seleccionada: {interpretacion}"
    messagebox.showinfo("Análisis", resultado)

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.title("Interpretaciones de 'mucho'")
ventana.geometry("400x300")

tk.Label(ventana, text="Ingrese una oración con 'mucho':").pack(pady=5)
entrada_oracion = tk.Entry(ventana, width=50)
entrada_oracion.pack(pady=5)

opcion_seleccionada = tk.StringVar(value="Intensamente")

interpretaciones = ["Intensamente", "Con frecuencia", "Por mucho tiempo", "Cantidad"]

tk.Label(ventana, text="Seleccione la interpretación:").pack(pady=5)
for interpretacion in interpretaciones:
    tk.Radiobutton(ventana, text=interpretacion, variable=opcion_seleccionada, value=interpretacion).pack()

tk.Button(ventana, text="Analizar", command=analizar_oracion).pack(pady=10)
tk.Button(ventana, text="Salir", command=salir).pack(pady=5)

ventana.mainloop()
