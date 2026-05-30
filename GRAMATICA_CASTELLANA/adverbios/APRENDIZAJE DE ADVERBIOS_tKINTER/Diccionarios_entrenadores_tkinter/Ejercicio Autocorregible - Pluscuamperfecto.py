import tkinter as tk
import difflib

# Crear ventana principal
root = tk.Tk()
root.title("Ejercicio Autocorregible - Pluscuamperfecto")
root.geometry("600x400")

# Reglas gramaticales del pluscuamperfecto
reglas_pluscuamperfecto = """
📜 Reglas:  
El pluscuamperfecto indica una acción pasada anterior a otra.  
Se forma con 'haber' en imperfecto + participio del verbo.  
Ejemplo: "Cuando llegué, ya habían comido."
"""

# Texto modelo de referencia
texto_modelo = "Cuando llegué, ellos ya habían salido."

# Función para validar el texto del usuario
def validar_texto():
    contenido = area_texto.get("1.0", tk.END).strip()
    palabras_clave = ["había", "habías", "habíamos", "habían"]

    if any(palabra in contenido for palabra in palabras_clave):
        similitud = difflib.SequenceMatcher(None, contenido.lower(), texto_modelo.lower()).ratio()
        
        if similitud > 0.6:
            mensaje.set("✅ ¡Tu respuesta es correcta!")
        else:
            mensaje.set("⚠️ Usaste el pluscuamperfecto, pero la estructura puede mejorar.")
    else:
        mensaje.set("❌ No encontré verbos en pluscuamperfecto. Intenta nuevamente.")

# Mostrar reglas
tk.Label(root, text="📖 Reglas del Pluscuamperfecto", font=("Arial", 14, "bold")).pack(pady=5)
tk.Label(root, text=reglas_pluscuamperfecto, font=("Arial", 12), wraplength=550).pack(pady=5)

# Área de redacción
area_texto = tk.Text(root, height=5, width=60, font=("Arial", 12))
area_texto.pack(pady=10)

# Botón para validar
tk.Button(root, text="Validar Redacción", command=validar_texto).pack(pady=5)

# Mensaje de resultado
mensaje = tk.StringVar()
tk.Label(root, textvariable=mensaje, font=("Arial", 12, "italic"), fg="blue").pack(pady=5)

# Ejecutar aplicación
root.mainloop()
