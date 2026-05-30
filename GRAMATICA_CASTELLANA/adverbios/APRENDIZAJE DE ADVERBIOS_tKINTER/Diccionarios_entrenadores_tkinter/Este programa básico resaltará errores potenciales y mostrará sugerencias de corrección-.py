import tkinter as tk
from tkinter import messagebox
import re

# Función que simula la revisión gramatical
def revisar_gramatica():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un texto.")
        return
    
    # Ejemplo simple de detección de errores
    errores = []
    if not texto.endswith(('.', '!', '?')):
        errores.append("La oración debe terminar con un punto, signo de exclamación o interrogación.")
    
    if "yo" in texto.lower() and texto.lower().count("yo") > 1:
        errores.append("Se repite 'yo' en la oración, intenta evitar redundancias.")
    
    # Mostrar resultados
    if errores:
        resultado = "\n".join(errores)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, f"Errores detectados:\n{resultado}")
        resultado_texto.config(state=tk.DISABLED)
    else:
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, "¡Sin errores detectados!")
        resultado_texto.config(state=tk.DISABLED)
        messagebox.showinfo("Revisión completa", "¡Tu texto es correcto!")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Revisión Gramatical Básica")
ventana.geometry("600x400")

# Widgets de la interfaz
label = tk.Label(ventana, text="Ingresa tu oración:", font=("Arial", 14))
label.pack(pady=10)

entrada_texto = tk.Text(ventana, height=5, width=60, font=("Arial", 12))
entrada_texto.pack(pady=10)

boton_revisar = tk.Button(ventana, text="Revisar Gramática", command=revisar_gramatica, font=("Arial", 12), bg="lightblue")
boton_revisar.pack(pady=10)

resultado_texto = tk.Text(ventana, height=5, width=60, font=("Arial", 12))
resultado_texto.pack(pady=10)
resultado_texto.config(state=tk.DISABLED)

# Iniciar el loop de la aplicación
ventana.mainloop()
