from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty
import random

# Ejercicios de ejemplo
EJERCICIOS = {
    "Ortografía": {
        "Nivel 1": {
            "Selección múltiple": [
                {
                    "pregunta": "¿Cuál palabra está escrita correctamente?",
                    "opciones": ["exámen", "examen", "exámenn"],
                    "respuesta": "examen"
                }
            ]
        }
    }
}

class MenuScreen(Screen):
    pass

class EjercicioScreen(Screen):
    pregunta = StringProperty("")
    opciones = ListProperty([])

    def cargar_ejercicio(self, area, nivel, tipo):
        ejercicio = random.choice(EJERCICIOS[area][nivel][tipo])
        self.pregunta = ejercicio["pregunta"]
        self.opciones = ejercicio["opciones"]
        self.correcta = ejercicio["respuesta"]

    def verificar_respuesta(self, seleccion):
        if seleccion == self.correcta:
            self.ids.resultado.text = "✅ ¡Correcto!"
        else:
            self.ids.resultado.text = f"❌ Incorrecto. Respuesta: {self.correcta}"

class CastellanoApp(App):
    def build(self):
        return self.root

if __name__ == "__main__":
    CastellanoApp().run()
