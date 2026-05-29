from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
from kivy.properties import (NumericProperty, StringProperty, 
                           ListProperty, BooleanProperty)
from kivy.metrics import dp, sp
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

import random
from datetime import datetime

# Diccionarios bilingües completos
TEXTS = {
    'es': {
        'app_title': '🌍 Entrenador de Inglés para Hispanohablantes',
        'exercise': 'Ejercicio',
        'of': 'de',
        'score': 'Puntuación',
        'time': 'Tiempo',
        'your_answer': 'Tu respuesta en inglés',
        'submit': '✅ Verificar',
        'hint': '💡 Pista',
        'skip': '⏭️ Saltar',
        'statistics': '📊 Estadísticas',
        'language': 'Idioma',
        'spanish': 'Español',
        'english': 'English',
        'correct': '¡Correcto!',
        'incorrect': 'Incorrecto',
        'complete_exercise': 'Ejercicio completado',
        'final_results': 'Resultados Finales',
        'restart': '🔄 Reiniciar',
        'exit': '🚪 Salir',
        'hint_used': 'Pista utilizada',
        'structures_mastered': 'Estructuras dominadas',
        'accuracy': 'Precisión',
        'spanish_sentence': 'Oración en español',
        'english_translation': 'Traducción al inglés',
        'grammar_explanation': 'Explicación gramatical',
        'common_mistake': 'Error común de hispanohablantes',
        'practice_tip': 'Consejo de práctica',
        'next_exercise': 'Siguiente ejercicio',
        'well_done': '¡Bien hecho!',
        'try_again': 'Intenta nuevamente',
        'exercise_progress': 'Progreso del ejercicio',
        'time_elapsed': 'Tiempo transcurrido',
        'hints_used': 'Pistas utilizadas',
        'mastered': 'Dominadas',
        'start_practice': 'Comenzar práctica',
        'continue_learning': 'Continuar aprendiendo'
    },
    'en': {
        'app_title': '🌍 English Trainer for Spanish Speakers',
        'exercise': 'Exercise',
        'of': 'of',
        'score': 'Score',
        'time': 'Time',
        'your_answer': 'Your answer in English',
        'submit': '✅ Check',
        'hint': '💡 Hint',
        'skip': '⏭️ Skip',
        'statistics': '📊 Statistics',
        'language': 'Language',
        'spanish': 'Español',
        'english': 'English',
        'correct': 'Correct!',
        'incorrect': 'Incorrect',
        'complete_exercise': 'Exercise completed',
        'final_results': 'Final Results',
        'restart': '🔄 Restart',
        'exit': '🚪 Exit',
        'hint_used': 'Hint used',
        'structures_mastered': 'Structures mastered',
        'accuracy': 'Accuracy',
        'spanish_sentence': 'Sentence in Spanish',
        'english_translation': 'Translation to English',
        'grammar_explanation': 'Grammar explanation',
        'common_mistake': 'Common mistake for Spanish speakers',
        'practice_tip': 'Practice tip',
        'next_exercise': 'Next exercise',
        'well_done': 'Well done!',
        'try_again': 'Try again',
        'exercise_progress': 'Exercise progress',
        'time_elapsed': 'Time elapsed',
        'hints_used': 'Hints used',
        'mastered': 'Mastered',
        'start_practice': 'Start practice',
        'continue_learning': 'Continue learning'
    }
}

# Paleta de colores bilingüe natural
COLORS = {
    'forest_dark': '#2D5A27',
    'forest_medium': '#4A7C59', 
    'forest_light': '#8FB996',
    'sky_dark': '#1E3A5F',
    'sky_medium': '#3A6EA5',
    'sky_light': '#87CEEB',
    'sunset_dark': '#E2725B',
    'sunset_medium': '#F4A261',
    'sunset_light': '#F9C74F',
    'water_dark': '#1A535C',
    'water_medium': '#4ECDC4',
    'water_light': '#A8DADC',
    'leaf_dark': '#386641',
    'leaf_medium': '#6A994E',
    'leaf_light': '#A7C957',
    'background_light': '#F8F9FA',
    'background_medium': '#E9ECEF',
    'text_dark': '#2B2D42',
    'text_medium': '#495057',
    'text_light': '#F8F9FA',
    'success_green': '#27AE60',
    'warning_orange': '#F39C12',
    'error_red': '#E74C3C',
    'info_blue': '#3498DB'
}

