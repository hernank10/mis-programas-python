import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random

class ArgumentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lección 9 (12.º Grado): Argumentación Superior")
        self.root.geometry("1000x800")
        self.root.resizable(True, True) # Permitir redimensionar la ventana

        self.current_frame = None
        self.create_menu_frame()

        # Estilos para una mejor apariencia
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e0f2f7') # Fondo de frames
        self.style.configure('TLabel', background='#e0f2f7', foreground='#0a3d62', font=('Roboto', 14)) # Etiquetas de concepto
        self.style.configure('Title.TLabel', font=('Roboto Black', 22, 'bold'), foreground='#0a3d62') # Títulos
        self.style.configure('TButton', font=('Roboto Medium', 13), background='#1e88e5', foreground='white') # Botones
        self.style.map('TButton', background=[('active', '#2196f3')]) # Efecto hover
        self.style.configure('Danger.TButton', background='#e53935') # Botón de salir
        self.style.map('Danger.TButton', background=[('active', '#f44336')])

    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.root, self)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=20)

    def create_menu_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.menu_frame = ttk.Frame(self.root, padding="30 30 30 30", style='TFrame')
        self.menu_frame.pack(fill='both', expand=True)
        self.current_frame = self.menu_frame

        title_label = ttk.Label(self.menu_frame, text="Lección 9 (12.º Grado - Preuniversitario):\nArgumentación para Contextos Profesionales y de Investigación Superior",
                                anchor="center", justify="center", style='Title.TLabel')
        title_label.pack(pady=30, ipadx=10, ipady=10)

        buttons_container = ttk.Frame(self.menu_frame, style='TFrame')
        buttons_container.pack(pady=20)

        button_width = 50 # Ancho fijo para los botones

        ttk.Button(buttons_container, text="1. Introducción: ¡Dominando la Argumentación para el Éxito!",
                   command=lambda: self.show_frame(IntroductionScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="2. Argumentación en la Investigación Original",
                   command=lambda: self.show_frame(OriginalResearchConceptScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="3. Análisis Crítico de Discurso y Argumentación Sofisticada",
                   command=lambda: self.show_frame(CriticalDiscourseConceptScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="4. Argumentación en Temas Controversiales y Delicados",
                   command=lambda: self.show_frame(ControversialTopicsConceptScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="5. Presentación Oral y Escrita de Alto Nivel",
                   command=lambda: self.show_frame(HighLevelPresentationConceptScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="6. Ejercicio: ¡Diseña tu Investigación Original!",
                   command=lambda: self.show_frame(ExerciseResearchDesignScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="7. Ejercicio: ¡Analiza un Discurso Complejo y Sofisticado!",
                   command=lambda: self.show_frame(ExerciseCriticalDiscourseAnalysisScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="8. Ejercicio: ¡Argumenta un Dilema Ético/Social!",
                   command=lambda: self.show_frame(ExerciseEthicalDilemmaArgumentScreen), width=button_width).pack(pady=10)
        ttk.Button(buttons_container, text="9. Salir de la Lección", style='Danger.TButton',
                   command=self.root.quit, width=button_width).pack(pady=20)


# --- Clases de Pantallas de Conceptos ---

class ConceptScreen(ttk.Frame):
    def __init__(self, parent, app_instance, title, content):
        super().__init__(parent, padding="25 25 25 25", style='TFrame')
        self.app = app_instance

        title_label = ttk.Label(self, text=title, anchor="center", justify="center", style='Title.TLabel')
        title_label.pack(pady=15)

        # Usar scrolledtext para contenido largo
        text_area = scrolledtext.ScrolledText(self, wrap='word', font=('Roboto', 12),
                                              bg='#f7fcfd', fg='#333333', padx=15, pady=15,
                                              height=25) # Ajustar altura para que se vea bien en la ventana
        text_area.insert(tk.END, content)
        text_area.config(state='disabled') # Hacer que el texto sea de solo lectura
        text_area.pack(pady=10, fill='both', expand=True)

        back_button = ttk.Button(self, text="Volver al Menú Principal", command=self.app.create_menu_frame)
        back_button.pack(pady=15)

class IntroductionScreen(ConceptScreen):
    def __init__(self, parent, app_instance):
        title = "Introducción: ¡Dominando la Argumentación para el Éxito Universitario y Profesional!"
        content = """¡Bienvenidos, futuros líderes y pensadores innovadores! 🌟

En 12.º Grado, su dominio de la argumentación culmina en la capacidad de investigar, analizar críticamente y persuadir en los contextos más exigentes.

Esta lección es su preparación final para el rigor académico y las demandas del mundo profesional. Aprenderán a:
   ✅ Liderar investigaciones originales y construir argumentos basados en hallazgos propios.
   ✅ Deconstruir discursos complejos e identificar tácticas persuasivas sofisticadas.
   ✅ Formular posiciones matizadas en temas controversiales, considerando implicaciones éticas.
   ✅ Presentar sus ideas con autoridad y claridad en formatos de alto nivel.

¡Es hora de refinar sus habilidades para influir, innovar y destacar en cualquier campo!"""
        super().__init__(parent, app_instance, title, content)

class OriginalResearchConceptScreen(ConceptScreen):
    def __init__(self, parent, app_instance):
        title = "Argumentación en la Investigación Original"
        content = """La investigación original es la cumbre de la argumentación académica: generar nuevo conocimiento y defenderlo.

--- 1. Formulación de una Pregunta de Investigación Original: ---
  * Delimitación del Problema: Identificar un vacío o una controversia específica en el conocimiento existente. No se trata solo de describir un tema, sino de buscar una respuesta nueva y no trivial.
  * Criterios de Originalidad: ¿Tu pregunta aporta algo genuinamente nuevo? ¿Resuelve una disputa académica? ¿Aplica una teoría existente a un nuevo contexto o población?
  * Factibilidad: ¿Es posible investigar esta pregunta con los recursos (tiempo, datos, acceso) disponibles?

--- 2. Diseño de Investigación Argumentativa (Metodología): ---
  * Selección y Justificación: La elección metodológica debe ser la mejor para responder tu pregunta.
    * Cuantitativa: Datos numéricos, estadísticas (encuestas a gran escala, experimentos). Justificación: medir, comparar, generalizar hallazgos.
    * Cualitativa: Datos textuales, interpretativos (entrevistas en profundidad, grupos focales, análisis de contenido). Justificación: comprender perspectivas, experiencias, significados profundos.
    * Mixta: Combinación de ambas. Justificación: visión más completa y robusta al abordar diferentes aspectos del problema.
  * Consideraciones Éticas: Fundamentales. Incluyen: consentimiento informado, privacidad y anonimato de los participantes, imparcialidad del investigador y manejo responsable de los datos.

--- 3. Análisis y Síntesis de Literatura Académica (Estado del Arte): ---
  * Identificación de Debates Centrales: ¿Qué dicen los principales autores sobre el tema? ¿Dónde hay desacuerdo o consenso?
  * Teorías Predominantes y Metodologías Aceptadas: Entender el 'lenguaje' y las normas del campo de estudio para posicionar tu trabajo.
  * Brechas en el Conocimiento: Es crucial identificar dónde tu investigación puede hacer una contribución original, llenando un vacío existente.

--- 4. Presentación de Hallazgos Originales: ---
  * Integración con la Literatura Existente: Tus hallazgos deben dialogar con lo que ya se sabe, ya sea confirmando, refutando o extendiendo el conocimiento. No los presentes de forma aislada.
  * Argumentación Coherente: Cada sección de tu investigación (introducción, metodología, resultados, discusión, conclusión) debe construir el argumento central de tu tesis original de forma lógica y secuencial."""
        super().__init__(parent, app_instance, title, content)

class CriticalDiscourseConceptScreen(ConceptScreen):
    def __init__(self, parent, app_instance):
        title = "Análisis Crítico de Discurso y Argumentación Sofisticada"
        content = """El pensamiento crítico avanzado es esencial para navegar y desmantelar discursos complejos y potencialmente engañosos.

--- 1. Deconstrucción de Discursos Políticos y Científicos Complejos: ---
  * Identificación de Agendas Ocultas: ¿Hay intereses económicos, políticos o ideológicos no declarados detrás del mensaje? ¿Quién se beneficia del discurso?
  * Suposiciones Implícitas: ¿Qué se da por sentado sin ser explícitamente dicho? ¿Hay premisas no declaradas o sesgos culturales/sociales?
  * Uso Estratégico de Estadísticas y Datos: Analiza si las estadísticas están presentadas de forma engañosa (ej. correlación vs. causalidad, tamaño de la muestra, gráficos manipulados) o si se omiten datos relevantes.
  * Apelaciones Retóricas Avanzadas:
    * Kairos: La oportunidad o el 'momento adecuado' para el discurso. ¿Por qué se dice esto AHORA?
    * Decorum: La adecuación del discurso al público, la situación y el estilo. ¿Es el tono apropiado para el mensaje y la audiencia, o busca manipular?

--- 2. Identificación de Falacias Lógicas Avanzadas y Tácticas Persuasivas Engañosas: ---
  * Ad Populum (Apelación a la Popularidad): Argumentar que algo es verdad porque muchas personas lo creen o hacen.
  * Falsa Dicotomía/Dilema Falso: Presentar solo dos opciones como si fueran las únicas posibles, cuando en realidad existen más.
  * Pendiente Resbaladiza: Afirmar que una acción inevitablemente conducirá a una serie de consecuencias negativas, a menudo exageradas y sin evidencia suficiente.
  * Tu Quoque (Tú También): Desacreditar un argumento señalando que el oponente también ha hecho lo que critica, en lugar de abordar el argumento en sí.
  * Apelación a la Ignorancia: Argumentar que algo es verdadero porque no se ha probado que sea falso, o falso porque no se ha probado que sea verdadero.
  * Hombre de Paja/Falsa Equivalencia: Distorsionar o exagerar el argumento del oponente para hacerlo más fácil de atacar, o equiparar dos cosas que no son realmente equivalentes.

--- 3. Evaluación de la Validez y Solidez de Argumentos de Expertos: ---
  * No solo el 'qué': Más allá de lo que dice un experto, analiza la calidad de su evidencia, la coherencia lógica de su razonamiento y si considera y aborda contrapuntos.
  * Consenso Científico vs. Opinión Individual: Distingue entre un hallazgo validado por el consenso de la comunidad académica y la opinión, incluso de un experto individual, que puede no ser representativa del campo."""
        super().__init__(parent, app_instance, title, content)

class ControversialTopicsConceptScreen(ConceptScreen):
    def __init__(self, parent, app_instance):
        title = "Argumentación en Temas Controversiales y Delicados"
        content = """Abordar la controversia y los dilemas éticos con maestría requiere no solo lógica, sino también empatía y una profunda consideración ética.

--- 1. Formulación de Posiciones Matizadas: ---
  * Reconocimiento de la Complejidad: Entender que muchos problemas no tienen soluciones binarias o 'correctas', sino múltiples perspectivas válidas y complejidades inherentes.
  * Integración de Múltiples Perspectivas: Mostrar que has considerado diferentes puntos de vista, incluso los opuestos. Esto no debilita tu Ethos; lo fortalece al demostrar un pensamiento exhaustivo.
  * Lenguaje Preciso: Evitar generalizaciones excesivas, simplificaciones y lenguaje polarizador que pueda alienar a la audiencia.

--- 2. Construcción de Argumentos Basados en Valores y Principios Éticos: ---
  * Más allá de los Datos: Reconocer que algunas decisiones se basan fundamentalmente en principios morales, justicia, equidad, derechos humanos, dignidad, etc., no solo en estadísticas.
  * Consistencia Ética: Asegurar que tu argumento no contradiga principios éticos fundamentales que tu audiencia o la sociedad en general valoran.
  * Apelación a la Conciencia: Utilizar Pathos de manera ética para inspirar acciones basadas en valores compartidos, sin manipular emociones.

--- 3. Comunicación Empática y Estratégica: ---
  * Respeto y Escucha Activa: Abordar a quienes tienen puntos de vista diferentes con respeto genuino, buscando entender sus razones, no solo refutarlas.
  * Anticipación de Reacciones Emocionales: En temas sensibles, saber que el público puede reaccionar emocionalmente. Prepara tu discurso para manejar estas reacciones con calma y tacto.
  * Adaptación sin Comprometer la Integridad: Ajustar el lenguaje y el enfoque al público sin sacrificar la verdad, la evidencia o tus principios fundamentales. La integridad es primordial."""
        super().__init__(parent, app_instance, title, content)

class HighLevelPresentationConceptScreen(ConceptScreen):
    def __init__(self, parent, app_instance):
        title = "Presentación Oral y Escrita de Alto Nivel"
        content = """La persuasión profesional y académica exige no solo un gran argumento, sino también una ejecución impecable en la presentación.

--- 1. Estrategias para Ponencias y Presentaciones Académicas: ---
  * Organización Lógica Impecable: Una introducción clara (problema, pregunta, tesis), un desarrollo estructurado (hallazgos, análisis con evidencia), y una conclusión memorable (reafirmación, implicaciones, llamado a la acción).
  * Claridad Visual (Diapositivas/Apoyos): Minimalismo visual, gráficos claros y etiquetados, puntos clave concisos. Las diapositivas deben apoyar, no reemplazar, al orador.
  * Manejo de Preguntas y Objeciones: Escuchar activamente la pregunta, procesarla rápidamente, responder con calma y autoridad. Admite limitaciones si es necesario, demuestra honestidad intelectual. 'Gracias por esa pregunta tan pertinente...'
  * Presencia y Credibilidad: Contacto visual, postura confiada, voz clara y modulada.

--- 2. Redacción de Documentos de Posición y Propuestas de Investigación: ---
  * Estructura Formal: Resumen ejecutivo, antecedentes, planteamiento del problema, revisión de literatura, metodología propuesta, resultados esperados, presupuesto (si aplica), cronograma, impacto y conclusiones.
  * Lenguaje Preciso y Conciso: Cada palabra cuenta. Evitar la redundancia, la ambigüedad y la jerga innecesaria. La claridad es primordial.
  * Argumentación Basada en Evidencia: Cada afirmación debe ser respaldada rigurosamente por datos, lógica sólida o referencias académicas fiables. No dejar espacio a la especulación infundada.

--- 3. Uso del Lenguaje Persuasivo para Impacto (con Ética): ---
  * Ritmo y Pausas Estratégicas: Utiliza el ritmo del habla y pausas para enfatizar puntos clave, permitir la asimilación de información compleja y crear tensión o reflexión.
  * Repetición Estratégica: De ideas centrales, frases memorables o eslóganes, para reforzar el mensaje sin ser redundante.
  * Analogías Complejas y Metáforas Potentes: Para explicar conceptos difíciles de forma accesible y relacionarlos con la experiencia de la audiencia.
  * Anécdotas Breves y Relevantes: Para humanizar el mensaje y generar conexión emocional (Pathos bien usado), siempre y cuando apoyen el argumento central.
  * Siempre al Servicio de la Claridad y la Verdad: Las técnicas retóricas deben amplificar la verdad, no distorsionar la realidad ni manipular al público. La integridad es primordial en toda comunicación persuasiva."""
        super().__init__(parent, app_instance, title, content)


# --- Clases de Pantallas de Ejercicios ---

class ExerciseResearchDesignScreen(ttk.Frame):
    def __init__(self, parent, app_instance):
        super().__init__(parent, padding="25 25 25 25", style='TFrame')
        self.app = app_instance

        self.problems = [
            {"problem_statement": "Existe una creciente polarización en las redes sociales sobre temas científicos (ej. cambio climático, vacunas). ¿Cómo se podría diseñar una investigación original que proponga estrategias para fomentar el diálogo constructivo y reducir la desinformación en estas plataformas?",
             "guide": """Tu diseño de investigación debe incluir:
    1. Una [b]pregunta de investigación específica y ORIGINAL[/b] (que no haya sido respondida directamente por otros).
    2. La [b]metodología propuesta[/b] (cuantitativa, cualitativa o mixta) y una [b]justificación clara[/b] de por qué es la más adecuada para tu pregunta.
    3. Los [b]tipos de datos[/b] que recopilarías (ej. encuestas, entrevistas, análisis de contenido de publicaciones, experimentos) y [b]cómo los analizarías[/b] para responder a tu pregunta.
    4. Las [b]posibles limitaciones de tu investigación[/b] y [b]desafíos éticos[/b] (ej. privacidad, sesgo del investigador, manipulación de datos)."""},
            {"problem_statement": "A pesar de la disponibilidad de información sobre hábitos de vida saludables, las tasas de obesidad y enfermedades crónicas siguen siendo altas en la población joven. ¿Cómo diseñarías una investigación original que explore la efectividad de intervenciones innovadoras (no solo educativas) para promover estilos de vida saludables en este grupo demográfico?",
             "guide": """Tu diseño de investigación debe incluir:
    1. Una [b]pregunta de investigación específica y ORIGINAL[/b] que aborde el problema.
    2. La [b]metodología propuesta[/b] (cuantitativa, cualitativa o mixta) y una [b]justificación clara[/b] de por qué es la más adecuada.
    3. Los [b]tipos de datos[/b] que recopilarías (ej. datos de salud, diarios de hábitos, grupos focales, resultados de programas piloto) y [b]cómo los analizarías[/b].
    4. [b]Consideraciones éticas clave[/b] al trabajar con una población joven (ej. consentimiento de padres/tutores, protección de datos sensibles, impacto psicológico)."""},
        ]
        self.current_problem_index = 0
        random.shuffle(self.problems)

        title_label = ttk.Label(self, text="Ejercicio: ¡Diseña tu Investigación Original!",
                                anchor="center", justify="center", style='Title.TLabel')
        title_label.pack(pady=15)

        self.problem_text_label = ttk.Label(self, text="", wraplength=900, justify="left", font=('Roboto', 13), foreground='#333333', background='#f0f8ff')
        self.problem_text_label.pack(pady=10, fill='x')

        ttk.Label(self, text="Tu Propuesta de Diseño de Investigación (Sé lo más detallado y específico posible):",
                  font=('Roboto Medium', 13), foreground='#0a3d62', background='#e0f2f7').pack(pady=(10,5), fill='x')
        self.user_design_input = scrolledtext.ScrolledText(self, wrap='word', font=('Roboto', 12),
                                                           bg='#ffffff', fg='#333333', padx=10, pady=10, height=15)
        self.user_design_input.pack(pady=10, fill='both', expand=True)

        button_frame = ttk.Frame(self, style='TFrame')
        button_frame.pack(pady=15)
        ttk.Button(button_frame, text="Enviar Diseño y Reflexionar", command=self.submit_design).pack(side='left', padx=10)
        ttk.Button(button_frame, text="Siguiente Tema (o volver al menú)", command=self.load_next_problem).pack(side='left', padx=10)
        ttk.Button(button_frame, text="Volver al Menú Principal", command=self.app.create_menu_frame).pack(side='left', padx=10)

        self.load_problem()

    def load_problem(self):
        if self.current_problem_index < len(self.problems):
            problem_data = self.problems[self.current_problem_index]
            self.problem_text_label.config(text=f"Problema de Investigación a Abordar:\n{problem_data['problem_statement']}\n\nInstrucciones para tu Diseño:\n{problem_data['guide']}")
            self.user_design_input.delete('1.0', tk.END)
        else:
            messagebox.showinfo("Ejercicio Terminado", "¡Has diseñado estrategias de investigación! ¡Excelente preparación para la universidad!")
            self.app.create_menu_frame()

    def submit_design(self):
        user_design = self.user_design_input.get('1.0', tk.END).strip()
        if not user_design:
            messagebox.showwarning("Entrada Vacía", "Por favor, escribe tu propuesta de diseño antes de enviar.")
            return

        feedback_message = (f"--- Tu Propuesta de Diseño de Investigación ---\n{user_design}\n\n"
                            f"--- Guía de Reflexión (Evalúa tu diseño como lo haría un comité académico) ---\n"
                            f"1. **Originalidad y Especificidad:** ¿Tu pregunta es genuinamente original y lo suficientemente específica para ser investigable?\n"
                            f"2. **Coherencia Metodológica:** ¿La metodología elegida es la más apropiada y justificaste por qué? ¿Los tipos de datos y análisis son coherentes con ella?\n"
                            f"3. **Factibilidad y Ética:** ¿Es tu diseño factible con recursos limitados? ¿Abordaste las limitaciones y los aspectos éticos de manera exhaustiva y reflexiva?\n\n"
                            f"¡Un diseño riguroso es el cimiento de una investigación creíble y con impacto! 🔬")
        
        messagebox.showinfo("Reflexión sobre tu Diseño", feedback_message)
        # No avanzamos automáticamente al siguiente problema, el usuario debe pulsar "Siguiente Tema"

    def load_next_problem(self):
        self.current_problem_index += 1
        self.load_problem()


class ExerciseCriticalDiscourseAnalysisScreen(ttk.Frame):
    def __init__(self, parent, app_instance):
        super().__init__(parent, padding="25 25 25 25", style='TFrame')
        self.app = app_instance

        title_label = ttk.Label(self, text="Ejercicio: ¡Analiza un Discurso Complejo y Sofisticado!",
                                anchor="center", justify="center", style='Title.TLabel')
        title_label.pack(pady=15)

        ttk.Label(self, text="Este ejercicio está en desarrollo para Tkinter. ¡Próximamente podrás deconstruir discursos políticos/científicos y detectar falacias avanzadas!",
                  wraplength=800, justify="center", font=('Roboto', 14), foreground='#5c6bc0').pack(pady=50)

        back_button = ttk.Button(self, text="Volver al Menú Principal", command=self.app.create_menu_frame)
        back_button.pack(pady=15)

class ExerciseEthicalDilemmaArgumentScreen(ttk.Frame):
    def __init__(self, parent, app_instance):
        super().__init__(parent, padding="25 25 25 25", style='TFrame')
        self.app = app_instance

        title_label = ttk.Label(self, text="Ejercicio: ¡Argumenta un Dilema Ético/Social!",
                                anchor="center", justify="center", style='Title.TLabel')
        title_label.pack(pady=15)

        ttk.Label(self, text="Este ejercicio está en desarrollo para Tkinter. ¡Próximamente podrás formular argumentos matizados sobre temas controversiales y éticos!",
                  wraplength=800, justify="center", font=('Roboto', 14), foreground='#5c6bc0').pack(pady=50)

        back_button = ttk.Button(self, text="Volver al Menú Principal", command=self.app.create_menu_frame)
        back_button.pack(pady=15)


# --- Ejecución de la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ArgumentationApp(root)
    root.mainloop()
