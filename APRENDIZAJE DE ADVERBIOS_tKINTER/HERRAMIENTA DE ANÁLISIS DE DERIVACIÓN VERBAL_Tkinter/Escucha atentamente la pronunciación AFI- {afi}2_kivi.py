from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from gtts import gTTS
import json
import random
import os

Builder.load_string('''
#:import Factory kivy.factory.Factory

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: '20dp'
        spacing: '15dp'
        
        Button:
            text: 'Practicar'
            font_size: '24sp'
            on_press: root.manager.current = 'category'
        
        Button:
            text: 'Administrar Ejemplos'
            font_size: '24sp'
            on_press: root.manager.current = 'manage'
        
        Button:
            text: 'Estadísticas'
            font_size: '24sp'
            on_press: root.show_stats()

<CategoryScreen>:
    GridLayout:
        cols: 2
        padding: '10dp'
        spacing: '10dp'
        
        Button:
            text: 'B/V'
            on_press: root.start_practice('B/V')
        Button:
            text: 'G/J'
            on_press: root.start_practice('G/J')
        Button:
            text: 'C/Z/S'
            on_press: root.start_practice('C/Z/S')
        Button:
            text: 'LL/Y'
            on_press: root.start_practice('LL/Y')
        Button:
            text: 'QU/C/K'
            on_press: root.start_practice('QU/C/K')
        Button:
            text: 'ACENTOS'
            on_press: root.start_practice('ACENTOS')
        
        Button:
            text: 'Volver'
            on_press: root.manager.current = 'main'

<PracticeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: '20dp'
        spacing: '15dp'
        
        Label:
            text: root.current_category
            font_size: '24sp'
            bold: True
            size_hint_y: None
            height: '50dp'
        
        Label:
            text: '[b]AFI:[/b] ' + root.current_afi
            markup: True
            font_size: '20sp'
            size_hint_y: None
            height: '50dp'
        
        Button:
            text: 'Escuchar Pronunciación'
            font_size: '20sp'
            on_press: root.play_audio()
            size_hint_y: None
            height: '60dp'
        
        TextInput:
            id: answer_input
            hint_text: 'Escribe la palabra aquí'
            font_size: '24sp'
            size_hint_y: None
            height: '80dp'
            multiline: False
        
        Label:
            id: feedback
            text: ''
            font_size: '20sp'
            color: 0,0.7,0,1
            size_hint_y: None
            height: '50dp'
        
        Button:
            text: 'Verificar'
            font_size: '24sp'
            on_press: root.check_answer()
        
        Button:
            text: 'Volver'
            on_press: root.manager.current = 'main'

<ManageScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        ScrollView:
            GridLayout:
                id: examples_grid
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                spacing: '10dp'
                padding: '10dp'
        
        BoxLayout:
            size_hint_y: None
            height: '60dp'
            spacing: '10dp'
            padding: '10dp'
            
            Button:
                text: 'Nuevo Ejemplo'
                on_press: Factory.EditPopup().open()
            
            Button:
                text: 'Volver'
                on_press: root.manager.current = 'main'

<EditPopup>:
    title: 'Editar Ejemplo'
    size_hint: 0.9, 0.9
    BoxLayout:
        orientation: 'vertical'
        padding: '10dp'
        spacing: '10dp'
        
        GridLayout:
            cols: 2
            spacing: '10dp'
            size_hint_y: None
            height: '300dp'
            
            Label:
                text: 'Palabra:'
            TextInput:
                id: palabra
            
            Label:
                text: 'AFI:'
            TextInput:
                id: afi
            
            Label:
                text: 'Categoría:'
            Spinner:
                id: categoria
                text: 'B/V'
                values: ['B/V', 'G/J', 'C/Z/S', 'LL/Y', 'QU/C/K', 'ACENTOS']
            
            Label:
                text: 'Regla:'
            TextInput:
                id: regla
            
            Label:
                text: 'Significado:'
            TextInput:
                id: significado
        
        Button:
            text: 'Guardar'
            size_hint_y: None
            height: '60dp'
            on_press: root.save_example()
''')

class MainScreen(Screen):
    def show_stats(self):
        stats = App.get_running_app().load_progress()
        content = BoxLayout(orientation='vertical', padding=10)
        scroll = ScrollView()
        grid = GridLayout(cols=1, size_hint_y=None, spacing=10)
        grid.bind(minimum_height=grid.setter('height'))
        
        for cat, data in stats.items():
            grid.add_widget(Label(
                text=f"{cat}: {data['correct']}/{data['total']} ({data['percentage']}%)",
                font_size='20sp'
            ))
        
        scroll.add_widget(grid)
        content.add_widget(scroll)
        content.add_widget(Button(text='Cerrar', on_press=lambda x: popup.dismiss()))
        
        popup = Popup(title='Estadísticas', content=content, size_hint=(0.9, 0.9))
        popup.open()

