from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
import random

# Datos base
ejemplos = [
    ("El hombre honrado", "adjetivo"),
    ("La dama duende", "adjetivo"),
    ("Las orillas del Maipo", "complemento"),
    ("La sin par Dulcinea", "complemento"),
    ("Aquel gran bulto que allí se ve", "proposición"),
    ("La persona a quien vimos ayer en el paseo", "proposición"),
    ("La campiña por donde transitábamos", "proposición")
]

diapo_texto = {
    "adjetivo": ["El hombre honrado", "La dama duende"],
    "complemento": ["Las orillas del Maipo", "La sin par Dulcinea"],
    "proposición": ["Aquel gran bulto que allí se ve", "La persona a quien vimos ayer en el paseo"]
}

class SintaxisApp(App):
    def build(self):
        self.creadas = []
        self.ejemplo_actual = random.choice(ejemplos)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text=f"Clasifica: {self.ejemplo_actual[0]}", font_size=20)
        self.layout.add_widget(self.label)

        self.spinner = Spinner(
            text='Selecciona el tipo',
            values=('adjetivo', 'complemento', 'proposición')
        )
        self.layout.add_widget(self.spinner)

        self.btn_clasificar = Button(text='Clasificar', on_press=self.clasificar)
        self.layout.add_widget(self.btn_clasificar)

        self.btn_diapositiva = Button(text='Ver diapositiva', on_press=self.ver_diapositiva)
        self.layout.add_widget(self.btn_diapositiva)

        self.oracion_input = TextInput(hint_text='Escribe tu propia oración', multiline=False)
        self.layout.add_widget(self.oracion_input)

        self.spinner_crear = Spinner(
            text='Tipo de modificación',
            values=('adjetivo', 'complemento', 'proposición')
        )
        self.layout.add_widget(self.spinner_crear)

        self.btn_crear = Button(text='Guardar oración', on_press=self.guardar_oracion)
        self.layout.add_widget(self.btn_crear)

        self.btn_ver_creadas = Button(text='Ver oraciones creadas', on_press=self.ver_creadas)
        self.layout.add_widget(self.btn_ver_creadas)

        return self.layout

    def clasificar(self, instance):
        seleccion = self.spinner.text
        correcto = self.ejemplo_actual[1]
        mensaje = "Correcto" if seleccion == correcto else f"Incorrecto, era: {correcto}"
        self.popup_resultado(mensaje)
        self.ejemplo_actual = random.choice(ejemplos)
        self.label.text = f"Clasifica: {self.ejemplo_actual[0]}"

    def ver_diapositiva(self, instance):
        contenido = ""
        for tipo, oraciones in diapo_texto.items():
            contenido += f"\n{tipo.upper()}\n" + "\n".join(oraciones) + "\n"
        self.popup_resultado(contenido)

    def guardar_oracion(self, instance):
        oracion = self.oracion_input.text.strip()
        tipo = self.spinner_crear.text
        if oracion:
            self.creadas.append((oracion, tipo))
            self.oracion_input.text = ""
            self.popup_resultado("¡Oración guardada!")

    def ver_creadas(self, instance):
        if self.creadas:
            contenido = "\n".join([f"{o} ({t})" for o, t in self.creadas])
        else:
            contenido = "Aún no has creado oraciones."
        self.popup_resultado(contenido)

    def popup_resultado(self, mensaje):
        popup = Popup(title='Resultado',
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

if __name__ == '__main__':
    SintaxisApp().run()
