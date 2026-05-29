import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
import json
import os
import pyttsx3

kivy.require("2.1.0")

engine = pyttsx3.init()
DATA_FILE = "ejemplos_ortografia.json"

# Diccionario de categorías
categorias = {
    "1": "Palabras con b y v",
    "2": "Palabras con c, s, z",
    "3": "Palabras con g, j",
    "4": "Palabras con ll y y (yeísmo)",
    "5": "Palabras con h (muda)",
    "6": "Palabras con dígrafos (ch, ll, rr, gu, qu)",
    "7": "Palabras con diptongos y hiatos",
    "8": "Palabras con tilde (acentuación)",
    "9": "Palabras homófonas y etimológicas"
}

# Cargar y guardar datos
def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {nombre: [] for nombre in categorias.values()}

def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def leer_voz(texto):
    engine.say(texto)
    engine.runAndWait()


class OrtografiaApp(App):
    def build(self):
        self.datos = cargar_datos()
        self.categoria_actual = list(categorias.values())[0]
        
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Selector de categoría
        self.spinner = Spinner(text=self.categoria_actual,
                               values=list(categorias.values()),
                               size_hint=(1, None), height=44)
        self.spinner.bind(text=self.on_categoria_selected)
        self.layout.add_widget(self.spinner)

        # Área de lista
        self.text_label = Label(text="Ejemplos:", size_hint=(1, None), height=30)
        self.layout.add_widget(self.text_label)

        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.lista_label = Label(size_hint_y=None, text="")
        self.lista_label.bind(texture_size=self.update_height)
        self.scroll.add_widget(self.lista_label)
        self.layout.add_widget(self.scroll)

        # Botones de acción
        botones = BoxLayout(size_hint=(1, None), height=44, spacing=5)
        botones.add_widget(Button(text="Ver", on_press=self.ver_ejemplos))
        botones.add_widget(Button(text="Agregar", on_press=self.agregar))
        botones.add_widget(Button(text="Editar", on_press=self.editar))
        self.layout.add_widget(botones)

        botones2 = BoxLayout(size_hint=(1, None), height=44, spacing=5)
        botones2.add_widget(Button(text="Escuchar", on_press=self.escuchar))
        botones2.add_widget(Button(text="Progreso", on_press=self.progreso))
        botones2.add_widget(Button(text="Guardar", on_press=self.guardar))
        self.layout.add_widget(botones2)

        self.ver_ejemplos()

        return self.layout

    def update_height(self, instance, value):
        instance.height = value[1]

    def on_categoria_selected(self, spinner, text):
        self.categoria_actual = text
        self.ver_ejemplos()

    def ver_ejemplos(self, instance=None):
        ejemplos = self.datos[self.categoria_actual]
        self.lista_label.text = "\n".join(f"• {ej}" for ej in ejemplos) if ejemplos else "No hay ejemplos aún."

    def agregar(self, instance):
        self.entrada_popup("Agregar ejemplo", "", self.agregar_ejemplo)

    def agregar_ejemplo(self, texto):
        if texto:
            self.datos[self.categoria_actual].append(texto)
            self.ver_ejemplos()

    def editar(self, instance):
        ejemplos = self.datos[self.categoria_actual]
        if not ejemplos:
            self.mensaje_popup("No hay ejemplos para editar.")
            return
        # Solo permite editar el último ejemplo para simplificar
        ultimo = ejemplos[-1]
        self.entrada_popup("Editar último ejemplo", ultimo, self.editar_ejemplo)

    def editar_ejemplo(self, texto):
        if texto:
            self.datos[self.categoria_actual][-1] = texto
            self.ver_ejemplos()

    def escuchar(self, instance):
        for ejemplo in self.datos[self.categoria_actual]:
            leer_voz(ejemplo)

    def progreso(self, instance):
        resumen = "\n".join(f"{cat}: {len(ejs)} ejemplos" for cat, ejs in self.datos.items())
        self.mensaje_popup(resumen)

    def guardar(self, instance):
        guardar_datos(self.datos)
        self.mensaje_popup("Datos guardados correctamente.")

    def mensaje_popup(self, mensaje):
        popup = Popup(title="Información",
                      content=Label(text=mensaje),
                      size_hint=(0.7, 0.4))
        popup.open()

    def entrada_popup(self, titulo, texto_inicial, on_confirmar):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        entrada = TextInput(text=texto_inicial, multiline=False)
        layout.add_widget(entrada)
        btn = Button(text="Aceptar", size_hint=(1, 0.3))
        layout.add_widget(btn)

        popup = Popup(title=titulo, content=layout, size_hint=(0.8, 0.4))
        btn.bind(on_press=lambda x: (on_confirmar(entrada.text), popup.dismiss()))
        popup.open()


if __name__ == "__main__":
    OrtografiaApp().run()
