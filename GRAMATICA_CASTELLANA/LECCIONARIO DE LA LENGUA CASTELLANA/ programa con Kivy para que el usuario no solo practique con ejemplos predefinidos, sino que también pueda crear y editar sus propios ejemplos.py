from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty, ListProperty
import random
import json
import os

# --- Ruta para el archivo de datos persistentes ---
DATA_FILE = 'ejercicios_data.json'

# --- Datos de ejemplo para ejercicios (ahora cargados o guardados) ---
# Intentamos cargar los datos existentes, si no, usamos los predefinidos.
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
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

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Cargar los datos al inicio del programa
EJERCICIOS_DATA = load_data()

# --- Clase principal de gestión de ejercicios (similar a ExerciseManager en Kotlin/C++) ---
class ExerciseManager:
    def __init__(self):
        self.current_exercises = []
        self.current_exercise_index = 0
        self.score = 0
        self.selected_area = None
        self.selected_level = None
        self.selected_type = None

    def get_areas(self):
        return list(EJERCICIOS_DATA.keys())

    def get_levels_for_area(self, area):
        return list(EJERCICIOS_DATA.get(area, {}).keys())

    def get_types_for_level(self, area, level):
        return list(EJERCICIOS_DATA.get(area, {}).get(level, {}).keys())

    def start_practice_session(self, area, level, exercise_type):
        self.selected_area = area
        self.selected_level = level
        self.selected_type = exercise_type
        exercises = EJERCICIOS_DATA.get(area, {}).get(level, {}).get(exercise_type, [])
        self.current_exercises = list(exercises) # Copia para barajar
        random.shuffle(self.current_exercises)
        self.current_exercise_index = 0
        self.score = 0
        return len(self.current_exercises)

    def get_next_exercise(self):
        if self.current_exercise_index < len(self.current_exercises):
            ejercicio = self.current_exercises[self.current_exercise_index]
            return ejercicio
        return None

    def submit_answer(self, user_answer):
        ejercicio = self.current_exercises[self.current_exercise_index]
        is_correct = False
        feedback = ""

        # Normalización de texto para comparación
        def normalize(text):
            if isinstance(text, str):
                return text.strip().lower()
            return text

        correct_answer = ejercicio['respuesta']
        
        if ejercicio['tipo'] == 'seleccion_multiple':
            is_correct = (normalize(user_answer) == normalize(correct_answer))
        elif ejercicio['tipo'] == 'completar_oraciones':
            user_answer_normalized = [normalize(u) for u in user_answer]
            correct_answer_normalized = [normalize(c) for c in correct_answer]
            is_correct = (user_answer_normalized == correct_answer_normalized)
        elif ejercicio['tipo'] == 'detectar_errores':
            user_error = normalize(user_answer.get('palabra_erronea', ''))
            user_correction = normalize(user_answer.get('correccion', ''))
            correct_error = normalize(correct_answer['palabra_erronea'])
            correct_correction = normalize(correct_answer['correccion'])
            is_correct = (user_error == correct_error and user_correction == correct_correction)
        elif ejercicio['tipo'] in ['reorganizar_oraciones', 'clasificacion_de_palabras', 'conjugacion_verbal']:
            is_correct = (normalize(user_answer) == normalize(correct_answer))
        else:
            feedback = "Tipo de ejercicio no reconocido para validación."

        if is_correct:
            self.score += 1
            feedback = "¡Correcto! ✅ "
        else:
            feedback = "Incorrecto. ❌ "
        feedback += f"Explicación: {ejercicio['explicacion']}"

        self.current_exercise_index += 1
        return is_correct, feedback

    def is_session_finished(self):
        return self.current_exercise_index >= len(self.current_exercises)

    def get_session_results(self):
        return f"Obtuviste {self.score} de {len(self.current_exercises)} preguntas correctas."

    # --- Métodos para el editor ---
    def add_area(self, area_name):
        if area_name not in EJERCICIOS_DATA:
            EJERCICIOS_DATA[area_name] = {}
            save_data(EJERCICIOS_DATA)
            return True
        return False

    def add_level(self, area_name, level_name):
        if area_name in EJERCICIOS_DATA and level_name not in EJERCICIOS_DATA[area_name]:
            EJERCICIOS_DATA[area_name][level_name] = {}
            save_data(EJERCICIOS_DATA)
            return True
        return False

    def add_type(self, area_name, level_name, type_name):
        if area_name in EJERCICIOS_DATA and level_name in EJERCICIOS_DATA[area_name] and type_name not in EJERCICIOS_DATA[area_name][level_name]:
            EJERCICIOS_DATA[area_name][level_name][type_name] = []
            save_data(EJERCICIOS_DATA)
            return True
        return False

    def get_exercises_in_category(self, area, level, exercise_type):
        return EJERCICIOS_DATA.get(area, {}).get(level, {}).get(exercise_type, [])

    def add_exercise(self, area, level, exercise_type, new_exercise_data):
        if area in EJERCICIOS_DATA and level in EJERCICIOS_DATA[area] and exercise_type in EJERCICIOS_DATA[area][level]:
            EJERCICIOS_DATA[area][level][exercise_type].append(new_exercise_data)
            save_data(EJERCICIOS_DATA)
            return True
        return False

    def update_exercise(self, area, level, exercise_type, index, updated_data):
        if area in EJERCICIOS_DATA and level in EJERCICIOS_DATA[area] and exercise_type in EJERCICIOS_DATA[area][level]:
            if 0 <= index < len(EJERCICIOS_DATA[area][level][exercise_type]):
                EJERCICIOS_DATA[area][level][exercise_type][index] = updated_data
                save_data(EJERCICIOS_DATA)
                return True
        return False

    def delete_exercise(self, area, level, exercise_type, index):
        if area in EJERCICIOS_DATA and level in EJERCICIOS_DATA[area] and exercise_type in EJERCICIOS_DATA[area][level]:
            if 0 <= index < len(EJERCICIOS_DATA[area][level][exercise_type]):
                del EJERCICIOS_DATA[area][level][exercise_type][index]
                save_data(EJERCICIOS_DATA)
                return True
        return False


