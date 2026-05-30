import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import textwrap
from PIL import Image, ImageTk
import os
import sys

# Estructura para almacenar ejemplos de oraciones condicionales
class ConditionalExample:
    def __init__(self, sentence, explanation, category):
        self.sentence = sentence
        self.explanation = explanation
        self.category = category

# Base de datos de ejemplos
examples = [
    ConditionalExample(
        "Si llueve, nos quedamos en casa.",
        "Condición presente real. Consecuencia inmediata.",
        "Reales"
    ),
    ConditionalExample(
        "Si tienes hambre, come algo.",
        "Condición presente. Consecuencia en imperativo.",
        "Reales"
    ),
    ConditionalExample(
        "Si terminas temprano, llámame.",
        "Condición futura posible. Consecuencia en imperativo.",
        "Reales"
    ),
    ConditionalExample(
        "Si estudias, apruebas el examen.",
        "Condición general/real. Relación causa-efecto.",
        "Reales"
    ),
    ConditionalExample(
        "Si quieres venir, debes avisar.",
        "Condición posible. Consecuencia con verbo modal.",
        "Reales"
    ),
    ConditionalExample(
        "Si tuviera dinero, compraría una casa.",
        "Condición improbable en presente. Deseo/consecuencia hipotética.",
        "Potenciales"
    ),
    ConditionalExample(
        "Si pudiera volar, viajaría por todo el mundo.",
        "Condición imposible física. Consecuencia imaginaria.",
        "Potenciales"
    ),
    ConditionalExample(
        "Si tuviese más tiempo, te ayudaría.",
        "Condición improbable. Oferta cortés hipotética.",
        "Potenciales"
    ),
    ConditionalExample(
        "Si lloviera mañana, cancelaríamos el picnic.",
        "Condición meteorológica futura improbable.",
        "Potenciales"
    ),
    ConditionalExample(
        "Si fuera tú, no iría a esa reunión.",
        "Consejo hipotético con improbabilidad de ser el otro.",
        "Potenciales"
    ),
    ConditionalExample(
        "Si hubieras estudiado, habrías aprobado el examen.",
        "Condición pasada no cumplida. Consecuencia lógica fallida.",
        "Irreales"
    ),
    ConditionalExample(
        "Si hubiese sabido que venías, te habría esperado.",
        "Condición pasada no conocida. Consecuencia deseada no realizada.",
        "Irreales"
    ),
    ConditionalExample(
        "Si hubiéramos salido antes, no habríamos perdido el tren.",
        "Acción pasada no realizada. Consecuencia negativa evitable.",
        "Irreales"
    ),
    ConditionalExample(
        "Si hubieses llamado, habría ido a recogerte.",
        "Acción pasada no realizada. Oferta de ayuda no materializada.",
        "Irreales"
    ),
    ConditionalExample(
        "Si no hubiera llovido, la boda habría sido en el jardín.",
        "Condición meteorológica pasada no deseada. Plan original frustrado.",
        "Irreales"
    )
]

# Colores para la interfaz
COLORS = {
    "background": "#2c3e50",
    "card_bg": "#34495e",
    "text": "#ecf0f1",
    "button": "#3498db",
    "button_hover": "#2980b9",
    "success": "#2ecc71",
    "error": "#e74c3c",
    "warning": "#f39c12",
    "juego1": "#3498db",
    "juego2": "#2ecc71",
    "juego3": "#f1c40f",
    "juego4": "#9b59b6",
    "juego5": "#e74c3c"
}

class ConditionalSentencesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Constructor de Oraciones Condicionales")
        self.root.geometry("1000x700")
        self.root.configure(bg=COLORS["background"])
        
        # Estado del juego
        self.score = 0
        self.level = 1
        self.streak = 0
        
        # Configurar estilo
        self.setup_styles()
        
        # Crear interfaz
        self.create_widgets()
        
        # Cargar imágenes para el juego de memoria
        self.load_images()
    
    def setup_styles(self):
        # Estilo para los botones
        style = ttk.Style()
        style.configure("TButton", 
                        font=("Arial", 12, "bold"),
                        padding=10,
                        background=COLORS["button"],
                        foreground=COLORS["text"])
        
        style.map("TButton", 
                  background=[("active", COLORS["button_hover"])],
                  foreground=[("active", COLORS["text"])])
        
        # Estilo para las etiquetas
        style.configure("Title.TLabel", 
                        font=("Arial", 24, "bold"),
                        background=COLORS["background"],
                        foreground=COLORS["text"])
        
        style.configure("Subtitle.TLabel", 
                        font=("Arial", 16, "italic"),
                        background=COLORS["background"],
                        foreground=COLORS["text"])
        
        style.configure("GameTitle.TLabel", 
                        font=("Arial", 18, "bold"),
                        background=COLORS["background"],
                        foreground=COLORS["text"])
        
        style.configure("Status.TLabel", 
                        font=("Arial", 12),
                        background=COLORS["background"],
                        foreground=COLORS["text"])
        
        style.configure("Card.TFrame", 
                        background=COLORS["card_bg"],
                        relief="raised",
                        borderwidth=2)
        
        style.configure("Card.TLabel", 
                        font=("Arial", 12),
                        background=COLORS["card_bg"],
                        foreground=COLORS["text"],
                        wraplength=380)
    
    def create_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title_label = ttk.Label(self.main_frame, text="Constructor de Oraciones Condicionales", style="Title.TLabel")
        title_label.pack(pady=10)
        
        subtitle_label = ttk.Label(self.main_frame, text="Aprende español con la RAE", style="Subtitle.TLabel")
        subtitle_label.pack(pady=5)
        
        # Estado del juego
        self.status_frame = ttk.Frame(self.main_frame)
        self.status_frame.pack(fill="x", pady=10)
        
        self.score_label = ttk.Label(self.status_frame, text=f"Puntuación: {self.score}", style="Status.TLabel")
        self.score_label.pack(side="left", padx=10)
        
        self.level_label = ttk.Label(self.status_frame, text=f"Nivel: {self.level}", style="Status.TLabel")
        self.level_label.pack(side="left", padx=10)
        
        self.streak_label = ttk.Label(self.status_frame, text=f"Racha: {self.streak}", style="Status.TLabel")
        self.streak_label.pack(side="left", padx=10)
        
        # Separador
        ttk.Separator(self.main_frame, orient="horizontal").pack(fill="x", pady=20)
        
        # Botones de juegos
        games_frame = ttk.Frame(self.main_frame)
        games_frame.pack(fill="both", expand=True)
        
        # Crear botones para cada juego
        games = [
            ("Juego 1: Construye la Oración", self.show_game1, COLORS["juego1"]),
            ("Juego 2: Clasifica el Tipo", self.show_game2, COLORS["juego2"]),
            ("Juego 3: Completa los Huecos", self.show_game3, COLORS["juego3"]),
            ("Juego 4: Ordena las Palabras", self.show_game4, COLORS["juego4"]),
            ("Juego 5: Memoria Condicional", self.show_game5, COLORS["juego5"])
        ]
        
        for i, (text, command, color) in enumerate(games):
            btn = ttk.Button(games_frame, text=text, command=command, style="TButton")
            btn.grid(row=i//2, column=i%2, padx=20, pady=15, sticky="nsew")
            btn.configure(style=f"TButton{color}")  # Usar estilo personalizado para cada botón
        
        # Configurar expansión de filas y columnas
        games_frame.columnconfigure(0, weight=1)
        games_frame.columnconfigure(1, weight=1)
        games_frame.rowconfigure(0, weight=1)
        games_frame.rowconfigure(1, weight=1)
        games_frame.rowconfigure(2, weight=1)
        
        # Botón de estadísticas
        stats_btn = ttk.Button(self.main_frame, text="Ver Estadísticas", command=self.show_stats)
        stats_btn.pack(pady=20)
    
    def load_images(self):
        # Cargar imágenes para el juego de memoria
        try:
            # Intento cargar imágenes desde el sistema
            self.card_back_img = Image.open("card_back.png") if os.path.exists("card_back.png") else None
            self.card_front_img = Image.open("card_front.png") if os.path.exists("card_front.png") else None
            
            if self.card_back_img and self.card_front_img:
                self.card_back_img = self.card_back_img.resize((100, 150), Image.LANCZOS)
                self.card_front_img = self.card_front_img.resize((100, 150), Image.LANCZOS)
                
                self.card_back_photo = ImageTk.PhotoImage(self.card_back_img)
                self.card_front_photo = ImageTk.PhotoImage(self.card_front_img)
            else:
                # Si no hay imágenes, usar colores
                self.card_back_photo = None
                self.card_front_photo = None
        except:
            # En caso de error, usar colores
            self.card_back_photo = None
            self.card_front_photo = None
    
    def update_score(self, correct):
        if correct:
            self.score += 10 * self.level
            self.streak += 1
            if self.streak % 5 == 0:
                self.level += 1
        else:
            self.streak = 0
        
        # Actualizar etiquetas de estado
        self.score_label.config(text=f"Puntuación: {self.score}")
        self.level_label.config(text=f"Nivel: {self.level}")
        self.streak_label.config(text=f"Racha: {self.streak}")
    
    def get_random_example(self):
        return random.choice(examples)
    
    def show_game1(self):
        self.clear_main_frame()
        
        # Configurar título del juego
        title_label = ttk.Label(self.main_frame, text="Juego 1: Construye la Oración", style="GameTitle.TLabel")
        title_label.pack(pady=10)
        
        # Obtener ejemplo aleatorio
        self.current_example = self.get_random_example()
        
        # Mostrar ejemplo
        example_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        example_frame.pack(fill="x", padx=50, pady=10)
        
        example_label = ttk.Label(example_frame, 
                                 text=f"Ejemplo: {self.current_example.sentence}\n\nExplicación: {self.current_example.explanation}",
                                 style="Card.TLabel")
        example_label.pack(padx=20, pady=20)
        
        # Entrada de usuario
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(fill="x", padx=50, pady=20)
        
        ttk.Label(input_frame, text="Escribe tu oración aquí:", style="Status.TLabel").pack(anchor="w")
        
        self.user_input = tk.Text(input_frame, height=4, width=60, font=("Arial", 12))
        self.user_input.pack(pady=10)
        
        # Botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        check_btn = ttk.Button(button_frame, text="Verificar", command=self.check_sentence)
        check_btn.pack(side="left", padx=10)
        
        next_btn = ttk.Button(button_frame, text="Siguiente", command=self.show_game1)
        next_btn.pack(side="left", padx=10)
        
        menu_btn = ttk.Button(button_frame, text="Menú Principal", command=self.create_widgets)
        menu_btn.pack(side="left", padx=10)
        
        # Mensaje
        self.message_label = ttk.Label(self.main_frame, text="", style="Status.TLabel", foreground=COLORS["success"])
        self.message_label.pack(pady=10)
    
    def check_sentence(self):
        user_text = self.user_input.get("1.0", "end-1c").strip()
        
        if not user_text:
            self.message_label.config(text="Por favor escribe una oración", foreground=COLORS["error"])
            return
        
        # Verificar estructura básica
        has_si = " si " in user_text.lower() or "Si " in user_text
        has_comma = "," in user_text
        
        if has_si and has_comma:
            self.message_label.config(text="¡Correcto! Buena construcción condicional.", foreground=COLORS["success"])
            self.update_score(True)
        else:
            self.message_label.config(text="Recuerda usar 'si' y una coma para separar condición y consecuencia", 
                                    foreground=COLORS["error"])
            self.update_score(False)
    
    def show_game2(self):
        self.clear_main_frame()
        
        # Configurar título del juego
        title_label = ttk.Label(self.main_frame, text="Juego 2: Clasifica el Tipo", style="GameTitle.TLabel")
        title_label.pack(pady=10)
        
        # Obtener ejemplo aleatorio
        self.current_example = self.get_random_example()
        
        # Mostrar ejemplo
        example_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        example_frame.pack(fill="x", padx=50, pady=20)
        
        example_label = ttk.Label(example_frame, 
                                 text=self.current_example.sentence,
                                 style="Card.TLabel")
        example_label.pack(padx=20, pady=20)
        
        # Opciones
        options_frame = ttk.Frame(self.main_frame)
        options_frame.pack(pady=20)
        
        self.category_var = tk.StringVar()
        
        real_btn = ttk.Radiobutton(options_frame, text="Real (Condición posible)", 
                                  variable=self.category_var, value="Reales")
        real_btn.pack(anchor="w", padx=20, pady=5)
        
        potencial_btn = ttk.Radiobutton(options_frame, text="Potencial (Condición improbable)", 
                                       variable=self.category_var, value="Potenciales")
        potencial_btn.pack(anchor="w", padx=20, pady=5)
        
        irreal_btn = ttk.Radiobutton(options_frame, text="Irreal (Condición imposible)", 
                                    variable=self.category_var, value="Irreales")
        irreal_btn.pack(anchor="w", padx=20, pady=5)
        
        # Botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        check_btn = ttk.Button(button_frame, text="Verificar", command=self.check_category)
        check_btn.pack(side="left", padx=10)
        
        next_btn = ttk.Button(button_frame, text="Siguiente", command=self.show_game2)
        next_btn.pack(side="left", padx=10)
        
        menu_btn = ttk.Button(button_frame, text="Menú Principal", command=self.create_widgets)
        menu_btn.pack(side="left", padx=10)
        
        # Mensaje
        self.message_label = ttk.Label(self.main_frame, text="", style="Status.TLabel")
        self.message_label.pack(pady=10)
    
    def check_category(self):
        selected_category = self.category_var.get()
        
        if not selected_category:
            self.message_label.config(text="Por favor selecciona una categoría", foreground=COLORS["error"])
            return
        
        if selected_category == self.current_example.category:
            self.message_label.config(text=f"¡Correcto! {self.current_example.explanation}", 
                                    foreground=COLORS["success"])
            self.update_score(True)
        else:
            self.message_label.config(text=f"Incorrecto. Es una oración {self.current_example.category}", 
                                    foreground=COLORS["error"])
            self.update_score(False)
    
    def show_game3(self):
        self.clear_main_frame()
        
        # Configurar título del juego
        title_label = ttk.Label(self.main_frame, text="Juego 3: Completa los Huecos", style="GameTitle.TLabel")
        title_label.pack(pady=10)
        
        # Obtener ejemplo aleatorio
        self.current_example = self.get_random_example()
        
        # Dividir la oración en palabras
        words = self.current_example.sentence.split()
        
        # Seleccionar palabras para ocultar (2-4 palabras)
        num_blanks = min(4, max(2, len(words) // 3))
        self.blank_indices = random.sample(range(len(words)), num_blanks)
        self.blank_indices.sort()
        
        self.blank_answers = []
        self.blank_entries = []
        
        # Mostrar instrucciones
        ttk.Label(self.main_frame, text="Completa los espacios en blanco:", style="Status.TLabel").pack(pady=10)
        
        # Crear frame para la oración
        sentence_frame = ttk.Frame(self.main_frame)
        sentence_frame.pack(pady=20, padx=50, fill="x")
        
        # Mostrar la oración con espacios en blanco
        for i, word in enumerate(words):
            if i in self.blank_indices:
                # Guardar la respuesta correcta
                self.blank_answers.append(word.strip(',.!?;'))
                
                # Crear entrada
                entry = ttk.Entry(sentence_frame, width=10, font=("Arial", 12))
                entry.pack(side="left", padx=5)
                self.blank_entries.append(entry)
            else:
                label = ttk.Label(sentence_frame, text=word + " ", font=("Arial", 12), 
                                 background=COLORS["background"], foreground=COLORS["text"])
                label.pack(side="left")
        
        # Botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        check_btn = ttk.Button(button_frame, text="Verificar", command=self.check_blanks)
        check_btn.pack(side="left", padx=10)
        
        next_btn = ttk.Button(button_frame, text="Siguiente", command=self.show_game3)
        next_btn.pack(side="left", padx=10)
        
        menu_btn = ttk.Button(button_frame, text="Menú Principal", command=self.create_widgets)
        menu_btn.pack(side="left", padx=10)
        
        # Mensaje
        self.message_label = ttk.Label(self.main_frame, text="", style="Status.TLabel")
        self.message_label.pack(pady=10)
    
    def check_blanks(self):
        all_correct = True
        
        for i, entry in enumerate(self.blank_entries):
            user_answer = entry.get().strip()
            correct_answer = self.blank_answers[i]
            
            # Comparar sin distinguir mayúsculas/minúsculas
            if user_answer.lower() != correct_answer.lower():
                entry.configure(style="Error.TEntry")
                all_correct = False
            else:
                entry.configure(style="Success.TEntry")
        
        if all_correct:
            self.message_label.config(text=f"¡Correcto! {self.current_example.explanation}", 
                                    foreground=COLORS["success"])
            self.update_score(True)
        else:
            self.message_label.config(text=f"Incorrecto. La oración correcta es: {self.current_example.sentence}", 
                                    foreground=COLORS["error"])
            self.update_score(False)
    
    def show_game4(self):
        self.clear_main_frame()
        
        # Configurar título del juego
        title_label = ttk.Label(self.main_frame, text="Juego 4: Ordena las Palabras", style="GameTitle.TLabel")
        title_label.pack(pady=10)
        
        # Obtener ejemplo aleatorio
        self.current_example = self.get_random_example()
        
        # Dividir la oración en palabras
        words = self.current_example.sentence.split()
        random.shuffle(words)
        self.shuffled_words = words
        
        # Palabras disponibles
        ttk.Label(self.main_frame, text="Palabras disponibles:", style="Status.TLabel").pack(pady=10)
        
        # Frame para palabras disponibles
        self.available_frame = ttk.Frame(self.main_frame)
        self.available_frame.pack(fill="x", padx=50, pady=10)
        
        # Mostrar palabras mezcladas
        for word in self.shuffled_words:
            btn = ttk.Button(self.available_frame, text=word, 
                            command=lambda w=word: self.select_word(w))
            btn.pack(side="left", padx=5, pady=5)
        
        # Orden seleccionado
        ttk.Label(self.main_frame, text="Tu oración:", style="Status.TLabel").pack(pady=10)
        
        # Frame para palabras seleccionadas
        self.selected_frame = ttk.Frame(self.main_frame)
        self.selected_frame.pack(fill="x", padx=50, pady=10)
        
        self.selected_words = []
        
        # Botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        check_btn = ttk.Button(button_frame, text="Verificar", command=self.check_order)
        check_btn.pack(side="left", padx=10)
        
        next_btn = ttk.Button(button_frame, text="Siguiente", command=self.show_game4)
        next_btn.pack(side="left", padx=10)
        
        menu_btn = ttk.Button(button_frame, text="Menú Principal", command=self.create_widgets)
        menu_btn.pack(side="left", padx=10)
        
        # Mensaje
        self.message_label = ttk.Label(self.main_frame, text="", style="Status.TLabel")
        self.message_label.pack(pady=10)
    
    def select_word(self, word):
        # Crear botón en la sección seleccionada
        btn = ttk.Button(self.selected_frame, text=word, 
                        command=lambda w=word: self.deselect_word(w))
        btn.pack(side="left", padx=5, pady=5)
        
        # Guardar palabra seleccionada
        self.selected_words.append(word)
        
        # Eliminar botón de palabras disponibles
        for child in self.available_frame.winfo_children():
            if child.cget("text") == word:
                child.destroy()
                break
    
    def deselect_word(self, word):
        # Crear botón de nuevo en palabras disponibles
        btn = ttk.Button(self.available_frame, text=word, 
                        command=lambda w=word: self.select_word(w))
        btn.pack(side="left", padx=5, pady=5)
        
        # Eliminar de palabras seleccionadas
        self.selected_words.remove(word)
        
        # Eliminar botón de la sección seleccionada
        for child in self.selected_frame.winfo_children():
            if child.cget("text") == word:
                child.destroy()
                break
    
    def check_order(self):
        user_sentence = " ".join(self.selected_words)
        
        if user_sentence == self.current_example.sentence:
            self.message_label.config(text="¡Correcto! Orden perfecto.", foreground=COLORS["success"])
            self.update_score(True)
        else:
            self.message_label.config(text=f"Incorrecto. La oración correcta es: {self.current_example.sentence}", 
                                    foreground=COLORS["error"])
            self.update_score(False)
    
    def show_game5(self):
        self.clear_main_frame()
        
        # Configurar título del juego
        title_label = ttk.Label(self.main_frame, text="Juego 5: Memoria Condicional", style="GameTitle.TLabel")
        title_label.pack(pady=10)
        
        # Instrucciones
        ttk.Label(self.main_frame, text="Encuentra pares de condición y consecuencia", style="Status.TLabel").pack(pady=10)
        
        # Seleccionar 4 ejemplos únicos
        self.current_memory_examples = random.sample(examples, min(4, len(examples)))
        
        # Crear pares de cartas (condición y consecuencia)
        self.memory_cards = []
        self.flipped_cards = []
        self.matched_pairs = 0
        
        for ex in self.current_memory_examples:
            # Dividir la oración
            if ',' in ex.sentence:
                parts = ex.sentence.split(',', 1)
                condition = parts[0].strip()
                consequence = parts[1].strip()
                
                # Agregar par de cartas
                self.memory_cards.append({"text": condition, "type": "condición"})
                self.memory_cards.append({"text": consequence, "type": "consecuencia"})
        
        # Mezclar las cartas
        random.shuffle(self.memory_cards)
        
        # Crear tablero de cartas
        self.cards_frame = ttk.Frame(self.main_frame)
        self.cards_frame.pack(pady=20, padx=50, fill="both", expand=True)
        
        self.card_buttons = []
        
        # Crear botones para las cartas
        for i, card in enumerate(self.memory_cards):
            row = i // 4
            col = i % 4
            
            if self.card_back_photo:
                btn = ttk.Button(self.cards_frame, image=self.card_back_photo, 
                                command=lambda idx=i: self.flip_card(idx))
            else:
                btn = ttk.Button(self.cards_frame, text="?", 
                                command=lambda idx=i: self.flip_card(idx),
                                width=10, style="TButton")
            
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.card_buttons.append(btn)
        
        # Información de pares
        self.pairs_label = ttk.Label(self.main_frame, text="Pares encontrados: 0/4", style="Status.TLabel")
        self.pairs_label.pack(pady=10)
        
        # Botones
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        menu_btn = ttk.Button(button_frame, text="Menú Principal", command=self.create_widgets)
        menu_btn.pack(padx=10)
    
    def flip_card(self, index):
        # No permitir voltear más de 2 cartas
        if len(self.flipped_cards) >= 2:
            return
        
        # Mostrar contenido de la carta
        card = self.memory_cards[index]
        
        if self.card_front_photo:
            self.card_buttons[index].configure(image=self.card_front_photo)
            self.card_buttons[index].image = self.card_front_photo  # Mantener referencia
        else:
            wrapped_text = textwrap.fill(f"{card['text']}\n({card['type']})", width=15)
            self.card_buttons[index].configure(text=wrapped_text)
        
        # Guardar carta volteada
        self.flipped_cards.append(index)
        
        # Si tenemos dos cartas volteadas, verificar si son un par
        if len(self.flipped_cards) == 2:
            self.root.after(1500, self.check_memory_pair)
    
    def check_memory_pair(self):
        idx1, idx2 = self.flipped_cards
        card1 = self.memory_cards[idx1]
        card2 = self.memory_cards[idx2]
        
        # Verificar si son un par válido
        valid_pair = False
        for ex in self.current_memory_examples:
            if card1["text"] in ex.sentence and card2["text"] in ex.sentence:
                valid_pair = True
                break
        
        if valid_pair and card1["type"] != card2["type"]:
            # Par correcto
            self.card_buttons[idx1].configure(state="disabled")
            self.card_buttons[idx2].configure(state="disabled")
            
            self.matched_pairs += 1
            self.pairs_label.config(text=f"Pares encontrados: {self.matched_pairs}/4")
            
            if self.matched_pairs == 4:
                messagebox.showinfo("¡Felicidades!", "¡Has completado el juego de memoria!")
                self.update_score(True)
        else:
            # Voltear las cartas de nuevo
            if self.card_back_photo:
                self.card_buttons[idx1].configure(image=self.card_back_photo)
                self.card_buttons[idx2].configure(image=self.card_back_photo)
            else:
                self.card_buttons[idx1].configure(text="?")
                self.card_buttons[idx2].configure(text="?")
        
        self.flipped_cards = []
    
    def show_stats(self):
        # Crear ventana de estadísticas
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Estadísticas del Juego")
        stats_window.geometry("500x400")
        stats_window.configure(bg=COLORS["background"])
        
        # Título
        ttk.Label(stats_window, text="Estadísticas del Juego", style="Title.TLabel").pack(pady=20)
        
        # Estadísticas
        stats_frame = ttk.Frame(stats_window, style="Card.TFrame")
        stats_frame.pack(fill="both", expand=True, padx=50, pady=20)
        
        ttk.Label(stats_frame, text=f"Puntuación total: {self.score}", style="Status.TLabel").pack(pady=10)
        ttk.Label(stats_frame, text=f"Nivel actual: {self.level}", style="Status.TLabel").pack(pady=10)
        ttk.Label(stats_frame, text=f"Racha actual: {self.streak}", style="Status.TLabel").pack(pady=10)
        
        # Distribución por categoría
        category_count = {"Reales": 0, "Potenciales": 0, "Irreales": 0}
        for ex in examples:
            category_count[ex.category] += 1
        
        ttk.Label(stats_frame, text="\nEjemplos por categoría:", style="Status.TLabel").pack(pady=10)
        for category, count in category_count.items():
            ttk.Label(stats_frame, text=f"{category}: {count} ejemplos", style="Status.TLabel").pack(pady=5)
        
        # Botón de cierre
        ttk.Button(stats_window, text="Cerrar", command=stats_window.destroy).pack(pady=20)
    
    def clear_main_frame(self):
        # Eliminar todos los widgets del frame principal
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def create_widgets(self):
        # Restaurar la pantalla principal
        self.clear_main_frame()
        self.__init__(self.root)  # Recrear la interfaz principal

# Función principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ConditionalSentencesApp(root)
    root.mainloop()
