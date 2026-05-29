import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class NeutrosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Sustantivos Neutros")
        self.root.geometry("900x700")
        
        # Cargar datos
        self.categorias = {
            "Cantidad": ["todo", "mucho", "más", "menos", "demasiado", "bastante", "asaz", "harto", "poco"],
            "Conceptos": ["algo", "nada", "nonada", "uno", "otro", "al"],
            "Infinitivos": ["cantar", "comer", "vivir", "pensar", "soñar", "andar", "amar", "temer", "reír", "llorar"]
        }
        
        self.archivo_datos = "ejemplos_neutros.json"
        self.ejemplos, self.personalizados = self.cargar_datos()
        
        # Configurar interfaz
        self.crear_menu_principal()
        self.configurar_estilos()
        
        # Variables de estado
        self.current_practice_index = 0
        self.quiz_score = 0
        self.quiz_questions = []

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#F0F0F0')
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#F0F0F0')
        style.configure('Subtitle.TLabel', font=('Arial', 12), background='#F0F0F0')

    def cargar_datos(self):
        try:
            with open(self.archivo_datos, "r") as f:
                datos = json.load(f)
                return datos["ejemplos"], datos["personalizados"]
        except:
            return [], []

    def guardar_datos(self):
        with open(self.archivo_datos, "w") as f:
            json.dump({"ejemplos": self.ejemplos, "personalizados": self.personalizados}, f)

    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        ttk.Label(main_frame, text="ESTUDIO DE SUSTANTIVOS NEUTROS", style='Title.TLabel').pack(pady=20)
        
        btn_style = {'width': 25, 'pady': 10}
        ttk.Button(main_frame, text="Modo Práctica", command=self.modo_practica).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Cuestionario Interactivo", command=self.cuestionario_interactivo).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Gestión de Ejemplos", command=self.gestion_ejemplos).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Diapositiva Conceptual", command=self.diapositiva_conceptual).pack(pady=5, **btn_style)
        ttk.Button(main_frame, text="Salir", command=self.root.quit).pack(pady=5, **btn_style)

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Resto de funcionalidades (practica, cuestionario, gestión)...
    # Implementar métodos similares usando widgets de Tkinter

    def modo_practica(self):
        self.limpiar_pantalla()
        
        practice_frame = ttk.Frame(self.root)
        practice_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        self.current_practice_index = 0
        self.mostrar_ejemplo_practica(practice_frame)
        
        ttk.Button(practice_frame, text="Volver al Menú", command=self.crear_menu_principal).pack(pady=20)

    def mostrar_ejemplo_practica(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.destroy()
        
        ejemplo = self.ejemplos[self.current_practice_index]
        
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
        self.entrada_usuario = ttk.Entry(content_frame, width=50)
        self.entrada_usuario.pack(pady=5)
        
        btn_frame = ttk.Frame(content_frame)
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="Verificar", command=lambda: self.verificar_respuesta(ejemplo)).pack(side=tk.LEFT, padx=5)
        
        if self.current_practice_index < len(self.ejemplos) - 1:
            ttk.Button(btn_frame, text="Siguiente", command=lambda: self.cambiar_ejemplo(1)).pack(side=tk.LEFT, padx=5)
        if self.current_practice_index > 0:
            ttk.Button(btn_frame, text="Anterior", command=lambda: self.cambiar_ejemplo(-1)).pack(side=tk.LEFT, padx=5)

    def verificar_respuesta(self, ejemplo):
        categoria_correcta = ejemplo['categoria']
        oracion_correcta = ejemplo['oracion']
        
        mensajes = []
        if self.categoria_var.get() == categoria_correcta:
            mensajes.append("✓ Categoría correcta!")
        else:
            mensajes.append(f"✗ Categoría correcta: {categoria_correcta}")
        
        if self.entrada_usuario.get().strip().lower() == oracion_correcta.lower():
            mensajes.append("✓ Escritura correcta!")
        else:
            mensajes.append(f"✗ Forma correcta: {oracion_correcta}")
        
        messagebox.showinfo("Resultado", "\n".join(mensajes))

    def cambiar_ejemplo(self, direction):
        self.current_practice_index = max(0, min(len(self.ejemplos)-1, self.current_practice_index + direction))
        self.mostrar_ejemplo_practica(self.root.winfo_children()[0])

    # Implementar métodos similares para cuestionario, gestión de ejemplos y diapositiva conceptual

    def diapositiva_conceptual(self):
        self.limpiar_pantalla()
        
        concept_frame = ttk.Frame(self.root)
        concept_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        ttk.Label(concept_frame, text="Conceptos Clave", style='Title.TLabel').pack(pady=10)
        
        content = """
        Categorías principales:
        - Sustantivos de cantidad: Expresan magnitudes (todo, mucho)
        - Sustantivos conceptuales: Nociones abstractas (algo, nada)
        - Infinitivos sustantivados: Verbos como núcleos nominales (el comer)
        
        Características:
        - No tienen género gramatical
        - Funcionan como núcleos nominales
        - Algunos admiten artículos
        - Muchos son invariables en número
        """
        
        text_widget = tk.Text(concept_frame, wrap=tk.WORD, font=('Arial', 12), 
                            height=15, width=60, padx=10, pady=10)
        text_widget.insert(tk.END, content)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(pady=10)
        
        ttk.Button(concept_frame, text="Volver al Menú", command=self.crear_menu_principal).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = NeutrosApp(root)
    root.mainloop()
