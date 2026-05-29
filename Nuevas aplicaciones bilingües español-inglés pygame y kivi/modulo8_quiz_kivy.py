# modulo8_quiz_kivy.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

# Banco de preguntas bilingüe (nivel básico)
preguntas = [
    {"en": "I am happy", "es": "Yo estoy feliz"},
    {"en": "She is my friend", "es": "Ella es mi amiga"},
    {"en": "We are students", "es": "Nosotros somos estudiantes"},
    {"en": "They play soccer", "es": "Ellos juegan fútbol"},
    {"en": "You are reading", "es": "Tú estás leyendo"}
]

class QuizGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.puntaje = 0
        self.pregunta_actual = None
        self.opciones_botones = []

        self.label_pregunta = Label(
            text="Traduce al español:\n",
            font_size=24,
            size_hint=(1, 0.3),
            halign="center",
            valign="middle"
        )
        self.add_widget(self.label_pregunta)

        self.layout_botones = BoxLayout(orientation="vertical", spacing=10)
        self.add_widget(self.layout_botones)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        self.layout_botones.clear_widgets()
        self.pregunta_actual = random.choice(preguntas)

        self.label_pregunta.text = f"Traduce al español:\n\n{self.pregunta_actual['en']}"

        # Generamos opciones falsas
        opciones = [self.pregunta_actual["es"]]
        while len(opciones) < 3:
            distractor = random.choice(preguntas)["es"]
            if distractor not in opciones:
                opciones.append(distractor)

        random.shuffle(opciones)

        for opcion in opciones:
            btn = Button(
                text=opcion,
                font_size=20,
                size_hint=(1, None),
                height=60,
                background_color=(0.8, 0, 0.3, 1)  # rubí
            )
            btn.bind(on_press=self.verificar_respuesta)
            self.layout_botones.add_widget(btn)
            self.opciones_botones.append(btn)

    def verificar_respuesta(self, instance):
        if instance.text == self.pregunta_actual["es"]:
            self.puntaje += 1
            contenido = Label(text=f"✅ Correcto!\nPuntaje: {self.puntaje}")
        else:
            contenido = Label(text=f"❌ Incorrecto!\nLa respuesta era:\n{self.pregunta_actual['es']}")

        popup = Popup(title="Resultado", content=contenido, size_hint=(0.7, 0.4))
        popup.bind(on_dismiss=lambda *a: self.mostrar_pregunta())
        popup.open()

class QuizApp(App):
    def build(self):
        return QuizGame()

if __name__ == "__main__":
    QuizApp().run()
