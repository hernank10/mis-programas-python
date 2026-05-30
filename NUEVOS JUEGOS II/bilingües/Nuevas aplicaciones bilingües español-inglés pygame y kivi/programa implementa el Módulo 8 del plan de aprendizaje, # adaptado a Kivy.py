# Este programa implementa el Módulo 8 del plan de aprendizaje,
# adaptado a Kivy, para un diseño de interfaz de usuario completo y multiplataforma.

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.lang import Builder
import sqlite3
import random
import os

# Database Configuration
DB_NAME = "preguntas.db"

def inicializar_db():
    """Conecta a la base de datos y crea la tabla si no existe,
       insertando datos iniciales si la tabla está vacía."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preguntas (
            id INTEGER PRIMARY KEY,
            oracion_original TEXT NOT NULL,
            oracion_transformada TEXT NOT NULL,
            tipo_transformacion TEXT NOT NULL,
            idioma TEXT NOT NULL,
            dificultad INTEGER NOT NULL
        )
    """)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM preguntas")
    if cursor.fetchone()[0] == 0:
        lecciones_iniciales = [
            ("The boy who is wearing a hat is my brother.", "El chico que lleva un sombrero es mi hermano.", "adjetiva", "inglés", 1),
            ("Es importante que estudies.", "That you study is important.", "sustantiva", "español", 1),
            ("I believe that she is right.", "Creo que ella tiene razón.", "sustantiva", "inglés", 1),
            ("The house where I was born is for sale.", "La casa donde nací está en venta.", "adjetiva", "español", 1),
            ("I know who stole the cookies.", "Sé quién robó las galletas.", "sustantiva", "inglés", 1),
            ("No sé si va a llover mañana.", "I don't know if it will rain tomorrow.", "sustantiva", "español", 1),
            ("Because it's raining, we can't go to the park.", "Como está lloviendo, no podemos ir al parque.", "causal", "inglés", 2),
            ("He was so tired that he fell asleep.", "Estaba tan cansado que se quedó dormido.", "consecutiva", "inglés", 2),
            ("Cuando llegué a casa, mi hermana ya se había ido.", "When I arrived home, my sister had already left.", "temporal", "español", 2),
            ("He works as if he were a machine.", "Trabaja como si fuera una máquina.", "comparativa", "inglés", 2),
            ("Debido a que tengo un examen, no puedo salir.", "Because I have an exam, I can't go out.", "causal", "español", 2),
            ("Tan pronto como vi el mensaje, te llamé.", "As soon as I saw the message, I called you.", "temporal", "español", 2),
            ("Although she was sick, she went to school.", "A pesar de que estaba enferma, fue a la escuela.", "concesiva", "inglés", 3),
            ("Para que apruebes el curso, tienes que estudiar más.", "In order for you to pass the course, you have to study more.", "final", "español", 3),
            ("I will help you, provided that you ask nicely.", "Te ayudaré, siempre y cuando pidas bien.", "condicional", "inglés", 3),
            ("Though it was cold, we went swimming.", "Aunque hacía frío, fuimos a nadar.", "concesiva", "inglés", 3),
            ("Por mucho que insistas, no cambiaré de opinión.", "However much you insist, I won't change my mind.", "concesiva", "español", 3),
            ("Para que lo entiendas, te lo explicaré de nuevo.", "So that you understand it, I will explain it again.", "final", "español", 3),
        ]
        cursor.executemany("INSERT INTO preguntas (oracion_original, oracion_transformada, tipo_transformacion, idioma, dificultad) VALUES (?, ?, ?, ?, ?)", lecciones_iniciales)
        conn.commit()
    conn.close()

