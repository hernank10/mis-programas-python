from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

class PunctuationPracticeApp(App):
    def build(self):
        self.title = "Práctica de Signos de Puntuación"

        self.ejercicios_por_signo = {
            "Coma": [
                {"sin": "Vamos a comer niños", "correcto": "Vamos a comer, niños."},
                {"sin": "María Pedro Ana y Luis vinieron", "correcto": "María, Pedro, Ana y Luis vinieron."}
            ],
            "Punto y coma": [
                {"sin": "Estudié toda la noche sin embargo no aprobé", "correcto": "Estudié toda la noche; sin embargo, no aprobé."},
                {"sin": "Era tarde estaba cansado", "correcto": "Era tarde; estaba cansado."}
            ],
            "Dos puntos": [
                {"sin": "Ella dijo Estoy feliz", "correcto": "Ella dijo: Estoy feliz."},
                {"sin": "Llevó lo necesario agua pan y una linterna", "correcto": "Llevó lo necesario: agua, pan y una linterna."}
            ],
            "Guiones": [
                {"sin": "El problema es económico político y social", "correcto": "El problema es económico-político y social."},
                {"sin": "La reunión fue martes miércoles y jueves", "correcto": "La reunión fue martes-miércoles y jueves."}
            ],
            "Paréntesis": [
                {"sin": "Mi madre que es doctora me cuidó", "correcto": "Mi madre (que es doctora) me cuidó."},
                {"sin": "Estaré ausente por motivos personales de salud", "correcto": "Estaré ausente (por motivos personales de salud)."}
            ],
            "Interrogación": [
                {"sin": "Dónde vives", "correcto": "¿Dónde vives?"},
                {"sin": "Qué hora es", "correcto": "¿Qué hora es?"}
            ],
            "Exclamación": [
                {"sin": "Qué sorpresa", "correcto": "¡Qué sorpresa!"},
                {"sin": "Feliz cumpleaños", "correcto": "¡Feliz cumpleaños!"}
            ],
            "Comillas": [
                {"sin": "Ella dijo No me gusta", "correcto": "Ella dijo: \"No me gusta\"."},
                {"sin": "La palabra casa viene del latín", "correcto": "La palabra \"casa\" viene del latín."}
            ],
            "Puntos suspensivos": [
                {"sin": "No sé qué decir", "correcto": "No sé qué decir..."},
                {"sin": "Tal vez mañana o pasado", "correcto": "Tal vez mañana... o pasado."}
            ]
        }

        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.label_ejercicio = Label(text="Selecciona un signo para comenzar", size_hint=(1, 0.2), font_size=20)
        self.layout.add_widget(self.label_ejercicio)

        self.input_usuario = TextInput(hint_text="Escribe aquí tu respuesta", multiline=False, size_hint=(1, 0.1), font_size=18)
        self.layout.add_widget(self.input_usuario)

        self.boton_verificar = Button(text="Verificar respuesta", size_hint=(1, 0.1), on_press=self.verificar)
        self.layout.add_widget(self.boton_verificar)

        self.menu_scroll = ScrollView(size_hint=(1, 0.6))
        self.menu_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.menu_layout.bind(minimum_height=self.menu_layout.setter('height'))

        for signo in self.ejercicios_por_signo:
            btn = Button(text=signo, size_hint_y=None, height=50)
            btn.bind(on_press=self.seleccionar_signo)
            self.menu_layout.add_widget(btn)

        self.menu_scroll.add_widget(self.menu_layout)
        self.layout.add_widget(self.menu_scroll)

        self.ejercicios = []
        self.index = 0

        return self.layout

    def seleccionar_signo(self, instance):
        signo = instance.text
        self.ejercicios = self.ejercicios_por_signo[signo]
        self.index = 0
        self.mostrar_ejercicio()

    def mostrar_ejercicio(self):
        if self.index < len(self.ejercicios):
            ejercicio = self.ejercicios[self.index]
            self.label_ejercicio.text = f"Corrige: {ejercicio['sin']}"
            self.input_usuario.text = ""
        else:
            self.mostrar_popup("¡Completado!", "Has terminado todos los ejercicios.")

    def verificar(self, instance):
        if not self.ejercicios:
            self.mostrar_popup("Atención", "Selecciona un signo primero.")
            return

        respuesta = self.input_usuario.text.strip()
        correcto = self.ejercicios[self.index]["correcto"]

        if respuesta == correcto:
            self.mostrar_popup("Correcto", "¡Bien hecho!")
        else:
            self.mostrar_popup("Incorrecto", f"La respuesta correcta era:\n{correcto}")

        self.index += 1
        self.mostrar_ejercicio()

    def mostrar_popup(self, titulo, mensaje):
        contenido = BoxLayout(orientation="vertical", padding=10)
        contenido.add_widget(Label(text=mensaje))
        cerrar = Button(text="Cerrar", size_hint=(1, 0.3))
        popup = Popup(title=titulo, content=contenido, size_hint=(0.8, 0.4))
        cerrar.bind(on_press=popup.dismiss)
        contenido.add_widget(cerrar)
        popup.open()


if __name__ == "__main__":
    PunctuationPracticeApp().run()
