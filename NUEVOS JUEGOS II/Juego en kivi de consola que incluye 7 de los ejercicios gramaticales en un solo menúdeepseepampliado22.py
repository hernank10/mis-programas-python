from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import random
import time

# Datos de los juegos (los mismos que en la versión consola)
oraciones_sujeto_predicado = [
    {"oracion": "El niño juega en el parque", "sujeto": "El niño", "predicado": "juega en el parque"},
    {"oracion": "María estudia matemáticas", "sujeto": "María", "predicado": "estudia matemáticas"},
    # ... (todos los datos anteriores)
]

# Clase para la pantalla principal
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Título
        title = Label(
            text='JUEGOS GRAMATICALES - ESPAÑOL/INGLÉS',
            font_size='24sp',
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)
        
        # Botones de juegos
        games_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.8))
        
        games = [
            ('🎯 Cazador de Sujeto', 'sujeto'),
            ('🧩 Puzzle de Oración', 'puzzle'),
            ('📊 Clasifica Oración', 'clasifica'),
            ('✏️ Corrector Oraciones', 'corrector'),
            ('🧱 Construye Oración', 'construye'),
            ('🏎️ Carrera Conectores', 'carrera'),
            ('🛡️ Defiende Gramática', 'defensa')
        ]
        
        for game_name, game_id in games:
            btn = Button(
                text=game_name,
                font_size='18sp',
                background_color=(0.2, 0.6, 0.8, 1)
            )
            btn.bind(on_press=lambda instance, id=game_id: self.go_to_game(id))
            games_layout.add_widget(btn)
        
        layout.add_widget(games_layout)
        self.add_widget(layout)
    
    def go_to_game(self, game_id):
        self.manager.current = game_id

# Clase para el juego de Sujeto y Predicado
class SujetoPredicadoScreen(Screen):
    def __init__(self, **kwargs):
        super(SujetoPredicadoScreen, self).__init__(**kwargs)
        self.puntaje = 0
        self.pregunta_actual = 0
        self.setup_ui()
    
    def setup_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        btn_back = Button(text='← Volver', size_hint=(0.2, 1))
        btn_back.bind(on_press=self.go_back)
        title = Label(text='🎯 Cazador de Sujeto y Predicado', font_size='20sp')
        header.add_widget(btn_back)
        header.add_widget(title)
        layout.add_widget(header)
        
        # Contenido del juego
        self.content = BoxLayout(orientation='vertical', spacing=15)
        layout.add_widget(self.content)
        
        self.add_widget(layout)
        self.cargar_pregunta()
    
    def cargar_pregunta(self):
        self.content.clear_widgets()
        
        if self.pregunta_actual >= len(oraciones_sujeto_predicado):
            self.mostrar_resultado()
            return
        
        pregunta = oraciones_sujeto_predicado[self.pregunta_actual]
        
        # Oración
        lbl_oracion = Label(
            text=f'Oración: {pregunta["oracion"]}',
            font_size='18sp',
            size_hint=(1, 0.3)
        )
        self.content.add_widget(lbl_oracion)
        
        # Inputs para sujeto y predicado
        self.input_sujeto = TextInput(
            hint_text='Escribe el sujeto aquí...',
            size_hint=(1, 0.2),
            multiline=False
        )
        self.content.add_widget(self.input_sujeto)
        
        self.input_predicado = TextInput(
            hint_text='Escribe el predicado aquí...',
            size_hint=(1, 0.2),
            multiline=False
        )
        self.content.add_widget(self.input_predicado)
        
        # Botón de verificación
        btn_verificar = Button(
            text='Verificar Respuesta',
            size_hint=(1, 0.2),
            background_color=(0.2, 0.8, 0.2, 1)
        )
        btn_verificar.bind(on_press=self.verificar_respuesta)
        self.content.add_widget(btn_verificar)
    
    def verificar_respuesta(self, instance):
        pregunta = oraciones_sujeto_predicado[self.pregunta_actual]
        sujeto_usuario = self.input_sujeto.text.strip()
        predicado_usuario = self.input_predicado.text.strip()
        
        correcto_sujeto = sujeto_usuario.lower() == pregunta["sujeto"].lower()
        correcto_predicado = predicado_usuario.lower() == pregunta["predicado"].lower()
        
        mensaje = ""
        if correcto_sujeto and correcto_predicado:
            mensaje = "✅ ¡Ambas respuestas correctas!"
            self.puntaje += 2
        elif correcto_sujeto:
            mensaje = "✅ Sujeto correcto, ❌ Predicado incorrecto"
            self.puntaje += 1
        elif correcto_predicado:
            mensaje = "❌ Sujeto incorrecto, ✅ Predicado correcto"
            self.puntaje += 1
        else:
            mensaje = "❌ Ambas respuestas incorrectas"
        
        # Mostrar popup con resultado
        popup = Popup(
            title='Resultado',
            content=Label(text=f'{mensaje}\n\nSujeto: {pregunta["sujeto"]}\nPredicado: {pregunta["predicado"]}'),
            size_hint=(0.8, 0.4)
        )
        popup.open()
        
        # Siguiente pregunta después de 2 segundos
        Clock.schedule_once(lambda dt: self.siguiente_pregunta(), 2)
    
    def siguiente_pregunta(self):
        self.pregunta_actual += 1
        self.cargar_pregunta()
    
    def mostrar_resultado(self):
        self.content.clear_widgets()
        resultado = Label(
            text=f'🎉 Juego Terminado!\nPuntuación: {self.puntaje}/{len(oraciones_sujeto_predicado)*2}',
            font_size='20sp'
        )
        self.content.add_widget(resultado)
        
        btn_reiniciar = Button(text='Jugar Again', size_hint=(1, 0.2))
        btn_reiniciar.bind(on_press=self.reiniciar_juego)
        self.content.add_widget(btn_reiniciar)
    
    def reiniciar_juego(self, instance):
        self.puntaje = 0
        self.pregunta_actual = 0
        self.cargar_pregunta()
    
    def go_back(self, instance):
        self.manager.current = 'main'

