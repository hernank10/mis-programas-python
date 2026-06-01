import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

class Lesson7App:
    def __init__(self, master):
        self.master = master
        master.title("Lección 7: Argumentación (10º Grado)")
        master.geometry("800x600") # Tamaño inicial de la ventana

        self.current_frame = None # Para saber qué frame está visible
        self.show_main_menu()

    def clear_frame(self):
        """Limpia todos los widgets del frame actual."""
        if self.current_frame:
            for widget in self.current_frame.winfo_children():
                widget.destroy()
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.master, padx=20, pady=20)
        self.current_frame.pack(fill="both", expand=True)

    def show_main_menu(self):
        self.clear_frame()
        self.master.title("Menú Principal - Lección 7")

        tk.Label(self.current_frame, text="Lección 7: Hechos, Opiniones y Evidencia", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Button(self.current_frame, text="1. Aprender la Teoría", command=self.show_theory, font=("Arial", 14), width=30, height=2).pack(pady=10)
        tk.Button(self.current_frame, text="2. Ver Ejemplos", command=self.show_examples, font=("Arial", 14), width=30, height=2).pack(pady=10)
        tk.Button(self.current_frame, text="3. Hacer Ejercicios", command=self.start_exercises, font=("Arial", 14), width=30, height=2).pack(pady=10)
        tk.Button(self.current_frame, text="4. Construir Mi Propio Argumento", command=self.write_full_argument, font=("Arial", 14), width=30, height=2).pack(pady=10)
        tk.Button(self.current_frame, text="5. Salir", command=self.master.quit, font=("Arial", 14), width=30, height=2, bg="lightcoral").pack(pady=10)

    def show_theory(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="Teoría: Hechos, Opiniones y Evidencia", font=("Arial", 18, "bold")).pack(pady=10)
        
        theory_text = """
        ¡Hola! En la argumentación, es fundamental distinguir lo que es verdad de lo que es una creencia.
        Hoy aprenderemos sobre los **hechos**, las **opiniones** y la **evidencia**.

        ⭐ 1. HECHO:
           Es una afirmación que puede ser **probada o verificada** como verdadera o falsa.
           Son datos, sucesos o realidades objetivas. No dependen de lo que alguien piense.
           Ejemplo: 'El agua hierve a 100 grados Celsius al nivel del mar.' (Se puede probar)

        ⭐ 2. OPINIÓN:
           Es una afirmación que expresa un **juicio personal**, un sentimiento o una creencia.
           No puede ser probada o desmentida objetivamente. Depende de la perspectiva de una persona.
           Ejemplo: 'El helado de chocolate es el más delicioso.' (Es un gusto personal)

        ⭐ 3. EVIDENCIA:
           Son los **datos, ejemplos, estadísticas, citas de expertos o resultados de estudios** que se usan para APOYAR una tesis o una razón.
           La evidencia convierte una opinión en un argumento más sólido, o demuestra la veracidad de un hecho.
           Ejemplo (evidencia para 'Los estudiantes con menos horas de sueño rinden menos'):
           'Un estudio de la Universidad X mostró que los alumnos que duermen menos de 7 horas obtienen un 15% menos de calificaciones en promedio.'
        """
        # Usamos ScrolledText para permitir texto más largo con scroll
        text_widget = scrolledtext.ScrolledText(self.current_frame, wrap=tk.WORD, font=("Arial", 12), height=20, width=80)
        text_widget.insert(tk.END, theory_text.replace("**", "")) # Tkinter Text widget doesn't render markdown bold directly
        text_widget.config(state=tk.DISABLED) # Hacerlo de solo lectura
        text_widget.pack(pady=10)

        tk.Button(self.current_frame, text="Volver al Menú", command=self.show_main_menu, font=("Arial", 12)).pack(pady=20)

    def show_examples(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="Ejemplos: Identificando y Usando Evidencia", font=("Arial", 18, "bold")).pack(pady=10)

        examples_data = [
            {"type": "OPINIÓN", "statement": "El rojo es el mejor color.", "explanation": "Es un gusto personal, no se puede probar."},
            {"type": "HECHO", "statement": "Bogotá es la capital de Colombia.", "explanation": "Se puede verificar en un mapa o enciclopedia."},
            {"type": "AFIRMACIÓN + EVIDENCIA",
             "statement": "El cambio climático es una realidad y afecta al planeta.",
             "evidence": "Los datos de la NASA muestran un aumento constante de la temperatura global en las últimas décadas y el derretimiento de los glaciares.",
             "explanation": "La evidencia convierte la afirmación en un argumento basado en hechos."}
        ]
        
        for ex in examples_data:
            frame = tk.Frame(self.current_frame, bd=2, relief="groove", padx=10, pady=10)
            frame.pack(pady=5, fill="x")
            
            tk.Label(frame, text=f"TIPO: {ex['type']}", font=("Arial", 12, "bold")).pack(anchor="w")
            tk.Label(frame, text=f"AFIRMACIÓN: '{ex['statement']}'", font=("Arial", 12)).pack(anchor="w")
            tk.Label(frame, text=f"Explicación: {ex['explanation']}", font=("Arial", 10, "italic")).pack(anchor="w")
            if "evidence" in ex:
                tk.Label(frame, text=f"Evidencia: {ex['evidence']}", font=("Arial", 10, "italic"), fg="blue").pack(anchor="w")

        tk.Button(self.current_frame, text="Volver al Menú", command=self.show_main_menu, font=("Arial", 12)).pack(pady=20)

    def start_exercises(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="¡A Practicar! Hechos, Opiniones y Evidencia", font=("Arial", 18, "bold")).pack(pady=10)

        self.identification_exercises = [
            {"q": "La oración 'El Sol es una estrella' es un...", "opt": ["Hecho", "Opinión"], "ans": 0, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."},
            {"q": "La oración 'Los lunes son el peor día de la semana' es una...", "opt": ["Hecho", "Opinión"], "ans": 1, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."},
            {"q": "La oración 'El agua es esencial para la vida' es un...", "opt": ["Hecho", "Opinión"], "ans": 0, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."},
            {"q": "La oración 'La lectura es aburrida' es una...", "opt": ["Hecho", "Opinión"], "ans": 1, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."},
            {"q": "La oración 'Hay 7 continentes en la Tierra' es un...", "opt": ["Hecho", "Opinión"], "ans": 0, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."},
            {"q": "La oración 'El chocolate es mejor que la vainilla' es una...", "opt": ["Hecho", "Opinión"], "ans": 1, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."},
            {"q": "La oración 'Las plantas realizan fotosíntesis' es un...", "opt": ["Hecho", "Opinión"], "ans": 0, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."},
            {"q": "La oración 'Los perros son más lindos que los gatos' es una...", "opt": ["Hecho", "Opinión"], "ans": 1, "fb_c": "¡Correcto!", "fb_i": "Incorrecto."}
        ]
        random.shuffle(self.identification_exercises)

        self.evidence_exercises = [
            {"statement": "El ejercicio físico mejora la salud.", "evidence_model": "Un estudio de la OMS (Organización Mundial de la Salud) indica que 30 minutos de actividad moderada al día reducen el riesgo de enfermedades crónicas en un 20%."},
            {"statement": "La lectura fomenta el desarrollo cognitivo en los niños.", "evidence_model": "Investigaciones de la Universidad de Oxford han demostrado que los niños que leen regularmente tienen un vocabulario más amplio y una mejor capacidad de comprensión."},
            {"statement": "El consumo excesivo de azúcar es perjudicial.", "evidence_model": "La Asociación Americana del Corazón advierte que una dieta alta en azúcares añadidos aumenta el riesgo de obesidad, diabetes tipo 2 y enfermedades cardíacas."},
            {"statement": "Aprender un nuevo idioma estimula el cerebro.", "evidence_model": "Neurocientíficos del MIT han encontrado que las personas bilingües muestran una mayor densidad de materia gris en ciertas áreas del cerebro, lo que indica un mayor desarrollo cognitivo."},
            {"statement": "El uso de pantallas antes de dormir afecta la calidad del sueño.", "evidence_model": "Estudios publicados en la revista 'Nature and Science of Sleep' revelan que la luz azul emitida por dispositivos electrónicos suprime la producción de melatonina, hormona reguladora del sueño."},
            {"statement": "La biodiversidad es crucial para la estabilidad de los ecosistemas.", "evidence_model": "Científicos del Programa de las Naciones Unidas para el Medio Ambiente han demostrado que los ecosistemas con mayor diversidad de especies son más resistentes a las perturbaciones y enfermedades."},
            {"statement": "El reciclaje reduce la contaminación ambiental.", "evidence_model": "Datos de la EPA (Agencia de Protección Ambiental de EE. UU.) muestran que el reciclaje de materiales como papel y plástico disminuye las emisiones de gases de efecto invernadero y el uso de recursos naturales."},
            {"statement": "El voluntariado mejora el bienestar emocional de las personas.", "evidence_model": "Investigaciones psicológicas de la Universidad de Harvard sugieren que las personas que realizan voluntariado experimentan niveles más bajos de estrés y una mayor satisfacción con la vida."},
            {"statement": "La educación de calidad es clave para el desarrollo económico de un país.", "evidence_model": "El Banco Mundial ha publicado informes que correlacionan directamente el nivel educativo de la población con el crecimiento del Producto Interno Bruto (PIB) y la reducción de la pobreza."},
            {"statement": "La inteligencia artificial está transformando la industria laboral.", "evidence_model": "Un informe de McKinsey & Company estima que la automatización y la IA podrían desplazar millones de empleos, pero también crear nuevas oportunidades en sectores emergentes."},
            {"statement": "El uso de transporte público reduce la huella de carbono.", "evidence_model": "Según la Agencia Europea del Medio Ambiente, optar por el transporte público en lugar del coche privado puede reducir las emisiones de CO2 en un 45% por pasajero-kilómetro."},
            {"statement": "La meditación puede disminuir los niveles de estrés.", "evidence_model": "Estudios científicos en la revista 'JAMA Internal Medicine' han demostrado que la práctica regular de la meditación de atención plena reduce significativamente los síntomas de ansiedad y depresión."}
        ]
        random.shuffle(self.evidence_exercises)

        self.current_exercise_index = 0
        self.identification_score = 0
        self.evidence_good_count = 0 # Autoevaluación del usuario

        self.show_identification_exercise()

    def show_identification_exercise(self):
        self.clear_frame()
        
        if self.current_exercise_index < len(self.identification_exercises):
            ex_data = self.identification_exercises[self.current_exercise_index]
            
            tk.Label(self.current_frame, text=f"Parte 1: Hechos u Opiniones (Pregunta {self.current_exercise_index + 1} de 8)", font=("Arial", 14, "bold")).pack(pady=10)
            tk.Label(self.current_frame, text=ex_data["q"], font=("Arial", 12)).pack(pady=10)

            self.identification_var = tk.IntVar()
            for i, opt in enumerate(ex_data["opt"]):
                tk.Radiobutton(self.current_frame, text=opt, variable=self.identification_var, value=i, font=("Arial", 12)).pack(anchor="w")
            
            def check_answer():
                if self.identification_var.get() == ex_data["ans"]:
                    messagebox.showinfo("Respuesta Correcta", ex_data["fb_c"])
                    self.identification_score += 1
                else:
                    messagebox.showerror("Respuesta Incorrecta", ex_data["fb_i"])
                
                self.current_exercise_index += 1
                self.show_identification_exercise() # Pasa al siguiente ejercicio

            tk.Button(self.current_frame, text="Verificar Respuesta", command=check_answer, font=("Arial", 12)).pack(pady=10)
        else:
            messagebox.showinfo("Parte 1 Terminada", f"¡Has terminado la Parte 1!\nTu puntuación: {self.identification_score} de 8.")
            self.current_exercise_index = 0 # Reset para la siguiente parte
            self.show_evidence_exercise()

    def show_evidence_exercise(self):
        self.clear_frame()

        if self.current_exercise_index < len(self.evidence_exercises):
            ex_data = self.evidence_exercises[self.current_exercise_index]

            tk.Label(self.current_frame, text=f"Parte 2: Añade Evidencia (Ejercicio {self.current_exercise_index + 1} de 12)", font=("Arial", 14, "bold")).pack(pady=10)
            tk.Label(self.current_frame, text=f"Afirmación: '{ex_data['statement']}'", font=("Arial", 12)).pack(pady=10)
            
            tk.Label(self.current_frame, text="Tu evidencia:", font=("Arial", 12)).pack(anchor="w")
            self.user_evidence_entry = scrolledtext.ScrolledText(self.current_frame, wrap=tk.WORD, font=("Arial", 12), height=5, width=60)
            self.user_evidence_entry.pack(pady=5)

            def reveal_model_and_evaluate():
                user_text = self.user_evidence_entry.get("1.0", tk.END).strip()
                if not user_text:
                    messagebox.showwarning("Atención", "Por favor, escribe tu evidencia antes de verificar.")
                    return

                # Mostrar la evidencia modelo
                tk.Label(self.current_frame, text="\n--- Evidencia Modelo ---", font=("Arial", 12, "bold"), fg="darkblue").pack(pady=(10,0))
                tk.Label(self.current_frame, text=f"'{ex_data['evidence_model']}'", font=("Arial", 11, "italic"), fg="blue", wraplength=600).pack()

                # Pregunta de autoevaluación
                tk.Label(self.current_frame, text="\n¿Consideras que tu evidencia es fuerte y lógica?", font=("Arial", 12)).pack(pady=5)
                self.self_evaluation_var = tk.IntVar()
                tk.Radiobutton(self.current_frame, text="Sí, creo que es buena.", variable=self.self_evaluation_var, value=1, font=("Arial", 11)).pack(anchor="w")
                tk.Radiobutton(self.current_frame, text="No, necesito mejorarla.", variable=self.self_evaluation_var, value=0, font=("Arial", 11)).pack(anchor="w")
                
                def proceed_to_next_evidence():
                    if self.self_evaluation_var.get() == 1:
                        self.evidence_good_count += 1
                    
                    self.current_exercise_index += 1
                    self.show_evidence_exercise()

                tk.Button(self.current_frame, text="Siguiente Ejercicio", command=proceed_to_next_evidence, font=("Arial", 12), bg="lightgreen").pack(pady=10)

            tk.Button(self.current_frame, text="Verificar y Autoevaluar", command=reveal_model_and_evaluate, font=("Arial", 12)).pack(pady=10)
        else:
            messagebox.showinfo("Ejercicios Terminados", 
                                f"¡Has terminado todos los ejercicios!\n"
                                f"Parte 1 (Hechos/Opiniones) correctas: {self.identification_score} de 8.\n"
                                f"Parte 2 (Tus evidencias fuertes): {self.evidence_good_count} de {len(self.evidence_exercises)}.\n"
                                f"¡Sigue practicando la argumentación!")
            self.show_main_menu()

    def write_full_argument(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="✍️ ¡Construye un Argumento Completo! ✍️", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.current_frame, text="Escribe una Tesis, una Razón y una Evidencia para un tema de tu interés.", font=("Arial", 12)).pack(pady=5)

        tk.Label(self.current_frame, text="1. Tu Tesis:", font=("Arial", 12, "bold")).pack(anchor="w")
        self.thesis_entry = scrolledtext.ScrolledText(self.current_frame, wrap=tk.WORD, font=("Arial", 12), height=3, width=70)
        self.thesis_entry.pack(pady=5)

        tk.Label(self.current_frame, text="2. Una Razón (porque...):", font=("Arial", 12, "bold")).pack(anchor="w")
        self.reason_entry = scrolledtext.ScrolledText(self.current_frame, wrap=tk.WORD, font=("Arial", 12), height=3, width=70)
        self.reason_entry.pack(pady=5)

        tk.Label(self.current_frame, text="3. Una Evidencia (dato, estudio, ejemplo):", font=("Arial", 12, "bold")).pack(anchor="w")
        self.evidence_entry = scrolledtext.ScrolledText(self.current_frame, wrap=tk.WORD, font=("Arial", 12), height=5, width=70)
        self.evidence_entry.pack(pady=5)

        def display_argument():
            thesis = self.thesis_entry.get("1.0", tk.END).strip()
            reason = self.reason_entry.get("1.0", tk.END).strip()
            evidence = self.evidence_entry.get("1.0", tk.END).strip()

            if not thesis or not reason or not evidence:
                messagebox.showwarning("Entrada Incompleta", "Por favor, completa todos los campos (Tesis, Razón, Evidencia).")
                return

            # Crear una nueva ventana para mostrar el argumento completo
            arg_window = tk.Toplevel(self.master)
            arg_window.title("Tu Argumento Completo")
            arg_window.geometry("500x350")
            
            tk.Label(arg_window, text="¡Has construido un argumento sólido!", font=("Arial", 14, "bold"), fg="darkgreen").pack(pady=10)
            tk.Label(arg_window, text="Tesis:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
            tk.Label(arg_window, text=thesis, font=("Arial", 11), wraplength=480, justify="left").pack(anchor="w", padx=10)
            
            tk.Label(arg_window, text="\nRazón:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
            tk.Label(arg_window, text=reason, font=("Arial", 11), wraplength=480, justify="left").pack(anchor="w", padx=10)
            
            tk.Label(arg_window, text="\nEvidencia:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10)
            tk.Label(arg_window, text=evidence, font=("Arial", 11), wraplength=480, justify="left").pack(anchor="w", padx=10)
            
            tk.Button(arg_window, text="Cerrar", command=arg_window.destroy, font=("Arial", 12)).pack(pady=15)


        tk.Button(self.current_frame, text="Mostrar Mi Argumento", command=display_argument, font=("Arial", 14), bg="lightblue").pack(pady=20)
        tk.Button(self.current_frame, text="Volver al Menú", command=self.show_main_menu, font=("Arial", 12)).pack(pady=10)


# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Lesson7App(root)
    root.mainloop()
