import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import textwrap

# Datos para la tabla comparativa
table_data = [
    ["Tipo", "Estructura Español", "Ejemplo Español", "Estructura Inglés", "Ejemplo Inglés"],
    ["Afirmativa", "Sujeto + Verbo + Objeto", "Ella lee libros", "Sujeto + Verbo + Objeto", "She reads books"],
    ["Negativa", "No + Verbo", "No tenemos tiempo", "Sujeto + do/does/did + not + verbo", "We do not have time"],
    ["Interrogativa Sí/No", "¿ + Verbo + Sujeto + ?", "¿Tú entiendes?", "Do/Does/Did + Sujeto + Verbo + ?", "Do you understand?"],
    ["Interrogativa WH-", "¿ + WH- + Verbo + Sujeto + ?", "¿Qué quieres tú?", "WH- + do/does/did + Sujeto + Verbo + ?", "What do you want?"],
    ["Exclamativa", "¡ + Qué/Cómo + !", "¡Qué sorpresa!", "What/How + !", "What a surprise!"]
]

# 100 ejercicios para practicar (español, inglés, tipo, dificultad)
exercises = [
    # Afirmativas (20)
    ("Él cocina pescado", "He cooks fish", "afirmativa", 1),
    ("Yo camino al parque", "I walk to the park", "afirmativa", 1),
    ("Nosotros estudiamos inglés", "We study English", "afirmativa", 1),
    ("Ella lee un libro", "She reads a book", "afirmativa", 1),
    ("Ellos juegan fútbol", "They play soccer", "afirmativa", 1),
    ("El niño corre rápido", "The boy runs fast", "afirmativa", 1),
    ("La mujer cocina bien", "The woman cooks well", "afirmativa", 1),
    ("Ustedes trabajan mucho", "You work a lot", "afirmativa", 1),
    ("Mi hermana canta bonito", "My sister sings beautifully", "afirmativa", 2),
    ("Nuestro equipo gana siempre", "Our team always wins", "afirmativa", 2),
    ("El sol brilla intensamente", "The sun shines brightly", "afirmativa", 2),
    ("Los estudiantes aprenden rápido", "The students learn quickly", "afirmativa", 2),
    ("Mi padre conduce cuidadosamente", "My father drives carefully", "afirmativa", 2),
    ("Esa empresa crece constantemente", "That company grows constantly", "afirmativa", 3),
    ("El proyecto avanza satisfactoriamente", "The project progresses satisfactorily", "afirmativa", 3),
    ("Nuestros productos mejoran continuamente", "Our products improve continuously", "afirmativa", 3),
    
    # Negativas (20)
    ("Ella no canta bien", "She does not sing well", "negativa", 1),
    ("Nosotros no jugamos fútbol", "We do not play soccer", "negativa", 1),
    ("Yo no como carne", "I do not eat meat", "negativa", 1),
    ("Ellos no estudian francés", "They do not study French", "negativa", 1),
    ("Tú no trabajas los domingos", "You do not work on Sundays", "negativa", 1),
    ("El niño no llora", "The boy does not cry", "negativa", 1),
    ("Usted no fuma", "You do not smoke", "negativa", 1),
    ("Ellas no bailan bien", "They do not dance well", "negativa", 1),
    ("Mi hermano no practica deportes", "My brother does not practice sports", "negativa", 2),
    ("Nuestro equipo no pierde nunca", "Our team never loses", "negativa", 2),
    ("Ese restaurante no abre los lunes", "That restaurant does not open on Mondays", "negativa", 2),
    ("El avión no llegó a tiempo", "The plane did not arrive on time", "negativa", 2),
    ("No entendí la pregunta", "I did not understand the question", "negativa", 2),
    ("El gobierno no aprobó la ley", "The government did not approve the law", "negativa", 3),
    ("La empresa no cumplió sus objetivos", "The company did not meet its objectives", "negativa", 3),
    
    # Interrogativas Sí/No (20)
    ("¿Ellos estudian inglés?", "Do they study English?", "interrogativa sí/no", 1),
    ("¿Tú necesitas ayuda?", "Do you need help?", "interrogativa sí/no", 1),
    ("¿Ella canta bien?", "Does she sing well?", "interrogativa sí/no", 1),
    ("¿Ustedes trabajan aquí?", "Do you work here?", "interrogativa sí/no", 1),
    ("¿El niño corre rápido?", "Does the boy run fast?", "interrogativa sí/no", 1),
    ("¿Ellos juegan fútbol?", "Do they play soccer?", "interrogativa sí/no", 1),
    ("¿Tu hermano lee mucho?", "Does your brother read a lot?", "interrogativa sí/no", 2),
    ("¿Tu familia viaja frecuentemente?", "Does your family travel frequently?", "interrogativa sí/no", 2),
    ("¿Comprendiste la lección?", "Did you understand the lesson?", "interrogativa sí/no", 2),
    ("¿Ellos terminaron el proyecto?", "Did they finish the project?", "interrogativa sí/no", 2),
    ("¿El equipo ganó el campeonato?", "Did the team win the championship?", "interrogativa sí/no", 2),
    ("¿Estudiarás medicina?", "Will you study medicine?", "interrogativa sí/no", 3),
    ("¿Habías visitado antes este lugar?", "Had you visited this place before?", "interrogativa sí/no", 3),
    
    # Interrogativas WH- (20)
    ("¿Dónde trabaja tu madre?", "Where does your mother work?", "interrogativa wh-", 1),
    ("¿Qué quieres comer?", "What do you want to eat?", "interrogativa wh-", 1),
    ("¿Cuándo llegaste?", "When did you arrive?", "interrogativa wh-", 1),
    ("¿Por qué lloras?", "Why do you cry?", "interrogativa wh-", 1),
    ("¿Cómo te llamas?", "What is your name?", "interrogativa wh-", 1),
    ("¿Dónde viven ellos?", "Where do they live?", "interrogativa wh-", 1),
    ("¿Qué estudia tu hermana?", "What does your sister study?", "interrogativa wh-", 2),
    ("¿Cuándo termina la película?", "When does the movie end?", "interrogativa wh-", 2),
    ("¿Cómo funciona esta máquina?", "How does this machine work?", "interrogativa wh-", 2),
    ("¿Por qué no viniste ayer?", "Why didn't you come yesterday?", "interrogativa wh-", 2),
    ("¿Qué habrías hecho diferente?", "What would you have done differently?", "interrogativa wh-", 3),
    ("¿Cómo podría mejorar mi pronunciación?", "How could I improve my pronunciation?", "interrogativa wh-", 3),
    
    # Exclamativas (20)
    ("¡Qué día tan horrible!", "What a horrible day!", "exclamativa", 1),
    ("¡Cómo me gusta este lugar!", "How I like this place!", "exclamativa", 1),
    ("¡Qué sorpresa!", "What a surprise!", "exclamativa", 1),
    ("¡Qué bonito!", "How beautiful!", "exclamativa", 1),
    ("¡Qué inteligente eres!", "How smart you are!", "exclamativa", 1),
    ("¡Qué rápido corres!", "How fast you run!", "exclamativa", 1),
    ("¡Qué bien cantas!", "How well you sing!", "exclamativa", 2),
    ("¡Qué increíble historia!", "What an incredible story!", "exclamativa", 2),
    ("¡Cómo has crecido!", "How you have grown!", "exclamativa", 2),
    ("¡Qué maravilloso resultado!", "What a wonderful result!", "exclamativa", 2),
    ("¡Qué desastre absoluto!", "What an absolute disaster!", "exclamativa", 3),
    ("¡Cómo podría olvidar ese momento!", "How could I forget that moment!", "exclamativa", 3),
]

class SentencePracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Practicador de Oraciones Español-Inglés")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # Variables de estado
        self.current_exercise = 0
        self.score = 0
        self.total_exercises = 20  # Por defecto 20 ejercicios
        self.exercise_list = []
        
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Pestaña de Inicio
        self.home_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.home_frame, text="Inicio")
        
        # Pestaña de Tabla Comparativa
        self.table_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.table_frame, text="Tabla Comparativa")
        
        # Pestaña de Práctica
        self.practice_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.practice_frame, text="Práctica")
        
        # Pestaña de Resultados
        self.results_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.results_frame, text="Resultados")
        
        # Configurar cada pestaña
        self.setup_home_tab()
        self.setup_table_tab()
        self.setup_practice_tab()
        self.setup_results_tab()
    
    def setup_home_tab(self):
        title_label = ttk.Label(self.home_frame, text="Practicador de Oraciones Español-Inglés", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        intro_text = """
        Esta aplicación te ayudará a practicar y dominar las diferentes estructuras de oraciones 
        en inglés y español. Podrás:
        
        • Consultar una tabla comparativa de estructuras gramaticales
        • Practicar con más de 100 ejercicios de traducción
        • Evaluar tu progreso con un sistema de puntuación
        • Identificar áreas de mejora
        
        ¡Selecciona la pestaña de práctica para comenzar!
        """
        
        intro_label = ttk.Label(self.home_frame, text=intro_text, justify="center")
        intro_label.pack(pady=20, padx=20)
        
        # Selector de número de ejercicios
        exercise_frame = ttk.Frame(self.home_frame)
        exercise_frame.pack(pady=10)
        
        ttk.Label(exercise_frame, text="Número de ejercicios:").grid(row=0, column=0, padx=5)
        self.exercise_count = tk.StringVar(value="20")
        exercise_spinbox = ttk.Spinbox(exercise_frame, from_=5, to=100, textvariable=self.exercise_count, width=10)
        exercise_spinbox.grid(row=0, column=1, padx=5)
        
        # Botón para comenzar práctica
        start_button = ttk.Button(self.home_frame, text="Comenzar Práctica", command=self.start_practice)
        start_button.pack(pady=20)
    
    def setup_table_tab(self):
        # Crear un widget de texto con scroll para la tabla
        text_widget = scrolledtext.ScrolledText(self.table_frame, wrap=tk.WORD, width=85, height=25)
        text_widget.pack(fill="both", expand=True)
        
        # Insertar datos de la tabla
        for row in table_data:
            if row[0] == "Tipo":
                # Encabezado
                line = f"{row[0]:<20} | {row[1]:<25} | {row[2]:<25} | {row[3]:<25} | {row[4]:<20}\n"
                text_widget.insert("end", line)
                text_widget.insert("end", "-" * 120 + "\n")
            else:
                line = f"{row[0]:<20} | {row[1]:<25} | {row[2]:<25} | {row[3]:<25} | {row[4]:<20}\n"
                text_widget.insert("end", line)
        
        text_widget.configure(state="disabled")
    
    def setup_practice_tab(self):
        # Frame para la oración en español
        spanish_frame = ttk.LabelFrame(self.practice_frame, text="Oración en Español", padding="10")
        spanish_frame.pack(fill="x", pady=10)
        
        self.spanish_label = ttk.Label(spanish_frame, text="", font=("Arial", 12), wraplength=600)
        self.spanish_label.pack()
        
        # Frame para la respuesta en inglés
        english_frame = ttk.LabelFrame(self.practice_frame, text="Traducción al Inglés", padding="10")
        english_frame.pack(fill="x", pady=10)
        
        self.answer_var = tk.StringVar()
        answer_entry = ttk.Entry(english_frame, textvariable=self.answer_var, font=("Arial", 12), width=50)
        answer_entry.pack(pady=5)
        answer_entry.bind("<Return>", lambda e: self.check_answer())
        
        # Frame para información adicional
        info_frame = ttk.Frame(self.practice_frame)
        info_frame.pack(fill="x", pady=10)
        
        ttk.Label(info_frame, text="Tipo:").grid(row=0, column=0, sticky="w", padx=5)
        self.type_label = ttk.Label(info_frame, text="", foreground="blue")
        self.type_label.grid(row=0, column=1, sticky="w", padx=5)
        
        ttk.Label(info_frame, text="Dificultad:").grid(row=0, column=2, sticky="w", padx=20)
        self.difficulty_label = ttk.Label(info_frame, text="", foreground="green")
        self.difficulty_label.grid(row=0, column=3, sticky="w", padx=5)
        
        ttk.Label(info_frame, text="Progreso:").grid(row=0, column=4, sticky="w", padx=20)
        self.progress_label = ttk.Label(info_frame, text="0/0")
        self.progress_label.grid(row=0, column=5, sticky="w", padx=5)
        
        # Barra de progreso
        self.progress_bar = ttk.Progressbar(self.practice_frame, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x", pady=5)
        
        # Frame para botones
        button_frame = ttk.Frame(self.practice_frame)
        button_frame.pack(pady=10)
        
        self.check_button = ttk.Button(button_frame, text="Verificar", command=self.check_answer)
        self.check_button.pack(side="left", padx=5)
        
        self.next_button = ttk.Button(button_frame, text="Siguiente", command=self.next_exercise, state="disabled")
        self.next_button.pack(side="left", padx=5)
        
        ttk.Button(button_frame, text="Finalizar Práctica", command=self.finish_practice).pack(side="left", padx=5)
        
        # Frame para retroalimentación
        feedback_frame = ttk.LabelFrame(self.practice_frame, text="Retroalimentación", padding="10")
        feedback_frame.pack(fill="x", pady=10)
        
        self.feedback_label = ttk.Label(feedback_frame, text="", foreground="red", wraplength=600)
        self.feedback_label.pack()
    
    def setup_results_tab(self):
        # Frame para estadísticas
        stats_frame = ttk.LabelFrame(self.results_frame, text="Estadísticas de la Sesión", padding="10")
        stats_frame.pack(fill="x", pady=10)
        
        ttk.Label(stats_frame, text="Puntuación Total:").grid(row=0, column=0, sticky="w", padx=5)
        self.score_label = ttk.Label(stats_frame, text="0", font=("Arial", 14, "bold"))
        self.score_label.grid(row=0, column=1, sticky="w", padx=5)
        
        ttk.Label(stats_frame, text="Porcentaje de Aciertos:").grid(row=0, column=2, sticky="w", padx=20)
        self.percentage_label = ttk.Label(stats_frame, text="0%", font=("Arial", 14, "bold"))
        self.percentage_label.grid(row=0, column=3, sticky="w", padx=5)
        
        ttk.Label(stats_frame, text="Ejercicios Completados:").grid(row=1, column=0, sticky="w", padx=5)
        self.completed_label = ttk.Label(stats_frame, text="0")
        self.completed_label.grid(row=1, column=1, sticky="w", padx=5)
        
        ttk.Label(stats_frame, text="Ejercicios por Tipo:").grid(row=1, column=2, sticky="w", padx=20)
        self.by_type_label = ttk.Label(stats_frame, text="")
        self.by_type_label.grid(row=1, column=3, sticky="w", padx=5)
        
        # Frame para detalles de resultados
        details_frame = ttk.LabelFrame(self.results_frame, text="Detalles de Resultados", padding="10")
        details_frame.pack(fill="both", expand=True, pady=10)
        
        # Treeview para mostrar resultados
        columns = ("#", "Español", "Tu Respuesta", "Respuesta Correcta", "Resultado")
        self.results_tree = ttk.Treeview(details_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, width=120)
        
        self.results_tree.column("#", width=40)
        self.results_tree.column("Español", width=200)
        self.results_tree.column("Tu Respuesta", width=200)
        self.results_tree.column("Respuesta Correcta", width=200)
        
        # Scrollbar para el treeview
        scrollbar = ttk.Scrollbar(details_frame, orient="vertical", command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=scrollbar.set)
        
        self.results_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botón para exportar resultados
        ttk.Button(self.results_frame, text="Exportar Resultados", command=self.export_results).pack(pady=10)
    
    def start_practice(self):
        try:
            self.total_exercises = int(self.exercise_count.get())
            if self.total_exercises < 5 or self.total_exercises > 100:
                messagebox.showerror("Error", "Por favor, ingresa un número entre 5 y 100")
                return
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido")
            return
        
        # Seleccionar ejercicios aleatorios
        self.exercise_list = random.sample(exercises, self.total_exercises)
        self.current_exercise = 0
        self.score = 0
        
        # Limpiar resultados anteriores
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Ir a la pestaña de práctica
        self.notebook.select(2)
        self.show_exercise()
    
    def show_exercise(self):
        if self.current_exercise < len(self.exercise_list):
            esp, eng, tipo, dificultad = self.exercise_list[self.current_exercise]
            self.spanish_label.config(text=esp)
            self.type_label.config(text=tipo)
            self.difficulty_label.config(text="★" * dificultad)
            self.progress_label.config(text=f"{self.current_exercise + 1}/{len(self.exercise_list)}")
            self.progress_bar["value"] = (self.current_exercise / len(self.exercise_list)) * 100
            
            self.answer_var.set("")
            self.feedback_label.config(text="")
            self.check_button.config(state="normal")
            self.next_button.config(state="disabled")
        else:
            self.finish_practice()
    
    def check_answer(self):
        esp, correct_eng, tipo, dificultad = self.exercise_list[self.current_exercise]
        user_answer = self.answer_var.get().strip()
        
        # Verificar si la respuesta es correcta
        is_correct = user_answer.lower() == correct_eng.lower()
        
        # Verificación flexible para respuestas "casi correctas"
        user_clean = user_answer.lower().replace("?", "").replace("!", "").replace(".", "").strip()
        correct_clean = correct_eng.lower().replace("?", "").replace("!", "").replace(".", "").strip()
        
        is_almost_correct = user_clean == correct_clean and not is_correct
        
        if is_correct:
            self.score += 1
            feedback = "✅ ¡Correcto! +1 punto"
            feedback_color = "green"
            result = "Correcto"
        elif is_almost_correct:
            self.score += 0.5
            feedback = f"✅ ¡Casi correcto! (+0.5 puntos) - La respuesta exacta es: {correct_eng}"
            feedback_color = "orange"
            result = "Parcial"
        else:
            feedback = f"❌ Incorrecto. La respuesta correcta es: {correct_eng}"
            feedback_color = "red"
            result = "Incorrecto"
        
        self.feedback_label.config(text=feedback, foreground=feedback_color)
        
        # Añadir resultado al treeview
        self.results_tree.insert("", "end", values=(
            self.current_exercise + 1,
            textwrap.shorten(esp, width=30, placeholder="..."),
            textwrap.shorten(user_answer, width=30, placeholder="..."),
            textwrap.shorten(correct_eng, width=30, placeholder="..."),
            result
        ))
        
        self.check_button.config(state="disabled")
        self.next_button.config(state="normal")
    
    def next_exercise(self):
        self.current_exercise += 1
        self.show_exercise()
    
    def finish_practice(self):
        # Calcular porcentaje
        percentage = (self.score / len(self.exercise_list)) * 100 if self.exercise_list else 0
        
        # Actualizar estadísticas
        self.score_label.config(text=f"{self.score}/{len(self.exercise_list)}")
        self.percentage_label.config(text=f"{percentage:.1f}%")
        self.completed_label.config(text=f"{len(self.exercise_list)}")
        
        # Calcular estadísticas por tipo
        type_stats = {}
        for esp, eng, tipo, dificultad in self.exercise_list:
            if tipo not in type_stats:
                type_stats[tipo] = {"total": 0, "correct": 0}
            
            # Buscar en el treeview los resultados por tipo
            for item in self.results_tree.get_children():
                values = self.results_tree.item(item, "values")
                if values and values[4] in ["Correcto", "Parcial"]:  # Índice 4 es el resultado
                    type_stats[tipo]["correct"] += 1 if values[4] == "Correcto" else 0.5
                type_stats[tipo]["total"] += 1
        
        stats_text = ", ".join([f"{k}: {v['correct']}/{v['total']}" for k, v in type_stats.items()])
        self.by_type_label.config(text=stats_text)
        
        # Mostrar mensaje de resultado
        if percentage >= 90:
            message = "🎖️ ¡Excelente! Dominas las estructuras gramaticales."
        elif percentage >= 70:
            message = "👍 ¡Buen trabajo! Sigues mejorando."
        elif percentage >= 50:
            message = "👌 No está mal. Sigue practicando."
        else:
            message = "💪 Necesitas más práctica. ¡Sigue intentándolo!"
        
        messagebox.showinfo("Resultados Finales", f"{message}\n\nPuntuación: {self.score}/{len(self.exercise_list)}\nPorcentaje: {percentage:.1f}%")
        
        # Ir a la pestaña de resultados
        self.notebook.select(3)
    
    def export_results(self):
        # Esta función exportaría los resultados a un archivo (no implementado completamente)
        messagebox.showinfo("Exportar", "Función de exportación no implementada completamente")

def main():
    root = tk.Tk()
    app = SentencePracticeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
