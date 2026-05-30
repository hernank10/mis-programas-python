import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio interactivo - Gramática Castellana")
root.geometry("500x300")

# Pregunta
pregunta = "¿Cuál es la forma correcta de escribir esta palabra?"
opciones = ["halla", "haya", "aya"]
respuesta_correcta = "haya"

# Variable para mostrar mensaje de resultado
mensaje_resultado = tk.StringVar()

# Función para validar respuesta
def validar_respuesta():
    seleccion = respuesta.get()
    if seleccion == respuesta_correcta:
        mensaje_resultado.set("¡Correcto! 'Haya' es la forma adecuada.")
    else:
        mensaje_resultado.set("Incorrecto. Intenta de nuevo.")

# Mostrar pregunta
label_pregunta = tk.Label(root, text=pregunta, font=("Arial", 12))
label_pregunta.pack(pady=10)

# Opciones de respuesta
respuesta = tk.StringVar()
for opcion in opciones:
    tk.Radiobutton(root, text=opcion, variable=respuesta, value=opcion).pack()

# Botón para verificar respuesta
boton_verificar = tk.Button(root, text="Verificar", command=validar_respuesta)
boton_verificar.pack(pady=10)

# Área de resultado
label_resultado = tk.Label(root, textvariable=mensaje_resultado, font=("Arial", 12))
label_resultado.pack(pady=10)

# Ejecutar aplicación
root.mainloop()