# --- Definición de Pantallas Kivy ---

class MainMenuScreen(Screen):
    pass

class PracticeSelectionScreen(Screen):
    manager_obj = ObjectProperty(None) # Referencia al ExerciseManager

    def on_enter(self, *args):
        self.ids.area_spinner.values = self.manager_obj.get_areas()
        self.ids.area_spinner.text = 'Selecciona Área'
        self.ids.level_spinner.values = []
        self.ids.level_spinner.text = 'Selecciona Nivel'
        self.ids.type_spinner.values = []
        self.ids.type_spinner.text = 'Selecciona Tipo'

    def update_levels(self, area):
        self.ids.level_spinner.values = self.manager_obj.get_levels_for_area(area)
        self.ids.level_spinner.text = 'Selecciona Nivel'
        self.ids.type_spinner.values = []
        self.ids.type_spinner.text = 'Selecciona Tipo'

    def update_types(self, area, level):
        self.ids.type_spinner.values = self.manager_obj.get_types_for_level(area, level)
        self.ids.type_spinner.text = 'Selecciona Tipo'

    def start_practice(self):
        area = self.ids.area_spinner.text
        level = self.ids.level_spinner.text
        exercise_type = self.ids.type_spinner.text

        if area == 'Selecciona Área' or level == 'Selecciona Nivel' or exercise_type == 'Selecciona Tipo':
            self.show_popup("Error", "Por favor, selecciona Área, Nivel y Tipo.")
            return

        total_exercises = self.manager_obj.start_practice_session(area, level, exercise_type)
        if total_exercises == 0:
            self.show_popup("Advertencia", "No hay ejercicios en esta categoría.")
        else:
            self.manager.get_screen('practice').update_exercise_ui()
            self.manager.current = 'practice'

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.7, 0.3))
        popup.open()


