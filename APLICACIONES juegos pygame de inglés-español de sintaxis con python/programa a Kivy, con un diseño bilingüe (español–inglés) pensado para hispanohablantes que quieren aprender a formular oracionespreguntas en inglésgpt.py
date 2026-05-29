from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
import random

# === Banco de ejercicios bilingües (ejemplo reducido a 10, expándelo hasta 100) ===
exercises = [
    {"spanish": "¿Cómo te llamas?", "english": ["What is your name?", "What's your name?"]},
    {"spanish": "¿Dónde vives?", "english": ["Where do you live?"]},
    {"spanish": "¿Puedes ayudarme?", "english": ["Can you help me?"]},
    {"spanish": "¿Qué hora es?", "english": ["What time is it?"]},
    {"spanish": "¿Hablas inglés?", "english": ["Do you speak English?"]},
    {"spanish": "Quiero aprender inglés.", "english": ["I want to learn English."]},
    {"spanish": "Ella estudia todos los días.", "english": ["She studies every day."]},
    {"spanish": "Estoy cansado, pero feliz.", "english": ["I am tired, but happy."]},
    {"spanish": "Tengo hambre y sed.", "english": ["I am hungry and thirsty."]},
    {"spanish": "Me gusta el café, pero prefiero el té.", "english": ["I like coffee, but I prefer tea."]},
]

# 🎨 Paleta natural (verde bosque, azul cielo, arena, tierra, blanco nube)
COLORS = {
    "forest_green": [0.13, 0.55, 0.13, 1],
    "sky_blue": [0.53, 0.81, 0.98, 1],
    "earth_brown": [0.55, 0.27, 0.07, 1],
    "sand": [0.96, 0.87, 0.70, 1],
    "cloud_white": [1, 1, 1, 1],
}

class BilingualTrainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Fondo arena
        with self.canvas.before:
            Color(*COLORS["sand"])
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.score = 0
        self.current = None

        # Etiqueta principal bilingüe
        self.label = Label(
            text="Haz clic en 'Nuevo ejercicio / New Exercise' para comenzar",
            font_size=20,
            color=COLORS["earth_brown"],
        )
        self.add_widget(self.label)

        # Entrada de texto
        self.input = TextInput(
            hint_text="Escribe tu respuesta en inglés / Write your answer in English",
            multiline=False,
            foreground_color=COLORS["forest_green"],
            background_color=COLORS["cloud_white"],
        )
        self.add_widget(self.input)

        # Botones
        button_layout = BoxLayout(size_hint_y=0.2)

        self.btn_new = Button(
            text="Nuevo ejercicio / New Exercise",
            color=COLORS["cloud_white"],
            background_color=COLORS["sky_blue"],
        )
        self.btn_new.bind(on_press=self.new_exercise)
        button_layout.add_widget(self.btn_new)

        self.btn_check = Button(
            text="Comprobar / Check",
            color=COLORS["cloud_white"],
            background_color=COLORS["forest_green"],
        )
        self.btn_check.bind(on_press=self.check_answer)
        button_layout.add_widget(self.btn_check)

        self.add_widget(button_layout)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def new_exercise(self, instance):
        self.current = random.choice(exercises)
        self.label.text = f"Traduce al inglés / Translate into English:\n{self.current['spanish']}"
        self.input.text = ""

    def check_answer(self, instance):
        if not self.current:
            return

        user_answer = self.input.text.strip()
        if user_answer in self.current["english"]:
            self.score += 1
            content = Label(
                text=f"🌿 ¡Correcto! / Correct ✅\nPuntaje / Score: {self.score}",
                color=COLORS["forest_green"]
            )
        else:
            correct = "\n".join(self.current["english"])
            content = Label(
                text=f"❌ Incorrecto / Incorrect\nRespuestas correctas / Correct answers:\n{correct}",
                color=COLORS["earth_brown"]
            )

        popup = Popup(title="Resultado / Result",
                      content=content,
                      size_hint=(0.8, 0.5))
        popup.open()

class BilingualApp(App):
    def build(self):
        return BilingualTrainer()

if __name__ == "__main__":
    BilingualApp().run()
