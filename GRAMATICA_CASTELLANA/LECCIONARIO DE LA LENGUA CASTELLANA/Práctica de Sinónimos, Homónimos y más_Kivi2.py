from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
import pyttsx3
import os
import random

Window.size = (600, 800)

# Diccionario de palabras
categorias = {
    "Sinónimos": ["alegre", "contento", "hermoso", "bello", "rápido", "veloz", "difícil", "complicado", "enseñar", "instruir"],
    "Homónimos": ["banco", "cura", "banda", "capital", "vela", "cola", "ratón", "vino", "sal", "gato"],
    "Homófonas": ["hola", "ola", "vaca", "baca", "casa", "caza", "bello", "vello", "haya", "halla"],
    "Isónimos": ["doctor", "médico", "niño", "infante", "madre", "progenitora", "padre", "progenitor", "estudiante", "alumno"],
    "Antónimos": ["alegría", "tristeza", "fuerte", "débil", "largo", "corto", "falso", "verdadero", "bueno", "malo"]
}

ejemplos = {
    "Sinónimos": "El día estaba alegre y contento, lleno de cosas hermosas y bellas...",
    "Homónimos": "Fui al banco a sentarme. Luego pasé por el banco a retirar dinero...",
    "Homófonas": "La ola golpeó la orilla. Dije hola al pescador...",
    "Isónimos": "El doctor y el médico llegaron a atender al infante...",
    "Antónimos": "Pasamos de la alegría a la tristeza. Algunos eran fuertes, otros débiles..."
}

puntaje_total = 0

class PracticaPalabras(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.categoria_actual = "Sinónimos"

        self.spinner = Spinner(text="Sinónimos", values=list(categorias.keys()), size_hint=(1, 0.1))
        self.spinner.bind(text=self.cambiar_categoria)
        self.add_widget(self.spinner)

        self.btn_palabras = Button(text="📋 Ver palabras aprendidas", on_press=self.ver_palabras)
        self.add_widget(self.btn_palabras)

        self.lbl_ensayo = Label(text="📝 Escribe tu ensayo:", size_hint=(1, 0.1))
        self.add_widget(self.lbl_ensayo)

        self.entrada_ensayo = TextInput(hint_text="Escribe aquí...", multiline=True, size_hint=(1, 0.5))
        self.add_widget(self.entrada_ensayo)

        self.btn_verificar = Button(text="✅ Verificar y guardar ensayo", on_press=self.procesar_ensayo)
        self.add_widget(self.btn_verificar)

        self.btn_ejemplo = Button(text="📌 Ver ejemplo automático", on_press=self.ver_ejemplo)
        self.add_widget(self.btn_ejemplo)

        self.btn_voz = Button(text="🔊 Leer ensayo en voz alta", on_press=self.leer_voz)
        self.add_widget(self.btn_voz)

        self.btn_prueba = Button(text="🧪 Prueba de selección múltiple", on_press=self.prueba_multiple)
        self.add_widget(self.btn_prueba)

        self.lbl_puntaje = Label(text="🎯 Puntaje total: 0", size_hint=(1, 0.1))
        self.add_widget(self.lbl_puntaje)

    def cambiar_categoria(self, spinner, text):
        self.categoria_actual = text

    def ver_palabras(self, instance):
        lista = categorias[self.categoria_actual]
        self.mostrar_popup("Palabras aprendidas", "\n".join(lista))

    def ver_ejemplo(self, instance):
        self.mostrar_popup("Ejemplo", ejemplos.get(self.categoria_actual, "No disponible"))

    def procesar_ensayo(self, instance):
        global puntaje_total
        texto = self.entrada_ensayo.text.lower()
        palabras = categorias[self.categoria_actual]
        coincidencias = [p for p in palabras if p in texto]
        if len(coincidencias) >= 5:
            resultado = "✅ ¡Bien hecho! Has usado al menos 5 palabras aprendidas."
            puntaje_total += 10
        else:
            resultado = "❌ Intenta incluir más palabras aprendidas."
            puntaje_total += 2

        self.lbl_puntaje.text = f"🎯 Puntaje total: {puntaje_total}"
        carpeta = "ensayos_guardados_kivy"
        os.makedirs(carpeta, exist_ok=True)
        archivo = os.path.join(carpeta, f"ensayo_{self.categoria_actual.lower()}.txt")
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(texto)
        self.mostrar_popup("Resultado", resultado)

    def leer_voz(self, instance):
        texto = self.entrada_ensayo.text.strip()
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()

    def prueba_multiple(self, instance):
        palabras = categorias[self.categoria_actual]
        palabra = random.choice(palabras)
        opciones = random.sample(palabras, 3)
        if palabra not in opciones:
            opciones[random.randint(0, 2)] = palabra
        texto = f"¿Cuál palabra es de la categoría '{self.categoria_actual}'?\n\n" + "\n".join(opciones)
        self.mostrar_popup("Prueba de selección múltiple", texto)

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo,
                      content=Label(text=mensaje),
                      size_hint=(0.8, 0.4))
        popup.open()

class PracticaApp(App):
    def build(self):
        return PracticaPalabras()

PracticaApp().run()

