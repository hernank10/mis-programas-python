from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

# Banco de ejercicios (ejemplo reducido, puedes expandir a 100)
exercises = [
    {"spanish": "¿Cómo te llamas?", "english": ["What is your name?", "What's your name?"]},
    {"spanish": "¿Dónde vives?", "english": ["Where do you live?"]},
    {"spanish": "¿Puedes ayudarme?", "english": ["Can you help me?"]},
    {"spanish": "¿Qué hora es?", "english": ["What time is it?"]},
    {"spanish": "¿Hablas inglés?", "english": ["Do you speak English?"]},
]

class QuestionTrainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.score = 0
        self.current = None

        # Widgets
        self.label = Label(text="Haz clic en 'Nuevo ejercicio' para comenzar", font_size=20)
        self.add_widget(self.label)

        self.input = TextInput(hint_text="Escribe tu respuesta en inglés", multiline=False)
        self.add_widget(self.input)

        button_layout = BoxLayout(size_hint_y=0.2)

        self.btn_new = Button(text="Nuevo ejercicio")
        self.btn_new.bind(on_press=self.new_exercise)
        button_layout.add_widget(self.btn_new)

        self.btn_check = Button(text="Comprobar")
        self.btn_check.bind(on_press=self.check_answer)
        button_layout.add_widget(self.btn_check)

        self.add_widget(button_layout)

    def new_exercise(self, instance):
        self.current = random.choice(exercises)
        self.label.text = f"Traduce al inglés: {self.current['spanish']}"
        self.input.text = ""

    def check_answer(self, instance):
        if not self.current:
            return

        user_answer = self.input.text.strip()
        if user_answer in self.current["english"]:
            self.score += 1
            content = Label(text=f"¡Correcto! ✅\nPuntaje: {self.score}")
        else:
            correct = ", ".join(self.current["english"])
            content = Label(text=f"❌ Incorrecto\nRespuestas correctas:\n{correct}")

        popup = Popup(title="Resultado",
                      content=content,
                      size_hint=(0.6, 0.4))
        popup.open()

class QuestionApp(App):
    def build(self):
        return QuestionTrainer()

if __name__ == "__main__":
    QuestionApp().run()