# Clase para el juego de Puzzle de Oración
class PuzzleOracionScreen(Screen):
    def __init__(self, **kwargs):
        super(PuzzleOracionScreen, self).__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header similar al anterior...
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        btn_back = Button(text='← Volver', size_hint=(0.2, 1))
        btn_back.bind(on_press=self.go_back)
        title = Label(text='🧩 Puzzle de la Oración', font_size='20sp')
        header.add_widget(btn_back)
        header.add_widget(title)
        layout.add_widget(header)
        
        # Implementar lógica del puzzle...
        content = Label(text='Próximamente: Puzzle de Oración')
        layout.add_widget(content)
        
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'main'

# Clase para la Carrera de Conectores (ejemplo más complejo)
class CarreraConectoresScreen(Screen):
    def __init__(self, **kwargs):
        super(CarreraConectoresScreen, self).__init__(**kwargs)
        self.posicion = 0
        self.meta = 15
        self.pregunta_actual = 0
        self.setup_ui()
    
    def setup_ui(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        btn_back = Button(text='← Volver', size_hint=(0.2, 1))
        btn_back.bind(on_press=self.go_back)
        title = Label(text='🏎️ Carrera de Conectores', font_size='20sp')
        header.add_widget(btn_back)
        header.add_widget(title)
        self.layout.add_widget(header)
        
        # Pista de carreras
        self.pista_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3))
        self.actualizar_pista()
        self.layout.add_widget(self.pista_layout)
        
        # Área de pregunta
        self.pregunta_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.6))
        self.layout.add_widget(self.pregunta_layout)
        
        self.add_widget(self.layout)
        self.cargar_pregunta()
    
    def actualizar_pista(self):
        self.pista_layout.clear_widgets()
        
        # Crear representación visual de la pista
        pista_label = Label(
            text=f'Posición: {self.posicion}/{self.meta}',
            font_size='16sp'
        )
        self.pista_layout.add_widget(pista_label)
        
        # Barra de progreso visual
        progreso = self.posicion / self.meta
        progress_bar = ProgressBar(max=self.meta, value=self.posicion, size_hint=(1, 0.2))
        self.pista_layout.add_widget(progress_bar)
        
        # Indicadores visuales
        indicadores = GridLayout(cols=5, size_hint=(1, 0.3))
        for i in range(5):
            estado = "🏁" if i == 4 else "●" if i <= progreso * 4 else "○"
            indicadores.add_widget(Label(text=estado, font_size='20sp'))
        self.pista_layout.add_widget(indicadores)
    
    def cargar_pregunta(self):
        self.pregunta_layout.clear_widgets()
        
        # Aquí cargarías una pregunta real de carrera_conectores
        pregunta_ejemplo = {
            "contexto": "No fui a la fiesta ______ estaba enfermo",
            "opciones": ["porque", "pero", "aunque"],
            "correcta": 0
        }
        
        lbl_contexto = Label(
            text=pregunta_ejemplo["contexto"],
            font_size='18sp',
            size_hint=(1, 0.4)
        )
        self.pregunta_layout.add_widget(lbl_contexto)
        
        # Botones de opciones
        opciones_layout = GridLayout(cols=1, spacing=10, size_hint=(1, 0.6))
        for i, opcion in enumerate(pregunta_ejemplo["opciones"]):
            btn = Button(
                text=opcion,
                font_size='16sp'
            )
            btn.bind(on_press=lambda instance, idx=i: self.verificar_respuesta(idx))
            opciones_layout.add_widget(btn)
        
        self.pregunta_layout.add_widget(opciones_layout)
    
    def verificar_respuesta(self, opcion_seleccionada):
        # Lógica de verificación (simplificada)
        if opcion_seleccionada == 0:  # Respuesta correcta
            self.posicion += 3
            mensaje = "✅ Correcto! +3 posiciones"
        else:
            self.posicion = max(0, self.posicion - 1)
            mensaje = "❌ Incorrecto! -1 posición"
        
        self.actualizar_pista()
        
        # Mostrar resultado
        popup = Popup(
            title='Resultado',
            content=Label(text=mensaje),
            size_hint=(0.6, 0.3)
        )
        popup.open()
        
        # Verificar si ganó
        if self.posicion >= self.meta:
            Clock.schedule_once(lambda dt: self.mostrar_victoria(), 1)
        else:
            Clock.schedule_once(lambda dt: self.siguiente_pregunta(), 1)
    
    def siguiente_pregunta(self):
        self.pregunta_actual += 1
        self.cargar_pregunta()
    
    def mostrar_victoria(self):
        popup = Popup(
            title='🎉 ¡Victoria!',
            content=Label(text='¡Has ganado la carrera de conectores!'),
            size_hint=(0.8, 0.4)
        )
        popup.open()
    
    def go_back(self, instance):
        self.manager.current = 'main'

# Screen Manager principal
class GramaticaApp(App):
    def build(self):
        self.sm = ScreenManager(transition=SlideTransition())
        
        # Agregar todas las pantallas
        screens = [
            ('main', MainScreen(name='main')),
            ('sujeto', SujetoPredicadoScreen(name='sujeto')),
            ('puzzle', PuzzleOracionScreen(name='puzzle')),
            ('carrera', CarreraConectoresScreen(name='carrera'))
        ]
        
        for screen_id, screen in screens:
            self.sm.add_widget(screen)
        
        return self.sm

if __name__ == '__main__':
    GramaticaApp().run()
