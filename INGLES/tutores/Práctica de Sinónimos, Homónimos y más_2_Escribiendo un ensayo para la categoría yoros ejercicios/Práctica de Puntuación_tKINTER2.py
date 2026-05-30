import tkinter as tk
from tkinter import messagebox

class PunctuationPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Signos de Puntuación")
        self.root.geometry("600x500")

        # Diccionario de ejercicios por tipo de signo
        self.ejercicios_por_signo = {
            "Coma": [
                {"sin": "Vamos a comer niños", "correcto": "Vamos a comer, niños."},
                {"sin": "María Pedro Ana y Luis vinieron", "correcto": "María, Pedro, Ana y Luis vinieron."}
            ],
            "Punto y coma": [
                {"sin": "Estudié toda la noche sin embargo no aprobé", "correcto": "Estudié toda la noche; sin embargo, no aprobé."},
                {"sin": "Era tarde estaba cansado", "correcto": "Era tarde; estaba cansado."}
            ],
            "Dos puntos": [
                {"sin": "Ella dijo Estoy feliz", "correcto": "Ella dijo: Estoy feliz."},
                {"sin": "Llevó lo necesario agua pan y una linterna", "correcto": "Llevó lo necesario: agua, pan y una linterna."}
            ],
            "Guiones": [
                {"sin": "El problema es económico político y social", "correcto": "El problema es económico-político y social."},
                {"sin": "La reunión fue martes miércoles y jueves", "correcto": "La reunión fue martes-miércoles y jueves."}
            ],
            "Paréntesis": [
                {"sin": "Mi madre que es doctora me cuidó", "correcto": "Mi madre (que es doctora) me cuidó."},
                {"sin": "Estaré ausente por motivos personales de salud", "correcto": "Estaré ausente (por motivos personales de salud)."}
            ],
            "Interrogación": [
                {"sin": "Dónde vives", "correcto": "¿Dónde vives?"},
                {"sin": "Qué hora es", "correcto": "¿Qué hora es?"}
            ],
            "Exclamación": [
                {"sin": "Qué sorpresa", "correcto": "¡Qué sorpresa!"},
                {"sin": "Feliz cumpleaños", "correcto": "¡Feliz cumpleaños!"}
            ],
            "Comillas": [
                {"sin": "Ella dijo No me gusta", "correcto": "Ella dijo: \"No me gusta\"."},
                {"sin": "La palabra casa viene del latín", "correcto": "La palabra \"casa\" viene del latín."}
            ],
            "Puntos suspensivos": [
                {"sin": "No sé qué decir", "correcto": "No sé qué decir..."},
                {"sin": "Tal vez mañana o pasado", "correcto": "Tal vez mañana... o pasado."}
            ]
        }

        self.ejercicios = []
        self.index = 0

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        # Frame con botones de signos
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=10)

        for signo in self.ejercicios_por_signo:
            btn = tk.Button(self.menu_frame, text=signo, width=14, command=lambda s=signo: self.load_ejercicios(s))
            btn.pack(side=tk.LEFT, padx=5)

    def create_widgets(self):
        # Muestra el ejemplo sin puntuación
        self.label_ejemplo = tk.Label(self.root, text="Selecciona un signo para comenzar", font=("Arial", 14))
        self.label_ejemplo.pack(pady=20)

        # Entrada del usuario
        self.entry_respuesta = tk.Entry(self.root, width=60, font=("Arial", 12))
        self.entry_respuesta.pack(pady=10)

        # Botón de verificar
        self.btn_verificar = tk.Button(self.root, text="Verificar respuesta", font=("Arial", 12), command=self.verificar)
        self.btn_verificar.pack(pady=10)

    def load_ejercicios(self, signo):
        self.ejercicios = self.ejercicios_por_signo[signo]
        self.index = 0
        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        if self.index < len(self.ejercicios):
            ejercicio = self.ejercicios[self.index]
            self.label_ejemplo.config(text=f"Corrige: {ejercicio['sin']}")
            self.entry_respuesta.delete(0, tk.END)
        else:
            messagebox.showinfo("¡Completado!", "Has terminado todos los ejercicios de este grupo.")

    def verificar(self):
        if not self.ejercicios:
            messagebox.showwarning("Atención", "Primero selecciona un signo del menú.")
            return

        usuario = self.entry_respuesta.get().strip()
        correcto = self.ejercicios[self.index]["correcto"]

        if usuario == correcto:
            messagebox.showinfo("Correcto", "¡Bien hecho!")
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era:\n{correcto}")

        self.index += 1
        self.mostrar_ejercicio()


# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = PunctuationPracticeApp(root)
    root.mainloop()
