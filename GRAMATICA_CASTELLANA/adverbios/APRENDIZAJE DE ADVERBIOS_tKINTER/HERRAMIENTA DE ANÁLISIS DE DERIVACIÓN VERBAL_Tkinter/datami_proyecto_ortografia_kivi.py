import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
import os

EJEMPLOS_FILE = "ejemplos.json"
PROGRESO_FILE = "progreso.json"

# Estructura de datos
if not os.path.exists(EJEMPLOS_FILE):
    with open(EJEMPLOS_FILE, "w") as f:
        json.dump([], f)

if not os.path.exists(PROGRESO_FILE):
    with open(PROGRESO_FILE, "w") as f:
        json.dump({}, f)

def cargar_ejemplos():
    with open(EJEMPLOS_FILE, "r") as f:
        return json.load(f)

def guardar_ejemplos(ejemplos):
    with open(EJEMPLOS_FILE, "w") as f:
        json.dump(ejemplos, f, indent=2)

def cargar_progreso():
    with open(PROGRESO_FILE, "r") as f:
        return json.load(f)

def guardar_progreso(progreso):
    with open(PROGRESO_FILE, "w") as f:
        json.dump(progreso, f, indent=2)

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text="Practicar reglas", on_press=self.ir_practica))
        layout.add_widget(Button(text="Agregar ejemplo", on_press=self.ir_agregar))
        layout.add_widget(Button(text="Ver progreso", on_press=self.ir_progreso))
        self.add_widget(layout)

    def ir_practica(self, instance):
        self.manager.current = "practica"

    def ir_agregar(self, instance):
        self.manager.current = "agregar"

    def ir_progreso(self, instance):
        self.manager.current = "progreso"

class AgregarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.input_palabra = TextInput(hint_text="Palabra")
        self.input_afi = TextInput(hint_text="AFI")
        self.input_regla = TextInput(hint_text="Regla ortográfica")
        self.input_tema = TextInput(hint_text="Tema")

        self.layout.add_widget(self.input_palabra)
        self.layout.add_widget(self.input_afi)
        self.layout.add_widget(self.input_regla)
        self.layout.add_widget(self.input_tema)

        self.layout.add_widget(Button(text="Guardar", on_press=self.guardar))
        self.layout.add_widget(Button(text="Volver", on_press=self.volver))
        self.add_widget(self.layout)

    def guardar(self, instance):
        palabra = self.input_palabra.text
        afi = self.input_afi.text
        regla = self.input_regla.text
        tema = self.input_tema.text
        ejemplos = cargar_ejemplos()
        ejemplos.append({"palabra": palabra, "afi": afi, "regla": regla, "tema": tema})
        guardar_ejemplos(ejemplos)
        self.input_palabra.text = ""
        self.input_afi.text = ""
        self.input_regla.text = ""
        self.input_tema.text = ""

    def volver(self, instance):
        self.manager.current = "menu"

class PracticaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.tema_spinner = Spinner(text="Elige un tema", values=())
        self.label = Label(text="")
        self.input = TextInput(hint_text="Escribe la palabra")
        self.resultado = Label(text="")
        self.boton_verificar = Button(text="Verificar", on_press=self.verificar)
        self.boton_volver = Button(text="Volver", on_press=self.volver)

        self.layout.add_widget(self.tema_spinner)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.boton_verificar)
        self.layout.add_widget(self.resultado)
        self.layout.add_widget(self.boton_volver)
        self.add_widget(self.layout)
        self.ejemplo_actual = None
        self.tema_spinner.bind(text=self.actualizar_tema)
        self.ejemplos_por_tema = self.organizar_por_tema()
        self.tema_spinner.values = list(self.ejemplos_por_tema.keys())

    def organizar_por_tema(self):
        ejemplos = cargar_ejemplos()
        por_tema = {}
        for ej in ejemplos:
            por_tema.setdefault(ej['tema'], []).append(ej)
        return por_tema

    def actualizar_tema(self, spinner, texto):
        if texto in self.ejemplos_por_tema:
            import random
            self.ejemplo_actual = random.choice(self.ejemplos_por_tema[texto])
            self.label.text = f"AFI: {self.ejemplo_actual['afi']}\nRegla: {self.ejemplo_actual['regla']}"
            self.input.text = ""
            self.resultado.text = ""

    def verificar(self, instance):
        if self.ejemplo_actual:
            palabra_correcta = self.ejemplo_actual['palabra']
            entrada = self.input.text.strip()
            progreso = cargar_progreso()
            key = palabra_correcta
            if entrada.lower() == palabra_correcta.lower():
                self.resultado.text = "¡Correcto!"
                progreso[key] = progreso.get(key, 0) + 1
            else:
                self.resultado.text = f"Incorrecto. Era: {palabra_correcta}"
                progreso[key] = progreso.get(key, 0) - 1
            guardar_progreso(progreso)

    def volver(self, instance):
        self.manager.current = "menu"

class ProgresoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        scroll = ScrollView()
        progreso = cargar_progreso()
        contenido = BoxLayout(orientation='vertical', size_hint_y=None)
        contenido.bind(minimum_height=contenido.setter('height'))

        for palabra, puntos in progreso.items():
            contenido.add_widget(Label(text=f"{palabra}: {puntos} pts"))

        scroll.add_widget(contenido)
        layout.add_widget(scroll)
        layout.add_widget(Button(text="Volver", on_press=self.volver))
        self.add_widget(layout)

    def volver(self, instance):
        self.manager.current = "menu"

class OrtografiaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(AgregarScreen(name="agregar"))
        sm.add_widget(PracticaScreen(name="practica"))
        sm.add_widget(ProgresoScreen(name="progreso"))
        return sm

if __name__ == '__main__':
    OrtografiaApp().run()
