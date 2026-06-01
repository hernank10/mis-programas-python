import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton # Para RadioButton-like behavior
from kivy.core.window import Window # Para ajustar el tamaño de la ventana si es necesario

# Cargar el archivo KV antes de la clase App
Builder.load_file('lesson7.kv')

class MainMenuScreen(Screen):
    pass # Definido principalmente en KV Lang

class TheoryScreen(Screen):
    pass # Contenido cargado desde KV, o dinámicamente si es muy largo

class ExamplesScreen(Screen):
    pass # Contenido cargado desde KV

class ExercisesScreen(Screen):
    current_question_index = NumericProperty(0)
    identification_score = NumericProperty(0)
    evidence_good_count = NumericProperty(0)
    feedback_text = StringProperty('')
    model_evidence_text = StringProperty('')
    user_evidence_input = ObjectProperty(None) # Para referenciar el TextInput desde Python

    identification_exercises = [
        {"q": "La oración 'El Sol es una estrella' es un...", "opt": ["Hecho", "Opinión"], "ans": 0},
        {"q": "La oración 'Los lunes son el peor día de la semana' es una...", "opt": ["Hecho", "Opinión"], "ans": 1},
        # ... más ejercicios
    ]

    evidence_exercises = [
        {"statement": "El ejercicio físico mejora la salud.", "evidence_model": "Un estudio de la OMS..."},
        {"statement": "La lectura fomenta el desarrollo cognitivo en los niños.", "evidence_model": "Investigaciones de la Universidad de Oxford..."},
        # ... más ejercicios (hasta 12)
    ]

    def on_enter(self, *args):
        # Se ejecuta cuando se entra a esta pantalla
        self.reset_exercises()

    def reset_exercises(self):
        self.current_question_index = 0
        self.identification_score = 0
        self.evidence_good_count = 0
        random.shuffle(self.identification_exercises)
        random.shuffle(self.evidence_exercises)
        self.load_current_exercise()

    def load_current_exercise(self):
        self.feedback_text = ''
        self.model_evidence_text = ''
        
        # Limpiar widgets dinámicos si existen
        # En Kivy, es común re-crear los widgets para cada pregunta o usar un 'Adapter' para listas
        # Aquí, por simplicidad, se asumiría que los widgets existen y se actualizan sus propiedades
        
        if self.current_question_index < len(self.identification_exercises):
            # Cargar ejercicio de identificación (Hecho/Opinión)
            ex = self.identification_exercises[self.current_question_index]
            self.ids.question_label.text = f"Parte 1: Hechos u Opiniones (Pregunta {self.current_question_index + 1} de {len(self.identification_exercises)})\n{ex['q']}"
            
            # Limpiar y recrear ToggleButtons para las opciones
            self.ids.options_layout.clear_widgets()
            for i, opt in enumerate(ex['opt']):
                btn = ToggleButton(text=opt, group='identification_options', font_size=20, size_hint_y=None, height=50)
                btn.bind(on_release=lambda x, index=i: self.check_identification_answer(index))
                self.ids.options_layout.add_widget(btn)
            
            self.ids.exercise_section_layout.height = '300dp' # Ajustar altura para esta sección
            self.ids.submit_button.text = "Verificar Respuesta"
            self.ids.submit_button.bind(on_release=self.check_identification_answer_wrapper) # Usamos un wrapper para pasar el control
            self.ids.user_input_section.clear_widgets() # Asegurarse de que no esté visible
            self.ids.model_output_section.clear_widgets() # Asegurarse de que no esté visible


        elif self.current_question_index - len(self.identification_exercises) < len(self.evidence_exercises):
            # Cargar ejercicio de añadir evidencia
            evidence_index = self.current_question_index - len(self.identification_exercises)
            ex = self.evidence_exercises[evidence_index]
            self.ids.question_label.text = f"Parte 2: Añade Evidencia (Ejercicio {evidence_index + 1} de {len(self.evidence_exercises)})\nAfirmación: '{ex['statement']}'"
            
            self.ids.options_layout.clear_widgets() # Limpiar opciones anteriores
            
            # Configurar el TextInput para la evidencia del usuario
            if not self.ids.user_evidence_input: # Crea el TextInput una vez si no existe
                self.user_evidence_input = TextInput(hint_text="Tu evidencia aquí...", multiline=True, font_size=18, size_hint_y=None, height=100)
                self.ids.user_input_section.add_widget(self.user_evidence_input)
            else:
                 self.ids.user_input_section.clear_widgets() # Limpiar y re-agregar si ya existía para asegurar el layout
                 self.ids.user_input_section.add_widget(self.user_evidence_input)
                 self.user_evidence_input.text = '' # Limpiar texto

            self.ids.exercise_section_layout.height = '400dp' # Ajustar altura
            self.ids.submit_button.text = "Verificar y Autoevaluar"
            self.ids.submit_button.bind(on_release=self.reveal_model_and_evaluate_wrapper) # Usamos un wrapper
            self.ids.model_output_section.clear_widgets() # Asegurarse de que no esté visible
        else:
            self.show_results()

    def check_identification_answer_wrapper(self, instance):
        # Desactivar el botón para evitar múltiples clics
        self.ids.submit_button.disabled = True
        
        selected_index = -1
        # En Kivy, con ToggleButtons, la variable group nos ayuda
        for btn in self.ids.options_layout.children:
            if btn.state == 'down':
                selected_index = self.identification_exercises[self.current_question_index]['opt'].index(btn.text)
                break
        
        if selected_index == self.identification_exercises[self.current_question_index]['ans']:
            self.feedback_text = '¡Correcto! ✅'
            self.identification_score += 1
        else:
            self.feedback_text = '¡Incorrecto! ❌'
        
        # Pequeña pausa visual antes de la siguiente pregunta
        Clock.schedule_once(self.go_next_exercise, 1.5)


    def reveal_model_and_evaluate_wrapper(self, instance):
        user_text = self.user_evidence_input.text.strip()
        if not user_text:
            self.feedback_text = "Por favor, escribe tu evidencia."
            return

        evidence_index = self.current_question_index - len(self.identification_exercises)
        model_text = self.evidence_exercises[evidence_index]['evidence_model']
        self.model_evidence_text = f"Una posible evidencia sería: '{model_text}'"
        
        # Quitar el botón de submit y poner los de autoevaluación
        self.ids.submit_button.disabled = True
        self.ids.user_input_section.clear_widgets() # Remove user input box
        
        self.ids.model_output_section.clear_widgets()
        self.ids.model_output_section.add_widget(Label(text=self.model_evidence_text, font_size=16, color=(0,0,1,1), text_size=(self.ids.model_output_section.width, None), halign='left', valign='top'))

        # Add self-evaluation buttons
        self.self_evaluation_var = NumericProperty(0) # Use a Kivy property for reactive updates
        self.ids.model_output_section.add_widget(Label(text="\n¿Consideras que tu evidencia es fuerte y lógica?", font_size=18))
        
        yes_btn = ToggleButton(text="Sí, creo que es buena.", group='evaluation', font_size=18, size_hint_y=None, height=50)
        no_btn = ToggleButton(text="No, necesito mejorarla.", group='evaluation', font_size=18, size_hint_y=None, height=50)
        
        # Bind to a method that saves the choice and then proceeds
        yes_btn.bind(on_release=lambda x: self._save_evaluation_and_proceed(1))
        no_btn.bind(on_release=lambda x: self._save_evaluation_and_proceed(0))
        
        self.ids.model_output_section.add_widget(yes_btn)
        self.ids.model_output_section.add_widget(no_btn)
        
    def _save_evaluation_and_proceed(self, value):
        self.self_evaluation_var = value
        if value == 1:
            self.evidence_good_count += 1
        Clock.schedule_once(self.go_next_exercise, 0.5) # Short delay before next question
        

    def go_next_exercise(self, dt):
        # Asegurarse de que el botón de submit se vuelva a activar si se usa
        self.ids.submit_button.disabled = False
        self.current_question_index += 1
        self.load_current_exercise()

    def show_results(self):
        self.feedback_text = (
            f"¡Ejercicios Terminados!\n"
            f"Parte 1 (Hechos/Opiniones) correctas: {self.identification_score} de {len(self.identification_exercises)}.\n"
            f"Parte 2 (Tus evidencias fuertes): {self.evidence_good_count} de {len(self.evidence_exercises)}.\n"
            f"¡Sigue fortaleciendo tus argumentos!"
        )
        # Aquí puedes cambiar a una pantalla de resultados o mostrar un popup
        self.manager.current = 'main_menu' # Volver al menú principal por ahora

