import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Diccionario con ejemplos de oraciones simples
types_of_sentences = {
    "Declarative": ["I like apples.", "She is a teacher.", "They play soccer."],
    "Interrogative": ["Do you like pizza?", "Is he your brother?", "Can we go now?"],
    "Imperative": ["Close the door.", "Please sit down.", "Open your book."],
    "Exclamatory": ["What a beautiful day!", "How fast he runs!", "That’s amazing!"],
}

class SentenceTrainer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.current_type = None
        self.current_sentence = None

        self.label = Label(text="Choose a type of sentence to practice", font_size=20)
        self.add_widget(self.label)

        # Botones de menú
        self.buttons_layout = BoxLayout(size_hint_y=0.2, spacing=5)
        for stype in types_of_sentences.keys():
            btn = Button(text=stype)
            btn.bind(on_press=self.select_type)
            self.buttons_layout.add_widget(btn)

        btn_mixed = Button(text="Mixed")
        btn_mixed.bind(on_press=self.mixed_mode)
        self.buttons_layout.add_widget(btn_mixed)

        self.add_widget(self.buttons_layout)

        # Campo de entrada y botón de verificación
        self.input_field = TextInput(hint_text="Write the sentence here", multiline=False, size_hint_y=0.2)
        self.add_widget(self.input_field)

        self.check_button = Button(text="Check", size_hint_y=0.2)
        self.check_button.bind(on_press=self.check_answer)
        self.add_widget(self.check_button)

        self.feedback = Label(text="", font_size=18)
        self.add_widget(self.feedback)

    def select_type(self, instance):
        self.current_type = instance.text
        self.current_sentence = random.choice(types_of_sentences[self.current_type])
        self.label.text = f"Write this {self.current_type} sentence: {self.current_sentence}".replace(self.current_sentence, "...")
        self.feedback.text = ""
        self.input_field.text = ""

    def mixed_mode(self, instance):
        self.current_type = random.choice(list(types_of_sentences.keys()))
        self.current_sentence = random.choice(types_of_sentences[self.current_type])
        self.label.text = f"Write this {self.current_type} sentence: ..."
        self.feedback.text = ""
        self.input_field.text = ""

    def check_answer(self, instance):
        user_answer = self.input_field.text.strip()
        if user_answer == self.current_sentence:
            self.feedback.text = "✅ Correct!"
        else:
            self.feedback.text = f"❌ Incorrect. The correct sentence is: {self.current_sentence}"

class SentenceTrainerApp(App):
    def build(self):
        return SentenceTrainer()

if __name__ == "__main__":
    SentenceTrainerApp().run()
