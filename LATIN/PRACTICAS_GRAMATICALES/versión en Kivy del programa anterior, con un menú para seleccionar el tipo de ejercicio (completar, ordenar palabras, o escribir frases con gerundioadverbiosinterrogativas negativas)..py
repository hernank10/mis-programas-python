from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

# ---------------------
# Banco de ejercicios
# ---------------------
complete_sentences = [
    {"question": "She ____ playing the guitar.", "answer": "is"},
    {"question": "They are ____ dinner now.", "answer": "having"},
    {"question": "He runs very ___.", "answer": "fast"},
]

order_words = [
    {"words": ["not", "are", "they", "coming"], "answer": "They are not coming."},
    {"words": ["working", "is", "she", "hard"], "answer": "She is working hard."},
]

unscramble_sentences = [
    {"words": ["Why", "not", "is", "he", "studying"], "answer": "Why is he not studying?"},
    {"words": ["She", "is", "quickly", "running"], "answer": "She is running quickly."},
]

# ---------------------
# Interfaz principal
# ---------------------
class GrammarApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Choose an exercise:")
        self.layout.add_widget(self.label)

        btn1 = Button(text="Complete the sentence")
        btn1.bind(on_press=self.complete_sentence)
        self.layout.add_widget(btn1)

        btn2 = Button(text="Order the words")
        btn2.bind(on_press=self.order_words_ex)
        self.layout.add_widget(btn2)

        btn3 = Button(text="Unscramble the sentence")
        btn3.bind(on_press=self.unscramble_ex)
        self.layout.add_widget(btn3)

        self.exercise_label = Label(text="")
        self.layout.add_widget(self.exercise_label)

        self.input = TextInput(hint_text="Write your answer here", multiline=False)
        self.layout.add_widget(self.input)

        self.submit_btn = Button(text="Submit")
        self.submit_btn.bind(on_press=self.check_answer)
        self.layout.add_widget(self.submit_btn)

        self.feedback = Label(text="")
        self.layout.add_widget(self.feedback)

        self.current_answer = ""
        return self.layout

    def complete_sentence(self, instance):
        ex = random.choice(complete_sentences)
        self.exercise_label.text = ex["question"]
        self.current_answer = ex["answer"]
        self.feedback.text = ""
        self.input.text = ""

    def order_words_ex(self, instance):
        ex = random.choice(order_words)
        self.exercise_label.text = "Arrange the words: " + " ".join(ex["words"])
        self.current_answer = ex["answer"]
        self.feedback.text = ""
        self.input.text = ""

    def unscramble_ex(self, instance):
        ex = random.choice(unscramble_sentences)
        self.exercise_label.text = "Unscramble: " + " ".join(ex["words"])
        self.current_answer = ex["answer"]
        self.feedback.text = ""
        self.input.text = ""

    def check_answer(self, instance):
        user_answer = self.input.text.strip()
        if user_answer.lower() == self.current_answer.lower():
            self.feedback.text = "✅ Correct!"
        else:
            self.feedback.text = f"❌ Incorrect. Correct answer: {self.current_answer}"


if __name__ == "__main__":
    GrammarApp().run()
