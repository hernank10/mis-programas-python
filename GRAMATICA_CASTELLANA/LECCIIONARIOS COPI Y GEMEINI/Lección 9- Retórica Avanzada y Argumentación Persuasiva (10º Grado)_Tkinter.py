import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk # ttk para widgets estilizados
import random

class Leccion9Grado10App:
    def __init__(self, master):
        self.master = master
        master.title("Lección 9: Retórica Avanzada y Argumentación Persuasiva (10º Grado)")
        master.geometry("1000x750")
        master.resizable(False, False) # Evita que el usuario cambie el tamaño de la ventana principal

        self.frames = {}
        self._create_main_menu_frame()
        self._create_introduction_frame()
        self._create_rhetorical_appeals_concept_frame()
        self._create_complex_structures_concept_frame()
        self._create_fallacies_and_adaptation_concept_frame()

        self.show_frame("main_menu")

    def _create_main_menu_frame(self):
        frame = tk.Frame(self.master, padx=30, pady=30, bg="#F0FFF0") # Verde claro suave
        self.frames["main_menu"] = frame

        ttk.Label(frame, text="Lección 9: Retórica Avanzada y Argumentación Persuasiva",
                  font=("Verdana", 24, "bold"), foreground="#2E8B57", background="#F0FFF0").pack(pady=30)

        options = [
            ("1. Introducción: ¡Maestros de la Persuasión!", "introduction"),
            ("2. Dominio de Apelaciones Retóricas (Ethos, Pathos, Logos)", "rhetorical_appeals_concept"),
            ("3. Estructuras Argumentativas Complejas (Toulmin, Rogerian)", "complex_structures_concept"),
            ("4. Anticipación de Contrapuntos y Falacias Lógicas", "fallacies_and_adaptation_concept"),
            ("5. NUEVO: Ejercicio: ¡Analiza el Discurso Retórico!", self._start_exercise_analyze_rhetorical_discourse),
            ("6. NUEVO: Ejercicio: ¡Construye un Argumento Estructurado!", self._start_exercise_construct_structured_argument),
            ("7. NUEVO: Ejercicio: ¡Prepara tu Refutación Sofisticada!", self._start_exercise_sophisticated_refutation),
            ("8. Salir de la Lección", self.master.quit)
        ]

        for text, command in options:
            if isinstance(command, str):
                btn = ttk.Button(frame, text=text, style="Menu.TButton",
                                 command=lambda f=command: self.show_frame(f))
            else:
                 btn = ttk.Button(frame, text=text, style="Menu.TButton",
                                 command=command)
            btn.pack(pady=8, fill="x", ipadx=20, ipady=5)
        
        # Estilo para los botones del menú
        style = ttk.Style()
        style.configure("Menu.TButton", font=("Arial", 14), background="#90EE90", foreground="black",
                        relief="raised", borderwidth=2, focusthickness=4, focuscolor="none")
        style.map("Menu.TButton", background=[('active', '#66CDAA')]) # Color al pasar el ratón

    def show_frame(self, frame_name):
        for name, frame in self.frames.items():
            if name == frame_name:
                frame.pack(fill="both", expand=True)
            else:
                frame.pack_forget()

    # --- Frames de Conceptos (Con un diseño mejorado y uso de ScrolledText) ---

    def _create_introduction_frame(self):
        frame = tk.Frame(self.master, padx=30, pady=30, bg="#F8F8FF") # Lavanda claro
        self.frames["introduction"] = frame

        ttk.Label(frame, text="Introducción: ¡Maestros de la Persuasión!",
                  font=("Verdana", 20, "bold"), foreground="#483D8B", background="#F8F8FF").pack(pady=15)
        
        intro_text = """¡Bienvenidos, futuros oradores y pensadores críticos de élite! 🗣️
En 9.º Grado, aprendieron a desentrañar la organización y a construir argumentos sólidos. ¡Ahora, en 10.º, es hora de DOMINAR la persuasión!

Nos sumergiremos en las técnicas que los grandes oradores y escritores usan para mover mentes y corazones. Aprenderán a no solo construir argumentos lógicos, sino a imbuirlos de fuerza emocional y credibilidad inquebrantable.

En esta lección, ustedes serán capaces de:
   ✅ **Aplicar conscientemente** Ethos, Pathos y Logos en sus propios discursos.
   ✅ **Diseñar argumentos complejos** usando modelos avanzados como el de Toulmin.
   ✅ **Anticipar y neutralizar** objeciones y falacias lógicas de manera proactiva.
   ✅ **Adaptar su estrategia retórica** a diferentes audiencias y contextos con maestría.

¡Prepárense para influir, convencer y liderar con la palabra!"""
        
        self._create_scrolled_text_display(frame, intro_text).pack(pady=10)
        self._create_back_button(frame).pack(pady=20)

    def _create_rhetorical_appeals_concept_frame(self):
        frame = tk.Frame(self.master, padx=30, pady=30, bg="#F8F8FF")
        self.frames["rhetorical_appeals_concept"] = frame

        ttk.Label(frame, text="Dominio de Apelaciones Retóricas (Ethos, Pathos, Logos)",
                  font=("Verdana", 20, "bold"), foreground="#483D8B", background="#F8F8FF").pack(pady=15)
        
        concept_text = """En 10.º Grado, no solo identificamos Ethos, Pathos y Logos, ¡los usamos estratégicamente!

--- **Ethos (Credibilidad)** ---
  * **Uso:** Construir confianza y autoridad.
  * **Estrategias de Organización:**
    * **Inicio del discurso:** Presentar cualificaciones, experiencia, valores compartidos.
    * **Integración de fuentes:** Citar expertos respetados al principio de una sección para validar un punto.
    * **Reconocimiento de limitaciones:** Mostrar humildad o conocimiento de la complejidad de un tema para parecer más objetivo.

--- **Pathos (Emoción)** ---
  * **Uso:** Conectar con la audiencia a un nivel emocional.
  * **Estrategias de Organización:**
    * **Introducción:** Usar anécdotas o historias impactantes para captar la atención emocional.
    * **Cuerpo del argumento:** Presentar ejemplos vívidos o testimonios personales en momentos clave para reforzar la conexión emocional.
    * **Conclusión:** Apelar a valores compartidos o un llamado a la acción que resuene emocionalmente.

--- **Logos (Lógica)** ---
  * **Uso:** Apelar a la razón y la evidencia.
  * **Estrategias de Organización:**
    * **Cuerpo del argumento:** Presentar evidencia (estadísticas, hechos, estudios) de forma clara y estructurada (ej. de lo general a lo específico).
    * **Causa y Efecto:** Organizar la información para mostrar relaciones lógicas claras.
    * **Problema-Solución:** Presentar el problema con datos y luego la solución lógica."""
        
        self._create_scrolled_text_display(frame, concept_text).pack(pady=10)
        self._create_back_button(frame).pack(pady=20)

    def _create_complex_structures_concept_frame(self):
        frame = tk.Frame(self.master, padx=30, pady=30, bg="#F8F8FF")
        self.frames["complex_structures_concept"] = frame

        ttk.Label(frame, text="Estructuras Argumentativas Complejas (Toulmin, Rogerian)",
                  font=("Verdana", 20, "bold"), foreground="#483D8B", background="#F8F8FF").pack(pady=15)
        
        concept_text = """Más allá de lo básico, las estructuras complejas te permiten argumentar con matices.

--- **Modelo de Toulmin** ---
  * **Componentes:**
    1.  **Aserción (Claim):** Tu punto principal.
    2.  **Datos (Data):** Evidencia que apoya la aserción.
    3.  **Garantía (Warrant):** La lógica que conecta los datos con la aserción (por qué los datos son relevantes).
    4.  **Respaldo (Backing):** Evidencia para la garantía.
    5.  **Refutación (Rebuttal):** Reconocimiento y respuesta a las objeciones.
    6.  **Cualificador (Qualifier):** Grado de certeza de la aserción (ej. 'probablemente', 'usualmente').
  * **Organización:** No es lineal; puedes presentar tu aserción, luego los datos, luego la garantía, y entrelazar refutaciones y cualificadores donde sean necesarios. Fomenta un argumento exhaustivo.

--- **Argumento Rogerian (Orientado al Consenso)** ---
  * **Objetivo:** No es "ganar" el debate, sino encontrar un terreno común y reducir la hostilidad.
  * **Organización:**
    1.  **Introducción:** Presentar el problema de forma neutral.
    2.  **Entendimiento de la Perspectiva Opuesta:** Explicar el punto de vista del oponente de forma justa y empática.
    3.  **Identificación de Terreno Común:** Destacar los puntos en los que ambos lados pueden estar de acuerdo.
    4.  **Presentación de tu Perspectiva:** Exponer tu propio argumento, mostrando cómo puede beneficiar a ambas partes o cómo es una solución superior.
    5.  **Conclusión:** Un llamado a la colaboración o a una solución mutuamente beneficiosa.
  * **Uso:** Temas polarizados donde se busca la reconciliación o soluciones prácticas."""
        
        self._create_scrolled_text_display(frame, concept_text).pack(pady=10)
        self._create_back_button(frame).pack(pady=20)

    def _create_fallacies_and_adaptation_concept_frame(self):
        frame = tk.Frame(self.master, padx=30, pady=30, bg="#F8F8FF")
        self.frames["fallacies_and_adaptation_concept"] = frame

        ttk.Label(frame, text="Anticipación y Neutralización de Contrapuntos y Falacias Lógicas",
                  font=("Verdana", 20, "bold"), foreground="#483D8B", background="#F8F8FF").pack(pady=15)
        
        concept_text = """Un gran persuasor no solo argumenta, ¡también se defiende!

--- **Anticipación y Neutralización de Contrapuntos:** ---
  * **Proactividad:** En lugar de esperar que te los presenten, incorpora y desmantela los contrapuntos *dentro* de tu propio argumento.
  * **Estrategias de Organización:**
    * **"Steel-manning":** Presenta el argumento del oponente en su versión más fuerte *antes* de refutarlo. Esto demuestra que lo entiendes y aumenta tu credibilidad.
    * **Inclusión Temprana:** Si sabes que una objeción es muy fuerte, abórdala al principio para despejar el camino para tu argumento principal.
    * **Análisis de Consecuencias:** Muestra cómo el contrapunto llevaría a resultados negativos o ilógicos.

--- **Identificación y Refutación de Falacias Lógicas (Ej. Ad Hominem, Hombre de Paja, Falsa Causa):** ---
  * **Organización de Refutación:**
    1.  **Identifica la falacia:** Nómbrala o descríbela.
    2.  **Explica por qué es una falacia:** Muestra cómo la lógica está rota.
    3.  **Re-enfoca el debate:** Dirige la atención de vuelta al argumento principal basado en evidencia y lógica.

--- **Adaptación Retórica a la Audiencia y el Contexto:** ---
  * **Audiencia Favorable:** Organiza para reforzar creencias, inspirar a la acción (quizás con más Pathos).
  * **Audiencia Escéptica/Hostil:** Empieza con terreno común (Rogerian), usa más Logos y Ethos, evita confrontaciones directas al inicio.
  * **Contexto (Oral vs. Escrito):**
    * **Oral:** Más repetición, frases más cortas, pausas, énfasis en Pathos y Ethos inmediatos.
    * **Escrito:** Más detalle, estructura visual (párrafos, títulos), citas extensas, más énfasis en Logos detallado.
  * **Organización para el Debate:** Estructura para presentar tu caso, refutar el oponente, y resumir tu posición, todo dentro de límites de tiempo estrictos."""
        
        self._create_scrolled_text_display(frame, concept_text).pack(pady=10)
        self._create_back_button(frame).pack(pady=20)


    def _create_scrolled_text_display(self, parent_frame, text_content):
        """Helper para crear un widget ScrolledText no editable para conceptos."""
        text_widget = scrolledtext.ScrolledText(parent_frame, width=90, height=20, font=("Arial", 12), 
                                                wrap=tk.WORD, bg="#FFFFFF", relief=tk.FLAT, bd=0, padx=10, pady=10)
        text_widget.insert(tk.END, text_content)
        text_widget.config(state=tk.DISABLED)
        return text_widget

    def _create_back_button(self, parent_frame):
        """Helper para crear un botón 'Volver al Menú Principal'."""
        return ttk.Button(parent_frame, text="Volver al Menú Principal", style="Back.TButton",
                          command=lambda: self.show_frame("main_menu"))
        style = ttk.Style()
        style.configure("Back.TButton", font=("Arial", 12), background="#ADD8E6", foreground="black",
                        relief="raised", borderwidth=2)
        style.map("Back.TButton", background=[('active', '#87CEEB')])


    # --- Métodos para Iniciar Ejercicios Avanzados (abren nuevas ventanas Toplevel) ---

    def _start_exercise_analyze_rhetorical_discourse(self):
        """Inicia el ejercicio 'Analiza el Discurso Retórico'."""
        ExerciseAnalyzeRhetoricalDiscourse(self.master)

    def _start_exercise_construct_structured_argument(self):
        """Inicia el ejercicio 'Construye un Argumento Estructurado'."""
        ExerciseConstructStructuredArgument(self.master)

    def _start_exercise_sophisticated_refutation(self):
        """Inicia el ejercicio 'Prepara tu Refutación Sofisticada'."""
        ExerciseSophisticatedRefutation(self.master)


