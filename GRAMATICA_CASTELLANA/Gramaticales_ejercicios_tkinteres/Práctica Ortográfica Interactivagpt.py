import tkinter as tk
from tkinter import messagebox
import random

# ===================
# DATOS DE LOS TEMAS
# ===================

# Tema 1: Uso del punto y coma
punto_y_coma = [
    ("Separa oraciones que están estrechamente relacionadas entre sí", "Separa oraciones relacionadas"),
    ("Antes de conectores como sin embargo, no obstante, aunque", "Antes de conectores"),
    ("Para separar elementos complejos de una enumeración", "Separar elementos complejos"),
    ("Cuando el verbo está elíptico (omitido) en una oración compuesta", "Verbo elíptico"),
    ("Para contrastar ideas en una misma oración", "Contrastar ideas"),
    ("Separar proposiciones yuxtapuestas extensas", "Proposiciones yuxtapuestas"),
    ("Antes de una oración que explica o resume lo anterior", "Explicación o resumen"),
    ("En textos jurídicos para separar incisos largos", "Textos jurídicos"),
    ("Cuando hay comas internas en los miembros de la oración", "Comas internas"),
    ("Para reforzar la pausa mayor sin terminar el enunciado", "Pausa mayor sin terminar")
]

# Tema 2: Uso de la "b" y la "v"
b_y_v = [
    ("Después de m se escribe b (ej: cambiar)", "Después de m"),
    ("Los verbos terminados en -bir (excepto hervir, servir y vivir)", "Verbos en -bir"),
    ("Las palabras que empiezan con bu-, bur-, bus-", "Empieza con bu-, bur-, bus-"),
    ("Las terminaciones -aba, -abas, -ábamos, -aban", "Terminaciones -aba..."),
    ("Los adjetivos terminados en -ívoro, -ívora", "Adjetivos -ívoro"),
    ("Palabras derivadas de otras que llevan b (ej: biblioteca -> bibliófilo)", "Derivadas con b"),
    ("Después de ol se escribe v (ej: volver)", "Después de ol"),
    ("Palabras que terminan en -ivo, -iva (excepto nocivo, lascivo)", "Terminaciones -ivo"),
    ("Los adjetivos que terminan en -ave, -avo, -eva, -eve, -evo", "Adjetivos -ave, -eva..."),
    ("Las palabras que empiezan con vice-, villa-, villar-", "Empieza con vice-, villa-")
]

# Temas disponibles
temas = {
    "Uso del punto y coma": punto_y_coma,
    "Uso de 'b' y 'v'": b_y_v
}

# ===================
# LÓGICA DEL PROGRAMA
# ===================
class ProgramaOrtografia:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica Ortográfica Interactiva")
        self.tema = None
        self.modo = None
        self.puntaje = 0
        self.total = 0
        self.ejercicios = []
        self.indice = 0

        self.crear_interfaz_inicio()

    def crear_interfaz_inicio(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Selecciona el tema", font=("Arial", 16)).pack(pady=10)

        for nombre in temas:
            tk.Button(self.root, text=nombre, width=40, command=lambda n=nombre: self.seleccionar_tema(n)).pack(pady=5)

    def seleccionar_tema(self, nombre):
        self.tema = nombre
        self.ejercicios = temas[nombre].copy()
        random.shuffle(self.ejercicios)
        self.mostrar_menu_modo()

    def mostrar_menu_modo(self):
        self.limpiar_ventana()
        tk.Label(self.root, text=f"Tema: {self.tema}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Modo práctica", command=lambda: self.iniciar_modo("practica"), width=30).pack(pady=5)
        tk.Button(self.root, text="Modo examen", command=lambda: self.iniciar_modo("examen"), width=30).pack(pady=5)

    def iniciar_modo(self, modo):
        self.modo = modo
        self.puntaje = 0
        self.total = len(self.ejercicios)
        self.indice = 0
        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        self.limpiar_ventana()
        if self.indice >= len(self.ejercicios):
            self.mostrar_resultado()
            return

        pregunta, respuesta_correcta = self.ejercicios[self.indice]

        tk.Label(self.root, text=f"Ejercicio {self.indice + 1} de {self.total}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.root, text=pregunta, wraplength=500, font=("Arial", 14)).pack(pady=10)

        self.respuesta_usuario = tk.Entry(self.root, font=("Arial", 12), width=50)
        self.respuesta_usuario.pack(pady=5)

        tk.Button(self.root, text="Responder", command=lambda: self.verificar_respuesta(respuesta_correcta)).pack(pady=10)

        if self.modo == "practica":
            tk.Button(self.root, text="Ver regla", command=lambda: self.mostrar_regla(respuesta_correcta)).pack(pady=5)

    def verificar_respuesta(self, correcta):
        r = self.respuesta_usuario.get().strip().lower()
        if r == correcta.strip().lower():
            self.puntaje += 1
            messagebox.showinfo("Correcto", "¡Muy bien!")
        else:
            messagebox.showwarning("Incorrecto", f"La respuesta correcta era: {correcta}")
        self.indice += 1
        self.mostrar_ejercicio()

    def mostrar_regla(self, regla):
        messagebox.showinfo("Regla", f"Regla: {regla}")

    def mostrar_resultado(self):
        self.limpiar_ventana()
        resultado = f"Puntaje final: {self.puntaje}/{self.total}"
        tk.Label(self.root, text=resultado, font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Volver al inicio", command=self.crear_interfaz_inicio).pack(pady=10)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ===================
# EJECUCIÓN
# ===================
if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramaOrtografia(root)
    root.mainloop()