class PracticeScreen(Screen):
    manager_obj = ObjectProperty(None)
    question_label = ObjectProperty(None)
    options_layout = ObjectProperty(None)
    feedback_label = ObjectProperty(None)
    submit_button = ObjectProperty(None)
    continue_button = ObjectProperty(None)
    answer_input = ObjectProperty(None)
    total_questions_label = ObjectProperty(None)
    current_exercise = None

    def on_enter(self, *args):
        self.update_exercise_ui()

    def update_exercise_ui(self):
        self.current_exercise = self.manager_obj.get_next_exercise()
        self.options_layout.clear_widgets()
        self.answer_input.text = ''
        self.feedback_label.text = ''
        self.submit_button.disabled = False
        self.continue_button.disabled = True
        self.total_questions_label.text = f"Pregunta {self.manager_obj.current_exercise_index + 1} de {len(self.manager_obj.current_exercises)}"


        if self.current_exercise:
            self.question_label.text = self.current_exercise['pregunta']
            self.answer_input.opacity = 1
            self.answer_input.size_hint_y = None
            self.answer_input.height = "40dp"
            self.answer_input.hint_text = "Escribe tu respuesta aquí..."

            if self.current_exercise['tipo'] == 'seleccion_multiple':
                self.answer_input.opacity = 0 # Ocultar TextInput
                self.answer_input.size_hint_y = 0
                self.answer_input.height = 0
                for i, option in enumerate(self.current_exercise['opciones']):
                    btn = Button(text=option, size_hint_y=None, height="40dp",
                                 on_release=lambda x, opt=option: self.submit_answer_button(opt))
                    self.options_layout.add_widget(btn)
                self.submit_button.disabled = True # Botones de opciones manejan el submit
            elif self.current_exercise['tipo'] == 'completar_oraciones':
                # No se oculta el input, pero la validación requiere múltiples entradas.
                # Para Kivy, simplificaremos a una sola entrada de texto delimitada por comas
                self.answer_input.hint_text = "Escribe tus palabras separadas por comas (ej: palabra1, palabra2)"
            elif self.current_exercise['tipo'] == 'detectar_errores':
                self.answer_input.hint_text = "Palabra errónea,Corrección (ej: cancion,canción)"
            else: # Otros tipos de texto simple
                self.answer_input.hint_text = "Escribe tu respuesta aquí..."
        else:
            self.question_label.text = self.manager_obj.get_session_results()
            self.submit_button.disabled = True
            self.answer_input.opacity = 0
            self.answer_input.size_hint_y = 0
            self.answer_input.height = 0
            self.continue_button.text = "Volver al Menú Principal"
            self.continue_button.disabled = False


    def submit_answer_button(self, answer_text=None):
        if self.current_exercise['tipo'] == 'seleccion_multiple':
            user_answer = answer_text
        elif self.current_exercise['tipo'] == 'completar_oraciones':
            user_answer = [s.strip() for s in self.answer_input.text.split(',')]
        elif self.current_exercise['tipo'] == 'detectar_errores':
            parts = [s.strip() for s in self.answer_input.text.split(',')]
            if len(parts) == 2:
                user_answer = {"palabra_erronea": parts[0], "correccion": parts[1]}
            else:
                self.feedback_label.text = "Formato incorrecto para 'detectar_errores'. Usa 'palabra,correccion'."
                return
        else: # Otros tipos de texto simple
            user_answer = self.answer_input.text

        is_correct, feedback = self.manager_obj.submit_answer(user_answer)
        self.feedback_label.text = feedback
        self.submit_button.disabled = True
        self.continue_button.disabled = False
        
        # Deshabilitar botones de opción para selección múltiple
        for child in self.options_layout.children:
            if isinstance(child, Button):
                child.disabled = True


    def continue_session(self):
        if self.manager_obj.is_session_finished():
            self.manager.current = 'main_menu' # O 'practice_selection'
        else:
            self.update_exercise_ui()


# --- Pantallas del Editor ---

class EditorMenuScreen(Screen):
    pass

