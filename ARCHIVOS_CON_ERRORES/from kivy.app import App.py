from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.storage.jsonstore import JsonStore
import json
import random

Builder.load_string('''
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        Button:
            text: 'Practicar Ejemplos'
            on_press: root.manager.current = 'practice'
            font_size: 24
            size_hint_y: 0.2
            
        Button:
            text: 'Conceptos Teóricos'
            on_press: root.manager.current = 'theory'
            font_size: 24
            size_hint_y: 0.2
            
        Button:
            text: 'Cuestionario'
            on_press: root.manager.current = 'quiz'
            font_size: 24
            size_hint_y: 0.2
            
        Button:
            text: 'Mis Ejemplos'
            on_press: root.manager.current = 'manage'
            font_size: 24
            size_hint_y: 0.2
            
        Button:
            text: 'Salir'
            on_press: app.stop()
            font_size: 24
            size_hint_y: 0.2

<PracticeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        Label:
            text: f'Ejemplo {root.current_index}/{len(root.examples)}'
            font_size: 24
            size_hint_y: 0.1
            
        ProgressBar:
            max: len(root.examples)
            value: root.current_index
            size_hint_y: 0.05
            
        Label:
            text: root.current_example['phrase']
            font_size: 20
            text_size: self.width, None
            size_hint_y: 0.3
            halign: 'center'
            valign: 'middle'
            
        TextInput:
            id: answer_input
            hint_text: 'Escribe tu respuesta...'
            font_size: 24
            size_hint_y: 0.2
            multiline: False
            
        BoxLayout:
            spacing: 10
            size_hint_y: 0.15
            
            Button:
                text: 'Comprobar'
                on_press: root.check_answer(answer_input.text)
                font_size: 24
                
            Button:
                text: 'Siguiente'
                on_press: root.next_example()
                font_size: 24

<TheoryScreen>:
    ScrollView:
        Label:
            text: root.theory_text
            font_size: 20
            text_size: self.width, None
            padding: 20
            size_hint_y: None
            height: self.texture_size[1]

<QuizScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        Label:
            text: f'Pregunta {root.current_index}/{len(root.questions)}'
            font_size: 24
            size_hint_y: 0.1
            
        Label:
            text: root.current_question['phrase']
            font_size: 20
            text_size: self.width, None
            size_hint_y: 0.3
            halign: 'center'
            valign: 'middle'
            
        GridLayout:
            cols: 2
            spacing: 10
            size_hint_y: 0.5
            
            Button:
                text: 'Distributivo'
                on_press: root.check_category('distributivos')
                font_size: 24
                
            Button:
                text: 'Múltiplo'
                on_press: root.check_category('múltiplos')
                font_size: 24
                
            Button:
                text: 'Partitivo'
                on_press: root.check_category('partitivos')
                font_size: 24
                
            Button:
                text: 'Colectivo'
                on_press: root.check_category('colectivos')
                font_size: 24

<ManageScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        
        ScrollView:
            GridLayout:
                id: examples_grid
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: 10
        
        Button:
            text: 'Nuevo Ejemplo'
            on_press: root.show_creator()
            font_size: 24
            size_hint_y: 0.15

<ExampleCreatorPopup>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        Label:
            text: 'Crear Nuevo Ejemplo'
            font_size: 24
            
        TextInput:
            id: phrase_input
            hint_text: 'Frase con espacio (_)'
            font_size: 20
            size_hint_y: 0.2
            
        TextInput:
            id: answer_input
            hint_text: 'Respuesta correcta'
            font_size: 20
            size_hint_y: 0.2
            
        Spinner:
            id: category_spinner
            text: 'Selecciona categoría'
            values: ['distributivos', 'múltiplos', 'partitivos', 'colectivos']
            font_size: 20
            size_hint_y: 0.2
            
        BoxLayout:
            spacing: 10
            size_hint_y: 0.2
            
            Button:
                text: 'Guardar'
                on_press: root.save_example()
                font_size: 24
                
            Button:
                text: 'Cancelar'
                on_press: root.dismiss()
                font_size: 24
''')

class MainScreen(Screen):
    pass

