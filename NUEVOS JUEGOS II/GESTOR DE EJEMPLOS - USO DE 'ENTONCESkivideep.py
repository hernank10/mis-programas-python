from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
import sqlite3
import os
from datetime import datetime

# Configuración de la ventana
Window.clearcolor = (0.95, 0.95, 0.95, 1)
Window.min_width = 800
Window.min_height = 600

class DatabaseManager:
    """Manejador de la base de datos"""
    def __init__(self, db_name="ejemplos_entonces.db"):
        self.db_name = db_name
        self.init_db()
        self.cargar_ejemplos_iniciales()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ejemplos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria TEXT NOT NULL,
                espanol TEXT NOT NULL,
                ingles TEXT NOT NULL,
                frances TEXT NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def cargar_ejemplos_iniciales(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM ejemplos")
        if cursor.fetchone()[0] == 0:
            ejemplos = [
                # Ejemplos temporales
                ("temporal", "Mi abuelo, en aquel entonces, era carpintero.", 
                 "My grandfather, back then, was a carpenter.", 
                 "Mon grand-père, à l'époque, était menuisier."),
                ("temporal", "La tecnología de entonces era mucho más simple.", 
                 "The technology of that time was much simpler.", 
                 "La technologie d'alors était beaucoup plus simple."),
                ("temporal", "Éramos muy felices entonces.", 
                 "We were very happy then.", 
                 "Nous étions très heureux alors."),
                
                # Ejemplos consecutivos
                ("consecutivo", "Está lloviendo; entonces, nos quedaremos en casa.", 
                 "It's raining; therefore, we will stay home.", 
                 "Il pleut ; donc, nous resterons à la maison."),
                ("consecutivo", "No tengo dinero, entonces no puedo ir al cine.", 
                 "I have no money, so I can't go to the movies.", 
                 "Je n'ai pas d'argent, donc je ne peux pas aller au cinéma."),
                
                # Ejemplos discursivos
                ("discursivo", "Entonces... ¿qué iba diciendo? Ah, sí, hablaba de mi viaje.", 
                 "So... what was I saying? Oh, right, I was talking about my trip.", 
                 "Alors... où en étais-je ? Ah, oui, je parlais de mon voyage."),
                ("discursivo", "Bueno, entonces, empecemos la reunión.", 
                 "Well then, let's start the meeting.", 
                 "Bon alors, commençons la réunion."),
            ]
            cursor.executemany('''
                INSERT INTO ejemplos (categoria, espanol, ingles, frances)
                VALUES (?, ?, ?, ?)
            ''', ejemplos)
            conn.commit()
        conn.close()

    def obtener_ejemplos(self, categoria=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        if categoria and categoria != "todas":
            cursor.execute('''
                SELECT id, categoria, espanol, ingles, frances 
                FROM ejemplos WHERE categoria = ? ORDER BY id
            ''', (categoria,))
        else:
            cursor.execute('''
                SELECT id, categoria, espanol, ingles, frances 
                FROM ejemplos ORDER BY id
            ''')
        resultados = cursor.fetchall()
        conn.close()
        return resultados

    def agregar_ejemplo(self, categoria, espanol, ingles, frances):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ejemplos (categoria, espanol, ingles, frances)
            VALUES (?, ?, ?, ?)
        ''', (categoria, espanol, ingles, frances))
        conn.commit()
        conn.close()
        return True

    def editar_ejemplo(self, id_ejemplo, categoria, espanol, ingles, frances):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE ejemplos 
            SET categoria = ?, espanol = ?, ingles = ?, frances = ?
            WHERE id = ?
        ''', (categoria, espanol, ingles, frances, id_ejemplo))
        conn.commit()
        conn.close()
        return True

    def eliminar_ejemplo(self, id_ejemplo):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ejemplos WHERE id = ?", (id_ejemplo,))
        conn.commit()
        conn.close()
        return True

    def obtener_estadisticas(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM ejemplos")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT categoria, COUNT(*) FROM ejemplos GROUP BY categoria")
        stats = cursor.fetchall()
        conn.close()
        return total, stats

class MenuPrincipal(Screen):
    """Pantalla del menú principal"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Título
        titulo = Label(
            text="🎓 Gestor de Ejemplos - Uso de 'Entonces'",
            font_size='24sp',
            size_hint_y=0.2,
            color=(0.2, 0.2, 0.2, 1)
        )
        layout.add_widget(titulo)
        
        # Botones del menú
        botones_layout = GridLayout(cols=2, spacing=15, size_hint_y=0.8)
        
        botones = [
            ("📖 Ver Ejemplos", "ver_ejemplos"),
            ("🔍 Buscar por Categoría", "buscar_categoria"),
            ("➕ Agregar Ejemplo", "agregar_ejemplo"),
            ("✏️ Editar Ejemplos", "editar_ejemplos"),
            ("🎯 Modo Práctica", "modo_practica"),
            ("📊 Estadísticas", "estadisticas"),
            ("💾 Exportar", "exportar"),
            ("❌ Salir", "salir")
        ]
        
        for texto, accion in botones:
            btn = Button(
                text=texto,
                font_size='18sp',
                background_color=(0.2, 0.6, 0.8, 1),
                size_hint_y=None,
                height=60
            )
            btn.bind(on_press=lambda x, a=accion: self.ir_a_pantalla(a))
            botones_layout.add_widget(btn)
        
        layout.add_widget(botones_layout)
        self.add_widget(layout)
    
    def ir_a_pantalla(self, pantalla):
        if pantalla == "salir":
            App.get_running_app().stop()
        else:
            self.manager.current = pantalla

class VerEjemplosScreen(Screen):
    """Pantalla para ver todos los ejemplos"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Barra superior
        top_bar = BoxLayout(size_hint_y=0.1)
        btn_volver = Button(text="← Volver", size_hint_x=0.2)
        btn_volver.bind(on_press=self.volver)
        titulo = Label(text="📚 Todos los Ejemplos", font_size='20sp')
        top_bar.add_widget(btn_volver)
        top_bar.add_widget(titulo)
        self.layout.add_widget(top_bar)
        
        # Área de scroll para los ejemplos
        scroll = ScrollView()
        self.ejemplos_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.ejemplos_layout.bind(minimum_height=self.ejemplos_layout.setter('height'))
        scroll.add_widget(self.ejemplos_layout)
        self.layout.add_widget(scroll)
        
        self.add_widget(self.layout)
        self.cargar_ejemplos()
    
    def cargar_ejemplos(self, categoria=None):
        self.ejemplos_layout.clear_widgets()
        ejemplos = self.db.obtener_ejemplos(categoria)
        
        for id_ej, cat, esp, ing, fr in ejemplos:
            ejemplo_box = BoxLayout(
                orientation='vertical', 
                size_hint_y=None, 
                height=150,
                padding=10,
                spacing=5
            )
            
            # Encabezado con ID y categoría
            header = BoxLayout(size_hint_y=0.2)
            header.add_widget(Label(text=f"ID: {id_ej}", size_hint_x=0.3))
            header.add_widget(Label(text=f"Categoría: {cat}", size_hint_x=0.7))
            ejemplo_box.add_widget(header)
            
            # Textos en los tres idiomas
            ejemplo_box.add_widget(Label(text=f"🇪🇸 {esp}", size_hint_y=0.3))
            ejemplo_box.add_widget(Label(text=f"🇬🇧 {ing}", size_hint_y=0.3))
            ejemplo_box.add_widget(Label(text=f"🇫🇷 {fr}", size_hint_y=0.3))
            
            self.ejemplos_layout.add_widget(ejemplo_box)
    
    def volver(self, instance):
        self.manager.current = "menu_principal"

class BuscarCategoriaScreen(Screen):
    """Pantalla para buscar por categoría"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Barra superior
        top_bar = BoxLayout(size_hint_y=0.1)
        btn_volver = Button(text="← Volver", size_hint_x=0.2)
        btn_volver.bind(on_press=self.volver)
        titulo = Label(text="🔍 Buscar por Categoría", font_size='20sp')
        top_bar.add_widget(btn_volver)
        top_bar.add_widget(titulo)
        layout.add_widget(top_bar)
        
        # Selector de categoría
        categorias_box = BoxLayout(size_hint_y=0.1, spacing=10)
        categorias_box.add_widget(Label(text="Categoría:"))
        self.spinner = Spinner(
            text='todas',
            values=('todas', 'temporal', 'consecutivo', 'discursivo'),
            size_hint_x=0.6
        )
        categorias_box.add_widget(self.spinner)
        
        btn_buscar = Button(text="Buscar", size_hint_x=0.3)
        btn_buscar.bind(on_press=self.buscar)
        categorias_box.add_widget(btn_buscar)
        layout.add_widget(categorias_box)
        
        # Área de resultados
        scroll = ScrollView()
        self.resultados_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.resultados_layout.bind(minimum_height=self.resultados_layout.setter('height'))
        scroll.add_widget(self.resultados_layout)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def buscar(self, instance):
        self.resultados_layout.clear_widgets()
        ejemplos = self.db.obtener_ejemplos(self.spinner.text)
        
        if not ejemplos:
            self.resultados_layout.add_widget(Label(text="No se encontraron ejemplos"))
            return
        
        for id_ej, cat, esp, ing, fr in ejemplos:
            ejemplo_box = BoxLayout(
                orientation='vertical', 
                size_hint_y=None, 
                height=120
            )
            ejemplo_box.add_widget(Label(text=f"ID: {id_ej} | Categoría: {cat}"))
            ejemplo_box.add_widget(Label(text=f"🇪🇸 {esp}"))
            ejemplo_box.add_widget(Label(text=f"🇬🇧 {ing}"))
            ejemplo_box.add_widget(Label(text=f"🇫🇷 {fr}"))
            self.resultados_layout.add_widget(ejemplo_box)
    
    def volver(self, instance):
        self.manager.current = "menu_principal"

class AgregarEjemploScreen(Screen):
    """Pantalla para agregar nuevos ejemplos"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Barra superior
        top_bar = BoxLayout(size_hint_y=0.1)
        btn_volver = Button(text="← Volver", size_hint_x=0.2)
        btn_volver.bind(on_press=self.volver)
        titulo = Label(text="➕ Agregar Nuevo Ejemplo", font_size='20sp')
        top_bar.add_widget(btn_volver)
        top_bar.add_widget(titulo)
        layout.add_widget(top_bar)
        
        # Formulario
        form_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.8)
        
        form_layout.add_widget(Label(text="Categoría:"))
        self.spinner_categoria = Spinner(
            text='temporal',
            values=('temporal', 'consecutivo', 'discursivo')
        )
        form_layout.add_widget(self.spinner_categoria)
        
        form_layout.add_widget(Label(text="Español:"))
        self.input_espanol = TextInput(multiline=True, size_hint_y=2)
        form_layout.add_widget(self.input_espanol)
        
        form_layout.add_widget(Label(text="Inglés:"))
        self.input_ingles = TextInput(multiline=True, size_hint_y=2)
        form_layout.add_widget(self.input_ingles)
        
        form_layout.add_widget(Label(text="Francés:"))
        self.input_frances = TextInput(multiline=True, size_hint_y=2)
        form_layout.add_widget(self.input_frances)
        
        layout.add_widget(form_layout)
        
        # Botones
        btn_guardar = Button(
            text="💾 Guardar Ejemplo",
            size_hint_y=0.1,
            background_color=(0.2, 0.8, 0.2, 1)
        )
        btn_guardar.bind(on_press=self.guardar_ejemplo)
        layout.add_widget(btn_guardar)
        
        self.add_widget(layout)
    
    def guardar_ejemplo(self, instance):
        categoria = self.spinner_categoria.text
        espanol = self.input_espanol.text.strip()
        ingles = self.input_ingles.text.strip()
        frances = self.input_frances.text.strip()
        
        if not all([espanol, ingles, frances]):
            self.mostrar_popup("Error", "Todos los campos son obligatorios")
            return
        
        if self.db.agregar_ejemplo(categoria, espanol, ingles, frances):
            self.mostrar_popup("Éxito", "Ejemplo agregado correctamente")
            self.limpiar_formulario()
        else:
            self.mostrar_popup("Error", "Error al agregar el ejemplo")
    
    def limpiar_formulario(self):
        self.input_espanol.text = ""
        self.input_ingles.text = ""
        self.input_frances.text = ""
    
    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(
            title=titulo,
            content=Label(text=mensaje),
            size_hint=(0.6, 0.4)
        )
        popup.open()
    
    def volver(self, instance):
        self.manager.current = "menu_principal"

