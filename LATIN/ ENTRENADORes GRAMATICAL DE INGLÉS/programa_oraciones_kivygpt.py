from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import random

# Diccionario con tipos de oraciones y ejemplos
oraciones = {
    "Simple": {"es": "Ella estudia todos los días.", "en": "She studies every day."},
    "Compuesta": {"es": "Quería ir al parque, pero empezó a llover.", "en": "I wanted to go to the park, but it started to rain."},
    "Compleja": {"es": "Me quedé en casa porque estaba cansado.", "en": "I stayed home because I was tired."},
    "Compuesta-compleja": {"es": "Me quedé en casa porque estaba cansado, y mi amigo fue a la fiesta.", "en": "I stayed home because I was tired, and my friend went to the party."},
    "Afirmativa": {"es": "Ella toca el piano.", "en": "She plays the piano."},
    "Negativa": {"es": "Ella no toca el piano.", "en": "She does not play the piano."},
    "Interrogativa": {"es": "¿Ella toca el piano?", "en": "Does she play the piano?"},
    "Imperativa": {"es": "Cierra la puerta.", "en": "Close the door."}
}

# Variable global de puntuación
puntuacion = {"correctas": 0, "intentos": 0}

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        layout.add_widget(Label(text="MENÚ PRINCIPAL", font_size=24))

        btn_tabla = Button(text="Ver tabla comparativa", on_press=self.ver_tabla)
        btn_practicar = Button(text="Practicar oraciones", on_press=self.practicar)
        btn_puntuacion = Button(text="Ver puntuación", on_press=self.ver_puntuacion)
        btn_salir = Button(text="Salir", on_press=lambda x: App.get_running_app().stop())

        layout.add_widget(btn_tabla)
        layout.add_widget(btn_practicar)
        layout.add_widget(btn_puntuacion)
        layout.add_widget(btn_salir)
        self.add_widget(layout)

    def ver_tabla(self, instance):
        self.manager.current = "tabla"

    def practicar(self, instance):
        self.manager.get_screen("practica").nueva_pregunta()
        self.manager.current = "practica"

    def ver_puntuacion(self, instance):
        self.manager.get_screen("puntuacion").actualizar()
        self.manager.current = "puntuacion"


class TablaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=3, spacing=5, padding=10)
        layout.add_widget(Label(text="[b]Tipo[/b]", markup=True))
        layout.add_widget(Label(text="[b]Español[/b]", markup=True))
        layout.add_widget(Label(text="[b]Inglés[/b]", markup=True))

        for tipo, ejemplos in oraciones.items():
            layout.add_widget(Label(text=tipo))
            layout.add_widget(Label(text=ejemplos["es"]))
            layout.add_widget(Label(text=ejemplos["en"]))

        btn_volver = Button(text="Volver al menú", size_hint_y=None, height=50,
                            on_press=lambda x: self.manager.current = "menu")
        root = BoxLayout(orientation="vertical")
        root.add_widget(layout)
        root.add_widget(btn_volver)
        self.add_widget(root)


class PracticaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = None
        self.direccion = None

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.enunciado = Label(text="Aquí aparecerá la oración", font_size=18)
        self.input_respuesta = TextInput(hint_text="Escribe tu respuesta aquí", multiline=False)
        self.resultado = Label(text="")
        btn_verificar = Button(text="Verificar respuesta", on_press=self.verificar)
        btn_volver = Button(text="Volver al menú", on_press=lambda x: self.manager.current == "menu")

        self.layout.add_widget(self.enunciado)
        self.layout.add_widget(self.input_respuesta)
        self.layout.add_widget(btn_verificar)
        self.layout.add_widget(self.resultado)
        self.layout.add_widget(btn_volver)
        self.add_widget(self.layout)

    def nueva_pregunta(self):
        self.tipo = random.choice(list(oraciones.keys()))
        self.direccion = random.choice(["es", "en"])
        if self.direccion == "es":
            self.enunciado.text = f"Traduce al ESPAÑOL: {oraciones[self.tipo]['en']}"
        else:
            self.enunciado.text = f"Translate into ENGLISH: {oraciones[self.tipo]['es']}"
        self.input_respuesta.text = ""
        self.resultado.text = ""

    def verificar(self, instance):
        respuesta = self.input_respuesta.text.strip()
        correcta = oraciones[self.tipo]["es"] if self.direccion == "es" else oraciones[self.tipo]["en"]

        puntuacion["intentos"] += 1
        if respuesta.lower() == correcta.lower():
            self.resultado.text = "✅ ¡Correcto!"
            puntuacion["correctas"] += 1
        else:
            self.resultado.text = f"❌ Incorrecto. Respuesta correcta: {correcta}"


class PuntuacionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="")
        btn_volver = Button(text="Volver al menú", on_press=lambda x: self.manager.current == "menu")
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        layout.add_widget(self.label)
        layout.add_widget(btn_volver)
        self.add_widget(layout)

    def actualizar(self):
        correctas = puntuacion["correctas"]
        intentos = puntuacion["intentos"]
        self.label.text = f"Puntuación: {correctas}/{intentos} respuestas correctas"


class OracionesApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(TablaScreen(name="tabla"))
        sm.add_widget(PracticaScreen(name="practica"))
        sm.add_widget(PuntuacionScreen(name="puntuacion"))
        return sm


if __name__ == "__main__":
    OracionesApp().run()
