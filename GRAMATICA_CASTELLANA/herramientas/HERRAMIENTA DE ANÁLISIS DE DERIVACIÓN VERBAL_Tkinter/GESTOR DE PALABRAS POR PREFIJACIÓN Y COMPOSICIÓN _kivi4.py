from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.recycleview import RecycleView
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder
import json

Builder.load_string('''
<RVRow@BoxLayout>:
    Label:
        text: root.texto
        size_hint_x: 0.3
    Label:
        text: root.tipo
        size_hint_x: 0.3
    Label:
        text: root.clasificacion
        size_hint_x: 0.2
    Label:
        text: root.significado
        size_hint_x: 0.2

<MainInterface>:
    orientation: 'vertical'
    TabbedPanel:
        id: tabs
        TabbedPanelItem:
            text: 'Prefijación'
            RV:
                id: rv_prefijos
                viewclass: 'RVRow'
                RecycleBoxLayout:
                    default_size: None, dp(40)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
        TabbedPanelItem:
            text: 'Composición'
            RV:
                id: rv_composiciones
                viewclass: 'RVRow'
                RecycleBoxLayout:
                    default_size: None, dp(40)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
    BoxLayout:
        size_hint_y: 0.1
        Button:
            text: 'Añadir'
            on_press: root.show_popup('add')
        Button:
            text: 'Editar'
            on_press: root.show_popup('edit')
        Button:
            text: 'Eliminar'
            on_press: root.delete_item()
        Button:
            text: 'Guardar'
            on_press: app.save_data()

<EditPopup>:
    title: 'Editar Ejemplo'
    size_hint: (0.9, 0.5)
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            id: campo1
            hint_text: 'Palabra'
        TextInput:
            id: campo2
            hint_text: 'Tipo/Prefijo'
        TextInput:
            id: campo3
            hint_text: 'Clasificación'
        TextInput:
            id: campo4
            hint_text: 'Significado'
        Button:
            text: 'Guardar'
            on_press: root.dismiss()
''')

class RV(RecycleView):
    data = ListProperty([])

class MainInterface(BoxLayout):
    current_tab = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.update_tabs()
    
    def update_tabs(self):
        self.ids.rv_prefijos.data = [
            {'texto': item['palabra'], 'tipo': item['prefijo'], 
             'clasificacion': item['clasificacion'], 'significado': item['significado']}
            for item in self.app.datos['prefijos']
        ]
        
        self.ids.rv_composiciones.data = [
            {'texto': item['palabra'], 'tipo': item['tipo'], 
             'clasificacion': item['clasificacion'], 'significado': item['significado']}
            for item in self.app.datos['composiciones']
        ]
    
    def show_popup(self, action):
        content = EditPopup()
        if action == 'edit':
            if not self.get_selected_item():
                return
            current = self.get_selected_item()
            content.ids.campo1.text = current['texto']
            content.ids.campo2.text = current['tipo']
            content.ids.campo3.text = current['clasificacion']
            content.ids.campo4.text = current['significado']
        
        popup = Popup(title='Nuevo Ejemplo' if action == 'add' else 'Editar Ejemplo',
                     content=content, size_hint=(0.8, 0.6))
        content.bind(on_dismiss=lambda x: self.save_changes(popup, action))
        popup.open()
    
    def save_changes(self, popup, action):
        campos = [popup.content.ids[f'campo{i}'].text for i in range(1,5)]
        if all(campos):
            if action == 'add':
                self.add_item(campos)
            else:
                self.edit_item(campos)
            self.update_tabs()
    
    def add_item(self, campos):
        tab = self.ids.tabs.current_tab.text
        new_item = {
            'palabra': campos[0],
            'prefijo' if tab == 'Prefijación' else 'tipo': campos[1],
            'clasificacion': campos[2],
            'significado': campos[3]
        }
        self.app.datos['prefijos' if tab == 'Prefijación' else 'composiciones'].append(new_item)
    
    def edit_item(self, campos):
        tab = self.ids.tabs.current_tab.text
        data = self.app.datos['prefijos' if tab == 'Prefijación' else 'composiciones']
        idx = self.get_selected_index()
        data[idx].update({
            'palabra': campos[0],
            'prefijo' if tab == 'Prefijación' else 'tipo': campos[1],
            'clasificacion': campos[2],
            'significado': campos[3]
        })
    
    def delete_item(self):
        tab = self.ids.tabs.current_tab.text
        idx = self.get_selected_index()
        if idx is not None:
            del self.app.datos['prefijos' if tab == 'Prefijación' else 'composiciones'][idx]
            self.update_tabs()
    
    def get_selected_index(self):
        rv = self.ids.rv_prefijos if self.ids.tabs.current_tab.text == 'Prefijación' else self.ids.rv_composiciones
        return rv.layout_manager.selected_index
    
    def get_selected_item(self):
        idx = self.get_selected_index()
        if idx is not None:
            tab = self.ids.tabs.current_tab.text
            return self.app.datos['prefijos' if tab == 'Prefijación' else 'composiciones'][idx]

class MorfologiaApp(App):
    datos = ListProperty()
    
    def build(self):
        self.load_data()
        return MainInterface()
    
    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                self.datos = json.load(f)
        except FileNotFoundError:
            self.datos = {
                "prefijos": [
                    {"palabra": "Antinuclear", "prefijo": "anti-", "clasificacion": "Oposición", "significado": "Contra energía nuclear"},
                    {"palabra": "Deshacer", "prefijo": "des-", "clasificacion": "Negación", "significado": "Revertir acción"}
                ],
                "composiciones": [
                    {"palabra": "Sacacorchos", "tipo": "Verbo+Sustantivo", "clasificacion": "Objeto-función", "significado": "Herramienta para corchos"},
                    {"palabra": "Agridulce", "tipo": "Adjetivo+Adjetivo", "clasificacion": "Característica", "significado": "Mezcla de sabores"}
                ]
            }
    
    def save_data(self):
        with open('data.json', 'w') as f:
            json.dump(self.datos, f, indent=2)

if __name__ == '__main__':
    MorfologiaApp().run()
