import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# ------------------ Datos ------------------
plurales_regulares = {
    "dog": "dogs",
    "book": "books",
    "car": "cars"
}

plurales_irregulares = {
    "child": "children",
    "mouse": "mice",
    "man": "men"
}

comparativos_regulares = {
    "big": ("bigger", "biggest"),
    "small": ("smaller", "smallest"),
    "tall": ("taller", "tallest")
}

comparativos_irregulares = {
    "good": ("better", "best"),
    "bad": ("worse", "worst"),
    "far": ("farther", "farthest")
}


# ------------------ Pantallas ------------------
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        layout.add_widget(Label(text="Grammar Trainer", font_size=32))

        btns = [
            ("Plurales regulares", "plurales_reg"),
            ("Plurales irregulares", "plurales_irr"),
            ("Comparativos regulares", "comp_reg"),
            ("Comparativos irregulares", "comp_irr"),
            ("Ejercicios mixtos", "mixtos"),
        ]

        for text, screen in btns:
            b = Button(text=text, size_hint=(1, 0.2))
            b.bind(on_release=lambda x, s=screen: self.go_to(s))
            layout.add_widget(b)

        self.add_widget(layout)

    def go_to(self, screen_name):
        self.manager.current = screen_name


class ExerciseScreen(Screen):
    def __init__(self, data, mode="plurales", **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.mode = mode
        self.words = list(data.keys())
        self.current_word = None
        self.score = 0

        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        self.word_label = Label(text="", font_size=28)
        self.layout.add_widget(self.word_label)

        self.input = TextInput(hint_text="Escribe tu respuesta", multiline=False, font_size=24)
        self.layout.add_widget(self.input)

        self.result_label = Label(text="", font_size=20)
        self.layout.add_widget(self.result_label)

        self.check_btn = Button(text="Check", size_hint=(1, 0.2))
        self.check_btn.bind(on_release=self.check_answer)
        self.layout.add_widget(self.check_btn)

        self.next_btn = Button(text="Next", size_hint=(1, 0.2))
        self.next_btn.bind(on_release=self.next_question)
        self.layout.add_widget(self.next_btn)

        self.score_label = Label(text="Score: 0", font_size=20)
        self.layout.add_widget(self.score_label)

        self.add_widget(self.layout)
        self.next_question()

    def next_question(self, *args):
        self.current_word = random.choice(self.words)
        self.word_label.text = f"Word: {self.current_word}"
        self.input.text = ""
        self.result_label.text = ""

    def check_answer(self, *args):
        user_answer = self.input.text.strip().lower()

        if self.mode == "comparativos":
            correct = self.data[self.current_word]
            if user_answer in correct:
                self.result_label.text = "✅ Correct!"
                self.score += 1
            else:
                self.result_label.text = f"❌ Incorrect. Correct: {correct[0]}, {correct[1]}"
        else:
            correct = self.data[self.current_word]
            if user_answer == correct:
                self.result_label.text = "✅ Correct!"
                self.score += 1
            else:
                self.result_label.text = f"❌ Incorrect. Correct: {correct}"

        self.score_label.text = f"Score: {self.score}"


class MixedExerciseScreen(ExerciseScreen):
    def __init__(self, **kwargs):
        all_data = {
            "plurales_regulares": plurales_regulares,
            "plurales_irregulares": plurales_irregulares,
            "comparativos_regulares": comparativos_regulares,
            "comparativos_irregulares": comparativos_irregulares,
        }
        self.all_data = all_data
        super().__init__({}, mode="mixed", **kwargs)

    def next_question(self, *args):
        category = random.choice(list(self.all_data.keys()))
        self.mode = "comparativos" if "comparativos" in category else "plurales"
        self.data = self.all_data[category]
        self.words = list(self.data.keys())
        self.current_word = random.choice(self.words)
        self.word_label.text = f"Word: {self.current_word}"
        self.input.text = ""
        self.result_label.text = ""


# ------------------ App ------------------
class GrammarApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(ExerciseScreen(plurales_regulares, mode="plurales", name="plurales_reg"))
        sm.add_widget(ExerciseScreen(plurales_irregulares, mode="plurales", name="plurales_irr"))
        sm.add_widget(ExerciseScreen(comparativos_regulares, mode="comparativos", name="comp_reg"))
        sm.add_widget(ExerciseScreen(comparativos_irregulares, mode="comparativos", name="comp_irr"))
        sm.add_widget(MixedExerciseScreen(name="mixtos"))

        return sm


if __name__ == "__main__":
    GrammarApp().run()