class CategorySelectionScreen(Screen):
    manager_obj = ObjectProperty(None)
    area_spinner = ObjectProperty(None)
    level_spinner = ObjectProperty(None)
    type_spinner = ObjectProperty(None)
    next_screen = StringProperty('') # Propiedad para saber a qué pantalla ir después de seleccionar categoría

    def on_enter(self, *args):
        self.update_areas()

    def update_areas(self):
        self.area_spinner.values = self.manager_obj.get_areas()
        self.area_spinner.text = 'Selecciona Área'
        self.update_levels('Selecciona Área') # Reset levels and types
        self.update_types('Selecciona Área', 'Selecciona Nivel')

    def update_levels(self, area):
        self.level_spinner.values = self.manager_obj.get_levels_for_area(area)
        self.level_spinner.text = 'Selecciona Nivel'
        self.update_types(area, 'Selecciona Nivel')

    def update_types(self, area, level):
        self.type_spinner.values = self.manager_obj.get_types_for_level(area, level)
        self.type_spinner.text = 'Selecciona Tipo'

    def create_category_popup(self, category_type):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        input_name = TextInput(hint_text=f"Nombre de nueva {category_type}")
        btn_layout = BoxLayout(size_hint_y=None, height="40dp", spacing=10)
        
        popup = Popup(title=f'Crear Nueva {category_type}', content=content, size_hint=(0.7, 0.3))

        def create_action(instance):
            name = input_name.text.strip()
            if not name:
                self.show_popup("Error", "El nombre no puede estar vacío.")
                return
            
            success = False
            if category_type == 'Área':
                success = self.manager_obj.add_area(name)
            elif category_type == 'Nivel':
                area = self.area_spinner.text
                if area == 'Selecciona Área':
                    self.show_popup("Error", "Primero selecciona un Área.")
                    return
                success = self.manager_obj.add_level(area, name)
            elif category_type == 'Tipo':
                area = self.area_spinner.text
                level = self.level_spinner.text
                if area == 'Selecciona Área' or level == 'Selecciona Nivel':
                    self.show_popup("Error", "Primero selecciona Área y Nivel.")
                    return
                success = self.manager_obj.add_type(area, level, name)

            if success:
                self.show_popup("Éxito", f"{category_type} '{name}' creada.")
                if category_type == 'Área': self.update_areas()
                elif category_type == 'Nivel': self.update_levels(self.area_spinner.text)
                elif category_type == 'Tipo': self.update_types(self.area_spinner.text, self.level_spinner.text)
            else:
                self.show_popup("Error", f"La {category_type} '{name}' ya existe o hubo un error.")
            popup.dismiss()

        btn_layout.add_widget(Button(text="Crear", on_release=create_action))
        btn_layout.add_widget(Button(text="Cancelar", on_release=popup.dismiss))

        content.add_widget(input_name)
        content.add_widget(btn_layout)
        popup.open()

    def confirm_selection(self):
        area = self.area_spinner.text
        level = self.level_spinner.text
        exercise_type = self.type_spinner.text

        if area == 'Selecciona Área' or level == 'Selecciona Nivel' or exercise_type == 'Selecciona Tipo':
            self.show_popup("Error", "Por favor, selecciona Área, Nivel y Tipo.")
            return
        
        # Pasar los datos seleccionados a la siguiente pantalla
        if self.next_screen == 'list_exercises':
            target_screen = self.manager.get_screen('list_exercises')
            target_screen.selected_area = area
            target_screen.selected_level = level
            target_screen.selected_type = exercise_type
        elif self.next_screen == 'add_exercise':
            target_screen = self.manager.get_screen('add_exercise')
            target_screen.selected_area = area
            target_screen.selected_level = level
            target_screen.selected_type = exercise_type
        elif self.next_screen == 'edit_exercise':
            target_screen = self.manager.get_screen('edit_exercise')
            target_screen.selected_area = area
            target_screen.selected_level = level
            target_screen.selected_type = exercise_type
        elif self.next_screen == 'delete_exercise':
            target_screen = self.manager.get_screen('delete_exercise')
            target_screen.selected_area = area
            target_screen.selected_level = level
            target_screen.selected_type = exercise_type
        
        self.manager.current = self.next_screen

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.7, 0.3))
        popup.open()


class ListExercisesScreen(Screen):
    manager_obj = ObjectProperty(None)
    exercises_list_layout = ObjectProperty(None)
    selected_area = StringProperty('')
    selected_level = StringProperty('')
    selected_type = StringProperty('')

    def on_enter(self, *args):
        self.display_exercises()

    def display_exercises(self):
        self.exercises_list_layout.clear_widgets()
        exercises = self.manager_obj.get_exercises_in_category(self.selected_area, self.selected_level, self.selected_type)
        
        if not exercises:
            self.exercises_list_layout.add_widget(Label(text="No hay ejercicios en esta categoría.", size_hint_y=None, height="40dp"))
            return

        for i, ejer in enumerate(exercises):
            box = BoxLayout(orientation='vertical', size_hint_y=None, height="120dp", spacing=5)
            box.add_widget(Label(text=f"Pregunta: {ejer['pregunta']}", halign='left', valign='top', size_hint_y=None, height="30dp", text_size=(self.width - 20, None)))
            box.add_widget(Label(text=f"Tipo: {ejer['tipo']}", halign='left', valign='top', size_hint_y=None, height="20dp", text_size=(self.width - 20, None)))
            box.add_widget(Label(text=f"Explicación: {ejer.get('explicacion', 'N/A')}", halign='left', valign='top', size_hint_y=None, height="30dp", text_size=(self.width - 20, None)))
            self.exercises_list_layout.add_widget(box)


