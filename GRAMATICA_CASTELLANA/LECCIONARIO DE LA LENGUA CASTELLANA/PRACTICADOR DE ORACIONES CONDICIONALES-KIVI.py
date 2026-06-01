from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ListProperty, BooleanProperty
from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
import random
import textwrap

# Configuración de colores
BACKGROUND = (0.1, 0.1, 0.2, 1)
WHITE = (1, 1, 1, 1)
BLUE = (0.2, 0.6, 1, 1)
GREEN = (0.2, 0.8, 0.2, 1)
RED = (1, 0.4, 0.4, 1)
YELLOW = (1, 1, 0.4, 1)
PURPLE = (0.7, 0.3, 0.9, 1)
DARK_BLUE = (0.1, 0.3, 0.6, 1)
LIGHT_BLUE = (0.4, 0.8, 1, 1)

# Base de datos de ejemplos
EJEMPLOS = {
    "Reales": [
        {"oracion": "Si llueve, nos quedamos en casa.", "explicacion": "Condición presente real. Consecuencia inmediata."},
        {"oracion": "Si tienes hambre, come algo.", "explicacion": "Condición presente. Consecuencia en imperativo."},
        {"oracion": "Si terminas temprano, llámame.", "explicacion": "Condición futura posible. Consecuencia en imperativo."},
        {"oracion": "Si estudias, apruebas el examen.", "explicacion": "Condición general/real. Relación causa-efecto."},
        {"oracion": "Si quieres venir, debes avisar.", "explicacion": "Condición posible. Consecuencia con verbo modal."}
    ],
    "Potenciales": [
        {"oracion": "Si tuviera dinero, compraría una casa.", "explicacion": "Condición improbable en presente. Deseo/consecuencia hipotética."},
        {"oracion": "Si pudiera volar, viajaría por todo el mundo.", "explicacion": "Condición imposible física. Consecuencia imaginaria."},
        {"oracion": "Si tuviese más tiempo, te ayudaría.", "explicacion": "Condición improbable. Oferta cortés hipotética."},
        {"oracion": "Si lloviera mañana, cancelaríamos el picnic.", "explicacion": "Condición meteorológica futura improbable."},
        {"oracion": "Si fuera tú, no iría a esa reunión.", "explicacion": "Consejo hipotético con improbabilidad de ser el otro."}
    ],
    "Irreales": [
        {"oracion": "Si hubieras estudiado, habrías aprobado el examen.", "explicacion": "Condición pasada no cumplida. Consecuencia lógica fallida."},
        {"oracion": "Si hubiese sabido que venías, te habría esperado.", "explicacion": "Condición pasada no conocida. Consecuencia deseada no realizada."},
        {"oracion": "Si hubiéramos salido antes, no habríamos perdido el tren.", "explicacion": "Acción pasada no realizada. Consecuencia negativa evitable."},
        {"oracion": "Si hubieses llamado, habría ido a recogerte.", "explicacion": "Acción pasada no realizada. Oferta de ayuda no materializada."},
        {"oracion": "Si no hubiera llovido, la boda habría sido en el jardín.", "explicacion": "Condición meteorológica pasada no deseada. Plan original frustrado."}
    ]
}

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.name = 'menu'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Título
        title = Label(text='Constructor de Oraciones Condicionales', 
                     font_size=32, bold=True, color=WHITE)
        subtitle = Label(text='Aprende español con la RAE', 
                        font_size=24, color=LIGHT_BLUE)
        
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(Label(size_hint_y=0.1))  # Espacio
        
        # Botones de juegos
        games = [
            ("Juego 1: Construye la Oración", 'game1', BLUE),
            ("Juego 2: Clasifica el Tipo", 'game2', GREEN),
            ("Juego 3: Completa los Huecos", 'game3', YELLOW),
            ("Juego 4: Ordena las Palabras", 'game4', PURPLE),
            ("Juego 5: Memoria Condicional", 'game5', RED)
        ]
        
        for text, screen_name, color in games:
            btn = Button(text=text, background_color=color, 
                         size_hint_y=0.12, font_size=20, bold=True)
            btn.bind(on_press=lambda _, sn=screen_name: self.switch_to(sn))
            layout.add_widget(btn)
        
        # Puntuación
        self.score_label = Label(text='Puntuación: 0 | Nivel: 1 | Racha: 0', 
                               font_size=18, color=WHITE, size_hint_y=0.1)
        layout.add_widget(self.score_label)
        
        self.add_widget(layout)
    
    def switch_to(self, screen_name):
        self.manager.current = screen_name
    
    def update_score(self, score, level, streak):
        self.score_label.text = f'Puntuación: {score} | Nivel: {level} | Racha: {streak}'

