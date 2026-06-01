import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

class AdvancedArgumentationApp:
    def __init__(self, master):
        self.master = master
        master.title("Lección 6: Argumentación Avanzada y Lógica (Preuniversitario)")
        
        # 1. Mejoras en Geometría y Centrado de Ventana
        self.window_width = 950
        self.window_height = 750
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (self.window_height/2))
        master.geometry(f"{self.window_width}x{self.window_height}+{x_cordinate}+{y_cordinate}")
        master.resizable(True, False) # Allow horizontal resizing, but not vertical
        master.config(bg="#F0F8FF") # 2. Color de Fondo General (AliceBlue)

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
        lesson_menu.add_command(label="Generar Nuevos Ejemplos", command=self.show_random_examples)
        lesson_menu.add_separator()
        lesson_menu.add_command(label="Salir", command=self.master.quit)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            # Keep the menu bar, only destroy other widgets
            if widget != self.master.winfo_children()[0]: # Assuming menubar is the first widget
                widget.destroy()
        # Ensure the background color is reset if clearing changes it
        self.master.config(bg="#F0F8FF")

    def show_main_page(self):
        self.clear_frame()
        
        main_label = tk.Label(self.master, text="¡Bienvenido a la Lección 6!\nArgumentación Avanzada y Lógica (Preuniversitario)", 
                              font=("Arial", 20, "bold"), pady=20, bg="#F0F8FF", fg="#2F4F4F") # DarkSlateGray
        main_label.pack()

        info_label = tk.Label(self.master, text="Usa el menú 'Lección' para navegar:\n\n"
                                               "📚 **Teoría:** Comprende validez, solidez y tipos de razonamiento.\n"
                                               "💡 **Ejemplos:** Observa estos conceptos en la práctica.\n"
                                               "📝 **Ejercicios:** ¡Evalúa argumentos y refuerza tu lógica!\n"
                                               "✨ **Generar Nuevos Ejemplos:** Para práctica ilimitada.",
                                               font=("Arial", 13), justify=tk.LEFT, bg="#F0F8FF", fg="#36454F") # Charcoal
        info_label.pack(pady=10)
        
        start_button = tk.Button(self.master, text="Comenzar Lección", command=self.show_theory, 
                                 font=("Arial", 15), bg="#FFD700", fg="black", padx=10, pady=5, 
                                 relief=tk.RAISED, bd=3) # Raised border for emphasis
        start_button.pack(pady=25)

    def show_theory(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="🧠 TEORÍA: ARGUMENTACIÓN AVANZADA Y LÓGICA 🔬", font=("Arial", 17, "bold"), pady=10, bg="#F0F8FF", fg="#004d40") # Dark green
        title_label.pack()

        theory_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=90, height=32, 
                                                bg="#FFFFFF", fg="#333333", relief=tk.FLAT, padx=10, pady=10) # White background, dark gray text, flat border
        theory_text.pack(pady=10, padx=20)
        
        theory_content = """
**1. Revisión Rápida: Los Fundamentos del Argumento** 🤔
   Un argumento es un conjunto de razones (premisas) que apoyan una afirmación (conclusión). En este nivel, no solo buscamos que los argumentos 'suenen bien', sino que sean **lógicamente impecables** y **fundamentados en la verdad**.

**2. Lógica Formal vs. Lógica Informal: Validez y Solidez** 🚨
   La **lógica** es la herramienta para evaluar la fuerza real de un razonamiento.

   **a. Lógica Formal:**
      - Se centra en la **estructura (forma)** del argumento, no en su contenido.
      - Concepto clave: **VALIDEZ**.
      - Un argumento es **válido** si su conclusión se sigue *necesariamente* de sus premisas. Si las premisas fueran verdaderas, la conclusión DEBERÍA ser verdadera.
      - **Importante:** Un argumento válido puede tener premisas falsas y/o una conclusión falsa.
      - **Ejemplo (Válido, pero NO sólido):**
        * Premisa 1: Todos los pájaros son mamíferos. (Falso)
        * Premisa 2: Un gorrión es un pájaro. (Verdadero)
        * Conclusión: Por lo tanto, un gorrión es un mamífero. (Falso)
        * *Análisis:* Es **válido** porque la estructura lógica es correcta. Si las premisas fueran ciertas, la conclusión lo sería.

   **b. Lógica Informal:**
      - Se centra en el **contenido** del argumento, su **pertinencia**, la **aceptabilidad** de las premisas y la **fuerza de la inferencia**.
      - Concepto clave: **SOLIDEZ (Soundness)**.
      - Un argumento es **sólido** si es **válido** (formalmente correcto) Y **todas sus premisas son verdaderas**.
      - **Un argumento sólido siempre tiene una conclusión verdadera.**
      - **Ejemplo (Válido y Sólido):**
        * Premisa 1: Todos los peces viven en el agua. (Verdadero)
        * Premisa 2: Un tiburón es un pez. (Verdadero)
        * Conclusión: Por lo tanto, un tiburón vive en el agua. (Verdadero)
        * *Análisis:* Este argumento es **válido** (estructura correcta) y **sólido** (premisas verdaderas).
      - Las falacias (vistas en lecciones anteriores) son errores que impiden la solidez.
   **Diferencia clave:** La **validez** es sobre la *forma*; la **solidez** es sobre la *forma* Y el *contenido* (verdad de las premisas).

**3. Tipos de Razonamiento: Deductivo e Inductivo** 📝

   **a. Razonamiento Deductivo:**
      - Va de lo **general a lo particular**.
      - Si las premisas son verdaderas y el argumento es válido, la conclusión es **necesariamente verdadera**.
      - **Objetivo:** Probar una conclusión específica a partir de verdades generales con **certeza**.
      - **Ejemplo:**
        * Premisa 1: Todos los insectos tienen seis patas.
        * Premisa 2: Las hormigas son insectos.
        * Conclusión: Por lo tanto, las hormigas tienen seis patas.

   **b. Razonamiento Inductivo:**
      - Va de lo **particular a lo general**.
      - Las premisas proporcionan **evidencia que apoya la probabilidad** de que la conclusión sea verdadera, pero no la garantizan.
      - **Objetivo:** Formular generalizaciones, predicciones o hipótesis basadas en observaciones específicas con **probabilidad** o **fuerza**.
      - **Evaluación:** Se evalúan como **fuertes/débiles**, no válidos/inválidos.
      - **Ejemplo:**
        * Premisa 1: Cada perro que he visto tiene cola.
        * Conclusión: Por lo tanto, todos los perros tienen cola.
        * *Análisis:* Es **fuerte**, pero no 100% cierto (podría haber un perro sin cola por accidente o mutación).
"""
        theory_text.insert(tk.END, theory_content)
        theory_text.config(state=tk.DISABLED) # Make text read-only

    def show_examples(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="💡 EJEMPLOS DE VALIDEZ, SOLIDEZ Y TIPOS DE RAZONAMIENTO 💡", font=("Arial", 16, "bold"), pady=10, bg="#F0F8FF", fg="#004d40")
        title_label.pack()

        examples_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=90, height=32, 
                                                  bg="#FFFFFF", fg="#333333", relief=tk.FLAT, padx=10, pady=10)
        examples_text.pack(pady=10, padx=20)

        examples_content = """
**Ejemplo 1: Deductivo, Válido y Sólido**
   - P1: Todos los atletas olímpicos entrenan duro.
   - P2: María es una atleta olímpica.
   - C: Por lo tanto, María entrena duro.
   *Análisis:* La conclusión se sigue necesariamente (válido) y todas las premisas son verdaderas (sólido).

---

**Ejemplo 2: Deductivo, Válido, pero NO Sólido**
   - P1: Todos los peces vuelan. (Falso)
   - P2: Una trucha es un pez. (Verdadero)
   - C: Por lo tanto, una trucha vuela. (Falso)
   *Análisis:* La estructura es correcta (válido), pero una premisa es falsa, por lo tanto, no es sólido.

---

**Ejemplo 3: Deductivo, Inválido (y por ende, no sólido)**
   - P1: Algunos estudiantes usan gafas.
   - P2: Juan usa gafas.
   - C: Por lo tanto, Juan es estudiante.
   *Análisis:* La conclusión NO se sigue necesariamente. Juan podría usar gafas por otra razón (inválido).

---

**Ejemplo 4: Inductivo Fuerte**
   - P1: Cada vez que he ido al parque en verano, ha hecho sol.
   - C: Es probable que la próxima vez que vaya al parque en verano, haga sol.
   *Análisis:* Las premisas aportan evidencia fuerte, haciendo la conclusión probable, pero no garantizada.

---
    
**Ejemplo 5: Inductivo Débil (Generalización Apresurada)**
   - P1: Ayer conocí a un conductor de taxi y era muy amable.
   - C: Por lo tanto, todos los conductores de taxi son muy amables.
   *Análisis:* La evidencia es insuficiente para la generalización, es un argumento inductivo muy débil.
"""
        examples_text.insert(tk.END, examples_content)
        examples_text.config(state=tk.DISABLED) # Make text read-only

    def start_exercises(self):
        self.exercises = [
            {"arg": "Todos los perros son mamíferos. Fido es un perro. Por lo tanto, Fido es un mamífero.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
            {"arg": "Cada vez que tiro una pelota al aire, cae. Por lo tanto, la próxima vez que tire una pelota al aire, caerá.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
            {"arg": "Todos los peces pueden volar. Los delfines son peces. Por lo tanto, los delfines pueden volar.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "NO SÓLIDO"},
            {"arg": "Algunos científicos usan gafas. Mi padre usa gafas. Por lo tanto, mi padre es científico.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "INVÁLIDO", "solidez_esperada": "NO APLICA"},
            {"arg": "He comido pizza en cinco pizzerías diferentes de esta ciudad y todas eran deliciosas. Probablemente, todas las pizzerías de esta ciudad son deliciosas.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
            {"arg": "Todos los gatos tienen cola. Félix no tiene cola. Por lo tanto, Félix no es un gato.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
            {"arg": "Conocí a una persona de esa ciudad y era muy ruidosa. Todas las personas de esa ciudad son ruidosas.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "DÉBIL"},
            {"arg": "Si es de día, hay luz solar. Es de día. Por lo tanto, hay luz solar.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
            {"arg": "Cada estudiante en la clase B obtuvo una A en el examen. Por lo tanto, el examen era fácil.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "DÉBIL"},
            {"arg": "Todas las plantas realizan fotosíntesis. Una rosa es una planta. Por lo tanto, una rosa realiza fotosíntesis.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
            {"arg": "El sol ha salido todos los días hasta ahora. Por lo tanto, el sol saldrá mañana.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
            {"arg": "Ningún futbolista es un malabarista. Messi es futbolista. Por lo tanto, Messi no es malabarista.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
            {"arg": "La mayoría de los votantes en las encuestas apoya al Candidato X. Por lo tanto, el Candidato X ganará las elecciones.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
            {"arg": "Si llueve, las calles se mojan. Las calles están mojadas. Por lo tanto, llovió.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "INVÁLIDO", "solidez_esperada": "NO APLICA"},
            {"arg": "Todos los insectos tienen ocho patas. Una araña es un insecto. Por lo tanto, una araña tiene ocho patas.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "NO SÓLIDO"},
            {"arg": "Este medicamento funcionó en 9 de cada 10 pacientes en el estudio. Es probable que funcione en ti.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "FUERTE"},
            {"arg": "Todos los cuadrados tienen cuatro lados. Esta figura es un cuadrado. Por lo tanto, esta figura tiene cuatro lados.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
            {"arg": "Mis últimas tres predicciones meteorológicas fueron correctas. Por lo tanto, mi próxima predicción también será correcta.", 
             "tipo_esperado": "INDUCTIVO", "fuerza_esperada": "DÉBIL"},
            {"arg": "Si un animal es un perro, entonces es un mamífero. Este animal es un mamífero. Por lo tanto, este animal es un perro.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "INVÁLIDO", "solidez_esperada": "NO APLICA"},
            {"arg": "Todos los cuerpos celestes con anillos son planetas. Saturno tiene anillos. Por lo tanto, Saturno es un planeta.", 
             "tipo_esperado": "DEDUCTIVO", "validez_esperada": "VÁLIDO", "solidez_esperada": "SÓLIDO"},
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

        title_label = tk.Label(self.master, text=f"📝 EJERCICIO {self.current_exercise_index + 1}/{self.total_exercises}: Evalúa el Argumento", 
                              font=("Arial", 16, "bold"), pady=10, bg="#F0F8FF", fg="#004d40")
        title_label.pack()

        arg_label = tk.Label(self.master, text=f"Argumento: \"{exercise['arg']}\"", wraplength=850, justify=tk.LEFT, 
                             font=("Arial", 12), fg="#00008B", bg="#F0F8FF") # DarkBlue
        arg_label.pack(pady=10, padx=20)
        
        # --- Pregunta de Tipo ---
        tk.Label(self.master, text="1. ¿Qué tipo de razonamiento es?", font=("Arial", 12), bg="#F0F8FF", fg="#333333").pack(pady=(10,0))
        self.type_var = tk.StringVar(self.master)
        self.type_var.set("")
        
        type_options_frame = tk.Frame(self.master, bg="#F0F8FF")
        type_options_frame.pack(anchor=tk.W, padx=50)
        tk.Radiobutton(type_options_frame, text="DEDUCTIVO", variable=self.type_var, value="DEDUCTIVO", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(side=tk.LEFT, padx=10) # LightBlue for selected radio
        tk.Radiobutton(type_options_frame, text="INDUCTIVO", variable=self.type_var, value="INDUCTIVO", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(side=tk.LEFT, padx=10)

        # --- Preguntas de Validez/Solidez/Fuerza (inicialmente ocultas) ---
        self.deductive_questions_frame = tk.Frame(self.master, bg="#F0F8FF")
        self.inductive_questions_frame = tk.Frame(self.master, bg="#F0F8FF")
        
        # Deductivo: Validez y Solidez
        tk.Label(self.deductive_questions_frame, text="2. Si es deductivo, ¿es VÁLIDO?", font=("Arial", 12), bg="#F0F8FF", fg="#333333").pack(pady=(10,0), anchor=tk.W)
        self.validity_var = tk.StringVar(self.deductive_questions_frame)
        self.validity_var.set("")
        tk.Radiobutton(self.deductive_questions_frame, text="SÍ", variable=self.validity_var, value="VÁLIDO", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(anchor=tk.W)
        tk.Radiobutton(self.deductive_questions_frame, text="NO (INVÁLIDO)", variable=self.validity_var, value="INVÁLIDO", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(anchor=tk.W)

        tk.Label(self.deductive_questions_frame, text="3. Si es válido, ¿es SÓLIDO? (Todas las premisas son verdaderas)", font=("Arial", 12), bg="#F0F8FF", fg="#333333").pack(pady=(10,0), anchor=tk.W)
        self.soundness_var = tk.StringVar(self.deductive_questions_frame)
        self.soundness_var.set("")
        tk.Radiobutton(self.deductive_questions_frame, text="SÍ (SÓLIDO)", variable=self.soundness_var, value="SÓLIDO", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(anchor=tk.W)
        tk.Radiobutton(self.deductive_questions_frame, text="NO (NO SÓLIDO)", variable=self.soundness_var, value="NO SÓLIDO", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(anchor=tk.W)

        # Inductivo: Fuerza
        tk.Label(self.inductive_questions_frame, text="2. Si es inductivo, ¿es FUERTE o DÉBIL?", font=("Arial", 12), bg="#F0F8FF", fg="#333333").pack(pady=(10,0), anchor=tk.W)
        self.strength_var = tk.StringVar(self.inductive_questions_frame)
        self.strength_var.set("")
        tk.Radiobutton(self.inductive_questions_frame, text="FUERTE", variable=self.strength_var, value="FUERTE", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(anchor=tk.W)
        tk.Radiobutton(self.inductive_questions_frame, text="DÉBIL", variable=self.strength_var, value="DÉBIL", 
                       font=("Arial", 11), bg="#F0F8FF", fg="#333333", selectcolor="#ADD8E6").pack(anchor=tk.W)

        # Show/hide relevant frames based on type selection
        self.type_var.trace_add("write", self.toggle_question_frames)
        self.toggle_question_frames() 

        submit_button = tk.Button(self.master, text="Comprobar Respuestas", command=self.check_exercise, 
                                  font=("Arial", 13), bg="#008CBA", fg="white", padx=10, pady=5, 
                                  relief=tk.RAISED, bd=3)
        submit_button.pack(pady=20)

    def toggle_question_frames(self, *args):
        selected_type = self.type_var.get()
        if selected_type == "DEDUCTIVO":
            self.deductive_questions_frame.pack(pady=5, padx=50, anchor=tk.W)
            self.inductive_questions_frame.pack_forget()
        elif selected_type == "INDUCTIVO":
            self.inductive_questions_frame.pack(pady=5, padx=50, anchor=tk.W)
            self.deductive_questions_frame.pack_forget()
        else: # No selection yet
            self.deductive_questions_frame.pack_forget()
            self.inductive_questions_frame.pack_forget()

    def check_exercise(self):
        exercise = self.exercises[self.current_exercise_index]
        
        selected_type = self.type_var.get()
        
        feedback_message = ""
        is_correct_overall = True

        # Check Type
        if not selected_type:
            messagebox.showwarning("Atención", "Por favor, selecciona el tipo de razonamiento.")
            return

        if selected_type == exercise["tipo_esperado"]:
            feedback_message += "✅ Tipo de razonamiento: Correcto.\n"
        else:
            feedback_message += f"❌ Tipo de razonamiento: Incorrecto. Era {exercise['tipo_esperado']}.\n"
            is_correct_overall = False

        if selected_type == "DEDUCTIVO":
            selected_validity = self.validity_var.get()
            selected_soundness = self.soundness_var.get()

            if not selected_validity:
                messagebox.showwarning("Atención", "Por favor, selecciona si es VÁLIDO.")
                return
            
            # Check Validity
            if selected_validity == exercise["validez_esperada"]:
                feedback_message += "✅ Validez: Correcta.\n"
            else:
                feedback_message += f"❌ Validez: Incorrecta. Era {exercise['validez_esperada']}.\n"
                is_correct_overall = False
            
            # Check Soundness (only if the exercise is supposed to be valid)
            if exercise["validez_esperada"] == "VÁLIDO":
                if not selected_soundness:
                    messagebox.showwarning("Atención", "Por favor, selecciona si es SÓLIDO.")
                    return

                if selected_soundness == exercise["solidez_esperada"]:
                    feedback_message += "✅ Solidez: Correcta.\n"
                else:
                    feedback_message += f"❌ Solidez: Incorrecta. Era {exercise['solidez_esperada']}.\n"
                    is_correct_overall = False
            else: # If the argument is invalid, it cannot be sound. No need to check user's soundness input.
                feedback_message += "   (Al ser inválido, no puede ser sólido. Su respuesta de solidez no se evalúa.)\n"
                # For scoring, we consider this path as "correct" if the validity was correctly identified as INVALID.
                # However, the overall_correctness is already determined by validity.
                pass 

        elif selected_type == "INDUCTIVO":
            selected_strength = self.strength_var.get()
            if not selected_strength:
                messagebox.showwarning("Atención", "Por favor, selecciona si es FUERTE o DÉBIL.")
                return

            # Check Strength
            if selected_strength == exercise["fuerza_esperada"]:
                feedback_message += "✅ Fuerza inductiva: Correcta.\n"
            else:
                feedback_message += f"❌ Fuerza inductiva: Incorrecta. Era {exercise['fuerza_esperada']}.\n"
                is_correct_overall = False
        
        # Only increment score if all specific checks for the chosen type were correct
        if selected_type == "DEDUCTIVO":
            if selected_type == exercise["tipo_esperado"] and selected_validity == exercise["validez_esperada"]:
                # Only check soundness if it was supposed to be valid, otherwise this part is skipped (correctly)
                if exercise["validez_esperada"] == "VÁLIDO":
                    if selected_soundness == exercise["solidez_esperada"]:
                        self.score += 1
                else: # If it was correctly identified as INVALID, then it's correct for this branch
                    self.score += 1
        elif selected_type == "INDUCTIVO":
            if selected_type == exercise["tipo_esperado"] and selected_strength == exercise["fuerza_esperada"]:
                self.score += 1

        if is_correct_overall: # This is a simple overall check for messagebox
            messagebox.showinfo("¡Correcto!", feedback_message)
        else:
            messagebox.showerror("¡Incorrecto!", feedback_message)
        
        self.current_exercise_index += 1
        self.display_exercise()

    def show_exercise_results(self):
        self.clear_frame()
        
        results_label = tk.Label(self.master, text="--- ¡FIN DE LOS EJERCICIOS DE EVALUACIÓN! ---", font=("Arial", 18, "bold"), pady=10, bg="#F0F8FF", fg="#004d40")
        results_label.pack()

        score_label = tk.Label(self.master, text=f"Tu puntuación final es: {self.score}/{self.total_exercises}!", font=("Arial", 15), pady=10, bg="#F0F8FF", fg="#333333")
        score_label.pack()

        if self.score >= self.total_exercises * 0.85:
            message = "🎉 ¡Felicidades! ¡Dominas la lógica y la argumentación avanzada!"
        elif self.score >= self.total_exercises * 0.6:
            message = "👍 ¡Muy bien! Estás en camino a un sólido pensamiento crítico."
        else:
            message = "✍️ ¡Sigue practicando! La lógica es una habilidad que mejora con la práctica."
        
        feedback_label = tk.Label(self.master, text=message, font=("Arial", 13), pady=10, bg="#F0F8FF", fg="#333333")
        feedback_label.pack()

        back_button = tk.Button(self.master, text="Volver al Menú Principal", command=self.show_main_page, 
                                font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5, 
                                relief=tk.RAISED, bd=3)
        back_button.pack(pady=20)

    def show_random_examples(self):
        self.clear_frame()
        
        title_label = tk.Label(self.master, text="✨ GENERADOR DE EJEMPLOS ALEATORIOS ✨", font=("Arial", 16, "bold"), pady=10, bg="#F0F8FF", fg="#004d40")
        title_label.pack()

        random_examples_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=("Arial", 12), width=90, height=32, 
                                                  bg="#FFFFFF", fg="#333333", relief=tk.FLAT, padx=10, pady=10)
        random_examples_text.pack(pady=10, padx=20)

        # Bases de datos para construir falacias aleatorias
        sujetos_general = ["Todos los estudiantes de esta universidad", "Cada persona en este país", 
                           "Los mamíferos", "Los metales", "Todos los números pares", "Los ciudadanos mayores de 18 años"]
        propiedades_general = ["pueden votar", "son vertebrados", "conducen electricidad", "han nacido"]

        sujetos_especifico = ["Juan", "Este perro", "El agua", "El hierro", "El número 4", "María", "Mi computadora"]
        propiedades_especifico_verdadero = ["es un estudiante", "ladra", "hierve a 100°C", "es un metal", "es un número par"]
        
        observaciones = ["He visto 1000 cisnes blancos", "Todos los cuervos que he visto son negros", 
                         "Las manzanas que he probado en esta región son dulces", "Cada día amanece después de la noche"]
        conclusiones_probables = ["Por lo tanto, todos los cisnes son blancos.", "Por lo tanto, todos los cuervos son negros.",
                                  "Probablemente, todas las manzanas de esta región son dulces.", "El sol saldrá mañana."]
        
        observaciones_debiles = ["Conocí a una persona de ese equipo y era desorganizada", "Solo dos personas se quejaron del servicio"]
        conclusiones_improbables = ["Por lo tanto, todo el equipo es desorganizado.", "El servicio es terrible para todos."]

        opciones_inv_ded = [
            ("Si hay fuego, hay humo. Hay humo. Por lo tanto, hay fuego.", "DEDUCTIVO", "INVÁLIDO"),
            ("Algunos gatos son negros. Mi gato es negro. Por lo tanto, mi gato es un gato.", "DEDUCTIVO", "INVÁLIDO"),
            ("Todos los libros son interesantes. 'Romeo y Julieta' es interesante. Por lo tanto, 'Romeo y Julieta' es un libro.", "DEDUCTIVO", "INVÁLIDO"),
            ("Todos los perros son animales. Un canario es un animal. Por lo tanto, un canario es un perro.", "DEDUCTIVO", "INVÁLIDO"),
        ]

        generated_content = ""
        for i in range(20):
            tipo_arg = random.choice(["DEDUCTIVO", "INDUCTIVO"])
            falacia_generada = ""
            
            if tipo_arg == "DEDUCTIVO":
                caso_validez = random.choice(["SOLIDO", "NO_SOLIDO_PREMISA_FALSA", "INVALIDO"])
                if caso_validez == "SOLIDO":
                    suj_gen = random.choice(["Los humanos", "Las aves", "Los cuadrados", "Los árboles"])
                    prop_gen = random.choice(["son mortales", "tienen alas", "tienen cuatro lados", "crecen con el sol"])
                    suj_esp = random.choice(["Sócrates", "Un águila", "Mi mesa", "Un roble"])
                    
                    if suj_esp == "Mi mesa": # For logical coherence
                        prop_gen = "tienen cuatro patas"
                        suj_gen = "Todas las mesas"
                    elif suj_esp == "Un roble":
                        prop_gen = "crecen con el sol"
                        suj_gen = "Los árboles"
                    elif suj_esp == "Sócrates":
                        prop_gen = "son mortales"
                        suj_gen = "Los humanos"
                    
                    falacia_generada = f"P1: {suj_gen} {prop_gen}. P2: {suj_esp} es un/una {suj_gen.lower().replace('todos los ', '').replace('todas las ', '').replace('los ', '').replace('las ', '').replace('s', '')}. C: Por lo tanto, {suj_esp} {prop_gen}."
                    
                elif caso_validez == "NO_SOLIDO_PREMISA_FALSA":
                    suj_gen = random.choice(["Todos los peces", "Todos los gatos", "Todos los insectos", "Todos los autos"])
                    prop_gen = random.choice(["pueden volar", "hablan español", "tienen ocho patas", "funcionan con agua"])
                    suj_esp = random.choice(["Un tiburón", "Mi mascota", "Una mosca", "Mi coche"])
                    
                    falacia_generada = f"P1: {suj_gen} {prop_gen}. P2: {suj_esp} es un/una {suj_gen.lower().replace('todos los ', '').replace('todas las ', '').replace('los ', '').replace('las ', '').replace('s', '')}. C: Por lo tanto, {suj_esp} {prop_gen}."
                
                elif caso_validez == "INVALIDO":
                    falacia_generada = random.choice(opciones_inv_ded)[0]
                    
            elif tipo_arg == "INDUCTIVO":
                if random.choice([True, False]): # Fuerte o débil
                    obs = random.choice(observaciones)
                    conc = random.choice(conclusiones_probables)
                    falacia_generada = f"{obs}. {conc}"
                else:
                    obs = random.choice(observaciones_debiles)
                    conc = random.choice(conclusiones_improbables)
                    falacia_generada = f"{obs}. {conc}"

            generated_content += f"--- Nuevo Ejemplo {i+1} ---\n"
            generated_content += f"Argumento: \"{falacia_generada}\"\n"
            generated_content += f"Tipo: {tipo_arg}\n\n"

        random_examples_text.insert(tk.END, generated_content)
        random_examples_text.config(state=tk.DISABLED) # Make text read-only

        back_button = tk.Button(self.master, text="Volver al Menú Principal", command=self.show_main_page, 
                                font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5, 
                                relief=tk.RAISED, bd=3)
        back_button.pack(pady=20)


def start_app():
    root = tk.Tk()
    app = AdvancedArgumentationApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_app()
