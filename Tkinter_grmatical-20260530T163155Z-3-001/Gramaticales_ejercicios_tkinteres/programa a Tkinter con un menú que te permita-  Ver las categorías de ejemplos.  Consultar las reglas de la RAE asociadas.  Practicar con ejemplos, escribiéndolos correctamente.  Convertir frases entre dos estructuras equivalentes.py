import tkinter as tk
from tkinter import messagebox

# Diccionario de ejemplos por categorías
ejemplos = {
    "Concesivas": [
        "Por más que estudies, no aprobarás sin práctica.",
        "Aunque lo intentes, será difícil lograrlo.",
        "Por más que no quieras, sí puedes intentarlo."
    ],
    "Condicionales": [
        "Si estudias, aprobarás.",
        "Si corres, llegarás a tiempo.",
        "Si no lo intentas, nunca sabrás el resultado."
    ],
    "Comparativas": [
        "Tan pronto como llegues, avísame.",
        "Más vale tarde que nunca.",
        "Tan fuerte como un roble."
    ],
    "Adversativas": [
        "Quiero ir, pero no puedo.",
        "Es listo, aunque un poco distraído.",
        "Lo intentó, sin embargo, falló."
    ]
}

# Reglas básicas (resumen inspirado en la RAE)
reglas = {
    "Concesivas": "Las oraciones concesivas expresan una dificultad u obstáculo que no impide la acción principal. Ej: 'Por más que estudies, aprobarás'.",
    "Condicionales": "Las oraciones condicionales expresan una condición necesaria. Ej: 'Si estudias, aprobarás'.",
    "Comparativas": "Las comparativas establecen relaciones de igualdad, inferioridad o superioridad. Ej: 'Tan rápido como un rayo'.",
    "Adversativas": "Las adversativas contraponen ideas. Ej: 'Quiero ir, pero no puedo'."
}

# Conversión entre estructuras
def convertir_frase(frase):
    if "Por más que no quieras" in frase:
        return frase.replace("Por más que no quieras, sí puedes intentarlo",
                             "Tan si quieras no puedes intentarlo")
    elif "Tan si quieras" in frase:
        return frase.replace("Tan si quieras no puedes intentarlo",
                             "Por más que no quieras, sí puedes intentarlo")
    else:
        return "Esta frase no es convertible en el sistema."

# Funciones de la GUI
def mostrar_reglas(categoria):
    messagebox.showinfo(f"Reglas de {categoria}", reglas[categoria])

def mostrar_ejemplos(categoria):
    lista = "\n".join(ejemplos[categoria])
    messagebox.showinfo(f"Ejemplos de {categoria}", lista)

def practicar(categoria):
    ventana = tk.Toplevel(root)
    ventana.title(f"Practicar {categoria}")
    ventana.geometry("400x200")

    label = tk.Label(ventana, text=f"Escribe este ejemplo:\n{ejemplos[categoria][0]}")
    label.pack(pady=10)

    entrada = tk.Entry(ventana, width=50)
    entrada.pack(pady=5)

    def verificar():
        if entrada.get().strip() == ejemplos[categoria][0]:
            messagebox.showinfo("Correcto", "¡Muy bien escrito!")
        else:
            messagebox.showerror("Error", "No coincide, revisa ortografía y acentos.")

    boton = tk.Button(ventana, text="Verificar", command=verificar)
    boton.pack(pady=10)

def convertir_interfaz():
    ventana = tk.Toplevel(root)
    ventana.title("Convertir frases")
    ventana.geometry("400x200")

    label = tk.Label(ventana, text="Escribe la frase a convertir:")
    label.pack(pady=10)

    entrada = tk.Entry(ventana, width=50)
    entrada.pack(pady=5)

    def procesar():
        frase = entrada.get().strip()
        resultado = convertir_frase(frase)
        messagebox.showinfo("Resultado", resultado)

    boton = tk.Button(ventana, text="Convertir", command=procesar)
    boton.pack(pady=10)

# Interfaz principal
root = tk.Tk()
root.title("Aprender Gramática con Ejemplos")
root.geometry("500x400")

titulo = tk.Label(root, text="Menú de Gramática", font=("Arial", 16, "bold"))
titulo.pack(pady=15)

for categoria in ejemplos.keys():
    frame = tk.Frame(root)
    frame.pack(pady=5)

    btn1 = tk.Button(frame, text=f"Reglas {categoria}", command=lambda c=categoria: mostrar_reglas(c))
    btn1.grid(row=0, column=0, padx=5)

    btn2 = tk.Button(frame, text=f"Ejemplos {categoria}", command=lambda c=categoria: mostrar_ejemplos(c))
    btn2.grid(row=0, column=1, padx=5)

    btn3 = tk.Button(frame, text=f"Practicar {categoria}", command=lambda c=categoria: practicar(c))
    btn3.grid(row=0, column=2, padx=5)

# Botón de conversión
btn_convertir = tk.Button(root, text="Convertir frases especiales", command=convertir_interfaz)
btn_convertir.pack(pady=20)

root.mainloop()