# Kivy Language (KV) for styling and structure
kv_code = """
<MainLayout>:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)

<BaseScreen>:
    # Common screen styling
    canvas.before:
        Color:
            rgb: 0.12, 0.12, 0.16
        Rectangle:
            size: self.size
            pos: self.pos

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        
        Label:
            text: 'Juego de Sintaxis'
            font_size: dp(60)
            halign: 'center'
            valign: 'middle'
            size_hint_y: None
            height: self.texture_size[1]
            color: 1, 1, 1, 1
        
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(15)
            padding: dp(20)
            size_hint: (0.8, 0.6)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            Button:
                text: 'Jugar'
                on_press: root.manager.current = 'juego'
                font_size: dp(35)
                background_color: (0.2, 0.2, 0.24, 1)
                background_normal: ''
                canvas.before:
                    Color:
                        rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(10)]
            
            Button:
                text: 'Estadísticas'
                on_press: root.manager.current = 'estadisticas'
                font_size: dp(35)
                background_color: (0.2, 0.2, 0.24, 1)
                background_normal: ''
                canvas.before:
                    Color:
                        rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(10)]

            Button:
                text: 'Ayuda'
                on_press: root.manager.current = 'ayuda'
                font_size: dp(35)
                background_color: (0.2, 0.2, 0.24, 1)
                background_normal: ''
                canvas.before:
                    Color:
                        rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(10)]
            
            Button:
                text: 'Salir'
                on_press: app.stop()
                font_size: dp(35)
                background_color: (0.2, 0.2, 0.24, 1)
                background_normal: ''
                canvas.before:
                    Color:
                        rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(10)]

<JuegoScreen>:
    name: 'juego'
    
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(60)
            padding: [0, 0, dp(20), 0]
            Label:
                text: 'Puntaje: ' + str(root.puntaje)
                font_size: dp(25)
                halign: 'left'
                valign: 'middle'
                text_size: self.size
                color: 1, 1, 1, 1
            Label:
                text: 'Dificultad: ' + str(root.dificultad_actual)
                font_size: dp(25)
                halign: 'right'
                valign: 'middle'
                text_size: self.size
                color: 1, 1, 1, 1

        BoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(10)
            canvas.before:
                Color:
                    rgb: 0.2, 0.2, 0.24, 0.6
                Rectangle:
                    size: self.size
                    pos: self.pos
            
            Label:
                text: root.oracion_actual
                font_size: dp(30)
                halign: 'center'
                valign: 'middle'
                text_size: self.size
                color: 1, 1, 1, 1

            Label:
                text: 'Transforma a: ' + root.tipo_transformacion
                font_size: dp(30)
                halign: 'center'
                valign: 'middle'
                text_size: self.size
                color: 1, 1, 1, 1
            
            TextInput:
                id: input_text
                hint_text: 'Escribe tu respuesta aquí'
                font_size: dp(25)
                size_hint_y: None
                height: dp(50)
                multiline: False
                on_text_validate: root.verificar_respuesta()
            
            Label:
                id: feedback_label
                text: ''
                font_size: dp(25)
                color: 0.48, 0.98, 0.35, 1
                halign: 'center'
                valign: 'middle'
                text_size: self.size

        Button:
            text: 'Volver al Menú'
            on_press: root.manager.current = 'menu'
            size_hint_y: None
            height: dp(50)
            background_color: (0.2, 0.2, 0.24, 1)
            background_normal: ''
            canvas.before:
                Color:
                    rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(10)]

<EstadisticasScreen>:
    name: 'estadisticas'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)
        spacing: dp(20)

        Label:
            text: 'Estadísticas'
            font_size: dp(60)
            halign: 'center'
            valign: 'middle'
            size_hint_y: None
            height: self.texture_size[1]
            color: 1, 1, 1, 1

        GridLayout:
            cols: 2
            spacing: dp(10)
            size_hint_y: 0.6

            Label:
                text: 'Puntaje más alto:'
                font_size: dp(30)
                halign: 'right'
                text_size: self.size
            Label:
                text: '150'
                font_size: dp(30)
                halign: 'left'
                color: 0.48, 0.98, 0.35, 1
                text_size: self.size

            Label:
                text: 'Oraciones correctas:'
                font_size: dp(30)
                halign: 'right'
                text_size: self.size
            Label:
                text: '75'
                font_size: dp(30)
                halign: 'left'
                color: 0.48, 0.98, 0.35, 1
                text_size: self.size
            
            Label:
                text: 'Dificultad máxima alcanzada:'
                font_size: dp(30)
                halign: 'right'
                text_size: self.size
            Label:
                text: '3'
                font_size: dp(30)
                halign: 'left'
                color: 0.48, 0.98, 0.35, 1
                text_size: self.size
        
        Button:
            text: 'Volver al Menú'
            on_press: root.manager.current = 'menu'
            size_hint_y: None
            height: dp(50)
            background_color: (0.2, 0.2, 0.24, 1)
            background_normal: ''
            canvas.before:
                Color:
                    rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(10)]
    
<AyudaScreen>:
    name: 'ayuda'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)
        spacing: dp(20)

        Label:
            text: 'Ayuda'
            font_size: dp(60)
            halign: 'center'
            valign: 'middle'
            size_hint_y: None
            height: self.texture_size[1]
            color: 1, 1, 1, 1
            
        Label:
            text: '[b]Instrucciones:[/b]\\n1. Elige una opción del menú principal.\\n2. En el juego, traduce la oración original a su equivalente en el idioma y la sintaxis especificada.\\n3. Escribe tu respuesta y presiona "Enter".\\n4. Si tu respuesta es correcta, tu puntaje subirá.\\n5. Para pasar de nivel, necesitas acertar 3 oraciones.'
            font_size: dp(25)
            halign: 'left'
            valign: 'top'
            text_size: (self.width, None)
            markup: True
            
        Button:
            text: 'Volver al Menú'
            on_press: root.manager.current = 'menu'
            size_hint_y: None
            height: dp(50)
            background_color: (0.2, 0.2, 0.24, 1)
            background_normal: ''
            canvas.before:
                Color:
                    rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(10)]

<ResultadosScreen>:
    name: 'resultados'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)
        spacing: dp(20)
        
        Label:
            text: '¡Resultados Finales!'
            font_size: dp(60)
            halign: 'center'
            valign: 'middle'
            size_hint_y: 0.5
            color: 1, 1, 1, 1
        
        Label:
            text: 'Tu puntaje es: ' + str(root.puntaje)
            font_size: dp(40)
            halign: 'center'
            valign: 'middle'
            size_hint_y: 0.3
            color: 1, 1, 1, 1

        Button:
            text: 'Jugar de Nuevo'
            on_press:
                root.manager.current = 'juego'
                root.manager.get_screen('juego').iniciar_juego()
            size_hint_y: None
            height: dp(60)
            background_color: (0.2, 0.2, 0.24, 1)
            background_normal: ''
            canvas.before:
                Color:
                    rgb: self.background_color if self.state == 'normal' else (1,1,1,1)
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(10)]

"""
# Load the KV language string
Builder.load_string(kv_code)