class AddExerciseScreen(Screen):
    manager_obj = ObjectProperty(None)
    selected_area = StringProperty('')
    selected_level = StringProperty('')
    selected_type = StringProperty('')
    question_input = ObjectProperty(None)
    type_spinner = ObjectProperty(None)
    answer_inputs_layout = ObjectProperty(None)
    explanation_input = ObjectProperty(None)

    def on_enter(self, *args):
        self.reset_ui()

    def reset_ui(self):
        self.question_input.text = ''
        self.type_spinner.values = ["seleccion_multiple", "completar_oraciones", "detectar_errores",
                                     "reorganizar_oraciones", "clasificacion_de_palabras", "conjugacion_verbal"]
        self.type_spinner.text = "Selecciona Tipo"
        self.answer_inputs_layout.clear_widgets()
        self.explanation_input.text = ''

    def generate_answer_inputs(self, exercise_type):
        self.answer_inputs_layout.clear_widgets()
        
        if exercise_type == "seleccion_multiple":
            self.answer_inputs_layout.add_widget(Label(text="Opciones (una por línea, vacío para terminar):", size_hint_y=None, height="30dp"))
            self.answer_inputs_layout.add_widget(TextInput(id='options_input', multiline=True, size_hint_y=None, height="80dp", hint_text="Opción 1\nOpción 2\n..."))
            self.answer_inputs_layout.add_widget(Label(text="Respuesta Correcta (una de las opciones):", size_hint_y=None, height="30dp"))
            self.answer_inputs_layout.add_widget(TextInput(id='correct_answer_input_str', multiline=False, size_hint_y=None, height="40dp"))
        elif exercise_type == "completar_oraciones":
            self.answer_inputs_layout.add_widget(Label(text="Palabras Correctas (separadas por comas):", size_hint_y=None, height="30dp"))
            self.answer_inputs_layout.add_widget(TextInput(id='correct_answer_input_list', multiline=False, size_hint_y=None, height="40dp", hint_text="palabra1,palabra2,..."))
        elif exercise_type == "detectar_errores":
            self.answer_inputs_layout.add_widget(Label(text="Palabra Errónea:", size_hint_y=None, height="30dp"))
            self.answer_inputs_layout.add_widget(TextInput(id='error_word_input', multiline=False, size_hint_y=None, height="40dp"))
            self.answer_inputs_layout.add_widget(Label(text="Corrección:", size_hint_y=None, height="30dp"))
            self.answer_inputs_layout.add_widget(TextInput(id='correction_input', multiline=False, size_hint_y=None, height="40dp"))
        else: # Otros tipos de texto simple
            self.answer_inputs_layout.add_widget(Label(text="Respuesta Correcta:", size_hint_y=None, height="30dp"))
            self.answer_inputs_layout.add_widget(TextInput(id='correct_answer_input_str', multiline=False, size_hint_y=None, height="40dp"))

    def get_answer_data_from_ui(self, exercise_type):
        respuesta = None
        opciones = []

        if exercise_type == "seleccion_multiple":
            options_text = self.answer_inputs_layout.ids.options_input.text.strip()
            opciones = [opt.strip() for opt in options_text.split('\n') if opt.strip()]
            respuesta = self.answer_inputs_layout.ids.correct_answer_input_str.text.strip()
            if not opciones:
                self.show_popup("Error", "Debes introducir al menos una opción.")
                return None, None
            if respuesta not in opciones:
                self.show_popup("Error", "La respuesta correcta debe ser una de las opciones.")
                return None, None
        elif exercise_type == "completar_oraciones":
            answer_text = self.answer_inputs_layout.ids.correct_answer_input_list.text.strip()
            respuesta = [s.strip() for s in answer_text.split(',') if s.strip()]
            if not respuesta:
                self.show_popup("Error", "Debes introducir al menos una palabra de respuesta.")
                return None, None
        elif exercise_type == "detectar_errores":
            error_word = self.answer_inputs_layout.ids.error_word_input.text.strip()
            correction = self.answer_inputs_layout.ids.correction_input.text.strip()
            if not error_word or not correction:
                self.show_popup("Error", "Ambos campos de palabra errónea y corrección deben ser llenados.")
                return None, None
            respuesta = {"palabra_erronea": error_word, "correccion": correction}
        else:
            respuesta = self.answer_inputs_layout.ids.correct_answer_input_str.text.strip()
            if not respuesta:
                self.show_popup("Error", "La respuesta no puede estar vacía.")
                return None, None
        
        return respuesta, opciones

    def add_new_exercise(self):
        question = self.question_input.text.strip()
        exercise_type = self.type_spinner.text
        explanation = self.explanation_input.text.strip()

        if not question or exercise_type == "Selecciona Tipo" or not explanation:
            self.show_popup("Error", "Por favor, completa todos los campos principales.")
            return

        respuesta, opciones = self.get_answer_data_from_ui(exercise_type)
        if respuesta is None: # Si hubo un error en get_answer_data_from_ui
            return

        new_exercise_data = {
            "pregunta": question,
            "tipo": exercise_type,
            "respuesta": respuesta,
            "explicacion": explanation
        }
        if opciones:
            new_exercise_data["opciones"] = opciones

        if self.manager_obj.add_exercise(self.selected_area, self.selected_level, self.selected_type, new_exercise_data):
            self.show_popup("Éxito", "Ejercicio añadido exitosamente.")
            self.reset_ui()
        else:
            self.show_popup("Error", "No se pudo añadir el ejercicio. Verifica la categoría.")
        
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.7, 0.3))
        popup.open()


