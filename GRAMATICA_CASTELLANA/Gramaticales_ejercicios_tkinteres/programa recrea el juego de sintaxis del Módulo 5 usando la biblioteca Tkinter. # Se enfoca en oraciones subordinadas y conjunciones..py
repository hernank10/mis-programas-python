# Este programa recrea el juego de sintaxis del Módulo 5 usando la biblioteca Tkinter.
# Se enfoca en oraciones subordinadas y conjunciones.
# Incluye un sistema de dificultad progresiva y un banco de preguntas ampliado.
# La interfaz está diseñada con los widgets estándar de Tkinter.

import tkinter as tk
from tkinter import font
import random

# --- Contenido de la lección (oraciones subordinadas y conjunciones) ---
# Cada tupla contiene:
# (oración_original, oración_transformada, tipo_transformación, idioma, dificultad)
lecciones_oraciones_mod5 = [
    # Dificultad 1: Subordinadas simples (sustantivas, adjetivas)
    ("The boy who is wearing a hat is my brother.", "El chico que lleva un sombrero es mi hermano.", "adjetiva", "inglés", 1),
    ("Es importante que estudies.", "That you study is important.", "sustantiva", "español", 1),
    ("I believe that she is right.", "Creo que ella tiene razón.", "sustantiva", "inglés", 1),
    ("The house where I was born is for sale.", "La casa donde nací está en venta.", "adjetiva", "español", 1),
    ("I know who stole the cookies.", "Sé quién robó las galletas.", "sustantiva", "inglés", 1),
    ("No sé si va a llover mañana.", "I don't know if it will rain tomorrow.", "sustantiva", "español", 1),

    # Dificultad 2: Subordinadas adverbiales (causa, temporal, consecutiva)
    ("Because it's raining, we can't go to the park.", "Como está lloviendo, no podemos ir al parque.", "causal", "inglés", 2),
    ("He was so tired that he fell asleep.", "Estaba tan cansado que se quedó dormido.", "consecutiva", "inglés", 2),
    ("Cuando llegué a casa, mi hermana ya se había ido.", "When I arrived home, my sister had already left.", "temporal", "español", 2),
    ("He works as if he were a machine.", "Trabaja como si fuera una máquina.", "comparativa", "inglés", 2),
    ("Debido a que tengo un examen, no puedo salir.", "Because I have an exam, I can't go out.", "causal", "español", 2),
    ("Tan pronto como vi el mensaje, te llamé.", "As soon as I saw the message, I called you.", "temporal", "español", 2),

    # Dificultad 3: Condicionales, concesivas y finales complejas
    ("Although she was sick, she went to school.", "A pesar de que estaba enferma, fue a la escuela.", "concesiva", "inglés", 3),
    ("Para que apruebes el curso, tienes que estudiar más.", "In order for you to pass the course, you have to study more.", "final", "español", 3),
    ("I will help you, provided that you ask nicely.", "Te ayudaré, siempre y cuando pidas bien.", "condicional", "inglés", 3),
    ("Though it was cold, we went swimming.", "Aunque hacía frío, fuimos a nadar.", "concesiva", "inglés", 3),
    ("Por mucho que insistas, no cambiaré de opinión.", "However much you insist, I won't change my mind.", "concesiva", "español", 3),
    ("Para que lo entiendas, te lo explicaré de nuevo.", "So that you understand it, I will explain it again.", "final", "español", 3),
]

