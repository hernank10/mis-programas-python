import tkinter as tk
from tkinter import messagebox
import random

# =================== TEMAS ======================
temas = {
    "Uso del punto y coma": [
        ("Separa oraciones independientes que están estrechamente relacionadas.",
         "Llegó tarde a casa; sin embargo, cenó con su familia."),
        ("Separa elementos complejos en una enumeración.",
         "Invité a Juan, el médico; a Luis, el abogado; y a Marta, la profesora."),
        ("Antes de conectores adversativos como 'sin embargo', 'no obstante'.",
         "Estudió mucho; sin embargo, no aprobó el examen."),
    ],
    "Uso de la 'b' y la 'v'": [
        ("Se escriben con 'b' los verbos terminados en -bir, excepto hervir, servir y vivir.",
         "Escribir, recibir, prohibir."),
        ("Se escriben con 'v' las palabras que empiezan con eva-, eve-, evi-, evo-.",
         "Evidente, evolución, evasión."),
        ("Después de b, d o n se escribe 'v'.",
         "Obvio, advertir, inventar."),
    ],
    "Tipos de oraciones compuestas": [
        ("Coordinadas copulativas: unen ideas con 'y', 'e', 'ni'.",
         "Pedro lee y Ana escribe."),
        ("Coordinadas adversativas: expresan contraste con 'pero', 'aunque', 'sin embargo'.",
         "Quise ir, pero estaba lloviendo."),
        ("Coordinadas disyuntivas: ofrecen opciones con 'o', 'u'.",
         "¿Vienes o te quedas?"),
        ("Coordinadas explicativas: aclaran una idea con 'es decir', 'esto es'.",
         "Juan es mi primo, es decir, el hijo de mi tía."),
        ("Subordinadas sustantivas: funcionan como un sustantivo dentro de la oración.",
         "Me alegra que vengas."),
        ("Subordinadas adjetivas: funcionan como adjetivo calificando un sustantivo.",
         "El coche que compré es rojo."),
        ("Subordinadas adverbiales: expresan tiempo, causa, condición...",
         "Lo haré cuando vuelva."),
        ("Yuxtapuestas: se separan con coma, punto y coma o dos puntos.",
         "Salió temprano, regresó tarde."),
    ]
}

# =================== VENTANA PRINCIPAL ======================
class PracticaOrtografia:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Ortografía")
        self.tema = tk.StringVar()
        self.modo = tk.StringVar(value="practica")
        self.score = 0
        self.index = 0
        self.lista_ejercicios = []
        self.crear_menu()

    def crear_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Elige un tema:").pack()
        for t in temas:
            tk.Radiobutton(self.root, text=t, variable=self.tema, value=t).pack(anchor="w")

        tk.Label(self.root, text="Elige el modo:").pack()
        tk.Radiobutton(self.root, text="Práctica", variable=self.modo, value="practica").pack(anchor="w")
        tk.Radiobutton(self.root, text="Examen", variable=self.modo, value="examen").pack(anchor="w")

        tk.Button(self.root, text="Comenzar", command=self.iniciar_ejercicio).pack(pady=10)

    def iniciar_ejercicio(self):
        if not self.tema.get():
            messagebox.showwarning("Atención", "Debes seleccionar un tema.")
            return
        self.score = 0
        self.index = 0
        self.lista_ejercicios = temas[self.tema.get()]
        random.shuffle(self.lista_ejercicios)
        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.index >= len(self.lista_ejercicios):
            self.mostrar_resultado()
            return

        regla, ejemplo = self.lista_ejercicios[self.index]

        tk.Label(self.root, text=f"Ejercicio {self.index + 1} de {len(self.lista_ejercicios)}").pack()

        if self.modo.get() == "practica":
            tk.Label(self.root, text=f"Regla: {regla}", wraplength=500).pack(pady=10)

        tk.Label(self.root, text="Escribe una oración que cumpla con esta regla:").pack()
        self.respuesta = tk.Text(self.root, height=3, width=60)
        self.respuesta.pack()

        tk.Button(self.root, text="Enviar", command=self.verificar_respuesta).pack(pady=5)

    def verificar_respuesta(self):
        user_input = self.respuesta.get("1.0", "end").strip()
        if user_input:
            self.score += 1
        self.index += 1
        self.mostrar_ejercicio()

    def mostrar_resultado(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Resultado final").pack()
        tk.Label(self.root, text=f"Puntaje: {self.score} de {len(self.lista_ejercicios)}").pack()
        tk.Button(self.root, text="Volver al menú", command=self.crear_menu).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = PracticaOrtografia(root)
    root.mainloop()
