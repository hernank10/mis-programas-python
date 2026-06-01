import tkinter as tk
from tkinter import messagebox

# 🧠 Datos base
ejercicios = [
    {"contra": "Hay quienes piensan que la lectura ya no es necesaria en la era digital.",
     "modelo": "Sin embargo, leer desarrolla pensamiento crítico, algo que las redes no siempre promueven."},
    {"contra": "Algunos afirman que el uniforme escolar limita la libertad individual.",
     "modelo": "Aunque limita la vestimenta, fomenta la igualdad visual y reduce presión social."},
    {"contra": "Se cree que las matemáticas solo sirven para ciertas profesiones.",
     "modelo": "No obstante, enseñan lógica, resolución de problemas y toma de decisiones cotidianas."},
    {"contra": "Muchos dicen que la historia no tiene utilidad práctica.",
     "modelo": "Aunque no se aplique literalmente, ayuda a comprender conflictos y evitar errores del pasado."},
    {"contra": "Algunas personas opinan que la educación física debería ser opcional.",
     "modelo": "Sin embargo, fortalece la salud, reduce el estrés y mejora la disciplina personal."},
    {"contra": "Muchos argumentan que aprender otro idioma es innecesario si no se viaja.",
     "modelo": "No obstante, conocer otro idioma abre puertas mentales, culturales y profesionales."},
    {"contra": "Se dice que la música es una pérdida de tiempo escolar.",
     "modelo": "Aunque no todos la estudien profesionalmente, potencia la memoria y la expresión."},
    {"contra": "Algunos creen que los trabajos en grupo no funcionan bien.",
     "modelo": "Sin embargo, son clave para desarrollar habilidades colaborativas y responsabilidad compartida."},
    {"contra": "Muchos piensan que memorizar fechas es inútil en historia.",
     "modelo": "No obstante, las fechas estructuran hechos, permiten relaciones cronológicas y análisis profundo."},
    {"contra": "Hay quien opina que el arte urbano no debería estar en espacios públicos.",
     "modelo": "Aunque puede ser controversial, refleja realidades sociales y estimula el pensamiento crítico."},
    {"contra": "Se afirma que el acceso libre a internet hace innecesarios los libros.",
     "modelo": "Sin embargo, los libros ofrecen profundidad, contexto y criterio que no siempre da internet."},
    {"contra": "Algunos piensan que los deportes solo sirven para entretener.",
     "modelo": "No obstante, enseñan esfuerzo, estrategia, disciplina y compañerismo."},
    {"contra": "Hay quienes opinan que la filosofía no tiene aplicación real.",
     "modelo": "Aunque no dé respuestas simples, enseña a preguntar, analizar y argumentar de forma sólida."},
    {"contra": "Se cree que los adolescentes no pueden participar en debates complejos.",
     "modelo": "Sin embargo, con guía pueden construir opiniones propias, respetar ideas y profundizar en temas."},
    {"contra": "Muchos dicen que las reglas escolares son demasiado estrictas.",
     "modelo": "Aunque puedan parecer rígidas, garantizan orden, respeto y seguridad para todos."},
    {"contra": "Algunos sostienen que leer poesía es una actividad anticuada.",
     "modelo": "No obstante, la poesía estimula sensibilidad, lenguaje figurado y reflexión estética."},
    {"contra": "Se dice que el diseño gráfico no es una materia seria.",
     "modelo": "Aunque sea visual, involucra comunicación efectiva, análisis cultural y pensamiento estratégico."},
    {"contra": "Hay quien piensa que escribir a mano ya no tiene valor.",
     "modelo": "Sin embargo, fortalece la memoria, la motricidad y el estilo personal de comunicación."},
    {"contra": "Algunos afirman que la ortografía no importa si se entiende el mensaje.",
     "modelo": "No obstante, escribir correctamente muestra respeto, claridad y mejora la credibilidad."},
    {"contra": "Se cree que los proyectos creativos no ayudan a mejorar el aprendizaje.",
     "modelo": "Aunque parezcan informales, fomentan autonomía, exploración y conexión entre saberes."}
]

# 🎯 Evaluación básica
def evaluar(texto):
    texto = texto.strip().lower()
    puntos = 0
    if any(c in texto for c in ["sin embargo", "aunque", "no obstante"]):
        puntos += 1
    if len(texto.split()) >= 8:
        puntos += 1
    if "." in texto or "," in texto:
        puntos += 1
    return puntos

# 🖼️ Interfaz principal
class RefutacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sintaxis Quest EDU – Lección 7 – Refutación lógica")
        self.index = 0
        self.total = 0

        self.contra_label = tk.Label(root, text="", wraplength=700, font=("Arial", 12, "bold"))
        self.contra_label.pack(pady=10)

        self.modelo_label = tk.Label(root, text="", wraplength=700, fg="gray")
        self.modelo_label.pack(pady=5)

        self.texto = tk.Text(root, height=4, width=80)
        self.texto.pack(pady=10)

        self.evaluar_btn = tk.Button(root, text="🧠 Evaluar respuesta", command=self.evaluar_actual)
        self.evaluar_btn.pack(pady=5)

        self.resultado = tk.Label(root, text="", wraplength=700, font=("Arial", 11))
        self.resultado.pack(pady=10)

        self.siguiente_btn = tk.Button(root, text="➡️ Siguiente", command=self.siguiente)
        self.siguiente_btn.pack(pady=5)

        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        if self.index < len(ejercicios):
            ej = ejercicios[self.index]
            self.contra_label.config(text=f"🗣️ {ej['contra']}")
            self.modelo_label.config(text=f"💡 Ejemplo: {ej['modelo']}")
            self.texto.delete("1.0", tk.END)
            self.resultado.config(text="")
        else:
            self.contra_label.config(text="✅ ¡Has terminado los 20 ejercicios!")
            self.modelo_label.config(text=f"🌟 Puntaje final: {self.total}/60")
            self.texto.destroy()
            self.evaluar_btn.config(state="disabled")
            self.siguiente_btn.config(text="Salir", command=self.root.quit)

    def evaluar_actual(self):
        respuesta = self.texto.get("1.0", tk.END)
        puntos = evaluar(respuesta)
        self.total += puntos
        if puntos == 3:
            fb = "🏅 Refutación sólida y bien estructurada."
        elif puntos == 2:
            fb = "✅ Buena respuesta, puedes mejorar con más detalle."
        elif puntos == 1:
            fb = "⚠️ Refutación débil. Usa conectores y más desarrollo."
        else:
            fb = "❌ No se detectó lógica o estructura suficiente."
        self.resultado.config(text=f"{fb}\nPuntaje: {puntos}/3")

    def siguiente(self):
        self.index += 1
        self.mostrar_ejercicio()

# 🚀 Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = RefutacionApp(root)
    root.mainloop()
