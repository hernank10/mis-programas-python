import tkinter as tk
from tkinter import messagebox

# Función para verificar respuestas
def verificar_respuestas():
    respuestas_correctas = ["se", "se", "se"]
    respuestas_usuario = [entrada1.get(), entrada2.get(), entrada3.get()]
    
    aciertos = sum([1 for i in range(3) if respuestas_usuario[i].strip().lower() == respuestas_correctas[i]])
    messagebox.showinfo("Resultado", f"Has acertado {aciertos} de 3 respuestas.")

# Crear ventana principal
root = tk.Tk()
root.title("Práctica de Oraciones Impersonales")

# Instrucciones
instrucciones = tk.Label(root, text="Completa las oraciones con la forma correcta de oraciones impersonales:")
instrucciones.pack()

# Ejercicios
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="_______ se dice que la gramática es compleja.").grid(row=0, column=0)
entrada1 = tk.Entry(frame)
entrada1.grid(row=0, column=1)

tk.Label(frame, text="_______ necesita estudiar más para mejorar en español.").grid(row=1, column=0)
entrada2 = tk.Entry(frame)
entrada2.grid(row=1, column=1)

tk.Label(frame, text="En este país, _______ habla español con fluidez.").grid(row=2, column=0)
entrada3 = tk.Entry(frame)
entrada3.grid(row=2, column=1)

# Botón de verificación
boton_verificar = tk.Button(root, text="Verificar respuestas", command=verificar_respuestas)
boton_verificar.pack()

root.mainloop()
