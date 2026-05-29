from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty, StringProperty, ListProperty
import requests
import json
import matplotlib.pyplot as plt
from io import BytesIO

Builder.load_string('''
<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        
        canvas.before:
            Color:
                rgba: 0.96, 0.96, 0.94, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        Label:
            text: 'APRENDE VERBOS'
            font_size: 40
            color: 0.35, 0.65, 0.82, 1
            bold: True
        
        TextInput:
            id: username
            hint_text: 'Usuario'
            size_hint_y: None
            height: 50
        
        TextInput:
            id: password
            hint_text: 'Contraseña'
            password: True
            size_hint_y: None
            height: 50
        
        Button:
            text: 'Iniciar Sesión'
            background_color: 0.35, 0.65, 0.82, 1
            on_press: root.login()
            size_hint_y: None
            height: 50
        
        Button:
            text: 'Registrarse'
            background_color: 0.93, 0.33, 0.33, 1
            on_press: root.manager.current = 'register'
            size_hint_y: None
            height: 50

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint_y: None
            height: 60
            spacing: 10
            padding: 10
            
            Button:
                text: 'Verbos'
                on_press: root.show_examples()
            
            Button:
                text: 'Progreso'
                on_press: root.show_progress()
            
            Button:
                text: 'Notificaciones'
                on_press: root.show_notifications()
        
        ScreenManager:
            id: content_manager
            
            Screen:
                name: 'examples'
                ScrollView:
                    RecycleView:
                        id: examples_list
                        viewclass: 'ExampleItem'
                        RecycleBoxLayout:
                            default_size: None, 80
                            default_size_hint: 1, None
                            size_hint_y: None
                            height: self.minimum_height
                            orientation: 'vertical'
            
            Screen:
                name: 'progress'
                Image:
                    id: progress_chart
            
            Screen:
                name: 'notifications'
                ScrollView:
                    GridLayout:
                        id: notifications_list
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height

<ExampleItem@BoxLayout>:
    verb: ''
    conjugation: ''
    sentence: ''
    orientation: 'vertical'
    spacing: 5
    padding: 10
    
    canvas.before:
        Color:
            rgba: 0.35, 0.65, 0.82, 0.1
        Rectangle:
            pos: self.pos
            size: self.size
    
    Label:
        text: root.verb
        bold: True
        color: 0.35, 0.65, 0.82, 1
    
    Label:
        text: root.conjugation
        color: 0.2, 0.2, 0.2, 1
    
    Label:
        text: root.sentence
        color: 0.4, 0.4, 0.4, 1
        italic: True
''')

class LoginScreen(Screen):
    API_URL = "http://localhost:8000"
    
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        
        try:
            response = requests.post(
                f"{self.API_URL}/token",
                data={"username": username, "password": password}
            )
            if response.status_code == 200:
                token = response.json()["access_token"]
                App.get_running_app().token = token
                self.manager.current = 'main'
                self.manager.get_screen('main').load_data()
        except Exception as e:
            print("Error:", e)

class MainScreen(Screen):
    token = StringProperty('')
    API_URL = "http://localhost:8000"
    
    def load_data(self):
        Clock.schedule_once(lambda dt: self._load_async())
    
    def _load_async(self):
        self.load_examples()
        self.load_progress()
        self.load_notifications()
    
    def load_examples(self):
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(
                f"{self.API_URL}/examples",
                headers=headers
            )
            examples = response.json()
            self.ids.examples_list.data = [
                {
                    'verb': ex['verb'],
                    'conjugation': ex['conjugation'],
                    'sentence': ex['sentence']
                } for ex in examples
            ]
        except Exception as e:
            print("Error loading examples:", e)
    
    def load_progress(self):
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(
                f"{self.API_URL}/progress/chart",
                headers=headers
            )
            buf = BytesIO(response.content)
            self.ids.progress_chart.texture = (
                App.get_running_app().load_image_from_bytes(buf.getvalue())
        except Exception as e:
            print("Error loading progress:", e)
    
    def load_notifications(self):
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(
                f"{self.API_URL}/notifications",
                headers=headers
            )
            notifications = response.json()
            layout = self.ids.notifications_list
            layout.clear_widgets()
            for notif in notifications:
                layout.add_widget(Label(
                    text=notif['message'],
                    color=(0.2, 0.2, 0.2, 1)
                )
        except Exception as e:
            print("Error loading notifications:", e)
    
    def show_examples(self):
        self.ids.content_manager.current = 'examples'
    
    def show_progress(self):
        self.ids.content_manager.current = 'progress'
    
    def show_notifications(self):
        self.ids.content_manager.current = 'notifications'

class VerbosApp(App):
    token = StringProperty('')
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        return sm
    
    def load_image_from_bytes(self, data):
        from kivy.core.image import Image as CoreImage
        buf = BytesIO(data)
        return CoreImage(buf, ext='png').texture

if __name__ == '__main__':
    VerbosApp().run()
