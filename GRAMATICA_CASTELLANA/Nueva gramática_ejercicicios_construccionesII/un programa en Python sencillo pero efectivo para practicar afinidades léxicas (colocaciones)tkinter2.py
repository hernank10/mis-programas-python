import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time
import csv
import os

vidas_iniciales = 3
tiempo_limite = 15

elementos = {
    "fácil": [
        {"frase": "Voy a ___ una vuelta por el parque.", "opciones": ["hacer", "dar", "crear", "formar"], "respuesta": "dar"},
        {"frase": "___ el desaliento en el ambiente escolar.", "opciones": ["Cunde", "Aparece", "Surge", "Emana"], "respuesta": "Cunde"},
        {"frase": "Van a ___ matrimonio pronto.", "opciones": ["formar", "crear", "contraer", "tener"], "respuesta": "contraer"}
    ],
    "intermedio": [
        {"frase": "Es importante ___ la virtud desde jóvenes.", "opciones": ["ejercer", "ejercitar", "imponer", "activar"], "respuesta": "ejercitar"},
        {"frase": "Este resultado es inverso ___ el anterior.", "opciones": ["a", "de", "con", "por"], "respuesta": "de"},
        {"frase": "Este argumento es contrario ___ tus ideas.", "opciones": ["con", "de", "a", "en"], "respuesta": "a"}
    ],
    "difícil": [
        {"frase": "Debemos ___ la actividad empresarial.", "opciones": ["crear", "activar", "desarrollar", "inventar"], "respuesta": "desarrollar"},
        {"frase": "___ influencia en el comportamiento del grupo.", "opciones": ["Ejercita", "Ejerce", "Aplica", "Expone"], "respuesta": "Ejerce"},
        {"frase": "Voy a ___ la consulta como abogado.", "opciones": ["atender", "consultar", "evacuar", "resolver"], "respuesta": "evacuar"}
    ]
}

estadisticas = []
ejemplos_usuario = []

class JuegoColocaciones:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Colocaciones")
        self.vidas = vidas_iniciales
        self.puntaje = 0
        self.pregunta_actual = {}
        self.nivel = "fácil"

        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Juego de Colocaciones", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Ver teoría", command=self.mostrar_teoria).pack(pady=5)
        tk.Button(self.root, text="Practicar", command=self.elegir_nivel).pack(pady=5)
        tk.Button(self.root, text="Crear ejemplos", command=self.crear_ejemplos).pack(pady=5)
        tk.Button(self.root, text="Ver estadísticas", command=self.exportar_estadisticas).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def mostrar_teoria(self):
        teoria = [
            "Las colocaciones léxicas son combinaciones fijas entre verbos y sustantivos.",
            "No se pueden deducir por lógica: se aprenden por uso y contexto.",
            "Ejemplos correctos: 'dar una vuelta', 'cunde el desaliento', 'contraer matrimonio'.",
            "Ejemplos incorrectos: 'hacer una vuelta', 'surge el desaliento', 'crear matrimonio'.",
            "Algunas colocaciones cambian según preposición: 'inverso de', 'contrario a'.",
            "Usar bien las colocaciones mejora tu fluidez y naturalidad al hablar."
        ]
        for mensaje in teoria:
            messagebox.showinfo("Teoría", mensaje)

    def elegir_nivel(self):
        nivel = simpledialog.askstring("Nivel", "Elige nivel: fácil, intermedio o difícil")
        if nivel in elementos:
            self.nivel = nivel
            self.vidas = vidas_iniciales
            self.puntaje = 0
            self.preguntas = random.sample(elementos[nivel], len(elementos[nivel]))
            self.siguiente_pregunta()
        else:
            messagebox.showwarning("Nivel", "Nivel no válido")

    def siguiente_pregunta(self):
        if not self.preguntas or self.vidas <= 0:
            messagebox.showinfo("Fin del juego", f"Puntaje: {self.puntaje}")
            self.guardar_estadisticas()
            self.main_menu()
            return

        self.pregunta_actual = self.preguntas.pop(0)
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Vidas: {'❤️' * self.vidas} | Puntaje: {self.puntaje}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.root, text=self.pregunta_actual["frase"], font=("Arial", 14)).pack(pady=10)

        self.tiempo_restante = tiempo_limite
        self.temporizador_label = tk.Label(self.root, text=f"Tiempo: {self.tiempo_restante}s")
        self.temporizador_label.pack(pady=5)
        self.actualizar_temporizador()

        for opcion in self.pregunta_actual["opciones"]:
            tk.Button(self.root, text=opcion, command=lambda o=opcion: self.verificar_respuesta(o)).pack(pady=2)

    def actualizar_temporizador(self):
        self.tiempo_restante -= 1
        self.temporizador_label.config(text=f"Tiempo: {self.tiempo_restante}s")
        if self.tiempo_restante <= 0:
            self.vidas -= 1
            estadisticas.append([self.pregunta_actual['frase'], '', self.pregunta_actual['respuesta'], 'Tiempo agotado'])
            messagebox.showinfo("Tiempo agotado", f"Respuesta correcta: {self.pregunta_actual['respuesta']}")
            self.siguiente_pregunta()
        else:
            self.root.after(1000, self.actualizar_temporizador)

    def verificar_respuesta(self, opcion):
        correcta = self.pregunta_actual["respuesta"]
        if opcion == correcta:
            self.puntaje += 1
            estadisticas.append([self.pregunta_actual['frase'], opcion, correcta, 'Correcta'])
            messagebox.showinfo("Correcto", "✔️ Bien hecho!")
        else:
            self.vidas -= 1
            estadisticas.append([self.pregunta_actual['frase'], opcion, correcta, 'Incorrecta'])
            messagebox.showerror("Incorrecto", f"La respuesta era: {correcta}")
        self.siguiente_pregunta()

    def crear_ejemplos(self):
        while True:
            ejemplo = simpledialog.askstring("Ejemplo", "Escribe tu ejemplo (o 'fin' para terminar):")
            if ejemplo is None or ejemplo.lower() == "fin":
                break
            ejemplos_usuario.append(ejemplo)
        with open("ejemplos_usuario.txt", "w", encoding="utf-8") as f:
            for ej in ejemplos_usuario:
                f.write(ej + "\n")
        messagebox.showinfo("Guardado", "Ejemplos guardados en ejemplos_usuario.txt")

    def guardar_estadisticas(self):
        archivo = "estadisticas_colocaciones.csv"
        with open(archivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(["Frase", "Respuesta dada", "Respuesta correcta", "Resultado"])
            escritor.writerows(estadisticas)

    def exportar_estadisticas(self):
        self.guardar_estadisticas()
        messagebox.showinfo("Estadísticas", "Se han exportado las estadísticas en 'estadisticas_colocaciones.csv'")

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoColocaciones(root)
    root.mainloop()
