from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import os

Window.size = (800, 600)

class ConsejoEditor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.consejos = self.cargar_consejos("consejos.txt")
        self.reescritos = [""] * len(self.consejos)
        self.index = 0

        self.label = Label(text=self.consejos[self.index], size_hint_y=None, height=60, halign="left", valign="middle")
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        self.textinput = TextInput(text="", multiline=True, size_hint_y=0.6)
        self.add_widget(self.textinput)

        self.btn_guardar = Button(text="Guardar y Siguiente", size_hint_y=None, height=50)
        self.btn_guardar.bind(on_press=self.siguiente_consejo)
        self.add_widget(self.btn_guardar)

        self.btn_exportar = Button(text="Exportar Reescritos", size_hint_y=None, height=40)
        self.btn_exportar.bind(on_press=self.exportar)
        self.add_widget(self.btn_exportar)

    def cargar_consejos(self, filename):
        if not os.path.exists(filename):
            return ["Archivo de consejos no encontrado."]
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def siguiente_consejo(self, instance):
        self.reescritos[self.index] = self.textinput.text.strip()
        self.index += 1

        if self.index < len(self.consejos):
            self.label.text = self.consejos[self.index]
            self.textinput.text = self.reescritos[self.index]
        else:
            self.label.text = "¡Has completado todos los consejos!"
            self.textinput.text = ""
            self.btn_guardar.disabled = True

    def exportar(self, instance):
        with open("reescritos.txt", "w", encoding="utf-8") as f:
            for i, texto in enumerate(self.reescritos):
                f.write(f"{i+1}. {texto}\n")
        self.label.text = "¡Reescritos exportados a 'reescritos.txt'!"


class ReescribirConsejosApp(App):
    def build(self):
        return ConsejoEditor()


if __name__ == "__main__":
    ReescribirConsejosApp().run()
