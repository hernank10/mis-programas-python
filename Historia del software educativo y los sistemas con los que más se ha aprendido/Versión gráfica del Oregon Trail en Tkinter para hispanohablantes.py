import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
import random
from datetime import datetime, timedelta
import json
import os
from PIL import Image, ImageTk
import sys

class OregonTrailGUI:
    """Versión gráfica del Oregon Trail en Tkinter para hispanohablantes"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Oregon Trail - Versión Gráfica")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c3e50')
        
        # Cargar recursos
        self.load_images()
        
        # Estado del juego
        self.game_state = {
            'distancia_recorrida': 0,
            'distancia_total': 2000,
            'fecha_actual': datetime(1848, 3, 1),
            'comida': 500,  # libras
            'municion': 100,  # balas
            'dinero': 500,  # dólares
            'salud': 100,  # porcentaje
            'ritmo': 'moderado',  # moderado, rápido, agotador
            'raciones': 'normal',  # escasas, normales, abundantes
            'clima': 'despejado',
            'terreno': 'llanura',
            'profundidad_rio': 0,
            'proximo_hito': 100,
            'hitos_pasados': 0,
            'dias_sin_comer': 0,
            'dias_enfermedad': 0,
            'miembros_grupo': [
                {'nombre': 'Tú', 'salud': 100, 'enfermo': False, 'herido': False},
                {'nombre': 'María', 'salud': 100, 'enfermo': False, 'herido': False},
                {'nombre': 'José', 'salud': 100, 'enfermo': False, 'herido': False},
                {'nombre': 'Ana', 'salud': 100, 'enfermo': False, 'herido': False},
                {'nombre': 'Pedro', 'salud': 100, 'enfermo': False, 'herido': False}
            ],
            'bueyes': 4,
            'condicion_carro': 100,
            'vivo': True,
            'juego_terminado': False,
            'razon': '',
            'puntuacion': 0,
            'dificultad': 'medio',
            'dias_viajados': 0
        }
        
        # Configuración del juego
        self.dificultades = {
            'facil': {'consumo_comida': 0.8, 'probabilidad_enfermedad': 0.05, 'probabilidad_evento': 0.1},
            'medio': {'consumo_comida': 1.0, 'probabilidad_enfermedad': 0.1, 'probabilidad_evento': 0.15},
            'dificil': {'consumo_comida': 1.2, 'probabilidad_enfermedad': 0.15, 'probabilidad_evento': 0.2},
            'experto': {'consumo_comida': 1.5, 'probabilidad_enfermedad': 0.2, 'probabilidad_evento': 0.25}
        }
        
        # Lista de hitos
        self.hitos = [
            {'nombre': 'Cruce del Río Kansas', 'distancia': 100, 'tipo': 'río'},
            {'nombre': 'Fuerte Kearny', 'distancia': 300, 'tipo': 'fuerte'},
            {'nombre': 'Chimney Rock', 'distancia': 550, 'tipo': 'referencia'},
            {'nombre': 'Fuerte Laramie', 'distancia': 650, 'tipo': 'fuerte'},
            {'nombre': 'Independence Rock', 'distancia': 800, 'tipo': 'referencia'},
            {'nombre': 'South Pass', 'distancia': 950, 'tipo': 'montaña'},
            {'nombre': 'Fuerte Bridger', 'distancia': 1050, 'tipo': 'fuerte'},
            {'nombre': 'Cruce del Río Green', 'distancia': 1150, 'tipo': 'río'},
            {'nombre': 'Soda Springs', 'distancia': 1250, 'tipo': 'referencia'},
            {'nombre': 'Fuerte Hall', 'distancia': 1350, 'tipo': 'fuerte'},
            {'nombre': 'Cruce del Río Snake', 'distancia': 1450, 'tipo': 'río'},
            {'nombre': 'Fuerte Boise', 'distancia': 1650, 'tipo': 'fuerte'},
            {'nombre': 'Montañas Azules', 'distancia': 1750, 'tipo': 'montaña'},
            {'nombre': 'Fuerte Walla Walla', 'distancia': 1850, 'tipo': 'fuerte'},
            {'nombre': 'The Dalles', 'distancia': 1950, 'tipo': 'referencia'},
            {'nombre': 'Oregon City', 'distancia': 2000, 'tipo': 'destino'}
        ]
        
        # Eventos
        self.eventos = [
            {'tipo': 'bueno', 'nombre': 'Encontraste bayas', 'efecto': 'comida', 'cantidad': 50},
            {'tipo': 'bueno', 'nombre': 'Cacería exitosa', 'efecto': 'comida', 'cantidad': 100},
            {'tipo': 'bueno', 'nombre': 'Comerciaste con nativos', 'efecto': 'comida', 'cantidad': 80},
            {'tipo': 'bueno', 'nombre': 'Encontraste carro abandonado', 'efecto': 'dinero', 'cantidad': 100},
            
            {'tipo': 'malo', 'nombre': 'Mordedura de serpiente', 'efecto': 'salud', 'cantidad': -20},
            {'tipo': 'malo', 'nombre': 'Rueda del carro rota', 'efecto': 'carro', 'cantidad': -30},
            {'tipo': 'malo', 'nombre': 'Buey se escapó', 'efecto': 'bueyes', 'cantidad': -1},
            {'tipo': 'malo', 'nombre': 'Comida echada a perder', 'efecto': 'comida', 'cantidad': -100},
            {'tipo': 'malo', 'nombre': 'Ladrones por la noche', 'efecto': 'dinero', 'cantidad': -100},
            
            {'tipo': 'enfermedad', 'nombre': 'Cólera', 'efecto': 'enfermedad', 'severidad': 'alta'},
            {'tipo': 'enfermedad', 'nombre': 'Disentería', 'efecto': 'enfermedad', 'severidad': 'media'},
            {'tipo': 'enfermedad', 'nombre': 'Tifus', 'efecto': 'enfermedad', 'severidad': 'alta'},
            {'tipo': 'enfermedad', 'nombre': 'Sarampión', 'efecto': 'enfermedad', 'severidad': 'baja'},
        ]
        
        # Precios
        self.precios = {
            'comida': 0.20,
            'municion': 2.00,
            'bueyes': 40.00,
            'rueda_carro': 10.00,
            'medicinas': 25.00
        }
        
        # Inicializar interfaz
        self.setup_ui()
        self.show_main_menu()
    
    def load_images(self):
        """Carga las imágenes del juego"""
        try:
            # Crear imágenes simples si no existen archivos
            self.images = {}
            colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
            
            for i, color in enumerate(colors):
                img = Image.new('RGB', (50, 50), color)
                self.images[f'icono{i}'] = ImageTk.PhotoImage(img)
        except:
            self.images = {}
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colores personalizados
        self.style.configure('Title.TLabel', font=('Arial', 24, 'bold'), 
                           foreground='#ecf0f1', background='#2c3e50')
        self.style.configure('Subtitle.TLabel', font=('Arial', 16), 
                           foreground='#bdc3c7', background='#2c3e50')
        self.style.configure('Status.TLabel', font=('Arial', 12), 
                           foreground='#ecf0f1', background='#34495e')
        self.style.configure('Button.TButton', font=('Arial', 12), padding=10)
        
        # Frames para diferentes pantallas
        self.menu_frame = ttk.Frame(self.main_frame)
        self.game_frame = ttk.Frame(self.main_frame)
        self.shop_frame = ttk.Frame(self.main_frame)
        
        # Configurar juego
        self.setup_menu_screen()
        self.setup_game_screen()
        self.setup_shop_screen()
    
    def setup_menu_screen(self):
        """Configura la pantalla del menú principal"""
        # Frame para el título
        title_frame = ttk.Frame(self.menu_frame, style='Title.TFrame')
        title_frame.pack(fill=tk.X, pady=20)
        
        ttk.Label(title_frame, text="OREGON TRAIL", 
                 style='Title.TLabel').pack(pady=10)
        ttk.Label(title_frame, text="Viaje a través del Salvaje Oeste", 
                 style='Subtitle.TLabel').pack()
        
        # Frame para botones
        button_frame = ttk.Frame(self.menu_frame)
        button_frame.pack(pady=50)
        
        # Botones del menú
        ttk.Button(button_frame, text="Nuevo Juego", 
                  command=self.start_new_game, 
                  style='Button.TButton', width=20).pack(pady=10)
        
        ttk.Button(button_frame, text="Elegir Dificultad", 
                  command=self.show_difficulty_menu,
                  style='Button.TButton', width=20).pack(pady=10)
        
        ttk.Button(button_frame, text="Instrucciones", 
                  command=self.show_instructions,
                  style='Button.TButton', width=20).pack(pady=10)
        
        ttk.Button(button_frame, text="Salir", 
                  command=self.root.quit,
                  style='Button.TButton', width=20).pack(pady=10)
        
        # Información de dificultad
        self.difficulty_label = ttk.Label(self.menu_frame, 
                                         text=f"Dificultad: {self.game_state['dificultad'].upper()}",
                                         font=('Arial', 12, 'bold'),
                                         foreground='#f39c12')
        self.difficulty_label.pack(pady=20)
    
    def setup_game_screen(self):
        """Configura la pantalla principal del juego"""
        # Frame superior: Información del viaje
        top_frame = ttk.Frame(self.game_frame)
        top_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Información del viaje
        travel_info = ttk.LabelFrame(top_frame, text="INFORMACIÓN DEL VIAJE", padding=10)
        travel_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.distance_label = ttk.Label(travel_info, 
                                       text="Distancia: 0 / 2000 millas",
                                       font=('Arial', 12))
        self.distance_label.pack(anchor=tk.W)
        
        self.date_label = ttk.Label(travel_info, 
                                   text="Fecha: Marzo 1, 1848",
                                   font=('Arial', 12))
        self.date_label.pack(anchor=tk.W)
        
        self.next_label = ttk.Label(travel_info, 
                                   text="Próximo hito: Cruce del Río Kansas (100 millas)",
                                   font=('Arial', 12))
        self.next_label.pack(anchor=tk.W)
        
        # Barra de progreso
        progress_frame = ttk.Frame(travel_info)
        progress_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(progress_frame, text="Progreso:").pack(side=tk.LEFT)
        self.progress_bar = ttk.Progressbar(progress_frame, 
                                           length=300, 
                                           mode='determinate')
        self.progress_bar.pack(side=tk.LEFT, padx=5)
        self.progress_label = ttk.Label(progress_frame, text="0%")
        self.progress_label.pack(side=tk.LEFT)
        
        # Estado del clima/terreno
        weather_frame = ttk.LabelFrame(top_frame, text="CONDICIONES", padding=10)
        weather_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.weather_label = ttk.Label(weather_frame, 
                                      text="Clima: Despejado",
                                      font=('Arial', 12))
        self.weather_label.pack(anchor=tk.W)
        
        self.terrain_label = ttk.Label(weather_frame, 
                                      text="Terreno: Llanura",
                                      font=('Arial', 12))
        self.terrain_label.pack(anchor=tk.W)
        
        # Frame medio: Recursos y grupo
        middle_frame = ttk.Frame(self.game_frame)
        middle_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Recursos
        resources_frame = ttk.LabelFrame(middle_frame, text="RECURSOS", padding=10)
        resources_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.food_label = ttk.Label(resources_frame, 
                                   text="Comida: 500 lbs",
                                   font=('Arial', 12))
        self.food_label.pack(anchor=tk.W, pady=2)
        
        self.ammo_label = ttk.Label(resources_frame, 
                                   text="Munición: 100 balas",
                                   font=('Arial', 12))
        self.ammo_label.pack(anchor=tk.W, pady=2)
        
        self.money_label = ttk.Label(resources_frame, 
                                    text="Dinero: $500",
                                    font=('Arial', 12))
        self.money_label.pack(anchor=tk.W, pady=2)
        
        self.oxen_label = ttk.Label(resources_frame, 
                                   text="Bueyes: 4",
                                   font=('Arial', 12))
        self.oxen_label.pack(anchor=tk.W, pady=2)
        
        self.wagon_label = ttk.Label(resources_frame, 
                                    text="Carro: 100%",
                                    font=('Arial', 12))
        self.wagon_label.pack(anchor=tk.W, pady=2)
        
        # Grupo
        group_frame = ttk.LabelFrame(middle_frame, text="GRUPO", padding=10)
        group_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.group_labels = []
        for i in range(5):
            label = ttk.Label(group_frame, 
                            text=f"Miembro {i+1}: 100%",
                            font=('Arial', 12))
            label.pack(anchor=tk.W, pady=2)
            self.group_labels.append(label)
        
        # Frame inferior: Controles y eventos
        bottom_frame = ttk.Frame(self.game_frame)
        bottom_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Controles
        controls_frame = ttk.LabelFrame(bottom_frame, text="ACCIONES", padding=10)
        controls_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Botones de acciones
        action_buttons = [
            ("Continuar Viaje", self.continue_travel),
            ("Cambiar Ritmo", self.change_pace),
            ("Cambiar Raciones", self.change_rations),
            ("Descansar", self.rest),
            ("Cazar", self.hunt),
            ("Comprar Suministros", self.open_shop),
            ("Guardar Juego", self.save_game),
            ("Volver al Menú", self.return_to_menu)
        ]
        
        for text, command in action_buttons:
            ttk.Button(controls_frame, text=text, 
                      command=command, 
                      style='Button.TButton').pack(fill=tk.X, pady=5)
        
        # Eventos
        events_frame = ttk.LabelFrame(bottom_frame, text="EVENTOS", padding=10)
        events_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Área de texto para eventos
        self.events_text = scrolledtext.ScrolledText(events_frame, 
                                                    height=15,
                                                    width=50,
                                                    font=('Courier', 10))
        self.events_text.pack(fill=tk.BOTH, expand=True)
        self.events_text.config(state=tk.DISABLED)
    
    def setup_shop_screen(self):
        """Configura la pantalla de tienda"""
        # Título
        ttk.Label(self.shop_frame, text="TIENDA DEL FUERTE", 
                 style='Title.TLabel').pack(pady=20)
        
        # Frame para productos
        products_frame = ttk.Frame(self.shop_frame)
        products_frame.pack(pady=10)
        
        # Productos disponibles
        self.products = [
            {'nombre': 'Comida', 'precio': 0.20, 'unidad': 'lb', 'cantidad': 0},
            {'nombre': 'Munición', 'precio': 2.00, 'unidad': '20 balas', 'cantidad': 0},
            {'nombre': 'Bueyes', 'precio': 40.00, 'unidad': 'cada uno', 'cantidad': 0},
            {'nombre': 'Ruedas', 'precio': 10.00, 'unidad': 'cada una', 'cantidad': 0},
            {'nombre': 'Medicinas', 'precio': 25.00, 'unidad': 'kit', 'cantidad': 0}
        ]
        
        self.product_vars = []
        self.product_spins = []
        
        for i, product in enumerate(self.products):
            frame = ttk.Frame(products_frame)
            frame.pack(fill=tk.X, pady=5)
            
            ttk.Label(frame, text=f"{product['nombre']}:", 
                     width=15).pack(side=tk.LEFT)
            ttk.Label(frame, text=f"${product['precio']:.2f} por {product['unidad']}", 
                     width=20).pack(side=tk.LEFT)
            
            spin = tk.Spinbox(frame, from_=0, to=100, width=10)
            spin.pack(side=tk.LEFT, padx=10)
            self.product_spins.append(spin)
            
            ttk.Label(frame, text=product['unidad']).pack(side=tk.LEFT)
        
        # Dinero disponible
        money_frame = ttk.Frame(self.shop_frame)
        money_frame.pack(pady=10)
        
        self.shop_money_label = ttk.Label(money_frame, 
                                         text="Dinero disponible: $500",
                                         font=('Arial', 12, 'bold'))
        self.shop_money_label.pack()
        
        # Total
        total_frame = ttk.Frame(self.shop_frame)
        total_frame.pack(pady=10)
        
        ttk.Label(total_frame, text="Total:", 
                 font=('Arial', 12, 'bold')).pack(side=tk.LEFT)
        self.total_label = ttk.Label(total_frame, text="$0.00",
                                    font=('Arial', 12, 'bold'))
        self.total_label.pack(side=tk.LEFT, padx=10)
        
        # Botones
        button_frame = ttk.Frame(self.shop_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Calcular Total", 
                  command=self.calculate_total).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Comprar", 
                  command=self.make_purchase).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Cancelar", 
                  command=self.close_shop).pack(side=tk.LEFT, padx=5)
    
    def show_main_menu(self):
        """Muestra el menú principal"""
        self.hide_all_frames()
        self.menu_frame.pack(fill=tk.BOTH, expand=True)
        self.update_difficulty_label()
    
    def show_game_screen(self):
        """Muestra la pantalla del juego"""
        self.hide_all_frames()
        self.game_frame.pack(fill=tk.BOTH, expand=True)
        self.update_game_display()
    
    def show_shop_screen(self):
        """Muestra la pantalla de la tienda"""
        self.hide_all_frames()
        self.shop_frame.pack(fill=tk.BOTH, expand=True)
        self.update_shop_display()
    
    def hide_all_frames(self):
        """Oculta todos los frames"""
        for frame in [self.menu_frame, self.game_frame, self.shop_frame]:
            frame.pack_forget()
    
    def update_difficulty_label(self):
        """Actualiza la etiqueta de dificultad"""
        self.difficulty_label.config(
            text=f"Dificultad: {self.game_state['dificultad'].upper()}"
        )
    
    def update_game_display(self):
        """Actualiza toda la información en pantalla"""
        # Información del viaje
        self.distance_label.config(
            text=f"Distancia: {self.game_state['distancia_recorrida']} / 2000 millas"
        )
        
        fecha = self.game_state['fecha_actual'].strftime("%B %d, %Y")
        self.date_label.config(text=f"Fecha: {fecha}")
        
        proximo_hito = self.get_next_landmark()
        if proximo_hito:
            self.next_label.config(
                text=f"Próximo hito: {proximo_hito['nombre']} "
                     f"({self.game_state['proximo_hito']} millas)"
            )
        
        # Barra de progreso
        progreso = (self.game_state['distancia_recorrida'] / 2000) * 100
        self.progress_bar['value'] = progreso
        self.progress_label.config(text=f"{progreso:.1f}%")
        
        # Condiciones
        self.weather_label.config(
            text=f"Clima: {self.game_state['clima'].capitalize()}"
        )
        self.terrain_label.config(
            text=f"Terreno: {self.game_state['terreno'].capitalize()}"
        )
        
        # Recursos
        self.food_label.config(
            text=f"Comida: {self.game_state['comida']} lbs"
        )
        self.ammo_label.config(
            text=f"Municón: {self.game_state['municion']} balas"
        )
        self.money_label.config(
            text=f"Dinero: ${self.game_state['dinero']}"
        )
        self.oxen_label.config(
            text=f"Bueyes: {self.game_state['bueyes']}"
        )
        self.wagon_label.config(
            text=f"Carro: {self.game_state['condicion_carro']}%"
        )
        
        # Grupo
        for i, miembro in enumerate(self.game_state['miembros_grupo']):
            estado = "Sano"
            if miembro['enfermo']:
                estado = "Enfermo"
            elif miembro['herido']:
                estado = "Herido"
            
            color = "#2ecc71"  # Verde para sano
            if miembro['salud'] < 50:
                color = "#f39c12"  # Naranja para medio
            if miembro['salud'] < 25:
                color = "#e74c3c"  # Rojo para peligro
            
            self.group_labels[i].config(
                text=f"{miembro['nombre']}: {miembro['salud']}% - {estado}",
                foreground=color
            )
        
        # Actualizar eventos
        self.update_events_display()
    
    def update_shop_display(self):
        """Actualiza la pantalla de la tienda"""
        self.shop_money_label.config(
            text=f"Dinero disponible: ${self.game_state['dinero']}"
        )
        self.calculate_total()
    
    def update_events_display(self):
        """Actualiza el área de eventos"""
        self.events_text.config(state=tk.NORMAL)
        self.events_text.delete(1.0, tk.END)
        
        # Mostrar últimos eventos
        if hasattr(self, 'event_history'):
            for event in self.event_history[-10:]:  # Últimos 10 eventos
                self.events_text.insert(tk.END, f"{event}\n")
        
        self.events_text.config(state=tk.DISABLED)
        self.events_text.see(tk.END)
    
    def log_event(self, mensaje):
        """Registra un evento en el historial"""
        if not hasattr(self, 'event_history'):
            self.event_history = []
        
        fecha = self.game_state['fecha_actual'].strftime("%m/%d")
        self.event_history.append(f"[{fecha}] {mensaje}")
        self.update_events_display()
    
    def start_new_game(self):
        """Inicia un nuevo juego"""
        # Preguntar por nombres del grupo
        respuesta = messagebox.askyesno(
            "Personalizar Grupo",
            "¿Deseas personalizar los nombres de tu grupo?"
        )
        
        if respuesta:
            self.customize_group_names()
        
        # Mostrar mensaje de inicio
        messagebox.showinfo(
            "¡Comienza la Aventura!",
            "¡Bienvenido al Oregon Trail!\n\n"
            "Tu viaje comienza en Independence, Missouri.\n"
            "Debes llegar a Oregon City (2000 millas) antes del invierno.\n\n"
            "Buena suerte, pionero!"
        )
        
        # Inicializar historial de eventos
        self.event_history = [
            "[03/01] Comienzas tu viaje desde Independence, Missouri",
            f"[03/01] Dificultad: {self.game_state['dificultad'].upper()}"
        ]
        
        self.show_game_screen()
    
    def customize_group_names(self):
        """Permite personalizar los nombres del grupo"""
        for i, miembro in enumerate(self.game_state['miembros_grupo']):
            if miembro['nombre'] != 'Tú':  # No cambiar el nombre del jugador
                nuevo_nombre = simpledialog.askstring(
                    "Nombre del Miembro",
                    f"Nombre para el miembro {i+1} (actual: {miembro['nombre']}):"
                )
                if nuevo_nombre:
                    miembro['nombre'] = nuevo_nombre
    
    def show_difficulty_menu(self):
        """Muestra el menú de dificultad"""
        dificultades = [
            ("Fácil", "facil"),
            ("Medio", "medio"),
            ("Difícil", "dificil"),
            ("Experto", "experto")
        ]
        
        # Crear ventana emergente
        popup = tk.Toplevel(self.root)
        popup.title("Elegir Dificultad")
        popup.geometry("400x300")
        popup.configure(bg='#34495e')
        popup.transient(self.root)
        popup.grab_set()
        
        ttk.Label(popup, text="ELIGE LA DIFICULTAD", 
                 style='Title.TLabel').pack(pady=20)
        
        for nombre, valor in dificultades:
            frame = ttk.Frame(popup)
            frame.pack(pady=5)
            
            ttk.Button(frame, text=nombre, 
                      command=lambda v=valor: self.set_difficulty(v, popup),
                      style='Button.TButton', width=20).pack()
        
        # Información de dificultad
        info_frame = ttk.Frame(popup)
        info_frame.pack(pady=20)
        
        info_text = """
