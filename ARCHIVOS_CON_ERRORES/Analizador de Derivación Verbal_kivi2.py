from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from collections import defaultdict
import json

Builder.load_string('''
<MainScreen>:
    do_default_tab: False
    background_color: 0.95, 0.95, 0.95, 1
    
    TabbedPanelItem:
        text: 'Análisis'
        BoxLayout:
            orientation: 'vertical'
            padding: 10
            spacing: 10
            
            BoxLayout:
                size_hint_y: None
                height: 50
                spacing: 10
                TextInput:
                    id: entrada_verbo
                    hint_text: 'Ingrese un verbo...'
                    size_hint_x: 0.7
                Button:
                    text: 'Analizar'
                    size_hint_x: 0.3
                    on_press: root.analizar_verbo()
            
            ScrollView:
                Label:
                    id: resultados
                    text_size: (self.width, None)
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding: 10, 10
                    markup: True
    
    TabbedPanelItem:
        text: 'Agregar'
        BoxLayout:
            orientation: 'vertical'
            padding: 10
            spacing: 10
            
            BoxLayout:
                orientation: 'vertical'
                spacing: 10
                size_hint_y: None
                height: 150
                
                TextInput:
                    id: nuevo_verbo
                    hint_text: 'Verbo'
                    size_hint_y: None
                    height: 40
                
                TextInput:
                    id: nuevo_patron
                    hint_text: 'Patrón (ej: -ear, a-N-ar)'
                    size_hint_y: None
                    height: 40
                
                TextInput:
                    id: nueva_region
                    hint_text: 'Región (opcional)'
                    size_hint_y: None
                    height: 40
            
            Button:
                text: 'Guardar Ejemplo'
                size_hint_y: None
                height: 50
                on_press: root.agregar_ejemplo()
    
    TabbedPanelItem:
        text: 'Ayuda'
        ScrollView:
            Label:
                text: root.texto_ayuda
                text_size: (self.width, None)
                size_hint_y: None
                height: self.texture_size[1]
                padding: 10, 10
                markup: True
''')

class MainScreen(TabbedPanel):
    texto_ayuda = '''
[b]Instrucciones de uso:[/b]

[color=000000]
1. [i]Análisis de verbos:[/i]
   • Ingrese un verbo en el campo de texto
   • Presione el botón "Analizar"
   • Revise los resultados en el área inferior

2. [i]Agregar nuevos ejemplos:[/i]
   • Complete todos los campos en la pestaña "Agregar"
   • Patrones válidos: -ar, -ear, a-N-ar, en-A-ecer, etc.
   • La región es opcional (ej: México, Andes)

3. [i]Consulta de ayuda:[/i]
   • Revise esta pestaña para dudas
   • Los datos se guardan automáticamente
[/color]'''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.analizador = DerivacionVerbal()
        self.cargar_datos()

    def cargar_datos(self):
        try:
            self.analizador.cargar_datos()
        except Exception as e:
            print("Error cargando datos:", str(e))

    def analizar_verbo(self):
        verbo = self.ids.entrada_verbo.text.strip().lower()
        if not verbo:
            self.ids.resultados.text = "[color=#ff0000]Error: Ingrese un verbo válido[/color]"
            return
        
        try:
            reporte = self.analizador.generar_informe(verbo)
            self.ids.resultados.text = reporte
        except Exception as e:
            self.ids.resultados.text = f"[color=#ff0000]Error en análisis: {str(e)}[/color]"

    def agregar_ejemplo(self):
        datos = {
            'verbo': self.ids.nuevo_verbo.text.strip(),
            'patron': self.ids.nuevo_patron.text.strip(),
            'region': self.ids.nueva_region.text.strip() or None
        }

        if not datos['verbo'] or not datos['patron']:
            self.ids.resultados.text = "[color=#ff0000]Error: Verbo y Patrón son obligatorios[/color]"
            return

        try:
            self.analizador.agregar_ejemplo(datos['verbo'], datos['patron'], datos['region'])
            self.limpiar_campos()
            self.ids.resultados.text = f"[color=#00aa00]✓ Ejemplo '{datos['verbo']}' agregado[/color]"
        except Exception as e:
            self.ids.resultados.text = f"[color=#ff0000]Error: {str(e)}[/color]"

    def limpiar_campos(self):
        self.ids.nuevo_verbo.text = ""
        self.ids.nuevo_patron.text = ""
        self.ids.nueva_region.text = ""

