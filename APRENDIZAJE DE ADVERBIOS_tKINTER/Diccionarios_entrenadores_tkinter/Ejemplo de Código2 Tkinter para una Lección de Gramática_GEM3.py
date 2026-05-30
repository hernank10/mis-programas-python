import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import json
import os
import re
import threading
import time
import uuid # Para IDs únicos, si los necesitas

# --- Librerías de Voz y Audio ---
from gtts import gTTS
from playsound import playsound
import sounddevice as sd
import numpy as np
import wavio
import speech_recognition as sr # Para STT (reconocimiento de voz a texto)
# --- Fin Librerías de Voz y Audio ---

class GrammarLessonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("El Castellañol: Tu Asistente de Escritura")
        self.root.geometry("1000x750")

        # --- Archivos de Datos ---
        self.user_progress_file = "user_progress.json"
        self.lessons_data_file = "lessons_data.json"
        self.templates_data_file = "templates_data.json"
        self.exercises_data_file = "exercises_data.json"
        self.phonetics_data_file = "phonetics_data.json" # Para la pestaña de fonética

        # --- Cargar Datos ---
        self.user_portfolio = []
        self.lessons_data = {}
        self.categorized_templates_data = {}
        self.exercises_data = {"ejercicios": []}
        self.phonetics_data = []

        self._load_user_progress()
        self._load_lessons_data()
        self._load_templates_data()
        self._load_exercises_data()
        self._load_phonetics_data()

        # --- Variables de Estado para Grabación ---
        self.recording = False
        self.audio_data = []
        self.samplerate = 44100
        self.channels = 1
        self.user_audio_filename = "temp_user_recording.wav"

        # --- Interfaz Principal ---
        self._create_main_notebook()

    # --- Métodos de Carga de Datos ---
    def _load_json_data(self, filename, default_value={}):
        """Carga datos de un archivo JSON, con manejo de errores y valor por defecto."""
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                messagebox.showwarning("Advertencia", f"No se encontró el archivo {filename}. Se usará un valor por defecto.")
                return default_value
        except json.JSONDecodeError as e:
            messagebox.showerror("Error JSON", f"Error al leer {filename}: {e}. El archivo puede estar corrupto.")
            return default_value
        except Exception as e:
            messagebox.showerror("Error de Carga", f"Error al cargar {filename}: {e}")
            return default_value

    def _load_user_progress(self):
        self.user_progress = self._load_json_data(self.user_progress_file, {"portfolio": [], "completed_exercises": [], "challenge_records": []})
        self.user_portfolio = self.user_progress.get("portfolio", [])

    def _load_lessons_data(self):
        self.lessons_data = self._load_json_data(self.lessons_data_file, {})

    def _load_templates_data(self):
        # La carga de plantillas necesita una estructura específica
        raw_templates = self._load_json_data(self.templates_data_file, {})
        self.categorized_templates_data = raw_templates # Asume que el JSON ya viene categorizado

    def _load_exercises_data(self):
        self.exercises_data = self._load_json_data(self.exercises_data_file, {"ejercicios": []})

    def _load_phonetics_data(self):
        self.phonetics_data = self._load_json_data(self.phonetics_data_file, [])


    # --- Utilidades de Voz (TTS y Grabación) ---
    def _speak_text(self, text, lang='es'):
        """Convierte texto a voz y lo reproduce en un hilo separado."""
        def _actual_speak():
            try:
                tts = gTTS(text=text, lang=lang, slow=False)
                temp_filename = "temp_tts_audio.mp3"
                tts.save(temp_filename)
                playsound(temp_filename)
                os.remove(temp_filename)
            except Exception as e:
                messagebox.showerror("Error de Voz", f"No se pudo reproducir el audio: {e}")
        threading.Thread(target=_actual_speak).start()

    def _start_recording(self, status_label):
        self.recording = True
        self.audio_data = []
        status_label.config(text="Grabando... Hable ahora.")
        # Desactivar botones relevantes durante la grabación si aplica
        # self.record_button.config(state=tk.DISABLED) # Si son accesibles desde aquí
        # self.stop_button.config(state=tk.NORMAL)

        self.record_thread = threading.Thread(target=self._record_audio_thread, args=(status_label,))
        self.record_thread.start()

    def _record_audio_thread(self, status_label):
        """Función que ejecuta la grabación en un hilo."""
        try:
            with sd.InputStream(samplerate=self.samplerate, channels=self.channels, dtype='float32') as stream:
                while self.recording:
                    chunk, overflowed = stream.read(int(self.samplerate * 0.1))
                    self.audio_data.append(chunk)
            status_label.config(text="Grabación finalizada.")
        except Exception as e:
            messagebox.showerror("Error de Grabación", f"Error durante la grabación: {e}")
            status_label.config(text="Error de grabación.")
            self.recording = False

    def _stop_recording(self, status_label):
        self.recording = False
        if hasattr(self, 'record_thread') and self.record_thread.is_alive():
            self.record_thread.join() # Esperar a que el hilo termine

        if self.audio_data:
            audio_array = np.concatenate(self.audio_data, axis=0)
            try:
                wavio.write(self.user_audio_filename, audio_array, self.samplerate, sampwidth=3)
                status_label.config(text=f"Grabación guardada: {self.user_audio_filename}")
                return True # Grabación exitosa
            except Exception as e:
                messagebox.showerror("Error al Guardar", f"No se pudo guardar el archivo de audio: {e}")
                status_label.config(text="Error al guardar grabación.")
                return False
        else:
            status_label.config(text="No se grabó ningún audio.")
            return False

    def _play_recording(self, status_label):
        if os.path.exists(self.user_audio_filename):
            status_label.config(text="Reproduciendo grabación...")
            threading.Thread(target=self._play_audio_thread, args=(status_label,)).start()
        else:
            messagebox.showwarning("Advertencia", "No hay grabación para reproducir.")
            status_label.config(text="No hay grabación.")

    def _play_audio_thread(self, status_label):
        try:
            playsound(self.user_audio_filename)
            status_label.config(text="Reproducción finalizada.")
        except Exception as e:
            messagebox.showerror("Error de Reproducción", f"No se pudo reproducir el audio: {e}")
            status_label.config(text="Error de reproducción.")

    def _recognize_speech_from_mic(self, audio_file_path, status_label):
        """Reconoce voz de un archivo de audio usando Google Web Speech API."""
        r = sr.Recognizer()
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio = r.record(source)
            status_label.config(text="Transcribiendo...")
            # Aquí es donde se podría seleccionar el dialecto más específico (es-ES, es-MX, etc.)
            text = r.recognize_google(audio, language="es-ES")
            return text
        except sr.UnknownValueError:
            status_label.config(text="No se pudo entender el audio.")
            return None
        except sr.RequestError as e:
            status_label.config(text=f"Error al conectar con el servicio de reconocimiento: {e}")
            return None
        except Exception as e:
            status_label.config(text=f"Error inesperado en el reconocimiento: {e}")
            return None


    # --- Creación de Pestañas Principales ---
    def _create_main_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Crear y añadir pestañas
        lessons_tab = ttk.Frame(self.notebook)
        writing_tab = ttk.Frame(self.notebook)
        exercises_tab = ttk.Frame(self.notebook)
        pronunciation_tab = ttk.Frame(self.notebook) # Nueva pestaña de Pronunciación
        phonetics_tab = ttk.Frame(self.notebook)     # Nueva pestaña de Fonética AFI

        self.notebook.add(lessons_tab, text="Lecciones 📚")
        self.notebook.add(writing_tab, text="Redacción Libre ✍️")
        self.notebook.add(exercises_tab, text="Ejercicios ✅")
        self.notebook.add(pronunciation_tab, text="Pronunciación 🗣️")
        self.notebook.add(phonetics_tab, text="Fonética AFI 🔊")

        # Cargar contenido en cada pestaña
        self._create_lessons_tab_content(lessons_tab)
        self._create_writing_tab_content(writing_tab)
        self._create_exercises_tab_content(exercises_tab)
        self._create_pronunciation_tab_content(pronunciation_tab)
        self._create_phonetics_tab_content(phonetics_tab)

    # --- Contenido de la Pestaña de Lecciones ---
    def _create_lessons_tab_content(self, parent_frame):
        lessons_frame = ttk.Frame(parent_frame, padding="15")
        lessons_frame.pack(fill="both", expand=True)

        ttk.Label(lessons_frame, text="Lecciones de Gramática Castellana", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Lista de lecciones
        lessons_list_frame = ttk.Frame(lessons_frame)
        lessons_list_frame.pack(side=tk.LEFT, fill="y", padx=10, pady=10)

        self.lessons_listbox = tk.Listbox(lessons_list_frame, height=15, width=30, font=("Arial", 11))
        for lesson_id, lesson_data in self.lessons_data.items():
            self.lessons_listbox.insert(tk.END, lesson_data['titulo'])
        self.lessons_listbox.pack(side=tk.LEFT, fill="y")

        lessons_scrollbar = ttk.Scrollbar(lessons_list_frame, orient="vertical", command=self.lessons_listbox.yview)
        lessons_scrollbar.pack(side=tk.RIGHT, fill="y")
        self.lessons_listbox.config(yscrollcommand=lessons_scrollbar.set)

        self.lessons_listbox.bind("<<ListboxSelect>>", self._display_lesson_content)

        # Contenido de la lección seleccionada
        self.lesson_content_frame = ttk.Frame(lessons_frame, relief=tk.GROOVE, borderwidth=2)
        self.lesson_content_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)

        self.lesson_title_label = ttk.Label(self.lesson_content_frame, text="Selecciona una lección", font=("Arial", 14, "bold"))
        self.lesson_title_label.pack(pady=5)

        self.lesson_text_display = scrolledtext.ScrolledText(self.lesson_content_frame, wrap=tk.WORD, height=20, font=("Arial", 11))
        self.lesson_text_display.pack(fill="both", expand=True, padx=5, pady=5)
        self.lesson_text_display.config(state=tk.DISABLED)

    def _display_lesson_content(self, event):
        selected_index = self.lessons_listbox.curselection()
        if not selected_index:
            return

        lesson_title = self.lessons_listbox.get(selected_index[0])
        lesson_id = None
        for lid, ldata in self.lessons_data.items():
            if ldata['titulo'] == lesson_title:
                lesson_id = lid
                break

        if lesson_id:
            lesson_data = self.lessons_data[lesson_id]
            self.lesson_title_label.config(text=lesson_data['titulo'])
            self.lesson_text_display.config(state=tk.NORMAL)
            self.lesson_text_display.delete("1.0", tk.END)
            self.lesson_text_display.insert(tk.END, lesson_data['contenido'])
            if 'ejemplos' in lesson_data and lesson_data['ejemplos']:
                self.lesson_text_display.insert(tk.END, "\n\nEjemplos:\n" + "\n".join(lesson_data['ejemplos']))
            self.lesson_text_display.config(state=tk.DISABLED)

            # Botón para leer la lección completa
            ttk.Button(self.lesson_content_frame, text="🔊 Leer Lección", command=lambda: self._speak_text(lesson_data['contenido'])).pack(pady=5)


    # --- Contenido de la Pestaña de Redacción Libre ---
    def _create_writing_tab_content(self, parent_frame):
        writing_frame = ttk.Frame(parent_frame, padding="15")
        writing_frame.pack(fill="both", expand=True)

        ttk.Label(writing_frame, text="Redacción Libre y con Plantillas", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Controles para plantillas
        template_control_frame = ttk.Frame(writing_frame)
        template_control_frame.pack(pady=10, fill="x")

        ttk.Label(template_control_frame, text="Seleccionar Plantilla:").pack(side=tk.LEFT, padx=5)
        self.template_combobox = ttk.Combobox(template_control_frame, state="readonly", width=30)
        self.template_combobox.pack(side=tk.LEFT, padx=5)
        
        template_names = []
        for category, templates in self.categorized_templates_data.items():
            for template_name in templates.keys():
                template_names.append(f"{category}: {template_name}")
        self.template_combobox['values'] = template_names
        self.template_combobox.bind("<<ComboboxSelected>>", self._load_template)

        self.clear_template_button = ttk.Button(template_control_frame, text="Limpiar Plantilla", command=self._clear_template_text)
        self.clear_template_button.pack(side=tk.LEFT, padx=5)

        # Área de escritura
        self.writing_text_area = scrolledtext.ScrolledText(writing_frame, wrap=tk.WORD, height=25, font=("Arial", 12))
        self.writing_text_area.pack(pady=10, fill="both", expand=True)

        # Botones de acción
        action_buttons_frame = ttk.Frame(writing_frame)
        action_buttons_frame.pack(pady=5)

        ttk.Button(action_buttons_frame, text="Guardar Escrito", command=self._save_written_text).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_buttons_frame, text="Limpiar Todo", command=self._clear_writing_area).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_buttons_frame, text="Leer Escrito", command=lambda: self._speak_text(self.writing_text_area.get("1.0", tk.END))).pack(side=tk.LEFT, padx=5)

        # Sugerencias (simplificadas)
        self.suggestion_label = ttk.Label(writing_frame, text="Sugerencias aparecerán aquí.", foreground="blue", font=("Arial", 10, "italic"))
        self.suggestion_label.pack(pady=5)
        self.writing_text_area.bind("<KeyRelease>", self._give_writing_suggestions) # Activar sugerencias al escribir

    def _load_template(self, event=None):
        selected_template_full_name = self.template_combobox.get()
        if not selected_template_full_name:
            return

        category, template_name = selected_template_full_name.split(": ", 1)
        template_data = self.categorized_templates_data.get(category, {}).get(template_name)

        if template_data:
            self.writing_text_area.delete("1.0", tk.END)
            # Construir la plantilla con marcadores
            template_text = template_data.get('descripcion', '') + "\n\n"
            structure = template_data.get('estructura_esperada', {})
            for key, value in structure.items():
                template_text += f"[{key.upper()}] (min. {value.get('min_len', 'N/A')} palabras)\n\n"
            
            self.writing_text_area.insert(tk.END, template_text)
            self.current_writing_expected_structure = structure # Guardar la estructura para futura evaluación
            self.suggestion_label.config(text=f"Plantilla '{template_name}' cargada. ¡Empieza a escribir!")
        else:
            self.suggestion_label.config(text="Error al cargar la plantilla.")

    def _clear_template_text(self):
        self.template_combobox.set('')
        self.current_writing_expected_structure = None
        self.suggestion_label.config(text="Plantilla borrada. Puedes escribir libremente.")

    def _save_written_text(self):
        text = self.writing_text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Guardar Escrito", "No hay texto para guardar.")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                                title="Guardar Escrito")
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text)
                messagebox.showinfo("Guardar Escrito", f"Escrito guardado exitosamente en:\n{filename}")
                self._add_to_portfolio({"tipo": "redaccion", "titulo": os.path.basename(filename), "contenido": text, "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            except Exception as e:
                messagebox.showerror("Error al Guardar", f"No se pudo guardar el escrito: {e}")

    def _clear_writing_area(self):
        self.writing_text_area.delete("1.0", tk.END)
        self.suggestion_label.config(text="Área de escritura limpia.")

    def _give_writing_suggestions(self, event=None):
        text = self.writing_text_area.get("1.0", tk.END)
        word_count = len(text.split())
        
        # Ejemplo muy básico de sugerencia
        if word_count < 10 and len(text.strip()) > 0:
            self.suggestion_label.config(text=f"Palabras: {word_count}. Sigue escribiendo, ¡vas bien!", foreground="blue")
        elif word_count >= 10:
            self.suggestion_label.config(text=f"Palabras: {word_count}. ¡Excelente! ¿Revisaste la ortografía y gramática?", foreground="green")
        else:
            self.suggestion_label.config(text="Sugerencias aparecerán aquí.", foreground="blue")

        # Esto sería el lugar para integrar language_tool_python si lo quieres en tiempo real
        # Aunque puede ser lento, se haría en un hilo separado
        # if self.language_tool_initialized and word_count > 5:
        #     self._check_grammar_in_background(text)

    # --- Contenido de la Pestaña de Ejercicios ---
    def _create_exercises_tab_content(self, parent_frame):
        exercises_frame = ttk.Frame(parent_frame, padding="15")
        exercises_frame.pack(fill="both", expand=True)

        ttk.Label(exercises_frame, text="Ejercicios de Castellano", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Selector de ejercicio
        exercise_selector_frame = ttk.Frame(exercises_frame)
        exercise_selector_frame.pack(pady=5, fill="x")

        ttk.Label(exercise_selector_frame, text="Selecciona un ejercicio:").pack(side=tk.LEFT, padx=5)
        self.exercise_combobox = ttk.Combobox(exercise_selector_frame, state="readonly", width=40)
        self.exercise_combobox['values'] = [f"Ejercicio {e['id']}: {e['pregunta'][:50]}..." for e in self.exercises_data['ejercicios']]
        self.exercise_combobox.bind("<<ComboboxSelected>>", self._load_selected_exercise)
        self.exercise_combobox.pack(side=tk.LEFT, padx=5)

        # Área de visualización del ejercicio
        self.exercise_display_frame = ttk.Frame(exercises_frame, relief=tk.GROOVE, borderwidth=2, padding=10)
        self.exercise_display_frame.pack(pady=10, fill="both", expand=True)

        self.exercise_question_label = ttk.Label(self.exercise_display_frame, text="Selecciona un ejercicio para empezar.", font=("Arial", 12, "bold"))
        self.exercise_question_label.pack(pady=10)

        self.exercise_controls_frame = ttk.Frame(self.exercise_display_frame)
        self.exercise_controls_frame.pack(pady=5)

        self.feedback_label = ttk.Label(self.exercise_display_frame, text="", font=("Arial", 10, "italic"))
        self.feedback_label.pack(pady=10)

    def _load_selected_exercise(self, event=None):
        selected_text = self.exercise_combobox.get()
        if not selected_text:
            return
        
        # Extraer el ID del ejercicio del texto seleccionado (Ej: "Ejercicio 1: ...")
        exercise_id_match = re.match(r"Ejercicio (\d+):", selected_text)
        if not exercise_id_match:
            messagebox.showerror("Error", "Formato de ejercicio inválido.")
            return

        exercise_id = exercise_id_match.group(1)
        exercise_data = next((e for e in self.exercises_data['ejercicios'] if e['id'] == exercise_id), None)

        if exercise_data:
            self._display_exercise(exercise_data)
        else:
            messagebox.showwarning("No encontrado", "El ejercicio seleccionado no se encontró.")

    def _display_exercise(self, exercise_data):
        # Limpiar frame de ejercicio
        for widget in self.exercise_controls_frame.winfo_children():
            widget.destroy()
        self.feedback_label.config(text="") # Limpiar feedback anterior

        self.current_exercise_data = exercise_data
        
        # Mostrar la pregunta del ejercicio
        self.exercise_question_label.config(text=exercise_data['pregunta'])
        
        # Añadir un botón para leer la pregunta en voz alta
        ttk.Button(self.exercise_display_frame, text="🔊 Leer Pregunta", command=lambda: self._speak_text(exercise_data['pregunta'])).pack(pady=5)

        # Lógica para diferentes tipos de ejercicios
        if exercise_data['tipo'] == 'fill_in_the_blank':
            ttk.Label(self.exercise_controls_frame, text="Completa el texto:").pack(pady=(10,0))
            text_frame = ttk.Frame(self.exercise_controls_frame)
            text_frame.pack(pady=5)
            
            self.entry_vars = []
            parts = re.split(r'\[BLANCO\]', exercise_data['texto'])
            
            for i, part in enumerate(parts):
                if part:
                    ttk.Label(text_frame, text=part, font=("Arial", 11)).pack(side=tk.LEFT)
                if i < len(parts) - 1:
                    entry_var = tk.StringVar()
                    entry = ttk.Entry(text_frame, textvariable=entry_var, width=20, font=("Arial", 11))
                    entry.pack(side=tk.LEFT, padx=2)
                    self.entry_vars.append(entry_var)
            
            ttk.Button(self.exercise_controls_frame, text="Comprobar", command=self._check_fill_in_the_blank).pack(pady=10)

        elif exercise_data['tipo'] == 'multiple_choice':
            ttk.Label(self.exercise_controls_frame, text="Elige la opción correcta:").pack(pady=(10,0))
            self.selected_option = tk.StringVar()
            
            for option in exercise_data['opciones']:
                rb = ttk.Radiobutton(self.exercise_controls_frame, text=option, variable=self.selected_option, value=option)
                rb.pack(anchor="w", padx=20, pady=2)
            
            ttk.Button(self.exercise_controls_frame, text="Comprobar", command=self._check_multiple_choice).pack(pady=10)

    def _check_fill_in_the_blank(self):
        user_answers = [var.get().strip() for var in self.entry_vars]
        correct_answers = self.current_exercise_data['respuesta_correcta'] # Asume lista si hay varios blancos

        if isinstance(correct_answers, str): # Si solo hay un blanco
            correct = user_answers[0].lower() == correct_answers.lower()
        else: # Si hay múltiples blancos
            correct = all(ua.lower() == ca.lower() for ua, ca in zip(user_answers, correct_answers))

        feedback = self.current_exercise_data['feedback']
        solution = self.current_exercise_data['respuesta_correcta'] # Podría ser user_answers[0] o ', '.join(correct_answers)
        self._show_exercise_feedback(correct, feedback, solution)
        if correct:
            self._add_completed_exercise(self.current_exercise_data['id'])


    def _check_multiple_choice(self):
        user_answer = self.selected_option.get().strip()
        correct_answer = self.current_exercise_data['respuesta_correcta']
        
        correct = user_answer.lower() == correct_answer.lower()
        feedback = self.current_exercise_data['feedback']
        
        self._show_exercise_feedback(correct, feedback, correct_answer)
        if correct:
            self._add_completed_exercise(self.current_exercise_data['id'])

    def _show_exercise_feedback(self, correct, feedback_message, solution_text=None):
        if correct:
            self.feedback_label.config(text=f"¡Correcto! ✅ {feedback_message}", foreground="green")
        else:
            self.feedback_label.config(text=f"Incorrecto ❌: {feedback_message}", foreground="red")
            if solution_text:
                solution_frame = ttk.Frame(self.feedback_label.master)
                solution_frame.pack(pady=5)
                ttk.Label(solution_frame, text=f"La solución correcta era: {solution_text}", font=("Arial", 10, "italic")).pack(side=tk.LEFT)
                ttk.Button(solution_frame, text="🔊", command=lambda: self._speak_text(solution_text)).pack(side=tk.LEFT, padx=5)

    def _add_completed_exercise(self, exercise_id):
        if exercise_id not in self.user_progress["completed_exercises"]:
            self.user_progress["completed_exercises"].append(exercise_id)
            # self._save_user_progress() # Guardar el progreso

    # --- Contenido de la Pestaña de Pronunciación (Grabación Básica) ---
    def _create_pronunciation_tab_content(self, parent_frame):
        pron_frame = ttk.Frame(parent_frame, padding="15")
        pron_frame.pack(fill="both", expand=True)

        ttk.Label(pron_frame, text="Ejercicios de Pronunciación", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Oración de modelo
        self.pron_model_text = "El rápido tren cruza la montaña." # Ejemplo de oración
        ttk.Label(pron_frame, text="Oración a practicar:", font=("Arial", 12)).pack(pady=(10,0))
        self.pron_display_label = ttk.Label(pron_frame, text=self.pron_model_text, font=("Arial", 14, "bold"), wraplength=700)
        self.pron_display_label.pack(pady=5)
        ttk.Button(pron_frame, text="🔊 Leer Modelo", command=lambda: self._speak_text(self.pron_model_text)).pack(pady=5)

        # Controles de grabación
        recording_controls_frame = ttk.Frame(pron_frame)
        recording_controls_frame.pack(pady=20)

        self.pron_record_button = ttk.Button(recording_controls_frame, text="Grabar mi Voz 🎤", command=lambda: self._start_recording(self.pron_status_label))
        self.pron_record_button.pack(side=tk.LEFT, padx=10)

        self.pron_stop_button = ttk.Button(recording_controls_frame, text="Detener ⏹️", command=lambda: self._stop_pron_recording())
        self.pron_stop_button.pack(side=tk.LEFT, padx=10)

        self.pron_play_button = ttk.Button(recording_controls_frame, text="Reproducir mi Grabación ▶️", command=lambda: self._play_recording(self.pron_status_label))
        self.pron_play_button.pack(side=tk.LEFT, padx=10)

        self.pron_status_label = ttk.Label(pron_frame, text="Listo para grabar...", font=("Arial", 10, "italic"))
        self.pron_status_label.pack(pady=10)

        # Evaluación STT básica
        ttk.Button(pron_frame, text="Evaluar Transcripción (STT)", command=self._evaluate_pron_stt).pack(pady=15)
        self.pron_stt_result_label = ttk.Label(pron_frame, text="Resultado de tu transcripción: ", font=("Arial", 11))
        self.pron_stt_result_label.pack(pady=5)
        self.pron_stt_feedback_label = ttk.Label(pron_frame, text="", font=("Arial", 11, "bold"))
        self.pron_stt_feedback_label.pack(pady=5)

    def _stop_pron_recording(self):
        # Llama al método general de detener grabación y actualiza los estados de los botones de esta pestaña
        success = self._stop_recording(self.pron_status_label)
        self.pron_record_button.config(state=tk.NORMAL)
        self.pron_stop_button.config(state=tk.DISABLED)
        if success:
            self.pron_play_button.config(state=tk.NORMAL)

    def _evaluate_pron_stt(self):
        if not os.path.exists(self.user_audio_filename):
            messagebox.showwarning("Advertencia", "Primero graba tu voz.")
            return

        self.pron_stt_result_label.config(text="Transcribiendo y evaluando...")
        self.pron_stt_feedback_label.config(text="")

        # Ejecutar reconocimiento en un hilo para no bloquear la GUI
        threading.Thread(target=self._run_stt_evaluation_thread).start()

    def _run_stt_evaluation_thread(self):
        user_transcript = self._recognize_speech_from_mic(self.user_audio_filename, self.pron_status_label)
        
        if user_transcript:
            self.pron_stt_result_label.config(text=f"Tu voz: '{user_transcript}'")
            if user_transcript.lower().strip() == self.pron_model_text.lower().strip():
                self.pron_stt_feedback_label.config(text="¡Excelente! Tu pronunciación coincide perfectamente con el texto. ✅", foreground="green")
            else:
                self.pron_stt_feedback_label.config(text=f"Tu pronunciación no coincidió exactamente. Intenta de nuevo. ❌", foreground="red")
        else:
            self.pron_stt_result_label.config(text="No se pudo reconocer tu voz.")
            self.pron_stt_feedback_label.config(text="")
        
        self.pron_status_label.config(text="Evaluación STT finalizada.")

    # --- Contenido de la Pestaña de Fonética AFI ---
    def _create_phonetics_tab_content(self, parent_frame):
        phonetics_frame = ttk.Frame(parent_frame, padding="15")
        phonetics_frame.pack(fill="both", expand=True)

        ttk.Label(phonetics_frame, text="Fonética y Fonología del Castellano (AFI)", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Frame para los botones de fonemas con scrollbar
        canvas = tk.Canvas(phonetics_frame)
        scrollbar = ttk.Scrollbar(phonetics_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        categorized_phonemes = {}
        for phoneme_data in self.phonetics_data:
            p_type = phoneme_data.get('tipo', 'Otros')
            if p_type not in categorized_phonemes:
                categorized_phonemes[p_type] = []
            categorized_phonemes[p_type].append(phoneme_data)

        for p_type, phonemes in categorized_phonemes.items():
            ttk.Label(scrollable_frame, text=p_type.capitalize(), font=("Arial", 14, "underline")).pack(anchor="w", pady=(10, 5), padx=5)
            
            type_frame = ttk.Frame(scrollable_frame)
            type_frame.pack(fill="x", padx=5)

            col_count = 0
            row_count = 0
            for phoneme_data in phonemes:
                symbol = phoneme_data['simbolo_afi']
                description = phoneme_data['descripcion']
                examples = phoneme_data['ejemplos_palabras']

                btn_width = max(5, len(symbol) + 2) 
                btn = ttk.Button(type_frame, text=symbol, 
                                 command=lambda s=symbol, d=description, e=examples: self._display_phoneme_info(s, d, e),
                                 width=btn_width)
                btn.grid(row=row_count, column=col_count, padx=3, pady=3, sticky="w")
                
                col_count += 1
                if col_count > 9:
                    col_count = 0
                    row_count += 1
            
        # Área de información y ejemplos del fonema seleccionado
        info_display_frame = ttk.Frame(phonetics_frame, relief=tk.GROOVE, borderwidth=2, padding=10)
        info_display_frame.pack(pady=10, fill="x")

        self.phoneme_symbol_label = ttk.Label(info_display_frame, text="", font=("Arial", 36, "bold"), foreground="#0056b3")
        self.phoneme_symbol_label.pack(pady=5)
        
        self.phoneme_desc_label = ttk.Label(info_display_frame, text="", font=("Arial", 12), wraplength=700, justify=tk.LEFT)
        self.phoneme_desc_label.pack(pady=5, anchor="w")
        
        ttk.Label(info_display_frame, text="Ejemplos:", font=("Arial", 11, "italic")).pack(pady=(10,0), anchor="w")
        self.phoneme_examples_frame = ttk.Frame(info_display_frame)
        self.phoneme_examples_frame.pack(pady=5, fill="x")

    def _display_phoneme_info(self, symbol, description, examples):
        """Muestra la información de un fonema seleccionado y reproduce su sonido."""
        self.phoneme_symbol_label.config(text=f"/{symbol}/")
        self.phoneme_desc_label.config(text=description)

        for widget in self.phoneme_examples_frame.winfo_children():
            widget.destroy()

        for word in examples:
            word_frame = ttk.Frame(self.phoneme_examples_frame)
            word_frame.pack(anchor="w", padx=5, pady=2)
            ttk.Label(word_frame, text=word, font=("Arial", 11)).pack(side=tk.LEFT)
            ttk.Button(word_frame, text="🔊", command=lambda w=word: self._speak_text(w, lang='es')).pack(side=tk.LEFT, padx=5)

        self._speak_text(symbol, lang='es') # Intenta reproducir el símbolo AFI como texto


    # --- Métodos de Portafolio (Simplificado) ---
    def _add_to_portfolio(self, item):
        self.user_portfolio.append(item)
        # Aquí podrías guardar self.user_progress[] o solo el portfolio
        # self._save_user_progress() # Llamar para persistencia

# --- Ejecutar la Aplicación ---
if __name__ == "__main__":
    # --- Crear archivos JSON dummy si no existen ---
    # Esto es crucial para que el programa tenga datos al iniciar por primera vez.
    if not os.path.exists("lessons_data.json"):
        with open("lessons_data.json", "w", encoding="utf-8") as f:
            json.dump({
                "1": {"titulo": "Uso de 'B' y 'V'", "contenido": "La 'b' se usa antes de 'l' y 'r'. Ej: 'blanco', 'brazo'. La 'v' en palabras como 'vista', 'vaca'.\n\nErrores comunes: confundir 'haber' con 'a ver', 'tubo' con 'tuvo'.", "ejemplos": ["bello", "vello", "baca", "vaca", "tubo", "tuvo"]},
                "2": {"titulo": "Acentuación de Agudas, Graves y Esdrújulas", "contenido": "Las palabras agudas llevan tilde cuando terminan en n, s o vocal. Ej: 'café', 'canción'.\nLas palabras graves/llanas llevan tilde cuando NO terminan en n, s o vocal. Ej: 'árbol', 'difícil'.\nLas palabras esdrújulas y sobresdrújulas siempre llevan tilde. Ej: 'música', 'cómetelo'.", "ejemplos": ["camión", "mesa", "teléfono", "rápidamente"]}
            }, f, ensure_ascii=False, indent=4)

    if not os.path.exists("templates_data.json"):
        with open("templates_data.json", "w", encoding="utf-8") as f:
            json.dump({
                "Narrativo": {
                    "Cuento Corto": {
                        "descripcion": "Plantilla básica para un cuento corto.",
                        "estructura_esperada": {
                            "titulo": {"min_len": 5, "max_len": 20},
                            "introduccion": {"min_len": 50},
                            "nudo": {"min_len": 150},
                            "desenlace": {"min_len": 70}
                        }
                    },
                    "Microrelato": {
                        "descripcion": "Plantilla para un relato muy breve.",
                        "estructura_esperada": {
                            "titulo": {"min_len": 3, "max_len": 10},
                            "historia": {"min_len": 30, "max_len": 100}
                        }
                    }
                },
                "Expositivo": {
                    "Artículo Informativo": {
                        "descripcion": "Estructura para un artículo que informa sobre un tema.",
                        "estructura_esperada": {
                            "titulo": {"min_len": 5, "max_len": 30},
                            "introduccion": {"min_len": 60},
                            "desarrollo_tema_1": {"min_len": 100},
                            "desarrollo_tema_2": {"min_len": 100},
                            "conclusion": {"min_len": 50}
                        }
                    }
                }
            }, f, ensure_ascii=False, indent=4)

    if not os.path.exists("exercises_data.json"):
        with open("exercises_data.json", "w", encoding="utf-8") as f:
            json.dump({
                "ejercicios": [
                    {
                        "id": "1",
                        "tipo": "multiple_choice",
                        "pregunta": "¿Cuál es la forma correcta del pretérito perfecto simple de 'ir' para 'yo'?",
                        "opciones": ["yo hiba", "yo iba", "yo iva"],
                        "respuesta_correcta": "yo iba",
                        "feedback": "La forma correcta es 'iba', con 'b', y sin 'h' inicial."
                    },
                    {
                        "id": "2",
                        "tipo": "fill_in_the_blank",
                        "pregunta": "Completa la frase: 'El perro [BLANCO] feliz en el [BLANCO].'",
                        "texto": "El perro [BLANCO] feliz en el [BLANCO].",
                        "respuesta_correcta": ["corre", "parque"],
                        "feedback": "¡Excelente! 'corre' y 'parque' completan la frase lógicamente."
                    },
                     {
                        "id": "3",
                        "tipo": "multiple_choice",
                        "pregunta": "¿Qué palabra es esdrújula?",
                        "opciones": ["cancion", "arbol", "murcielago"],
                        "respuesta_correcta": "murcielago",
                        "feedback": "'Murciélago' lleva el acento en la antepenúltima sílaba y siempre se tilda."
                    }
                ]
            }, f, ensure_ascii=False, indent=4)

    if not os.path.exists("phonetics_data.json"):
        with open("phonetics_data.json", "w", encoding="utf-8") as f:
            json.dump([
                {"simbolo_afi": "a", "descripcion": "Vocal abierta central no redondeada (como en 'casa')", "ejemplos_palabras": ["casa", "mano"], "tipo": "vocal"},
                {"simbolo_afi": "e", "descripcion": "Vocal media anterior no redondeada (como en 'mesa')", "ejemplos_palabras": ["mesa", "verde"], "tipo": "vocal"},
                {"simbolo_afi": "i", "descripcion": "Vocal cerrada anterior no redondeada (como en 'libro')", "ejemplos_palabras": ["libro", "cine"], "tipo": "vocal"},
                {"simbolo_afi": "o", "descripcion": "Vocal media posterior redondeada (como en 'sol')", "ejemplos_palabras": ["sol", "mono"], "tipo": "vocal"},
                {"simbolo_afi": "u", "descripcion": "Vocal cerrada posterior redondeada (como en 'luna')", "ejemplos_palabras": ["luna", "azul"], "tipo": "vocal"},
                {"simbolo_afi": "p", "descripcion": "Consonante oclusiva bilabial sorda (como en 'padre')", "ejemplos_palabras": ["padre", "papel"], "tipo": "consonante"},
                {"simbolo_afi": "r", "descripcion": "Consonante vibrante simple alveolar (como en 'pero')", "ejemplos_palabras": ["pero", "caro"], "tipo": "consonante"},
                {"simbolo_afi": "ɾ", "descripcion": "Consonante vibrante múltiple alveolar (como en 'perro')", "ejemplos_palabras": ["perro", "rojo"], "tipo": "consonante"},
                {"simbolo_afi": "θ", "descripcion": "Consonante fricativa dental sorda (sonido de la 'z' o 'c' en España)", "ejemplos_palabras": ["zapato", "cinco"], "tipo": "consonante"}
            ], f, ensure_ascii=False, indent=4)

    if not os.path.exists("user_progress.json"):
        with open("user_progress.json", "w", encoding="utf-8") as f:
            json.dump({"portfolio": [], "completed_exercises": [], "challenge_records": []}, f, ensure_ascii=False, indent=4)

    root = tk.Tk()
    app = GrammarLessonApp(root)
    root.mainloop()