class ModoPracticaScreen(Screen):
    """Pantalla para el modo de práctica"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        self.ejemplos = []
        self.indice_actual = 0
        
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Barra superior
        top_bar = BoxLayout(size_hint_y=0.1)
        btn_volver = Button(text="← Volver", size_hint_x=0.2)
        btn_volver.bind(on_press=self.volver)
        self.titulo = Label(text="🎯 Modo Práctica", font_size='20sp')
        top_bar.add_widget(btn_volver)
        top_bar.add_widget(self.titulo)
        self.layout.add_widget(top_bar)
        
        # Área de práctica
        self.contenido_layout = BoxLayout(orientation='vertical', spacing=15)
        
        self.label_espanol = Label(
            text="Presiona 'Comenzar' para iniciar",
            font_size='18sp',
            size_hint_y=0.4,
            text_size=(None, None)
        )
        self.contenido_layout.add_widget(self.label_espanol)
        
        self.label_traducciones = Label(
            text="",
            font_size='16sp',
            size_hint_y=0.4,
            text_size=(None, None)
        )
        self.contenido_layout.add_widget(self.label_traducciones)
        
        self.layout.add_widget(self.contenido_layout)
        
        # Botones
        botones_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        self.btn_inicio = Button(text="▶️ Comenzar", background_color=(0.2, 0.8, 0.2, 1))
        self.btn_inicio.bind(on_press=self.comenzar_practica)
        botones_layout.add_widget(self.btn_inicio)
        
        self.btn_siguiente = Button(text="➡️ Siguiente", disabled=True)
        self.btn_siguiente.bind(on_press=self.siguiente_ejemplo)
        botones_layout.add_widget(self.btn_siguiente)
        
        self.btn_revelar = Button(text="👁️ Revelar", disabled=True)
        self.btn_revelar.bind(on_press=self.revelar_traducciones)
        botones_layout.add_widget(self.btn_revelar)
        
        self.layout.add_widget(botones_layout)
        self.add_widget(self.layout)
    
    def comenzar_practica(self, instance):
        self.ejemplos = self.db.obtener_ejemplos()
        if not self.ejemplos:
            self.label_espanol.text = "No hay ejemplos para practicar"
            return
        
        self.indice_actual = 0
        self.btn_inicio.disabled = True
        self.btn_siguiente.disabled = False
        self.btn_revelar.disabled = False
        self.mostrar_ejemplo_actual()
    
    def mostrar_ejemplo_actual(self):
        if self.indice_actual < len(self.ejemplos):
            id_ej, cat, esp, ing, fr = self.ejemplos[self.indice_actual]
            self.label_espanol.text = f"🇪🇸 {esp}"
            self.label_traducciones.text = "¿Recuerdas las traducciones?"
            self.titulo.text = f"🎯 Práctica ({self.indice_actual + 1}/{len(self.ejemplos)})"
        else:
            self.label_espanol.text = "¡Práctica completada! 🎉"
            self.label_traducciones.text = "Has revisado todos los ejemplos"
            self.btn_siguiente.disabled = True
            self.btn_revelar.disabled = True
    
    def revelar_traducciones(self, instance):
        if self.indice_actual < len(self.ejemplos):
            id_ej, cat, esp, ing, fr = self.ejemplos[self.indice_actual]
            self.label_traducciones.text = f"🇬🇧 {ing}\n🇫🇷 {fr}"
    
    def siguiente_ejemplo(self, instance):
        self.indice_actual += 1
        self.mostrar_ejemplo_actual()
    
    def volver(self, instance):
        self.manager.current = "menu_principal"

class EstadisticasScreen(Screen):
    """Pantalla de estadísticas"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Barra superior
        top_bar = BoxLayout(size_hint_y=0.1)
        btn_volver = Button(text="← Volver", size_hint_x=0.2)
        btn_volver.bind(on_press=self.volver)
        titulo = Label(text="📊 Estadísticas", font_size='20sp')
        top_bar.add_widget(btn_volver)
        top_bar.add_widget(titulo)
        layout.add_widget(top_bar)
        
        # Contenido de estadísticas
        self.contenido = GridLayout(cols=1, spacing=10, size_hint_y=0.9)
        layout.add_widget(self.contenido)
        
        self.add_widget(layout)
        self.actualizar_estadisticas()
    
    def actualizar_estadisticas(self):
        self.contenido.clear_widgets()
        total, stats = self.db.obtener_estadisticas()
        
        self.contenido.add_widget(Label(
            text=f"📈 Total de ejemplos: {total}",
            font_size='20sp',
            size_hint_y=0.2
        ))
        
        for categoria, cantidad in stats:
            porcentaje = (cantidad / total) * 100 if total > 0 else 0
            self.contenido.add_widget(Label(
                text=f"• {categoria.capitalize()}: {cantidad} ejemplos ({porcentaje:.1f}%)",
                font_size='16sp'
            ))
    
    def volver(self, instance):
        self.manager.current = "menu_principal"

class GestorEntoncesApp(App):
    """Aplicación principal"""
    def build(self):
        self.title = "Gestor de Ejemplos - Uso de 'Entonces'"
        
        # Configurar el gestor de pantallas
        sm = ScreenManager()
        
        # Agregar pantallas
        sm.add_widget(MenuPrincipal(name='menu_principal'))
        sm.add_widget(VerEjemplosScreen(name='ver_ejemplos'))
        sm.add_widget(BuscarCategoriaScreen(name='buscar_categoria'))
        sm.add_widget(AgregarEjemploScreen(name='agregar_ejemplo'))
        sm.add_widget(ModoPracticaScreen(name='modo_practica'))
        sm.add_widget(EstadisticasScreen(name='estadisticas'))
        
        return sm

if __name__ == '__main__':
    GestorEntoncesApp().run()
