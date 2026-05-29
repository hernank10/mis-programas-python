# main.py - Base de la aplicación Kivy conectando todos los módulos

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

# Módulos personalizados
from avatar_module import AvatarSelector
from timer_mode import TimerMode
from firebase_integration import enviar_estadisticas
from user_progress import cargar_usuario, guardar_usuario
from preguntas_random import obtener_pregunta_random

# Datos globales
usuario_actual = None
puntaje = 0

# Interfaz Kivy
KV = '''
MDScreen:
    name: 'main'

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDLabel:
            id: pregunta_lbl
            text: "Pulsa el botón para una pregunta"
            halign: "center"

        MDRaisedButton:
            text: "Mostrar Pregunta"
            pos_hint: {"center_x": 0.5}
            on_release: app.mostrar_pregunta()

        MDRaisedButton:
            text: "Modo Contrarreloj"
            pos_hint: {"center_x": 0.5}
            on_release: app.iniciar_modo_timer()

        MDRaisedButton:
            text: "Seleccionar Avatar"
            pos_hint: {"center_x": 0.5}
            on_release: app.seleccionar_avatar()

        MDRaisedButton:
            text: "Enviar progreso a Firebase"
            pos_hint: {"center_x": 0.5}
            on_release: app.enviar_estadisticas()
'''

class MainApp(MDApp):
    def build(self):
        self.title = "App Educativa Kivy"
        Window.size = (360, 640)
        self.screen = Builder.load_string(KV)
        return self.screen

    def mostrar_pregunta(self):
        pregunta = obtener_pregunta_random()
        self.screen.ids.pregunta_lbl.text = pregunta.get("prompt", "Pregunta no disponible")

    def iniciar_modo_timer(self):
        TimerMode().start()

    def seleccionar_avatar(self):
        AvatarSelector().open()

    def enviar_estadisticas(self):
        enviar_estadisticas(usuario_actual, puntaje)

if __name__ == '__main__':
    usuario_actual = cargar_usuario("usuario_demo")
    MainApp().run()
    guardar_usuario("usuario_demo", usuario_actual)
