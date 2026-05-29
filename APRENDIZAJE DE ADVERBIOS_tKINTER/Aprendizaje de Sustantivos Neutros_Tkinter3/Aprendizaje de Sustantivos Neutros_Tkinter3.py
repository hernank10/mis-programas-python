import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import random
import winsound

class NeutrosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Sustantivos Neutros")
        self.root.geometry("1000x750")
        
        # Cargar datos iniciales
        self.categorias = {
            "Cantidad": ["todo", "mucho", "más", "menos", "demasiado", "bastante", "asaz", "harto", "poco"],
            "Conceptos": ["algo", "nada", "nonada", "uno", "otro", "al"],
            "Infinitivos": ["cantar", "comer", "vivir", "pensar", "soñar", "andar", "amar", "temer", "reír", "llorar"]
        }
        
        self.archivo_datos = "ejemplos_neutros.json"
        self.ejemplos_base = [
            {"oracion": "Dios lo ha creado todo", "categoria": "Cantidad", "tipo": "todo"},
            {"oracion": "Mucho se habla, pero poco se actúa", "categoria": "Cantidad", "tipo": "mucho"},
            # ... (Agregar los 50 ejemplos aquí)
        ]
        self.ejemplos, self.personalizados = self.cargar_datos()
        
        # Configuración inicial
        self.configurar_estilos()
        self.crear_menu_principal()
        self.configurar_estados()

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#F0F0F0')
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('TLabel', font=('Arial', 10), background='#F0F0F0')
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#F0F0F0')
        style.configure('Subtitle.TLabel', font=('Arial', 12), background='#F0F0F0')
        style.configure('Progress.Horizontal.TProgressbar', thickness=20)

    def configurar_estados(self):
        self.current_practice_index = 0
        self.correct_count = 0
        self.incorrect_count = 0
        self.quiz_score = 0
        self.quiz_questions = []
        self.current_quiz_index = 0

    def cargar_datos(self):
        try:
            with open(self.archivo_datos, "r") as f:
                datos = json.load(f)
                return datos["ejemplos"], datos["personalizados"]
        except:
            return self.ejemplos_base, []

    def guardar_datos(self):
        with open(self.archivo_datos, "w") as f:
            json.dump({
                "ejemplos": self.ejemplos,
                "personalizados": self.personalizados
            }, f, indent=2)

    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        ttk.Label(main_frame, text="ESTUDIO DE SUSTANTIVOS NEUTROS", style='Title.TLabel').pack(pady=20)
        
        btn_style = {'width': 25, 'pady': 10}
        ttk.Button(main_frame, text="Modo Práctica", command=self.modo_practica).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Cuestionario Interactivo", command=self.iniciar_cuestionario).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Gestión de Ejemplos", command=self.gestion_ejemplos).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Diapositiva Conceptual", command=self.mostrar_diapositiva).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Importar/Exportar", command=self.menu_import_export).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Salir", command=self.root.quit).pack(pady=5, **btn_style)

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def modo_practica(self):
        self.limpiar_pantalla()
        self.configurar_estados()
        
        practice_frame = ttk.Frame(self.root)
        practice_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        self.barra_progreso = ttk.Progressbar(practice_frame, orient='horizontal', 
                                            length=400, mode='determinate',
                                            style='Progress.Horizontal.TProgressbar')
        self.barra_progreso.pack(pady=10)
        
        self.mostrar_ejemplo_practica(practice_frame)
        
        ttk.Button(practice_frame, text="Volver al Menú", command=self.crear_menu_principal).pack(pady=20)

    def mostrar_ejemplo_practica(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.destroy()
        
        if self.current_practice_index >= len(self.ejemplos):
            self.mostrar_resultado_practica()
            return

        ejemplo = self.ejemplos[self.current_practice_index]
        self.actualizar_barra_progreso()
        
        content_frame = ttk.Frame(frame)
        content_frame.pack(expand=True, pady=20)
        
        ttk.Label(content_frame, text=f"Ejemplo {self.current_practice_index + 1}/{len(self.ejemplos)}", 
                 style='Subtitle.TLabel').pack(pady=10)
        
        ttk.Label(content_frame, text=ejemplo['oracion'], font=('Arial', 12, 'italic')).pack(pady=10)
        
        ttk.Label(content_frame, text="Selecciona la categoría:").pack(pady=5)
        self.categoria_var = tk.StringVar()
        categorias_combobox = ttk.Combobox(content_frame, textvariable=self.categoria_var, 
                                         values=list(self.categorias.keys()))
        categorias_combobox.pack(pady=5)
        
        ttk.Label(content_frame, text="Escribe la oración completa:").pack(pady=5)
        self.entrada_usuario = ttk.Entry(content_frame, width=60)
        self.entrada_usuario.pack(pady=5)
        
        btn_frame = ttk.Frame(content_frame)
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="Verificar", command=lambda: self.verificar_respuesta(ejemplo)).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Siguiente", command=lambda: self.cambiar_ejemplo(1)).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Anterior", command=lambda: self.cambiar_ejemplo(-1)).pack(side=tk.LEFT, padx=5)

    def verificar_respuesta(self, ejemplo):
        categoria_correcta = ejemplo['categoria']
        oracion_correcta = ejemplo['oracion']
        correcto = True
        
        if self.categoria_var.get() != categoria_correcta:
            correcto = False
        if self.entrada_usuario.get().strip().lower() != oracion_correcta.lower():
            correcto = False
        
        if correcto:
            self.correct_count += 1
            self.play_sound(True)
            messagebox.showinfo("Correcto", "✓ Todas las respuestas son correctas!")
        else:
            self.incorrect_count += 1
            self.play_sound(False)
            mensaje = []
            if self.categoria_var.get() != categoria_correcta:
                mensaje.append(f"Categoría correcta: {categoria_correcta}")
            if self.entrada_usuario.get().strip().lower() != oracion_correcta.lower():
                mensaje.append(f"Oración correcta: {oracion_correcta}")
            messagebox.showinfo("Incorrecto", "\n".join(mensaje))
        
        self.current_practice_index += 1
        self.mostrar_ejemplo_practica(self.root.winfo_children()[0])

    # ... (Resto de funcionalidades implementadas similar al código anterior)

    def menu_import_export(self):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Importar ejemplos", command=self.importar_ejemplos)
        menu.add_command(label="Exportar ejemplos", command=self.exportar_ejemplos)
        menu.post(self.root.winfo_pointerx(), self.root.winfo_pointery())

    def play_sound(self, correct):
        try:
            if correct:
                winsound.Beep(1000, 200)
            else:
                winsound.Beep(400, 500)
        except:
            pass

    def mostrar_diapositiva(self):
        self.limpiar_pantalla()
        
        diapositiva_frame = ttk.Frame(self.root)
        diapositiva_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        contenido = """
        SUSTANTIVOS NEUTROS - CONCEPTOS CLAVE

        1. Categorías Principales:
        • Cantidad: Expresan magnitudes (todo, mucho, bastante)
        • Conceptos: Nociones abstractas (algo, nada, uno)
        • Infinitivos: Verbos sustantivados (el comer, el vivir)

        2. Características:
        - No tienen género gramatical
        - Funcionan como núcleos nominales
        - Algunos admiten artículos
        - Muchos son invariables en número

        3. Usos Especiales:
        • 'Todo' requiere 'lo' como complemento
        • 'Nada' admite artículo femenino
        • Infinitivos pueden pluralizarse
        """
        
        text_widget = tk.Text(diapositiva_frame, wrap=tk.WORD, font=('Arial', 12), 
                            height=20, width=80, padx=10, pady=10)
        text_widget.insert(tk.END, contenido)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(pady=10)
        
        ttk.Button(diapositiva_frame, text="Volver al Menú", command=self.crear_menu_principal).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = NeutrosApp(root)
    root.mainloop()
