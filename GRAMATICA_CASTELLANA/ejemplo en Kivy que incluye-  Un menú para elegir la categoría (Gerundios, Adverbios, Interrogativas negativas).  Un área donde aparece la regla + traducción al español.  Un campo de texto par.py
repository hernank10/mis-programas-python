import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


# -----------------------
# Datos de ejemplo
# -----------------------
gerundios = [
    ("Gerund as subject", "Swimming is fun.", "Nadar es divertido."),
    ("Gerund after verb", "I enjoy reading.", "Disfruto leer."),
    ("Gerund after preposition", "She is good at dancing.", "Ella es buena para bailar.")
]

adverbios = [
    ("Adverb of frequency", "He always studies at night.", "Él siempre estudia de noche."),
    ("Adverb of manner", "She sings beautifully.", "Ella canta hermosamente."),
    ("Adverb of time", "I will see you tomorrow.", "Te veré mañana.")
]

interrogativas = [
    ("Negative question (Present Simple)", "Don’t you like pizza?", "¿No te gusta la pizza?"),
    ("Negative question (Present Continuous)", "Isn’t he working now?", "¿No está trabajando ahora?"),
    ("Negative question (Past)", "Didn’t they call you?", "¿No te llamaron?")
]

categorias = {
    "Gerundios": gerundios,
    "Adverbios": adverbios,
    "Interrogativas Negativas": interrogativas
}


# -----------------------
# Interfaz principal
# -----------------------
class EstudioIngles(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Estado
        self.categoria_actual = None
        self.ejemplo_actual = None

        # Etiqueta de instrucción
        self.lbl_titulo = Label(text="Elige una categoría para empezar", font_size=20, size_hint=(1, 0.1))
        self.add_widget(self.lbl_titulo)

        # Botones de categorías
        box_categorias = BoxLayout(size_hint=(1, 0.1))
        for nombre in categorias.keys():
            btn = Button(text=nombre, on_press=self.seleccionar_categoria)
            box_categorias.add_widget(btn)
        self.add_widget(box_categorias)

        # Área de ejemplo
        self.lbl_regla = Label(text="", font_size=18, size_hint=(1, 0.2))
        self.add_widget(self.lbl_regla)

        # Campo de entrada
        self.txt_respuesta = TextInput(hint_text="Escribe aquí la frase en inglés", multiline=False, size_hint=(1, 0.1))
        self.add_widget(self.txt_respuesta)

        # Botones de acción
        box_acciones = BoxLayout(size_hint=(1, 0.1))
        self.btn_verificar = Button(text="Verificar", on_press=self.verificar_respuesta)
        self.btn_siguiente = Button(text="Siguiente", on_press=self.nuevo_ejemplo)
        box_acciones.add_widget(self.btn_verificar)
        box_acciones.add_widget(self.btn_siguiente)
        self.add_widget(box_acciones)

        # Retroalimentación
        self.lbl_feedback = Label(text="", font_size=18, size_hint=(1, 0.1))
        self.add_widget(self.lbl_feedback)

    def seleccionar_categoria(self, instance):
        self.categoria_actual = instance.text
        self.nuevo_ejemplo()

    def nuevo_ejemplo(self, *args):
        if not self.categoria_actual:
            return
        self.ejemplo_actual = random.choice(categorias[self.categoria_actual])
        regla, ejemplo, traduccion = self.ejemplo_actual
        self.lbl_regla.text = f"[{regla}]\nES: {traduccion}"
        self.txt_respuesta.text = ""
        self.lbl_feedback.text = ""

    def verificar_respuesta(self, *args):
        if not self.ejemplo_actual:
            return
        _, ejemplo_correcto, _ = self.ejemplo_actual
        respuesta = self.txt_respuesta.text.strip()
        if respuesta.lower() == ejemplo_correcto.lower():
            self.lbl_feedback.text = "✅ Correcto!"
            self.lbl_feedback.color = (0, 1, 0, 1)  # Verde
        else:
            self.lbl_feedback.text = f"❌ Incorrecto.\nCorrecto: {ejemplo_correcto}"
            self.lbl_feedback.color = (1, 0, 0, 1)  # Rojo


class InglesApp(App):
    def build(self):
        return EstudioIngles()


if __name__ == "__main__":
    InglesApp().run()
