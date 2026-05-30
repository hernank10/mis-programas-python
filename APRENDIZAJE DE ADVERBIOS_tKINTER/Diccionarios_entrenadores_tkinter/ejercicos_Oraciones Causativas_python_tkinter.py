import tkinter as tk
from tkinter import messagebox, simpledialog

class OracionesCausativasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oraciones Causativas")
        self.root.geometry("400x300")

        tk.Label(root, text="Menú Principal", font=("Arial", 14)).pack(pady=10)

        tk.Button(root, text="Ver Teoría", command=self.mostrar_teoria).pack(pady=5)
        tk.Button(root, text="Ver Ejemplos", command=self.mostrar_ejemplos).pack(pady=5)
        tk.Button(root, text="Practicar Escritura", command=self.ejercicio_escritura).pack(pady=5)
        tk.Button(root, text="Realizar Test", command=self.test_interactivo).pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=10)
    
    def mostrar_teoria(self):
        teoria = ("Las oraciones causativas usan el verbo 'hacer' para indicar que una acción es causada por alguien o algo.\n"
                  "Ejemplo: 'La lluvia hace crecer las plantas'.")
        messagebox.showinfo("Teoría", teoria)
    
    def mostrar_ejemplos(self):
        ejemplos = ("Ejemplos de oraciones causativas:\n"
                    "1. La guerra hizo subir los precios.\n"
                    "2. La lluvia hace crecer las plantas.\n"
                    "3. El jefe nos hizo subir los precios.")
        messagebox.showinfo("Ejemplos", ejemplos)
    
    def ejercicio_escritura(self):
        respuesta = simpledialog.askstring("Practicar Escritura", "Escribe una oración usando 'hacer' como verbo causativo:")
        if respuesta:
            messagebox.showinfo("Respuesta Guardada", f"Tu oración: {respuesta}")
    
    def test_interactivo(self):
        preguntas = [
            ("¿Cuál de las siguientes es una oración causativa?", ["La guerra hizo subir los precios", "El niño juega en el parque", "Cociné la cena"], 0),
            ("¿Qué verbo se usa en las oraciones causativas?", ["Ser", "Hacer", "Tener"], 1)
        ]
        
        for pregunta, opciones, correcta in preguntas:
            respuesta = simpledialog.askstring("Test", f"{pregunta}\nOpciones: {', '.join(opciones)}")
            if respuesta and respuesta.strip() == opciones[correcta]:
                messagebox.showinfo("Resultado", "¡Correcto!")
            else:
                messagebox.showwarning("Resultado", "Incorrecto.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OracionesCausativasApp(root)
    root.mainloop()