class BilingualExercise:
    def __init__(self, exercise_type, instruction_es, instruction_en, 
                 spanish_sentence, correct_answer, hint_es, hint_en, 
                 difficulty, grammar_explanation_es, grammar_explanation_en,
                 common_mistake_es, common_mistake_en):
        self.type = exercise_type
        self.instruction_es = instruction_es
        self.instruction_en = instruction_en
        self.spanish_sentence = spanish_sentence
        self.correct_answer = correct_answer
        self.hint_es = hint_es
        self.hint_en = hint_en
        self.difficulty = difficulty
        self.grammar_explanation_es = grammar_explanation_es
        self.grammar_explanation_en = grammar_explanation_en
        self.common_mistake_es = common_mistake_es
        self.common_mistake_en = common_mistake_en

class BilingualExerciseWidget(BoxLayout):
    def __init__(self, exercise, current_language, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(15)
        self.current_language = current_language
        
        # Fondo natural
        with self.canvas.before:
            Color(rgb=get_color_from_hex(COLORS['background_light']))
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        self.build_exercise_widget(exercise)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def build_exercise_widget(self, exercise):
        # Tipo y dificultad
        type_layout = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(10))
        
        # Icono según tipo de ejercicio
        type_icon = self.get_exercise_icon(exercise.type)
        
        type_layout.add_widget(Label(
            text=f'[b]{type_icon} {exercise.type}[/b]',
            markup=True,
            font_size=sp(16),
            color=get_color_from_hex(COLORS['forest_dark']),
            size_hint_x=0.6
        ))
        
        # Color de dificultad
        difficulty_color = self.get_difficulty_color(exercise.difficulty)
        difficulty_text = exercise.difficulty.upper() if self.current_language == 'en' else self.translate_difficulty(exercise.difficulty)
        
        type_layout.add_widget(Label(
            text=f'[{difficulty_text}]',
            font_size=sp(14),
            color=get_color_from_hex(difficulty_color),
            size_hint_x=0.4
        ))
        self.add_widget(type_layout)
        
        # Instrucción bilingüe
        instruction = exercise.instruction_en if self.current_language == 'en' else exercise.instruction_es
        self.add_widget(Label(
            text=instruction,
            font_size=sp(15),
            color=get_color_from_hex(COLORS['text_dark']),
            size_hint_y=None,
            height=dp(50),
            text_size=(None, None)
        ))
        
        # Oración en español (siempre visible para referencia)
        spanish_label = Label(
            text=f'[b]🇪🇸 {TEXTS[self.current_language]["spanish_sentence"]}:[/b]\n[i]"{exercise.spanish_sentence}"[/i]',
            markup=True,
            font_size=sp(14),
            color=get_color_from_hex(COLORS['water_dark']),
            size_hint_y=None,
            height=dp(60),
            text_size=(None, None)
        )
        self.add_widget(spanish_label)
    
    def get_exercise_icon(self, exercise_type):
        icons = {
            'to be': '🔤',
            'do/does': '🔄', 
            'wh- questions': '❓',
            'question tags': '🏷️',
            'indirect questions': '🗣️',
            'mixed questions': '🌀'
        }
        for key, icon in icons.items():
            if key in exercise_type.lower():
                return icon
        return '📝'
    
    def get_difficulty_color(self, difficulty):
        colors = {
            'básico': COLORS['leaf_medium'],
            'intermedio': COLORS['sunset_medium'],
            'avanzado': COLORS['sky_medium'],
            'basic': COLORS['leaf_medium'],
            'intermediate': COLORS['sunset_medium'],
            'advanced': COLORS['sky_medium']
        }
        return colors.get(difficulty, COLORS['text_medium'])
    
    def translate_difficulty(self, difficulty):
        translations = {
            'básico': 'basic',
            'intermedio': 'intermediate', 
            'avanzado': 'advanced'
        }
        return translations.get(difficulty, difficulty)