class ExerciseAnalyzeRhetoricalDiscourse:
    """Clase para el ejercicio 'Analiza el Discurso Retórico'."""
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Ejercicio: ¡Analiza el Discurso Retórico!")
        self.window.geometry("1000x800")
        self.window.transient(master)

        self.frame = tk.Frame(self.window, padx=25, pady=25, bg="#F0F8FF")
        self.frame.pack(fill="both", expand=True)

        self.discourses = [
            {"title": "Extracto de un Discurso Político",
             "text": "Compatriotas, les hablo hoy no como un político, sino como un padre que ve el futuro de sus hijos amenazado. Hemos presenciado cómo nuestras industrias languidecen por políticas miopes, dejando a miles sin sustento. Es una verdad innegable que cada cifra de desempleo representa una familia con menos esperanza. Por eso, mi propuesta, basada en rigurosos estudios económicos, es la única vía lógica para revitalizar nuestra nación. ¡Unámonos por un futuro próspero y seguro!",
             "analysis_guide": {
                 "ethos": "El orador construye Ethos al inicio: 'no como un político, sino como un padre' (apela a la moralidad y experiencia común), y más adelante con 'basada en rigurosos estudios económicos' (apela a la credibilidad experta).",
                 "pathos": "Fuerte uso de Pathos: 'futuro de sus hijos amenazado', 'industrias languidecen', 'miles sin sustento', 'familia con menos esperanza'. Usa un lenguaje emocional para conectar.",
                 "logos": "Uso limitado de Logos en el extracto: 'cifra de desempleo' y 'rigurosos estudios económicos' son menciones, pero no se presentan los datos concretos. Se asume que la propuesta es 'la única vía lógica' sin detallar la lógica.",
                 "organization": "La organización comienza con Pathos (conexión emocional y personal), pasa a plantear el 'problema' con más Pathos, luego presenta una solución con una ligera apelación a Logos (estudios) y concluye con un llamado a la acción emocional. Prioriza la conexión y el impacto emocional sobre el detalle lógico en este extracto."
             }},
            {"title": "Extracto de un Editorial Científico",
             "text": "La evidencia acumulada durante décadas, proveniente de miles de estudios revisados por pares, demuestra inequívocamente que el cambio climático es un fenómeno acelerado por la actividad humana. Los datos satelitales confirman un aumento sostenido de la temperatura global, correlacionado directamente con los niveles de CO2 atmosférico. Quienes insisten en que 'es un ciclo natural' ignoran la magnitud y velocidad de los cambios actuales, los cuales superan con creces cualquier fluctuación histórica. La inacción actual tendrá repercusiones severas, no solo ecológicas, sino socioeconómicas demostrables.",
             "analysis_guide": {
                 "ethos": "Construye Ethos con 'evidencia acumulada durante décadas', 'miles de estudios revisados por pares', 'datos satelitales'. Apela a la autoridad de la ciencia y la comunidad investigadora.",
                 "pathos": "Uso muy limitado de Pathos, se enfoca en la objetividad: 'repercusiones severas' es lo más cercano a una apelación emocional, pero se acompaña de 'socioeconómicas demostrables', manteniendo un tono racional.",
                 "logos": "Fuerte uso de Logos: 'evidencia acumulada', 'datos sateliales confirman aumento sostenido', 'correlacionado directamente con niveles de CO2'. Refuta directamente un contrapunto ('es un ciclo natural') usando lógica y evidencia ('superan con creces cualquier fluctuación histórica').",
                 "organization": "La organización es deductiva, iniciando con la aserción respaldada por Logos (evidencia científica), luego refuta directamente el contrapunto popular con más Logos. Termina con las consecuencias, manteniendo un tono de advertencia basado en la lógica. Prioriza la lógica y la evidencia sobre la emoción."
             }}
        ]
        random.shuffle(self.discourses)
        self.current_discourse_index = 0
        self._load_discourse()

    def _load_discourse(self):
        if self.current_discourse_index < len(self.discourses):
            for widget in self.frame.winfo_children():
                widget.destroy()

            discourse_data = self.discourses[self.current_discourse_index]

            ttk.Label(self.frame, text=f"Ejercicio: ¡Analiza el Discurso Retórico! (Extracto {self.current_discourse_index + 1})", 
                      font=("Arial", 18, "bold"), foreground="#4682B4", background="#F0F8FF").pack(pady=10)
            
            ttk.Label(self.frame, text=discourse_data['title'], 
                      font=("Arial", 15, "italic"), background="#F0F8FF").pack(pady=5)
            
            self.discourse_display = scrolledtext.ScrolledText(self.frame, width=95, height=10, font=("Arial", 12), wrap=tk.WORD, bg="#E6E6FA", relief=tk.FLAT, bd=1)
            self.discourse_display.insert(tk.END, discourse_data['text'])
            self.discourse_display.config(state=tk.DISABLED)
            self.discourse_display.pack(pady=10)

            ttk.Label(self.frame, text="\nTu análisis: Identifica y explica cómo se usan Ethos, Pathos, Logos en este extracto. ¿Cómo la organización contribuye (o no) a la persuasión?", 
                      font=("Arial", 13, "bold"), background="#F0F8FF").pack(pady=10)
            
            self.user_analysis_entry = scrolledtext.ScrolledText(self.frame, width=95, height=8, font=("Arial", 11), wrap=tk.WORD, bg="#FFFFFF", relief=tk.SUNKEN, bd=1)
            self.user_analysis_entry.pack(pady=5)

            ttk.Button(self.frame, text="Ver Análisis Experto y Continuar", style="Analyze.TButton", 
                       command=self._show_analysis_and_continue).pack(pady=15)
        else:
            self.window.destroy()
            messagebox.showinfo("Ejercicio Terminado", "¡Has analizado varios discursos! Sigue aplicando estas habilidades críticas. 🗣️✍️")

    def _show_analysis_and_continue(self):
        user_input = self.user_analysis_entry.get("1.0", tk.END).strip()
        discourse_data = self.discourses[self.current_discourse_index]

        expert_analysis = f"--- Análisis Experto ---\n" \
                          f"**Ethos:** {discourse_data['analysis_guide']['ethos']}\n" \
                          f"**Pathos:** {discourse_data['analysis_guide']['pathos']}\n" \
                          f"**Logos:** {discourse_data['analysis_guide']['logos']}\n" \
                          f"**Organización:** {discourse_data['analysis_guide']['organization']}"

        messagebox.showinfo("Tu Análisis y el Experto", 
                            f"--- Tu Análisis ---\n{user_input}\n\n"
                            f"{expert_analysis}\n\n"
                            "¡Compara tu análisis! La clave es ver cómo estas apelaciones trabajan juntas en la estructura.")
        
        self.current_discourse_index += 1
        self._load_discourse()

