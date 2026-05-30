import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio de Caligrafía")
ventana.geometry("600x400")

# Texto en diferentes idiomas
texto_ejemplo = "\u3053\u308c\u306f\u554f\u984c\u3067\u3059"  # Japonés

# Etiqueta para mostrar el texto
etiqueta = tk.Label(ventana, text=texto_ejemplo, font=("Hiragino Sans", 24))
etiqueta.pack(pady=20)

# Entrada para escribir
entrada = tk.Entry(ventana, font=("Arial", 20))
entrada.pack(pady=10)

# Verificar la respuesta
def verificar():
    if entrada.get() == texto_ejemplo:
        resultado.config(text="¡Correcto!", fg="green")
    else:
        resultado.config(text="Incorrecto. Intenta de nuevo.", fg="red")

boton = tk.Button(ventana, text="Verificar", command=verificar)
boton.pack(pady=10)

# Etiqueta para resultado
resultado = tk.Label(ventana, text="", font=("Arial", 16))
resultado.pack(pady=20)

ventana.mainloop()
