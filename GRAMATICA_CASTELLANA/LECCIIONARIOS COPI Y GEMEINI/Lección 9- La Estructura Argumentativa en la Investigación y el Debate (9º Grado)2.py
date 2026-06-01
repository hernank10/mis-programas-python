import tkinter as tk
from tkinter import scrolledtext, messagebox
import random

class Leccion9App:
    def __init__(self, master):
        self.master = master
        master.title("Lección 9: La Estructura Argumentativa en la Investigación y el Debate (9º Grado)")
        master.geometry("900x700") # Tamaño de ventana inicial

        self.frames = {}
        self._create_main_menu_frame()
        self._create_introduction_frame()
        self._create_credibility_concept_frame()
        # Puedes añadir más métodos para crear frames para el resto de conceptos y juegos

        self.show_frame("main_menu")

    def _create_main_menu_frame(self):
        """Crea el frame del menú principal."""
        frame = tk.Frame(self.master, padx=20, pady=20, bg="#F0F8FF")
        self.frames["main_menu"] = frame

        tk.Label(frame, text="Lección 9: Maestros de la Investigación y el Debate (9º Grado)", font=("Arial", 20, "bold"), fg="#2F4F4F", bg="#F0F8FF").pack(pady=20)

        options = [
            ("Introducción: ¡Maestros de la Investigación y el Debate!", "introduction"),
            ("Evaluación de Credibilidad: ¿El Orden Dice la Verdad?", "credibility_concept"),
            ("Jugar: ¡El Detective de la Credibilidad!", self.start_game_credibility_analysis), # Llama a un método para el juego
            ("Organización para la Síntesis: ¡Tejiendo Hilos de Información!", None), # Placeholder para otros conceptos
            ("Argumentos Contrarrestantes y Refutaciones: ¡Fortaleciendo tu Voz!", None), # Placeholder
            ("NUEVO: Ejercicio: ¡Organización y Credibilidad en la Noticia!", self.start_exercise_analyze_organization_for_credibility), # Llama al nuevo ejercicio
            ("NUEVO: Ejercicio: ¡Construye un Argumento Sintetizando Fuentes!", None), # Placeholder
            ("NUEVO: Ejercicio: ¡Construye tu Refutación!", None), # Placeholder
            ("Salir de la Lección", self.master.quit)
        ]

        for text, command in options:
            if isinstance(command, str): # Si es un nombre de frame
                btn = tk.Button(frame, text=text, font=("Arial", 14), bg="#ADD8E6", fg="black", padx=10, pady=5,
                                command=lambda f=command: self.show_frame(f))
            else: # Si es una función (para juegos o salir)
                 btn = tk.Button(frame, text=text, font=("Arial", 14), bg="#ADD8E6", fg="black", padx=10, pady=5,
                                command=command)
            btn.pack(pady=7, fill="x")

    def _create_introduction_frame(self):
        """Crea el frame para la introducción."""
        frame = tk.Frame(self.master, padx=20, pady=20, bg="#F0F8FF")
        self.frames["introduction"] = frame

        tk.Label(frame, text="Introducción: ¡Maestros de la Investigación y el Debate!", font=("Arial", 18, "bold"), fg="#2F4F4F", bg="#F0F8FF").pack(pady=10)
        intro_text = """¡Bienvenidos, jóvenes pensadores críticos! 🚀
Ya son expertos en organizar ideas y entender cómo la estructura afecta un mensaje.
En 9.º Grado, llevaremos esto al siguiente nivel: ¡serán verdaderos detectives de la información y arquitectos de argumentos sólidos!

En esta lección, ustedes aprenderán a:
   ✅ Evaluar la credibilidad de fuentes analizando cómo organizan su información.
   ✅ Sintetizar y organizar ideas de MÚLTIPLES fuentes en argumentos complejos.
   ✅ Construir refutaciones efectivas, anticipando y contrarrestando objeciones.

¡Prepárense para investigar, analizar y debatir como expertos!"""
        tk.Label(frame, text=intro_text, font=("Arial", 12), justify="left", wraplength=800, bg="#F0F8FF").pack(pady=10)

        tk.Button(frame, text="Volver al Menú Principal", font=("Arial", 12), bg="#B0E0E6", command=lambda: self.show_frame("main_menu")).pack(pady=20)

    def _create_credibility_concept_frame(self):
        """Crea el frame para el concepto de evaluación de credibilidad."""
        frame = tk.Frame(self.master, padx=20, pady=20, bg="#F0F8FF")
        self.frames["credibility_concept"] = frame

        tk.Label(frame, text="Evaluación de Credibilidad: ¿El Orden Dice la Verdad?", font=("Arial", 18, "bold"), fg="#2F4F4F", bg="#F0F8FF").pack(pady=10)
        concept_text = """La forma en que se organiza la información puede ser una pista sobre la **credibilidad** de una fuente y si hay **sesgos**.

--- Preguntas Clave al Analizar la Organización de una Fuente: ---
  1. **¿Qué se presenta primero? ¿Qué se deja para el final?**
     * Sesgo: Si un autor presenta primero solo los datos que apoyan su punto y deja las objeciones (o las minimiza) al final, puede estar tratando de influenciarte.
     * Credibilidad: Una fuente equilibrada puede presentar primero el contexto del problema, luego las diferentes perspectivas y finalmente su conclusión, o incluso admitir limitaciones al inicio.

  2. **¿Se omite información clave o se le resta importancia por su posición?**
     * Sesgo: Ignorar contra-argumentos o colocarlos en un lugar secundario (ej. una nota al pie de página) es una señal de que la organización busca favorecer una postura.
     * Credibilidad: Presentar objeciones y luego refutarlas de forma lógica demuestra un argumento más robusto y honesto.

  3. **¿Cómo se organiza la evidencia? ¿Hay un flujo lógico o es una 'lista' de hechos aislados?**
     * Credibilidad: La evidencia bien organizada, que fluye lógicamente para apoyar una tesis, es más persuasiva y creíble que una mera acumulación de datos.

  4. **¿Los datos presentados al principio son conclusiones o puntos de partida para el análisis?**
     * Credibilidad: Un texto que presenta datos como punto de partida para una discusión (inductivo) puede parecer más abierto que uno que comienza con conclusiones fuertes y luego busca apoyar (deductivo) sin considerar otras opciones.

¡Ser un lector crítico significa ver más allá de las palabras: hay que ver cómo están presentadas!"""
        tk.Label(frame, text=concept_text, font=("Arial", 12), justify="left", wraplength=800, bg="#F0F8FF").pack(pady=10)

        tk.Button(frame, text="Volver al Menú Principal", font=("Arial", 12), bg="#B0E0E6", command=lambda: self.show_frame("main_menu")).pack(pady=20)
        
    def show_frame(self, frame_name):
        """Muestra el frame especificado y oculta los demás."""
        for name, frame in self.frames.items():
            if name == frame_name:
                frame.pack(fill="both", expand=True)
            else:
                frame.pack_forget()

    # --- Métodos para los Juegos y Ejercicios (se inician en nuevas ventanas o frames) ---

    def start_game_credibility_analysis(self):
        """Inicia el juego 'El Detective de la Credibilidad'."""
        self.credibility_game_window = tk.Toplevel(self.master)
        self.credibility_game_window.title("Juego: ¡El Detective de la Credibilidad!")
        self.credibility_game_window.geometry("800x600")
        self.credibility_game_window.transient(self.master) # Hace que la ventana de juego dependa de la principal

        self.credibility_game_frame = tk.Frame(self.credibility_game_window, padx=20, pady=20, bg="#F8F8FF")
        self.credibility_game_frame.pack(fill="both", expand=True)

        self.credibility_scenarios = [
            {"text": "El plan X es la única solución viable para la economía. Mis oponentes presentan argumentos débiles, que ignoro por el momento. Lo importante es que, al implementar el plan X, veremos un crecimiento sin precedentes en solo seis meses.",
             "analysis_points": "El autor posiciona su plan como 'la única solución viable' al inicio, descartando 'débiles' argumentos contrarios sin presentarlos. Esto indica un posible sesgo y falta de equilibrio. La evidencia (crecimiento) se presenta como una promesa sin detalles organizativos sobre cómo se logrará, lo que podría reducir la credibilidad."},
            {"text": "Recientes estudios sugieren una correlación entre el uso prolongado de pantallas y ciertos patrones de sueño alterados en adolescentes. Si bien algunos podrían argumentar que los factores sociales influyen más, la evidencia neurobiológica indica que la exposición a la luz azul antes de dormir es un factor significativo que interrumpe la producción de melatonina.",
             "analysis_points": "El autor presenta una correlación con evidencia ('estudios recientes') y luego aborda una posible objeción ('algunos podrían argumentar...'), para luego refutarla con evidencia científica ('evidencia neurobiológica'). Esta organización de 'reconocer y refutar' aumenta la credibilidad y muestra un argumento más robusto."},
        ]
        random.shuffle(self.credibility_scenarios)
        self.current_credibility_scenario_index = 0
        self._load_credibility_scenario()

    def _load_credibility_scenario(self):
        """Carga el escenario actual del juego 'El Detective de la Credibilidad'."""
        if self.current_credibility_scenario_index < len(self.credibility_scenarios):
            for widget in self.credibility_game_frame.winfo_children():
                widget.destroy() # Limpiar el frame para el nuevo escenario

            s = self.credibility_scenarios[self.current_credibility_scenario_index]

            tk.Label(self.credibility_game_frame, text=f"Juego: ¡El Detective de la Credibilidad! (Escenario {self.current_credibility_scenario_index + 1})", 
                     font=("Arial", 16, "bold"), fg="#4682B4", bg="#F8F8FF").pack(pady=10)
            
            tk.Label(self.credibility_game_frame, text="Lee el siguiente extracto y analiza su organización:", 
                     font=("Arial", 12), bg="#F8F8FF").pack(pady=5)
            
            self.article_text_display = scrolledtext.ScrolledText(self.credibility_game_frame, width=80, height=8, font=("Arial", 11), wrap=tk.WORD, bg="#E0FFFF")
            self.article_text_display.insert(tk.END, s['text'])
            self.article_text_display.config(state=tk.DISABLED) # No editable
            self.article_text_display.pack(pady=10)

            tk.Label(self.credibility_game_frame, text="\nTu análisis: ¿Cómo la organización de este texto influye en su credibilidad o revela un posible sesgo?", 
                     font=("Arial", 12, "bold"), bg="#F8F8FF").pack(pady=10)
            
            self.user_analysis_entry = scrolledtext.ScrolledText(self.credibility_game_frame, width=80, height=5, font=("Arial", 11), wrap=tk.WORD, bg="#FFFFFF")
            self.user_analysis_entry.pack(pady=5)

            tk.Button(self.credibility_game_frame, text="Ver Análisis Experto", font=("Arial", 12), bg="#98FB98", 
                      command=self._show_credibility_analysis_result).pack(pady=10)
        else:
            self.credibility_game_window.destroy()
            messagebox.showinfo("Juego Terminado", "¡Has completado el juego del Detective de la Credibilidad!\n¡Sigue entrenando tu ojo crítico! 🕵️‍♀️")

    def _show_credibility_analysis_result(self):
        """Muestra el resultado del análisis en el juego de credibilidad."""
        s = self.credibility_scenarios[self.current_credibility_scenario_index]
        user_input = self.user_analysis_entry.get("1.0", tk.END).strip()

        messagebox.showinfo("Análisis de Credibilidad", 
                            f"--- Análisis Experto ---\n{s['analysis_points']}\n\n"
                            f"--- Tu Análisis ---\n{user_input}\n\n"
                            "¡Compara tu análisis! La clave es ver más allá de las palabras y entender la estrategia detrás del orden.")
        
        self.current_credibility_scenario_index += 1
        self._load_credibility_scenario()

    # --- NUEVOS EJERCICIOS DE ESCRITURA CON REFLEXIÓN ---

    def start_exercise_analyze_organization_for_credibility(self):
        """Inicia el ejercicio 'Organización y Credibilidad en la Noticia'."""
        self.exercise_credibility_window = tk.Toplevel(self.master)
        self.exercise_credibility_window.title("Ejercicio: ¡Organización y Credibilidad en la Noticia!")
        self.exercise_credibility_window.geometry("900x750")
        self.exercise_credibility_window.transient(self.master)

        self.exercise_credibility_frame = tk.Frame(self.exercise_credibility_window, padx=20, pady=20, bg="#F0F8FF")
        self.exercise_credibility_frame.pack(fill="both", expand=True)

        self.articles_for_exercise = [
            {"title": "Titular A: 'Crisis Energética: Precios Disparados por Nuevas Regulaciones Gubernamentales'",
             "text": "Los recientes aumentos en el costo de la energía son una consecuencia directa e ineludible de las nuevas regulaciones impuestas por el gobierno, que han estrangulado la producción. Expertos de la industria han advertido repetidamente que estas políticas llevarían a esta situación. La medida busca, según algunos, 'proteger el medio ambiente', pero el costo económico es devastador."},
            
            {"title": "Titular B: 'Preocupación por Costo Energético: Análisis de Múltiples Factores y Soluciones'",
             "text": "El aumento en los costos de la energía es un fenómeno complejo influenciado por una combinación de factores, incluyendo la fluctuación de los precios internacionales del petróleo, un incremento en la demanda global y, en menor medida, la implementación de nuevas regulaciones ambientales. Un reciente informe económico (Fuente X) detalla cómo la escasez de recursos y los desafíos de la cadena de suministro también contribuyen a la situación. Diversas soluciones, desde la inversión en energías renovables hasta la optimización del consumo, están siendo debatidas por especialistas."}
        ]
        random.shuffle(self.articles_for_exercise) # Aleatorizar el orden de los artículos

        self.current_exercise_article_index = 0
        self._load_exercise_article()

    def _load_exercise_article(self):
        """Carga el artículo actual para el ejercicio de credibilidad."""
        if self.current_exercise_article_index < len(self.articles_for_exercise):
            for widget in self.exercise_credibility_frame.winfo_children():
                widget.destroy() # Limpiar el frame para el nuevo artículo

            article_data = self.articles_for_exercise[self.current_exercise_article_index]

            tk.Label(self.exercise_credibility_frame, text=f"Artículo {self.current_exercise_article_index + 1} de {len(self.articles_for_exercise)}:", 
                     font=("Arial", 16, "bold"), fg="#4682B4", bg="#F0F8FF").pack(pady=10)
            
            tk.Label(self.exercise_credibility_frame, text=article_data['title'], 
                     font=("Arial", 14, "italic"), bg="#F0F8FF").pack(pady=5)
            
            self.article_display = scrolledtext.ScrolledText(self.exercise_credibility_frame, width=90, height=7, font=("Arial", 11), wrap=tk.WORD, bg="#E6E6FA")
            self.article_display.insert(tk.END, article_data['text'])
            self.article_display.config(state=tk.DISABLED)
            self.article_display.pack(pady=10)

            tk.Label(self.exercise_credibility_frame, text="\nTu análisis: ¿Cómo la organización de este texto influye en su credibilidad o revela un posible sesgo?", 
                     font=("Arial", 12, "bold"), bg="#F0F8FF").pack(pady=10)
            
            self.user_analysis_entry_exercise = scrolledtext.ScrolledText(self.exercise_credibility_frame, width=90, height=6, font=("Arial", 11), wrap=tk.WORD, bg="#FFFFFF")
            self.user_analysis_entry_exercise.pack(pady=5)

            tk.Button(self.exercise_credibility_frame, text="Enviar y Ver Reflexión", font=("Arial", 12), bg="#98FB98", 
                      command=self._show_exercise_credibility_reflection).pack(pady=10)
        else:
            self.exercise_credibility_window.destroy()
            messagebox.showinfo("Ejercicio Terminado", "¡Has completado el ejercicio de análisis de credibilidad!\n¡Sigue entrenando tu ojo crítico! 🕵️‍♀️")

    def _show_exercise_credibility_reflection(self):
        """Muestra la reflexión guiada para el ejercicio de credibilidad."""
        current_article_index = self.current_exercise_article_index
        user_input = self.user_analysis_entry_exercise.get("1.0", tk.END).strip()

        # Usar el análisis predefinido para la reflexión
        # Nota: En un sistema real, un backend o IA podría generar una retroalimentación más dinámica.
        # Aquí, estamos usando el 'bias_hint' del escenario original para simular una reflexión experta.
        simulated_expert_analysis = (
            "--- Análisis Experto Simulado (Referencia de Nuestro Programa) ---\n"
            "El Titular A tiende a culpar directamente al gobierno al inicio, usando un lenguaje fuerte como 'directa e ineludible' y 'estrangulado', y citando 'expertos de la industria' de forma vaga. Minimiza los objetivos ambientales. Su organización es deductiva y prioriza la crítica, sugiriendo un fuerte sesgo.\n\n"
            "El Titular B, en cambio, presenta el aumento como un 'fenómeno complejo' con 'múltiples factores', citando una 'fuente X' específica y discutiendo 'diversas soluciones'. Su organización es más equilibrada e inductiva, lo que le confiere mayor objetividad."
        )

        messagebox.showinfo("Tu Reflexión sobre el Artículo", 
                            f"Tu análisis:\n'{user_input}'\n\n"
                            f"--- Reflexión Guiada ---\n"
                            "Piensa en lo siguiente:\n"
                            "  1. ¿Qué información se puso al principio o al final? ¿Por qué crees que el autor tomó esa decisión?\n"
                            "  2. ¿Se omitió o minimizó alguna información relevante? ¿Cómo afectaría eso la credibilidad?\n"
                            "  3. ¿El texto intentó generar una emoción específica (ej. miedo, enojo) a través de cómo organizó los puntos?\n\n"
                            "¡La clave es leer la organización entre líneas!\n\n"
                            "Para una comparación con un análisis de referencia, mira la consola o un documento de apoyo si este fuera un programa completo." # Mencionamos esto ya que no tenemos el "expert_analysis" directo aquí
                            )
        
        self.current_exercise_article_index += 1
        self._load_exercise_article()


# --- Iniciar la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Leccion9App(root)
    root.mainloop()