class PracticeScreen(Screen):
    examples = ListProperty([])
    current_index = NumericProperty(0)
    current_example = ObjectProperty(None)
    
    def on_pre_enter(self):
        self.examples = App.get_running_app().store.get('examples')['data']
        self.current_index = 0
        self.load_example()
    
    def load_example(self):
        if self.current_index < len(self.examples):
            self.current_example = self.examples[self.current_index]
    
    def next_example(self):
        self.current_index += 1
        if self.current_index >= len(self.examples):
            self.manager.current = 'main'
        else:
            self.load_example()
            self.ids.answer_input.text = ''
    
    def check_answer(self, answer):
        if answer.lower() == self.current_example['answer'].lower():
            App.get_running_app().show_toast('¡Correcto!')
        else:
            App.get_running_app().show_toast(f'Error. Correcto: {self.current_example["answer"]}')
        self.next_example()

class TheoryScreen(Screen):
    theory_text = '''
    [b]Conceptos Clave:[/b]
    
    [i]Distributivos:[/i]
    - Sendos/sendas: Siempre plural
    - Cada: Invariable
    
    [i]Múltiplos:[/i]
    - Doble, triple, céntuplo
    - Sufijo -tanto
    
    [i]Partitivos:[/i]
    - Fracciones: tercio, cuarto
    - Sufijo -avo
    
    [i]Colectivos:[/i]
    - Grupos: docena, centenar, millar
    '''

class QuizScreen(Screen):
    questions = ListProperty([])
    current_index = NumericProperty(0)
    current_question = ObjectProperty(None)
    score = NumericProperty(0)
    
    def on_pre_enter(self):
        all_examples = App.get_running_app().store.get('examples')['data']
        self.questions = random.sample(all_examples, 10)
        self.current_index = 0
        self.score = 0
        self.load_question()
    
    def load_question(self):
        if self.current_index < len(self.questions):
            self.current_question = self.questions[self.current_index]
    
    def check_category(self, category):
        if category == self.current_question['category']:
            self.score += 1
            App.get_running_app().show_toast('¡Correcto!')
        else:
            App.get_running_app().show_toast(f'Categoría correcta: {self.current_question["category"]}')
        
        self.current_index += 1
        if self.current_index >= len(self.questions):
            self.manager.current = 'quiz_result'
        else:
            self.load_question()

class ManageScreen(Screen):
    def on_pre_enter(self):
        self.load_examples()
    
    def load_examples(self):
        grid = self.ids.examples_grid
        grid.clear_widgets()
        
        examples = App.get_running_app().store.get('examples')['data']
        for ex in examples:
            if ex.get('custom', False):
                btn = Button(text=f"{ex['phrase']} -> {ex['answer']}", 
                            size_hint_y=None, height=60)
                btn.bind(on_press=lambda _, e=ex: self.delete_example(e))
                grid.add_widget(btn)
    
    def delete_example(self, example):
        app = App.get_running_app()
        app.store.put('examples', data=[e for e in app.store.get('examples')['data'] if e != example])
        self.load_examples()
    
    def show_creator(self):
        popup = ExampleCreatorPopup()
        popup.open()

class ExampleCreatorPopup(ModalView):
    def save_example(self):
        example = {
            'phrase': self.ids.phrase_input.text,
            'answer': self.ids.answer_input.text,
            'category': self.ids.category_spinner.text,
            'custom': True
        }
        
        app = App.get_running_app()
        examples = app.store.get('examples')['data']
        examples.append(example)
        app.store.put('examples', data=examples)
        
        self.dismiss()
        App.get_running_app().show_toast('Ejemplo guardado!')

class NumeralsApp(App):
    def build(self):
        self.store = JsonStore('data.json')
        if not self.store.exists('examples'):
            with open('default_examples.json') as f:
                default_data = json.load(f)
            self.store.put('examples', data=default_data)
        
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(PracticeScreen(name='practice'))
        sm.add_widget(TheoryScreen(name='theory'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ManageScreen(name='manage'))
        return sm
    
    def show_toast(self, message):
        from kivy.clock import Clock
        toast = Label(text=message, size_hint=(None, None), size=(400, 100),
                     pos_hint={'center_x': 0.5, 'top': 0.1}, color=(1,1,1,1),
                     canvas.before: Color(rgba=(0,0,0,0.7)), Rectangle(size=self.size, pos=self.pos))
        
        main_screen = self.root.get_screen('main')
        main_screen.add_widget(toast)
        Clock.schedule_once(lambda dt: main_screen.remove_widget(toast), 2)

if __name__ == '__main__':
    NumeralsApp().run()