class JuegoSintaxisApp:
    def __init__(self, master):
        self.master = master
        master.title("Juego de Sintaxis - Módulo 5")
        master.geometry("1000x700")
        master.configure(bg="#0A0A1F") # Fondo oscuro para simular el espacio

        # Estilos de fuente
        self.fuente_titulo = font.Font(family="Helvetica", size=40, weight="bold")
        self.fuente_normal = font.Font(family="Helvetica", size=20)
        self.fuente_pregunta = font.Font(family="Helvetica", size=18)

        # Variables de estado del juego
        self.estado_juego = "menu"
        self.puntaje = 0
        self.preguntas_jugadas = []
        self.pregunta_actual = None
        self.preguntas_correctas_nivel = 0
        self.correctas_para_subir = 3
        self.dificultad_actual = 1

        # Contenedor principal para los widgets
        self.main_frame = tk.Frame(master, bg="#0A0A1F")
        self.main_frame.pack(expand=True, fill="both")

        self.show_menu()

    def clear_screen(self):
        """Elimina todos los widgets de la pantalla principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_menu(self):
        """Muestra la pantalla del menú de inicio."""
        self.clear_screen()
        
        titulo = tk.Label(self.main_frame, text="Módulo 5: Subordinadas y Conjunciones",
                          font=self.fuente_titulo, fg="white", bg="#0A0A1F")
        titulo.place(relx=0.5, rely=0.35, anchor="center")

        btn_iniciar = tk.Button(self.main_frame, text="🚀 ¡Empezar!",
                                font=self.fuente_normal, bg="#5C6BC0", fg="white",
                                relief="flat", padx=20, pady=10,
                                command=self.iniciar_juego)
        btn_iniciar.place(relx=0.5, rely=0.55, anchor="center")

    def iniciar_juego(self):
        """Inicializa las variables y comienza el juego."""
        self.estado_juego = "jugando"
        self.puntaje = 0
        self.preguntas_jugadas.clear()
        self.dificultad_actual = 1
        self.preguntas_correctas_nivel = 0
        self.obtener_nueva_pregunta()
        self.show_game_screen()

    def show_game_screen(self):
        """Muestra la interfaz principal del juego."""
        self.clear_screen()

        # Marco superior para la información del juego
        info_frame = tk.Frame(self.main_frame, bg="#0A0A1F")
        info_frame.pack(fill="x", pady=10)

        self.puntaje_label = tk.Label(info_frame, text=f"Puntaje: {self.puntaje}",
                                      font=self.fuente_normal, fg="white", bg="#0A0A1F")
        self.puntaje_label.pack(side="left", padx=20)

        self.dificultad_label = tk.Label(info_frame, text=f"Dificultad: {self.dificultad_actual}",
                                        font=self.fuente_normal, fg="white", bg="#0A0A1F")
        self.dificultad_label.pack(side="right", padx=20)

        # Labels de la pregunta
        self.tipo_label = tk.Label(self.main_frame, text="", font=self.fuente_normal,
                                   fg="white", bg="#0A0A1F", wraplength=800)
        self.tipo_label.place(relx=0.5, rely=0.3, anchor="center")

        self.pregunta_label = tk.Label(self.main_frame, text="", font=self.fuente_pregunta,
                                       fg="white", bg="#0A0A1F", wraplength=800)
        self.pregunta_label.place(relx=0.5, rely=0.4, anchor="center")

        self.feedback_label = tk.Label(self.main_frame, text="", font=self.fuente_normal,
                                       fg="yellow", bg="#0A0A1F")
        self.feedback_label.place(relx=0.5, rely=0.6, anchor="center")

        # Entrada del usuario
        self.respuesta_entry = tk.Entry(self.main_frame, width=50, font=self.fuente_pregunta,
                                      bd=0, highlightthickness=2, highlightcolor="#5C6BC0",
                                      bg="#2C2C40", fg="white", insertbackground="white")
        self.respuesta_entry.bind("<Return>", self.verificar_respuesta)
        self.respuesta_entry.place(relx=0.5, rely=0.75, anchor="center")
        self.respuesta_entry.focus()
        
        # Actualiza el contenido de los labels
        self.update_question_display()

    def obtener_nueva_pregunta(self):
        """Selecciona una nueva oración y la carga en la interfaz."""
        preguntas_disponibles = [p for p in lecciones_oraciones_mod5 if p[4] == self.dificultad_actual and p not in self.preguntas_jugadas]
        
        if preguntas_disponibles:
            self.pregunta_actual = random.choice(preguntas_disponibles)
            self.preguntas_jugadas.append(self.pregunta_actual)
            self.update_question_display()
        else:
            if self.dificultad_actual < 3:
                self.subir_nivel_dificultad()
                self.obtener_nueva_pregunta()
            else:
                self.ir_a_resultados()

    def update_question_display(self):
        """Actualiza los labels de la pregunta en la pantalla del juego."""
        if self.pregunta_actual:
            self.tipo_label.config(text=f"Transforma a: {self.pregunta_actual[2].capitalize()} {'🇪🇸' if self.pregunta_actual[3] == 'español' else '🇬🇧'}")
            self.pregunta_label.config(text=self.pregunta_actual[0])
            self.respuesta_entry.delete(0, tk.END)

    def verificar_respuesta(self, event=None):
        """Verifica la respuesta del usuario y actualiza el estado del juego."""
        respuesta_correcta = self.pregunta_actual[1]
        respuesta_usuario = self.respuesta_entry.get().strip()
        
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            self.feedback_label.config(text=f"¡Correcto! Es una oración {self.pregunta_actual[2]} ✅✨", fg="#4CAF50")
            self.puntaje += 1
            self.preguntas_correctas_nivel += 1
            
            if self.preguntas_correctas_nivel >= self.correctas_para_subir and self.dificultad_actual < 3:
                self.subir_nivel_dificultad()
        else:
            self.feedback_label.config(text=f"Incorrecto. La respuesta es '{respuesta_correcta}'. ❌💔", fg="#F44336")
        
        self.puntaje_label.config(text=f"Puntaje: {self.puntaje}")
        self.master.after(2000, self.obtener_nueva_pregunta)

    def subir_nivel_dificultad(self):
        """Incrementa la dificultad del juego."""
        self.dificultad_actual += 1
        self.preguntas_correctas_nivel = 0
        self.feedback_label.config(text=f"¡Subiste a Dificultad {self.dificultad_actual}! 🎉", fg="#2196F3")
        self.dificultad_label.config(text=f"Dificultad: {self.dificultad_actual}")
        
    def ir_a_resultados(self):
        """Muestra la pantalla de resultados finales."""
        self.clear_screen()
        
        titulo_final = tk.Label(self.main_frame, text="Resultados", font=self.fuente_titulo,
                                fg="white", bg="#0A0A1F")
        titulo_final.place(relx=0.5, rely=0.35, anchor="center")
        
        puntaje_final = tk.Label(self.main_frame, text=f"Puntaje final: {self.puntaje} de {len(self.preguntas_jugadas)}",
                                 font=self.fuente_normal, fg="white", bg="#0A0A1F")
        puntaje_final.place(relx=0.5, rely=0.5, anchor="center")
        
        btn_reintentar = tk.Button(self.main_frame, text="🎮 Jugar de Nuevo",
                                   font=self.fuente_normal, bg="#5C6BC0", fg="white",
                                   relief="flat", padx=20, pady=10,
                                   command=self.iniciar_juego)
        btn_reintentar.place(relx=0.5, rely=0.7, anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoSintaxisApp(root)
    root.mainloop()
