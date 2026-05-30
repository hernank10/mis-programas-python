from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.metrics import dp, sp
from kivy.utils import get_color_from_hex

import random
from datetime import datetime

class Exercise:
    def __init__(self, exercise_type, instruction, spanish_sentence, correct_answer, hint, difficulty):
        self.type = exercise_type
        self.instruction = instruction
        self.spanish_sentence = spanish_sentence
        self.correct_answer = correct_answer
        self.hint = hint
        self.difficulty = difficulty

class ExerciseWidget(BoxLayout):
    def __init__(self, exercise, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(15)
        
        # Tipo y dificultad
        type_layout = BoxLayout(size_hint_y=None, height=dp(40))
        type_layout.add_widget(Label(
            text=f'[b]{exercise.type}[/b]',
            markup=True,
            font_size=sp(18),
            color=get_color_from_hex('#2C3E50'),
            size_hint_x=0.7
        ))
        type_layout.add_widget(Label(
            text=f'[{exercise.difficulty.upper()}]',
            font_size=sp(14),
            color=get_color_from_hex('#3498DB'),
            size_hint_x=0.3
        ))
        self.add_widget(type_layout)
        
        # Instrucción
        self.add_widget(Label(
            text=exercise.instruction,
            font_size=sp(16),
            color=get_color_from_hex('#3498DB'),
            size_hint_y=None,
            height=dp(40)
        ))
        
        # Oración en español
        self.add_widget(Label(
            text=f'[i]"{exercise.spanish_sentence}"[/i]',
            markup=True,
            font_size=sp(16),
            color=get_color_from_hex('#3498DB'),
            size_hint_y=None,
            height=dp(60)
        ))

class StatsModal(ModalView):
    def __init__(self, stats_data, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.9, 0.8)
        self.auto_dismiss = True
        
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Título
        title = Label(
            text='[b]📊 Estadísticas Detalladas[/b]',
            markup=True,
            font_size=sp(22),
            size_hint_y=None,
            height=dp(50)
        )
        layout.add_widget(title)
        
        # Contenido de estadísticas
        scroll = ScrollView()
        stats_layout = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        stats_layout.bind(minimum_height=stats_layout.setter('height'))
        
        for stat in stats_data:
            stats_layout.add_widget(Label(
                text=f'[b]{stat["label"]}:[/b]',
                markup=True,
                font_size=sp(16),
                size_hint_y=None,
                height=dp(30)
            ))
            stats_layout.add_widget(Label(
                text=str(stat["value"]),
                font_size=sp(16),
                size_hint_y=None,
                height=dp(30)
            ))
        
        scroll.add_widget(stats_layout)
        layout.add_widget(scroll)
        
        # Botón cerrar
        close_btn = Button(
            text='Cerrar',
            size_hint_y=None,
            height=dp(50),
            background_color=get_color_from_hex('#3498DB')
        )
        close_btn.bind(on_press=self.dismiss)
        layout.add_widget(close_btn)
        
        self.add_widget(layout)

class EnglishQuestionsApp(App):
    current_exercise = NumericProperty(0)
    score = NumericProperty(0)
    progress = NumericProperty(0)
    time_elapsed = StringProperty("00:00")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exercises = []
        self.all_exercises = []
        self.start_time = None
        self.mastered_structures = set()
        self.hints_used = 0
        self.clock_event = None
        
    def build(self):
        # Configurar la ventana
        Window.clearcolor = get_color_from_hex('#3498DB')
        self.title = "🏆 Entrenador de Preguntas en Inglés"
        
        # Inicializar ejercicios
        self.initialize_exercises()
        self.all_exercises = self.complete_100_exercises()
        
        # Layout principal
        self.main_layout = BoxLayout(orientation='vertical', spacing=dp(10))
        
        # Header con progreso
        self.setup_header()
        
        # Área de ejercicio
        self.setup_exercise_area()
        
        # Área de respuesta
        self.setup_answer_area()
        
        # Controles
        self.setup_controls()
        
        # Iniciar timer
        self.start_time = datetime.now()
        self.clock_event = Clock.schedule_interval(self.update_time, 1)
        
        # Cargar primer ejercicio
        self.load_exercise()
        
        return self.main_layout
    
    def setup_header(self):
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(120))
        
        # Título
        title = Label(
            text='[b]🏆 ENTRENADOR DE PREGUNTAS EN INGLÉS[/b]',
            markup=True,
            font_size=sp(20),
            size_hint_y=None,
            height=dp(40)
        )
        header.add_widget(title)
        
        # Barra de progreso
        self.progress_bar = ProgressBar(
            max=100,
            size_hint_y=None,
            height=dp(20)
        )
        header.add_widget(self.progress_bar)
        
        # Stats en tiempo real
        stats_layout = GridLayout(cols=3, size_hint_y=None, height=dp(40))
        
        self.progress_label = Label(
            text='Ejercicio: 0/100',
            font_size=sp(14)
        )
        stats_layout.add_widget(self.progress_label)
        
        self.score_label = Label(
            text='Puntuación: 0',
            font_size=sp(14)
        )
        stats_layout.add_widget(self.score_label)
        
        self.time_label = Label(
            text='Tiempo: 00:00',
            font_size=sp(14)
        )
        stats_layout.add_widget(self.time_label)
        
        header.add_widget(stats_layout)
        self.main_layout.add_widget(header)
    
    def setup_exercise_area(self):
        exercise_scroll = ScrollView(size_hint_y=0.4)
        self.exercise_layout = BoxLayout(
            orientation='vertical', 
            size_hint_y=None,
            padding=dp(20),
            spacing=dp(15)
        )
        self.exercise_layout.bind(minimum_height=self.exercise_layout.setter('height'))
        exercise_scroll.add_widget(self.exercise_layout)
        self.main_layout.add_widget(exercise_scroll)
    
    def setup_answer_area(self):
        answer_layout = BoxLayout(orientation='vertical', size_hint_y=0.3, spacing=dp(10))
        
        # Label para respuesta
        answer_layout.add_widget(Label(
            text='[b]Tu respuesta:[/b]',
            markup=True,
            font_size=sp(16),
            size_hint_y=None,
            height=dp(30)
        ))
        
        # Campo de texto para respuesta
        self.answer_input = TextInput(
            multiline=True,
            size_hint_y=0.7,
            font_size=sp(16),
            background_color=get_color_from_hex('#3498DB')
        )
        answer_layout.add_widget(self.answer_input)
        
        # Área de feedback
        self.feedback_label = Label(
            text='',
            font_size=sp(14),
            size_hint_y=0.3,
            text_size=(None, None),
            color=get_color_from_hex('#2C3E50')
        )
        answer_layout.add_widget(self.feedback_label)
        
        self.main_layout.add_widget(answer_layout)
    
    def setup_controls(self):
        controls_layout = GridLayout(cols=4, size_hint_y=None, height=dp(60), spacing=dp(10))
        
        # Botón Enviar
        self.submit_btn = Button(
            text='✅ Enviar',
            background_color=get_color_from_hex('#27AE60')
        )
        self.submit_btn.bind(on_press=self.check_answer)
        controls_layout.add_widget(self.submit_btn)
        
        # Botón Pista
        self.hint_btn = Button(
            text='💡 Pista',
            background_color=get_color_from_hex('#F39C12')
        )
        self.hint_btn.bind(on_press=self.show_hint)
        controls_layout.add_widget(self.hint_btn)
        
        # Botón Saltar
        self.skip_btn = Button(
            text='⏭️ Saltar',
            background_color=get_color_from_hex('#E74C3C')
        )
        self.skip_btn.bind(on_press=self.skip_exercise)
        controls_layout.add_widget(self.skip_btn)
        
        # Botón Estadísticas
        self.stats_btn = Button(
            text='📊 Stats',
            background_color=get_color_from_hex('#3498DB')
        )
        self.stats_btn.bind(on_press=self.show_statistics)
        controls_layout.add_widget(self.stats_btn)
        
        self.main_layout.add_widget(controls_layout)
    
    def initialize_exercises(self):
        self.exercises = [
            Exercise(
                "Preguntas con 'to be' - Presente",
                "Convierte la afirmación en pregunta usando 'to be' en presente:",
                "Él es profesor",
                "Is he a teacher?",
                "Recuerda invertir el orden: Verbo + Sujeto + Complemento",
                "básico"
            ),
            Exercise(
                "Preguntas con 'to be' - Presente",
                "Convierte la afirmación en pregunta usando 'to be' en presente:",
                "Ellos están en casa",
                "Are they at home?",
                "They → they, 'están' → are",
                "básico"
            ),
            Exercise(
                "Preguntas con Do/Does - Presente",
                "Convierte en pregunta usando Do/Does:",
                "Ella trabaja aquí",
                "Does she work here?",
                "She/he/it → DOES + verbo en forma base (sin -s)",
                "básico"
            ),
            Exercise(
                "Preguntas con Do/Does - Presente",
                "Convierte en pregunta usando Do/Does:",
                "Nosotros vivimos en Madrid",
                "Do we live in Madrid?",
                "I/you/we/they → DO + verbo en forma base",
                "básico"
            ),
            Exercise(
                "Preguntas con What",
                "Formula una pregunta con WHAT para esta respuesta:",
                "RESPUESTA: I want a coffee",
                "What do you want?",
                "What + do/does/did + sujeto + verbo",
                "intermedio"
            ),
            Exercise(
                "Preguntas con Where",
                "Formula una pregunta con WHERE:",
                "RESPUESTA: She lives in London",
                "Where does she live?",
                "Where + does + she + live?",
                "intermedio"
            )
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
                # Crear variaciones del ejercicio
                modified_spanish = exercise.spanish_sentence
                modified_answer = exercise.correct_answer
                
                for original, replacement in variations[i % len(variations)].items():
                    if original.lower() in modified_spanish.lower():
                        modified_spanish = modified_spanish.replace(original, replacement)
                        modified_answer = modified_answer.replace(original, replacement)
                
                new_exercise = Exercise(
                    exercise.type,
                    exercise.instruction,
                    modified_spanish,
                    modified_answer,
                    exercise.hint,
                    exercise.difficulty
                )
                completed_exercises.append(new_exercise)

        random.shuffle(completed_exercises)
        return completed_exercises[:100]
    
    def load_exercise(self):
        if self.current_exercise >= len(self.all_exercises):
            self.show_final_results()
            return
        
        # Limpiar layout de ejercicio
        self.exercise_layout.clear_widgets()
        
        exercise = self.all_exercises[self.current_exercise]
        exercise_widget = ExerciseWidget(exercise)
        self.exercise_layout.add_widget(exercise_widget)
        
        # Limpiar campos
        self.answer_input.text = ''
        self.feedback_label.text = ''
        
        # Actualizar progreso
        self.update_progress()
    
    def update_progress(self):
        self.progress = (self.current_exercise / len(self.all_exercises)) * 100
        self.progress_bar.value = self.progress
        self.progress_label.text = f'Ejercicio: {self.current_exercise + 1}/{len(self.all_exercises)}'
        self.score_label.text = f'Puntuación: {self.score}'
    
    def update_time(self, dt):
        if self.start_time:
            elapsed = datetime.now() - self.start_time
            minutes = elapsed.seconds // 60
            seconds = elapsed.seconds % 60
            self.time_label.text = f'Tiempo: {minutes:02d}:{seconds:02d}'
            self.time_elapsed = f'{minutes:02d}:{seconds:02d}'
    
    def check_answer(self, instance):
        user_answer = self.answer_input.text.strip()
        if not user_answer:
            self.feedback_label.text = '[color=#E74C3C]Por favor, escribe una respuesta.[/color]'
            return
        
        exercise = self.all_exercises[self.current_exercise]
        is_correct, feedback_type = self.verify_answer(user_answer, exercise.correct_answer)
        
        if is_correct:
            self.feedback_label.text = '[color=#27AE60]✅ ¡CORRECTO![/color]'
            self.score += 2 if feedback_type == "exacta" else 1
            self.mastered_structures.add(exercise.type)
            
            # Mostrar respuesta correcta
            Clock.schedule_once(lambda dt: self.show_correct_answer(exercise), 1.5)
        else:
            self.feedback_label.text = '[color=#E74C3C]❌ INCORRECTO. Intenta nuevamente.[/color]'
    
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
    
    def show_correct_answer(self, exercise):
        self.feedback_label.text = f'[color=#2980B9]📝 Respuesta correcta: {exercise.correct_answer}\n\n💡 {exercise.hint}[/color]'
        
        # Siguiente ejercicio después de 3 segundos
        Clock.schedule_once(lambda dt: self.next_exercise(), 3)
    
    def show_hint(self, instance):
        exercise = self.all_exercises[self.current_exercise]
        self.hints_used += 1
        self.feedback_label.text = f'[color=#F39C12]💡 PISTA: {exercise.hint}[/color]'
    
    def skip_exercise(self, instance):
        self.next_exercise()
    
    def next_exercise(self):
        self.current_exercise += 1
        if self.current_exercise < len(self.all_exercises):
            self.load_exercise()
        else:
            self.show_final_results()
    
    def show_statistics(self, instance):
        stats_data = [
            {"label": "Ejercicios completados", "value": f"{self.current_exercise}/100"},
            {"label": "Puntuación total", "value": self.score},
            {"label": "Porcentaje de acierto", "value": f"{(self.score / (self.current_exercise * 2)) * 100:.1f}%"},
            {"label": "Tiempo transcurrido", "value": self.time_elapsed},
            {"label": "Pistas utilizadas", "value": self.hints_used},
            {"label": "Estructuras dominadas", "value": len(self.mastered_structures)}
        ]
        
        modal = StatsModal(stats_data)
        modal.open()
    
    def show_final_results(self):
        total_time = datetime.now() - self.start_time
        minutes = total_time.seconds // 60
        seconds = total_time.seconds % 60
        accuracy = (self.score / (len(self.all_exercises) * 2)) * 100
        
        result_text = f"""
🎓 ENTRENAMIENTO COMPLETADO!

📊 Ejercicios: {self.current_exercise}/100
✅ Puntuación: {self.score}/{(len(self.all_exercises) * 2)}
📈 Acierto: {accuracy:.1f}%
⏱️ Tiempo: {minutes:02d}:{seconds:02d}
💡 Pistas: {self.hints_used}
🔗 Estructuras: {len(self.mastered_structures)}

"""
        if accuracy >= 90:
            result_text += "🏆 ¡EXCELENTE! Dominas las preguntas en inglés"
        elif accuracy >= 70:
            result_text += "👍 ¡MUY BIEN! Buen dominio"
        elif accuracy >= 50:
            result_text += "📚 ¡BIEN! Sigue practicando"
        else:
            result_text += "💪 ¡Ánimo! La práctica es clave"
        
        # Crear modal de resultados
        result_modal = ModalView(size_hint=(0.8, 0.6))
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        layout.add_widget(Label(
            text='[b]🏆 Resultados Finales[/b]',
            markup=True,
            font_size=sp(22)
        ))
        
        result_label = Label(
            text=result_text,
            font_size=sp(16),
            text_size=(None, None)
        )
        layout.add_widget(result_label)
        
        btn_layout = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(10))
        
        restart_btn = Button(text='Reiniciar', background_color=get_color_from_hex('#27AE60'))
        restart_btn.bind(on_press=lambda x: self.restart_training(result_modal))
        btn_layout.add_widget(restart_btn)
        
        close_btn = Button(text='Salir', background_color=get_color_from_hex('#E74C3C'))
        close_btn.bind(on_press=self.stop)
        btn_layout.add_widget(close_btn)
        
        layout.add_widget(btn_layout)
        result_modal.add_widget(layout)
        result_modal.open()
    
    def restart_training(self, modal):
        modal.dismiss()
        self.current_exercise = 0
        self.score = 0
        self.hints_used = 0
        self.mastered_structures.clear()
        self.start_time = datetime.now()
        random.shuffle(self.all_exercises)
        self.load_exercise()
    
    def on_stop(self):
        # Cancelar el evento del reloj cuando la app se cierra
        if self.clock_event:
            self.clock_event.cancel()

if __name__ == '__main__':
    EnglishQuestionsApp().run()