class DerivacionVerbalApp(App):
    def build(self):
        return MainScreen()

    def on_stop(self):
        self.root.analizador.guardar_datos()

class DerivacionVerbal:
    def __init__(self):
        self.store = JsonStore('datos_verbos.json')
        self.cargar_datos_base()
        self.cargar_datos()

    def cargar_datos_base(self):
        if not self.store.exists('ejemplos'):
            self._inicializar_datos()

    def _inicializar_datos(self):
        datos_iniciales = {
            'ejemplos': {
                '-ear': ['canturrear', 'matear', 'patear'],
                '-izar': ['argentinizar', 'computerizar'],
                'a-N-ar': ['abotonar', 'aterrizar'],
                'en-A-ecer': ['entristecer', 'enriquecer']
            },
            'variantes': {
                'diacronicas': {'enriquir': 'enriquecer', 'atristar': 'entristecer'},
                'diatopicas': {'concientizar': ['América'], 'liderizar': ['Región Andina']}
            }
        self.store.put('data', data=json.dumps(datos_iniciales))

    def cargar_datos(self):
        data = json.loads(self.store.get('data')['data'])
        self.ejemplos = data['ejemplos']
        self.variantes = data['variantes']

    def guardar_datos(self):
        data = {
            'ejemplos': self.ejemplos,
            'variantes': self.variantes
        }
        self.store.put('data', data=json.dumps(data))

    def agregar_ejemplo(self, verbo, patron, region=None):
        if patron not in self.ejemplos:
            self.ejemplos[patron] = []
        self.ejemplos[patron].append(verbo)
        
        if region:
            self.variantes['diatopicas'][verbo] = [region]

    def generar_informe(self, verbo):
        reporte = []
        reporte.append(f"[b][size=20]🔍 Análisis de: {verbo}[/size][/b]\n")
        
        # Análisis morfológico
        reporte.append("[b][size=16]1. Estructura morfológica:[/size][/b]")
        reporte.extend(self._analizar_morfologia(verbo))
        
        # Patrones
        reporte.append("\n[b][size=16]2. Patrones detectados:[/size][/b]")
        reporte.extend(self._detectar_patrones(verbo))
        
        # Variantes
        reporte.append("\n[b][size=16]3. Variantes registradas:[/size][/b]")
        reporte.extend(self._buscar_variantes(verbo))
        
        # Ejemplos
        reporte.append("\n[b][size=16]4. Ejemplos relacionados:[/size][/b]")
        reporte.extend(self._buscar_ejemplos(verbo))
        
        return '\n'.join(reporte)

    def _analizar_morfologia(self, verbo):
        sufijos = ['ar', 'ear', 'ecer', 'izar', 'ificar']
        analisis = []
        for sufijo in sufijos:
            if verbo.endswith(sufijo):
                base = verbo[:-len(sufijo)]
                analisis.append(f"   • [color=0044ff]{base}[/color] + [color=ff4400]-{sufijo}[/color]")
        return analisis or ["   - No se detectó estructura clara"]

    def _detectar_patrones(self, verbo):
        patrones = []
        for patron, ejemplos in self.ejemplos.items():
            if verbo in ejemplos:
                patrones.append(f"   • {patron}")
        return patrones or ["   - No coincide con patrones conocidos"]

    def _buscar_variantes(self, verbo):
        variantes = []
        if verbo in self.variantes['diacronicas']:
            variantes.append(f"   • Histórica: {self.variantes['diacronicas'][verbo]}")
        if verbo in self.variantes['diatopicas']:
            regiones = ', '.join(self.variantes['diatopicas'][verbo])
            variantes.append(f"   • Geográfica: {regiones}")
        return variantes or ["   - Sin variantes registradas"]

    def _buscar_ejemplos(self, verbo):
        relacionados = []
        for patron, ejemplos in self.ejemplos.items():
            if verbo in ejemplos:
                relacionados.extend([f"   • {e}" for e in ejemplos if e != verbo][:3])
        return relacionados or ["   - No se encontraron ejemplos relacionados"]

if __name__ == '__main__':
    DerivacionVerbalApp().run()