class BaseGameScreen(Screen):
    score = NumericProperty(0)
    level = NumericProperty(1)
    streak = NumericProperty(0)
    message = StringProperty('')
    message_color = ListProperty(WHITE)
    
    def __init__(self, **kwargs):
        super(BaseGameScreen, self).__init__(**kwargs)
        self.game_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.add_widget(self.game_layout)
        
        # Botones de navegación
        nav_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        self.back_btn = Button(text='Menú', background_color=DARK_BLUE, size_hint_x=0.3)
        self.back_btn.bind(on_press=self.go_to_menu)
        self.next_btn = Button(text='Siguiente', background_color=PURPLE, size_hint_x=0.7)
        self.next_btn.bind(on_press=self.next_example)
        nav_layout.add_widget(self.back_btn)
        nav_layout.add_widget(self.next_btn)
        self.game_layout.add_widget(nav_layout)
        
        # Contenido del juego
        self.content_layout = BoxLayout(orientation='vertical', padding=10, spacing=15)
        self.game_layout.add_widget(self.content_layout)
        
        # Mensaje
        self.msg_label = Label(text=self.message, color=self.message_color, size_hint_y=0.1)
        self.game_layout.add_widget(self.msg_label)
        
        self.bind(message=self.update_message)
        self.bind(message_color=self.update_message_color)
        
        self.current_example = self.get_random_example()
    
    def update_message(self, instance, value):
        self.msg_label.text = value
    
    def update_message_color(self, instance, value):
        self.msg_label.color = value
    
    def show_message(self, text, color, duration=3):
        self.message = text
        self.message_color = color
        Clock.schedule_once(self.clear_message, duration)
    
    def clear_message(self, dt):
        self.message = ''
    
    def get_random_example(self):
        category = random.choice(list(EJEMPLOS.keys()))
        return random.choice(EJEMPLOS[category])
    
    def next_example(self, instance):
        self.current_example = self.get_random_example()
        self.reset_game()
    
    def go_to_menu(self, instance):
        self.manager.get_screen('menu').update_score(self.score, self.level, self.streak)
        self.manager.current = 'menu'
    
    def update_score(self, correct):
        if correct:
            self.score += 10 * self.level
            self.streak += 1
            if self.streak % 5 == 0:
                self.level += 1
            return True
        else:
            self.streak = 0
            return False
    
    def reset_game(self):
        # Método que será implementado en cada juego específico
        pass

class Game1Screen(BaseGameScreen):
    def __init__(self, **kwargs):
        super(Game1Screen, self).__init__(**kwargs)
        self.name = 'game1'
        self.build_ui()
    
    def build_ui(self):
        # Limpiar layout
        self.content_layout.clear_widgets()
        
        # Título
        title = Label(text='Juego 1: Construye la Oración', 
                     font_size=28, bold=True, color=BLUE)
        self.content_layout.add_widget(title)
        
        # Instrucciones
        instructions = Label(text='Escribe una oración condicional similar a:', 
                            font_size=20, color=WHITE)
        self.content_layout.add_widget(instructions)
        
        # Ejemplo
        self.example_label = Label(text=self.current_example['oracion'], 
                                  font_size=20, color=YELLOW)
        self.content_layout.add_widget(self.example_label)
        
        # Explicación
        self.expl_label = Label(text=self.current_example['explicacion'], 
                               font_size=16, color=LIGHT_BLUE)
        self.content_layout.add_widget(self.expl_label)
        
        # Entrada de usuario
        self.user_input = TextInput(multiline=False, size_hint_y=0.2, 
                                  font_size=20, background_color=(0.2, 0.2, 0.3, 1))
        self.content_layout.add_widget(self.user_input)
        
        # Botón de verificación
        self.check_btn = Button(text='Verificar', background_color=GREEN, size_hint_y=0.15)
        self.check_btn.bind(on_press=self.verify_sentence)
        self.content_layout.add_widget(self.check_btn)
        
        # Espacio
        self.content_layout.add_widget(Label(size_hint_y=0.1))
    
    def reset_game(self):
        self.build_ui()
    
    def verify_sentence(self, instance):
        user_text = self.user_input.text.strip()
        if 'si ' in user_text.lower() and ',' in user_text:
            correct = self.update_score(True)
            self.show_message('¡Correcto! Buena construcción condicional.', GREEN)
        else:
            correct = self.update_score(False)
            self.show_message('Recuerda usar "si" y una coma para separar condición y consecuencia', RED)

