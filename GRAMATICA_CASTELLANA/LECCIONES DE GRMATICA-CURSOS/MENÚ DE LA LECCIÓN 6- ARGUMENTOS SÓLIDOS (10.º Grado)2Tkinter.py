import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

class ArgumentLessonApp:
    def __init__(self, master):
        self.master = master
        master.title("Lección 6: Construyendo Argumentos Sólidos (10.º Grado)")
        master.geometry("800x600")
        master.resizable(False, False) # Optional: prevent window resizing

        self.create_menu()
        self.show_main_page()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        lesson_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Lección", menu=lesson_menu)
        lesson_menu.add_command(label="Teoría", command=self.show_theory)
        lesson_menu.add_command(label="Ejemplos", command=self.show_examples)
        lesson_menu.add_command(label="Ejercicios", command=self.start_exercises)
        lesson_menu.add_command(label="Construye Tu Propio Argumento", command=self.show_build_argument)
        lesson_menu.add_separator()
        lesson_menu.add_command(label="Salir", command=self.master.quit)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_menu() # Re-add menu after clearing

    def show_main_page(self):
        self.clear_frame()
        
        main_label = tk.Label(self.master, text="¡Bienvenido a la Lección 6!\nConstruyendo Argumentos Sólidos (10.º Grado)", font=("Arial", 18, "bold"), pady=20)
        main_label.pack()

        info_label = tk.Label(self.master, text="Usa el menú 'Lección' para navegar:\n\n"
                                               "📚 Teoría: Aprende sobre la estructura de un argumento.\n"
                                               "💡 Ejemplos: Ve argumentos bien hechos.\n"
                                               "📝 Ejercicios: ¡Practica identificando las partes!\n"
                                               "✍️ Construye Tu Propio Argumento: ¡Crea tus ideas sólidas!",
                                               font=("Arial", 12), justify=tk.LEFT)
        info_label.pack(pady=10)
        
        start_button = tk.Button(self.master, text="Empezar Lección", command=self.show_theory, font=("Arial", 14), bg="#4CAF50", fg="white")
        start_button.pack(pady=20)

    def show_theory(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="📚 TEORÍA: LA ESTRUCTURA DE UN ARGUMENTO SÓLIDO 📚", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        theory_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=70, height=25)
        theory_text.pack(pady=10, padx=20)
        
        theory_content = """
1. **La Arquitectura del Razonamiento: ¿Cómo se construye un argumento sólido?** 🤔
   En grados anteriores, aprendimos que una opinión necesita razones (argumentos) y pruebas (evidencias). Ahora, vamos a darle una **estructura formal** a esas ideas, algo esencial para ensayos, debates y cualquier texto persuasivo.
   Piensa en un argumento como un edificio bien construido: necesita un plano principal (la tesis), pilares fuertes (los argumentos de apoyo) y un buen techo que lo cierre (la conclusión).

2. **La TESIS: El Corazón de tu Argumento** ❤️
   La **TESIS** es la **idea central, la postura principal** que quieres defender o probar en tu texto. ¡Es la afirmación clave sobre la que girará toda tu argumentación!
   - Debe ser una oración **completa, clara, específica y debatible** (alguien podría estar en desacuerdo).
   - **❌ Mal ejemplo de Tesis:** 'Los animales son importantes.' (Demasiado general, no debatible).
   - **✅ Buen ejemplo de Tesis:** 'La implementación de programas de reciclaje obligatorio es crucial para la sostenibilidad ambiental urbana.' (Clara, específica, se puede debatir).

3. **ARGUMENTOS DE APOYO: Los Pilares del Razonamiento** 💪
   Los **ARGUMENTOS DE APOYO** son las **razones principales** que utilizas para sustentar tu tesis. Cada argumento de apoyo es una afirmación que, si se prueba con evidencias, fortalece tu tesis.
   - Piensa en ellos como los 'porqués' de tu tesis. Puedes usar argumentos lógicos, de autoridad o de experiencia.
   - **Ejemplo (para la tesis 'La implementación de programas de reciclaje obligatorio es crucial para la sostenibilidad ambiental urbana'):**
     - **Argumento 1:** 'Reduce significativamente la cantidad de residuos que llegan a los vertederos.'
     - **Argumento 2:** 'Fomenta la economía circular al dar nueva vida a los materiales.'
     - **Argumento 3:** 'Disminuye el consumo de recursos naturales y la energía necesaria para producir nuevos materiales.'
   - ¡Recuerda! Cada argumento de apoyo debe ser, a su vez, sustentado con **evidencias** (datos, ejemplos, citas de expertos).

4. **La CONCLUSIÓN: Cerrando con Fuerza** 💥
   La **CONCLUSIÓN** es la parte final de tu argumentación donde **reafirmas tu tesis principal** de una manera fresca y convincente. A veces, también puedes resumir brevemente tus argumentos más importantes.
   - No es solo repetir la tesis al pie de la letra, sino darle un cierre que deje una impresión duradera en el lector/oyente.
   - **Ejemplo (para la tesis de reciclaje):** 'En resumen, considerando la reducción de residuos, el impulso a la economía circular y la conservación de recursos, resulta innegable que la obligatoriedad del reciclaje es una medida fundamental para asegurar un futuro urbano más sostenible y responsable.'
   - La conclusión debe dejar al público con una idea clara y reforzada de tu postura.
"""
        theory_text.insert(tk.END, theory_content)
        theory_text.config(state=tk.DISABLED) # Make text read-only

    def show_examples(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="💡 EJEMPLOS: ARGUMENTOS SÓLIDOS EN ACCIÓN 💡", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        examples_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=70, height=25)
        examples_text.pack(pady=10, padx=20)

        examples_content = """
**Ejemplo 1: La importancia de aprender un segundo idioma.**
 - **TESIS:** Aprender un segundo idioma desde la infancia ofrece beneficios cognitivos y culturales invaluables para los estudiantes.
 - **ARGUMENTO DE APOYO 1:** Mejora las habilidades cognitivas como la resolución de problemas y la multitarea.
 - **ARGUMENTO DE APOYO 2:** Permite una mayor apreciación y comprensión de diferentes culturas y perspectivas.
 - **CONCLUSIÓN:** Por lo tanto, integrar la enseñanza de un segundo idioma desde temprana edad es esencial para desarrollar mentes más ágiles y ciudadanos globales más empáticos.

---

**Ejemplo 2: ¿Deberían prohibirse los deberes escolares en primaria?**
 - **TESIS:** Prohibir los deberes escolares en la educación primaria beneficiaría el bienestar y el desarrollo integral de los niños.
 - **ARGUMENTO DE APOYO 1:** Reduce el estrés y la presión académica excesiva en los niños pequeños.
 - **ARGUMENTO DE APOYO 2:** Permite más tiempo para actividades extracurriculares, juego libre y tiempo en familia.
 - **CONCLUSIÓN:** En consecuencia, al eliminar los deberes en primaria, se fomenta un equilibrio más saludable entre la vida escolar y personal de los niños, promoviendo un desarrollo más completo y feliz.
"""
        examples_text.insert(tk.END, examples_content)
        examples_text.config(state=tk.DISABLED) # Make text read-only

    def start_exercises(self):
        self.exercises = [
            {"pasaje": "Es vital que los gobiernos inviertan más en energía solar. **Esta fuente de energía es limpia y renovable.** Además, reduce la dependencia de los combustibles fósiles. Por todo esto, la inversión en energía solar es una prioridad.", "destacado": "Esta fuente de energía es limpia y renovable.", "respuesta": "argumento de apoyo", "pista": "Es una razón que defiende la inversión en energía solar."},
            {"pasaje": "**Los videojuegos desarrollan habilidades de resolución de problemas en los jóvenes.** Esto se debe a que muchos juegos requieren estrategia y pensamiento crítico. Además, fomentan la creatividad al permitir la construcción de mundos virtuales. Por tanto, su potencial educativo es innegable.", "destacado": "Los videojuegos desarrollan habilidades de resolución de problemas en los jóvenes.", "respuesta": "tesis", "pista": "Es la idea principal que se va a defender en el texto."},
            {"pasaje": "La prohibición de los plásticos de un solo uso es crucial. **Ayuda a proteger la vida marina y los ecosistemas acuáticos.** También disminuye la acumulación de basura. En definitiva, esta medida es fundamental para la salud de nuestro planeta.", "destacado": "Ayuda a proteger la vida marina y los ecosistemas acuáticos.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica para la prohibición de plásticos."},
            {"pasaje": "El voluntariado en la comunidad trae grandes beneficios. Fomenta el sentido de pertenencia y mejora la autoestima. **En resumen, participar en actividades de voluntariado es una forma efectiva de construir una sociedad más solidaria y un bienestar personal.**", "destacado": "En resumen, participar en actividades de voluntariado es una forma efectiva de construir una sociedad más solidaria y un bienestar personal.", "respuesta": "conclusion", "pista": "Es la frase que cierra y resume la idea principal."},
            {"pasaje": "**El aprendizaje de idiomas extranjeros debería ser obligatorio desde la escuela primaria.** Esto se debe a que mejora la agilidad mental. También abre puertas a oportunidades culturales y laborales. Por ende, es una inversión a largo plazo.", "destacado": "El aprendizaje de idiomas extranjeros debería ser obligatorio desde la escuela primaria.", "respuesta": "tesis", "pista": "Es la afirmación principal que se defiende."},
            {"pasaje": "El uso excesivo de redes sociales puede tener efectos negativos en la salud mental de los adolescentes. **Puede aumentar sentimientos de ansiedad y depresión.** Además, distorsiona la percepción de la realidad. En conclusión, es necesario un uso consciente.", "destacado": "Puede aumentar sentimientos de ansiedad y depresión.", "respuesta": "argumento de apoyo", "pista": "Es una de las razones que explican los efectos negativos."},
            {"pasaje": "La lectura regular es fundamental para el desarrollo intelectual. Amplía el vocabulario y mejora la comprensión. **Por lo tanto, fomentar el hábito de la lectura desde temprana edad es crucial para formar individuos críticos y bien informados.**", "destacado": "Por lo tanto, fomentar el hábito de la lectura desde temprana edad es crucial para formar individuos críticos y bien informados.", "respuesta": "conclusion", "pista": "La frase final que resume y concluye el argumento."},
            {"pasaje": "**La educación pública de calidad es un pilar fundamental para el progreso de una nación.** Garantiza igualdad de oportunidades para todos los ciudadanos. Además, invierte en el capital humano del país. Por estas razones, es una prioridad.", "destacado": "La educación pública de calidad es un pilar fundamental para el progreso de una nación.", "respuesta": "tesis", "pista": "Es la afirmación central que se argumenta."},
            {"pasaje": "El transporte público eficiente es vital para las grandes ciudades. **Reduce la congestión del tráfico y la contaminación del aire.** También es más económico para los ciudadanos. En definitiva, mejora la calidad de vida urbana.", "destacado": "Reduce la congestión del tráfico y la contaminación del aire.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica por la que el transporte público es vital."},
            {"pasaje": "El arte debe ser accesible para todos. Promueve la creatividad y la expresión personal. **En consecuencia, las políticas públicas deben asegurar el acceso universal a museos y exposiciones.**", "destacado": "En consecuencia, las políticas públicas deben asegurar el acceso universal a museos y exposiciones.", "respuesta": "conclusion", "pista": "Sintetiza la idea y propone una acción basada en los argumentos."},
            {"pasaje": "**El voluntariado debería ser una actividad obligatoria en la secundaria.** Fomenta la empatía y la responsabilidad social. Además, permite a los jóvenes adquirir nuevas habilidades. Su impacto positivo es evidente.", "destacado": "El voluntariado debería ser una actividad obligatoria en la secundaria.", "respuesta": "tesis", "pista": "Es la postura principal del argumento."},
            {"pasaje": "Invertir en tecnología educativa en las aulas es esencial. **Prepara a los estudiantes para el mundo digital del futuro.** También personaliza el aprendizaje. Por ende, modernizar las herramientas es clave.", "destacado": "Prepara a los estudiantes para el mundo digital del futuro.", "respuesta": "argumento de apoyo", "pista": "Es una razón que apoya la inversión en tecnología."},
            {"pasaje": "El deporte profesional fomenta valores positivos. **Inspira a la juventud a llevar vidas activas y saludables.** Genera trabajo y promueve el turismo deportivo. Claramente, su impacto social es significativo.", "destacado": "Inspira a la juventud a llevar vidas activas y saludables.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica de los beneficios del deporte."},
            {"pasaje": "Las dietas veganas son una opción sostenible y ética. **Reducen la huella de carbono y el consumo de agua asociado a la ganadería.** Además, evitan el maltrato animal. Por eso, son una elección consciente.", "destacado": "Reducen la huella de carbono y el consumo de agua asociado a la ganadería.", "respuesta": "argumento de apoyo", "pista": "Es una razón específica para la sostenibilidad."},
            {"pasaje": "La pena de muerte no es una medida justa ni efectiva. No disuade el crimen y es irreversible en caso de error. **Por lo tanto, se deben buscar alternativas que promuevan la justicia restaurativa y la rehabilitación.**", "destacado": "Por lo tanto, se deben buscar alternativas que promuevan la justicia restaurativa y la rehabilitación.", "respuesta": "conclusion", "pista": "Es la frase final que propone una acción o reafirma la postura."},
            {"pasaje": "**El acceso a internet debería ser considerado un derecho humano básico.** Permite el acceso a la información y la educación. También facilita la comunicación y la participación ciudadana. Su universalidad es vital.", "destacado": "El acceso a internet debería ser considerado un derecho humano básico.", "respuesta": "tesis", "pista": "Es la afirmación principal que se defiende."},
            {"pasaje": "La crisis climática requiere acciones urgentes. **Las emisiones de gases de efecto invernadero están calentando el planeta a un ritmo alarmante.** Esto está causando desastres naturales más frecuentes. Es imperativo actuar ya.", "destacado": "Las emisiones de gases de efecto invernadero están calentando el planeta a un ritmo alarmante.", "respuesta": "argumento de apoyo", "pista": "Es una razón que explica por qué la crisis es urgente."},
            {"pasaje": "La robótica avanzada traerá grandes cambios al mercado laboral. **Creará nuevos empleos en áreas de tecnología y mantenimiento.** Sin embargo, también automatizará tareas repetitivas. En suma, requerirá una adaptación constante.", "destacado": "Creará nuevos empleos en áreas de tecnología y mantenimiento.", "respuesta": "argumento de apoyo", "pista": "Es una de las razones sobre el impacto de la robótica."},
            {"pasaje": "Es fundamental que las ciudades promuevan espacios verdes. **Mejoran la calidad del aire y reducen el estrés de los ciudadanos.** Además, fomentan la biodiversidad. En definitiva, son esenciales para el bienestar urbano.", "destacado": "Mejoran la calidad del aire y reducen el estrés de los ciudadanos.", "respuesta": "argumento de apoyo", "pista": "Es una de las razones que justifican la importancia de los espacios verdes."},
            {"pasaje": "La inteligencia artificial tiene el potencial de revolucionar la medicina. Puede ayudar a diagnosticar enfermedades con mayor precisión y a desarrollar nuevos tratamientos. **En conclusión, la IA es una herramienta prometedora para el futuro de la salud.**", "destacado": "En conclusión, la IA es una herramienta prometedora para el futuro de la salud.", "respuesta": "conclusion", "pista": "La frase final que resume y reafirma el potencial de la IA."},
        ]
        random.shuffle(self.exercises)
        self.current_exercise_index = 0
        self.score = 0
        self.total_exercises = len(self.exercises)
        
        self.display_exercise()

    def display_exercise(self):
        self.clear_frame()
        
        if self.current_exercise_index >= self.total_exercises:
            self.show_exercise_results()
            return

        exercise = self.exercises[self.current_exercise_index]

        title_label = tk.Label(self.master, text=f"📝 EJERCICIO {self.current_exercise_index + 1}/{self.total_exercises}: Identifica la Estructura", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        passage_label = tk.Label(self.master, text=f"Pasaje: {exercise['pasaje']}", wraplength=700, justify=tk.LEFT, font=("Arial", 12))
        passage_label.pack(pady=5, padx=20)
        
        highlighted_label = tk.Label(self.master, text=f"Frase destacada: {exercise['destacado']}", wraplength=700, justify=tk.LEFT, font=("Arial", 12, "italic"), fg="blue")
        highlighted_label.pack(pady=5, padx=20)

        question_label = tk.Label(self.master, text="¿Qué parte de la estructura argumentativa es?", font=("Arial", 12), pady=10)
        question_label.pack()

        self.choice_var = tk.StringVar(self.master)
        self.choice_var.set("") # Clear previous selection

        options = ["TESIS", "ARGUMENTO DE APOYO", "CONCLUSIÓN"]
        for option in options:
            rb = tk.Radiobutton(self.master, text=option, variable=self.choice_var, value=option.lower(), font=("Arial", 11))
            rb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(self.master, text="Comprobar", command=self.check_exercise, font=("Arial", 12), bg="#008CBA", fg="white")
        submit_button.pack(pady=15)

    def check_exercise(self):
        selected_answer = self.choice_var.get()
        correct_answer = self.exercises[self.current_exercise_index]['respuesta']
        pista = self.exercises[self.current_exercise_index]['pista']

        if not selected_answer:
            messagebox.showwarning("Atención", "Por favor, selecciona una opción antes de comprobar.")
            return

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("¡Correcto!", "✅ ¡Identificaste bien esa parte!")
        else:
            messagebox.showerror("¡Incorrecto!", f"❌ ¡Incorrecto! La respuesta correcta era: '{correct_answer.upper()}'.\nPista: {pista}")
        
        self.current_exercise_index += 1
        self.display_exercise()

    def show_exercise_results(self):
        self.clear_frame()
        
        results_label = tk.Label(self.master, text="--- ¡FIN DE LOS EJERCICIOS! ---", font=("Arial", 16, "bold"), pady=10)
        results_label.pack()

        score_label = tk.Label(self.master, text=f"Tu puntuación final es: {self.score}/{self.total_exercises}!", font=("Arial", 14), pady=10)
        score_label.pack()

        if self.score >= self.total_exercises * 0.8:
            message = "🎉 ¡Felicidades! ¡Eres un arquitecto de argumentos sólidos!"
        elif self.score >= self.total_exercises * 0.5:
            message = "👍 ¡Muy bien! Ya entiendes las partes clave de un argumento."
        else:
            message = "✍️ ¡Sigue practicando! Con más esfuerzo, ¡estructurarás tus ideas como un experto!"
        
        feedback_label = tk.Label(self.master, text=message, font=("Arial", 12), pady=10)
        feedback_label.pack()

        back_button = tk.Button(self.master, text="Volver al Menú Principal", command=self.show_main_page, font=("Arial", 12), bg="#4CAF50", fg="white")
        back_button.pack(pady=20)

    def show_build_argument(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="✍️ ¡CONSTRUYE TU PROPIO ARGUMENTO COMPLETO! ✍️", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        instruction_label = tk.Label(self.master, text="Ahora es tu turno de construir un argumento sólido con todas sus partes.\n"
                                                      "Piensa en un tema que te interese y sobre el que tengas una postura clara.",
                                                      wraplength=700, justify=tk.LEFT, font=("Arial", 12))
        instruction_label.pack(pady=10, padx=20)

        # Thesis
        tk.Label(self.master, text="1. Tu TESIS (Postura Principal):", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=20, pady=(10,0))
        self.thesis_entry = scrolledtext.ScrolledText(self.master, height=2, width=80, font=("Arial", 11), wrap=tk.WORD)
        self.thesis_entry.pack(padx=20)

        # Argument 1
        tk.Label(self.master, text="2. ARGUMENTO DE APOYO 1:", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=20, pady=(10,0))
        self.arg1_entry = scrolledtext.ScrolledText(self.master, height=2, width=80, font=("Arial", 11), wrap=tk.WORD)
        self.arg1_entry.pack(padx=20)

        # Argument 2
        tk.Label(self.master, text="3. ARGUMENTO DE APOYO 2:", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=20, pady=(10,0))
        self.arg2_entry = scrolledtext.ScrolledText(self.master, height=2, width=80, font=("Arial", 11), wrap=tk.WORD)
        self.arg2_entry.pack(padx=20)

        # Conclusion
        tk.Label(self.master, text="4. Tu CONCLUSIÓN:", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=20, pady=(10,0))
        self.conclusion_entry = scrolledtext.ScrolledText(self.master, height=3, width=80, font=("Arial", 11), wrap=tk.WORD)
        self.conclusion_entry.pack(padx=20)

        submit_button = tk.Button(self.master, text="Mostrar Mi Argumento", command=self.display_user_argument, font=("Arial", 14), bg="#008CBA", fg="white")
        submit_button.pack(pady=20)

    def display_user_argument(self):
        thesis = self.thesis_entry.get("1.0", tk.END).strip()
        arg1 = self.arg1_entry.get("1.0", tk.END).strip()
        arg2 = self.arg2_entry.get("1.0", tk.END).strip()
        conclusion = self.conclusion_entry.get("1.0", tk.END).strip()

        if not all([thesis, arg1, arg2, conclusion]):
            messagebox.showwarning("Campos Incompletos", "Por favor, completa todas las partes de tu argumento.")
            return

        self.clear_frame()
        
        results_label = tk.Label(self.master, text="--- ¡TU ARGUMENTO CONSTRUIDO! ---", font=("Arial", 16, "bold"), pady=10)
        results_label.pack()

        argument_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=70, height=20)
        argument_display.pack(pady=10, padx=20)

        display_content = f"""
**TESIS:** {thesis}

**ARGUMENTO DE APOYO 1:** {arg1}

**ARGUMENTO DE APOYO 2:** {arg2}

**CONCLUSIÓN:** {conclusion}
"""
        argument_display.insert(tk.END, display_content)
        argument_display.config(state=tk.DISABLED) # Make text read-only

        back_button = tk.Button(self.master, text="Volver al Menú Principal", command=self.show_main_page, font=("Arial", 12), bg="#4CAF50", fg="white")
        back_button.pack(pady=20)


def start_app():
    root = tk.Tk()
    app = ArgumentLessonApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_app()