class BaseScreen(Screen):
    pass

class MenuScreen(BaseScreen):
    pass

class EstadisticasScreen(BaseScreen):
    pass

class AyudaScreen(BaseScreen):
    pass

class ResultadosScreen(BaseScreen):
    puntaje = 0

class JuegoScreen(BaseScreen):
    puntaje = 0
    dificultad_actual = 1
    oracion_actual = StringProperty("")
    tipo_transformacion = StringProperty("")
    
    preguntas_jugadas_ids = []
    pregunta_actual = None
    preguntas_correctas_nivel = 0
    correctas_para_subir = 3
    
    def on_enter(self, *args):
        self.iniciar_juego()

    def iniciar_juego(self):
        self.puntaje = 0
        self.preguntas_jugadas_ids = []
        self.dificultad_actual = 1
        self.preguntas_correctas_nivel = 0
        self.obtener_nueva_pregunta()

    def obtener_nueva_pregunta(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM preguntas WHERE dificultad = ?", (self.dificultad_actual,))
        preguntas_disponibles_db = cursor.fetchall()
        conn.close()
        
        preguntas_no_jugadas = [p for p in preguntas_disponibles_db if p[0] not in self.preguntas_jugadas_ids]
        
        if preguntas_no_jugadas:
            self.pregunta_actual = random.choice(preguntas_no_jugadas)
            self.preguntas_jugadas_ids.append(self.pregunta_actual[0])
            self.ids.input_text.text = ""
            self.oracion_actual = self.pregunta_actual[1]
            self.tipo_transformacion = self.pregunta_actual[3].capitalize()
        else:
            if self.dificultad_actual < 3:
                self.subir_nivel_dificultad()
                self.obtener_nueva_pregunta()
            else:
                self.ir_a_resultados()

    def verificar_respuesta(self):
        if self.pregunta_actual is None:
            return

        respuesta_correcta = self.pregunta_actual[2].lower().strip()
        respuesta_usuario = self.ids.input_text.text.lower().strip()
        
        feedback_label = self.ids.feedback_label
        
        if respuesta_usuario == respuesta_correcta:
            feedback_label.text = "¡Correcto! ✅✨"
            feedback_label.color = (0.48, 0.98, 0.35, 1) # Verde
            self.puntaje += 1
            self.preguntas_correctas_nivel += 1
            if self.preguntas_correctas_nivel >= self.correctas_para_subir and self.dificultad_actual < 3:
                self.subir_nivel_dificultad()
            Clock.schedule_once(lambda dt: self.obtener_nueva_pregunta(), 1.5)
        else:
            feedback_label.text = "Incorrecto. ❌💔"
            feedback_label.color = (1, 0.39, 0.28, 1) # Rojo
            Clock.schedule_once(lambda dt: self.obtener_nueva_pregunta(), 1.5)

    def subir_nivel_dificultad(self):
        self.dificultad_actual += 1
        self.preguntas_correctas_nivel = 0
        self.ids.feedback_label.text = f"¡Subiste a Dificultad {self.dificultad_actual}! 🎉"
        self.ids.feedback_label.color = (0.48, 0.98, 0.35, 1) # Verde

    def ir_a_resultados(self):
        self.manager.current = 'resultados'
        self.manager.get_screen('resultados').puntaje = self.puntaje

class JuegoSintaxisApp(App):
    def build(self):
        inicializar_db()
        
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(JuegoScreen(name='juego'))
        sm.add_widget(EstadisticasScreen(name='estadisticas'))
        sm.add_widget(AyudaScreen(name='ayuda'))
        sm.add_widget(ResultadosScreen(name='resultados'))
        return sm

if __name__ == '__main__':
    JuegoSintaxisApp().run()
