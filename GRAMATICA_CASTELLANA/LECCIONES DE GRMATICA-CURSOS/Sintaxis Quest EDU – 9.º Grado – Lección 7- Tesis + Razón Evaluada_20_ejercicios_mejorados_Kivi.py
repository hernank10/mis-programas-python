from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.dropdownitem import MDDropDownMenu
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size = (800, 600)

# 📚 Lista de ejercicios con modelo
ejercicios = [
    {"tesis": "Las tareas escolares deben tener un propósito claro", 
     "ejemplo": "Porque refuerzan lo aprendido y no solo ocupan tiempo."},
    {"tesis": "El reciclaje debe enseñarse desde primaria", 
     "ejemplo": "Ya que promueve conciencia ambiental desde temprana edad."},
    {"tesis": "La lectura diaria mejora el desempeño escolar", 
     "ejemplo": "Porque desarrolla vocabulario y comprensión lectora."},
    # [... hasta ejercicio 20 ...]
    {"tesis": "La tecnología debe usarse con responsabilidad", 
     "ejemplo": "Porque puede educar, pero también desinformar."}
]

# 🧠 Evaluación de texto argumentativo
def evaluar_respuesta(razon):
    razon = razon.strip().lower()
    puntos = 0
    conectores = ["porque", "ya que", "debido a"]
    if any(c in razon for c in conectores):
        puntos += 1
    if len(razon.split()) >= 5:
        puntos += 1
    if "." in razon or "," in razon:
        puntos += 1
    if puntos == 3:
        return "🏅 ¡Argumento sólido, bien estructurado!", puntos
    elif puntos == 2:
        return "✅ ¡Buena razón, podrías agregar más detalle!", puntos
    elif puntos == 1:
        return "⚠️ Tiene potencial pero le falta estructura.", puntos
    else:
        return "❌ Falta conexión lógica o desarrollo.", puntos

# 🧩 App principal
class ArgumentacionApp(MDApp):
    resultado = StringProperty("")
    actual = 0
    total = 0

    def build(self):
        self.screen = MDScreen()

        self.tesis_label = MDLabel(text="Tesis:", halign="center", font_style="H6")
        self.ejemplo_label = MDLabel(text="Ejemplo:", halign="center", theme_text_color="Hint")
        self.text_input = MDTextField(hint_text="Escribe tu razón aquí...", multiline=True)

        self.next_button = MDRaisedButton(text="🧠 Evaluar", on_release=self.evaluar)
        self.advance_button = MDRaisedButton(text="➡️ Siguiente", on_release=self.siguiente)

        self.resultado_label = MDLabel(text=self.resultado, halign="center", theme_text_color="Custom")

        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(self.tesis_label)
        layout.add_widget(self.ejemplo_label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.next_button)
        layout.add_widget(self.resultado_label)
        layout.add_widget(self.advance_button)

        self.screen.add_widget(layout)
        self.cargar_ejercicio()
        return self.screen

    def cargar_ejercicio(self):
        if self.actual < len(ejercicios):
            ejercicio = ejercicios[self.actual]
            self.tesis_label.text = f"Tesis {self.actual+1}: {ejercicio['tesis']}"
            self.ejemplo_label.text = f"Ejemplo: {ejercicio['ejemplo']}"
            self.text_input.text = ""
            self.resultado_label.text = ""
        else:
            self.tesis_label.text = "🧠 ¡Has completado todos los ejercicios!"
            self.ejemplo_label.text = f"🌟 Puntaje final: {self.total}/{len(ejercicios)*3}"
            self.text_input.opacity = 0
            self.next_button.opacity = 0
            self.advance_button.text = "Salir"
            self.advance_button.on_release = lambda x: self.stop()

    def evaluar(self, instance):
        razon = self.text_input.text
        fb, puntos = evaluar_respuesta(razon)
        self.resultado_label.text = f"{fb} (Puntaje: {puntos}/3)"
        self.total += puntos

    def siguiente(self, instance):
        self.actual += 1
        self.cargar_ejercicio()

ArgumentacionApp().run()
