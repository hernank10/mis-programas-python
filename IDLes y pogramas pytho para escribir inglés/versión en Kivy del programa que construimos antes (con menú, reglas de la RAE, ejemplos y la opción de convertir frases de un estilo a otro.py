from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# -------------------------
# Datos del programa
# -------------------------
reglas_rae = [
    "El 'si' sin tilde introduce una condición (conjunción condicional).",
    "El 'sí' con tilde funciona como adverbio de afirmación o pronombre reflexivo.",
    "La expresión 'por más que' introduce una idea concesiva.",
    "Se deben evitar redundancias o cruces ilógicos en condicionales y concesivas.",
    "El verbo debe concordar con el sujeto explícito o tácito." 
]

ejemplos = {
    "Condicionales": [
        "Si estudias, aprobarás.",
        "Si corres rápido, ganarás la carrera.",
        "Si llueve, no iremos al parque."
    ],
    "Concesivas": [
        "Por más que llores, no cambiarás mi decisión.",
        "Aunque grites, no te escucharán.",
        "Aun cuando estudies, el examen será difícil."
    ]
}

# Conversión básica de frases
def convertir_frase(frase):
    if frase.startswith("Por más que"):
        return frase.replace("Por más que", "Si", 1)
    elif frase.startswith("Si"):
        return frase.replace("Si", "Por más que", 1)
    else:
        return "No se pudo convertir automáticamente."

# -------------------------
# Pantallas
# -------------------------
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        btn1 = Button(text="📘 Ver Reglas RAE")
        btn1.bind(on_press=lambda x: self.manager.current_screen.show_rules())
        btn1.bind(on_release=lambda x: setattr(self.manager, 'current', 'reglas'))

        btn2 = Button(text="📝 Ver Ejemplos")
        btn2.bind(on_release=lambda x: setattr(self.manager, 'current', 'ejemplos'))

        btn3 = Button(text="🔄 Convertir Frase")
        btn3.bind(on_release=lambda x: setattr(self.manager, 'current', 'convertir'))

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        self.add_widget(layout)

class ReglasScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        for r in reglas_rae:
            content.add_widget(Label(text=r, size_hint_y=None, height=40))

        scroll.add_widget(content)
        layout.add_widget(scroll)
        layout.add_widget(Button(text="⬅ Volver", size_hint_y=None, height=50,
                                 on_release=lambda x: setattr(self.manager, 'current', 'menu')))
        self.add_widget(layout)

class EjemplosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        for categoria, frases in ejemplos.items():
            content.add_widget(Label(text=f"[b]{categoria}[/b]", markup=True, size_hint_y=None, height=40))
            for f in frases:
                content.add_widget(Label(text=f, size_hint_y=None, height=30))

        scroll.add_widget(content)
        layout.add_widget(scroll)
        layout.add_widget(Button(text="⬅ Volver", size_hint_y=None, height=50,
                                 on_release=lambda x: setattr(self.manager, 'current', 'menu')))
        self.add_widget(layout)

class ConvertirScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.entrada = TextInput(hint_text="Escribe una frase para convertir", multiline=False)
        self.resultado = Label(text="Resultado aparecerá aquí")
        self.btn_convertir = Button(text="Convertir", size_hint_y=None, height=50)
        self.btn_convertir.bind(on_release=self.convertir)

        self.layout.add_widget(self.entrada)
        self.layout.add_widget(self.btn_convertir)
        self.layout.add_widget(self.resultado)
        self.layout.add_widget(Button(text="⬅ Volver", size_hint_y=None, height=50,
                                      on_release=lambda x: setattr(self.manager, 'current', 'menu')))
        self.add_widget(self.layout)

    def convertir(self, instance):
        frase = self.entrada.text.strip()
        self.resultado.text = convertir_frase(frase)

# -------------------------
# App Principal
# -------------------------
class FrasesApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ReglasScreen(name='reglas'))
        sm.add_widget(EjemplosScreen(name='ejemplos'))
        sm.add_widget(ConvertirScreen(name='convertir'))
        return sm

if __name__ == '__main__':
    FrasesApp().run()
