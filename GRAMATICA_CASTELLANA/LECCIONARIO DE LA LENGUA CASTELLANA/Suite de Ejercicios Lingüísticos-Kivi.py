from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import datetime

# Diccionario de ejercicios y textos
ejercicios = {
    "Diptongos": "Escribe palabras con diptongos como tierra, cielo, miedo...",
    "Triptongos": "Escribe palabras con triptongos como limpiáis, estudiéis...",
    "Hiatos": "Escribe palabras con hiatos como poesía, tía, aéreo...",
    "Prefijos": "Escribe palabras con prefijos como predecir, imposible, subterráneo...",
    "Compuestas": "Corrige: AUTOESCUELA, PARARRAYOS, SACAPUNTAS...",
    "Tildación agudas": "Escribe correctamente: CAFE, CANTAR, AVION, PAPEL, CAFE...",
    "Tildación esdrújulas": "Corrige: TELEFONO, MUSICA, QUIMICA, MATEMATICAS...",
}

class EjercicioApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.spinner = Spinner(
            text='Selecciona un ejercicio',
            values=list(ejercicios.keys()),
            size_hint=(1, 0.1)
        )
        self.spinner.bind(text=self.cambiar_ejercicio)

        self.instruccion = Label(
            text='Selecciona un ejercicio del menú',
            size_hint=(1, 0.2)
        )

        self.text_input = TextInput(
            hint_text='Escribe tu respuesta aquí...',
            size_hint=(1, 0.5)
        )

        self.btn_guardar = Button(
            text='Guardar Respuesta',
            size_hint=(1, 0.2)
        )
        self.btn_guardar.bind(on_press=self.guardar_respuesta)

        self.add_widget(self.spinner)
        self.add_widget(self.instruccion)
        self.add_widget(self.text_input)
        self.add_widget(self.btn_guardar)

    def cambiar_ejercicio(self, spinner, text):
        self.instruccion.text = ejercicios.get(text, '')

    def guardar_respuesta(self, instance):
        ejercicio = self.spinner.text
        respuesta = self.text_input.text.strip()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if ejercicio and respuesta:
            with open("respuestas_usuario.txt", "a", encoding='utf-8') as f:
                f.write(f"[{timestamp}] {ejercicio}: {respuesta}\n")

            self.text_input.text = ""
            self.instruccion.text = f"Respuesta guardada para {ejercicio}."

class MiApp(App):
    def build(self):
        return EjercicioApp()

if __name__ == "__main__":
    MiApp().run()