class EditExerciseScreen(Screen):
    manager_obj = ObjectProperty(None)
    selected_area = StringProperty('')
    selected_level = StringProperty('')
    selected_type = StringProperty('')
    exercises_list_layout = ObjectProperty(None)
    current_edit_index = -1
    
    question_input = ObjectProperty(None)
    type_label = ObjectProperty(None) # Solo para mostrar, no para editar
    explanation_input = ObjectProperty(None)
    options_input = ObjectProperty(None) # Para seleccion_multiple
    correct_answer_str_input = ObjectProperty(None) # Para str-based answers
    correct_answer_list_input = ObjectProperty(None) # Para list-based answers
    error_word_input = ObjectProperty(None) # Para detectar_errores
    correction_input = ObjectProperty(None) # Para detectar_errores

    def on_enter(self, *args):
        self.current_edit_index = -1
        self.load_exercises_for_editing()
        self.clear_edit_form()

    def load_exercises_for_editing(self):
        self.exercises_list_layout.clear_widgets()
        exercises = self.manager_obj.get_exercises_in_category(self.selected_area, self.selected_level, self.selected_type)

        if not exercises:
            self.exercises_list_layout.add_widget(Label(text="No hay ejercicios para editar en esta categoría.", size_hint_y=None, height="40dp"))
            return

        for i, ejer in enumerate(exercises):
            btn = Button(text=f"{i+1}. {ejer['pregunta']} ({ejer['tipo']})", 
                         size_hint_y=None, height="50dp",
                         on_release=lambda x, idx=i: self.load_exercise_to_form(idx))
            self.exercises_list_layout.add_widget(btn)

    def load_exercise_to_form(self, index):
        exercises = self.manager_obj.get_exercises_in_category(self.selected_area, self.selected_level, self.selected_type)
        if 0 <= index < len(exercises):
            self.current_edit_index = index
            ejer = exercises[index]
            self.question_input.text = ejer['pregunta']
            self.type_label.text = f"Tipo: {ejer['tipo']}"
            self.explanation_input.text = ejer.get('explicacion', '')
            
            # Limpiar y preparar inputs de respuesta específicos
            self.reset_answer_inputs()

            if ejer['tipo'] == 'seleccion_multiple':
                self.options_input.text = '\n'.join(ejer.get('opciones', []))
                self.correct_answer_str_input.text = ejer['respuesta']
                self.options_input.size_hint_y = None
                self.options_input.height = "80dp"
                self.correct_answer_str_input.size_hint_y = None
                self.correct_answer_str_input.height = "40dp"
            elif ejer['tipo'] == 'completar_oraciones':
                self.correct_answer_list_input.text = ','.join(ejer['respuesta'])
                self.correct_answer_list_input.size_hint_y = None
                self.correct_answer_list_input.height = "40dp"
            elif ejer['tipo'] == 'detectar_errores':
                self.error_word_input.text = ejer['respuesta'].get('palabra_erronea', '')
                self.correction_input.text = ejer['respuesta'].get('correccion', '')
                self.error_word_input.size_hint_y = None
                self.error_word_input.height = "40dp"
                self.correction_input.size_hint_y = None
                self.correction_input.height = "40dp"
            else: # Otros tipos de texto simple
                self.correct_answer_str_input.text = ejer['respuesta']
                self.correct_answer_str_input.size_hint_y = None
                self.correct_answer_str_input.height = "40dp"
        else:
            self.show_popup("Error", "Índice de ejercicio no válido.")

    def reset_answer_inputs(self):
        self.options_input.text = ''
        self.correct_answer_str_input.text = ''
        self.correct_answer_list_input.text = ''
        self.error_word_input.text = ''
        self.correction_input.text = ''

        # Ocultar todos los campos específicos de respuesta
        self.options_input.size_hint_y = 0
        self.options_input.height = 0
        self.correct_answer_str_input.size_hint_y = 0
        self.correct_answer_str_input.height = 0
        self.correct_answer_list_input.size_hint_y = 0
        self.correct_answer_list_input.height = 0
        self.error_word_input.size_hint_y = 0
        self.error_word_input.height = 0
        self.correction_input.size_hint_y = 0
        self.correction_input.height = 0


    def clear_edit_form(self):
        self.current_edit_index = -1
        self.question_input.text = ''
        self.type_label.text = 'Tipo: N/A'
        self.explanation_input.text = ''
        self.reset_answer_inputs()

    def save_edited_exercise(self):
        if self.current_edit_index == -1:
            self.show_popup("Error", "Ningún ejercicio seleccionado para editar.")
            return

        exercises = self.manager_obj.get_exercises_in_category(self.selected_area, self.selected_level, self.selected_type)
        original_ejer = exercises[self.current_edit_index]
        
        updated_data = original_ejer.copy()
        updated_data['pregunta'] = self.question_input.text.strip()
        updated_data['explicacion'] = self.explanation_input.text.strip()

        # Actualizar la respuesta basada en el tipo original
        if updated_data['tipo'] == 'seleccion_multiple':
            options_text = self.options_input.text.strip()
            updated_data['opciones'] = [opt.strip() for opt in options_text.split('\n') if opt.strip()]
            updated_data['respuesta'] = self.correct_answer_str_input.text.strip()
            if not updated_data['opciones']:
                self.show_popup("Error", "Las opciones no pueden estar vacías para selección múltiple.")
                return
            if updated_data['respuesta'] not in updated_data['opciones']:
                self.show_popup("Error", "La respuesta correcta debe ser una de las opciones.")
                return
        elif updated_data['tipo'] == 'completar_oraciones':
            answer_text = self.correct_answer_list_input.text.strip()
            updated_data['respuesta'] = [s.strip() for s in answer_text.split(',') if s.strip()]
            if not updated_data['respuesta']:
                self.show_popup("Error", "Las palabras de respuesta no pueden estar vacías.")
                return
        elif updated_data['tipo'] == 'detectar_errores':
            updated_data['respuesta'] = {
                "palabra_erronea": self.error_word_input.text.strip(),
                "correccion": self.correction_input.text.strip()
            }
            if not updated_data['respuesta']['palabra_erronea'] or not updated_data['respuesta']['correccion']:
                self.show_popup("Error", "La palabra errónea y la corrección no pueden estar vacías.")
                return
        else: # Otros tipos de texto simple
            updated_data['respuesta'] = self.correct_answer_str_input.text.strip()
            if not updated_data['respuesta']:
                self.show_popup("Error", "La respuesta no puede estar vacía.")
                return

        if self.manager_obj.update_exercise(self.selected_area, self.selected_level, self.selected_type, self.current_edit_index, updated_data):
            self.show_popup("Éxito", "Ejercicio actualizado exitosamente.")
            self.load_exercises_for_editing() # Recargar la lista
            self.clear_edit_form()
        else:
            self.show_popup("Error", "No se pudo actualizar el ejercicio.")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.7, 0.3))
        popup.open()


