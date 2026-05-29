from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty, BooleanProperty
from kivy.clock import Clock, mainthread
from kivy.lang import Builder
import subprocess
import sys
import platform
import threading

Builder.load_string('''
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        
        ScrollView:
            Label:
                id: log_label
                text: root.log_text
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                halign: 'left'
                valign: 'top'
        
        GridLayout:
            cols: 2
            spacing: 10
            size_hint_y: None
            height: 100
            
            Button:
                text: 'Instalar Dependencias'
                on_press: root.instalar_dependencias()
                disabled: root.dependencias_instaladas
            
            Button:
                text: 'Abrir CRUD'
                on_press: root.manager.current = 'crud'
                disabled: not root.dependencias_instaladas
            
            Button:
                text: 'Modo Práctica'
                on_press: root.manager.current = 'quiz'
            
            Button:
                text: 'Salir'
                on_press: app.stop()

<CRUDScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        
        RecycleView:
            id: rv
            viewclass: 'Label'
            RecycleBoxLayout:
                default_size: None, dp(40)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        
        BoxLayout:
            size_hint_y: None
            height: 50
            spacing: 10
            
            Button:
                text: 'Añadir'
                on_press: root.mostrar_dialogo_anadir()
            
            Button:
                text: 'Eliminar'
                on_press: root.eliminar_item()
            
            Button:
                text: 'Volver'
                on_press: root.manager.current = 'main'

<QuizScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        
        Label:
            id: prefijo_label
            text: root.prefijo_actual
            font_size: 30
            halign: 'center'
        
        Label:
            id: palabra_label
            text: root.palabra_actual
            font_size: 30
            halign: 'center'
        
        TextInput:
            id: respuesta_input
            font_size: 24
            multiline: False
            hint_text: 'Escribe la palabra completa'
        
        Label:
            text: f'Puntuación: {root.puntaje}/{root.total_preguntas}'
            font_size: 20
        
        BoxLayout:
            spacing: 10
            size_hint_y: None
            height: 50
            
            Button:
                text: 'Verificar'
                on_press: root.verificar_respuesta()
            
            Button:
                text: 'Volver'
                on_press: root.manager.current = 'main'
''')

class MainScreen(Screen):
    log_text = StringProperty('')
    dependencias_instaladas = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.verificar_dependencias()

    def verificar_dependencias(self):
        try:
            import kivy
            import fastapi
            self.dependencias_instaladas = True
            self.log_text = 'Dependencias ya instaladas!\n'
        except ImportError:
            self.log_text = 'Dependencias requeridas no instaladas.\n'

    def instalar_dependencias(self):
        threading.Thread(target=self._instalar_background).start()

    def _instalar_background(self):
        requerimientos = ['kivy', 'fastapi', 'uvicorn', 'python-multipart']
        for pkg in requerimientos:
            self.actualizar_log(f'Instalando {pkg}...')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
                self.actualizar_log(f'✓ {pkg} instalado\n')
            except Exception as e:
                self.actualizar_log(f'✗ Error instalando {pkg}: {str(e)}\n')
        
        if platform.system() == "Darwin":
            self.instalar_dependencias_macos()
        
        self.dependencias_instaladas = True

    def instalar_dependencias_macos(self):
        self.actualizar_log('Instalando dependencias para macOS...\n')
        try:
            subprocess.run(['brew', 'install', 'sdl2', 'sdl2_image', 'sdl2_ttf', 'sdl2_mixer', 'portaudio'])
            self.actualizar_log('✓ Dependencias macOS instaladas\n')
        except Exception as e:
            self.actualizar_log(f'✗ Error dependencias macOS: {str(e)}\n')

    @mainthread
    def actualizar_log(self, mensaje):
        self.log_text += mensaje

class CRUDScreen(Screen):
    datos = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datos = [
            {'text': 'Antinuclear - anti- - Oposición'},
            {'text': 'Deshacer - des- - Negación'}
        ]

    def mostrar_dialogo_anadir(self):
        content = BoxLayout(orientation='vertical', padding=10)
        campos = [
            ('Palabra:', 'text'),
            ('Prefijo:', 'text'),
            ('Clasificación:', 'text'),
            ('Significado:', 'text')
        ]
        entries = {}
        
        for label, hint in campos:
            box = BoxLayout(size_hint_y=None, height=40)
            box.add_widget(Label(text=label))
            entry = TextInput(hint_text=hint)
            entries[label] = entry
            box.add_widget(entry)
            content.add_widget(box)

        def guardar(_):
            nuevo_item = ' - '.join([entry.text for entry in entries.values()])
            self.datos.append({'text': nuevo_item})
            popup.dismiss()

        btn_guardar = Button(text='Guardar', size_hint_y=None, height=50)
        btn_guardar.bind(on_press=guardar)
        content.add_widget(btn_guardar)
        
        popup = Popup(title='Nuevo Prefijo', content=content)
        popup.open()

    def eliminar_item(self):
        if self.ids.rv.layout_manager.selected_nodes:
            index = self.ids.rv.layout_manager.selected_nodes[0]
            self.datos.pop(index)

class QuizScreen(Screen):
    preguntas = ListProperty([
        {'prefijo': 'anti-', 'palabra': 'nuclear', 'respuesta': 'antinuclear'},
        {'prefijo': 'des-', 'palabra': 'hacer', 'respuesta': 'deshacer'}
    ])
    prefijo_actual = StringProperty('')
    palabra_actual = StringProperty('')
    puntaje = 0
    total_preguntas = 0
    indice_actual = 0

    def on_pre_enter(self):
        self.iniciar_quiz()

    def iniciar_quiz(self):
        self.total_preguntas = len(self.preguntas)
        self.indice_actual = 0
        self.puntaje = 0
        self.mostrar_siguiente_pregunta()

    def mostrar_siguiente_pregunta(self):
        if self.indice_actual < len(self.preguntas):
            pregunta = self.preguntas[self.indice_actual]
            self.prefijo_actual = pregunta['prefijo']
            self.palabra_actual = pregunta['palabra']
            self.ids.respuesta_input.text = ''
        else:
            self.manager.current = 'main'

    def verificar_respuesta(self):
        respuesta = self.ids.respuesta_input.text.strip().lower()
        correcta = self.preguntas[self.indice_actual]['respuesta']
        
        if respuesta == correcta:
            self.puntaje += 1
        
        self.indice_actual += 1
        self.mostrar_siguiente_pregunta()

class PrefijosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CRUDScreen(name='crud'))
        sm.add_widget(QuizScreen(name='quiz'))
        return sm

if __name__ == '__main__':
    PrefijosApp().run()
