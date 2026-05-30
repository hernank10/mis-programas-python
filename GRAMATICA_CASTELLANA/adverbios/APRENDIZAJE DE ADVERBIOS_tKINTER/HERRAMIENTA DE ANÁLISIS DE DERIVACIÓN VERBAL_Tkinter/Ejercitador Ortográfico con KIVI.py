from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

API_URL = "http://127.0.0.1:8000"  # cambia si lo usas en un móvil real

class OrtografiaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.categoria_spinner = Spinner(text='Selecciona categoría', size_hint=(1, None), height=44)
        self.layout.add_widget(self.categoria_spinner)

        self.ejemplos_label = Label(text="Ejemplos:", size_hint_y=None, height=200)
        self.layout.add_widget(self.ejemplos_label)

        self.input_text = TextInput(hint_text="Nuevo ejemplo", size_hint=(1, None), height=44)
        self.layout.add_widget(self.input_text)

        self.add_button = Button(text="Agregar", size_hint=(1, None), height=44)
        self.add_button.bind(on_press=self.agregar_ejemplo)
        self.layout.add_widget(self.add_button)

        self.load_categorias()

        self.categoria_spinner.bind(text=self.ver_ejemplos)

        return self.layout

    def load_categorias(self):
        try:
            response = requests.get(f"{API_URL}/categorias")
            categorias = response.json()["categorias"]
            self.categoria_spinner.values = categorias
        except Exception as e:
            self.ejemplos_label.text = f"Error cargando categorías: {e}"

    def ver_ejemplos(self, spinner, text):
        try:
            response = requests.get(f"{API_URL}/ejemplos/{text}")
            ejemplos = response.json()["ejemplos"]
            self.ejemplos_label.text = "\n".join([f"{i}. {e}" for i, e in enumerate(ejemplos)])
        except Exception as e:
            self.ejemplos_label.text = f"Error cargando ejemplos: {e}"

    def agregar_ejemplo(self, instance):
        categoria = self.categoria_spinner.text
        ejemplo = self.input_text.text.strip()
        if not ejemplo or categoria == "Selecciona categoría":
            return
        data = {"categoria": categoria, "ejemplo": ejemplo}
        try:
            r = requests.post(f"{API_URL}/agregar", json=data)
            self.input_text.text = ""
            self.ver_ejemplos(None, categoria)
        except Exception as e:
            self.ejemplos_label.text = f"Error al agregar: {e}"

if __name__ == '__main__':
    OrtografiaApp().run()