# --- Ejercicios Adicionales (Placeholders para que los puedas implementar siguiendo el patrón) ---

class ExerciseConstructStructuredArgument:
    """Clase placeholder para el ejercicio 'Construye un Argumento Estructurado'."""
    def __init__(self, master):
        messagebox.showinfo("Próximamente", "Este ejercicio de 'Construye un Argumento Estructurado' estará disponible pronto. ¡Requiere un análisis detallado!")
        # Aquí iría la implementación completa del ejercicio con sus widgets y lógica
        # Por ahora, solo cerramos la ventana de mensaje
        pass # No se crea Toplevel aquí, el messagebox ya es suficiente.

class ExerciseSophisticatedRefutation:
    """Clase placeholder para el ejercicio 'Prepara tu Refutación Sofisticada'."""
    def __init__(self, master):
        messagebox.showinfo("Próximamente", "Este ejercicio de 'Prepara tu Refutación Sofisticada' estará disponible pronto. ¡Requiere un análisis detallado!")
        # Aquí iría la implementación completa del ejercicio
        pass # No se crea Toplevel aquí

# --- Estilo para ttk (Themed Tkinter) ---
def setup_ttk_styles():
    style = ttk.Style()
    style.theme_use("clam") # Un tema moderno de ttk

    # Estilo para los labels de encabezado
    style.configure("TLabel", background="#F0FFF0", foreground="#2F4F4F")
    
    # Estilo para los botones generales
    style.configure("TButton", font=("Arial", 12), padding=8, relief="flat", background="#D4EDDA", foreground="#285C3C")
    style.map("TButton", background=[('active', '#B3E0C1')])

    # Estilo específico para los botones de "Analizar"
    style.configure("Analyze.TButton", font=("Arial", 13, "bold"), background="#87CEEB", foreground="white")
    style.map("Analyze.TButton", background=[('active', '#6495ED')])

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    setup_ttk_styles() # Configurar estilos antes de iniciar la aplicación
    app = Leccion9Grado10App(root)
    root.mainloop()