Fácil: Más comida, menos enfermedades
Medio: Desafío equilibrado
Difícil: Menos recursos, más peligros
Experto: Solo para los más valientes
        """
        
        ttk.Label(info_frame, text=info_text,
                 font=('Arial', 10),
                 foreground='#bdc3c7',
                 justify=tk.LEFT).pack()
    
    def set_difficulty(self, dificultad, popup):
        """Establece la dificultad del juego"""
        self.game_state['dificultad'] = dificultad
        self.update_difficulty_label()
        popup.destroy()
        
        messagebox.showinfo(
            "Dificultad Establecida",
            f"Dificultad cambiada a: {dificultad.upper()}"
        )
    
    def show_instructions(self):
        """Muestra las instrucciones del juego"""
        instrucciones = """
OBJETIVO:
Viajar desde Independence, Missouri hasta Oregon City (2000 millas)
manteniendo a tu grupo con vida y saludable.

CONTROLES:
- Usa los botones para realizar acciones diarias
- Gestiona tus recursos cuidadosamente
- Toma decisiones en eventos especiales

RECURSOS:
• Comida: Consumida diariamente
• Munición: Para cazar y defensa
• Dinero: Para comprar suministros
• Bueyes: Tiran de tu carro

CONSEJOS:
1. Mantén suficiente comida
2. Descansa en los fuertes
3. No viajes demasiado rápido
4. Caza cuando sea necesario
5. Repara el carro a tiempo

