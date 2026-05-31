from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import json
import os
from datetime import datetime

EJEMPLOS_ARCHIVO = "ejemplos.json"
BITACORA_ARCHIVO = "bitacora.txt"
ESTADISTICAS_ARCHIVO = "estadisticas.json"

EJEMPLOS = {
    "correctas": [
        "Ir y venir a Madrid",
        "Tan bueno o mejor que tú",
        "Tengo tanto o más derecho que tú"
    ],
    "incorrectas": [
        "Espero y me alegraré de que todo le salga bien",
        "Deseo y confío en que apruebes",
        "Intentó y logró que todo saliera perfecto"
    ]
}

if os.path.exists(EJEMPLOS_ARCHIVO):
    with open(EJEMPLOS_ARCHIVO, "r", encoding="utf-8") as f:
        EJEMPLOS = json.load(f)

def guardar_ejemplos():
    with open(EJEMPLOS_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(EJEMPLOS, f, indent=4, ensure_ascii=False)

def registrar_en_bitacora(tipo, correctas, total):
    with open(BITACORA_ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Tipo: {tipo}, Correctas: {correctas}/{total}\n")

def actualizar_estadisticas(tipo, correctas, total):
    if os.path.exists(ESTADISTICAS_ARCHIVO):
        with open(ESTADISTICAS_ARCHIVO, "r", encoding="utf-8") as f:
            stats = json.load(f)
    else:
        stats = {}

    if tipo not in stats:
        stats[tipo] = {"total": 0, "correctas": 0}

    stats[tipo]["total"] += total
    stats[tipo]["correctas"] += correctas

    with open(ESTADISTICAS_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

class SintaxisApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        botones = [
            ("📘 Ver Teoría", self.mostrar_teoria),
            ("✅ Practicar Correctas", lambda _: self.practicar("correctas")),
            ("❌ Practicar Incorrectas", lambda _: self.practicar("incorrectas")),
            ("✍️ Completar Oración", self.completar_oracion),
            ("➕ Agregar Ejemplo", self.agregar_ejemplo),
            ("📈 Ver Estadísticas", self.mostrar_estadisticas),
        ]

        for texto, funcion in botones:
            btn = Button(text=texto, size_hint=(1, None), height=50)
            btn.bind(on_release=funcion)
            layout.add_widget(btn)

        return layout

    def popup(self, title, content):
        popup = Popup(title=title,
                      content=Label(text=content),
                      size_hint=(.8, .4))
        popup.open()

    def mostrar_teoria(self, instance):
        teoria = (
            "Construcción incorrecta: No se debe aplicar a dos palabras un régimen que sólo conviene a una.\n"
            "Ejemplo incorrecto: 'Espero y me alegraré de que todo le salga bien.'\n\n"
            "Construcciones aceptadas: Hay casos elípticos aceptables por el uso.\n"
            "Ejemplo correcto: 'Ir y venir a Madrid', 'Tan bueno o mejor que tú'."
        )
        self.popup("Teoría", teoria)

    def practicar(self, tipo):
        correctas = 0
        total = len(EJEMPLOS[tipo])

        def preguntar(indice):
            if indice >= total:
                self.popup("Resultado", f"Respondiste correctamente {correctas} de {total}.")
                registrar_en_bitacora(tipo, correctas, total)
                actualizar_estadisticas(tipo, correctas, total)
                return

            ejemplo = EJEMPLOS[tipo][indice]
            popup = Popup(title="¿Es correcta esta construcción?",
                          size_hint=(.9, .5))
            box = BoxLayout(orientation='vertical', spacing=10, padding=10)
            label = Label(text=ejemplo)
            botones = BoxLayout(size_hint_y=0.3, spacing=10)

            def responder(valor):
                nonlocal correctas
                if valor == (tipo == "correctas"):
                    correctas += 1
                popup.dismiss()
                preguntar(indice + 1)

            btn_si = Button(text="Sí")
            btn_si.bind(on_release=lambda _: responder(True))
            btn_no = Button(text="No")
            btn_no.bind(on_release=lambda _: responder(False))
            botones.add_widget(btn_si)
            botones.add_widget(btn_no)

            box.add_widget(label)
            box.add_widget(botones)
            popup.content = box
            popup.open()

        preguntar(0)

    def completar_oracion(self, instance):
        base = "Tengo tanto ___ más paciencia que tú."
        popup = Popup(title="Completa la oración", size_hint=(.9, .5))
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=base)
        respuesta = TextInput(multiline=False)
        botones = BoxLayout(size_hint_y=0.3)

        def verificar(_):
            correcto = respuesta.text.strip().lower() == "o"
            if correcto:
                self.popup("Correcto", "¡Bien hecho!")
                registrar_en_bitacora("completar", 1, 1)
                actualizar_estadisticas("completar", 1, 1)
            else:
                self.popup("Incorrecto", "La respuesta correcta era: 'o'")
                registrar_en_bitacora("completar", 0, 1)
                actualizar_estadisticas("completar", 0, 1)
            popup.dismiss()

        btn_verificar = Button(text="Verificar")
        btn_verificar.bind(on_release=verificar)

        layout.add_widget(label)
        layout.add_widget(respuesta)
        layout.add_widget(btn_verificar)
        popup.content = layout
        popup.open()

    def agregar_ejemplo(self, instance):
        popup = Popup(title="Agregar Ejemplo", size_hint=(.9, .6))
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        tipo_input = TextInput(hint_text="Tipo (correctas o incorrectas)", multiline=False)
        texto_input = TextInput(hint_text="Nuevo ejemplo", multiline=True)
        botones = BoxLayout(size_hint_y=0.3)

        def guardar(_):
            tipo = tipo_input.text.strip().lower()
            texto = texto_input.text.strip()
            if tipo in EJEMPLOS and texto:
                if len(EJEMPLOS[tipo]) < 100:
                    EJEMPLOS[tipo].append(texto)
                    guardar_ejemplos()
                    self.popup("Guardado", "Ejemplo guardado correctamente.")
                else:
                    self.popup("Error", "Ya hay 100 ejemplos en esta categoría.")
            else:
                self.popup("Error", "Tipo inválido o texto vacío.")
            popup.dismiss()

        btn_guardar = Button(text="Guardar")
        btn_guardar.bind(on_release=guardar)
        botones.add_widget(btn_guardar)

        layout.add_widget(tipo_input)
        layout.add_widget(texto_input)
        layout.add_widget(botones)
        popup.content = layout
        popup.open()

    def mostrar_estadisticas(self, instance):
        if os.path.exists(ESTADISTICAS_ARCHIVO):
            with open(ESTADISTICAS_ARCHIVO, "r", encoding="utf-8") as f:
                stats = json.load(f)
            resultado = ""
            for tipo, datos in stats.items():
                total = datos['total']
                correctas = datos['correctas']
                porcentaje = (correctas / total * 100) if total > 0 else 0
                resultado += f"{tipo.capitalize()}: {correctas}/{total} correctas ({porcentaje:.1f}%)\n"
            self.popup("Estadísticas", resultado)
        else:
            self.popup("Estadísticas", "No hay estadísticas disponibles todavía.")

if __name__ == '__main__':
    Window.size = (400, 600)
    SintaxisApp().run()
