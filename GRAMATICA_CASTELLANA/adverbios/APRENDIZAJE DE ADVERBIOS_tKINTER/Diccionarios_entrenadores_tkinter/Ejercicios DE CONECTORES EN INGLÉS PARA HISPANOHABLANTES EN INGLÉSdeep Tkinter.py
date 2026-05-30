import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from datetime import datetime

class EnglishQuestionsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏆 Entrenador de Preguntas en Inglés - Para Hispanohablantes")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f8ff')
        
        # Variables del programa
        self.exercises = self.initialize_exercises()
        self.current_exercise_index = 0
        self.score = 0
        self.completed_exercises = 0
        self.start_time = datetime.now()
        self.mastered_structures = set()
        self.hints_used = 0
        
        # Cargar ejercicios completos
        self.all_exercises = self.complete_100_exercises()
        
        self.setup_gui()
        self.load_exercise()

    def initialize_exercises(self):
        return [
            {
                "type": "Preguntas con 'to be' - Presente",
                "instruction": "Convierte la afirmación en pregunta usando 'to be' en presente:",
                "spanish_sentence": "Él es profesor",
                "correct_answer": "Is he a teacher?",
                "hint": "Recuerda invertir el orden: Verbo + Sujeto + Complemento",
                "difficulty": "básico"
            },
            {
                "type": "Preguntas con 'to be' - Presente",
                "instruction": "Convierte la afirmación en pregunta usando 'to be' en presente:",
                "spanish_sentence": "Ellos están en casa",
                "correct_answer": "Are they at home?",
                "hint": "They → they, 'están' → are",
                "difficulty": "básico"
            },
            {
                "type": "Preguntas con Do/Does - Presente",
                "instruction": "Convierte en pregunta usando Do/Does:",
                "spanish_sentence": "Ella trabaja aquí",
                "correct_answer": "Does she work here?",
                "hint": "She/he/it → DOES + verbo en forma base (sin -s)",
                "difficulty": "básico"
            },
            {
                "type": "Preguntas con Do/Does - Presente",
                "instruction": "Convierte en pregunta usando Do/Does:",
                "spanish_sentence": "Nosotros vivimos en Madrid",
                "correct_answer": "Do we live in Madrid?",
                "hint": "I/you/we/they → DO + verbo en forma base",
                "difficulty": "básico"
            },
            {
                "type": "Preguntas con What",
                "instruction": "Formula una pregunta con WHAT para esta respuesta:",
                "spanish_sentence": "RESPUESTA: I want a coffee",
                "correct_answer": "What do you want?",
                "hint": "What + do/does/did + sujeto + verbo",
                "difficulty": "intermedio"
            },
            {
                "type": "Preguntas con Where",
                "instruction": "Formula una pregunta con WHERE:",
                "spanish_sentence": "RESPUESTA: She lives in London",
                "correct_answer": "Where does she live?",
                "hint": "Where + does + she + live?",
                "difficulty": "intermedio"
            },
            {
                "type": "Preguntas con Who como sujeto",
                "instruction": "Formula la pregunta correctamente:",
                "spanish_sentence": "¿Quién llamó a la puerta?",
                "correct_answer": "Who called at the door?",
                "hint": "Cuando Who es sujeto, NO usa auxiliar",
                "difficulty": "avanzado"
            },
            {
                "type": "Preguntas indirectas",
                "instruction": "Convierte en pregunta indirecta (más formal):",
                "spanish_sentence": "¿Dónde está el banco?",
                "correct_answer": "Could you tell me where the bank is?",
                "hint": "Frase introductoria + orden afirmativo: where the bank IS (no 'is the bank')",
                "difficulty": "avanzado"
            },
            {
                "type": "Question Tags",
                "instruction": "Añade la question tag correcta:",
                "spanish_sentence": "She is beautiful",
                "correct_answer": "She is beautiful, isn't she?",
                "hint": "Afirmativo → tag negativo. Mismo auxiliar que la frase principal",
                "difficulty": "intermedio"
            }
        ]

    def complete_100_exercises(self):
        base_exercises = self.exercises
        completed_exercises = []

        variations = [
            {"trabajar": "enseñar", "oficina": "escuela", "profesor": "maestro"},
            {"estudiar": "aprender", "inglés": "francés", "café": "té"},
            {"vivir": "trabajar", "Madrid": "Barcelona", "Londres": "París"},
            {"querer": "necesitar", "llamar": "visitar", "banco": "hospital"}
        ]

        for i in range(4):
            for exercise in base_exercises:
                new_exercise = exercise.copy()
                variation = variations[i % len(variations)]

                modified_spanish = new_exercise["spanish_sentence"]
                modified_answer = new_exercise["correct_answer"]

                for original, replacement in variation.items():
                    if original.lower() in modified_spanish.lower():
                        modified_spanish = modified_spanish.replace(original, replacement)
                        modified_answer = modified_answer.replace(original, replacement)

                completed_exercises.append({
                    "type": new_exercise["type"],
                    "instruction": new_exercise["instruction"],
                    "spanish_sentence": modified_spanish,
                    "correct_answer": modified_answer,
                    "hint": new_exercise["hint"],
                    "difficulty": new_exercise["difficulty"]
                })

        random.shuffle(completed_exercises)
        return completed_exercises[:100]

    def setup_gui(self):
        # Configurar estilo
        style = ttk.Style()
        style.configure('TFrame', background='#f0f8ff')
        style.configure('TLabel', background='#f0f8ff', font=('Arial', 10))
        style.configure('Title.TLabel', background='#f0f8ff', font=('Arial', 14, 'bold'))
        style.configure('TButton', font=('Arial', 10))
        style.configure('Success.TButton', background='#4CAF50', foreground='white')
        style.configure('Warning.TButton', background='#FF9800', foreground='white')
        style.configure('Danger.TButton', background='#f44336', foreground='white')

        # Marco principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Título
        title_label = ttk.Label(main_frame, text="🏆 ENTRENADOR DE PREGUNTAS EN INGLÉS", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Panel de progreso
        self.setup_progress_panel(main_frame)

        # Panel del ejercicio
        self.setup_exercise_panel(main_frame)

        # Panel de controles
        self.setup_control_panel(main_frame)

        # Panel de estadísticas
        self.setup_stats_panel(main_frame)

    def setup_progress_panel(self, parent):
        progress_frame = ttk.LabelFrame(parent, text="📊 Progreso", padding="10")
        progress_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        progress_frame.columnconfigure(1, weight=1)

        # Barra de progreso
        self.progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
        progress_bar.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 5))

        # Labels de progreso
        self.progress_label = ttk.Label(progress_frame, text="Ejercicio 0/100 - 0%")
        self.progress_label.grid(row=1, column=0, columnspan=3)

        # Score y tiempo
        stats_frame = ttk.Frame(progress_frame)
        stats_frame.grid(row=2, column=0, columnspan=3, pady=(5, 0))

        self.score_label = ttk.Label(stats_frame, text="Puntuación: 0")
        self.score_label.pack(side=tk.LEFT, padx=(0, 20))

        self.time_label = ttk.Label(stats_frame, text="Tiempo: 00:00")
        self.time_label.pack(side=tk.LEFT)

    def setup_exercise_panel(self, parent):
        exercise_frame = ttk.LabelFrame(parent, text="🎯 Ejercicio Actual", padding="15")
        exercise_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        exercise_frame.columnconfigure(1, weight=1)

        # Información del ejercicio
        self.type_label = ttk.Label(exercise_frame, text="", style='Title.TLabel')
        self.type_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        self.instruction_label = ttk.Label(exercise_frame, text="", font=('Arial', 11, 'bold'))
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        self.spanish_label = ttk.Label(exercise_frame, text="", font=('Arial', 11))
        self.spanish_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 20))

        # Campo de respuesta
        ttk.Label(exercise_frame, text="Tu respuesta:").grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        
        self.answer_entry = tk.Text(exercise_frame, height=3, width=50, font=('Arial', 10))
        self.answer_entry.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Bind Enter key to submit
        self.answer_entry.bind('<KeyPress>', self.on_key_press)

        # Área de feedback
        self.feedback_text = scrolledtext.ScrolledText(exercise_frame, height=4, width=50, 
                                                      font=('Arial', 9), state=tk.DISABLED)
        self.feedback_text.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))

    def setup_control_panel(self, parent):
        control_frame = ttk.Frame(parent)
        control_frame.grid(row=3, column=0, columnspan=3, pady=(0, 10))

        # Botones
        self.submit_btn = ttk.Button(control_frame, text="✅ Enviar Respuesta", 
                                   command=self.check_answer)
        self.submit_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.hint_btn = ttk.Button(control_frame, text="💡 Mostrar Pista", 
                                 command=self.show_hint, style='Warning.TButton')
        self.hint_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.skip_btn = ttk.Button(control_frame, text="⏭️ Saltar Ejercicio", 
                                 command=self.skip_exercise, style='Danger.TButton')
        self.skip_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.stats_btn = ttk.Button(control_frame, text="📈 Estadísticas", 
                                  command=self.show_statistics)
        self.stats_btn.pack(side=tk.LEFT)

    def setup_stats_panel(self, parent):
        stats_frame = ttk.LabelFrame(parent, text="📈 Estadísticas Detalladas", padding="10")
        stats_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        parent.rowconfigure(4, weight=1)

        # Treeview para estadísticas
        columns = ('Categoría', 'Ejercicios', 'Correctos', 'Porcentaje')
        self.stats_tree = ttk.Treeview(stats_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.stats_tree.heading(col, text=col)
            self.stats_tree.column(col, width=120)

        self.stats_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar para el treeview
        scrollbar = ttk.Scrollbar(stats_frame, orient=tk.VERTICAL, command=self.stats_tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.stats_tree.configure(yscrollcommand=scrollbar.set)

        stats_frame.columnconfigure(0, weight=1)
        stats_frame.rowconfigure(0, weight=1)

    def on_key_press(self, event):
        if event.keysym == 'Return' and event.state == 0:  # Enter sin Ctrl
            self.check_answer()
            return "break"  # Prevenir nueva línea
        return True

    def load_exercise(self):
        if self.current_exercise_index >= len(self.all_exercises):
            self.show_final_results()
            return

        exercise = self.all_exercises[self.current_exercise_index]
        
        # Actualizar interfaz
        self.type_label.config(text=f"{exercise['type']} - [{exercise['difficulty'].upper()}]")
        self.instruction_label.config(text=exercise['instruction'])
        self.spanish_label.config(text=f"🔸 {exercise['spanish_sentence']}")
        
        # Limpiar campos
        self.answer_entry.delete('1.0', tk.END)
        self.feedback_text.config(state=tk.NORMAL)
        self.feedback_text.delete('1.0', tk.END)
        self.feedback_text.config(state=tk.DISABLED)
        
        # Actualizar progreso
        self.update_progress()

    def update_progress(self):
        # Barra de progreso
        progress = (self.current_exercise_index / len(self.all_exercises)) * 100
        self.progress_var.set(progress)
        
        # Labels
        self.progress_label.config(
            text=f"Ejercicio {self.current_exercise_index + 1}/{len(self.all_exercises)} - {progress:.1f}%"
        )
        
        # Puntuación
        self.score_label.config(text=f"Puntuación: {self.score}")
        
        # Tiempo
        elapsed = datetime.now() - self.start_time
        minutes = elapsed.seconds // 60
        seconds = elapsed.seconds % 60
        self.time_label.config(text=f"Tiempo: {minutes:02d}:{seconds:02d}")

    def check_answer(self):
        user_answer = self.answer_entry.get('1.0', tk.END).strip()
        if not user_answer:
            messagebox.showwarning("Advertencia", "Por favor, escribe una respuesta.")
            return

        exercise = self.all_exercises[self.current_exercise_index]
        is_correct, feedback = self.verify_answer(user_answer, exercise['correct_answer'])

        # Mostrar feedback
        self.feedback_text.config(state=tk.NORMAL)
        self.feedback_text.delete('1.0', tk.END)
        
        if is_correct:
            self.feedback_text.insert(tk.END, "✅ ¡CORRECTO!\n\n", 'success')
            self.score += 2 if feedback == "exacta" else 1
            self.mastered_structures.add(exercise['type'])
        else:
            self.feedback_text.insert(tk.END, "❌ INCORRECTO\n\n", 'error')
        
        self.feedback_text.insert(tk.END, f"Respuesta correcta: {exercise['correct_answer']}\n\n")
        self.feedback_text.insert(tk.END, f"Explicación: {exercise['hint']}")
        
        # Configurar tags para colores
        self.feedback_text.tag_config('success', foreground='green', font=('Arial', 10, 'bold'))
        self.feedback_text.tag_config('error', foreground='red', font=('Arial', 10, 'bold'))
        
        self.feedback_text.config(state=tk.DISABLED)

        # Actualizar estadísticas
        self.update_statistics()
        
        # Preparar siguiente ejercicio después de 3 segundos
        self.root.after(3000, self.next_exercise)

    def verify_answer(self, user_answer, correct_answer):
        def normalize(text):
            return text.strip().lower().replace("'", "").replace("  ", " ")
        
        user_norm = normalize(user_answer)
        correct_norm = normalize(correct_answer)
        
        if user_norm == correct_norm:
            return True, "exacta"
        
        user_words = set(user_norm.split())
        correct_words = set(correct_norm.split())
        
        match_percentage = len(user_words.intersection(correct_words)) / len(correct_words)
        
        if match_percentage >= 0.8:
            return True, "aproximada"
        
        return False, "incorrecta"

    def show_hint(self):
        exercise = self.all_exercises[self.current_exercise_index]
        self.hints_used += 1
        
        self.feedback_text.config(state=tk.NORMAL)
        self.feedback_text.delete('1.0', tk.END)
        self.feedback_text.insert(tk.END, f"💡 PISTA: {exercise['hint']}")
        self.feedback_text.config(state=tk.DISABLED)

    def skip_exercise(self):
        result = messagebox.askyesno("Saltar ejercicio", 
                                   "¿Estás seguro de que quieres saltar este ejercicio?")
        if result:
            self.next_exercise()

    def next_exercise(self):
        self.current_exercise_index += 1
        self.completed_exercises += 1
        
        if self.current_exercise_index < len(self.all_exercises):
            self.load_exercise()
        else:
            self.show_final_results()

    def update_statistics(self):
        # Limpiar treeview
        for item in self.stats_tree.get_children():
            self.stats_tree.delete(item)
        
        # Calcular estadísticas por categoría
        category_stats = {}
        for i in range(self.current_exercise_index + 1):
            if i < len(self.all_exercises):
                exercise = self.all_exercises[i]
                cat = exercise['type']
                if cat not in category_stats:
                    category_stats[cat] = {'total': 0, 'correct': 0}
                category_stats[cat]['total'] += 1
                # Aquí deberías llevar un registro más detallado de respuestas correctas
        
        # Agregar datos al treeview (esto es un ejemplo simplificado)
        for category, stats in category_stats.items():
            percentage = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
            self.stats_tree.insert('', tk.END, values=(
                category, stats['total'], stats['correct'], f"{percentage:.1f}%"
            ))

    def show_statistics(self):
        stats_window = tk.Toplevel(self.root)
        stats_window.title("📊 Estadísticas Detalladas")
        stats_window.geometry("600x400")
        stats_window.configure(bg='#f0f8ff')
        
        # Aquí puedes mostrar estadísticas más detalladas
        ttk.Label(stats_window, text="Estadísticas en desarrollo...", 
                 font=('Arial', 12)).pack(pady=20)

    def show_final_results(self):
        total_time = datetime.now() - self.start_time
        minutes = total_time.seconds // 60
        seconds = total_time.seconds % 60
        
        accuracy = (self.score / (len(self.all_exercises) * 2)) * 100
        
        result_text = f"""
🎓 RESULTADOS FINALES

📊 Ejercicios completados: {self.completed_exercises}/100
✅ Puntuación final: {self.score}/{(len(self.all_exercises) * 2)}
📈 Porcentaje de acierto: {accuracy:.1f}%
⏱️ Tiempo total: {minutes:02d}:{seconds:02d}
💡 Pistas usadas: {self.hints_used}
🔗 Estructuras dominadas: {len(self.mastered_structures)}

"""
        if accuracy >= 90:
            result_text += "🏆 ¡EXCELENTE! Dominas la formación de preguntas"
        elif accuracy >= 70:
            result_text += "👍 ¡MUY BIEN! Buen dominio de estructuras interrogativas"
        elif accuracy >= 50:
            result_text += "📚 ¡BIEN! Bases sólidas, sigue practicando"
        else:
            result_text += "💪 ¡EN DESARROLLO! La práctica es clave"

        messagebox.showinfo("🏆 Entrenamiento Completado", result_text)
        
        # Preguntar si quiere reiniciar
        if messagebox.askyesno("Reiniciar", "¿Quieres reiniciar el entrenamiento?"):
            self.restart_training()

    def restart_training(self):
        self.current_exercise_index = 0
        self.score = 0
        self.completed_exercises = 0
        self.start_time = datetime.now()
        self.mastered_structures = set()
        self.hints_used = 0
        
        # Re-mezclar ejercicios
        random.shuffle(self.all_exercises)
        
        self.load_exercise()

def main():
    root = tk.Tk()
    app = EnglishQuestionsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
