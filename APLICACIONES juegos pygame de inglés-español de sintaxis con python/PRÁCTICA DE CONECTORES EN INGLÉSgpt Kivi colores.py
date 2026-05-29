from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
import random

# Banco de ejercicios (ejemplo reducido, puedes expandir a 100)
exercises = [
    {"spanish": "¿Cómo te llamas?", "english": ["What is your name?", "What's your name?"]},
    {"spanish": "¿Dónde vives?", "english": ["Where do you live?"]},
    {"spanish": "¿Puedes ayudarme?", "english": ["Can you help me?"]},
    {"spanish": "¿Qué hora es?", "english": ["What time is it?"]},
    {"spanish": "¿Hablas inglés?", "english": ["Do you speak English?"]},
]

# 🎨 Paleta de colores naturaleza
COLORS = {
    "forest_green": [0.13, 0.55, 0.13, 1],   # Verde bosque
    "sky_blue": [0.53, 0.81, 0.98, 1],      # Azul cielo
    "earth_brown": [0.55, 0.27, 0.07, 1],   # Marrón tierra
    "sand": [0.96, 0.87, 0.70, 1],          # Arena
    "cloud_white": [1, 1, 1, 1],            # Blanco nube
}

class QuestionTrainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Fondo natural con canvas
        with self.canvas.before:
            Color(*COLORS["sand"])  # Arena de fondo
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.score = 0
        self.current = None

        # Etiqueta principal
        self.label = Label(
            text="Haz clic en 'Nuevo ejercicio' para comenzar",
            font_size=20,
            color=COLORS["earth_brown"],  # texto marrón tierra
        )
        self.add_widget(self.label)

        # Entrada de texto
        self.input = TextInput(
            hint_text="Escribe tu respuesta en inglés",
            multiline=False,
            foreground_color=COLORS["forest_green"],  # texto verde bosque
            background_color=COLORS["cloud_white"],  # fondo blanco nube
        )
        self.add_widget(self.input)

        # Botones en un layout horizontal
        button_layout = BoxLayout(size_hint_y=0.2)

        self.btn_new = Button(
            text="Nuevo ejercicio",
            color=COLORS["cloud_white"],              # texto blanco
            background_color=COLORS["sky_blue"],      # fondo azul cielo
        )
        self.btn_new.bind(on_press=self.new_exercise)
        button_layout.add_widget(self.btn_new)

        self.btn_check = Button(
            text="Comprobar",
            color=COLORS["cloud_white"],             # texto blanco
            background_color=COLORS["forest_green"], # fondo verde bosque
        )
        self.btn_check.bind(on_press=self.check_answer)
        button_layout.add_widget(self.btn_check)

        self.add_widget(button_layout)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

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
            content = Label(text=f"🌿 ¡Correcto! ✅\nPuntaje: {self.score}",
                            color=COLORS["forest_green"])
        else:
            correct = ", ".join(self.current["english"])
            content = Label(text=f"❌ Incorrecto\nRespuestas correctas:\n{correct}",
                            color=COLORS["earth_brown"])

        popup = Popup(title="Resultado",
                      content=content,
                      size_hint=(0.7, 0.4))
        popup.open()

class QuestionApp(App):
    def build(self):
        return QuestionTrainer()

if __name__ == "__main__":
    QuestionApp().run()