class BilingualEnglishTrainerApp(App):
    current_language = StringProperty('es')  # 'es' o 'en'
    current_exercise = NumericProperty(0)
    score = NumericProperty(0)
    progress = NumericProperty(0)
    time_elapsed = StringProperty("00:00")
    total_exercises = NumericProperty(100)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exercises = []
        self.all_exercises = []
        self.start_time = None
        self.mastered_structures = set()
        self.hints_used = 0
        self.clock_event = None
        
    def build(self):
        # Configuración de la ventana
        Window.clearcolor = get_color_from_hex(COLORS['background_light'])
        self.title = TEXTS[self.current_language]['app_title']
        
        # Inicializar ejercicios bilingües
        self.initialize_bilingual_exercises()
        self.all_exercises = self.complete_100_exercises()
        
        # Construir interfaz
        return self.build_interface()
    
    def build_interface(self):
        main_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        
        # Header con controles de idioma
        main_layout.add_widget(self.build_header())
        
        # Área de progreso
        main_layout.add_widget(self.build_progress_area())
        
        # Área de ejercicio
        main_layout.add_widget(self.build_exercise_area())
        
        # Área de respuesta
        main_layout.add_widget(self.build_answer_area())
        
        # Controles
        main_layout.add_widget(self.build_controls())
        
        # Iniciar timer
        self.start_time = datetime.now()
        self.clock_event = Clock.schedule_interval(self.update_time, 1)
        
        # Cargar primer ejercicio
        Clock.schedule_once(lambda dt: self.load_exercise(), 0.1)
        
        return main_layout
    
    def build_header(self):
        header = BoxLayout(size_hint_y=None, height=dp(80), padding=dp(10))
        
        with header.canvas.before:
            Color(rgb=get_color_from_hex(COLORS['forest_dark']))
            header.rect = Rectangle(pos=header.pos, size=header.size)
        header.bind(pos=self.update_header_rect, size=self.update_header_rect)
        
        # Título
        title_label = Label(
            text=f'[b]{TEXTS[self.current_language]["app_title"]}[/b]',
            markup=True,
            font_size=sp(18),
            color=get_color_from_hex(COLORS['text_light']),
            size_hint_x=0.7
        )
        header.add_widget(title_label)
        
        # Selector de idioma
        language_layout = BoxLayout(size_hint_x=0.3, spacing=dp(5))
        
        language_label = Label(
            text=f'🌐 {TEXTS[self.current_language]["language"]}:',
            color=get_color_from_hex(COLORS['text_light']),
            size_hint_x=0.5
        )
        language_layout.add_widget(language_label)
        
        self.language_spinner = Spinner(
            text='Español' if self.current_language == 'es' else 'English',
            values=('Español', 'English'),
            size_hint_x=0.5,
            background_color=get_color_from_hex(COLORS['sky_medium'])
        )
        self.language_spinner.bind(text=self.on_language_change)
        language_layout.add_widget(self.language_spinner)
        
        header.add_widget(language_layout)
        return header
    
    def update_header_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
    
    def build_progress_area(self):
        progress_layout = BoxLayout(size_hint_y=None, height=dp(80), padding=dp(10))
        
        # Barra de progreso y estadísticas
        stats_grid = GridLayout(cols=2, rows=2, spacing=dp(5))
        
        # Barra de progreso
        self.progress_bar = ProgressBar(
            max=100,
            size_hint_y=None,
            height=dp(20)
        )
        stats_grid.add_widget(Label(
            text=f'📈 {TEXTS[self.current_language]["exercise_progress"]}:',
            color=get_color_from_hex(COLORS['text_dark'])
        ))
        stats_grid.add_widget(self.progress_bar)
        
        # Estadísticas en tiempo real
        self.progress_label = Label(
            text=f'{TEXTS[self.current_language]["exercise"]}: 0/{self.total_exercises}',
            color=get_color_from_hex(COLORS['text_dark'])
        )
        stats_grid.add_widget(self.progress_label)
        
        self.score_label = Label(
            text=f'⭐ {TEXTS[self.current_language]["score"]}: 0',
            color=get_color_from_hex(COLORS['text_dark'])
        )
        stats_grid.add_widget(self.score_label)
        
        progress_layout.add_widget(stats_grid)
        return progress_layout
    
    def build_exercise_area(self):
        self.exercise_scroll = ScrollView(size_hint_y=0.4)
        self.exercise_layout = BoxLayout(
            orientation='vertical', 
            size_hint_y=None,
            padding=dp(15),
            spacing=dp(10)
        )
        self.exercise_layout.bind(minimum_height=self.exercise_layout.setter('height'))
        self.exercise_scroll.add_widget(self.exercise_layout)
        return self.exercise_scroll
    
    def build_answer_area(self):
        answer_layout = BoxLayout(orientation='vertical', size_hint_y=0.3, 
                                padding=dp(10), spacing=dp(5))
        
        # Label para respuesta
        answer_layout.add_widget(Label(
            text=f'✏️ {TEXTS[self.current_language]["your_answer"]}:',
            font_size=sp(16),
            color=get_color_from_hex(COLORS['text_dark']),
            size_hint_y=None,
            height=dp(30)
        ))
        
        # Campo de texto para respuesta
        self.answer_input = TextInput(
            multiline=True,
            size_hint_y=0.6,
            font_size=sp(16),
            background_color=get_color_from_hex(COLORS['background_medium']),
            foreground_color=get_color_from_hex(COLORS['text_dark']),
            hint_text=f'Escribe tu respuesta en inglés aquí...' if self.current_language == 'es' else 'Write your answer in English here...'
        )
        answer_layout.add_widget(self.answer_input)
        
        # Área de feedback bilingüe
        self.feedback_label = Label(
            text='',
            font_size=sp(14),
            size_hint_y=0.4,
            text_size=(None, None),
            color=get_color_from_hex(COLORS['text_dark'])
        )
        answer_layout.add_widget(self.feedback_label)
        
        return answer_layout
    
    def build_controls(self):
        controls_layout = GridLayout(cols=4, size_hint_y=None, height=dp(70), 
                                   spacing=dp(10), padding=dp(10))
        
        # Botones con iconos y colores temáticos
        buttons_info = [
            ('✅', 'submit', COLORS['leaf_medium'], self.check_answer),
            ('💡', 'hint', COLORS['sunset_medium'], self.show_hint),
            ('⏭️', 'skip', COLORS['sky_medium'], self.skip_exercise),
            ('📊', 'statistics', COLORS['water_medium'], self.show_statistics)
        ]
        
        for icon, text_key, color, callback in buttons_info:
            btn = Button(
                text=f'{icon} {TEXTS[self.current_language][text_key]}',
                background_color=get_color_from_hex(color),
                color=get_color_from_hex(COLORS['text_light']),
                font_size=sp(14)
            )
            btn.bind(on_press=callback)
            controls_layout.add_widget(btn)
        
        return controls_layout
    
    def initialize_bilingual_exercises(self):
        """Ejercicios específicamente diseñados para dificultades de hispanohablantes"""
        self.exercises = [
            BilingualExercise(
                "Preguntas con 'to be' / 'to be' Questions",
                "Convierte la afirmación en pregunta:",
                "Turn the statement into a question:",
                "Él es profesor",
                "Is he a teacher?",
                "Recuerda invertir el orden: Verbo + Sujeto",
                "Remember to invert the order: Verb + Subject",
                "básico/basic",
                "En español usamos entonación, en inglés invertimos el verbo 'to be'",
                "In Spanish we use intonation, in English we invert the verb 'to be'",
                "Decir 'He is teacher?' en lugar de 'Is he a teacher?'",
                "Saying 'He is teacher?' instead of 'Is he a teacher?'"
            ),
            BilingualExercise(
                "Preguntas con Do/Does / Do/Does Questions", 
                "Convierte en pregunta usando Do/Does:",
                "Turn into a question using Do/Does:",
                "Ella trabaja aquí",
                "Does she work here?",
                "Para he/she/it usa DOES + verbo en forma base",
                "For he/she/it use DOES + base verb form",
                "básico/basic",
                "Los hispanohablantes olvidan usar 'do/does' en preguntas",
                "Spanish speakers forget to use 'do/does' in questions",
                "Decir 'Work she here?' en lugar de 'Does she work here?'",
                "Saying 'Work she here?' instead of 'Does she work here?'"
            ),
            # ... más ejercicios bilingües ...
        ]
    
    def complete_100_exercises(self):
        """Completar hasta 100 ejercicios con variaciones"""
        completed = []
        for i in range(25):  # 25 variaciones de 4 ejercicios base
            for exercise in self.exercises:
                new_exercise = BilingualExercise(
                    exercise.type,
                    exercise.instruction_es,
                    exercise.instruction_en,
                    self.vary_sentence(exercise.spanish_sentence, i),
                    self.vary_answer(exercise.correct_answer, i),
                    exercise.hint_es,
                    exercise.hint_en,
                    exercise.difficulty,
                    exercise.grammar_explanation_es,
                    exercise.grammar_explanation_en,
                    exercise.common_mistake_es,
                    exercise.common_mistake_en
                )
                completed.append(new_exercise)
        
        random.shuffle(completed)
        return completed[:100]
    
    def vary_sentence(self, sentence, variation_index):
        """Crear variaciones de oraciones en español"""
        variations = [
            {"profesor": "médico", "trabaja": "estudia", "aquí": "allí"},
            {"es": "era", "trabaja": "enseña", "profesor": "ingeniero"},
            # ... más variaciones ...
        ]
        varied = sentence
        variation = variations[variation_index % len(variations)]
        for original, replacement in variation.items():
            varied = varied.replace(original, replacement)
        return varied
    
    def vary_answer(self, answer, variation_index):
        """Crear variaciones de respuestas en inglés"""
        variations = [
            {"teacher": "doctor", "work": "study", "here": "there"},
            {"is": "was", "work": "teach", "teacher": "engineer"},
            # ... más variaciones ...
        ]
        varied = answer
        variation = variations[variation_index % len(variations)]
        for original, replacement in variation.items():
            varied = varied.replace(original, replacement)
        return varied
    
    def load_exercise(self):
        if self.current_exercise >= len(self.all_exercises):
            self.show_final_results()
            return
        
        # Limpiar área de ejercicio
        self.exercise_layout.clear_widgets()
        
        exercise = self.all_exercises[self.current_exercise]
        exercise_widget = BilingualExerciseWidget(exercise, self.current_language)
        self.exercise_layout.add_widget(exercise_widget)
        
        # Limpiar campos
        self.answer_input.text = ''
        self.feedback_label.text = ''
        
        # Actualizar progreso
        self.update_progress()
    
    def update_progress(self):
        self.progress = (self.current_exercise / len(self.all_exercises)) * 100
        self.progress_bar.value = self.progress
        
        exercise_text = TEXTS[self.current_language]['exercise']
        of_text = TEXTS[self.current_language]['of']
        self.progress_label.text = f'{exercise_text}: {self.current_exercise + 1}{of_text}{len(self.all_exercises)}'
        
        score_text = TEXTS[self.current_language]['score']
        self.score_label.text = f'⭐ {score_text}: {self.score}'
    
    def update_time(self, dt):
        if self.start_time:
            elapsed = datetime.now() - self.start_time
            minutes = elapsed.seconds // 60
            seconds = elapsed.seconds % 60
            time_text = TEXTS[self.current_language]['time']
            self.time_elapsed = f'{time_text}: {minutes:02d}:{seconds:02d}'
    
    def check_answer(self, instance):
        user_answer = self.answer_input.text.strip()
        if not user_answer:
            warning = TEXTS[self.current_language]['try_again']
            self.feedback_label.text = f'[color={COLORS["error_red"]}]⚠️ {warning}[/color]'
            return
        
        exercise = self.all_exercises[self.current_exercise]
        is_correct, feedback_type = self.verify_answer(user_answer, exercise.correct_answer)
        
        if is_correct:
            correct_text = TEXTS[self.current_language]['correct']
            self.feedback_label.text = f'[color={COLORS["success_green"]}]✅ {correct_text}![/color]'
            self.score += 2 if feedback_type == "exact" else 1
            self.mastered_structures.add(exercise.type)
            
            # Mostrar explicación gramatical bilingüe
            Clock.schedule_once(lambda dt: self.show_grammar_explanation(exercise), 1.5)
        else:
            incorrect_text = TEXTS[self.current_language]['incorrect']
            self.feedback_label.text = f'[color={COLORS["error_red"]}]❌ {incorrect_text}[/color]'
    
    def verify_answer(self, user_answer, correct_answer):
        """Verificación flexible de respuestas"""
        def normalize(text):
            return text.strip().lower().replace("'", "").replace('"', '').replace("  ", " ")
        
        user_norm = normalize(user_answer)
        correct_norm = normalize(correct_answer)
        
        if user_norm == correct_norm:
            return True, "exact"
        
        # Verificación semántica para respuestas aproximadas
        user_words = set(user_norm.split())
        correct_words = set(correct_norm.split())
        
        similarity = len(user_words.intersection(correct_words)) / len(correct_words)
        return similarity >= 0.8, "approximate"
    
    def show_grammar_explanation(self, exercise):
        """Mostrar explicación gramatical bilingüe"""
        explanation = (exercise.grammar_explanation_en if self.current_language == 'en' 
                      else exercise.grammar_explanation_es)
        common_mistake = (exercise.common_mistake_en if self.current_language == 'en' 
                         else exercise.common_mistake_es)
        
        feedback_text = f"""
[color={COLORS["success_green"]}]✅ {TEXTS[self.current_language]["well_done"]}![/color]

[color={COLORS["info_blue"]}]📖 {TEXTS[self.current_language]["grammar_explanation"]}:[/color]
{explanation}

[color={COLORS["warning_orange"]}]💡 {TEXTS[self.current_language]["common_mistake"]}:[/color]
{common_mistake}

[color={COLORS["forest_medium"]}]🌿 {TEXTS[self.current_language]["practice_tip"]}[/color]
"""
        self.feedback_label.text = feedback_text
        
        # Siguiente ejercicio después de 4 segundos
        Clock.schedule_once(lambda dt: self.next_exercise(), 4)
    
    def show_hint(self, instance):
        exercise = self.all_exercises[self.current_exercise]
        self.hints_used += 1
        hint = exercise.hint_en if self.current_language == 'en' else exercise.hint_es
        hint_text = TEXTS[self.current_language]['hint_used']
        self.feedback_label.text = f'[color={COLORS["warning_orange"]}]💡 {hint_text}: {hint}[/color]'
    
    def skip_exercise(self, instance):
        self.next_exercise()
    
    def next_exercise(self):
        self.current_exercise += 1
        if self.current_exercise < len(self.all_exercises):
            self.load_exercise()
        else:
            self.show_final_results()
    
    def show_statistics(self, instance):
        """Mostrar estadísticas bilingües"""
        stats_modal = ModalView(size_hint=(0.8, 0.6), auto_dismiss=True)
        
        stats_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Título
        title = Label(
            text=f'[b]📊 {TEXTS[self.current_language]["statistics"]}[/b]',
            markup=True,
            font_size=sp(20),
            color=get_color_from_hex(COLORS['forest_dark']),
            size_hint_y=None,
            height=dp(40)
        )
        stats_layout.add_widget(title)
        
        # Estadísticas
        stats_text = f"""
🌿 {TEXTS[self.current_language]['exercise']}: {self.current_exercise}/{self.total_exercises}
⭐ {TEXTS[self.current_language]['score']}: {self.score}
📈 {TEXTS[self.current_language]['accuracy']}: {(self.score/(self.current_exercise*2)*100):.1f}%
⏱️ {TEXTS[self.current_language]['time_elapsed']}: {self.time_elapsed.split(": ")[1]}
💡 {TEXTS[self.current_language]['hints_used']}: {self.hints_used}
🌱 {TEXTS[self.current_language]['structures_mastered']}: {len(self.mastered_structures)}
"""
        stats_label = Label(
            text=stats_text,
            font_size=sp(16),
            text_size=(None, None)
        )
        stats_layout.add_widget(stats_label)
        
        # Botón cerrar
        close_btn = Button(
            text=TEXTS[self.current_language]['continue_learning'],
            size_hint_y=None,
            height=dp(50),
            background_color=get_color_from_hex(COLORS['sky_medium'])
        )
        close_btn.bind(on_press=stats_modal.dismiss)
        stats_layout.add_widget(close_btn)
        
        stats_modal.add_widget(stats_layout)
        stats_modal.open()
    
    def show_final_results(self):
        """Mostrar resultados finales bilingües"""
        total_time = datetime.now() - self.start_time
        minutes = total_time.seconds // 60
        seconds = total_time.seconds % 60
        accuracy = (self.score / (len(self.all_exercises) * 2)) * 100
        
        # Texto de resultados según idioma
        if self.current_language == 'en':
            result_text = self.get_english_results(accuracy, minutes, seconds)
        else:
            result_text = self.get_spanish_results(accuracy, minutes, seconds)
        
        # Modal de resultados
        result_modal = ModalView(size_hint=(0.85, 0.7))
        result_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        result_layout.add_widget(Label(
            text=f'[b]🎓 {TEXTS[self.current_language]["final_results"]}[/b]',
            markup=True,
            font_size=sp(22),
            size_hint_y=None,
            height=dp(50)
        ))
        
        result_label = Label(
            text=result_text,
            font_size=sp(16),
            text_size=(None, None)
        )
        result_layout.add_widget(result_label)
        
        # Botones
        btn_layout = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(10))
        
        restart_btn = Button(
            text=TEXTS[self.current_language]['restart'],
            background_color=get_color_from_hex(COLORS['leaf_medium'])
        )
        restart_btn.bind(on_press=lambda x: self.restart_training(result_modal))
        btn_layout.add_widget(restart_btn)
        
        exit_btn = Button(
            text=TEXTS[self.current_language]['exit'],
            background_color=get_color_from_hex(COLORS['sunset_medium'])
        )
        exit_btn.bind(on_press=self.stop)
        btn_layout.add_widget(exit_btn)
        
        result_layout.add_widget(btn_layout)
        result_modal.add_widget(result_layout)
        result_modal.open()
    
    def get_spanish_results(self, accuracy, minutes, seconds):
        """Resultados en español"""
        if accuracy >= 90:
            evaluation = "🏔️ ¡EXCELENTE! Dominas las preguntas en inglés"
        elif accuracy >= 70:
            evaluation = "🌅 ¡MUY BIEN! Buen dominio del inglés"
        elif accuracy >= 50:
            evaluation = "🌱 ¡BIEN! Sigue practicando"
        else:
            evaluation = "🌵 ¡Ánimo! La práctica constante es clave"
        
        return f"""
🌿 Ejercicios completados: {self.current_exercise}/100
⭐ Puntuación final: {self.score}/{(len(self.all_exercises) * 2)}
📈 Precisión: {accuracy:.1f}%
⏱️ Tiempo total: {minutes:02d}:{seconds:02d}
💡 Pistas utilizadas: {self.hints_used}
🌱 Estructuras dominadas: {len(self.mastered_structures)}

{evaluation}

💡 Consejo: Practica diariamente para mejorar tu fluidez.
"""
    
    def get_english_results(self, accuracy, minutes, seconds):
        """Results in English"""
        if accuracy >= 90:
            evaluation = "🏔️ EXCELLENT! You master English questions"
        elif accuracy >= 70:
            evaluation = "🌅 VERY GOOD! Strong English skills"
        elif accuracy >= 50:
            evaluation = "🌱 GOOD! Keep practicing regularly"
        else:
            evaluation = "🌵 Keep going! Consistent practice is key"
        
        return f"""
🌿 Exercises completed: {self.current_exercise}/100
⭐ Final score: {self.score}/{(len(self.all_exercises) * 2)}
📈 Accuracy: {accuracy:.1f}%
⏱️ Total time: {minutes:02d}:{seconds:02d}
💡 Hints used: {self.hints_used}
🌱 Structures mastered: {len(self.mastered_structures)}

{evaluation}

💡 Tip: Practice daily to improve your fluency.
"""
    
    def on_language_change(self, spinner, text):
        """Cambiar idioma de la interfaz"""
        new_lang = 'es' if text == 'Español' else 'en'
        if new_lang != self.current_language:
            self.current_language = new_lang
            self.update_interface_language()
    
    def update_interface_language(self):
        """Actualizar toda la interfaz al nuevo idioma"""
        self.title = TEXTS[self.current_language]['app_title']
        
        # Reconstruir la interfaz
        self.root.clear_widgets()
        new_interface = self.build_interface()
        self.root.add_widget(new_interface)
        
        # Recargar ejercicio actual con nuevo idioma
        self.load_exercise()
    
    def restart_training(self, modal):
        """Reiniciar el entrenamiento"""
        modal.dismiss()
        self.current_exercise = 0
        self.score = 0
        self.hints_used = 0
        self.mastered_structures.clear()
        self.start_time = datetime.now()
        random.shuffle(self.all_exercises)
        self.load_exercise()
    
    def on_stop(self):
        if self.clock_event:
            self.clock_event.cancel()

if __name__ == '__main__':
    BilingualEnglishTrainerApp().run()