class ArgumentBuilderScreen(Screen):
    # Propiedades para almacenar la tesis, razón, evidencia
    thesis_text = StringProperty('')
    reason_text = StringProperty('')
    evidence_text = StringProperty('')
    full_argument_display = StringProperty('')

    def build_argument(self):
        thesis = self.ids.thesis_input.text.strip()
        reason = self.ids.reason_input.text.strip()
        evidence = self.ids.evidence_input.text.strip()

        if not thesis or not reason or not evidence:
            self.full_argument_display = "Por favor, completa todos los campos (Tesis, Razón, Evidencia)."
            return

        self.full_argument_display = (
            f"--- Tu Argumento Completo ---\n"
            f"Tesis: '{thesis}'\n"
            f"Razón: '{reason}'\n"
            f"Evidencia: '{evidence}'\n\n"
            f"¡Excelente! Has construido un argumento completo. ¡La práctica hace al maestro!"
        )

class LessonApp(App):
    def build(self):
        self.title = "Lección 7: Argumentación (Kivy)"
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(TheoryScreen(name='theory'))
        sm.add_widget(ExamplesScreen(name='examples'))
        sm.add_widget(ExercisesScreen(name='exercises'))
        sm.add_widget(ArgumentBuilderScreen(name='build_argument'))
        return sm

if __name__ == '__main__':
    from kivy.clock import Clock # Importar Clock aquí para usarlo en la clase
    LessonApp().run()
