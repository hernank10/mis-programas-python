# Programa de práctica de consejos gramaticales con Kivy
# Nuevo modo: mostrar primero el consejo y luego pedir que lo escriban

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

# Listas de consejos (ejemplo, deberás completar con los 200)
consejos_es = [
    "Coloca siempre los adjetivos antes de los sustantivos en inglés.",
    "Aprende el orden común de los adjetivos: opinión, tamaño, edad, forma, color, origen, material, propósito.",
    "Ejemplo: una hermosa mesa grande, redonda, roja, italiana, de madera para comer.",
]

consejos_en = [
    "Always place adjectives before nouns in English.",
    "Learn common adjective order: opinion, size, age, shape, color, origin, material, purpose.",
    "Example: a beautiful big old round red Italian wooden dining table.",
]

# Pantalla de Menú
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        layout.add_widget(Label(text="MENÚ PRINCIPAL", font_size=28))

        # Modo normal (escribir directamente)
        btn_es = Button(text="Practicar consejos en Español (modo directo)", size_hint=(1, 0.2))
        btn_es.bind(on_press=lambda x: self.manager.get_screen("practica").iniciar(consejos_es, "Español", mostrar_antes=False))
        layout.add_widget(btn_es)

        btn_en = Button(text="Practicar consejos en Inglés (modo directo)", size_hint=(1, 0.2))
        btn_en.bind(on_press=lambda x: self.manager.get_screen("practica").iniciar(consejos_en, "Inglés", mostrar_antes=False))
        layout.add_widget(btn_en)

        # Nuevo modo guiado (primero mostrar consejo, luego pedirlo)
        btn_es_guiado = Button(text="Practicar consejos en Español (modo guiado)", size_hint=(1, 0.2))
        btn_es_guiado.bind(on_press=lambda x: self.manager.get_screen("practica").iniciar(consejos_es, "Español", mostrar_antes=True))
        layout.add_widget(btn_es_guiado)

        btn_en_guiado = Button(text="Practicar consejos en Inglés (modo guiado)", size_hint=(1, 0.2))
        btn_en_guiado.bind(on_press=lambda x: self.manager.get_screen("practica").iniciar(consejos_en, "Inglés", mostrar_antes=True))
        layout.add_widget(btn_en_guiado)

        btn_exit = Button(text="Salir", size_hint=(1, 0.2))
        btn_exit.bind(on_press=lambda x: App.get_running_app().stop())
        layout.add_widget(btn_exit)

        self.add_widget(layout)

# Pantalla de Práctica
class PracticaScreen(Screen):
    def __init__(self, **kwargs):
        super(PracticaScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.titulo = Label(text="", font_size=24)
        self.layout.add_widget(self.titulo)

        self.consejo_label = Label(text="", font_size=18)
        self.layout.add_widget(self.consejo_label)

        self.input_text = TextInput(multiline=False, font_size=18, size_hint=(1, 0.2))
        self.layout.add_widget(self.input_text)

        self.btn_check = Button(text="Verificar", size_hint=(1, 0.2))
        self.btn_check.bind(on_press=self.verificar)
        self.layout.add_widget(self.btn_check)

        self.resultado = Label(text="", font_size=18)
        self.layout.add_widget(self.resultado)

        self.puntuacion_label = Label(text="Puntuación: 0", font_size=18)
        self.layout.add_widget(self.puntuacion_label)

        self.btn_volver = Button(text="Volver al menú", size_hint=(1, 0.2))
        self.btn_volver.bind(on_press=lambda x: self.manager.current == "menu")
        self.layout.add_widget(self.btn_volver)

        self.add_widget(self.layout)

        # Variables de control
        self.consejos = []
        self.index = 0
        self.puntuacion = 0
        self.modo_guiado = False
        self.mostrado = False  # indica si ya se mostró el consejo antes de pedirlo

    def iniciar(self, lista_consejos, idioma, mostrar_antes):
        self.consejos = lista_consejos
        self.index = 0
        self.puntuacion = 0
        self.modo_guiado = mostrar_antes
        self.mostrado = False
        self.titulo.text = f"Practicando consejos en {idioma}"
        self.btn_check.text = "Continuar"
        self.mostrar_consejo()
        self.manager.current = "practica"

    def mostrar_consejo(self):
        if self.index < len(self.consejos):
            self.consejo_actual = self.consejos[self.index]
            if self.modo_guiado and not self.mostrado:
                # Mostrar primero el consejo, sin pedir escribir aún
                self.consejo_label.text = f"Consejo {self.index + 1}:\n{self.consejo_actual}"
                self.input_text.text = ""
                self.input_text.disabled = True
                self.btn_check.text = "Listo, escribir"
                self.resultado.text = ""
                self.mostrado = True
            else:
                # Ahora pedir escribir el consejo
                self.consejo_label.text = f"Consejo {self.index + 1}: Escribe exactamente como aparecía"
                self.input_text.text = ""
                self.input_text.disabled = False
                self.btn_check.text = "Verificar"
                self.resultado.text = ""
                self.mostrado = False
        else:
            self.consejo_label.text = "¡Has completado todos los consejos!"
            self.btn_check.disabled = True

    def verificar(self, instance):
        if self.modo_guiado and self.mostrado:
            # Si estaba mostrando el consejo, ahora lo oculta y pide escritura
            self.mostrar_consejo()
        else:
            respuesta = self.input_text.text.strip()
            if respuesta == self.consejo_actual:
                self.resultado.text = "✅ Correcto"
                self.puntuacion += 1
            else:
                self.resultado.text = f"❌ Incorrecto\nEl consejo correcto era:\n{self.consejo_actual}"
            self.puntuacion_label.text = f"Puntuación: {self.puntuacion}"
            self.index += 1
            self.mostrar_consejo()

# App principal
class ConsejosApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(PracticaScreen(name="practica"))
        return sm

if __name__ == "__main__":
    ConsejosApp().run()
