from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
import json

reglas = []

class DerivacionForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=5, padding=10, **kwargs)

        self.inputs = {}

        campos = [
            "Verbo derivado", "Base léxica", "Afijo derivativo",
            "Patrón morfológico", "Descripción del patrón",
            "Variación (tipo)", "Detalle de la variación",
            "Caso (prototípico/excepción)", "Ejemplo del caso",
            "Regla redactada"
        ]

        for campo in campos:
            self.add_widget(Label(text=campo))
            self.inputs[campo] = TextInput(multiline=False)
            self.add_widget(self.inputs[campo])

        self.btn_guardar = Button(text="Guardar Regla", size_hint_y=None, height=40)
        self.btn_guardar.bind(on_press=self.guardar_regla)
        self.add_widget(self.btn_guardar)

        self.btn_ver = Button(text="Ver Reglas Guardadas", size_hint_y=None, height=40)
        self.btn_ver.bind(on_press=self.mostrar_reglas)
        self.add_widget(self.btn_ver)

        self.btn_exportar = Button(text="Exportar a JSON", size_hint_y=None, height=40)
        self.btn_exportar.bind(on_press=self.exportar_json)
        self.add_widget(self.btn_exportar)

    def guardar_regla(self, instance):
        datos = {k: v.text for k, v in self.inputs.items()}
        if not datos["Verbo derivado"] or not datos["Base léxica"] or not datos["Afijo derivativo"]:
            self.mostrar_popup("Error", "Debes llenar al menos el verbo, la base y el afijo.")
            return

        regla = {
            "verbo": datos["Verbo derivado"],
            "base": datos["Base léxica"],
            "afijo": datos["Afijo derivativo"],
            "patron": datos["Patrón morfológico"],
            "descripcion_patron": datos["Descripción del patrón"],
            "variacion": {"tipo": datos["Variación (tipo)"], "detalle": datos["Detalle de la variación"]},
            "caso": {"tipo": datos["Caso (prototípico/excepción)"], "ejemplo": datos["Ejemplo del caso"]},
            "regla_redactada": datos["Regla redactada"]
        }

        reglas.append(regla)
        self.mostrar_popup("Guardado", "Regla añadida con éxito.")
        for campo in self.inputs.values():
            campo.text = ""

    def mostrar_reglas(self, instance):
        if not reglas:
            self.mostrar_popup("Sin reglas", "Aún no has registrado ninguna regla.")
            return

        texto = ""
        for i, r in enumerate(reglas):
            texto += f"[{i+1}] {r['verbo']} = {r['base']} + {r['afijo']}\n"
            texto += f"  Patrón: {r['patron']} ({r['descripcion_patron']})\n"
            texto += f"  Variación: {r['variacion']['tipo']} - {r['variacion']['detalle']}\n"
            texto += f"  Caso: {r['caso']['tipo']} - {r['caso']['ejemplo']}\n"
            texto += f"  Regla: {r['regla_redactada']}\n\n"

        content = Label(text=texto, size_hint_y=None)
        content.bind(texture_size=content.setter('size'))
        scroll = ScrollView(size_hint=(1, None), size=(400, 400))
        scroll.add_widget(content)

        popup = Popup(title='Reglas Registradas', content=scroll, size_hint=(0.9, 0.9))
        popup.open()

    def exportar_json(self, instance):
        with open("reglas_kivy.json", "w", encoding="utf-8") as f:
            json.dump(reglas, f, indent=4, ensure_ascii=False)
        self.mostrar_popup("Exportado", "Reglas guardadas en reglas_kivy.json.")

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(title=titulo, content=Label(text=mensaje), size_hint=(0.7, 0.4))
        popup.open()

class DerivacionApp(App):
    def build(self):
        return DerivacionForm()

if __name__ == "__main__":
    DerivacionApp().run()