class DeleteExerciseScreen(Screen):
    manager_obj = ObjectProperty(None)
    selected_area = StringProperty('')
    selected_level = StringProperty('')
    selected_type = StringProperty('')
    exercises_list_layout = ObjectProperty(None)

    def on_enter(self, *args):
        self.display_exercises_for_delete()

    def display_exercises_for_delete(self):
        self.exercises_list_layout.clear_widgets()
        exercises = self.manager_obj.get_exercises_in_category(self.selected_area, self.selected_level, self.selected_type)
        
        if not exercises:
            self.exercises_list_layout.add_widget(Label(text="No hay ejercicios para eliminar en esta categoría.", size_hint_y=None, height="40dp"))
            return

        for i, ejer in enumerate(exercises):
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height="60dp", spacing=10)
            box.add_widget(Label(text=f"{i+1}. {ejer['pregunta']} ({ejer['tipo']})", halign='left', valign='middle', text_size=(self.width * 0.7 - 20, None)))
            btn_delete = Button(text="Eliminar", size_hint_x=None, width="100dp",
                                on_release=lambda x, idx=i: self.confirm_delete_exercise(idx))
            box.add_widget(btn_delete)
            self.exercises_list_layout.add_widget(box)

    def confirm_delete_exercise(self, index):
        exercises = self.manager_obj.get_exercises_in_category(self.selected_area, self.selected_level, self.selected_type)
        if 0 <= index < len(exercises):
            ejer_to_delete = exercises[index]
            content = BoxLayout(orientation='vertical', padding=10, spacing=10)
            content.add_widget(Label(text=f"¿Estás seguro de eliminar:\n'{ejer_to_delete['pregunta']}'?", halign='center', valign='middle'))
            
            btn_layout = BoxLayout(size_hint_y=None, height="40dp", spacing=10)
            btn_layout.add_widget(Button(text="Sí, Eliminar", on_release=lambda x: self.delete_selected_exercise(index, popup)))
            btn_layout.add_widget(Button(text="No, Cancelar", on_release=lambda x: popup.dismiss()))
            content.add_widget(btn_layout)

            popup = Popup(title="Confirmar Eliminación", content=content, size_hint=(0.8, 0.4))
            popup.open()
        else:
            self.show_popup("Error", "Índice de ejercicio no válido.")

    def delete_selected_exercise(self, index, popup):
        if self.manager_obj.delete_exercise(self.selected_area, self.selected_level, self.selected_type, index):
            self.show_popup("Éxito", "Ejercicio eliminado exitosamente.")
            self.display_exercises_for_delete() # Recargar la lista
        else:
            self.show_popup("Error", "No se pudo eliminar el ejercicio.")
        popup.dismiss()

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.7, 0.3))
        popup.open()


