from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock

questions = {
    "fácil": ("Completa: Juan es ___ alto ___ Pedro.", "más que"),
    "intermedio": ("Completa: María corre ___ rápido ___ Ana.", "tan como"),
    "avanzado": ("Completa: El coche es ___ costoso ___ el avión.", "menos que")
}

class AvatarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Selecciona tu avatar", font_size=28, pos_hint={"center_x": 0.5, "center_y": 0.85}))

        for i in range(1, 4):
            avatar = Image(source=f"avatar{i}.png", size_hint=(0.25, 0.25),
                           pos_hint={"center_x": 0.2 + i * 0.25, "center_y": 0.5})
            btn = Button(text=f"Avatar {i}", size_hint=(0.2, 0.1),
                         pos_hint={"center_x": 0.2 + i * 0.25, "center_y": 0.25})
            btn.bind(on_press=lambda instance, a=f"avatar{i}.png": self.select_avatar(a))
            self.add_widget(avatar)
            self.add_widget(btn)

    def select_avatar(self, avatar_path):
        self.manager.get_screen("level").avatar = avatar_path
        self.manager.get_screen("exercise").avatar_path = avatar_path
        self.manager.current = "level"

class LevelScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.avatar = ""
        self.add_widget(Label(text="Selecciona Nivel", font_size=28, pos_hint={"center_x": 0.5, "center_y": 0.8}))

        for i, level in enumerate(["fácil", "intermedio", "avanzado"]):
            btn = Button(text=level.capitalize(), size_hint=(0.3, 0.1),
                         pos_hint={"center_x": 0.5, "center_y": 0.6 - i * 0.15})
            btn.bind(on_press=lambda instance, l=level: self.select_level(l))
            self.add_widget(btn)

    def select_level(self, level):
        self.manager.get_screen("exercise").set_level(level)
        self.manager.current = "exercise"

class ExerciseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.level = "fácil"
        self.avatar_path = ""
        self.timer = 20  # segundos por pregunta
        self.clock_event = None

        self.avatar_img = Image(source="", size_hint=(0.15, 0.15), pos_hint={"center_x": 0.1, "center_y": 0.9})
        self.question_label = Label(text="", font_size=20, pos_hint={"center_x": 0.5, "center_y": 0.7})
        self.input = TextInput(multiline=False, size_hint=(0.6, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.55})
        self.feedback = Label(text="", font_size=20, pos_hint={"center_x": 0.5, "center_y": 0.25})
        self.medal_img = Image(source="", size_hint=(0.2, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.4})
        self.timer_label = Label(text="Tiempo: 20", font_size=18, pos_hint={"center_x": 0.85, "center_y": 0.9})

        check_button = Button(text="Verificar", size_hint=(0.3, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        check_button.bind(on_press=self.check_answer)

        self.add_widget(self.avatar_img)
        self.add_widget(self.question_label)
        self.add_widget(self.input)
        self.add_widget(check_button)
        self.add_widget(self.feedback)
        self.add_widget(self.medal_img)
        self.add_widget(self.timer_label)

    def set_level(self, level):
        self.level = level
        question, _ = questions[level]
        self.question_label.text = f"[{level.upper()}] {question}"
        self.input.text = ""
        self.feedback.text = ""
        self.medal_img.source = ""
        self.timer = 20
        self.timer_label.text = f"Tiempo: {self.timer}"
        self.avatar_img.source = self.avatar_path

        if self.clock_event:
            self.clock_event.cancel()
        self.clock_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.timer -= 1
        self.timer_label.text = f"Tiempo: {self.timer}"
        if self.timer <= 0:
            self.clock_event.cancel()
            self.feedback.text = "⏰ ¡Se acabó el tiempo!"
            self.input.disabled = True

    def check_answer(self, instance):
        if self.timer <= 0:
            self.feedback.text = "Tiempo agotado. Intenta de nuevo."
            return

        correct_answer = questions[self.level][1]
        user_input = self.input.text.strip().lower()
        if user_input == correct_answer:
            self.feedback.text = "¡Correcto! Has ganado una medalla 🥇"
            self.medal_img.source = "medalla_oro.png"
        else:
            self.feedback.text = "Respuesta incorrecta ❌"
            self.medal_img.source = ""

        if self.clock_event:
            self.clock_event.cancel()

class OrtotronAvataresApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AvatarScreen(name="avatar"))
        sm.add_widget(LevelScreen(name="level"))
        sm.add_widget(ExerciseScreen(name="exercise"))
        return sm

if __name__ == "__main__":
    OrtotronAvataresApp().run()
