import tkinter as tk
from tkinter import messagebox

# 🧠 Base de ejercicios
ejercicios = [
    {"tesis": "La filosofía debería ser obligatoria en bachillerato",
     "modelo": "Porque enseña a pensar con profundidad, cuestionar y argumentar con claridad."},
    {"tesis": "Las TIC deben utilizarse con fines pedagógicos en clase",
     "modelo": "Ya que promueven aprendizaje interactivo, accesible y actual."},
    {"tesis": "La educación artística es tan importante como la científica",
     "modelo": "Porque ambas desarrollan creatividad, pensamiento crítico y sensibilidad."},
    {"tesis": "La lectura crítica debe practicarse en todas las asignaturas",
     "modelo": "Ya que ayuda a interpretar, analizar y construir conocimientos sólidos."},
    {"tesis": "La educación ambiental debe incluirse en cada nivel escolar",
     "modelo": "Porque forma conciencia ecológica y responsabilidad global."},
    {"tesis": "La historia local debería tener más espacio en el currículo",
     "modelo": "Porque permite reconocer raíces, valorar identidades y comprender el presente."},
    {"tesis": "Los proyectos interdisciplinarios enriquecen el aprendizaje",
     "modelo": "Debido a que conectan saberes, promueven colaboración y creatividad."},
    {"tesis": "La expresión oral debe ser parte del proceso evaluativo",
     "modelo": "Ya que fortalece comunicación, autoconfianza y pensamiento estructurado."},
    {"tesis": "El análisis de noticias debe integrarse al área de lenguaje",
     "modelo": "Porque estimula la comprensión crítica y el diálogo argumentativo."},
    {"tesis": "Los estudiantes deben tener espacios de participación democrática",
     "modelo": "Porque así ejercen sus derechos, construyen ciudadanía y aprenden a dialogar."},
    {"tesis": "La evaluación formativa es más útil que la sumativa",
     "modelo": "Ya que permite acompañar el proceso y fomentar la mejora continua."},
    {"tesis": "Las salidas pedagógicas fortalecen los contenidos teóricos",
     "modelo": "Porque vinculan el conocimiento con el entorno real y cultural."},
    {"tesis": "El trabajo colaborativo desarrolla habilidades blandas",
     "modelo": "Como liderazgo, empatía, negociación y planificación compartida."},
    {"tesis": "La creatividad debe ser valorada como competencia académica",
     "modelo": "Porque permite innovar, resolver problemas y expresarse con originalidad."},
    {"tesis": "El pensamiento científico ayuda a resolver problemas reales",
     "modelo": "Ya que se basa en observación, hipótesis, experimentación y análisis."},
    {"tesis": "El arte permite comprender emociones y contextos sociales",
     "modelo": "Porque es lenguaje, testimonio y exploración del mundo humano."},
    {"tesis": "La argumentación previene los discursos de odio",
     "modelo": "Porque exige pensar, justificar y respetar otras voces."},
    {"tesis": "Las ciencias naturales deben conectarse con la vida cotidiana",
     "modelo": "Para que sean significativas, útiles y contextualizadas."},
    {"tesis": "La educación financiera debería enseñarse desde secundaria",
     "modelo": "Ya que forma conciencia sobre ahorro, gasto, inversión y planificación."},
    {"tesis": "Los textos literarios permiten construir identidad cultural",
     "modelo": "Porque reflejan valores, lenguajes, conflictos y sueños colectivos."}
]

# 🎯 Evaluador automático
def evaluar_respuesta(respuesta):
    respuesta = respuesta.strip().lower()
    puntos = 0
    conectores = ["porque", "ya que", "debido a que", "por ejemplo", "además", "esto demuestra que"]
    if any(c in respuesta for c in conectores):
        puntos += 1
    if len(respuesta.split()) >= 8:
        puntos += 1
    if "." in respuesta or "," in respuesta:
        puntos += 1
    return puntos

# 🖼️ Interfaz principal
class TesisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sintaxis Quest EDU – Lección 7 – Desarrollo de tesis (11.º Grado)")
        self.index = 0
        self.total = 0

        self.label_tesis = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=700)
        self.label_tesis.pack(pady=10)

        self.label_modelo = tk.Label(root, text="", font=("Arial", 10), fg="gray", wraplength=700)
        self.label_modelo.pack(pady=5)

        self.input_text = tk.Text(root, height=4, width=80)
        self.input_text.pack(pady=10)

        self.btn_evaluar = tk.Button(root, text="🧠 Evaluar respuesta", command=self.evaluar_actual)
        self.btn_evaluar.pack(pady=5)

        self.label_resultado = tk.Label(root, text="", font=("Arial", 11), wraplength=700)
        self.label_resultado.pack(pady=10)

        self.btn_siguiente = tk.Button(root, text="➡️ Siguiente", command=self.siguiente)
        self.btn_siguiente.pack(pady=5)

        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        if self.index < len(ejercicios):
            ej = ejercicios[self.index]
            self.label_tesis.config(text=f"Tesis {self.index + 1}: {ej['tesis']}")
            self.label_modelo.config(text=f"💡 Ejemplo: {ej['modelo']}")
            self.input_text.delete("1.0", tk.END)
            self.label_resultado.config(text="")
        else:
            self.label_tesis.config(text="🎉 ¡Has completado todos los ejercicios!")
            self.label_modelo.config(text=f"🌟 Puntaje final: {self.total}/60")
            self.input_text.destroy()
            self.btn_evaluar.config(state="disabled")
            self.btn_siguiente.config(text="Salir", command=self.root.quit)

    def evaluar_actual(self):
        razon = self.input_text.get("1.0", tk.END)
        puntos = evaluar_respuesta(razon)
        self.total += puntos
        if puntos == 3:
            fb = "🏅 Justificación profunda y bien redactada."
        elif puntos == 2:
            fb = "✅ Argumento correcto. Puedes ampliar más."
        elif puntos == 1:
            fb = "⚠️ Breve o débil. Intenta desarrollar mejor la idea."
        else:
            fb = "❌ No se detectó argumento con lógica suficiente."
        self.label_resultado.config(text=f"{fb}\nPuntaje: {puntos}/3")

    def siguiente(self):
        self.index += 1
        self.mostrar_ejercicio()

# 🚀 Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = TesisApp(root)
    root.mainloop()