# --- La App Kivy ---
class CastellanoApp(App):
    manager = ExerciseManager() # Instancia del gestor de lógica

    def build(self):
        sm = ScreenManager()
        
        # Pantallas de práctica
        main_menu = MainMenuScreen(name='main_menu')
        practice_selection = PracticeSelectionScreen(name='practice_selection')
        practice_selection.manager_obj = self.manager # Pasar la referencia
        practice_screen = PracticeScreen(name='practice')
        practice_screen.manager_obj = self.manager # Pasar la referencia

        # Pantallas del editor
        editor_menu = EditorMenuScreen(name='editor_menu')
        
        category_selection_for_list = CategorySelectionScreen(name='category_selection_list')
        category_selection_for_list.manager_obj = self.manager
        category_selection_for_list.next_screen = 'list_exercises' # Indicar a dónde ir después

        category_selection_for_add = CategorySelectionScreen(name='category_selection_add')
        category_selection_for_add.manager_obj = self.manager
        category_selection_for_add.next_screen = 'add_exercise'

        category_selection_for_edit = CategorySelectionScreen(name='category_selection_edit')
        category_selection_for_edit.manager_obj = self.manager
        category_selection_for_edit.next_screen = 'edit_exercise'

        category_selection_for_delete = CategorySelectionScreen(name='category_selection_delete')
        category_selection_for_delete.manager_obj = self.manager
        category_selection_for_delete.next_screen = 'delete_exercise'

        list_exercises_screen = ListExercisesScreen(name='list_exercises')
        list_exercises_screen.manager_obj = self.manager

        add_exercise_screen = AddExerciseScreen(name='add_exercise')
        add_exercise_screen.manager_obj = self.manager

        edit_exercise_screen = EditExerciseScreen(name='edit_exercise')
        edit_exercise_screen.manager_obj = self.manager

        delete_exercise_screen = DeleteExerciseScreen(name='delete_exercise')
        delete_exercise_screen.manager_obj = self.manager


        sm.add_widget(main_menu)
        sm.add_widget(practice_selection)
        sm.add_widget(practice_screen)
        sm.add_widget(editor_menu)
        sm.add_widget(category_selection_for_list)
        sm.add_widget(category_selection_for_add)
        sm.add_widget(category_selection_for_edit)
        sm.add_widget(category_selection_for_delete)
        sm.add_widget(list_exercises_screen)
        sm.add_widget(add_exercise_screen)
        sm.add_widget(edit_exercise_screen)
        sm.add_widget(delete_exercise_screen)

        return sm

if __name__ == '__main__':
    CastellanoApp().run()
