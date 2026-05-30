import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import json
import os
import re
from datetime import datetime, date

# Importar matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Ocultar la barra de herramientas por defecto de matplotlib
plt.rcParams['toolbar'] = 'None'


# --- Archivos de Datos Globales ---
USERS_FILE = "users.json"
LESSONS_DATA_FILE = "lessons_data.json"
TEMPLATES_DATA_FILE = "templates_data.json"
EXERCISES_DATA_FILE = "exercises_exercises.json" # Renombrado para evitar conflictos si ya existe un exercises.json


# --- Datos de Ejemplo (si los archivos no existen) ---
DEFAULT_LESSONS = {
    "1": {"titulo": "Uso de 'B' y 'V'", "contenido": "La 'b' se usa antes de 'l' y 'r'. Ej: 'blanco', 'brazo'. La 'v' en palabras como 'vista', 'vaca'.", "ejemplos": ["bello", "vello"], "nivel": "Principiante 1", "temas": ["ortografia", "reglas_b_v"]},
    "2": {"titulo": "Acentuación Básica", "contenido": "Las agudas se tildan...", "ejemplos": ["cafe", "arbol"], "nivel": "Principiante 1", "temas": ["acentuacion", "ortografia"]},
    "3": {"titulo": "El Subjuntivo en Contextos de Viaje", "contenido": "El subjuntivo se usa para expresar deseos, dudas o emociones. En viajes, lo verás en frases como 'Espero que disfrutes tu viaje'.", "nivel": "Intermedio 1", "temas": ["verbos_subjuntivo", "viajes"]},
    "4": {"titulo": "Vocabulario Esencial para Viajar", "contenido": "Aprende palabras clave para moverte, pedir comida y más. Ej: 'billete', 'maleta', 'hotel', 'restaurante'.", "nivel": "Principiante 1", "temas": ["vocabulario", "viajes"]},
    "5": {"titulo": "Recetas en Español", "contenido": "Entiende las instrucciones de cocina en español. 'Ingredientes', 'preparación', 'horno', 'sartén'.", "nivel": "Intermedio 2", "temas": ["vocabulario", "cocina"]},
    "6": {"titulo": "Condicionales en el Ámbito Laboral", "contenido": "Usa condicionales para hablar de posibilidades y negociaciones. Ej: 'Si tuvieras tiempo, podríamos discutirlo'.", "nivel": "Avanzado 1", "temas": ["gramatica", "negocios"]},
    "7": {"titulo": "Expresiones Idiomáticas de Negocios", "contenido": "Frases comunes en el mundo de los negocios. Ej: 'ponerse las pilas', 'dar en el clavo'.", "nivel": "Avanzado 2", "temas": ["vocabulario", "negocios"]}
}
DEFAULT_TEMPLATES = {
    "Narrativo": {
        "Cuento Corto": {"descripcion": "Plantilla para un cuento corto con introducción, nudo y desenlace.", "estructura_esperada": {"titulo": {"min_len": 3}, "introduccion": {"min_len": 50}, "nudo": {"min_len": 100}, "desenlace": {"min_len": 50}}, "nivel": "Principiante 1"},
        "Diario de Viaje": {"descripcion": "Escribe sobre tus experiencias en un viaje. Incluye fechas, lugares y emociones.", "estructura_esperada": {"fecha": {}, "lugar": {}, "eventos": {"min_len": 80}, "emociones": {"min_len": 30}}, "nivel": "Principiante 2", "temas": ["viajes"]}
    },
    "Formal": {
        "Correo Electrónico de Negocios": {"descripcion": "Plantilla para redactar un correo formal de negocios.", "estructura_esperada": {"saludo": {}, "motivo": {"min_len": 40}, "cierre": {}}, "nivel": "Intermedio 1", "temas": ["negocios"]}
    }
}
DEFAULT_EXERCISES = {
    "ejercicios": [
        {"id": "1", "tipo": "multiple_choice", "pregunta": "¿'Haber' o 'a ver'?", "opciones": ["haber", "a ver"], "respuesta_correcta": "a ver", "feedback": "La forma correcta es 'a ver' cuando se refiere a mirar.", "nivel": "Principiante 1", "temas": ["ortografia"]},
        {"id": "2", "tipo": "fill_in_the_blank", "pregunta": "El [BLANCO] es azul.", "texto": "El [BLANCO] es azul.", "respuesta_correcta": ["cielo"], "feedback": "Bien! El cielo es azul.", "nivel": "Principiante 1", "temas": ["vocabulario"]},
        {"id": "3", "tipo": "multiple_choice", "pregunta": "¿Qué palabra es esdrújula?", "opciones": ["cancion", "arbol", "murcielago"], "respuesta_correcta": "murcielago", "feedback": "'Murciélago' lleva el acento en la antepenúltima sílaba y siempre se tilda.", "nivel": "Principiante 1", "temas": ["acentuacion", "ortografia"]},
        {"id": "4", "tipo": "fill_in_the_blank", "pregunta": "En el aeropuerto, necesito mi [BLANCO] y el [BLANCO].", "texto": "En el aeropuerto, necesito mi [BLANCO] y el [BLANCO].", "respuesta_correcta": ["pasaporte", "billete"], "feedback": "¡Esenciales para viajar!", "nivel": "Principiante 2", "temas": ["vocabulario", "viajes"]},
        {"id": "5", "tipo": "multiple_choice", "pregunta": "¿Qué expresión usarías para invitar a alguien a cenar?", "opciones": ["Vamos a comer algo.", "Te invito a cenar.", "Nos vemos en la cena."], "respuesta_correcta": "Te invito a cenar.", "feedback": "'Te invito a cenar' es la forma más directa de invitar.", "nivel": "Intermedio 1", "temas": ["vocabulario", "cocina"]},
        {"id": "6", "tipo": "fill_in_the_blank", "pregunta": "Si [BLANCO] el informe a tiempo, [BLANCO] la presentación.", "texto": "Si [BLANCO] el informe a tiempo, [BLANCO] la presentación.", "respuesta_correcta": ["hubiéramos terminado", "habríamos hecho"], "feedback": "Condicional compuesto, perfecto para escenarios hipotéticos en el trabajo.", "nivel": "Avanzado 1", "temas": ["gramatica", "negocios"]}
    ]
}


