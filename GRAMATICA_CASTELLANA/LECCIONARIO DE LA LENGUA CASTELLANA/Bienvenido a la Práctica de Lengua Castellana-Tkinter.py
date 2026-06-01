import tkinter as tk
from tkinter import messagebox
import random

# --- Datos de ejemplo para ejercicios (mismos que antes) ---
EJERCICIOS_DATA = {
    "Ortografía": {
        "Básico": {
            "Uso correcto de tildes": [
                {"pregunta": "¿Qué palabra necesita tilde: 'examen' o 'arbol'?", "tipo": "seleccion_multiple", "opciones": ["examen", "arbol"], "respuesta": "arbol", "explicacion": "Árbol lleva tilde porque es una palabra grave terminada en 'l'."},
                {"pregunta": "Completa con 'el' o 'él': '___ es mi amigo, y ___ perro es suyo.'", "tipo": "completar_oraciones", "respuesta": ["él", "el"], "explicacion": "'Él' es pronombre personal y 'el' es artículo."},
                {"pregunta": "Detecta el error: 'La cancion me gusto mucho.'", "tipo": "detectar_errores", "respuesta": {"palabra_erronea": "cancion", "correccion": "canción"}, "explicacion": "Canción lleva tilde por ser palabra aguda terminada en 'n'."},
            ],
            "Selección múltiple": [
                {"pregunta": "¿Cuál de las siguientes palabras está escrita correctamente?", "tipo": "seleccion_multiple", "opciones": ["vaca", "baca"], "respuesta": "vaca", "explicacion": "Vaca (animal) se escribe con 'v'."}
            ]
        },
        "Intermedio": {
            "Uso correcto de tildes": [
                {"pregunta": "¿Qué palabra necesita tilde: 'telefono' o 'mesa'?", "tipo": "seleccion_multiple", "opciones": ["telefono", "mesa"], "respuesta": "telefono", "explicacion": "Teléfono lleva tilde porque es una palabra esdrújula."},
                {"pregunta": "Completa con 'mas' o 'más': 'Quiero ___ tiempo para estudiar.'", "tipo": "completar_oraciones", "respuesta": ["más"], "explicacion": "'Más' lleva tilde cuando es adverbio de cantidad."},
            ]
        }
    },
    "Morfología": {
        "Básico": {
            "Clasificación de palabras": [
                {"pregunta": "Clasifica 'casa': ¿sustantivo, verbo o adjetivo?", "tipo": "seleccion_multiple", "opciones": ["sustantivo", "verbo", "adjetivo"], "respuesta": "sustantivo", "explicacion": "Casa es una palabra que nombra una cosa, por lo tanto es un sustantivo."},
            ],
            "Conjugación verbal": [
                {"pregunta": "Conjuga el verbo 'cantar' en presente, primera persona singular.", "tipo": "conjugacion_verbal", "respuesta": "canto", "explicacion": "Yo canto."},
            ]
        }
    },
    "Sintaxis": {
        "Básico": {
            "Reorganizar oraciones": [
                {"pregunta": "Ordena las palabras: 'come / Manzanas / Juan'.", "tipo": "reorganizar_oraciones", "respuesta": "Juan come manzanas.", "explicacion": "El orden lógico es Sujeto + Verbo + Objeto."},
                {"pregunta": "Ordena las palabras: 'es / Mi / grande / casa'.", "tipo": "reorganizar_oraciones", "respuesta": "Mi casa es grande.", "explicacion": "El orden lógico es Posesivo + Sustantivo + Verbo + Adjetivo."},
            ]
        }
    }
}

