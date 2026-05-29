from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
import random

# Datos de conectores
conectores = {
    "Adición": {
        "ejemplos": ["además", "también", "incluso", "asimismo"],
        "consejos": [
            "Usa 'además' para sumar ideas relacionadas.",
            "Evita repetir 'también' varias veces.",
            "Prefiere 'asimismo' en contextos formales.",
            "Usa 'incluso' para enfatizar lo inesperado."
        ]
    },
    "Contraste": {
        "ejemplos": ["pero", "aunque", "sin embargo", "no obstante"],
        "consejos": [
            "Usa 'pero' para introducir una objeción ligera.",
            "'Sin embargo' indica oposición con más fuerza.",
            "No combines 'pero' con 'sin embargo'.",
            "'Aunque' introduce una idea opuesta dentro de una oración."
        ]
    },
    "Causa": {
        "ejemplos": ["porque", "ya que", "dado que", "debido a que"],
        "consejos": [
            "Usa 'porque' para causas claras.",
            "Prefiere 'dado que' en textos académicos.",
            "'Debido a que' necesita un verbo después.",
            "Evita usar 'por' como si fuera 'porque'."
        ]
    },
    "Consecuencia": {
        "ejemplos": ["por eso", "por lo tanto", "en consecuencia", "así que"],
        "consejos": [
            "Usa 'por eso' en lenguaje informal.",
            "'Por lo tanto' es ideal para argumentar.",
            "'En consecuencia' es perfecto para cerrar ideas.",
            "Evita usar 'entonces' sin lógica clara."
        ]
    }
}

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text="Aprende Conectores Discursivos", font_size=24))

        layout.add_widget(Button(text="1. Estudiar consejos", size_hint_y=None, height=60,
                                 on_press=lambda x: self.show_text("Consejos", self.get_consejos())))
        layout.add_widget(Button(text="2. Ver ejemplos", size_hint_y=None, height=60,
                                 on_press=lambda x: self.show_text("Ejemplos", self.get_ejemplos())))
        layout.add_widget(Button(text="3. Practicar", size_hint_y=None, height=60,
                                 on_press=lambda x: self.manager.current = 'practice'))
        layout.add_widget(Button(text="Salir", size_hint_y=None, height=60,
                                 on_press=lambda x: App.get_running_app().stop()))

        self.add_widget(layout)

    def get_consejos(self):
        texto = ""
        for tipo, data in conectores.items():
            texto += f"\n🔹 {tipo}:\n"
            for consejo in data["consejos"]:
                texto += f" - {consejo}\n"
        return texto

    def get_ejemplos(self):
        texto = ""
        for tipo, data in conectores.items():
            texto += f"\n🔸 {tipo}: {', '.join(data['ejemplos'])}"
        return texto

    def show_text(self, title, content):
        box = BoxLayout(orientation='vertical')
        scroll = ScrollView()
        label = Label(text=content, size_hint_y=None)
        label.bind(texture_size=label.setter('size'))
        scroll.add_widget(label)
        box.add_widget(scroll)
        popup = Popup(title=title, content=box, size_hint=(0.9, 0.9))
        popup.open()


class PracticeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.add_widget(self.layout)
        self.puntos = 0
        self.contador = 0
        self.siguiente_pregunta()

    def siguiente_pregunta(self):
        self.layout.clear_widgets()
        if self.contador >= 5:
            popup = Popup(title="Resultado",
                          content=Label(text=f"Puntaje: {self.puntos}/5"),
                          size_hint=(0.6, 0.4))
            popup.open()
            self.manager.current = 'main'
            return

        self.tipo, data = random.choice(list(conectores.items()))
        self.ejemplo = random.choice(data['ejemplos'])
        opciones = random.sample(list(conectores.keys()), 3)
        if self.tipo not in opciones:
            opciones[random.randint(0, 2)] = self.tipo
        random.shuffle(opciones)

        self.layout.add_widget(Label(text=f"¿A qué tipo pertenece '{self.ejemplo}'?", font_size=20))

        for op in opciones:
            btn = Button(text=op, size_hint_y=None, height=60,
                         on_press=lambda b, o=op: self.responder(o))
            self.layout.add_widget(btn)

    def responder(self, seleccion):
        if seleccion == self.tipo:
            self.puntos += 1
        self.contador += 1
        self.siguiente_pregunta()


class ConectoresApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(PracticeScreen(name='practice'))
        return sm


if __name__ == '__main__':
    ConectoresApp().run()