# --- Plantilla de progreso para un nuevo usuario ---
DEFAULT_USER_PROGRESS = {
    "nivel_actual": "Principiante 1",
    "lecciones_completadas": [],
    "ejercicios_completados": [],
    "rendimiento_por_tema": {}, # Se irá llenando con { "tema": {"intentos": X, "aciertos": Y, "porcentaje_aciertos": Z} }
    "portfolio": [],
    "puntos": 0,
    "nivel_experiencia": "Novato",
    "ultima_conexion": None, # Esto se actualizará al iniciar sesión
    "racha_actual": 0,
    "racha_maxima": 0,
    "insignias": []
}

class GrammarLessonApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw() # Ocultar la ventana principal al inicio

        self.all_users_data = {}
        self.current_username = None
        self.current_user_progress = {}

        self._load_all_users_data()
        self._load_static_content_data()

        self._show_login_screen()

    # --- Métodos de carga/guardado de JSON y usuarios ---
    def _load_json_data(self, filename, default_value):
        """Carga datos de un archivo JSON con manejo de errores. Crea el archivo si no existe."""
        try:
            if not os.path.exists(filename):
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(default_value, f, ensure_ascii=False, indent=4)
                return default_value
            
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            messagebox.showerror("Error JSON", f"Error al leer {filename}: {e}. El archivo puede estar corrupto. Se restablecerá a valores por defecto.")
            # Si el archivo está corrupto, lo sobrescribe con los valores por defecto
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(default_value, f, ensure_ascii=False, indent=4)
            return default_value
        except Exception as e:
            messagebox.showerror("Error de Carga", f"Error al cargar {filename}: {e}")
            return default_value

    def _load_all_users_data(self):
        """Carga todos los perfiles de usuario desde el archivo USERS_FILE."""
        self.all_users_data = self._load_json_data(USERS_FILE, {})

    def _save_all_users_data(self):
        """Guarda todos los perfiles de usuario en el archivo USERS_FILE."""
        try:
            with open(USERS_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.all_users_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error al Guardar Usuarios", f"No se pudo guardar el archivo de usuarios: {e}")

    def _load_static_content_data(self):
        """Carga los datos de lecciones, plantillas y ejercicios."""
        self.lessons_data = self._load_json_data(LESSONS_DATA_FILE, DEFAULT_LESSONS)
        self.categorized_templates_data = self._load_json_data(TEMPLATES_DATA_FILE, DEFAULT_TEMPLATES)
        self.exercises_data = self._load_json_data(EXERCISES_DATA_FILE, DEFAULT_EXERCISES)

    def _show_login_screen(self):
        """Muestra la ventana de inicio de sesión o creación de perfil."""
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Bienvenido a El Castellañol")
        self.login_window.geometry("400x300")
        self.login_window.grab_set() # Hace que esta ventana sea modal

        # Asegurar que si se cierra esta ventana, se cierre la aplicación
        self.login_window.protocol("WM_DELETE_WINDOW", self.root.quit)

        main_frame = ttk.Frame(self.login_window, padding="20")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(main_frame, text="Selecciona o crea tu perfil:", font=("Helvetica", 14, "bold")).pack(pady=15)

        # Selección de usuario existente
        if self.all_users_data:
            ttk.Label(main_frame, text="Usuario existente:").pack(pady=(10, 5))
            self.user_combobox = ttk.Combobox(main_frame, values=sorted(list(self.all_users_data.keys())), state="readonly", width=30)
            self.user_combobox.pack(pady=5)
            # No se necesita bind para seleccionar, el botón lo hará
            ttk.Button(main_frame, text="Iniciar Sesión", command=self._login_selected_user).pack(pady=5)
        else:
            ttk.Label(main_frame, text="No hay usuarios. Crea uno nuevo.").pack(pady=(10, 5))

        # Creación de nuevo usuario
        ttk.Separator(main_frame, orient="horizontal").pack(fill="x", pady=10)
        ttk.Label(main_frame, text="Crear nuevo usuario:").pack(pady=(10, 5))
        self.new_user_entry = ttk.Entry(main_frame, width=30)
        self.new_user_entry.pack(pady=5)
        ttk.Button(main_frame, text="Crear y Entrar", command=self._create_new_user).pack(pady=5)

    def _login_selected_user(self):
        """Intenta iniciar sesión con el usuario seleccionado."""
        username = self.user_combobox.get()
        if not username:
            messagebox.showwarning("Error de Usuario", "Por favor, selecciona un usuario de la lista.")
            return
        
        self.current_username = username
        self._load_user_data(self.current_username)
        self._check_study_streak() # Revisar racha al loguearse
        self._check_achievements() # Revisar logros al loguearse
        self.login_window.destroy()
        self.root.deiconify() # Mostrar la ventana principal
        self._create_main_notebook() # Recrear la interfaz para el usuario cargado

    def _create_new_user(self):
        """Crea un nuevo perfil de usuario y lo carga."""
        username = self.new_user_entry.get().strip()
        if not username:
            messagebox.showwarning("Error de Usuario", "Por favor, ingresa un nombre de usuario.")
            return
        if username in self.all_users_data:
            messagebox.showerror("Error de Usuario", "Ese nombre de usuario ya existe. Por favor, elige otro.")
            return

        new_user_data = DEFAULT_USER_PROGRESS.copy()
        # Asegurarse de que los diccionarios anidados sean copias profundas si tuvieran datos más complejos
        new_user_data["rendimiento_por_tema"] = {} # Reinicia este diccionario para el nuevo usuario
        new_user_data["portfolio"] = [] # Reinicia esta lista
        new_user_data["insignias"] = [] # Reinicia esta lista

        # Establecer primera conexión para la racha
        new_user_data["ultima_conexion"] = date.today().isoformat()
        new_user_data["racha_actual"] = 1
        new_user_data["racha_maxima"] = 1

        self.all_users_data[username] = new_user_data
        self._save_all_users_data() # Guarda el nuevo usuario en el archivo global
        self.current_username = username
        self._load_user_data(self.current_username) # Carga el progreso del nuevo usuario
        
        self.login_window.destroy()
        self.root.deiconify()
        self._create_main_notebook()

    def _load_user_data(self, username):
        """Carga los datos de progreso del usuario especificado y asegura la integridad de las claves."""
        self.current_user_progress = self.all_users_data.get(username, DEFAULT_USER_PROGRESS.copy())
        
        # Asegurarse de que todas las claves de DEFAULT_USER_PROGRESS existan para el usuario
        # Esto es útil si agregas nuevas claves por defecto en futuras versiones
        for key, default_val in DEFAULT_USER_PROGRESS.items():
            if key not in self.current_user_progress:
                # Hacer una copia profunda para diccionarios/listas para evitar referencias compartidas
                if isinstance(default_val, dict):
                    self.current_user_progress[key] = default_val.copy()
                elif isinstance(default_val, list):
                    self.current_user_progress[key] = default_val[:]
                else:
                    self.current_user_progress[key] = default_val


    def _save_current_user_progress(self):
        """Guarda el progreso del usuario actual en el archivo global de usuarios."""
        if self.current_username:
            self.all_users_data[self.current_username] = self.current_user_progress
            self._save_all_users_data()
            self._update_user_status_label() # Actualizar el label del usuario al guardar

    def _update_user_status_label(self):
        """Actualiza la etiqueta de estado del usuario en la parte superior de la interfaz principal."""
        if hasattr(self, 'user_status_label') and self.user_status_label.winfo_exists():
            self.user_status_label.config(text=f"Usuario: {self.current_username} | Nivel: {self.current_user_progress['nivel_actual']} | Puntos: {self.current_user_progress['puntos']} | Racha: {self.current_user_progress['racha_actual']} días")


    # --- Gamificación: Puntos y Niveles de Experiencia ---
    def _add_points(self, points):
        """Añade puntos al usuario actual y actualiza su nivel de experiencia."""
        if "puntos" not in self.current_user_progress: # Para compatibilidad con usuarios antiguos
            self.current_user_progress["puntos"] = 0
        self.current_user_progress["puntos"] += points
        self._update_experience_level()
        self._save_current_user_progress()

    def _update_experience_level(self):
        """Calcula y actualiza el nivel de experiencia del usuario según sus puntos."""
        puntos = self.current_user_progress.get("puntos", 0)
        if puntos >= 1000:
            self.current_user_progress["nivel_experiencia"] = "Maestro"
        elif puntos >= 500:
            self.current_user_progress["nivel_experiencia"] = "Erudito"
        elif puntos >= 200:
            self.current_user_progress["nivel_experiencia"] = "Aprendiz"
        else:
            self.current_user_progress["nivel_experiencia"] = "Novato"
        self._update_user_status_label() # Actualizar el label del usuario si cambia el nivel de experiencia


    # --- Gamificación: Rachas de Estudio ---
    def _check_study_streak(self):
        """Verifica y actualiza la racha de estudio del usuario."""
        hoy = date.today()
        ultima_conexion_str = self.current_user_progress.get("ultima_conexion")
        
        if ultima_conexion_str:
            ultima_conexion = date.fromisoformat(ultima_conexion_str)
            diferencia_dias = (hoy - ultima_conexion).days
            
            if diferencia_dias == 1:  # Si se conectó ayer, la racha continúa
                self.current_user_progress["racha_actual"] += 1
                if self.current_user_progress["racha_actual"] > self.current_user_progress.get("racha_maxima", 0):
                    self.current_user_progress["racha_maxima"] = self.current_user_progress["racha_actual"]
            elif diferencia_dias > 1:  # Si no se conectó ayer, la racha se reinicia
                self.current_user_progress["racha_actual"] = 1 # Racha reiniciada
            # Si diferencia_dias == 0, significa que se conectó hoy (o múltiples veces hoy), la racha no cambia
        else: # Primera conexión registrada para este usuario
            self.current_user_progress["racha_actual"] = 1
            self.current_user_progress["racha_maxima"] = 1

        self.current_user_progress["ultima_conexion"] = hoy.isoformat()
        self._save_current_user_progress()
        self._update_user_status_label()


    # --- Gamificación: Insignias/Logros ---
    def _check_achievements(self):
        """Verifica si el usuario ha desbloqueado alguna insignia."""
        if "insignias" not in self.current_user_progress:
            self.current_user_progress["insignias"] = []

        # Insignia "Maestro de la Tilde"
        if "maestro_tilde" not in self.current_user_progress["insignias"]:
            acentuacion_stats = self.current_user_progress["rendimiento_por_tema"].get("acentuacion", {"intentos": 0, "porcentaje_aciertos": 0})
            if acentuacion_stats["intentos"] >= 5 and acentuacion_stats["porcentaje_aciertos"] >= 90:
                self.current_user_progress["insignias"].append("maestro_tilde")
                messagebox.showinfo("¡Logro Desbloqueado!", "¡Has ganado la insignia 'Maestro de la Tilde' por tu excelencia en acentuación!")
        
        # Insignia "Viajero Lingüístico"
        if "viajero_linguistico" not in self.current_user_progress["insignias"]:
            lecciones_viajes_completadas = [lid for lid in self.current_user_progress["lecciones_completadas"]
                                            if "viajes" in self.lessons_data.get(lid, {}).get("temas", [])]
            if len(lecciones_viajes_completadas) >= 2: # Requiere 2 lecciones de viajes completadas
                self.current_user_progress["insignias"].append("viajero_linguistico")
                messagebox.showinfo("¡Logro Desbloqueado!", "¡Felicidades! Eres un 'Viajero Lingüístico' al explorar las lecciones de viaje.")

        # Insignia "Escritor Veloz" (Ejemplo: si la última redacción tuvo más de 200 palabras)
        # Esto es un ejemplo, necesitarías una lógica para registrar el tiempo/palabras de la redacción.
        # Por ahora, solo si ha guardado al menos una redacción
        if "escritor_veloz" not in self.current_user_progress["insignias"] and self.current_user_progress["portfolio"]:
             # Para un ejemplo más realista, necesitarías guardar la cuenta de palabras con la redacción.
             # Por simplicidad, asumiremos que tener un escrito ya es un logro inicial.
            self.current_user_progress["insignias"].append("escritor_veloz")
            messagebox.showinfo("¡Logro Desbloqueado!", "¡Has ganado la insignia 'Escritor Veloz' por tu primera redacción!")


        self._save_current_user_progress() # Guarda las insignias obtenidas


    # --- Creación de Pestañas Principales ---
    def _create_main_notebook(self):
        """Crea y organiza las pestañas principales de la aplicación."""
        if hasattr(self, 'notebook') and self.notebook.winfo_exists():
            self.notebook.destroy() # Destruir si ya existe para reconstruir después del login/cambio de nivel

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Crear y añadir pestañas
        lessons_tab = ttk.Frame(self.notebook)
        writing_tab = ttk.Frame(self.notebook)
        exercises_tab = ttk.Frame(self.notebook)
        stats_tab = ttk.Frame(self.notebook)
        portfolio_tab = ttk.Frame(self.notebook)
        achievements_tab = ttk.Frame(self.notebook)

        self.notebook.add(lessons_tab, text="Lecciones 📚")
        self.notebook.add(writing_tab, text="Redacción Libre ✍️")
        self.notebook.add(exercises_tab, text="Ejercicios ✅")
        self.notebook.add(stats_tab, text="Estadísticas 📊")
        self.notebook.add(portfolio_tab, text="Portafolio 📄")
        self.notebook.add(achievements_tab, text="Logros 🏅")

        # Cargar contenido en cada pestaña
        self._create_lessons_tab_content(lessons_tab)
        self._create_writing_tab_content(writing_tab)
        self._create_exercises_tab_content(exercises_tab)
        self._create_stats_tab_content(stats_tab)
        self._create_portfolio_tab_content(portfolio_tab)
        self._create_achievements_tab_content(achievements_tab)

        # Etiqueta de estado del usuario (arriba de las pestañas)
        # Se recrea cada vez que se llama a _create_main_notebook
        if hasattr(self, 'user_status_label') and self.user_status_label.winfo_exists():
            self.user_status_label.destroy() # Eliminar la anterior para recrearla
        self.user_status_label = ttk.Label(self.root, text="", font=("Arial", 10, "italic"))
        self.user_status_label.pack(pady=5, anchor="e")
        self._update_user_status_label()


    # --- Contenido de la Pestaña de Lecciones ---
    def _create_lessons_tab_content(self, parent_frame):
        """Crea los widgets y la lógica para la pestaña de lecciones."""
        lessons_frame = ttk.Frame(parent_frame, padding="15")
        lessons_frame.pack(fill="both", expand=True)

        control_frame = ttk.Frame(lessons_frame)
        control_frame.pack(fill="x", pady=5)

        ttk.Label(control_frame, text="Filtrar por Tema:").pack(side=tk.LEFT, padx=5)
        self.lesson_topic_filter = ttk.Combobox(control_frame, state="readonly", width=20)
        # Obtener todos los temas únicos de las lecciones
        all_topics = sorted(list(set(t for l in self.lessons_data.values() for t in l.get('temas', []))))
        self.lesson_topic_filter['values'] = ["Todos"] + all_topics
        self.lesson_topic_filter.set("Todos")
        self.lesson_topic_filter.bind("<<ComboboxSelected>>", self._populate_lessons_listbox)
        self.lesson_topic_filter.pack(side=tk.LEFT, padx=5)

        ttk.Label(lessons_frame, text="Lecciones de Gramática Castellana", font=("Helvetica", 16, "bold")).pack(pady=10)

        lessons_list_frame = ttk.Frame(lessons_frame)
        lessons_list_frame.pack(side=tk.LEFT, fill="y", padx=10, pady=10)

        self.lessons_listbox = tk.Listbox(lessons_list_frame, height=15, width=30, font=("Arial", 11))
        self.lessons_listbox.pack(side=tk.LEFT, fill="y")
        lessons_scrollbar = ttk.Scrollbar(lessons_list_frame, orient="vertical", command=self.lessons_listbox.yview)
        lessons_scrollbar.pack(side=tk.RIGHT, fill="y")
        self.lessons_listbox.config(yscrollcommand=lessons_scrollbar.set)
        self.lessons_listbox.bind("<<ListboxSelect>>", self._display_lesson_content)

        self.lesson_content_frame = ttk.Frame(lessons_frame, relief=tk.GROOVE, borderwidth=2)
        self.lesson_content_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)
        self.lesson_title_label = ttk.Label(self.lesson_content_frame, text="Selecciona una lección", font=("Arial", 14, "bold"))
        self.lesson_title_label.pack(pady=5)
        self.lesson_text_display = scrolledtext.ScrolledText(self.lesson_content_frame, wrap=tk.WORD, height=20, font=("Arial", 11))
        self.lesson_text_display.pack(fill="both", expand=True, padx=5, pady=5)
        self.lesson_text_display.config(state=tk.DISABLED)

        self._populate_lessons_listbox() # Llamar al inicio para poblar la lista


    def _populate_lessons_listbox(self, event=None):
        """Rellena la Listbox de lecciones según el filtro de tema y el nivel del usuario."""
        self.lessons_listbox.delete(0, tk.END)
        selected_topic = self.lesson_topic_filter.get()
        current_user_level = self.current_user_progress['nivel_actual']

        for lesson_id, lesson_data in self.lessons_data.items():
            if self._is_content_available_by_level(lesson_data, current_user_level):
                if selected_topic == "Todos" or selected_topic in lesson_data.get('temas', []):
                    self.lessons_listbox.insert(tk.END, lesson_data['titulo'])

    def _display_lesson_content(self, event):
        """Muestra el contenido de la lección seleccionada."""
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


    # --- Contenido de la Pestaña de Redacción Libre ---
    def _create_writing_tab_content(self, parent_frame):
        """Crea los widgets y la lógica para la pestaña de redacción libre."""
        writing_frame = ttk.Frame(parent_frame, padding="15")
        writing_frame.pack(fill="both", expand=True)

        ttk.Label(writing_frame, text="Redacción Libre y con Plantillas", font=("Helvetica", 16, "bold")).pack(pady=10)

        template_control_frame = ttk.Frame(writing_frame)
        template_control_frame.pack(pady=10, fill="x")

        ttk.Label(template_control_frame, text="Seleccionar Plantilla:").pack(side=tk.LEFT, padx=5)
        self.template_combobox = ttk.Combobox(template_control_frame, state="readonly", width=30)

        template_names = []
        for category, templates in self.categorized_templates_data.items():
            for template_name, t_data in templates.items():
                if self._is_content_available_by_level(t_data, self.current_user_progress['nivel_actual']):
                    template_names.append(f"{category}: {template_name}")
        self.template_combobox['values'] = template_names
        self.template_combobox.bind("<<ComboboxSelected>>", self._load_template)
        self.template_combobox.pack(side=tk.LEFT, padx=5)

        self.clear_template_button = ttk.Button(template_control_frame, text="Limpiar Plantilla", command=self._clear_template_text)
        self.clear_template_button.pack(side=tk.LEFT, padx=5)

        self.writing_text_area = scrolledtext.ScrolledText(writing_frame, wrap=tk.WORD, height=25, font=("Arial", 12))
        self.writing_text_area.pack(pady=10, fill="both", expand=True)

        action_buttons_frame = ttk.Frame(writing_frame)
        action_buttons_frame.pack(pady=5)

        ttk.Button(action_buttons_frame, text="Guardar Escrito", command=self._save_written_text).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_buttons_frame, text="Limpiar Todo", command=self._clear_writing_area).pack(side=tk.LEFT, padx=5)

        self.suggestion_label = ttk.Label(writing_frame, text="Sugerencias aparecerán aquí.", foreground="blue", font=("Arial", 10, "italic"))
        self.suggestion_label.pack(pady=5)
        self.writing_text_area.bind("<KeyRelease>", self._give_writing_suggestions)

    def _load_template(self, event=None):
        """Carga una plantilla de redacción en el área de texto."""
        selected_template_full_name = self.template_combobox.get()
        if not selected_template_full_name:
            return

        category, template_name = selected_template_full_name.split(": ", 1)
        template_data = self.categorized_templates_data.get(category, {}).get(template_name)

        if template_data:
            self.writing_text_area.delete("1.0", tk.END)
            template_text = template_data.get('descripcion', '') + "\n\n"
            structure = template_data.get('estructura_esperada', {})
            for key, value in structure.items():
                min_len = value.get('min_len', 'N/A')
                template_text += f"[{key.upper()}] (mín. {min_len} palabras)\n\n"
            
            self.writing_text_area.insert(tk.END, template_text)
            self.current_writing_expected_structure = structure
            self.suggestion_label.config(text=f"Plantilla '{template_name}' cargada. ¡Empieza a escribir!")
        else:
            self.suggestion_label.config(text="Error al cargar la plantilla.")

    def _clear_template_text(self):
        """Limpia la selección de plantilla."""
        self.template_combobox.set('')
        self.current_writing_expected_structure = None
        self.suggestion_label.config(text="Plantilla borrada. Puedes escribir libremente.")

    def _save_written_text(self):
        """Guarda el texto escrito por el usuario y lo añade al portafolio."""
        text = self.writing_text_area.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Guardar Escrito", "No hay texto para guardar.")
            return

        # Pedir un título al usuario para el escrito
        title_dialog = tk.Toplevel(self.root)
        title_dialog.title("Título del Escrito")
        title_dialog.transient(self.root)
        title_dialog.grab_set()
        
        ttk.Label(title_dialog, text="Título para tu escrito:").pack(pady=10)
        title_entry = ttk.Entry(title_dialog, width=40)
        title_entry.pack(pady=5)
        title_entry.focus_set()

        written_title = tk.StringVar() # Para guardar el título

        def on_save_title():
            nonlocal written_title
            title = title_entry.get().strip()
            if not title:
                messagebox.showwarning("Atención", "El título no puede estar vacío.", parent=title_dialog)
                return
            written_title.set(title)
            title_dialog.destroy()

        ttk.Button(title_dialog, text="Guardar Título", command=on_save_title).pack(pady=10)
        self.root.wait_window(title_dialog) # Esperar a que la ventana de título se cierre

        if not written_title.get(): # Si el usuario cerró la ventana o no puso título
            messagebox.showinfo("Guardar Escrito", "Guardado cancelado.")
            return

        # El archivo se guarda localmente, y una referencia se guarda en el portafolio del usuario
        # Opcional: podrías guardar el texto directamente en el JSON del portfolio
        # Por simplicidad, lo guardaremos directamente en el JSON del portfolio
        try:
            self._add_to_portfolio({
                "tipo": "redaccion",
                "titulo": written_title.get(),
                "contenido": text,
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            messagebox.showinfo("Guardar Escrito", f"Escrito '{written_title.get()}' guardado exitosamente en tu portafolio.")
            self._check_achievements() # Revisar logros después de guardar escrito
            self._populate_portfolio_listbox() # Actualizar la lista del portafolio
        except Exception as e:
            messagebox.showerror("Error al Guardar", f"No se pudo guardar el escrito: {e}")


    def _clear_writing_area(self):
        """Limpia el área de texto de redacción."""
        self.writing_text_area.delete("1.0", tk.END)
        self.suggestion_label.config(text="Área de escritura limpia.")

    def _give_writing_suggestions(self, event=None):
        """Ofrece sugerencias básicas mientras el usuario escribe."""
        text = self.writing_text_area.get("1.0", tk.END)
        word_count = len(text.split())

        if word_count < 10 and len(text.strip()) > 0:
            self.suggestion_label.config(text=f"Palabras: {word_count}. Sigue escribiendo, ¡vas bien!", foreground="blue")
        elif word_count >= 10:
            self.suggestion_label.config(text=f"Palabras: {word_count}. ¡Excelente! ¿Revisaste la ortografía y gramática?", foreground="green")
        else:
            self.suggestion_label.config(text="Sugerencias aparecerán aquí.", foreground="blue")


    # --- Contenido de la Pestaña de Ejercicios ---
    def _create_exercises_tab_content(self, parent_frame):
        """Crea los widgets y la lógica para la pestaña de ejercicios."""
        exercises_frame = ttk.Frame(parent_frame, padding="15")
        exercises_frame.pack(fill="both", expand=True)

        control_frame = ttk.Frame(exercises_frame)
        control_frame.pack(fill="x", pady=5)

        ttk.Label(control_frame, text="Filtrar por Tema:").pack(side=tk.LEFT, padx=5)
        self.exercise_topic_filter = ttk.Combobox(control_frame, state="readonly", width=20)
        all_topics = sorted(list(set(t for e in self.exercises_data['ejercicios'] for t in e.get('temas', []))))
        self.exercise_topic_filter['values'] = ["Todos"] + all_topics
        self.exercise_topic_filter.set("Todos")
        self.exercise_topic_filter.bind("<<ComboboxSelected>>", self._populate_exercises_combobox)
        self.exercise_topic_filter.pack(side=tk.LEFT, padx=5)


        ttk.Label(exercises_frame, text="Ejercicios de Castellano", font=("Helvetica", 16, "bold")).pack(pady=10)

        exercise_selector_frame = ttk.Frame(exercises_frame)
        exercise_selector_frame.pack(pady=5, fill="x")

        ttk.Label(exercise_selector_frame, text="Selecciona un ejercicio:").pack(side=tk.LEFT, padx=5)
        self.exercise_combobox = ttk.Combobox(exercise_selector_frame, state="readonly", width=40)
        self.exercise_combobox.bind("<<ComboboxSelected>>", self._load_selected_exercise)
        self.exercise_combobox.pack(side=tk.LEFT, padx=5)

        self.exercise_display_frame = ttk.Frame(exercises_frame, relief=tk.GROOVE, borderwidth=2, padding=10)
        self.exercise_display_frame.pack(pady=10, fill="both", expand=True)

        self.exercise_question_label = ttk.Label(self.exercise_display_frame, text="Selecciona un ejercicio para empezar.", font=("Arial", 12, "bold"))
        self.exercise_question_label.pack(pady=10)

        self.exercise_controls_frame = ttk.Frame(self.exercise_display_frame)
        self.exercise_controls_frame.pack(pady=5)

        self.feedback_label = ttk.Label(self.exercise_display_frame, text="", font=("Arial", 10, "italic"))
        self.feedback_label.pack(pady=10)

        self._populate_exercises_combobox() # Llamar al inicio para poblar la combobox

    def _populate_exercises_combobox(self, event=None):
        """Rellena la Combobox de ejercicios según el filtro de tema y el nivel del usuario."""
        selected_topic = self.exercise_topic_filter.get()
        current_user_level = self.current_user_progress['nivel_actual']
        
        exercise_options = []
        for e in self.exercises_data['ejercicios']:
            if self._is_content_available_by_level(e, current_user_level):
                if selected_topic == "Todos" or selected_topic in e.get('temas', []):
                    exercise_options.append(f"Ejercicio {e['id']}: {e['pregunta'][:50]}...")
        self.exercise_combobox['values'] = exercise_options
        self.exercise_combobox.set('') # Limpiar la selección actual
        self.exercise_question_label.config(text="Selecciona un ejercicio para empezar.")
        for widget in self.exercise_controls_frame.winfo_children():
            widget.destroy()
        self.feedback_label.config(text="")

    def _load_selected_exercise(self, event=None):
        """Carga el ejercicio seleccionado en la interfaz."""
        selected_text = self.exercise_combobox.get()
        if not selected_text:
            return

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
        """Muestra el ejercicio en la interfaz según su tipo."""
        for widget in self.exercise_controls_frame.winfo_children():
            widget.destroy()
        self.feedback_label.config(text="")

        self.current_exercise_data = exercise_data
        self.exercise_question_label.config(text=exercise_data['pregunta'])

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
        """Verifica la respuesta del ejercicio de completar espacios."""
        user_answers = [var.get().strip() for var in self.entry_vars]
        correct_answers = self.current_exercise_data['respuesta_correcta']

        correct = False
        if isinstance(correct_answers, str):
            correct = user_answers[0].lower() == correct_answers.lower()
        else: # Asume que es una lista de respuestas para múltiples blancos
            if len(user_answers) == len(correct_answers):
                correct = all(ua.lower() == ca.lower() for ua, ca in zip(user_answers, correct_answers))
            else:
                correct = False # Número de respuestas no coincide

        feedback = self.current_exercise_data['feedback']
        solution = self.current_exercise_data['respuesta_correcta']
        self._show_exercise_feedback(correct, feedback, solution)
        self._update_topic_performance(self.current_exercise_data.get('temas', []), correct)
        if correct:
            self._add_points(10)  # Gana puntos por ejercicio correcto
            self._add_completed_exercise(self.current_exercise_data['id'])
            self._check_level_up() # Revisar si el usuario puede subir de nivel
        self._check_achievements() # Revisar logros después de ejercicio


    def _check_multiple_choice(self):
        """Verifica la respuesta del ejercicio de opción múltiple."""
        user_answer = self.selected_option.get().strip()
        correct_answer = self.current_exercise_data['respuesta_correcta']

        correct = user_answer.lower() == correct_answer.lower()
        feedback = self.current_exercise_data['feedback']

        self._show_exercise_feedback(correct, feedback, correct_answer)
        self._update_topic_performance(self.current_exercise_data.get('temas', []), correct)
        if correct:
            self._add_points(10) # Gana puntos por ejercicio correcto
            self._add_completed_exercise(self.current_exercise_data['id'])
            self._check_level_up() # Revisar si el usuario puede subir de nivel
        self._check_achievements() # Revisar logros después de ejercicio

    def _show_exercise_feedback(self, correct, feedback_message, solution_text=None):
        """Muestra el feedback al usuario después de un ejercicio."""
        for widget in self.feedback_label.master.winfo_children(): # Eliminar feedback anterior si lo hay
            if isinstance(widget, ttk.Label) and widget != self.feedback_label:
                widget.destroy()

        if correct:
            self.feedback_label.config(text=f"¡Correcto! ✅ {feedback_message}", foreground="green")
        else:
            self.feedback_label.config(text=f"Incorrecto ❌: {feedback_message}", foreground="red")
            if solution_text:
                solution_display = solution_text if isinstance(solution_text, str) else ", ".join(solution_text)
                ttk.Label(self.feedback_label.master, text=f"La solución correcta era: {solution_display}", font=("Arial", 10, "italic")).pack(pady=2)

    def _add_completed_exercise(self, exercise_id):
        """Añade un ejercicio a la lista de completados del usuario si no está ya."""
        if exercise_id not in self.current_user_progress["ejercicios_completados"]:
            self.current_user_progress["ejercicios_completados"].append(exercise_id)
            self._save_current_user_progress() # Guardar progreso al completar ejercicio

    def _update_topic_performance(self, themes, correct):
        """Actualiza las estadísticas de rendimiento por tema para el usuario actual."""
        if not themes:
            return

        for theme in themes:
            if theme not in self.current_user_progress["rendimiento_por_tema"]:
                self.current_user_progress["rendimiento_por_tema"][theme] = {"intentos": 0, "aciertos": 0, "porcentaje_aciertos": 0.0}

            self.current_user_progress["rendimiento_por_tema"][theme]["intentos"] += 1
            if correct:
                self.current_user_progress["rendimiento_por_tema"][theme]["aciertos"] += 1

            total_attempts = self.current_user_progress["rendimiento_por_tema"][theme]["intentos"]
            total_correct = self.current_user_progress["rendimiento_por_tema"][theme]["aciertos"]
            
            if total_attempts > 0:
                self.current_user_progress["rendimiento_por_tema"][theme]["porcentaje_aciertos"] = (total_correct / total_attempts) * 100
            else:
                self.current_user_progress["rendimiento_por_tema"][theme]["porcentaje_aciertos"] = 0.0
        
        self._save_current_user_progress() # Guardar después de actualizar rendimiento


    def _check_level_up(self):
        """Verifica si el usuario ha cumplido los requisitos para subir de nivel."""
        current_level = self.current_user_progress.get("nivel_actual", "Principiante 1")
        niveles_orden = ["Principiante 1", "Principiante 2", "Intermedio 1", "Intermedio 2", "Avanzado 1", "Avanzado 2"]
        
        try:
            current_level_index = niveles_orden.index(current_level)
        except ValueError: # Nivel no encontrado en la lista, quizás un nivel futuro
            return

        if current_level_index + 1 >= len(niveles_orden):
            return # Ya está en el nivel más alto

        next_level = niveles_orden[current_level_index + 1]

        # Criterio de avance: Por ejemplo, debe haber completado al menos el 70% de los ejercicios disponibles en su nivel actual
        exercises_in_current_level = [e for e in self.exercises_data['ejercicios'] 
                                      if self._is_content_available_by_level(e, current_level) and e.get('nivel') == current_level]
        
        completed_exercises_in_current_level_ids = [
            e_id for e_id in self.current_user_progress["ejercicios_completados"]
            if next((e for e in exercises_in_current_level if e['id'] == e_id), None) is not None
        ]

        if not exercises_in_current_level: # No hay ejercicios definidos para este nivel
            return

        completion_percentage = (len(completed_exercises_in_current_level_ids) / len(exercises_in_current_level)) * 100

        if completion_percentage >= 70: # Umbral de 70% para avanzar
            self.current_user_progress["nivel_actual"] = next_level
            self._save_current_user_progress()
            messagebox.showinfo("¡Felicidades!", f"¡Has completado la mayoría de los ejercicios del nivel {current_level} y has desbloqueado el nivel {next_level}!")
            # Refrescar la interfaz para mostrar el nuevo contenido desbloqueado
            self._create_main_notebook() # Esto reconstruirá las pestañas con el nuevo nivel
            self._update_user_status_label() # Actualizar label

    # --- Helper para determinar si el contenido debe ser visible/seleccionable por el nivel del usuario ---
    def _is_content_available_by_level(self, content_data, user_level):
        """Comprueba si un elemento de contenido es accesible dado el nivel del usuario."""
        niveles_orden = ["Principiante 1", "Principiante 2", "Intermedio 1", "Intermedio 2", "Avanzado 1", "Avanzado 2"]
        content_level = content_data.get("nivel")

        if content_level in niveles_orden and user_level in niveles_orden:
            return niveles_orden.index(content_level) <= niveles_orden.index(user_level)
        return False


    # --- CONTENIDO DE LA PESTAÑA DE ESTADÍSTICAS ---
    def _create_stats_tab_content(self, parent_frame):
        """Crea los widgets y la lógica para la pestaña de estadísticas."""
        stats_frame = ttk.Frame(parent_frame, padding="15")
        stats_frame.pack(fill="both", expand=True)

        ttk.Label(stats_frame, text="Progreso y Estadísticas", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Frame para los gráficos
        self.stats_plot_frame = ttk.Frame(stats_frame)
        self.stats_plot_frame.pack(fill="both", expand=True, pady=10)

        # Botón para actualizar estadísticas
        ttk.Button(stats_frame, text="Actualizar Estadísticas", command=self._plot_user_stats).pack(pady=5)

        # Llamar a la función para graficar al inicio
        self._plot_user_stats()

    def _plot_user_stats(self):
        """Genera y muestra gráficos de las estadísticas del usuario."""
        # Limpiar el frame de gráficos si ya hay algo
        for widget in self.stats_plot_frame.winfo_children():
            widget.destroy()

        rendimiento_por_tema = self.current_user_progress.get("rendimiento_por_tema", {})
        
        if not rendimiento_por_tema:
            ttk.Label(self.stats_plot_frame, text="Aún no hay datos de rendimiento para mostrar.\nCompleta algunos ejercicios para ver tus estadísticas.", font=("Arial", 12)).pack(pady=20)
            return

        temas = []
        porcentajes = []
        for tema, stats in rendimiento_por_tema.items():
            if stats["intentos"] > 0: # Solo mostrar temas con al menos un intento
                temas.append(tema)
                porcentajes.append(stats["porcentaje_aciertos"])

        if not temas: # Si no hay temas con intentos
            ttk.Label(self.stats_plot_frame, text="Aún no hay datos de rendimiento para mostrar.\nCompleta algunos ejercicios para ver tus estadísticas.", font=("Arial", 12)).pack(pady=20)
            return

        # Crear figura de matplotlib
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Gráfico de barras de aciertos por tema
        ax.bar(temas, porcentajes, color='skyblue')
        ax.set_ylabel('Porcentaje de Aciertos (%)')
        ax.set_title('Rendimiento por Tema')
        ax.set_ylim(0, 100)
        plt.xticks(rotation=45, ha='right') # Rotar etiquetas para mejor legibilidad
        plt.tight_layout() # Ajustar el diseño para que las etiquetas no se corten

        # Integrar la figura de matplotlib en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.stats_plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas.draw()
        
        # Opcional: barra de herramientas de navegación para el gráfico (se puede desactivar con plt.rcParams['toolbar'] = 'None')
        # toolbar = NavigationToolbar2Tk(canvas, self.stats_plot_frame)
        # toolbar.update()
        # canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    # --- CONTENIDO DE LA PESTAÑA DE PORTAFOLIO ---
    def _create_portfolio_tab_content(self, parent_frame):
        """Crea los widgets y la lógica para la pestaña de portafolio."""
        portfolio_frame = ttk.Frame(parent_frame, padding="15")
        portfolio_frame.pack(fill="both", expand=True)

        ttk.Label(portfolio_frame, text="Tu Portafolio de Redacciones", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Lista de redacciones guardadas
        portfolio_list_frame = ttk.Frame(portfolio_frame)
        portfolio_list_frame.pack(side=tk.LEFT, fill="y", padx=10, pady=10)

        self.portfolio_listbox = tk.Listbox(portfolio_list_frame, height=15, width=40, font=("Arial", 11))
        self.portfolio_listbox.pack(side=tk.LEFT, fill="y")

        portfolio_scrollbar = ttk.Scrollbar(portfolio_list_frame, orient="vertical", command=self.portfolio_listbox.yview)
        portfolio_scrollbar.pack(side=tk.RIGHT, fill="y")
        self.portfolio_listbox.config(yscrollcommand=portfolio_scrollbar.set)
        self.portfolio_listbox.bind("<<ListboxSelect>>", self._display_portfolio_item)

        # Contenido de la redacción seleccionada
        self.portfolio_content_frame = ttk.Frame(portfolio_frame, relief=tk.GROOVE, borderwidth=2)
        self.portfolio_content_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)

        self.portfolio_title_label = ttk.Label(self.portfolio_content_frame, text="Selecciona un escrito", font=("Arial", 14, "bold"))
        self.portfolio_title_label.pack(pady=5)

        self.portfolio_text_display = scrolledtext.ScrolledText(self.portfolio_content_frame, wrap=tk.WORD, height=20, font=("Arial", 11))
        self.portfolio_text_display.pack(fill="both", expand=True, padx=5, pady=5)
        self.portfolio_text_display.config(state=tk.DISABLED)

        self._populate_portfolio_listbox() # Llenar la lista al inicio

    def _add_to_portfolio(self, item):
        """Añade un nuevo elemento (ej. redacción) al portafolio del usuario."""
        self.current_user_progress["portfolio"].append(item)
        self._save_current_user_progress() # Guardar progreso al añadir al portafolio

    def _populate_portfolio_listbox(self):
        """Rellena la Listbox del portafolio con los escritos del usuario."""
        self.portfolio_listbox.delete(0, tk.END)
        for item in self.current_user_progress.get("portfolio", []):
            self.portfolio_listbox.insert(tk.END, f"{item.get('titulo', 'Sin título')} ({item.get('fecha', 'Fecha desconocida')})")

    def _display_portfolio_item(self, event):
        """Muestra el contenido de un escrito seleccionado del portafolio."""
        selected_index = self.portfolio_listbox.curselection()
        if not selected_index:
            return

        selected_item_data = self.current_user_progress["portfolio"][selected_index[0]]
        
        self.portfolio_title_label.config(text=selected_item_data.get('titulo', 'Sin título'))
        self.portfolio_text_display.config(state=tk.NORMAL)
        self.portfolio_text_display.delete("1.0", tk.END)
        self.portfolio_text_display.insert(tk.END, selected_item_data.get('contenido', 'Contenido no disponible.'))
        self.portfolio_text_display.config(state=tk.DISABLED)

    # --- Contenido de la Pestaña de Logros ---
    def _create_achievements_tab_content(self, parent_frame):
        """Crea los widgets y la lógica para la pestaña de logros."""
        achievements_frame = ttk.Frame(parent_frame, padding="15")
        achievements_frame.pack(fill="both", expand=True)

        ttk.Label(achievements_frame, text="Tus Logros Desbloqueados", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.achievements_text_display = scrolledtext.ScrolledText(achievements_frame, wrap=tk.WORD, height=20, font=("Arial", 12))
        self.achievements_text_display.pack(fill="both", expand=True, padx=5, pady=5)
        self.achievements_text_display.config(state=tk.DISABLED)

        self._display_achievements()

    def _display_achievements(self):
        """Muestra las insignias y la racha máxima del usuario."""
        self.achievements_text_display.config(state=tk.NORMAL)
        self.achievements_text_display.delete("1.0", tk.END)

        achievements_map = {
            "maestro_tilde": "Maestro de la Tilde: Demostraste un dominio excepcional en acentuación.",
            "viajero_linguistico": "Viajero Lingüístico: Completaste tus primeras lecciones de español para viajes.",
            "escritor_veloz": "Escritor Veloz: Guardaste tu primera redacción en el portafolio.", # Descripción actualizada
            # Puedes añadir más descripciones aquí para cada insignia
            "racha_7_dias": "Racha de 7 Días: ¡Siete días seguidos aprendiendo!"
        }

        if not self.current_user_progress.get("insignias"):
            self.achievements_text_display.insert(tk.END, "Aún no has desbloqueado ninguna insignia. ¡Sigue practicando para ganar la primera!")
        else:
            self.achievements_text_display.insert(tk.END, "¡Felicitaciones por tus logros!\n\n")
            for insignia_id in self.current_user_progress["insignias"]:
                description = achievements_map.get(insignia_id, f"Insignia desconocida: {insignia_id}")
                self.achievements_text_display.insert(tk.END, f"🏅 {description}\n\n")
        
        # También puedes mostrar la racha más larga aquí
        racha_maxima = self.current_user_progress.get("racha_maxima", 0)
        self.achievements_text_display.insert(tk.END, f"\nTu racha de estudio más larga es de: {racha_maxima} días.")


        self.achievements_text_display.config(state=tk.DISABLED)


# --- Ejecutar la Aplicación ---
if __name__ == "__main__":
    # Asegurarse de que los archivos JSON estáticos existan con contenido por defecto
    # La función _load_json_data ahora crea el archivo si no existe,
    # así que estas comprobaciones directas son redundantes pero no hacen daño.
    # Se recomienda que los archivos por defecto tengan contenido inicial para no empezar vacíos.
    if not os.path.exists(LESSONS_DATA_FILE):
        with open(LESSONS_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_LESSONS, f, ensure_ascii=False, indent=4)
    if not os.path.exists(TEMPLATES_DATA_FILE):
        with open(TEMPLATES_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_TEMPLATES, f, ensure_ascii=False, indent=4)
    if not os.path.exists(EXERCISES_DATA_FILE):
        with open(EXERCISES_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_EXERCISES, f, ensure_ascii=False, indent=4)
    
    root = tk.Tk()
    app = GrammarLessonApp(root)
    root.mainloop()