# --- Clase Principal de la Aplicación ---
class App:
    def __init__(self, master):
        self.master = master
        master.title("Práctica de Lengua Castellana")
        master.geometry("600x400") # Tamaño de la ventana

        self.current_frame = None
        self.current_area = None
        self.current_nivel = None
        self.current_tipo_ejercicio = None
        self.exercises_to_run = []
        self.current_exercise_index = 0
        self.score = 0

        self.show_main_menu()

    def clear_frame(self):
        """Destruye todos los widgets del frame actual."""
        if self.current_frame:
            for widget in self.current_frame.winfo_children():
                widget.destroy()
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.master, padx=20, pady=20)
        self.current_frame.pack(fill="both", expand=True)

    def show_main_menu(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="✨ ¡Bienvenido a la Práctica de Lengua Castellana! ✨", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(self.current_frame, text="1. Empezar a practicar", command=self.show_area_selection, width=30, height=2).pack(pady=5)
        tk.Button(self.current_frame, text="2. Salir", command=self.master.quit, width=30, height=2).pack(pady=5)

    def show_area_selection(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="📚 Selecciona un Área del Lenguaje:", font=("Arial", 14, "bold")).pack(pady=10)
        
        areas = list(EJERCICIOS_DATA.keys())
        for i, area in enumerate(areas):
            tk.Button(self.current_frame, text=f"{i + 1}. {area}", command=lambda a=area: self.show_level_selection(a), width=30, height=1).pack(pady=2)
        
        tk.Button(self.current_frame, text="Volver al Menú Principal", command=self.show_main_menu, width=30).pack(pady=10)

    def show_level_selection(self, area):
        self.clear_area = area # Guardar la selección
        self.clear_frame()
        tk.Label(self.current_frame, text=f"🎯 Nivel para {area}:", font=("Arial", 14, "bold")).pack(pady=10)

        niveles = list(EJERCICIOS_DATA[area].keys())
        for i, nivel in enumerate(niveles):
            tk.Button(self.current_frame, text=f"{i + 1}. {nivel}", command=lambda n=nivel: self.show_exercise_type_selection(area, n), width=30, height=1).pack(pady=2)
        
        tk.Button(self.current_frame, text="Volver a Áreas", command=self.show_area_selection, width=30).pack(pady=10)

    def show_exercise_type_selection(self, area, nivel):
        self.current_area = area
        self.current_nivel = nivel
        self.clear_frame()
        tk.Label(self.current_frame, text=f"🧪 Tipos de Ejercicio para {area} - {nivel}:", font=("Arial", 14, "bold")).pack(pady=10)

        tipos_ejercicios = list(EJERCICIOS_DATA[area][nivel].keys())
        for i, tipo in enumerate(tipos_ejercicios):
            tk.Button(self.current_frame, text=f"{i + 1}. {tipo}", command=lambda t=tipo: self.start_exercises(area, nivel, t), width=30, height=1).pack(pady=2)
        
        tk.Button(self.current_frame, text="Volver a Niveles", command=lambda: self.show_level_selection(area), width=30).pack(pady=10)

    def start_exercises(self, area, nivel, tipo_ejercicio):
        self.current_tipo_ejercicio = tipo_ejercicio
        self.exercises_to_run = list(EJERCICIOS_DATA[area][nivel][tipo_ejercicio])
        random.shuffle(self.exercises_to_run)
        self.current_exercise_index = 0
        self.score = 0
        self.display_next_exercise()

    def display_next_exercise(self):
        self.clear_frame()
        if self.current_exercise_index < len(self.exercises_to_run):
            ejercicio = self.exercises_to_run[self.current_exercise_index]
            tk.Label(self.current_frame, text=f"Pregunta {self.current_exercise_index + 1}:", font=("Arial", 12, "bold")).pack(pady=5)
            tk.Label(self.current_frame, text=ejercicio['pregunta'], font=("Arial", 12)).pack(pady=5)

            # --- Renderizar según el tipo de ejercicio ---
            if ejercicio['tipo'] == 'seleccion_multiple':
                self.selected_option = tk.StringVar(value="")
                for i, option in enumerate(ejercicio['opciones']):
                    tk.Radiobutton(self.current_frame, text=option, variable=self.selected_option, value=option).pack(anchor="w")
                tk.Button(self.current_frame, text="Comprobar", command=lambda: self.check_answer_multiple_choice(ejercicio)).pack(pady=10)

            elif ejercicio['tipo'] == 'completar_oraciones':
                self.user_entries = []
                num_espacios = ejercicio['pregunta'].count('___')
                labels_and_entries_frame = tk.Frame(self.current_frame)
                labels_and_entries_frame.pack()
                
                parts = ejercicio['pregunta'].split('___')
                for i, part in enumerate(parts):
                    if part:
                        tk.Label(labels_and_entries_frame, text=part).pack(side="left")
                    if i < num_espacios:
                        entry = tk.Entry(labels_and_entries_frame, width=15)
                        entry.pack(side="left", padx=2)
                        self.user_entries.append(entry)
                
                tk.Button(self.current_frame, text="Comprobar", command=lambda: self.check_answer_complete_sentences(ejercicio)).pack(pady=10)
            
            elif ejercicio['tipo'] == 'detectar_errores':
                tk.Label(self.current_frame, text=ejercicio['pregunta'], font=("Arial", 12)).pack(pady=5)
                tk.Label(self.current_frame, text="Palabra errónea:", font=("Arial", 10)).pack(anchor="w")
                self.error_word_entry = tk.Entry(self.current_frame, width=30)
                self.error_word_entry.pack(pady=2, anchor="w")
                tk.Label(self.current_frame, text="Corrección:", font=("Arial", 10)).pack(anchor="w")
                self.correction_entry = tk.Entry(self.current_frame, width=30)
                self.correction_entry.pack(pady=2, anchor="w")
                tk.Button(self.current_frame, text="Comprobar", command=lambda: self.check_answer_detect_errors(ejercicio)).pack(pady=10)

            elif ejercicio['tipo'] == 'reorganizar_oraciones':
                tk.Label(self.current_frame, text="Ordena las palabras:", font=("Arial", 10)).pack(anchor="w")
                tk.Label(self.current_frame, text=ejercicio['pregunta'], font=("Arial", 12, "italic")).pack(pady=5)
                self.reorder_entry = tk.Entry(self.current_frame, width=50)
                self.reorder_entry.pack(pady=5)
                tk.Button(self.current_frame, text="Comprobar", command=lambda: self.check_answer_reorder(ejercicio)).pack(pady=10)

            elif ejercicio['tipo'] == 'clasificacion_de_palabras':
                self.classification_entry = tk.Entry(self.current_frame, width=30)
                self.classification_entry.pack(pady=5)
                tk.Button(self.current_frame, text="Comprobar", command=lambda: self.check_answer_classification(ejercicio)).pack(pady=10)

            elif ejercicio['tipo'] == 'conjugacion_verbal':
                self.conjugation_entry = tk.Entry(self.current_frame, width=30)
                self.conjugation_entry.pack(pady=5)
                tk.Button(self.current_frame, text="Comprobar", command=lambda: self.check_answer_conjugation(ejercicio)).pack(pady=10)
            
            else:
                tk.Label(self.current_frame, text="Tipo de ejercicio no implementado aún en la GUI.", fg="red").pack(pady=10)
                tk.Button(self.current_frame, text="Siguiente Ejercicio", command=self.go_to_next_exercise).pack(pady=10)

        else:
            self.show_results()

    # --- Métodos de Comprobación de Respuestas ---
    def check_answer_multiple_choice(self, ejercicio):
        user_answer = self.selected_option.get().lower()
        correct = (user_answer == ejercicio['respuesta'].lower())
        self.show_feedback(correct, ejercicio)

    def check_answer_complete_sentences(self, ejercicio):
        user_answers = [entry.get().strip().lower() for entry in self.user_entries]
        correct_answers_normalized = [r.lower() for r in ejercicio['respuesta']]
        correct = (user_answers == correct_answers_normalized)
        self.show_feedback(correct, ejercicio)

    def check_answer_detect_errors(self, ejercicio):
        error_word = self.error_word_entry.get().strip().lower()
        correction = self.correction_entry.get().strip().lower()
        correct = (error_word == ejercicio['respuesta']['palabra_erronea'].lower() and
                   correction == ejercicio['respuesta']['correccion'].lower())
        self.show_feedback(correct, ejercicio)

    def check_answer_reorder(self, ejercicio):
        user_answer = self.reorder_entry.get().strip()
        # Para reorganizar, podemos ser un poco más flexibles o muy estrictos.
        # Por ahora, comparación directa después de normalizar espacios.
        normalized_user_answer = ' '.join(user_answer.split()).lower()
        normalized_correct_answer = ' '.join(ejercicio['respuesta'].split()).lower()
        
        correct = (normalized_user_answer == normalized_correct_answer)
        self.show_feedback(correct, ejercicio)

    def check_answer_classification(self, ejercicio):
        user_answer = self.classification_entry.get().strip().lower()
        correct = (user_answer == ejercicio['respuesta'].lower())
        self.show_feedback(correct, ejercicio)

    def check_answer_conjugation(self, ejercicio):
        user_answer = self.conjugation_entry.get().strip().lower()
        correct = (user_answer == ejercicio['respuesta'].lower())
        self.show_feedback(correct, ejercicio)

    def show_feedback(self, is_correct, ejercicio):
        feedback_message = ""
        if is_correct:
            self.score += 1
            feedback_message = f"¡Correcto! ✅\n"
        else:
            feedback_message = f"Incorrecto. ❌\n"
        
        feedback_message += f"Explicación: {ejercicio['explicacion']}"
        
        messagebox.showinfo("Feedback", feedback_message)
        self.go_to_next_exercise()

    def go_to_next_exercise(self):
        self.current_exercise_index += 1
        self.display_next_exercise()

    def show_results(self):
        self.clear_frame()
        tk.Label(self.current_frame, text="--- ¡Sesión de Práctica Terminada! ---", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.current_frame, text=f"Obtuviste {self.score} de {len(self.exercises_to_run)} preguntas correctas.", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.current_frame, text="¡Sigue practicando para mejorar! 💪", font=("Arial", 12)).pack(pady=10)
        tk.Button(self.current_frame, text="Volver al Menú Principal", command=self.show_main_menu, width=30).pack(pady=10)

# --- Punto de entrada de la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
