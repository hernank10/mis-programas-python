import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

class Lesson7App:
    def __init__(self, master):
        self.master = master
        master.title("Lección 7: Refutación y Contraargumentación (11º Grado)")
        master.geometry("900x700") # Tamaño inicial de la ventana

        self.current_frame = None # Para saber qué frame está visible
        self.show_main_menu()

    def clear_frame(self):
        """Limpia todos los widgets del frame actual y crea uno nuevo."""
        if self.current_frame:
            for widget in self.current_frame.winfo_children():
                widget.destroy()
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.master, padx=25, pady=25, bg="#F0F0F0") # Un fondo claro
        self.current_frame.pack(fill="both", expand=True)

    def show_main_menu(self):
        self.clear_frame()
        self.master.title("Menú Principal - Lección 7")

        tk.Label(self.current_frame, text="Lección 7: Refutación y Contraargumentación", font=("Arial", 24, "bold"), fg="#333333", bg="#F0F0F0").pack(pady=30)

        button_style = {"font": ("Arial", 16), "width": 35, "height": 2, "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049"}

        tk.Button(self.current_frame, text="1. Aprender la Teoría", command=self.show_theory, **button_style).pack(pady=10)
        tk.Button(self.current_frame, text="2. Ver Ejemplos", command=self.show_examples, **button_style).pack(pady=10)
        tk.Button(self.current_frame, text="3. Hacer Ejercicios (Refutación)", command=self.start_exercises, **button_style).pack(pady=10)
        tk.Button(self.current_frame, text="4. Construir Mi Propio Argumento Completo", command=self.write_full_argument_with_refutation, **button_style).pack(pady=10)
        tk.Button(self.current_frame, text="5. Salir", command=self.master.quit, font=("Arial", 16), width=35, height=2, bg="#FF6347", fg="white", activebackground="#e0523e").pack(pady=20)

    def show_theory(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="Teoría: Refutación y Contraargumentación", font=("Arial", 20, "bold"), fg="#333333", bg="#F0F0F0").pack(pady=15)
        
        theory_text = """
        ¡Hola! En grados anteriores, aprendimos a construir tesis y a dar razones con evidencia.
        Hoy subiremos un nivel: vamos a aprender a **dialogar con otros argumentos**, incluso si son contrarios.

        ⭐ 1. CONTRAARGUMENTO:
           Es un argumento que se presenta para **oponerse o contradecir** una tesis o un argumento previo.
           Es pensar en '¿Qué diría alguien que no está de acuerdo conmigo?'
           Ejemplo de Tesis: 'La educación en línea es superior a la presencial.'
           Contraargumento: 'Sin embargo, la educación presencial fomenta una mejor interacción social y oportunidades de networking.'

        ⭐ 2. REFUTACIÓN:
           Es la acción de **desmentir, invalidar o demostrar la falsedad** de un argumento o contraargumento.
           No basta con presentar el contraargumento; hay que explicar por qué NO es tan fuerte o por qué tu argumento principal SIGUE SIENDO VÁLIDO a pesar de la objeción.
           Pregunta clave: '¿Por qué ese contraargumento no invalida mi tesis?'

           Ejemplo (continuando el anterior):
           Tesis: 'La educación en línea es superior a la presencial.'
           Contraargumento: 'Sin embargo, la educación presencial fomenta una mejor interacción social y oportunidades de networking.'
           Refutación: 'Si bien es cierto que la interacción física es valiosa, las plataformas en línea actuales ofrecen herramientas avanzadas de colaboración y foros que, aunque diferentes, permiten construir redes y habilidades de comunicación digital, esenciales en el mundo actual.'

        La refutación fortalece tu propio argumento porque demuestras que has considerado otras perspectivas y puedes defender tu posición de manera integral.
        """
        # Usamos ScrolledText para permitir texto más largo con scroll
        text_widget = scrolledtext.ScrolledText(self.current_frame, wrap=tk.WORD, font=("Arial", 13), height=20, width=90, bd=2, relief="groove", padx=10, pady=10)
        # Reemplazar '**' para que parezca negrita en un editor de texto plano, aunque Tkinter no renderice Markdown
        text_widget.insert(tk.END, theory_text.replace("**", "")) 
        text_widget.config(state=tk.DISABLED) # Hacerlo de solo lectura
        text_widget.pack(pady=15)

        tk.Button(self.current_frame, text="Volver al Menú", command=self.show_main_menu, font=("Arial", 14), bg="#007BFF", fg="white", activebackground="#0056b3").pack(pady=20)

    def show_examples(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="Ejemplos: Construyendo Refutaciones", font=("Arial", 20, "bold"), fg="#333333", bg="#F0F0F0").pack(pady=15)

        examples_data = [
            {
                "thesis": "Es fundamental prohibir el uso de teléfonos móviles en el aula para mejorar la concentración.",
                "counterargument": "Algunos argumentan que los móviles son herramientas útiles para la investigación y el aprendizaje.",
                "refutation": "Si bien los móviles pueden ser una herramienta, su uso incontrolado genera distracciones constantes, y las escuelas pueden proveer tabletas o computadoras con fines educativos, sin los riesgos de interrupción personal de los móviles."
            },
            {
                "thesis": "La inteligencia artificial traerá más beneficios que perjuicios a la sociedad.",
                "counterargument": "Hay quienes temen que la IA cause una pérdida masiva de empleos y una brecha social.",
                "refutation": "Aunque la IA transformará el mercado laboral, también generará nuevas profesiones y una mayor eficiencia en muchos sectores, permitiendo a los humanos enfocarse en tareas más creativas y de mayor valor si se invierte en reentrenamiento laboral."
            },
            {
                "thesis": "El consumo de carne debería reducirse globalmente por razones ambientales.",
                "counterargument": "Otros señalan que la ganadería es una fuente vital de ingresos para muchas comunidades y una parte integral de la cultura alimentaria.",
                "refutation": "Aunque la ganadería sostiene a muchas familias, existen alternativas económicas y nutricionales sostenibles, como la agricultura orgánica o las proteínas vegetales, que podrían adoptarse gradualmente para mitigar el impacto ambiental sin erradicar las tradiciones."
            }
        ]
        
        examples_frame = tk.Frame(self.current_frame, bg="#F0F0F0")
        examples_frame.pack(pady=10)

        for ex in examples_data:
            frame = tk.Frame(examples_frame, bd=2, relief="groove", padx=15, pady=15, bg="white")
            frame.pack(pady=10, fill="x")
            
            tk.Label(frame, text=f"Tesis: '{ex['thesis']}'", font=("Arial", 13, "bold"), wraplength=700, justify="left", bg="white").pack(anchor="w", pady=(0, 5))
            tk.Label(frame, text=f"  Contraargumento: '{ex['counterargument']}'", font=("Arial", 12, "italic"), wraplength=700, justify="left", bg="white", fg="darkred").pack(anchor="w", pady=(0, 5))
            tk.Label(frame, text=f"  Refutación: '{ex['refutation']}'", font=("Arial", 12), wraplength=700, justify="left", bg="white", fg="darkgreen").pack(anchor="w", pady=(0, 5))

        tk.Button(self.current_frame, text="Volver al Menú", command=self.show_main_menu, font=("Arial", 14), bg="#007BFF", fg="white", activebackground="#0056b3").pack(pady=20)

    def start_exercises(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="¡A Practicar! Refutación y Contraargumentación", font=("Arial", 20, "bold"), fg="#333333", bg="#F0F0F0").pack(pady=15)

        self.exercises = [
            {
                "thesis": "Las redes sociales han mejorado la comunicación global.",
                "counterargument": "Algunos dicen que las redes sociales aíslan a las personas y reducen la interacción cara a cara.",
                "refutation": "Si bien las interacciones presenciales son importantes, las redes sociales permiten mantener contacto con personas a distancia y facilitan la conexión con comunidades con intereses afines, superando barreras geográficas que antes eran insalvables."
            },
            {
                "thesis": "La energía solar es la mejor alternativa para el futuro energético.",
                "counterargument": "Se argumenta que la energía solar es intermitente y requiere grandes superficies para su producción.",
                "refutation": "Aunque es cierto que la producción solar depende de la luz solar y del espacio, los avances en almacenamiento de energía (baterías) y en la eficiencia de los paneles, junto con la instalación en techos y espacios no cultivables, están resolviendo estas limitaciones, haciéndola cada vez más viable."
            },
            {
                "thesis": "Es esencial que los jóvenes aprendan a programar desde temprana edad.",
                "counterargument": "Hay quienes creen que programar es una habilidad muy específica que no todos necesitan.",
                "refutation": "Si bien no todos serán programadores, aprender a programar desarrolla el pensamiento lógico, la resolución de problemas y la creatividad, habilidades transferibles y fundamentales para cualquier carrera en el siglo XXI, independientemente del campo."
            },
            {
                "thesis": "Las ciudades deberían priorizar el transporte público sobre el uso de vehículos privados.",
                "counterargument": "Algunos usuarios prefieren la comodidad y flexibilidad del coche privado.",
                "refutation": "Aunque la comodidad individual es un factor, priorizar el transporte público reduce la congestión, la contaminación y el estrés vial, beneficiando a la mayoría de los ciudadanos y haciendo las ciudades más habitables para todos."
            },
            {
                "thesis": "La inteligencia artificial no podrá reemplazar la creatividad humana.",
                "counterargument": "Se ha demostrado que la IA puede generar arte, música y textos que parecen creativos.",
                "refutation": "Si bien la IA puede imitar y recombinar patrones existentes para crear 'arte', su creatividad es algorítmica y carece de la intencionalidad, la emoción y la capacidad de experiencia subjetiva que impulsan la verdadera creatividad humana."
            },
            {
                "thesis": "Los videojuegos con fines educativos son una herramienta pedagógica muy eficaz.",
                "counterargument": "Críticos señalan que el tiempo frente a la pantalla es perjudicial para la salud y el desarrollo social.",
                "refutation": "Aunque el tiempo excesivo de pantalla es un riesgo, los videojuegos educativos, usados con moderación, aprovechan el enganche y la interactividad para enseñar de forma lúdica, mejorando la motivación y la retención de conocimientos más allá de lo que un libro de texto tradicional puede lograr."
            },
            {
                "thesis": "La exploración espacial es una inversión valiosa para la humanidad.",
                "counterargument": "Hay quienes argumentan que esos fondos deberían usarse para resolver problemas en la Tierra.",
                "refutation": "Aunque es vital abordar los problemas terrestres, la inversión en exploración espacial genera avances tecnológicos (como materiales o medicina) que benefician directamente a la vida en la Tierra, además de inspirar a futuras generaciones de científicos e ingenieros."
            },
            {
                "thesis": "El aprendizaje autodirigido (sin profesor) es más efectivo para muchos estudiantes.",
                "counterargument": "Se dice que el profesor es esencial para guiar y motivar a los estudiantes.",
                "refutation": "Si bien la guía de un profesor es útil, el aprendizaje autodirigido fomenta la autonomía, la curiosidad intrínseca y la capacidad de buscar información de forma independiente, habilidades clave para el aprendizaje continuo en la vida adulta, que un entorno puramente guiado no siempre desarrolla."
            },
            {
                "thesis": "Las dietas vegetarianas son más saludables que las que incluyen carne.",
                "counterargument": "Algunos nutricionistas advierten que una dieta vegetariana puede carecer de ciertos nutrientes si no está bien planificada.",
                "refutation": "Aunque es cierto que una dieta vegetariana requiere planificación para asegurar todos los nutrientes, una dieta balanceada basada en plantas, rica en legumbres, frutos secos y vegetales, no solo provee todos los nutrientes necesarios sino que también reduce el riesgo de enfermedades cardíacas y obesidad, superando los beneficios de una dieta omnívora promedio."
            },
            {
                "thesis": "La globalización ha beneficiado principalmente a los países desarrollados.",
                "counterargument": "Se argumenta que la globalización ha sacado a millones de personas de la pobreza en países en desarrollo.",
                "refutation": "Si bien la globalización ha impulsado el crecimiento económico en algunas regiones en desarrollo, este crecimiento a menudo ha venido acompañado de una mayor desigualdad interna, explotación laboral y degradación ambiental, con beneficios desproporcionados para las grandes corporaciones y los países más ricos."
            },
            {
                "thesis": "El voto electrónico debería implementarse para modernizar las elecciones.",
                "counterargument": "Expertos en seguridad informática advierten sobre los riesgos de manipulación y falta de transparencia del voto electrónico.",
                "refutation": "Aunque la seguridad es una preocupación legítima, con las tecnologías de encriptación y los sistemas de auditoría adecuados (como el blockchain), el voto electrónico podría ser más seguro y auditable que los sistemas manuales actuales, además de facilitar la participación y reducir costos logísticos."
            },
            {
                "thesis": "Es fundamental que los gobiernos inviertan más en arte y cultura.",
                "counterargument": "Algunos piensan que hay necesidades más urgentes, como la salud o la educación.",
                "refutation": "Si bien la salud y la educación son prioritarias, la inversión en arte y cultura no es un gasto, sino una inversión en el desarrollo integral de la sociedad. Fomenta la identidad, la creatividad, el turismo y la cohesión social, contribuyendo al bienestar tanto como los servicios básicos."
            },
            {
                "thesis": "La pena de muerte no es una medida de justicia efectiva.",
                "counterargument": "Partidarios de la pena de muerte argumentan que disuade a futuros criminales.",
                "refutation": "A pesar de la creencia en su efecto disuasorio, estudios en diversos países no han demostrado una correlación directa entre la existencia de la pena de muerte y una disminución significativa de la criminalidad, lo que sugiere que no es un factor determinante en la prevención de delitos."
            },
            {
                "thesis": "La educación universitaria debería ser gratuita para todos.",
                "counterargument": "Se objeta que la gratuidad podría saturar las universidades y bajar la calidad educativa.",
                "refutation": "Aunque la masificación es un riesgo, un sistema de universidades gratuitas y bien financiadas, con criterios de admisión claros y programas de apoyo, permitiría a más talentos acceder a la educación superior sin barreras económicas, elevando el nivel educativo general y no necesariamente la calidad."
            },
            {
                "thesis": "Las redes sociales son más perjudiciales que beneficiosas para la salud mental.",
                "counterargument": "Algunos defienden que las redes sociales ofrecen apoyo comunitario y reducen la sensación de soledad.",
                "refutation": "Si bien pueden ofrecer apoyo en ciertas situaciones, el uso problemático de las redes sociales está asociado con mayores tasas de ansiedad, depresión y baja autoestima, superando los beneficios potenciales de conexión, especialmente entre los adolescentes, debido a la presión social y la comparación constante."
            },
            {
                "thesis": "Los coches eléctricos son la solución definitiva para la crisis climática.",
                "counterargument": "Se señala que la producción de baterías y la generación de electricidad para cargarlos también tienen un impacto ambiental.",
                "refutation": "Aunque la producción de baterías y la generación de electricidad aún tienen una huella, la tendencia es hacia baterías más sostenibles y una matriz energética basada en renovables. A largo plazo, los coches eléctricos son mucho más eficientes y emiten menos gases de efecto invernadero en su ciclo de vida que los de combustión, representando una mejora neta."
            },
            {
                "thesis": "Es esencial regular estrictamente las grandes empresas tecnológicas para proteger la privacidad de los usuarios.",
                "counterargument": "Las empresas tecnológicas argumentan que la regulación excesiva frena la innovación y el desarrollo.",
                "refutation": "Si bien la innovación es importante, una regulación adecuada de la privacidad no la frena, sino que establece un marco de confianza. Sin regulación, el poder de recolección de datos de estas empresas puede llevar a abusos, discriminación y manipulación, haciendo de la protección de datos un derecho fundamental por encima de la pura 'innovación'."
            },
            {
                "thesis": "La telemedicina debería ser el estándar para la atención médica primaria.",
                "counterargument": "Se objeta que la telemedicina no permite el examen físico completo ni la conexión personal con el médico.",
                "refutation": "Aunque el examen físico y la conexión personal son valiosos, la telemedicina ofrece mayor accesibilidad (especialmente en zonas rurales), reduce tiempos de espera y costos, y es ideal para el seguimiento de enfermedades crónicas o consultas no urgentes, liberando recursos para los casos que sí requieren atención presencial."
            },
            {
                "thesis": "Los plásticos de un solo uso deberían ser prohibidos globalmente.",
                "counterargument": "La industria argumenta que los plásticos son baratos, versátiles y esenciales en muchas aplicaciones, incluyendo la higiene y la medicina.",
                "refutation": "Si bien los plásticos son útiles en ciertos contextos (como la medicina), su uso masivo en productos desechables causa una contaminación ambiental insostenible. Existen alternativas reutilizables y materiales biodegradables para la mayoría de los usos de un solo uso, lo que demuestra que su prohibición es viable y necesaria."
            },
            {
                "thesis": "El consumo de contenido digital (series, películas) es mejor que la lectura de libros.",
                "counterargument": "Los defensores de los libros argumentan que la lectura profunda estimula más la imaginación y el pensamiento crítico.",
                "refutation": "Aunque el contenido digital ofrece estimulación visual y auditiva inmediata, la lectura de libros requiere un procesamiento mental más activo, construye el vocabulario de forma más rica, y desarrolla la capacidad de concentración y el pensamiento crítico de una manera que el consumo pasivo de medios audiovisuales no puede igualar completamente, siendo habilidades complementarias pero no equivalentes."
            },
        ]

        random.shuffle(self.exercises) 
        self.current_exercise_index = 0
        self.good_refutations_count = 0
        self.total_exercises = len(self.exercises)

        self.display_exercise()

    def display_exercise(self):
        if self.current_exercise_index >= self.total_exercises:
            messagebox.showinfo("Ejercicios Terminados", 
                                f"¡Has terminado todos los ejercicios!\n"
                                f"Consideras que diste {self.good_refutations_count} refutaciones fuertes de {self.total_exercises} ejercicios.\n"
                                f"¡Sigue practicando la argumentación avanzada!")
            self.show_main_menu()
            return

        ex = self.exercises[self.current_exercise_index]
        
        exercise_frame = tk.Frame(self.current_frame, bg="#F0F0F0", bd=2, relief="groove", padx=15, pady=15)
        exercise_frame.pack(pady=10, fill="both", expand=True)

        tk.Label(exercise_frame, text=f"Ejercicio {self.current_exercise_index + 1} de {self.total_exercises}", font=("Arial", 16, "bold"), fg="#444444", bg="#F0F0F0").pack(pady=(0, 10))

        tk.Label(exercise_frame, text="Tesis:", font=("Arial", 14, "bold"), wraplength=750, justify="left", bg="#F0F0F0").pack(anchor="w")
        tk.Label(exercise_frame, text=f"'{ex['thesis']}'", font=("Arial", 13), wraplength=750, justify="left", bg="#F0F0F0").pack(anchor="w", pady=(0, 10))

        tk.Label(exercise_frame, text="Contraargumento:", font=("Arial", 14, "bold"), wraplength=750, justify="left", bg="#F0F0F0").pack(anchor="w")
        tk.Label(exercise_frame, text=f"'{ex['counterargument']}'", font=("Arial", 13, "italic"), wraplength=750, justify="left", bg="#F0F0F0", fg="darkred").pack(anchor="w", pady=(0, 10))

        tk.Label(exercise_frame, text="Tu Refutación:", font=("Arial", 14, "bold"), bg="#F0F0F0").pack(anchor="w", pady=(10, 0))
        self.user_refutation_text = scrolledtext.ScrolledText(exercise_frame, wrap=tk.WORD, font=("Arial", 12), height=6, width=80, bd=2, relief="sunken")
        self.user_refutation_text.pack(pady=(0, 10))

        self.feedback_label = tk.Label(exercise_frame, text="", font=("Arial", 12), fg="blue", bg="#F0F0F0")
        self.feedback_label.pack(pady=5)

        self.autoevaluation_var = tk.IntVar()
        
        def check_and_show_model():
            user_input = self.user_refutation_text.get("1.0", tk.END).strip()
            if not user_input:
                messagebox.showwarning("Entrada Vacía", "Por favor, escribe tu refutación antes de verificar.")
                return

            self.feedback_label.config(text=f"Refutación Modelo: '{ex['refutation']}'", fg="darkgreen", wraplength=750, justify="left")

            # Deshabilitar input y botón de verificar
            self.user_refutation_text.config(state=tk.DISABLED)
            verify_button.config(state=tk.DISABLED)

            # Mostrar opciones de autoevaluación
            tk.Label(exercise_frame, text="¿Consideras que tu refutación fue fuerte y lógica?", font=("Arial", 13, "bold"), bg="#F0F0F0").pack(pady=(10, 5))
            
            tk.Radiobutton(exercise_frame, text="Sí, creo que fue buena. 👍", variable=self.autoevaluation_var, value=1, font=("Arial", 12), bg="#F0F0F0", fg="#333333").pack(anchor="center")
            tk.Radiobutton(exercise_frame, text="No, necesito mejorarla. 👎", variable=self.autoevaluation_var, value=0, font=("Arial", 12), bg="#F0F0F0", fg="#333333").pack(anchor="center")

            next_button = tk.Button(exercise_frame, text="Siguiente Ejercicio", command=self.go_next_exercise, font=("Arial", 14), bg="#28A745", fg="white", activebackground="#218838")
            next_button.pack(pady=15)

        verify_button = tk.Button(exercise_frame, text="Verificar y Mostrar Modelo", command=check_and_show_model, font=("Arial", 14), bg="#FFC107", fg="black", activebackground="#e0a800")
        verify_button.pack(pady=10)

    def go_next_exercise(self):
        if self.autoevaluation_var.get() == 1:
            self.good_refutations_count += 1
        self.current_exercise_index += 1
        self.clear_frame() # Limpiar para el siguiente ejercicio
        self.display_exercise()

    def write_full_argument_with_refutation(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="✍️ ¡Crea un Argumento Completo con Refutación! ✍️", font=("Arial", 20, "bold"), fg="#333333", bg="#F0F0F0").pack(pady=15)
        tk.Label(self.current_frame, text="Escribe tu tesis, razón, evidencia, un contraargumento y tu refutación.", font=("Arial", 14), bg="#F0F0F0").pack(pady=5)

        form_frame = tk.Frame(self.current_frame, bg="#F0F0F0", bd=2, relief="groove", padx=15, pady=15)
        form_frame.pack(pady=10, fill="both", expand=True)

        fields = [
            ("1. Tu Tesis:", "thesis_input", 4),
            ("2. Una Razón para tu tesis:", "reason_input", 4),
            ("3. Una Evidencia para tu razón:", "evidence_input", 5),
            ("4. Un Contraargumento a tu tesis/razón:", "counterargument_input", 4),
            ("5. Tu Refutación al contraargumento:", "refutation_input", 6)
        ]

        self.input_widgets = {} # Diccionario para guardar referencias a los scrolledtext

        for label_text, id_name, height_val in fields:
            tk.Label(form_frame, text=label_text, font=("Arial", 14, "bold"), bg="#F0F0F0").pack(anchor="w", pady=(10, 0))
            text_widget = scrolledtext.ScrolledText(form_frame, wrap=tk.WORD, font=("Arial", 12), height=height_val, width=90, bd=2, relief="sunken")
            text_widget.pack(pady=(0, 10))
            self.input_widgets[id_name] = text_widget
        
        self.output_argument_label = tk.Label(form_frame, text="", font=("Arial", 12), fg="darkblue", wraplength=800, justify="left", bg="#F0F0F0")
        self.output_argument_label.pack(pady=10)

        def display_full_argument():
            thesis = self.input_widgets["thesis_input"].get("1.0", tk.END).strip()
            reason = self.input_widgets["reason_input"].get("1.0", tk.END).strip()
            evidence = self.input_widgets["evidence_input"].get("1.0", tk.END).strip()
            counterargument = self.input_widgets["counterargument_input"].get("1.0", tk.END).strip()
            refutation = self.input_widgets["refutation_input"].get("1.0", tk.END).strip()

            if not all([thesis, reason, evidence, counterargument, refutation]):
                messagebox.showwarning("Entrada Incompleta", "Por favor, completa todos los campos para construir tu argumento.")
                return

            full_arg_text = (
                f"--- Tu Argumento Construido ---\n\n"
                f"Tesis: '{thesis}'\n\n"
                f"Razón: '{reason}'\n\n"
                f"Evidencia: '{evidence}'\n\n"
                f"Contraargumento: '{counterargument}'\n\n"
                f"Refutación: '{refutation}'\n\n"
                f"¡Felicitaciones! Has construido un argumento completo y sofisticado. ¡Esta es una habilidad preuniversitaria crucial!"
            )
            self.output_argument_label.config(text=full_arg_text)

        tk.Button(self.current_frame, text="Mostrar Mi Argumento Completo", command=display_full_argument, font=("Arial", 16), bg="#6C757D", fg="white", activebackground="#5a6268").pack(pady=15)
        tk.Button(self.current_frame, text="Volver al Menú", command=self.show_main_menu, font=("Arial", 14), bg="#007BFF", fg="white", activebackground="#0056b3").pack(pady=10)

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Lesson7App(root)
    root.mainloop()
