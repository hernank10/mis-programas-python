from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


# Lista principal de ejemplos, se modifica en tiempo real
ejemplos = [
    "Usa la 'b' en palabras como 'burro', 'bello', 'barrera'.",
    "Las palabras que terminan en '-ción' llevan 'c', como 'educación'.",
    "Las formas verbales que terminan en '-ger' o '-gir' se escriben con 'g'.",
    "Después de 'm' se escribe 'b': 'tambor', 'embudo'.",
    "Se usa tilde en palabras agudas terminadas en vocal, n o s.",
    "Las palabras homófonas se escriben diferente: 'votar' y 'botar'."
]


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        layout.add_widget(Button(text="📘 Practicar reglas", on_press=self.go_to_practicar))
        layout.add_widget(Button(text="✍ Crear/Editar ejemplos", on_press=self.go_to_editar))
        layout.add_widget(Button(text="❌ Salir", on_press=App.get_running_app().stop))

        self.add_widget(layout)

    def go_to_practicar(self, instance):
        self.manager.current = 'practicar'

    def go_to_editar(self, instance):
        self.manager.current = 'editar'


class PracticarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_label = Label(text=ejemplos[self.index], halign="center")
        self.layout.add_widget(self.text_label)

        self.next_button = Button(text="➡ Siguiente", on_press=self.siguiente_ejemplo)
        self.layout.add_widget(self.next_button)

        self.back_button = Button(text="🔙 Volver al menú", on_press=self.volver)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def siguiente_ejemplo(self, instance):
        self.index = (self.index + 1) % len(ejemplos)
        self.text_label.text = ejemplos[self.index]

    def volver(self, instance):
        self.manager.current = 'menu'


class EditarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.lista_textos = BoxLayout(orientation='vertical', size_hint_y=None)
        self.lista_textos.bind(minimum_height=self.lista_textos.setter('height'))
        self.scroll.add_widget(self.lista_textos)

        self.text_input = TextInput(hint_text="Escribe un nuevo ejemplo aquí", size_hint=(1, 0.2))
        self.boton_agregar = Button(text="➕ Agregar", on_press=self.agregar_ejemplo)
        self.boton_volver = Button(text="🔙 Volver al menú", on_press=self.volver)

        self.layout.add_widget(self.scroll)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.boton_agregar)
        self.layout.add_widget(self.boton_volver)

        self.add_widget(self.layout)
        self.mostrar_ejemplos()

    def mostrar_ejemplos(self):
        self.lista_textos.clear_widgets()
        for i, texto in enumerate(ejemplos):
            fila = BoxLayout(size_hint_y=None, height=40)
            fila.add_widget(Label(text=f"{i+1}. {texto}", halign='left'))
            boton_borrar = Button(text="❌", size_hint_x=None, width=50)
            boton_borrar.bind(on_press=lambda btn, idx=i: self.borrar_ejemplo(idx))
            fila.add_widget(boton_borrar)
            self.lista_textos.add_widget(fila)

    def agregar_ejemplo(self, instance):
        nuevo = self.text_input.text.strip()
        if nuevo:
            ejemplos.append(nuevo)
            self.text_input.text = ""
            self.mostrar_ejemplos()

    def borrar_ejemplo(self, idx):
        if 0 <= idx < len(ejemplos):
            del ejemplos[idx]
            self.mostrar_ejemplos()

    def volver(self, instance):
        self.manager.current = 'menu'


class ReglasApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(PracticarScreen(name='practicar'))
        sm.add_widget(EditarScreen(name='editar'))
        return sm


if __name__ == '__main__':
    ReglasApp().run()
