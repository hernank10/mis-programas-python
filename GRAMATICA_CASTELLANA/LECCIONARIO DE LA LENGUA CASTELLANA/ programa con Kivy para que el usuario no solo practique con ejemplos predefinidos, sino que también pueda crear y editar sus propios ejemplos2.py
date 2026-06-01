import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock
import random

kivy.require('2.0.0') # Reemplaza con tu versión de Kivy

# --- Datos de ejemplo para ejercicios (los mismos que hemos usado) ---
# Se recomienda cargar esto desde un archivo JSON o una base de datos real en un proyecto más grande
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

# --- Clases de Pantallas (Screens) ---

class MainMenuScreen(Screen):
    pass # Definido en .kv

class AreaSelectionScreen(Screen):
    pass # Definido en .kv

class LevelSelectionScreen(Screen):
    selected_area = StringProperty("") # Para mostrar en la UI

class ExerciseTypeSelectionScreen(Screen):
    selected_area = StringProperty("")
    selected_level = StringProperty("")

class ExerciseScreen(Screen):
    question_text = StringProperty("")
    feedback_text = StringProperty("")
    current_exercise_type = StringProperty("")
    options_list = ListProperty([]) # Para selección múltiple
    user_inputs = ListProperty([]) # Para completar oraciones, detectar errores, etc.

    # Usaremos estas propiedades para enlazar con los widgets en el .kv
    input1 = ObjectProperty(None) # Para el primer TextInput (ej. en detectar errores)
    input2 = ObjectProperty(None) # Para el segundo TextInput (ej. en detectar errores)

    def on_enter(self, *args):
        self.parent.app.display_next_exercise() # Llama al método del App al entrar a esta pantalla

    def check_answer(self):
        app = self.parent.app
        ejercicio = app.exercises_to_run[app.current_exercise_index -1] # El ejercicio actual
        is_correct = False
        feedback_message = ""

        if self.current_exercise_type == 'seleccion_multiple':
            # Obtener el texto del botón seleccionado (solo uno puede estar "down")
            selected_option_widget = next((btn for btn in self.ids.options_layout.children if btn.state == 'down'), None)
            user_answer = selected_option_widget.text.lower() if selected_option_widget else ""
            is_correct = (user_answer == ejercicio['respuesta'].lower())
            
        elif self.current_exercise_type == 'completar_oraciones':
            user_answers = [ti.text.strip().lower() for ti in self.ids.inputs_layout.children if isinstance(ti, TextInput)]
            # Invertir el orden ya que Kivy añade los widgets de derecha a izquierda por defecto en BoxLayout
            user_answers.reverse() 
            correct_answers_normalized = [r.lower() for r in ejercicio['respuesta']]
            is_correct = (user_answers == correct_answers_normalized)

        elif self.current_exercise_type == 'detectar_errores':
            error_word = self.ids.error_word_input.text.strip().lower()
            correction = self.ids.correction_input.text.strip().lower()
            is_correct = (error_word == ejercicio['respuesta']['palabra_erronea'].lower() and
                          correction == ejercicio['respuesta']['correccion'].lower())
        
        elif self.current_exercise_type == 'reorganizar_oraciones':
            user_answer = self.ids.reorder_input.text.strip()
            normalized_user_answer = ' '.join(user_answer.split()).lower()
            normalized_correct_answer = ' '.join(ejercicio['respuesta'].split()).lower()
            is_correct = (normalized_user_answer == normalized_correct_answer)

        elif self.current_exercise_type == 'clasificacion_de_palabras':
            user_answer = self.ids.classification_input.text.strip().lower()
            is_correct = (user_answer == ejercicio['respuesta'].lower())

        elif self.current_exercise_type == 'conjugacion_verbal':
            user_answer = self.ids.conjugation_input.text.strip().lower()
            is_correct = (user_answer == ejercicio['respuesta'].lower())

        # Proporcionar feedback visual y lógico
        if is_correct:
            self.parent.app.score += 1
            feedback_message = f"¡Correcto! ✅\n"
        else:
            feedback_message = f"Incorrecto. ❌\n"
        
        self.feedback_text = feedback_message + f"Explicación: {ejercicio['explicacion']}"
        
        # Usar Clock.schedule_once para mostrar el feedback y luego pasar al siguiente ejercicio
        # Esto permite que el usuario vea el feedback antes de que la pantalla cambie
        Clock.schedule_once(lambda dt: self.parent.app.go_to_next_exercise(), 2) # Espera 2 segundos

class ResultsScreen(Screen):
    final_score_text = StringProperty("")
    total_questions_text = StringProperty("")

