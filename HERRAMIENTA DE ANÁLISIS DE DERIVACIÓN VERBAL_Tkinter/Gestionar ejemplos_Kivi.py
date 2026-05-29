from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, DictProperty
from kivy.storage.jsonstore import JsonStore
import json
import os

DATA_FILE = "verbos_kivy.json"
CATEGORIAS = {
    '1': "Epéntesis",
    '2': "Síncopa",
    '3': "Alternancias",
    '4': "Pretéritos Fuertes",
    '5': "Participios",
    '6': "Conjug. Especial",
    '7': "Defectivos"
}

class MainScreen(BoxLayout):
    spinner_categorias = ObjectProperty(None)
    lista_verbos = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store = JsonStore(DATA_FILE)
        self.cargar_datos()
        self.actualizar_lista()
    
    def cargar_datos(self):
        if not os.path.exists(DATA_FILE):
            datos_iniciales = {k: [] for k in CATEGORIAS}
            with open(DATA_FILE, 'w') as f:
                json.dump(datos_iniciales, f)
                
    def actualizar_lista(self, instance=None, value=None):
        self.lista_verbos.clear_widgets()
        cat = self.spinner_categorias.text
        key = [k for k, v in CATEGORIAS.items() if v == cat][0]
        
        for ejemplo in self.store.get(key)['value']:
            btn = Button(
                text=f"{ejemplo['verbo']}: {ejemplo['ejemplo'][:30]}...",
                size_hint_y=None,
                height=40
            )
            btn.ejemplo_data = ejemplo
            btn.bind(on_release=self.mostrar_detalle)
            self.lista_verbos.add_widget(btn)
    
    def mostrar_detalle(self, instance):
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text=f"Verbo: {instance.ejemplo_data['verbo']}"))
        content.add_widget(Label(text=f"Conjugación: {instance.ejemplo_data['conjugacion']}"))
        content.add_widget(Label(text=f"Ejemplo: {instance.ejemplo_data['ejemplo']}"))
        
        popup = Popup(
            title="Detalle del Ejemplo",
            content=content,
            size_hint=(0.8, 0.6)
        )
        popup.open()

class VerbosKivyApp(App):
    def build(self):
        self.title = "Gestor de Verbos Kivy"
        return MainScreen()

class EditarPopup(Popup):
    verbo = ObjectProperty(None)
    conjugacion = ObjectProperty(None)
    ejemplo = ObjectProperty(None)
    
    def __init__(self, callback=None, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback
    
    def guardar(self):
        if self.callback:
            self.callback({
                'verbo': self.verbo.text,
                'conjugacion': self.conjugacion.text,
                'ejemplo': self.ejemplo.text
            })
        self.dismiss()

class ProgressPopup(Popup):
    def __init__(self, datos, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=2, spacing=10)
        
        total = 0
        for cat in CATEGORIAS.values():
            key = [k for k, v in CATEGORIAS.items() if v == cat][0]
            cantidad = len(datos[key])
            total += cantidad
            layout.add_widget(Label(text=cat))
            layout.add_widget(Label(text=f"{cantidad}/100"))
        
        layout.add_widget(Label(text="TOTAL", bold=True))
        layout.add_widget(Label(text=f"{total}/700"))
        
        self.content = layout

# Funcionalidades CRUD
def agregar_ejemplo(main_screen):
    def guardar_ejemplo(datos):
        cat = main_screen.spinner_categorias.text
        key = [k for k, v in CATEGORIAS.items() if v == cat][0]
        
        if len(main_screen.store.get(key)['value']) >= 100:
            mostrar_error("Límite alcanzado", "Máximo 100 ejemplos por categoría")
            return
        
        nuevos_datos = main_screen.store.get(key)['value'] + [{
            'id': len(main_screen.store.get(key)['value']) + 1,
            **datos
        }]
        
        main_screen.store.put(key, value=nuevos_datos)
        main_screen.actualizar_lista()
    
    popup = EditarPopup(callback=guardar_ejemplo)
    popup.open()

def editar_ejemplo(main_screen, ejemplo):
    def actualizar_ejemplo(datos):
        cat = main_screen.spinner_categorias.text
        key = [k for k, v in CATEGORIAS.items() if v == cat][0]
        
        nuevos_datos = [d if d['id'] != ejemplo['id'] else {**d, **datos} 
                       for d in main_screen.store.get(key)['value']]
        
        main_screen.store.put(key, value=nuevos_datos)
        main_screen.actualizar_lista()
    
    popup = EditarPopup(callback=actualizar_ejemplo)
    popup.verbo.text = ejemplo['verbo']
    popup.conjugacion.text = ejemplo['conjugacion']
    popup.ejemplo.text = ejemplo['ejemplo']
    popup.open()

def mostrar_error(titulo, mensaje):
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text=mensaje))
    btn = Button(text="Cerrar", size_hint_y=0.2)
    popup = Popup(title=titulo, content=content)
    btn.bind(on_release=popup.dismiss)
    content.add_widget(btn)
    popup.open()

if __name__ == '__main__':
    VerbosKivyApp().run()
