from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import choice

# Banco de ejercicios por tipo de oración
ejercicios = {
    "Enunciativa afirmativa": [
        ("Hoy ___ un gran día.", "Hoy es un gran día."),
        ("Los estudiantes ___ su tarea.", "Los estudiantes hicieron su tarea.")
    ],
    "Enunciativa negativa": [
        ("No ___ a clase ayer.", "No fui a clase ayer."),
        ("Ella no ___ la ventana.", "Ella no cerró la ventana.")
    ],
    "Interrogativa directa": [
        ("¿___ vendrás mañana?", "¿Tú vendrás mañana?"),
        ("¿A qué hora ___ el tren?", "¿A qué hora llega el tren?")
    ],
    "Interrogativa indirecta": [
        ("No sé si ___ al cine.", "No sé si iré al cine."),
        ("Me pregunto cuándo ___ la lluvia.", "Me pregunto cuándo parará la lluvia.")
    ],
    "Exclamativa": [
        ("¡___ maravilla!", "¡Qué maravilla!"),
        ("¡___ rápido corres!", "¡Qué rápido corres!")
    ],
    "Imperativa": [
        ("___ la puerta, por favor.", "Cierra la puerta, por favor."),
        ("___ silencio en clase.", "Guarden silencio en clase.")
    ],
    "Desiderativa": [
        ("Ojalá ___ a tiempo.", "Ojalá llegues a tiempo."),
        ("Quisiera que todo ___ bien.", "Quisiera que todo salga bien.")
    ],
    "Dubitativa": [
        ("Tal vez ___ mañana.", "Tal vez llueva mañana."),
        ("Quizá ___ estudiar más.", "Quizá deba estudiar más.")
    ]
}

class OracionApp(App):
    def build(self):
        self.title = "Práctica de oraciones simples"
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.label = Label(text="Selecciona un tipo de oración", font_size=20)
        self.layout.add_widget(self.label)

        # Botones de selección
        for tipo in ejercicios:
            btn = Button(text=tipo, size_hint_y=None, height=40)
            btn.bind(on_press=self.mostrar_ejercicio)
            self.layout.add_widget(btn)

        self.ejemplo = Label(text="", font_size=18)
        self.layout.add_widget(self.ejemplo)

        self.entrada = TextInput(hint_text="Escribe la oración completa", size_hint_y=None, height=40)
        self.layout.add_widget(self.entrada)

        self.btn_verificar = Button(text="Verificar respuesta", size_hint_y=None, height=40)
        self.btn_verificar.bind(on_press=self.verificar_respuesta)
        self.layout.add_widget(self.btn_verificar)

        self.resultado = Label(text="", font_size=18)
        self.layout.add_widget(self.resultado)

        self.tipo_actual = ""
        self.correcta = ""

        return self.layout

    def mostrar_ejercicio(self, instance):
        self.tipo_actual = instance.text
        ejemplo, self.correcta = choice(ejercicios[self.tipo_actual])
        self.ejemplo.text = f"Completa la oración:\n{ejemplo}"
        self.entrada.text = ""
        self.resultado.text = ""

    def verificar_respuesta(self, instance):
        user_input = self.entrada.text.strip()
        if user_input.lower() == self.correcta.lower():
            self.resultado.text = "✅ ¡Correcto!"
        else:
            self.resultado.text = f"❌ Incorrecto. Respuesta esperada:\n{self.correcta}"

if __name__ == '__main__':
    OracionApp().run()
