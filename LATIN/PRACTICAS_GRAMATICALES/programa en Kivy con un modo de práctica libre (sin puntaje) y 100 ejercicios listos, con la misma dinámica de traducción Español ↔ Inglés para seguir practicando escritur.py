from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import random

# --- Lista de 100 ejercicios (Español -> Inglés)
EXERCISES = [
    ("correr", "run"),
    ("comer", "eat"),
    ("beber", "drink"),
    ("leer", "read"),
    ("escribir", "write"),
    ("hablar", "speak"),
    ("escuchar", "listen"),
    ("dormir", "sleep"),
    ("caminar", "walk"),
    ("conducir", "drive"),
    ("pensar", "think"),
    ("saber", "know"),
    ("aprender", "learn"),
    ("enseñar", "teach"),
    ("abrir", "open"),
    ("cerrar", "close"),
    ("empezar", "start"),
    ("terminar", "finish"),
    ("comprar", "buy"),
    ("vender", "sell"),
    ("pagar", "pay"),
    ("trabajar", "work"),
    ("jugar", "play"),
    ("cantar", "sing"),
    ("bailar", "dance"),
    ("mirar", "watch"),
    ("ver", "see"),
    ("llamar", "call"),
    ("esperar", "wait"),
    ("encontrar", "find"),
    ("perder", "lose"),
    ("ganar", "win"),
    ("ayudar", "help"),
    ("necesitar", "need"),
    ("querer", "want"),
    ("gustar", "like"),
    ("odiar", "hate"),
    ("sentir", "feel"),
    ("recordar", "remember"),
    ("olvidar", "forget"),
    ("llorar", "cry"),
    ("reír", "laugh"),
    ("viajar", "travel"),
    ("visitar", "visit"),
    ("conocer", "meet"),
    ("decir", "say"),
    ("contar", "tell"),
    ("responder", "answer"),
    ("preguntar", "ask"),
    ("cortar", "cut"),
    ("cocinar", "cook"),
    ("limpiar", "clean"),
    ("lavar", "wash"),
    ("subir", "go up"),
    ("bajar", "go down"),
    ("entrar", "enter"),
    ("salir", "leave"),
    ("llevar", "carry"),
    ("traer", "bring"),
    ("empujar", "push"),
    ("tirar", "pull"),
    ("romper", "break"),
    ("arreglar", "fix"),
    ("crear", "create"),
    ("usar", "use"),
    ("mover", "move"),
    ("parar", "stop"),
    ("continuar", "continue"),
    ("vivir", "live"),
    ("morir", "die"),
    ("nacer", "be born"),
    ("crecer", "grow"),
    ("caminar", "walk"),
    ("correr", "run"),
    ("saltar", "jump"),
    ("subir", "climb"),
    ("caer", "fall"),
    ("volar", "fly"),
    ("nadar", "swim"),
    ("pensar", "think"),
    ("imaginar", "imagine"),
    ("soñar", "dream"),
    ("decidir", "decide"),
    ("cambiar", "change"),
    ("quedarse", "stay"),
    ("moverse", "move"),
    ("girar", "turn"),
    ("empezar", "begin"),
    ("terminar", "end"),
    ("probar", "try"),
    ("usar", "use"),
    ("funcionar", "work"),
    ("construir", "build"),
    ("romper", "break"),
    ("arreglar", "repair"),
    ("abrir", "open"),
    ("cerrar", "shut"),
    ("luchar", "fight"),
    ("ganar", "earn"),
    ("perder", "miss"),
    ("enviar", "send"),
    ("recibir", "receive"),
]

class PracticeApp(App):
    def build(self):
        self.current_ex = None

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.label = Label(text="Presiona 'Nuevo' para comenzar", font_size=22, size_hint_y=None, height=60)
        layout.add_widget(self.label)

        self.input = TextInput(hint_text="Escribe la traducción aquí", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.input)

        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.check_btn = Button(text="Verificar", on_press=self.check_answer)
        self.next_btn = Button(text="Nuevo", on_press=self.new_exercise)
        button_layout.add_widget(self.check_btn)
        button_layout.add_widget(self.next_btn)
        layout.add_widget(button_layout)

        self.feedback = Label(text="", font_size=18)
        layout.add_widget(self.feedback)

        return layout

    def new_exercise(self, instance):
        self.current_ex = random.choice(EXERCISES)
        self.label.text = f"Traduce al inglés: {self.current_ex[0]}"
        self.input.text = ""
        self.feedback.text = ""

    def check_answer(self, instance):
        if not self.current_ex:
            return
        user_ans = self.input.text.strip().lower()
        correct = self.current_ex[1].lower()
        if user_ans == correct:
            self.feedback.text = "✅ Correcto!"
        else:
            self.feedback.text = f"❌ Incorrecto. Respuesta: {correct}"

if __name__ == "__main__":
    PracticeApp().run()
