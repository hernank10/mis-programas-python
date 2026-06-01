import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

class FalacyLessonApp:
    def __init__(self, master):
        self.master = master
        master.title("Lección 6: ¡Detectando Falacias! (11.º Grado)")
        master.geometry("900x700") # A bit larger for more content
        master.resizable(False, False) 

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
        lesson_menu.add_command(label="Practicar Refutación", command=self.start_refutation_practice)
        lesson_menu.add_separator()
        lesson_menu.add_command(label="Salir", command=self.master.quit)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_menu() # Re-add menu after clearing

    def show_main_page(self):
        self.clear_frame()
        
        main_label = tk.Label(self.master, text="¡Bienvenido a la Lección 6!\n¡Detectando Trampas en la Argumentación! (11.º Grado)", font=("Arial", 18, "bold"), pady=20)
        main_label.pack()

        info_label = tk.Label(self.master, text="Usa el menú 'Lección' para navegar:\n\n"
                                               "📚 Teoría: Aprende qué son y cuáles son las falacias comunes.\n"
                                               "💡 Ejemplos: Ve cómo lucen las falacias en la práctica.\n"
                                               "📝 Ejercicios: ¡Practica identificando tipos de falacias!\n"
                                               "✍️ Practicar Refutación: ¡Aprende a desarmar falacias!",
                                               font=("Arial", 12), justify=tk.LEFT)
        info_label.pack(pady=10)
        
        start_button = tk.Button(self.master, text="Empezar Lección", command=self.show_theory, font=("Arial", 14), bg="#FFD700", fg="black")
        start_button.pack(pady=20)

    def show_theory(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="📚 TEORÍA: ARGUMENTOS DESHONESTOS - FALACIAS COMUNES 📚", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        theory_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=90, height=30)
        theory_text.pack(pady=10, padx=20)
        
        theory_content = """
**1. El Poder y los Peligros de la Persuasión** 🤔
   Ya sabemos cómo construir argumentos sólidos. Pero, ¿qué pasa cuando alguien intenta convencernos usando trucos o razonamientos defectuosos? A esto le llamamos **falacias**.
   Una **falacia** es un argumento que parece válido o convincente a primera vista, pero que en realidad esconde un **error lógico** o una intención de engañar. Identificarlas es crucial para nuestro pensamiento crítico.

**2. Explorando Falacias Comunes** 🚨

   **a. Ad Hominem (Ataque Personal):**
      - **Explicación:** Atacar a la **persona** que presenta el argumento, en lugar de refutar el argumento mismo.
      - **Ejemplo:** "No podemos creer lo que dice el científico sobre el cambio climático; ¡él solo busca fama!" (En lugar de discutir sus datos o teorías).

   **b. Ad Populum (Apelación a la Popularidad o al Pueblo):**
      - **Explicación:** Afirmar que algo es verdadero o correcto solo porque **muchas personas lo creen o lo hacen**. La popularidad no es prueba de verdad.
      - **Ejemplo:** "Millones de personas usan esta red social, así que debe ser la mejor para conectar con amigos." (La popularidad no garantiza que sea la 'mejor' para todos o que sea segura).

   **c. Falsa Causa (Post Hoc, Ergo Propter Hoc):**
      - **Explicación:** Suponer que porque un evento ocurrió **después** de otro, el primero debe ser la **causa** del segundo. (Correlación no implica causalidad).
      - **Ejemplo:** "Desde que prohibieron los patinetes eléctricos en el parque, ha llovido más. La prohibición causó el mal tiempo." (Absurdo, pero ilustra la idea).

   **d. Generalización Apresurada:**
      - **Explicación:** Llegar a una **conclusión general basándose en evidencia insuficiente** o en muy pocos casos particulares.
      - **Ejemplo:** "Probé un plato de comida de este restaurante y no me gustó; toda su comida debe ser horrible." (Un solo plato no define la calidad de todo el menú).

   **e. Petición de Principio (Argumento Circular):**
      - **Explicación:** La **conclusión del argumento ya está implícita o explícitamente contenida en una de las premisas**. Se asume como verdad lo que se quiere probar.
      - **Ejemplo:** "El ejercicio físico es bueno porque mejora la salud. Y ¿por qué mejora la salud? Porque es bueno hacer ejercicio." (No se añade información, se repite la idea).

   **f. Hombre de Paja:**
      - **Explicación:** **Distorsionar, exagerar o crear una versión débil** del argumento del oponente para que sea más fácil de atacar o refutar, en lugar de debatir la postura real.
      - **Ejemplo:**
         - **Persona A:** "Deberíamos invertir en energías renovables para un futuro más sostenible."
         - **Persona B:** "Ah, ¿así que quieres destruir nuestra economía y dejar a miles de personas sin trabajo en la industria petrolera? ¡Eso es irresponsable!" (B distorsiona la propuesta de A).

   **g. Pendiente Resbaladiza:**
      - **Explicación:** Afirmar que una **acción inicial inevitablemente conducirá a una serie de consecuencias negativas y extremas**, sin suficiente evidencia para cada paso de la cadena.
      - **Ejemplo:** "Si permitimos que los estudiantes usen teléfonos en el aula, pronto no prestarán atención, sus notas bajarán, abandonarán la escuela y terminarán sin futuro." (Una cadena de eventos exagerada e infundada).

   **h. Ad Ignorantiam (Apelación a la Ignorancia):**
      - **Explicación:** Afirmar que algo es verdadero porque **no se ha probado que sea falso**, o viceversa. La ausencia de prueba no es una prueba.
      - **Ejemplo:** "Nadie ha podido demostrar que los ovnis no nos visitan, por lo tanto, las visitas extraterrestres son una realidad." (La falta de evidencia en contra no prueba que sea cierto).
"""
        theory_text.insert(tk.END, theory_content)
        theory_text.config(state=tk.DISABLED) # Make text read-only

    def show_examples(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="💡 EJEMPLOS: ¡IDENTIFICANDO FALACIAS! 💡", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        examples_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=90, height=30)
        examples_text.pack(pady=10, padx=20)

        examples_content = """
**Ejemplo 1:** "No podemos confiar en la opinión del Dr. López sobre la vacuna, ¡él siempre ha sido un poco excéntrico y vive aislado!"
 - **Tipo de Falacia:** **Ad Hominem**. Se ataca la personalidad del Dr. López, no la validez de su argumento sobre la vacuna.

---

**Ejemplo 2:** "Todo el mundo en mi clase piensa que las clases a las 7 AM son una tortura, así que deben eliminarlas del horario escolar."
 - **Tipo de Falacia:** **Ad Populum**. La opinión popular de un grupo (la clase) no justifica una medida educativa.

---

**Ejemplo 3:** "Después de que mi equipo de fútbol empezó a usar uniformes verdes, ganaron todos sus partidos. ¡Los uniformes verdes les dan suerte!"
 - **Tipo de Falacia:** **Falsa Causa**. Se asume que el color del uniforme es la causa de las victorias sin una conexión lógica real.

---

**Ejemplo 4:** "Conocí a dos políticos que eran corruptos, por lo tanto, todos los políticos son corruptos."
 - **Tipo de Falacia:** **Generalización Apresurada**. Se saca una conclusión general sobre una profesión entera basándose en solo dos ejemplos.

---

**Ejemplo 5:** "La libertad de expresión es fundamental porque es esencial para una sociedad libre."
 - **Tipo de Falacia:** **Petición de Principio**. La conclusión ("es esencial para una sociedad libre") es básicamente una reafirmación de la premisa ("la libertad de expresión es fundamental"). No se aporta nueva información.

---

**Ejemplo 6:**
  - **Persona A:** "Deberíamos considerar implementar un sistema de transporte público más robusto para reducir el uso de autos."
  - **Persona B:** "Así que lo que quieres es obligar a todos a usar buses lentos y sucios, y eliminar los autos privados. ¡Eso es una dictadura!"
 - **Tipo de Falacia:** **Hombre de Paja**. La Persona B distorsiona el argumento de la Persona A a una posición extrema y fácilmente atacable que no fue la original.

---

**Ejemplo 7:** "Si le das un dulce a un niño cada vez que llora, pronto esperará dulces todo el tiempo, luego exigirá más y más, y terminará siendo un adulto caprichoso y malcriado que no puede lidiar con la frustración."
 - **Tipo de Falacia:** **Pendiente Resbaladiza**. Se exagera una pequeña acción inicial (un dulce) hasta una serie de consecuencias extremas y negativas sin suficiente justificación.

---

**Ejemplo 8:** "No hay pruebas de que exista vida inteligente en otros planetas, por lo tanto, no existe."
 - **Tipo de Falacia:** **Ad Ignorantiam**. La ausencia de prueba no es una prueba de inexistencia.
"""
        examples_text.insert(tk.END, examples_content)
        examples_text.config(state=tk.DISABLED) # Make text read-only

    def start_exercises(self):
        self.exercises = [
            {"falacia": "El candidato a la alcaldía no debería hablar de educación, ¡si él ni siquiera terminó la universidad!", "tipo": "Ad Hominem", "pista": "Ataca a la persona, no a sus ideas."},
            {"falacia": "La mayoría de la gente en mi ciudad piensa que el nuevo centro comercial es lo mejor, así que no puede ser malo para los pequeños negocios.", "tipo": "Ad Populum", "pista": "Basado en la popularidad, no en hechos económicos."},
            {"falacia": "Desde que me compré zapatillas nuevas, he corrido más rápido. Las zapatillas nuevas son la causa de mi mejora.", "tipo": "Falsa Causa", "pista": "Confunde correlación con causalidad."},
            {"falacia": "Probé dos restaurantes en esta ciudad y ambos eran caros. Por lo tanto, comer aquí es muy costoso.", "tipo": "Generalización Apresurada", "pista": "Saca una conclusión amplia de pocos ejemplos."},
            {"falacia": "Dios es real porque lo dice la fe, y la fe es creer en lo que es real.", "tipo": "Petición de Principio", "pista": "La conclusión ya está incluida en la premisa."},
            {"falacia": "Mi oponente dice que debemos reducir la jornada laboral. Lo que él quiere es que la gente trabaje menos y el país se vuelva perezoso.", "tipo": "Hombre de Paja", "pista": "Distorsiona el argumento original para atacarlo."},
            {"falacia": "Si dejamos que los estudiantes elijan sus materias, pronto querrán elegir el horario, luego las reglas de la escuela, y al final, la escuela se convertirá en un caos sin control.", "tipo": "Pendiente Resbaladiza", "pista": "Exagera las consecuencias futuras."},
            {"falacia": "No se ha demostrado que el té verde cure el cáncer, por lo tanto, no lo hace.", "tipo": "Ad Ignorantiam", "pista": "La falta de prueba no es prueba de no existencia."},
            {"falacia": "Todos mis amigos están comprando este nuevo videojuego, así que debe ser increíble y yo también debo tenerlo.", "tipo": "Ad Populum", "pista": "Apela a lo que 'todos hacen'."},
            {"falacia": "No podemos aceptar el argumento de María sobre la igualdad de género; ella es muy feminista y solo ve las cosas desde su perspectiva.", "tipo": "Ad Hominem", "pista": "Ataca la ideología de la persona en lugar del argumento."},
            {"falacia": "Después de que mi equipo de fútbol perdió, me puse calcetines diferentes al día siguiente y ganaron. Los calcetines diferentes me dieron suerte.", "tipo": "Falsa Causa", "pista": "Asocia eventos sin relación causal real."},
            {"falacia": "Visité un solo pueblo en la costa y la gente era muy amable. Por lo tanto, toda la gente de la costa es muy amable.", "tipo": "Generalización Apresurada", "pista": "Basado en una sola experiencia limitada."},
            {"falacia": "Los ovnis existen porque nadie ha probado lo contrario.", "tipo": "Ad Ignorantiam", "pista": "Se basa en la ausencia de evidencia en contra."},
            {"falacia": "Fumar es malo porque es perjudicial para la salud, y es perjudicial para la salud porque es malo fumar.", "tipo": "Petición de Principio", "pista": "El argumento se repite a sí mismo."},
            {"falacia": "El profesor dice que no se debe usar IA para las tareas. Él solo quiere que trabajemos más.", "tipo": "Ad Hominem", "pista": "Desacredita al profesor, no su regla."},
            {"falacia": "Si permitimos que los niños jueguen con tablets, se volverán adictos, no socializarán y nunca desarrollarán habilidades del mundo real.", "tipo": "Pendiente Resbaladiza", "pista": "Cadena de consecuencias extremas no justificadas."},
            {"falacia": "Si la mayoría de los estudiantes prefiere las clases virtuales, entonces estas son intrínsecamente superiores a las presenciales.", "tipo": "Ad Populum", "pista": "La preferencia popular no define la superioridad intrínseca."},
            {"falacia": "Comencé el día con el pie izquierdo y luego me caí. Por lo tanto, levantarme con el pie izquierdo me causó la caída.", "tipo": "Falsa Causa", "pista": "Superstición que asume causalidad por secuencia."},
            {"falacia": "Mi vecino, que es vegetariano, se enfermó la semana pasada. Ser vegetariano te hace más propenso a enfermarte.", "tipo": "Generalización Apresurada", "pista": "Un solo caso no es suficiente para generalizar."},
            {"falacia": "El alma es inmortal porque no puede morir.", "tipo": "Petición de Principio", "pista": "Define inmortalidad por no poder morir, es circular."},
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

        title_label = tk.Label(self.master, text=f"📝 EJERCICIO {self.current_exercise_index + 1}/{self.total_exercises}: Identifica la Falacia", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        falacy_label = tk.Label(self.master, text=f"Afirmación: \"{exercise['falacia']}\"", wraplength=800, justify=tk.LEFT, font=("Arial", 12), fg="darkred")
        falacy_label.pack(pady=10, padx=20)
        
        question_label = tk.Label(self.master, text="¿Qué tipo de falacia contiene esta afirmación?", font=("Arial", 12), pady=10)
        question_label.pack()

        self.choice_var = tk.StringVar(self.master)
        self.choice_var.set("") # Clear previous selection

        options = [
            "Ad Hominem", "Ad Populum", "Falsa Causa", "Generalización Apresurada",
            "Petición de Principio", "Hombre de Paja", "Pendiente Resbaladiza", "Ad Ignorantiam"
        ]
        
        # Organize radio buttons in two columns for better layout
        frame_options = tk.Frame(self.master)
        frame_options.pack(pady=10)

        for i, option in enumerate(options):
            rb = tk.Radiobutton(frame_options, text=option, variable=self.choice_var, value=option.lower(), font=("Arial", 11))
            if i % 2 == 0:
                rb.grid(row=i//2, column=0, sticky=tk.W, padx=5, pady=2)
            else:
                rb.grid(row=i//2, column=1, sticky=tk.W, padx=5, pady=2)

        submit_button = tk.Button(self.master, text="Comprobar", command=self.check_exercise, font=("Arial", 12), bg="#FF6F00", fg="white")
        submit_button.pack(pady=15)

    def check_exercise(self):
        selected_answer = self.choice_var.get()
        correct_answer = self.exercises[self.current_exercise_index]['tipo'].lower()
        pista = self.exercises[self.current_exercise_index]['pista']

        if not selected_answer:
            messagebox.showwarning("Atención", "Por favor, selecciona una opción antes de comprobar.")
            return

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("¡Correcto!", "✅ ¡Identificaste la falacia correctamente!")
        else:
            messagebox.showerror("¡Incorrecto!", f"❌ ¡Incorrecto! La respuesta correcta era: '{correct_answer.upper()}'.\nPista: {pista}")
        
        self.current_exercise_index += 1
        self.display_exercise()

    def show_exercise_results(self):
        self.clear_frame()
        
        results_label = tk.Label(self.master, text="--- ¡FIN DE LOS EJERCICIOS DE IDENTIFICACIÓN! ---", font=("Arial", 16, "bold"), pady=10)
        results_label.pack()

        score_label = tk.Label(self.master, text=f"Tu puntuación final es: {self.score}/{self.total_exercises}!", font=("Arial", 14), pady=10)
        score_label.pack()

        if self.score >= self.total_exercises * 0.85:
            message = "🎉 ¡Felicidades! ¡Eres un experto detective de falacias!"
        elif self.score >= self.total_exercises * 0.6:
            message = "👍 ¡Muy bien! Ya entiendes cómo detectar las falacias más comunes."
        else:
            message = "✍️ ¡Sigue practicando! Con más esfuerzo, ¡ninguna falacia te engañará!"
        
        feedback_label = tk.Label(self.master, text=message, font=("Arial", 12), pady=10)
        feedback_label.pack()

        back_button = tk.Button(self.master, text="Volver al Menú Principal", command=self.show_main_page, font=("Arial", 12), bg="#4CAF50", fg="white")
        back_button.pack(pady=20)

    def start_refutation_practice(self):
        self.refutation_exercises = [
            {"falacia": "No hay que confiar en lo que dice ese economista; ¡está calvo y usa gafas viejas!", "tipo": "Ad Hominem", "sugerencia_refutacion": "Enfócate en el argumento, no en la apariencia. Puedes decir: 'La apariencia de una persona no tiene relación con la validez de sus ideas económicas. Centrémonos en sus propuestas.'"},
            {"falacia": "Todos mis compañeros de clase están de acuerdo en que la tarea es inútil, así que el profesor debería eliminarla.", "tipo": "Ad Populum", "sugerencia_refutacion": "Explica que la popularidad no define la utilidad. Puedes decir: 'Aunque muchos no estén de acuerdo, el número de personas que opinan algo no determina si la tarea es útil para el aprendizaje. Podríamos discutir su propósito.'"},
            {"falacia": "Desde que me mudé a esta casa, mi equipo de fútbol favorito siempre gana. Mi nueva casa trae suerte al equipo.", "tipo": "Falsa Causa", "sugerencia_refutacion": "Señala la falta de conexión lógica. Puedes decir: 'Que tu equipo gane después de tu mudanza es una coincidencia, no hay evidencia que relacione tu casa con los resultados deportivos.'"},
            {"falacia": "Conocí a un turista de ese país que fue muy grosero. Toda la gente de ese país es grosera.", "tipo": "Generalización Apresurada", "sugerencia_refutacion": "Pide más evidencia o señala la muestra insuficiente. Puedes decir: 'Basar una conclusión sobre un país entero en la experiencia con una sola persona es una generalización apresurada; una persona no representa a toda una población.'"},
            {"falacia": "La verdad es importante porque es fundamental decirla.", "tipo": "Petición de Principio", "sugerencia_refutacion": "Muestra que el argumento es circular. Puedes decir: 'Estás usando la misma idea para probarse a sí misma. Necesitamos una razón externa para entender por qué la verdad es importante.'"},
            {"falacia": "Mi vecino dice que deberíamos apoyar el comercio local. Lo que él quiere es que paguemos más por todo y que los grandes supermercados desaparezcan.", "tipo": "Hombre de Paja", "sugerencia_refutacion": "Clarifica la posición real del oponente. Puedes decir: 'Mi vecino no ha dicho que quiera que paguemos más ni que desaparezcan los supermercados; su punto es apoyar la economía local, lo cual es diferente.'"},
            {"falacia": "Si no exigimos que los estudiantes usen uniforme, se vestirán de manera inapropiada, esto causará distracciones, la disciplina desaparecerá y la escuela se volverá un desorden total.", "tipo": "Pendiente Resbaladiza", "sugerencia_refutacion": "Cuestiona la inevitabilidad de las consecuencias. Puedes decir: 'No hay evidencia de que no usar uniforme conduzca inevitablemente a la falta de disciplina y al caos. Podríamos tener reglas de vestimenta sin que sea un uniforme, por ejemplo.'"},
            {"falacia": "Como nadie ha demostrado que los viajes en el tiempo son imposibles, es probable que existan y que ya nos estén visitando viajeros del futuro.", "tipo": "Ad Ignorantiam", "sugerencia_refutacion": "Recuerda que la ausencia de prueba no es prueba. Puedes decir: 'El hecho de que no podamos probar la imposibilidad de algo no lo convierte automáticamente en una posibilidad o una realidad. La carga de la prueba recae en quien afirma que existe.'"},
        ]
        random.shuffle(self.refutation_exercises)
        self.current_refutation_index = 0
        self.display_refutation_exercise()

    def display_refutation_exercise(self):
        self.clear_frame()

        if self.current_refutation_index >= len(self.refutation_exercises):
            self.show_refutation_results()
            return

        exercise = self.refutation_exercises[self.current_refutation_index]

        title_label = tk.Label(self.master, text=f"✍️ PRACTICA DE REFUTACIÓN {self.current_refutation_index + 1}/{len(self.refutation_exercises)} ✍️", font=("Arial", 16, "bold"), pady=10)
        title_label.pack()

        falacy_text_label = tk.Label(self.master, text=f"**Falacia a Refutar ({exercise['tipo']}):**", font=("Arial", 13, "bold"), fg="darkred")
        falacy_text_label.pack(pady=(10,0))
        falacy_label = tk.Label(self.master, text=f"\"{exercise['falacia']}\"", wraplength=800, justify=tk.LEFT, font=("Arial", 12, "italic"))
        falacy_label.pack(pady=(0,10), padx=20)

        instruction_label = tk.Label(self.master, text="Piensa cómo refutarías esta falacia. Luego, compara con la sugerencia.", font=("Arial", 12), pady=10)
        instruction_label.pack()
        
        self.refutation_entry = scrolledtext.ScrolledText(self.master, height=5, width=80, font=("Arial", 11), wrap=tk.WORD)
        self.refutation_entry.pack(pady=10, padx=20)

        show_refutation_button = tk.Button(self.master, text="Ver Sugerencia de Refutación", command=self.show_suggested_refutation, font=("Arial", 12), bg="#008CBA", fg="white")
        show_refutation_button.pack(pady=10)
        
        next_button = tk.Button(self.master, text="Siguiente Falacia", command=self.next_refutation_exercise, font=("Arial", 12), bg="#4CAF50", fg="white")
        next_button.pack(pady=5)

    def show_suggested_refutation(self):
        exercise = self.refutation_exercises[self.current_refutation_index]
        messagebox.showinfo("Sugerencia de Refutación", f"Tipo de Falacia: {exercise['tipo']}\n\nSugerencia: {exercise['sugerencia_refutacion']}")

    def next_refutation_exercise(self):
        self.current_refutation_index += 1
        self.display_refutation_exercise()

    def show_refutation_results(self):
        self.clear_frame()
        
        results_label = tk.Label(self.master, text="--- ¡FIN DE LA PRÁCTICA DE REFUTACIÓN! ---", font=("Arial", 16, "bold"), pady=10)
        results_label.pack()

        final_message = tk.Label(self.master, text="¡Has practicado cómo desarmar argumentos defectuosos!\n"
                                                  "Recuerda: la clave es identificar el error lógico y señalarlo de forma clara y respetuosa.",
                                                  wraplength=700, justify=tk.CENTER, font=("Arial", 12), pady=10)
        final_message.pack()

        back_button = tk.Button(self.master, text="Volver al Menú Principal", command=self.show_main_page, font=("Arial", 12), bg="#4CAF50", fg="white")
        back_button.pack(pady=20)

def start_app():
    root = tk.Tk()
    app = FalacyLessonApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_app()