class Game2Screen(BaseGameScreen):
    def __init__(self, **kwargs):
        super(Game2Screen, self).__init__(**kwargs)
        self.name = 'game2'
        self.build_ui()
    
    def build_ui(self):
        # Limpiar layout
        self.content_layout.clear_widgets()
        
        # Título
        title = Label(text='Juego 2: Clasifica el Tipo', 
                     font_size=28, bold=True, color=GREEN)
        self.content_layout.add_widget(title)
        
        # Instrucciones
        instructions = Label(text='¿Qué tipo de oración condicional es la siguiente?', 
                            font_size=20, color=WHITE)
        self.content_layout.add_widget(instructions)
        
        # Ejemplo
        self.example_label = Label(text=self.current_example['oracion'], 
                                  font_size=20, color=YELLOW, size_hint_y=0.3)
        self.example_label.bind(size=self.example_label.setter('text_size'))
        self.example_label.halign = 'center'
        self.example_label.valign = 'middle'
        self.content_layout.add_widget(self.example_label)
        
        # Botones de categorías
        btn_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.6)
        
        real_btn = Button(text='Real (Condición posible)', background_color=BLUE)
        real_btn.bind(on_press=lambda x: self.check_category('Reales'))
        btn_layout.add_widget(real_btn)
        
        pot_btn = Button(text='Potencial (Condición improbable)', background_color=GREEN)
        pot_btn.bind(on_press=lambda x: self.check_category('Potenciales'))
        btn_layout.add_widget(pot_btn)
        
        irr_btn = Button(text='Irreal (Condición imposible)', background_color=RED)
        irr_btn.bind(on_press=lambda x: self.check_category('Irreales'))
        btn_layout.add_widget(irr_btn)
        
        self.content_layout.add_widget(btn_layout)
    
    def reset_game(self):
        self.build_ui()
    
    def check_category(self, selected_category):
        # Determinar la categoría correcta
        correct_category = None
        for cat, examples in EJEMPLOS.items():
            for ex in examples:
                if ex['oracion'] == self.current_example['oracion']:
                    correct_category = cat
                    break
            if correct_category:
                break
        
        if selected_category == correct_category:
            correct = self.update_score(True)
            self.show_message(f'¡Correcto! {self.current_example["explicacion"]}', GREEN)
        else:
            correct = self.update_score(False)
            self.show_message(f'Incorrecto. Es una oración {correct_category}', RED)

