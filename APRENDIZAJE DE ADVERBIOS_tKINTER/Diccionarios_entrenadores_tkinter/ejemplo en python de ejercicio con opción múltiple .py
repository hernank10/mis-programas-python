import tkinter as tk

# Crear ventana
root = tk.Tk()
root.title("Ejercicio de Gramática")
root.geometry("500x300")

# Pregunta
pregunta = "¿Cuál es la forma correcta del verbo en pluscuamperfecto?"
opciones = ["había cantado", "cantó", "cantaría"]
respuesta_correcta = "había cantado"

# Variable para la selección
respuesta_usuario = tk.StringVar()

# Validar respuesta
def verificar_respuesta():
    if respuesta_usuario.get() == respuesta_correcta:
        resultado.set("¡Correcto!")
    else:
        resultado.set("Incorrecto, intenta de nuevo.")

# Mostrar pregunta
tk.Label(root, text=pregunta, font=("Arial", 12)).pack(pady=10)

# Opciones
for opcion in opciones:
    tk.Radiobutton(root, text=opcion, variable=respuesta_usuario, value=opcion).pack()

# Botón de verificación
tk.Button(root, text="Verificar", command=verificar_respuesta).pack(pady=10)

# Área de resultado
resultado = tk.StringVar()
tk.Label(root, textvariable=resultado, font=("Arial", 12)).pack(pady=10)

# Ejecutar aplicación
root.mainloop()