# --- Clase Principal de la Aplicación Kivy ---
class CastellanoApp(App):
    area_selection_screen = ObjectProperty(None)
    level_selection_screen = ObjectProperty(None)
    exercise_type_selection_screen = ObjectProperty(None)
    exercise_screen = ObjectProperty(None)
    results_screen = ObjectProperty(None)

    current_area = StringProperty("")
    current_nivel = StringProperty("")
    current_tipo_ejercicio = StringProperty("")

    exercises_to_run = ListProperty([])
    current_exercise_index = NumericProperty(0)
    score = NumericProperty(0)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainMenuScreen(name='main_menu'))
        
        self.area_selection_screen = AreaSelectionScreen(name='area_selection')
        self.sm.add_widget(self.area_selection_screen)

        self.level_selection_screen = LevelSelectionScreen(name='level_selection')
        self.sm.add_widget(self.level_selection_screen)

        self.exercise_type_selection_screen = ExerciseTypeSelectionScreen(name='exercise_type_selection')
        self.sm.add_widget(self.exercise_type_selection_screen)

        self.exercise_screen = ExerciseScreen(name='exercise_screen')
        self.sm.add_widget(self.exercise_screen)

        self.results_screen = ResultsScreen(name='results_screen')
        self.sm.add_widget(self.results_screen)

        return self.sm

    def show_area_selection(self):
        # Reiniciar propiedades de selección en caso de volver atrás
        self.current_area = ""
        self.current_nivel = ""
        self.current_tipo_ejercicio = ""

        # Limpiar botones anteriores y añadir nuevos dinámicamente
        self.area_selection_screen.ids.area_buttons_layout.clear_widgets()
        areas = list(EJERCICIOS_DATA.keys())
        for area_name in areas:
            btn = Button(text=area_name, size_hint_y=None, height=50)
            btn.bind(on_release=lambda instance, a=area_name: self.select_area(a))
            self.area_selection_screen.ids.area_buttons_layout.add_widget(btn)
        
        self.sm.current = 'area_selection'

    def select_area(self, area):
        self.current_area = area
        self.level_selection_screen.selected_area = area # Actualizar la propiedad de la pantalla
        
        # Limpiar y añadir botones de nivel dinámicamente
        self.level_selection_screen.ids.level_buttons_layout.clear_widgets()
        niveles = list(EJERCICIOS_DATA[area].keys())
        for nivel_name in niveles:
            btn = Button(text=nivel_name, size_hint_y=None, height=50)
            btn.bind(on_release=lambda instance, n=nivel_name: self.select_level(area, n))
            self.level_selection_screen.ids.level_buttons_layout.add_widget(btn)

        self.sm.current = 'level_selection'

    def select_level(self, area, nivel):
        self.current_area = area
        self.current_nivel = nivel
        self.exercise_type_selection_screen.selected_area = area
        self.exercise_type_selection_screen.selected_level = nivel

        # Limpiar y añadir botones de tipo de ejercicio dinámicamente
        self.exercise_type_selection_screen.ids.type_buttons_layout.clear_widgets()
        tipos_ejercicios = list(EJERCICIOS_DATA[area][nivel].keys())
        for tipo_name in tipos_ejercicios:
            btn = Button(text=tipo_name, size_hint_y=None, height=50)
            btn.bind(on_release=lambda instance, t=tipo_name: self.start_practice(area, nivel, t))
            self.exercise_type_selection_screen.ids.type_buttons_layout.add_widget(btn)

        self.sm.current = 'exercise_type_selection'

    def start_practice(self, area, nivel, tipo_ejercicio):
        self.current_area = area
        self.current_nivel = nivel
        self.current_tipo_ejercicio = tipo_ejercicio
        
        self.exercises_to_run = list(EJERCICIOS_DATA[area][nivel][tipo_ejercicio])
        random.shuffle(self.exercises_to_run)
        self.current_exercise_index = 0
        self.score = 0
        self.sm.current = 'exercise_screen' # Al cambiar de pantalla, se llamará a on_enter de ExerciseScreen

    def display_next_exercise(self):
        if self.current_exercise_index < len(self.exercises_to_run):
            ejercicio = self.exercises_to_run[self.current_exercise_index]
            self.current_exercise_index += 1 # Incrementar para la siguiente vez
            
            self.exercise_screen.question_text = f"Pregunta {self.current_exercise_index}/{len(self.exercises_to_run)}: {ejercicio['pregunta']}"
            self.exercise_screen.feedback_text = "" # Limpiar feedback anterior
            self.exercise_screen.current_exercise_type = ejercicio['tipo'] # Actualizar tipo de ejercicio en la pantalla
            
            # Limpiar widgets dinámicos anteriores
            self.exercise_screen.ids.dynamic_exercise_content.clear_widgets()

            if ejercicio['tipo'] == 'seleccion_multiple':
                options_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=len(ejercicio['opciones']) * 60)
                # Kivy ToggleButton permite grupos de radio buttons
                for option_text in ejercicio['opciones']:
                    btn = ToggleButton(text=option_text, group='options_group', size_hint_y=None, height=50)
                    options_layout.add_widget(btn)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(options_layout)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Button(text="Comprobar", on_release=lambda x: self.exercise_screen.check_answer(), size_hint_y=None, height=50))
                # Guardar referencia al layout de opciones para la comprobación
                self.exercise_screen.ids.options_layout = options_layout 

            elif ejercicio['tipo'] == 'completar_oraciones':
                inputs_layout = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=None, height=50)
                num_espacios = ejercicio['pregunta'].count('___')
                parts = ejercicio['pregunta'].split('___')
                
                # Crear widgets para la oración y los inputs
                for i, part in enumerate(parts):
                    if part:
                        inputs_layout.add_widget(Label(text=part, size_hint_x=None, width=len(part)*10+20)) # Ancho aproximado
                    if i < num_espacios:
                        text_input = TextInput(multiline=False, size_hint_x=None, width=100)
                        inputs_layout.add_widget(text_input)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(inputs_layout)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Button(text="Comprobar", on_release=lambda x: self.exercise_screen.check_answer(), size_hint_y=None, height=50))
                # Guardar referencia al layout de inputs para la comprobación
                self.exercise_screen.ids.inputs_layout = inputs_layout

            elif ejercicio['tipo'] == 'detectar_errores':
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Label(text="Palabra errónea:", size_hint_y=None, height=30))
                error_input = TextInput(multiline=False, size_hint_y=None, height=40)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(error_input)
                self.exercise_screen.ids.error_word_input = error_input # Guardar referencia
                
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Label(text="Corrección:", size_hint_y=None, height=30))
                correction_input = TextInput(multiline=False, size_hint_y=None, height=40)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(correction_input)
                self.exercise_screen.ids.correction_input = correction_input # Guardar referencia
                
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Button(text="Comprobar", on_release=lambda x: self.exercise_screen.check_answer(), size_hint_y=None, height=50))
            
            elif ejercicio['tipo'] == 'reorganizar_oraciones':
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Label(text="Ordena las palabras:", size_hint_y=None, height=30))
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Label(text=ejercicio['pregunta'], font_size=18, size_hint_y=None, height=40))
                reorder_input = TextInput(multiline=False, size_hint_y=None, height=40)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(reorder_input)
                self.exercise_screen.ids.reorder_input = reorder_input
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Button(text="Comprobar", on_release=lambda x: self.exercise_screen.check_answer(), size_hint_y=None, height=50))
            
            elif ejercicio['tipo'] == 'clasificacion_de_palabras':
                classification_input = TextInput(multiline=False, size_hint_y=None, height=40)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(classification_input)
                self.exercise_screen.ids.classification_input = classification_input
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Button(text="Comprobar", on_release=lambda x: self.exercise_screen.check_answer(), size_hint_y=None, height=50))
            
            elif ejercicio['tipo'] == 'conjugacion_verbal':
                conjugation_input = TextInput(multiline=False, size_hint_y=None, height=40)
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(conjugation_input)
                self.exercise_screen.ids.conjugation_input = conjugation_input
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Button(text="Comprobar", on_release=lambda x: self.exercise_screen.check_answer(), size_hint_y=None, height=50))
            
            else:
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Label(text="Tipo de ejercicio no implementado para GUI aún.", color=(1,0,0,1)))
                self.exercise_screen.ids.dynamic_exercise_content.add_widget(Button(text="Siguiente Ejercicio (no implementado)", on_release=lambda x: self.go_to_next_exercise()))

        else:
            self.show_results()

    def go_to_next_exercise(self):
        # Limpiar el feedback de la pantalla de ejercicio
        self.exercise_screen.feedback_text = ""
        # Volver a llamar a display_next_exercise para cargar el siguiente o los resultados
        self.display_next_exercise()

    def show_results(self):
        self.results_screen.final_score_text = f"Obtuviste {self.score} de {len(self.exercises_to_run)} preguntas correctas."
        self.results_screen.total_questions_text = "¡Sigue practicando para mejorar! 💪"
        self.sm.current = 'results_screen'

if __name__ == '__main__':
    CastellanoApp().run()
