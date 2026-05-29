import tkinter as tk
from tkinter import messagebox
import random

def mostrar_teoria():
    teoria = """
    En español, los dativos no seleccionados aparecen en construcciones anticausativas
    y pueden interpretarse como causantes accidentales. Ejemplo:
    - Juan rompió el móvil. (transitiva)
    - A Juan se le rompió el móvil. (anticausativa con dativo)
    """
    messagebox.showinfo("Teoría", teoria)

def mostrar_ejemplos():
    ejemplos = [
        "A Pedro se le cayó el vaso.",
        "A María se le perdió la llave.",
        "A Juan se le olvidó la cita.",
        "A Sofía se le quemó la comida."
    ]
    messagebox.showinfo("Ejemplos", "\n".join(ejemplos))

def practicar_escritura():
    def verificar_oracion():
        oracion = entrada.get()
        if "se le" in oracion or "a " in oracion:
            messagebox.showinfo("Resultado", "¡Bien! Tu oración contiene un dativo no seleccionado.")
        else:
            messagebox.showwarning("Resultado", "Revisa la estructura, intenta incluir 'se le' y un verbo de cambio de estado.")
    
    ventana_ejercicio = tk.Toplevel()
    ventana_ejercicio.title("Practicar Escritura")
    tk.Label(ventana_ejercicio, text="Escribe una oración con un dativo no seleccionado:").pack()
    entrada = tk.Entry(ventana_ejercicio, width=50)
    entrada.pack()
    tk.Button(ventana_ejercicio, text="Verificar", command=verificar_oracion).pack()

def test_interactivo():
    preguntas = {
        "¿Cuál de estas oraciones tiene un dativo no seleccionado?": {
            "A": "Pedro rompió el vaso.",
            "B": "A Pedro se le rompió el vaso.",
            "C": "Pedro tiene un vaso azul.",
            "respuesta": "B"
        },
        "En la oración 'A Sofía se le cayó el libro', ¿qué función tiene 'A Sofía'?": {
            "A": "Sujeto",
            "B": "Objeto directo",
            "C": "Dativo no seleccionado",
            "respuesta": "C"
        }
    }
    
    def hacer_pregunta():
        pregunta, opciones = random.choice(list(preguntas.items()))
        ventana_pregunta = tk.Toplevel()
        ventana_pregunta.title("Test Interactivo")
        tk.Label(ventana_pregunta, text=pregunta).pack()
        
        def verificar_respuesta(opcion):
            if opcion == opciones["respuesta"]:
                messagebox.showinfo("Resultado", "¡Correcto!")
            else:
                messagebox.showwarning("Resultado", f"Incorrecto. La respuesta correcta era {opciones['respuesta']}.")
            ventana_pregunta.destroy()
        
        for clave, valor in opciones.items():
            if clave != "respuesta":
                tk.Button(ventana_pregunta, text=valor, command=lambda c=clave: verificar_respuesta(c)).pack()
    
    hacer_pregunta()

def menu():
    root = tk.Tk()
    root.title("Práctica de Dativos No Seleccionados")
    tk.Label(root, text="Menú de práctica", font=("Arial", 14)).pack()
    tk.Button(root, text="Leer teoría", command=mostrar_teoria).pack(fill="x")
    tk.Button(root, text="Ver ejemplos", command=mostrar_ejemplos).pack(fill="x")
    tk.Button(root, text="Practicar escritura", command=practicar_escritura).pack(fill="x")
    tk.Button(root, text="Test interactivo", command=test_interactivo).pack(fill="x")
    tk.Button(root, text="Salir", command=root.quit).pack(fill="x")
    root.mainloop()

if __name__ == "__main__":
    menu()
