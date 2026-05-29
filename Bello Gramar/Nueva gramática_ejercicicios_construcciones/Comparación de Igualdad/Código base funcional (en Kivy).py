from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Pantallas
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Bienvenido a Ortotrón", font_size=32, pos_hint={"center_x": 0.5, "center_y": 0.8}))
        start_button = Button(text="Comenzar", size_hint=(0.3, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.5})
        start_button.bind(on_press=self.start_exercise)
        self.add_widget(start_button)

    def start_exercise(self, instance):
        self.manager.current = "exercise"

class ExerciseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.question = Label(text="Completa: Juan es ___ alto ___ Pedro.", pos_hint={"center_x": 0.5, "center_y": 0.7})
        self.input = TextInput(multiline=False, size_hint=(0.6, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.5})
        check_button = Button(text="Verificar", size_hint=(0.3, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        check_button.bind(on_press=self.check_answer)
        self.feedback = Label(text="", pos_hint={"center_x": 0.5, "center_y": 0.2})

        self.add_widget(self.question)
        self.add_widget(self.input)
        self.add_widget(check_button)
        self.add_widget(self.feedback)

    def check_answer(self, instance):
        user_input = self.input.text.strip().lower()
        if user_input == "más que":
            self.feedback.text = "¡Correcto! 🏆"
        else:
            self.feedback.text = "Intenta de nuevo ❌"

# Configuración
class OrtotronApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ExerciseScreen(name="exercise"))
        return sm

if __name__ == "__main__":
    OrtotronApp().run()