class CategoryScreen(Screen):
    def start_practice(self, category):
        app = App.get_running_app()
        app.current_category = category
        app.load_examples()
        app.shuffle_examples()
        self.manager.current = 'practice'

class PracticeScreen(Screen):
    current_category = StringProperty('')
    current_afi = StringProperty('')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = None
    
    def on_pre_enter(self):
        app = App.get_running_app()
        self.current_category = app.current_category
        self.load_next_word()
    
    def load_next_word(self):
        app = App.get_running_app()
        if app.example_index < len(app.current_examples):
            example = app.current_examples[app.example_index]
            self.current_afi = example['AFI']
            self.ids.answer_input.text = ''
            self.ids.feedback.text = ''
    
    def play_audio(self):
        app = App.get_running_app()
        example = app.current_examples[app.example_index]
        tts = gTTS(text=example['palabra'], lang='es')
        tts.save('temp.mp3')
        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load('temp.mp3')
        if self.sound:
            self.sound.play()
    
    def check_answer(self):
        app = App.get_running_app()
        example = app.current_examples[app.example_index]
        user_answer = self.ids.answer_input.text.strip().lower()
        correct = example['palabra'].lower()
        
        if user_answer == correct:
            feedback = "[b]✓ Correcto![/b]\n" + example['regla']
            app.correct_answers += 1
        else:
            feedback = f"[b]✗ Error:[/b] {correct}\n" + example['regla']
        
        self.ids.feedback.text = feedback
        app.example_index += 1
        app.save_progress()
        
        if app.example_index < len(app.current_examples):
            Clock.schedule_once(lambda dt: self.load_next_word(), 2)
        else:
            self.show_results()

    def show_results(self):
        app = App.get_running_app()
        total = len(app.current_examples)
        result = f"Resultado: {app.correct_answers}/{total}"
        popup = Popup(title='Práctica Completada',
                     content=Label(text=result, font_size='24sp'),
                     size_hint=(0.8, 0.4))
        popup.open()
        self.manager.current = 'main'

class ManageScreen(Screen):
    def on_pre_enter(self):
        self.load_examples()
    
    def load_examples(self):
        app = App.get_running_app()
        self.ids.examples_grid.clear_widgets()
        for example in app.examples:
            btn = Button(
                text=f"{example['palabra']} ({example['categoria']})",
                size_hint_y=None,
                height='60dp',
                on_press=lambda x, e=example: self.edit_example(e)
            )
            self.ids.examples_grid.add_widget(btn)

    def edit_example(self, example):
        popup = Factory.EditPopup()
        popup.ids.palabra.text = example['palabra']
        popup.ids.afi.text = example['AFI']
        popup.ids.categoria.text = example['categoria']
        popup.ids.regla.text = example['regla']
        popup.ids.significado.text = example['significado']
        popup.example = example
        popup.open()

class EditPopup(Popup):
    def save_example(self):
        app = App.get_running_app()
        new_example = {
            'palabra': self.ids.palabra.text,
            'AFI': self.ids.afi.text,
            'categoria': self.ids.categoria.text,
            'regla': self.ids.regla.text,
            'significado': self.ids.significado.text
        }
        
        if hasattr(self, 'example'):
            index = app.examples.index(self.example)
            app.examples[index] = new_example
        else:
            app.examples.append(new_example)
        
        app.save_examples()
        app.root.get_screen('manage').load_examples()
        self.dismiss()

class OrthoApp(App):
    examples = ListProperty()
    current_examples = ListProperty()
    current_category = StringProperty('')
    example_index = 0
    correct_answers = 0
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CategoryScreen(name='category'))
        sm.add_widget(PracticeScreen(name='practice'))
        sm.add_widget(ManageScreen(name='manage'))
        return sm
    
    def on_start(self):
        self.load_examples()
        self.load_progress()
    
    def load_examples(self):
        try:
            with open('ejemplos.json') as f:
                self.examples = json.load(f)
        except FileNotFoundError:
            self.examples = []
    
    def save_examples(self):
        with open('ejemplos.json', 'w') as f:
            json.dump(self.examples, f, indent=2)
    
    def shuffle_examples(self):
        self.current_examples = [
            e for e in self.examples 
            if e['categoria'] == self.current_category
        ]
        random.shuffle(self.current_examples)
        self.example_index = 0
        self.correct_answers = 0
    
    def load_progress(self):
        try:
            with open('progreso.json') as f:
                self.progress = json.load(f)
        except FileNotFoundError:
            self.progress = {}
    
    def save_progress(self):
        category_progress = self.progress.get(self.current_category, {
            'total': 0,
            'correct': 0
        })
        category_progress['total'] += 1
        if self.ids.feedback.text.startswith('✓'):
            category_progress['correct'] += 1
        self.progress[self.current_category] = category_progress
        
        with open('progreso.json', 'w') as f:
            json.dump(self.progress, f, indent=2)

if __name__ == '__main__':
    OrthoApp().run()
