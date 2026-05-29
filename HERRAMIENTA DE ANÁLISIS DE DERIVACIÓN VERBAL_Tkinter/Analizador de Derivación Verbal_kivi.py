from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from collections import defaultdict
import json

Builder.load_string('''
<MainScreen>:
    TabbedPanel:
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

1. [i]Análisis de verbos:[/i]
   • Ingrese un verbo en el campo de texto
   • Presione el botón "Analizar"

2. [i]Agregar ejemplos:[/i]
   • Complete los campos en la pestaña "Agregar"
   • Los patrones deben seguir la notación:
     ej: -ear, a-N-ar, en-A-ecer

3. [i]Datos:[/i]
   • Se guardan automáticamente al cerrar
   • Se cargan al iniciar la aplicación'''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.analizador = DerivacionVerbal()
        self.cargar_datos()

    def cargar_datos(self):
        try:
            self.analizador.cargar_datos()
        except Exception as e:
            print(f"Error cargando datos: {str(e)}")

    def analizar_verbo(self):
        verbo = self.ids.entrada_verbo.text.strip().lower()
        if not verbo:
            self.actualizar_resultados("[color=#ff0000]Error: Ingrese un verbo válido[/color]")
            return
        
        reporte = self.analizador.generar_informe_gui(verbo)
        self.actualizar_resultados(reporte)

    def agregar_ejemplo(self):
        verbo = self.ids.nuevo_verbo.text.strip()
        patron = self.ids.nuevo_patron.text.strip()
        region = self.ids.nueva_region.text.strip() or None

        if not verbo or not patron:
            self.actualizar_resultados("[color=#ff0000]Error: Verbo y Patrón son obligatorios[/color]")
            return

        self.analizador.agregar_ejemplo(verbo, patron, region)
        self.limpiar_campos()
        self.actualizar_resultados(f"[color=#00aa00]Ejemplo '{verbo}' agregado correctamente[/color]")

    def actualizar_resultados(self, texto):
        self.ids.resultados.text = texto

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
        self.patrones = {
            'sufijos_comunes': ['-ar', '-ear', '-ecer', '-izar', '-ificar'],
            'parasintesis': ['a-...-ar', 'en-...-ar', 'des-...-ar'],
            'interfijos': ['-ec-', '-ific-', '-iz-']
        }
        self.cargar_datos_base()

    def cargar_datos_base(self):
        if not self.store.exists('ejemplos'):
            self.store.put('ejemplos', 
                ejemplos=json.dumps({
                    '-ear': ['canturrear', 'matear', 'patear'],
                    '-izar': ['argentinizar', 'computerizar'],
                    'a-N-ar': ['abotonar', 'aterrizar'],
                    'en-A-ecer': ['entristecer', 'enriquecer']
                })
            )
            
        if not self.store.exists('variantes'):
            self.store.put('variantes',
                diacronicas=json.dumps({
                    'enriquir': 'enriquecer',
                    'atristar': 'entristecer'
                }),
                diatopicas=json.dumps({
                    'concientizar': ['América'],
                    'liderizar': ['Región Andina']
                })
            )

    def cargar_datos(self):
        try:
            self.ejemplos = json.loads(self.store.get('ejemplos')['ejemplos'])
            self.variantes = {
                'diacronicas': json.loads(self.store.get('variantes')['diacronicas']),
                'diatopicas': json.loads(self.store.get('variantes')['diatopicas'])
            }
        except Exception as e:
            print(f"Error cargando datos: {str(e)}")

    def guardar_datos(self):
        try:
            self.store.put('ejemplos', ejemplos=json.dumps(self.ejemplos))
            self.store.put('variantes',
                diacronicas=json.dumps(self.variantes['diacronicas']),
                diatopicas=json.dumps(self.variantes['diatopicas'])
            )
        except Exception as e:
            print(f"Error guardando datos: {str(e)}")

    def generar_informe_gui(self, verbo):
        reporte = []
        reporte.append(f"[b]🔍 Análisis de: {verbo}[/b]\n")
        
        # Bases y afijos
        bases = self.identificar_bases(verbo)
        reporte.append("[b]1. BASES Y AFIJOS:[/b]")
        for base, sufijo in bases:
            reporte.append(f"   - [i]Base:[/i] {base.ljust(15)} [i]Sufijo:[/i] {sufijo}")
        
        # Patrones
        patrones = self.analizar_patron(verbo)
        reporte.append("\n[b]2. PATRONES DETECTADOS:[/b]")
        for p in patrones:
            reporte.append(f"   - {p}")
        
        # Variantes
        variantes = self.verificar_variacion(verbo)
        reporte.append("\n[b]3. VARIACIÓN:[/b]")
        if variantes:
            for v in variantes:
                reporte.append(f"   - {v}")
        else:
            reporte.append("   - No se registran variantes")
        
        # Ejemplos relacionados
        reporte.append("\n[b]4. EJEMPLOS RELACIONADOS:[/b]")
        encontrados = False
        for patron, ejemplos in self.ejemplos.items():
            if verbo in ejemplos:
                encontrados = True
                reporte.append(f"   - Ejemplo de [i]{patron}[/i]:")
                reporte.append(f"     {', '.join(e for e in ejemplos if e != verbo)[:50]}...")
        if not encontrados:
            reporte.append("   - No se encontraron ejemplos relacionados")
        
        return '\n'.join(reporte)

    # Mantener los mismos métodos de análisis que en versiones anteriores
    # ... [Los métodos restantes son similares a la versión anterior]

if __name__ == '__main__':
    DerivacionVerbalApp().run()