class Game3Screen(BaseGameScreen):
    def __init__(self, **kwargs):
        super(Game3Screen, self).__init__(**kwargs)
        self.name = 'game3'
        self.user_answers = []
        self.blank_widgets = []
        self.build_ui()
    
    def build_ui(self):
        # Limpiar layout
        self.content_layout.clear_widgets()
        self.user_answers = []
        self.blank_widgets = []
        
        # Título
        title = Label(text='Juego 3: Completa los Huecos', 
                     font_size=28, bold=True, color=YELLOW)
        self.content_layout.add_widget(title)
        
        # Instrucciones
        instructions = Label(text='Completa los espacios en blanco:', 
                            font_size=20, color=WHITE)
        self.content_layout.add_widget(instructions)
        
        # Preparar oración con huecos
        sentence = self.current_example['oracion']
        words = sentence.split()
        
        # Seleccionar palabras para ocultar
        num_blanks = min(4, max(2, len(words) // 3))
        blank_indices = random.sample(range(len(words)), num_blanks)
        blank_indices.sort()
        
        self.answers = []
        self.blanked_sentence = []
        
        for i, word in enumerate(words):
            if i in blank_indices:
                self.blanked_sentence.append('_____')
                self.answers.append(word.strip('.,;?!'))
            else:
                self.blanked_sentence.append(word)
        
        # Crear layout para la oración
        scroll_view = ScrollView(size_hint=(1, 0.5), do_scroll_x=True)
        sentence_layout = GridLayout(cols=len(self.blanked_sentence), spacing=10, 
                                    size_hint_x=None, height=100)
        sentence_layout.bind(minimum_width=sentence_layout.setter('width'))
        
        for i, part in enumerate(self.blanked_sentence):
            if part == '_____':
                # Crear entrada para el espacio en blanco
                blank_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=120)
                
                lbl = Label(text='_____', color=LIGHT_BLUE, size_hint_y=0.5)
                blank_layout.add_widget(lbl)
                
                text_input = TextInput(multiline=False, size_hint_y=0.5, 
                                      font_size=16, background_color=(0.2, 0.2, 0.3, 1))
                self.user_answers.append(text_input)
                self.blank_widgets.append(text_input)
                blank_layout.add_widget(text_input)
                
                sentence_layout.add_widget(blank_layout)
            else:
                lbl = Label(text=part, color=WHITE, size_hint_x=None, width=len(part)*15)
                sentence_layout.add_widget(lbl)
        
        scroll_view.add_widget(sentence_layout)
        self.content_layout.add_widget(scroll_view)
        
        # Botón de verificación
        self.check_btn = Button(text='Verificar', background_color=GREEN, size_hint_y=0.15)
        self.check_btn.bind(on_press=self.verify_answers)
        self.content_layout.add_widget(self.check_btn)
    
    def reset_game(self):
        self.build_ui()
    
    def verify_answers(self, instance):
        all_correct = True
        for i in range(len(self.answers)):
            user_answer = self.user_answers[i].text.strip().lower()
            correct_answer = self.answers[i].lower()
            
            if user_answer != correct_answer:
                all_correct = False
                self.blank_widgets[i].background_color = (1, 0.5, 0.5, 1)
            else:
                self.blank_widgets[i].background_color = (0.5, 1, 0.5, 1)
        
        if all_correct:
            correct = self.update_score(True)
            self.show_message('¡Correcto! ' + self.current_example['explicacion'], GREEN)
        else:
            correct = self.update_score(False)
            self.show_message(f'Incorrecto. La respuesta era: {self.current_example["oracion"]}', RED)

class Game4Screen(BaseGameScreen):
    def __init__(self, **kwargs):
        super(Game4Screen, self).__init__(**kwargs)
        self.name = 'game4'
        self.word_buttons = []
        self.build_ui()
    
    def build_ui(self):
        # Limpiar layout
        self.content_layout.clear_widgets()
        self.word_buttons = []
        
        # Título
        title = Label(text='Juego 4: Ordena las Palabras', 
                     font_size=28, bold=True, color=PURPLE)
        self.content_layout.add_widget(title)
        
        # Instrucciones
        instructions = Label(text='Arrastra las palabras para formar la oración correcta:', 
                            font_size=20, color=WHITE)
        self.content_layout.add_widget(instructions)
        
        # Preparar palabras
        sentence = self.current_example['oracion']
        words = sentence.split()
        random.shuffle(words)
        
        # Crear layout para palabras
        scroll_view = ScrollView(size_hint=(1, 0.5), do_scroll_x=True)
        self.words_layout = GridLayout(cols=len(words), spacing=10, 
                                      size_hint_x=None, height=100)
        self.words_layout.bind(minimum_width=self.words_layout.setter('width'))
        
        for word in words:
            btn = Button(text=word, background_color=DARK_BLUE, 
                        size_hint_x=None, width=len(word)*20 + 30)
            btn.bind(on_touch_move=self.on_touch_move)
            self.word_buttons.append(btn)
            self.words_layout.add_widget(btn)
        
        scroll_view.add_widget(self.words_layout)
        self.content_layout.add_widget(scroll_view)
        
        # Área de solución
        solution_label = Label(text='Arrastra las palabras aquí para formar la oración:', 
                             font_size=18, color=WHITE, size_hint_y=0.1)
        self.content_layout.add_widget(solution_label)
        
        self.solution_layout = GridLayout(cols=len(words), spacing=10, 
                                         size_hint_y=0.15, size_hint_x=None)
        self.solution_layout.bind(minimum_width=self.solution_layout.setter('width'))
        
        scroll_solution = ScrollView(size_hint=(1, 0.2), do_scroll_x=True)
        scroll_solution.add_widget(self.solution_layout)
        self.content_layout.add_widget(scroll_solution)
        
        # Botón de verificación
        self.check_btn = Button(text='Verificar', background_color=GREEN, size_hint_y=0.1)
        self.check_btn.bind(on_press=self.verify_order)
        self.content_layout.add_widget(self.check_btn)
    
    def on_touch_move(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # Mover el botón con el dedo
            instance.center_x = touch.x
            instance.center_y = touch.y
            
            # Comprobar si está sobre el área de solución
            if self.solution_layout.collide_point(*touch.pos):
                # Clonar el botón para la solución
                if not hasattr(instance, 'in_solution'):
                    clone = Button(text=instance.text, background_color=GREEN,
                                  size_hint_x=None, width=instance.width)
                    self.solution_layout.add_widget(clone)
                    instance.in_solution = True
    
    def reset_game(self):
        self.build_ui()
    
    def verify_order(self, instance):
        ordered_sentence = ' '.join(btn.text for btn in self.solution_layout.children[::-1])
        
        if ordered_sentence == self.current_example['oracion']:
            correct = self.update_score(True)
            self.show_message('¡Correcto! Orden perfecto.', GREEN)
        else:
            correct = self.update_score(False)
            self.show_message(f'Incorrecto. La oración correcta es: {self.current_example["oracion"]}', RED)

class Game5Screen(BaseGameScreen):
    def __init__(self, **kwargs):
        super(Game5Screen, self).__init__(**kwargs)
        self.name = 'game5'
        self.cards = []
        self.card_widgets = []
        self.build_ui()
    
    def build_ui(self):
        # Limpiar layout
        self.content_layout.clear_widgets()
        
        # Título
        title = Label(text='Juego 5: Memoria Condicional', 
                     font_size=28, bold=True, color=RED)
        self.content_layout.add_widget(title)
        
        # Instrucciones
        instructions = Label(text='Encuentra pares de condición y consecuencia', 
                            font_size=20, color=WHITE)
        self.content_layout.add_widget(instructions)
        
        # Crear layout de cartas
        grid = GridLayout(cols=2, rows=4, spacing=10, size_hint_y=0.7)
        
        # Seleccionar 4 pares de oraciones
        self.cards = []
        used_indices = set()
        
        while len(self.cards) < 8:
            category = random.choice(list(EJEMPLOS.keys()))
            example = random.choice(EJEMPLOS[category])
            
            if example["oracion"] in used_indices:
                continue
            
            used_indices.add(example["oracion"])
            
            # Dividir la oración
            parts = example["oracion"].split(",")
            if len(parts) >= 2:
                protasis = parts[0].strip()
                apodosis = ", ".join(parts[1:]).strip()
                
                self.cards.append({"text": protasis, "type": "protasis", "pair": len(self.cards)//2})
                self.cards.append({"text": apodosis, "type": "apodosis", "pair": len(self.cards)//2})
        
        # Barajar las cartas
        random.shuffle(self.cards)
        
        # Crear botones para las cartas
        self.card_widgets = []
        for card in self.cards:
            btn = Button(text='?', background_color=DARK_BLUE)
            btn.card_data = card
            btn.bind(on_press=self.reveal_card)
            grid.add_widget(btn)
            self.card_widgets.append(btn)
        
        self.content_layout.add_widget(grid)
        
        # Contador de pares
        self.pairs_label = Label(text='Pares encontrados: 0/4', font_size=18, color=WHITE)
        self.content_layout.add_widget(self.pairs_label)
        
        self.selected_cards = []
        self.matched_pairs = 0
    
    def reveal_card(self, instance):
        if instance.text != '?' or len(self.selected_cards) >= 2:
            return
        
        instance.text = instance.card_data['text']
        self.selected_cards.append(instance)
        
        if len(self.selected_cards) == 2:
            Clock.schedule_once(self.check_match, 1.0)
    
    def check_match(self, dt):
        card1, card2 = self.selected_cards
        if card1.card_data['pair'] == card2.card_data['pair']:
            card1.background_color = GREEN
            card2.background_color = GREEN
            self.matched_pairs += 1
            self.pairs_label.text = f'Pares encontrados: {self.matched_pairs}/4'
            correct = self.update_score(True)
            self.show_message('¡Par correcto!', GREEN)
            
            if self.matched_pairs == 4:
                self.show_message('¡Felicidades! Has completado el juego de memoria', GREEN)
        else:
            card1.text = '?'
            card2.text = '?'
            correct = self.update_score(False)
            self.show_message('Intenta de nuevo', RED)
        
        self.selected_cards = []
    
    def reset_game(self):
        self.build_ui()

class ConditionalSentencesApp(App):
    def build(self):
        # Configurar tamaño de la ventana
        Window.size = (1000, 700)
        
        # Crear ScreenManager
        sm = ScreenManager()
        
        # Añadir pantallas
        menu_screen = MenuScreen()
        sm.add_widget(menu_screen)
        sm.add_widget(Game1Screen())
        sm.add_widget(Game2Screen())
        sm.add_widget(Game3Screen())
        sm.add_widget(Game4Screen())
        sm.add_widget(Game5Screen())
        
        return sm

if __name__ == '__main__':
    ConditionalSentencesApp().run()
