import tkinter as tk
from tkinter import messagebox

def mostrar_teoria():
    messagebox.showinfo("Teoría", "Los verbos de apoyo forman una unidad semántica con un sustantivo, creando expresiones como 'dar un paseo' o 'tomar una decisión'.")

def mostrar_ejemplos():
    ejemplos = "\n- Dar un paseo\n- Echar una mirada\n- Hacer un esfuerzo\n- Tomar una decisión\n- Tener en cuenta"
    messagebox.showinfo("Ejemplos", f"Ejemplos de verbos de apoyo:{ejemplos}")

def ejercicio_escritura():
    def guardar_texto():
        texto = entrada.get()
        messagebox.showinfo("Respuesta guardada", "Gracias por tu respuesta. Puedes seguir practicando más oraciones.")
        entrada.delete(0, tk.END)
    
    ventana = tk.Toplevel(root)
    ventana.title("Ejercicio de Escritura")
    tk.Label(ventana, text="Escribe una oración usando un verbo de apoyo:").pack()
    entrada = tk.Entry(ventana, width=50)
    entrada.pack()
    tk.Button(ventana, text="Guardar", command=guardar_texto).pack()

def test_interactivo():
    preguntas = [
        ("¿Cuál de las siguientes es una construcción con verbo de apoyo?", ["Comer una manzana", "Tomar una decisión", "Correr rápido"], 1),
        ("¿Cuál es un verbo de apoyo típico?", ["Saltar", "Hacer", "Llorar"], 1),
    ]
    
    def verificar_respuesta(i, seleccion):
        if seleccion == preguntas[i][2]:
            messagebox.showinfo("Resultado", "¡Correcto!")
        else:
            messagebox.showerror("Resultado", "Incorrecto.")
    
    ventana = tk.Toplevel(root)
    ventana.title("Test Interactivo")
    
    for i, (pregunta, opciones, correcta) in enumerate(preguntas):
        tk.Label(ventana, text=pregunta).pack()
        for j, opcion in enumerate(opciones):
            tk.Button(ventana, text=opcion, command=lambda i=i, j=j: verificar_respuesta(i, j)).pack()

def salir():
    root.destroy()

def menu():
    global root
    root = tk.Tk()
    root.title("Práctica de Verbos de Apoyo")
    
    tk.Label(root, text="*** MENÚ PRINCIPAL ***").pack()
    tk.Button(root, text="Ver teoría sobre verbos de apoyo", command=mostrar_teoria).pack()
    tk.Button(root, text="Ver ejemplos de verbos de apoyo", command=mostrar_ejemplos).pack()
    tk.Button(root, text="Practicar escritura de oraciones", command=ejercicio_escritura).pack()
    tk.Button(root, text="Realizar un test interactivo", command=test_interactivo).pack()
    tk.Button(root, text="Salir", command=salir).pack()
    
    root.mainloop()

if __name__ == "__main__":
    menu()
