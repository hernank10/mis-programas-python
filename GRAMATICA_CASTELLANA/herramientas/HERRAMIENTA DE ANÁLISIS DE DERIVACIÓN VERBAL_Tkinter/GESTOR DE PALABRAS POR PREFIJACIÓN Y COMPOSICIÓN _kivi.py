from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
import json
import os

ARCHIVO = "palabras.json"

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_datos(data):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

class PalabraManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.datos = cargar_datos()

        self.spinner = Spinner(
            text='Selecciona categoría',
            values=sorted(self.datos.keys()),
            size_hint=(1, 0.1)
        )
        self.spinner.bind(text=self.mostrar_palabras)
        self.add_widget(self.spinner)

        self.lista_palabras = Label(text='Selecciona una categoría', size_hint=(1, 0.5))
        self.add_widget(self.lista_palabras)

        btn_agregar = Button(text='Agregar palabra', size_hint=(1, 0.1))
        btn_agregar.bind(on_press=self.abrir_popup_agregar)
        self.add_widget(btn_agregar)

        btn_guardar = Button(text='Guardar datos', size_hint=(1, 0.1))
        btn_guardar.bind(on_press=lambda instance: guardar_datos(self.datos))
        self.add_widget(btn_guardar)

    def mostrar_palabras(self, spinner, text):
        palabras = self.datos.get(text, [])
        if palabras:
            texto = '\n'.join([f"{p[0]} ({p[1]}) → {p[2]}" for p in palabras])
        else:
            texto = "No hay palabras en esta categoría."
        self.lista_palabras.text = texto

    def abrir_popup_agregar(self, instance):
        popup = PopupAgregar(self)
        popup.open()

    def agregar_palabra(self, categoria, palabra, formacion, significado):
        if categoria not in self.datos:
            self.datos[categoria] = []
            self.spinner.values = sorted(self.datos.keys())
        self.datos[categoria].append([palabra, formacion, significado])
        if self.spinner.text == categoria:
            self.mostrar_palabras(None, categoria)

class PopupAgregar(Popup):
    def __init__(self, parent, **kwargs):
        super().__init__(title="Agregar palabra", size_hint=(0.9, 0.7), **kwargs)
        self.parent_widget = parent

        layout = BoxLayout(orientation='vertical')
        self.cat_input = TextInput(hint_text='Categoría', multiline=False)
        self.pal_input = TextInput(hint_text='Palabra', multiline=False)
        self.form_input = TextInput(hint_text='Formación', multiline=False)
        self.sign_input = TextInput(hint_text='Significado', multiline=True)

        btn_agregar = Button(text='Agregar')
        btn_agregar.bind(on_press=self.agregar_y_cerrar)

        layout.add_widget(self.cat_input)
        layout.add_widget(self.pal_input)
        layout.add_widget(self.form_input)
        layout.add_widget(self.sign_input)
        layout.add_widget(btn_agregar)

        self.content = layout

    def agregar_y_cerrar(self, instance):
        categoria = self.cat_input.text.strip()
        palabra = self.pal_input.text.strip()
        formacion = self.form_input.text.strip()
        significado = self.sign_input.text.strip()

        if categoria and palabra and significado:
            self.parent_widget.agregar_palabra(categoria, palabra, formacion, significado)
            self.dismiss()

class GestorPalabrasApp(App):
    def build(self):
        return PalabraManager()

if __name__ == '__main__':
    GestorPalabrasApp().run()
