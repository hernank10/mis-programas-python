import json
import os
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

FILE_NAME = "ejemplos.json"

def cargar_ejemplos():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_ejemplos(ejemplos):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(ejemplos, f, indent=4, ensure_ascii=False)

class MenuScreen(Screen):
    pass

class VerEjemplosScreen(Screen):
    list_container = ObjectProperty(None)

    def on_enter(self):
        self.mostrar_ejemplos()

    def mostrar_ejemplos(self):
        self.list_container.clear_widgets()
        ejemplos = self.manager.ejemplos
        if not ejemplos:
            self.list_container.add_widget(Label(text="No hay ejemplos guardados."))
            return
        
        for ejemplo in ejemplos:
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
            box.add_widget(Label(text=f"[b]ID:[/b] {ejemplo['id']}", markup=True))
            box.add_widget(Label(text=f"Español: {ejemplo['es']}"))
            box.add_widget(Label(text=f"Inglés: {ejemplo['en']}"))
            box.add_widget(Label(text=f"Francés: {ejemplo['fr']}"))
            
            # Botón para editar
            edit_btn = Button(text="Editar", size_hint_y=None, height=30)
            edit_btn.bind(on_release=lambda btn, id=ejemplo['id']: self.manager.goto_editar(id))
            box.add_widget(edit_btn)
            
            self.list_container.add_widget(box)
            self.list_container.add_widget(Label(size_hint_y=None, height=20)) # Separador

class AgregarScreen(Screen):
    es_input = ObjectProperty(None)
    en_input = ObjectProperty(None)
    fr_input = ObjectProperty(None)

    def guardar_ejemplo(self):
        ejemplos = self.manager.ejemplos
        es = self.es_input.text
        en = self.en_input.text
        fr = self.fr_input.text

        if not es or not en or not fr:
            self.mostrar_popup("Error", "Todos los campos son obligatorios.")
            return

        nuevo_id = 1
        if ejemplos:
            nuevo_id = max(e['id'] for e in ejemplos) + 1
        
        ejemplos.append({"id": nuevo_id, "es": es, "en": en, "fr": fr})
        guardar_ejemplos(ejemplos)
        
        self.es_input.text = ""
        self.en_input.text = ""
        self.fr_input.text = ""

        self.mostrar_popup("Éxito", "Ejemplo guardado correctamente.")

    def mostrar_popup(self, title, text):
        popup = Popup(title=title, content=Label(text=text), size_hint=(0.8, 0.4))
        popup.open()

class EditarScreen(Screen):
    es_input = ObjectProperty(None)
    en_input = ObjectProperty(None)
    fr_input = ObjectProperty(None)
    ejemplo_id = None

    def on_enter(self):
        self.cargar_ejemplo_para_editar()

    def cargar_ejemplo_para_editar(self):
        ejemplos = self.manager.ejemplos
        ejemplo = next((e for e in ejemplos if e['id'] == self.ejemplo_id), None)
        if ejemplo:
            self.es_input.text = ejemplo['es']
            self.en_input.text = ejemplo['en']
            self.fr_input.text = ejemplo['fr']
        else:
            self.manager.current = "ver_ejemplos"

    def guardar_cambios(self):
        ejemplos = self.manager.ejemplos
        ejemplo = next((e for e in ejemplos if e['id'] == self.ejemplo_id), None)
        
        if ejemplo:
            ejemplo['es'] = self.es_input.text
            ejemplo['en'] = self.en_input.text
            ejemplo['fr'] = self.fr_input.text
            guardar_ejemplos(ejemplos)
            self.manager.current = "ver_ejemplos"

class PracticarScreen(Screen):
    pregunta_label = ObjectProperty(None)
    en_input = ObjectProperty(None)
    fr_input = ObjectProperty(None)
    es_respuesta = None

    def on_enter(self):
        self.siguiente_pregunta()

    def siguiente_pregunta(self):
        ejemplos = self.manager.ejemplos
        if not ejemplos:
            self.pregunta_label.text = "No hay ejemplos para practicar."
            self.en_input.text = ""
            self.fr_input.text = ""
            self.en_input.disabled = True
            self.fr_input.disabled = True
            return

        ejemplo_actual = random.choice(ejemplos)
        self.es_respuesta = ejemplo_actual['es']
        self.pregunta_label.text = f"Traduce la siguiente frase en inglés y francés:\n\n[b]Español:[/b] {self.es_respuesta}"
        self.en_input.text = ""
        self.fr_input.text = ""
        self.en_input.disabled = False
        self.fr_input.disabled = False

    def revisar_respuesta(self):
        ejemplos = self.manager.ejemplos
        ejemplo = next((e for e in ejemplos if e['es'] == self.es_respuesta), None)
        
        if not ejemplo:
            return

        respuesta_en = self.en_input.text
        respuesta_fr = self.fr_input.text

        msg = f"Respuesta correcta:\nInglés: {ejemplo['en']}\nFrancés: {ejemplo['fr']}"
        
        popup = Popup(title="Revisar", content=Label(text=msg), size_hint=(0.8, 0.4))
        popup.open()
        
class EjemplosApp(App):
    ejemplos = []

    def build(self):
        self.ejemplos = cargar_ejemplos()
        sm = ScreenManager()
        sm.ejemplos = self.ejemplos
        
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(VerEjemplosScreen(name="ver_ejemplos"))
        sm.add_widget(AgregarScreen(name="agregar"))
        sm.add_widget(EditarScreen(name="editar"))
        sm.add_widget(PracticarScreen(name="practicar"))
        
        sm.goto_editar = self.goto_editar
        return sm

    def goto_editar(self, ejemplo_id):
        self.root.get_screen("editar").ejemplo_id = ejemplo_id
        self.root.current = "editar"

if __name__ == "__main__":
    EjemplosApp().run()
