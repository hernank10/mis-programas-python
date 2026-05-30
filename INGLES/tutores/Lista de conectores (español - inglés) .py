from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

# Lista de conectores (español -> inglés)
conectores = {
    "sin embargo": "however",
    "por lo tanto": "therefore",
    "aunque": "although",
    "además": "moreover",
    "en cambio": "instead",
    "por ejemplo": "for example",
    "a pesar de": "despite",
    "mientras tanto": "meanwhile",
    "en conclusión": "in conclusion",
    "finalmente": "finally"
}

class ConectoresApp(App):
    def build(self):
        self.puntaje = 0
        self.modo_estudio = True  # Inicia en modo estudio
        self.conector_actual = None

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.label = Label(text="Presiona 'Nuevo conector' para comenzar", font_size=20)
        layout.add_widget(self.label)

        self.input = TextInput(hint_text="Escribe la traducción en inglés aquí", multiline=False, font_size=18)
        layout.add_widget(self.input)

        # Botones
        botones = BoxLayout(size_hint_y=0.3, spacing=10)
        btn_nuevo = Button(text="Nuevo conector", on_press=self.nuevo_conector)
        btn_verificar = Button(text="Verificar", on_press=self.verificar)
        btn_modo = Button(text="Cambiar a Modo Práctica", on_press=self.cambiar_modo)
        botones.add_widget(btn_nuevo)
        botones.add_widget(btn_verificar)
        botones.add_widget(btn_modo)

        layout.add_widget(botones)

        self.puntaje_label = Label(text="Puntaje: 0", font_size=18)
        layout.add_widget(self.puntaje_label)

        return layout

    def nuevo_conector(self, instance):
        self.conector_actual = random.choice(list(conectores.keys()))
        if self.modo_estudio:
            # En modo estudio se muestran ambas traducciones
            self.label.text = f"{self.conector_actual} → {conectores[self.conector_actual]}"
        else:
            # En modo práctica solo se muestra el español
            self.label.text = f"Traduce al inglés: {self.conector_actual}"
        self.input.text = ""

    def verificar(self, instance):
        if self.modo_estudio:
            popup = Popup(title="Modo Estudio",
                          content=Label(text="En modo estudio no hay verificación.\nSolo observa y memoriza."),
                          size_hint=(0.6, 0.4))
            popup.open()
            return

        if not self.conector_actual:
            return

        respuesta = self.input.text.strip().lower()
        correcta = conectores[self.conector_actual].lower()

        if respuesta == correcta:
            self.puntaje += 1
            msg = f"✅ Correcto: {respuesta}"
        else:
            msg = f"❌ Incorrecto.\nLa respuesta correcta era: {correcta}"

        self.puntaje_label.text = f"Puntaje: {self.puntaje}"

        popup = Popup(title="Resultado",
                      content=Label(text=msg),
                      size_hint=(0.6, 0.4))
        popup.open()

    def cambiar_modo(self, instance):
        self.modo_estudio = not self.modo_estudio
        if self.modo_estudio:
            instance.text = "Cambiar a Modo Práctica"
            self.label.text = "Modo Estudio: Presiona 'Nuevo conector'"
        else:
            instance.text = "Cambiar a Modo Estudio"
            self.label.text = "Modo Práctica: Presiona 'Nuevo conector'"

if __name__ == "__main__":
    ConectoresApp().run()
