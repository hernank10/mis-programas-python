# Adaptación a Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import random

# Datos de ejemplo
oraciones_condicionales = {
    "Reales": [
        {"oracion": "Si estudias, aprobarás el examen.", "explicacion": "Condición real. SI + Presente + Futuro."},
        {"oracion": "Si llueve, nos quedamos en casa.", "explicacion": "Condición presente real. SI + Presente + Presente."}
    ],
    "Potenciales": [
        {"oracion": "Si estudiaras más, aprobarías fácilmente.", "explicacion": "Condición hipotética. SI + Pret. Imperfecto Subj. + Condicional simple."},
        {"oracion": "Si vinieras mañana, podrías ayudarme.", "explicacion": "Condición futura dudosa. SI + Pret. Imperfecto Subj. + Condicional simple."}
    ],
    "Irreales": [
        {"oracion": "Si hubieras estudiado, habrías aprobado.", "explicacion": "Condición no cumplida en el pasado. SI + Pret. Pluscuamperfecto Subj. + Condicional compuesto."},
        {"oracion": "Si me lo hubieras dicho, no habría venido.", "explicacion": "Condición pasada no cumplida. SI + Pluscuamperfecto Subj. + Condicional compuesto."}
    ]
}

class JuegoOrdenar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.puntos = 0
        self.palabras = []
        self.respuesta = []
        self.oracion_objetivo = ""
        self.explicacion = ""
        self.label_puntos = Label(text=f"🎯 Puntos: {self.puntos}")
        self.add_widget(self.label_puntos)
        self.label_instruccion = Label(text="🔤 Haz clic en las palabras en orden para formar la oración:")
        self.add_widget(self.label_instruccion)
        self.contenedor_palabras = BoxLayout()
        self.add_widget(self.contenedor_palabras)
        self.label_resultado = Label(text="")
        self.add_widget(self.label_resultado)
        self.nueva_oracion()

    def nueva_oracion(self):
        categoria = random.choice(list(oraciones_condicionales.keys()))
        seleccion = random.choice(oraciones_condicionales[categoria])
        self.oracion_objetivo = seleccion['oracion']
        self.explicacion = seleccion['explicacion']
        self.palabras = self.oracion_objetivo.split()
        random.shuffle(self.palabras)
        self.respuesta = []
        self.label_resultado.text = ""
        self.mostrar_botones()

    def mostrar_botones(self):
        self.contenedor_palabras.clear_widgets()
        for palabra in self.palabras:
            btn = Button(text=palabra)
            btn.bind(on_press=self.agregar_palabra)
            self.contenedor_palabras.add_widget(btn)

    def agregar_palabra(self, instancia):
        palabra = instancia.text
        self.respuesta.append(palabra)
        instancia.disabled = True
        if len(self.respuesta) == len(self.oracion_objetivo.split()):
            resultado = " ".join(self.respuesta)
            if resultado.strip() == self.oracion_objetivo:
                self.label_resultado.text = f"✅ ¡Correcto! 🎊\n📘 {self.explicacion}"
                self.puntos += 1
                self.label_puntos.text = f"🎯 Puntos: {self.puntos}"
            else:
                self.label_resultado.text = f"❌ Incorrecto.\nEra: {self.oracion_objetivo}\n📘 {self.explicacion}"
            self.nueva_oracion()

class MenuPrincipal(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="🎮 Selecciona un juego condicional:", size_hint_y=None, height=40))

        juegos = [
            ("Juego 2: Ordenar palabras 🧩", self.ir_juego_ordenar),
            ("Juego 3: Completar espacios ✏️", self.juego_en_construccion),
            ("Juego 4: Memoria 🧠", self.juego_en_construccion),
            ("Juego 5: Construcción de oración 🧱", self.juego_en_construccion),
            ("Juego 6: Selección múltiple ✅", self.juego_en_construccion),
            ("Juego 7: Aventura textual 🗺️", self.juego_en_construccion),
            ("Juego 8: Carrera de condicionales 🚗", self.juego_en_construccion),
            ("Juego 9: Rompecabezas lógico 🧠", self.juego_en_construccion),
            ("Juego 10: Quiz visual 🖼️", self.juego_en_construccion),
        ]

        scroll = ScrollView()
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        for texto, funcion in juegos:
            btn = Button(text=texto, size_hint_y=None, height=40)
            btn.bind(on_press=funcion)
            layout.add_widget(btn)

        scroll.add_widget(layout)
        self.add_widget(scroll)

    def ir_juego_ordenar(self, instance):
        self.clear_widgets()
        self.add_widget(JuegoOrdenar())

    def juego_en_construccion(self, instance):
        popup = Popup(title="En construcción 🚧", content=Label(text="Este juego estará disponible próximamente."),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class JuegosCondicionalesApp(App):
    def build(self):
        return MenuPrincipal()

if __name__ == '__main__':
    JuegosCondicionalesApp().run()
