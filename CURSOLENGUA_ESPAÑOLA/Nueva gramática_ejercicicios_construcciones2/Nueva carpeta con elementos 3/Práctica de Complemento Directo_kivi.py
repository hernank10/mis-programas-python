from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
import random

class ComplementoDirectoApp(App):
    def build(self):
        return MainScreen()

class MainScreen(BoxLayout):
    current_example = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Ejemplos base
        self.ejemplos_base = [
            ("He visto una película", "una película"),
            ("Compré un coche nuevo", "un coche nuevo"),
            ("Ella leyó el libro", "el libro"),
            ("Pedro pintó la casa", "la casa"),
            ("María cocinó la cena", "la cena"),
            ("Juan rompió el vaso", "el vaso"),
            ("Ana organizó la fiesta", "la fiesta"),
            ("Escuchamos la canción", "la canción"),
            ("Clara escribió una carta", "una carta"),
            ("Luis abrió la puerta", "la puerta"),
            ("El niño rompió el juguete", "el juguete"),
            ("Vi a tu hermano", "a tu hermano"),
            ("Tocamos la guitarra", "la guitarra"),
            ("Perdí el tren", "el tren"),
            ("Ganamos el partido", "el partido"),
            ("Leí la noticia", "la noticia"),
            ("Encontré las llaves", "las llaves"),
            ("Terminé el informe", "el informe"),
            ("Comprendí la explicación", "la explicación"),
            ("Guardó el documento", "el documento"),
            ("Encendió la luz", "la luz"),
            ("Apagó el televisor", "el televisor"),
            ("Escribí un poema", "un poema"),
            ("El perro encontró el hueso", "el hueso"),
            ("La profesora corrigió los exámenes", "los exámenes"),
            ("Vi la película dos veces", "la película"),
            ("Descargué la aplicación", "la aplicación"),
            ("Revisé los correos", "los correos"),
            ("Presenté el proyecto", "el proyecto"),
            ("Recibí el paquete", "el paquete"),
            ("El gato atrapó al ratón", "al ratón"),
            ("El policía detuvo al ladrón", "al ladrón"),
            ("Marina horneó un pastel", "un pastel"),
            ("El mecánico arregló el coche", "el coche"),
            ("Sandra limpió la cocina", "la cocina"),
            ("José vendió su bicicleta", "su bicicleta"),
            ("Miramos las estrellas", "las estrellas"),
            ("Guardé los documentos", "los documentos"),
            ("El niño abrazó a su madre", "a su madre"),
            ("Carmen escribió un correo", "un correo"),
            ("Tiré la basura", "la basura"),
            ("Compramos frutas frescas", "frutas frescas"),
            ("El pintor terminó el mural", "el mural"),
            ("Sara decoró la habitación", "la habitación"),
            ("Le mostré la foto", "la foto"),
            ("Claudia trajo el informe", "el informe"),
            ("El niño escondió el juguete", "el juguete"),
            ("Tomé el medicamento", "el medicamento"),
            ("El alumno entregó la tarea", "la tarea"),
            ("Luis bebió el jugo", "el jugo")
        ]

        self.current = 0

        self.label_instruction = Label(text="Selecciona el complemento directo:")
        self.label_example = Label(text="", size_hint_y=None, height=40)
        self.input_user = TextInput(hint_text="Escribe el complemento directo", multiline=False)
        self.button_check = Button(text="Verificar", on_press=self.check_answer)
        self.result_label = Label(text="", size_hint_y=None, height=30)

        self.add_widget(self.label_instruction)
        self.add_widget(self.label_example)
        self.add_widget(self.input_user)
        self.add_widget(self.button_check)
        self.add_widget(self.result_label)

        self.show_next_example()

    def show_next_example(self):
        if self.current < len(self.ejemplos_base):
            ejemplo = self.ejemplos_base[self.current]
            self.label_example.text = ejemplo[0]
        else:
            self.label_example.text = "¡Has completado todos los ejemplos!"

    def check_answer(self, instance):
        user_input = self.input_user.text.strip().lower()
        correct = self.ejemplos_base[self.current][1].strip().lower()

        if user_input == correct:
            self.result_label.text = "¡Correcto!"
        else:
            self.result_label.text = f"Incorrecto. La respuesta era: '{correct}'"

        self.current += 1
        self.input_user.text = ""
        self.show_next_example()

if __name__ == '__main__':
    ComplementoDirectoApp().run()