¡Buena suerte en tu viaje!
        """
        
        messagebox.showinfo("Instrucciones del Juego", instrucciones)
    
    def continue_travel(self):
        """Continúa el viaje por un día"""
        if self.game_state['juego_terminado']:
            self.show_game_over()
            return
        
        # Calcular distancia del día
        distancia = self.calcular_distancia_diaria()
        self.game_state['distancia_recorrida'] += distancia
        self.game_state['dias_viajados'] += 1
        
        # Consumir comida
        if not self.consumir_comida():
            self.log_event("⚠️ ¡No hay comida! El grupo pasa hambre.")
        
        # Actualizar clima y terreno
        self.actualizar_clima()
        
        # Verificar hito
        hito = self.verificar_hito()
        if hito:
            self.log_event(f"🎯 ¡Alcanzaste {hito['nombre']}!")
            if hito['tipo'] == 'fuerte':
                self.log_event("🏰 Puedes descansar y comprar suministros aquí.")
        
        # Evento aleatorio
        if random.random() < self.dificultades[self.game_state['dificultad']]['probabilidad_evento']:
            self.generar_evento_aleatorio()
        
        # Actualizar salud
        self.actualizar_salud()
        
        # Avanzar fecha
        self.game_state['fecha_actual'] += timedelta(days=1)
        
        # Verificar fin de juego
        if self.verificar_fin_juego():
            self.show_game_over()
            return
        
        # Actualizar pantalla
        self.update_game_display()
        
        # Mostrar resumen del día
        self.mostrar_resumen_dia(distancia)
    
    def calcular_distancia_diaria(self):
        """Calcula la distancia recorrida en un día"""
        factores_ritmo = {
            'moderado': random.randint(15, 20),
            'rapido': random.randint(20, 25),
            'agotador': random.randint(25, 30)
        }
        
        factores_terreno = {
            'llanura': 1.0,
            'colinas': 0.8,
            'montaña': 0.5,
            'desierto': 0.7,
            'bosque': 0.9
        }
        
        factores_clima = {
            'despejado': 1.0,
            'lluvioso': 0.8,
            'tormenta': 0.5,
            'calor': 0.9,
            'frio': 0.8,
            'viento': 0.7
        }
        
        factor_carro = self.game_state['condicion_carro'] / 100.0
        factor_bueyes = min(self.game_state['bueyes'] / 4.0, 1.0)
        
        distancia_base = factores_ritmo[self.game_state['ritmo']]
        modificador_terreno = factores_terreno[self.game_state['terreno']]
        modificador_clima = factores_clima[self.game_state['clima']]
        
        distancia = distancia_base * modificador_terreno * modificador_clima * factor_carro * factor_bueyes
        
        return max(5, int(distancia))
    
    def consumir_comida(self):
        """Consume comida según las raciones"""
        consumo_raciones = {
            'escasas': 1,
            'normales': 2,
            'abundantes': 3
        }
        
        consumo_por_persona = consumo_raciones[self.game_state['raciones']]
        consumo_total = consumo_por_persona * len(self.game_state['miembros_grupo'])
        
        factor_dificultad = self.dificultades[self.game_state['dificultad']]['consumo_comida']
        consumo_total = int(consumo_total * factor_dificultad)
        
        if self.game_state['comida'] >= consumo_total:
            self.game_state['comida'] -= consumo_total
            self.game_state['dias_sin_comer'] = 0
            return True
        else:
            self.game_state['comida'] = 0
            self.game_state['dias_sin_comer'] += 1
            return False
    
    def actualizar_clima(self):
        """Actualiza las condiciones climáticas"""
        if random.random() < 0.3:
            climas = ['despejado', 'lluvioso', 'tormenta', 'calor', 'frio', 'viento']
            self.game_state['clima'] = random.choice(climas)
        
        distancia = self.game_state['distancia_recorrida']
        if distancia < 300:
            terrenos = ['llanura', 'colinas']
        elif distancia < 800:
            terrenos = ['llanura', 'colinas', 'bosque']
        elif distancia < 1200:
            terrenos = ['colinas', 'montaña', 'bosque']
        elif distancia < 1600:
            terrenos = ['montaña', 'desierto', 'colinas']
        else:
            terrenos = ['bosque', 'colinas', 'llanura']
        
        if random.random() < 0.2:
            self.game_state['terreno'] = random.choice(terrenos)
    
    def verificar_hito(self):
        """Verifica si se ha alcanzado un hito"""
        distancia_actual = self.game_state['distancia_recorrida']
        for hito in self.hitos:
            if abs(distancia_actual - hito['distancia']) < 10 and hito['distancia'] > self.game_state['hitos_pasados']:
                self.game_state['hitos_pasados'] = hito['distancia']
                proximo = self.get_next_landmark()
                if proximo:
                    self.game_state['proximo_hito'] = proximo['distancia']
                return hito
        return None
    
    def get_next_landmark(self):
        """Obtiene el próximo hito"""
        for hito in self.hitos:
            if hito['distancia'] > self.game_state['distancia_recorrida']:
                return hito
        return None
    
    def generar_evento_aleatorio(self):
        """Genera un evento aleatorio"""
        evento = random.choice(self.eventos)
        self.manejar_evento(evento)
    
    def manejar_evento(self, evento):
        """Maneja un evento específico"""
        mensaje = f"📢 {evento['nombre']}"
        self.log_event(mensaje)
        
        if evento['tipo'] == 'bueno':
            if evento['efecto'] == 'comida':
                self.game_state['comida'] += evento['cantidad']
                self.log_event(f"  +{evento['cantidad']} lbs de comida")
            elif evento['efecto'] == 'dinero':
                self.game_state['dinero'] += evento['cantidad']
                self.log_event(f"  +${evento['cantidad']}")
        
        elif evento['tipo'] == 'malo':
            if evento['efecto'] == 'salud':
                victima = random.choice(self.game_state['miembros_grupo'])
                victima['salud'] = max(0, victima['salud'] + evento['cantidad'])
                self.log_event(f"  {victima['nombre']} pierde {-evento['cantidad']}% de salud")
            
            elif evento['efecto'] == 'carro':
                self.game_state['condicion_carro'] = max(0, self.game_state['condicion_carro'] + evento['cantidad'])
                self.log_event(f"  Carro dañado: {self.game_state['condicion_carro']}%")
            
            elif evento['efecto'] == 'bueyes':
                if self.game_state['bueyes'] > 1:
                    self.game_state['bueyes'] += evento['cantidad']
                    self.log_event(f"  Bueyes restantes: {self.game_state['bueyes']}")
            
            elif evento['efecto'] == 'comida':
                self.game_state['comida'] = max(0, self.game_state['comida'] + evento['cantidad'])
                self.log_event(f"  Comida restante: {self.game_state['comida']} lbs")
            
            elif evento['efecto'] == 'dinero':
                perdida = random.randint(50, 150)
                self.game_state['dinero'] = max(0, self.game_state['dinero'] - perdida)
                self.log_event(f"  Perdiste ${perdida}")
        
        elif evento['tipo'] == 'enfermedad':
            probabilidad = self.dificultades[self.game_state['dificultad']]['probabilidad_enfermedad']
            if random.random() < probabilidad:
                victima = random.choice(self.game_state['miembros_grupo'])
                victima['enfermo'] = True
                self.log_event(f"  {victima['nombre']} se enferma de {evento['nombre']}")
    
    def actualizar_salud(self):
        """Actualiza la salud del grupo"""
        # Efecto del ritmo
        efecto_ritmo = {
            'moderado': 0,
            'rapido': -1,
            'agotador': -3
        }
        
        # Efecto de las raciones
        efecto_raciones = {
            'escasas': -2,
            'normales': 0,
            'abundantes': 1
        }
        
        # Efecto del clima
        efecto_clima = {
            'despejado': 0,
            'lluvioso': -1,
            'tormenta': -3,
            'calor': -1,
            'frio': -2,
            'viento': -1
        }
        
        # Efecto de días sin comida
        if self.game_state['dias_sin_comer'] > 0:
            perdida_salud = self.game_state['dias_sin_comer'] * 5
            for miembro in self.game_state['miembros_grupo']:
                miembro['salud'] = max(0, miembro['salud'] - perdida_salud)
        
        # Aplicar efectos
        for miembro in self.game_state['miembros_grupo']:
            if miembro['salud'] > 0:
                cambio_salud = (efecto_ritmo[self.game_state['ritmo']] +
                              efecto_raciones[self.game_state['raciones']] +
                              efecto_clima[self.game_state['clima']])
                
                if miembro['enfermo']:
                    cambio_salud -= random.randint(5, 15)
                
                if miembro['herido']:
                    cambio_salud -= random.randint(3, 10)
                
                miembro['salud'] = max(0, min(100, miembro['salud'] + cambio_salud))
        
        # Recuperación aleatoria de enfermedades
        for miembro in self.game_state['miembros_grupo']:
            if miembro['enfermo'] and random.random() < 0.3:
                miembro['enfermo'] = False
                self.log_event(f"  {miembro['nombre']} se recupera de la enfermedad")
        
        # Calcular salud promedio
        salud_total = sum(m['salud'] for m in self.game_state['miembros_grupo'])
        miembros_vivos = len([m for m in self.game_state['miembros_grupo'] if m['salud'] > 0])
        
        if miembros_vivos > 0:
            self.game_state['salud'] = salud_total // miembros_vivos
        else:
            self.game_state['salud'] = 0
    
    def verificar_fin_juego(self):
        """Verifica condiciones de fin de juego"""
        # Todos muertos
        miembros_vivos = [m for m in self.game_state['miembros_grupo'] if m['salud'] > 0]
        if len(miembros_vivos) == 0:
            self.game_state['juego_terminado'] = True
            self.game_state['razon'] = "Todos los miembros del grupo han muerto."
            return True
        
        # Hambre
        if self.game_state['dias_sin_comer'] >= 7:
            self.game_state['juego_terminado'] = True
            self.game_state['razon'] = "El grupo murió de hambre."
            return True
        
        # Carro destruido
        if self.game_state['condicion_carro'] <= 0:
            self.game_state['juego_terminado'] = True
            self.game_state['razon'] = "El carro está destruido."
            return True
        
        # Sin bueyes
        if self.game_state['bueyes'] <= 0:
            self.game_state['juego_terminado'] = True
            self.game_state['razon'] = "No hay bueyes para tirar del carro."
            return True
        
        # Llegó a Oregon
        if self.game_state['distancia_recorrida'] >= self.game_state['distancia_total']:
            self.game_state['juego_terminado'] = True
            self.game_state['razon'] = "¡Llegaste a Oregon!"
            return True
        
        # Invierno (después de noviembre)
        if self.game_state['fecha_actual'].month >= 11:
            self.game_state['juego_terminado'] = True
            self.game_state['razon'] = "El invierno llegó. Estás atrapado en las montañas."
            return True
        
        return False
    
    def mostrar_resumen_dia(self, distancia):
        """Muestra un resumen del día"""
        mensaje = f"📅 Día {self.game_state['dias_viajados']} completado\n"
        mensaje += f"📏 Distancia recorrida: {distancia} millas\n"
        mensaje += f"🍖 Comida restante: {self.game_state['comida']} lbs\n"
        mensaje += f"❤️ Salud del grupo: {self.game_state['salud']}%"
        
        messagebox.showinfo("Resumen del Día", mensaje)
    
    def change_pace(self):
        """Cambia el ritmo de viaje"""
        popup = tk.Toplevel(self.root)
        popup.title("Cambiar Ritmo")
        popup.geometry("400x250")
        popup.configure(bg='#34495e')
        popup.transient(self.root)
        popup.grab_set()
        
        ttk.Label(popup, text="RITMO DE VIAJE", 
                 style='Title.TLabel').pack(pady=20)
        
        ritmos = [
            ("Moderado", "moderado", "Velocidad normal, buena salud"),
            ("Rápido", "rapido", "Más velocidad, menos salud"),
            ("Agotador", "agotador", "Máxima velocidad, mucha fatiga")
        ]
        
        for nombre, valor, descripcion in ritmos:
            frame = ttk.Frame(popup)
            frame.pack(fill=tk.X, padx=20, pady=5)
            
            ttk.Radiobutton(frame, text=nombre, 
                          value=valor,
                          variable=tk.StringVar(value=self.game_state['ritmo']),
                          command=lambda v=valor: self.set_pace(v, popup)).pack(anchor=tk.W)
            
            ttk.Label(frame, text=descripcion,
                     font=('Arial', 9),
                     foreground='#bdc3c7').pack(anchor=tk.W)
    
    def set_pace(self, ritmo, popup):
        """Establece el ritmo de viaje"""
        self.game_state['ritmo'] = ritmo
        self.log_event(f"⚡ Ritmo cambiado a: {ritmo}")
        popup.destroy()
        self.update_game_display()
    
    def change_rations(self):
        """Cambia las raciones de comida"""
        popup = tk.Toplevel(self.root)
        popup.title("Cambiar Raciones")
        popup.geometry("400x250")
        popup.configure(bg='#34495e')
        popup.transient(self.root)
        popup.grab_set()
        
        ttk.Label(popup, text="RACIONES DE COMIDA", 
                 style='Title.TLabel').pack(pady=20)
        
        raciones = [
            ("Escasas", "escasas", "Ahorra comida, mala salud"),
            ("Normales", "normales", "Equilibrio comida/salud"),
            ("Abundantes", "abundantes", "Buena salud, gasta comida")
        ]
        
        for nombre, valor, descripcion in raciones:
            frame = ttk.Frame(popup)
            frame.pack(fill=tk.X, padx=20, pady=5)
            
            ttk.Radiobutton(frame, text=nombre, 
                          value=valor,
                          variable=tk.StringVar(value=self.game_state['raciones']),
                          command=lambda v=valor: self.set_rations(v, popup)).pack(anchor=tk.W)
            
            ttk.Label(frame, text=descripcion,
                     font=('Arial', 9),
                     foreground='#bdc3c7').pack(anchor=tk.W)
    
    def set_rations(self, raciones, popup):
        """Establece las raciones de comida"""
        self.game_state['raciones'] = raciones
        self.log_event(f"🍽️ Raciones cambiadas a: {raciones}")
        popup.destroy()
        self.update_game_display()
    
    def rest(self):
        """Descansa por un día"""
        respuesta = messagebox.askyesno(
            "Descansar",
            "¿Descansar por un día?\n\n"
            "La salud del grupo mejorará,\n"
            "pero consumirás comida."
        )
        
        if respuesta:
            self.game_state['fecha_actual'] += timedelta(days=1)
            self.consumir_comida()
            
            # Mejorar salud
            for miembro in self.game_state['miembros_grupo']:
                if miembro['salud'] < 100:
                    mejora = random.randint(5, 15)
                    miembro['salud'] = min(100, miembro['salud'] + mejora)
            
            self.log_event("😴 El grupo descansa y recupera salud")
            self.update_game_display()
    
    def hunt(self):
        """Caza para obtener comida"""
        if self.game_state['municion'] < 10:
            messagebox.showwarning(
                "Sin Munición",
                "Necesitas al menos 10 balas para cazar."
            )
            return
        
        respuesta = messagebox.askyesno(
            "Cazar",
            "¿Usar 10 balas para cazar?\n"
            "Puedes obtener 50-200 lbs de comida."
        )
        
        if respuesta:
            self.game_state['municion'] -= 10
            
            # Simular caza
            probabilidad_exito = random.random()
            if probabilidad_exito > 0.4:  # 60% de éxito
                comida_obtenida = random.randint(50, 200)
                self.game_state['comida'] += comida_obtenida
                self.log_event(f"🎯 Caza exitosa! +{comida_obtenida} lbs de comida")
                messagebox.showinfo(
                    "Caza Exitosa",
                    f"¡Caza exitosa!\nObtuviste {comida_obtenida} lbs de comida."
                )
            else:
                self.log_event("🎯 Fallaste la caza")
                messagebox.showinfo(
                    "Caza Fallida",
                    "No lograste cazar nada.\nPerdiste 10 balas."
                )
            
            self.update_game_display()
    
    def open_shop(self):
        """Abre la tienda"""
        # Verificar si estamos en un fuerte
        en_fuerte = False
        for hito in self.hitos:
            if hito['tipo'] == 'fuerte':
                distancia_diferencia = abs(self.game_state['distancia_recorrida'] - hito['distancia'])
                if distancia_diferencia < 20:
                    en_fuerte = True
                    break
        
        if not en_fuerte:
            messagebox.showwarning(
                "No hay Fuerte Cercano",
                "Debes estar cerca de un fuerte para comprar suministros."
            )
            return
        
        self.show_shop_screen()
    
    def calculate_total(self):
        """Calcula el total de la compra"""
        total = 0
        
        # Productos y sus índices
        productos = [
            {'spin_index': 0, 'precio': self.precios['comida'], 'multiplicador': 1},
            {'spin_index': 1, 'precio': self.precios['municion'], 'multiplicador': 20},
            {'spin_index': 2, 'precio': self.precios['bueyes'], 'multiplicador': 1},
            {'spin_index': 3, 'precio': self.precios['rueda_carro'], 'multiplicador': 1},
            {'spin_index': 4, 'precio': self.precios['medicinas'], 'multiplicador': 1}
        ]
        
        for producto in productos:
            try:
                cantidad = int(self.product_spins[producto['spin_index']].get())
                total += cantidad * producto['precio'] * producto['multiplicador']
            except:
                pass
        
        self.total_label.config(text=f"${total:.2f}")
        return total
    
    def make_purchase(self):
        """Realiza la compra"""
        total = self.calculate_total()
        
        if total > self.game_state['dinero']:
            messagebox.showerror(
                "Fondos Insuficientes",
                f"No tienes suficiente dinero.\n"
                f"Total: ${total:.2f}\n"
                f"Disponible: ${self.game_state['dinero']}"
            )
            return
        
        if total == 0:
            messagebox.showinfo(
                "Compra Vacía",
                "No seleccionaste ningún artículo."
            )
            return
        
        # Confirmar compra
        confirmacion = messagebox.askyesno(
            "Confirmar Compra",
            f"¿Confirmar compra por ${total:.2f}?"
        )
        
        if not confirmacion:
            return
        
        # Procesar compra
        self.game_state['dinero'] -= total
        
        # Comida
        try:
            cantidad_comida = int(self.product_spins[0].get())
            self.game_state['comida'] += cantidad_comida
        except:
            pass
        
        # Munición
        try:
            cantidad_municion = int(self.product_spins[1].get())
            self.game_state['municion'] += cantidad_municion * 20
        except:
            pass
        
        # Bueyes
        try:
            cantidad_bueyes = int(self.product_spins[2].get())
            self.game_state['bueyes'] += cantidad_bueyes
            if self.game_state['bueyes'] > 8:
                self.game_state['bueyes'] = 8
        except:
            pass
        
        # Ruedas (mejora carro)
        try:
            cantidad_ruedas = int(self.product_spins[3].get())
            self.game_state['condicion_carro'] = min(
                100, self.game_state['condicion_carro'] + (cantidad_ruedas * 10)
            )
        except:
            pass
        
        # Medicinas
        try:
            cantidad_medicinas = int(self.product_spins[4].get())
            # Mejorar salud del grupo
            for miembro in self.game_state['miembros_grupo']:
                miembro['salud'] = min(100, miembro['salud'] + (cantidad_medicinas * 10))
                if cantidad_medicinas > 0:
                    miembro['enfermo'] = False
                    miembro['herido'] = False
        except:
            pass
        
        # Registrar evento
        self.log_event(f"🛒 Compra realizada por ${total:.2f}")
        
        # Cerrar tienda
        self.close_shop()
        
        # Actualizar pantalla
        self.update_game_display()
        
        messagebox.showinfo(
            "Compra Exitosa",
            f"Compra completada por ${total:.2f}\n"
            f"Recursos actualizados."
        )
    
    def close_shop(self):
        """Cierra la tienda"""
        # Resetear contadores
        for spin in self.product_spins:
            spin.delete(0, tk.END)
            spin.insert(0, "0")
        
        self.show_game_screen()
    
    def save_game(self):
        """Guarda el juego"""
        nombre_archivo = simpledialog.askstring(
            "Guardar Juego",
            "Nombre del archivo de guardado:"
        )
        
        if not nombre_archivo:
            return
        
        if not nombre_archivo.endswith('.otrail'):
            nombre_archivo += '.otrail'
        
        try:
            # Convertir datetime a string para JSON
            estado_guardado = self.game_state.copy()
            estado_guardado['fecha_actual'] = estado_guardado['fecha_actual'].isoformat()
            
            with open(nombre_archivo, 'w') as f:
                json.dump(estado_guardado, f, indent=2)
            
            messagebox.showinfo(
                "Juego Guardado",
                f"Juego guardado en: {nombre_archivo}"
            )
            
            self.log_event(f"💾 Juego guardado: {nombre_archivo}")
            
        except Exception as e:
            messagebox.showerror(
                "Error al Guardar",
                f"No se pudo guardar el juego:\n{str(e)}"
            )
    
    def return_to_menu(self):
        """Regresa al menú principal"""
        respuesta = messagebox.askyesno(
            "Volver al Menú",
            "¿Volver al menú principal?\n\n"
            "Tu progreso no se guardará automáticamente."
        )
        
        if respuesta:
            self.show_main_menu()
    
    def show_game_over(self):
        """Muestra la pantalla de fin de juego"""
        # Calcular puntuación
        puntuacion = self.calcular_puntuacion()
        
        # Crear ventana de fin de juego
        popup = tk.Toplevel(self.root)
        popup.title("Fin del Juego")
        popup.geometry("600x500")
        popup.configure(bg='#2c3e50')
        popup.transient(self.root)
        popup.grab_set()
        
        # Título
        titulo = "¡JUEGO TERMINADO!"
        if self.game_state['razon'] == "¡Llegaste a Oregon!":
            titulo = "¡FELICIDADES!"
        
        ttk.Label(popup, text=titulo, 
                 style='Title.TLabel').pack(pady=20)
        
        # Razón
        ttk.Label(popup, text=self.game_state['razon'],
                 font=('Arial', 14),
                 foreground='#e74c3c' if "murió" in self.game_state['razon'] else '#2ecc71').pack(pady=10)
        
        # Estadísticas
        stats_frame = ttk.LabelFrame(popup, text="ESTADÍSTICAS", padding=15)
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        estadisticas = [
            f"Distancia recorrida: {self.game_state['distancia_recorrida']} / 2000 millas",
            f"Días viajados: {self.game_state['dias_viajados']}",
            f"Miembros vivos: {len([m for m in self.game_state['miembros_grupo'] if m['salud'] > 0])}/5",
            f"Hitos alcanzados: {self.game_state['hitos_pasados'] // 100}",
            f"Comida restante: {self.game_state['comida']} lbs",
            f"Dinero restante: ${self.game_state['dinero']}",
            f"Puntuación final: {puntuacion}"
        ]
        
        for stat in estadisticas:
            ttk.Label(stats_frame, text=stat,
                     font=('Arial', 11)).pack(anchor=tk.W, pady=2)
        
        # Miembros del grupo
        group_frame = ttk.LabelFrame(popup, text="ESTADO DEL GRUPO", padding=15)
        group_frame.pack(fill=tk.X, padx=20, pady=10)
        
        for miembro in self.game_state['miembros_grupo']:
            estado = "VIVO" if miembro['salud'] > 0 else "MUERTO"
            color = "#2ecc71" if miembro['salud'] > 0 else "#e74c3c"
            
            ttk.Label(group_frame, 
                     text=f"{miembro['nombre']}: {estado} (Salud: {miembro['salud']}%)",
                     font=('Arial', 11),
                     foreground=color).pack(anchor=tk.W, pady=2)
        
        # Botones
        button_frame = ttk.Frame(popup)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Nuevo Juego",
                  command=lambda: self.restart_game(popup)).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Volver al Menú",
                  command=lambda: self.return_from_game_over(popup)).pack(side=tk.LEFT, padx=5)
    
    def calcular_puntuacion(self):
        """Calcula la puntuación final"""
        if not self.game_state['juego_terminado']:
            return 0
        
        puntuacion = 0
        
        # Puntos por distancia
        puntos_distancia = self.game_state['distancia_recorrida'] * 10
        puntuacion += puntos_distancia
        
        # Puntos por miembros vivos
        miembros_vivos = len([m for m in self.game_state['miembros_grupo'] if m['salud'] > 0])
        puntuacion += miembros_vivos * 1000
        
        # Puntos por recursos
        puntuacion += self.game_state['comida'] * 2
        puntuacion += self.game_state['municion'] * 5
        puntuacion += self.game_state['dinero'] * 10
        
        # Puntos por salud
        puntuacion += self.game_state['salud'] * 50
        
        # Puntos por hitos
        puntuacion += (self.game_state['hitos_pasados'] // 100) * 500
        
        # Bonus por llegar a Oregon
        if self.game_state['razon'] == "¡Llegaste a Oregon!":
            puntuacion *= 2
            puntuacion += 10000
        
        # Multiplicador por dificultad
        multiplicadores = {
            'facil': 0.5,
            'medio': 1.0,
            'dificil': 1.5,
            'experto': 2.0
        }
        
        puntuacion = int(puntuacion * multiplicadores[self.game_state['dificultad']])
        
        self.game_state['puntuacion'] = puntuacion
        return puntuacion
    
    def restart_game(self, popup):
        """Reinicia el juego"""
        popup.destroy()
        self.__init__(self.root)
        self.start_new_game()
    
    def return_from_game_over(self, popup):
        """Regresa al menú desde fin de juego"""
        popup.destroy()
        self.show_main_menu()

# ===========================================
# FUNCIÓN PRINCIPAL
# ===========================================
def main():
    """Función principal"""
    root = tk.Tk()
    app = OregonTrailGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
