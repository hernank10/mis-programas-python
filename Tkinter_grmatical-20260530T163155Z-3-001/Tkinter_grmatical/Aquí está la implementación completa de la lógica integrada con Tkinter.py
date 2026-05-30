import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

class GrammarTutorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tutor Gramatical Avanzado")
        self.geometry("1000x800")
        self.CONSEJOS = self.cargar_consejos()
        self.progreso = self.cargar_progreso()
        self.configurar_estilos()
        self.crear_interfaz()
        
    def configurar_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Titulo.TLabel', font=('Arial', 18, 'bold'), foreground='#2c3e50')
        self.style.configure('Nivel.TLabel', font=('Arial', 14), foreground='#3498db')
        self.style.configure('Categoria.TButton', font=('Arial', 12), padding=10, 
                           foreground='#34495e', background='#ecf0f1')
        self.style.map('Categoria.TButton', background=[('active', '#3498db')])
        self.style.configure('Progress.Horizontal.TProgressbar', thickness=25, troughcolor='#bdc3c7')
        
    def crear_interfaz(self):
        # Marco principal
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Cabecera
        ttk.Label(self.main_frame, text="Tutor Gramatical", style='Titulo.TLabel').pack(pady=10)
        
        # Panel de progreso
        self.panel_progreso = ttk.LabelFrame(self.main_frame, text="Tu Progreso")
        self.panel_progreso.pack(fill=tk.X, pady=10)
        
        self.barra_progreso = ttk.Progressbar(self.panel_progreso, style='Progress.Horizontal.TProgressbar',
                                            orient=tk.HORIZONTAL, length=300, maximum=100)
        self.barra_progreso.pack(pady=5)
        
        self.lbl_nivel = ttk.Label(self.panel_progreso, style='Nivel.TLabel')
        self.lbl_nivel.pack()
        
        # Panel de categorías
        self.panel_categorias = ttk.LabelFrame(self.main_frame, text="Selecciona una Categoría")
        self.panel_categorias.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.crear_botones_categorias()
        
        # Panel de control
        self.panel_control = ttk.Frame(self.main_frame)
        self.panel_control.pack(fill=tk.X, pady=10)
        
        ttk.Button(self.panel_control, text="Logros", command=self.mostrar_logros).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.panel_control, text="Salir", command=self.guardar_y_salir).pack(side=tk.RIGHT, padx=5)
        
        self.actualizar_ui()
    
    def cargar_consejos(self):
        return {
            "Concordancia": {
                "Sujetos Colectivos": [
                    {"consejo": "Los sustantivos colectivos requieren verbo en singular",
                     "ejemplo": "La gente (aplaude/aplauden) → Respuesta: aplaude"}
                ]
            }
        }
    
    def cargar_progreso(self):
        try:
            with open('progreso.json', 'r') as f:
                data = json.load(f)
                return self.migrar_progreso(data)
        except FileNotFoundError:
            return self.crear_progreso_inicial()
    
    def crear_progreso_inicial(self):
        return {
            'progreso': {cat: {sub: [False]*len(ej) 
                            for sub, ej in self.CONSEJOS[cat].items()} 
                        for cat in self.CONSEJOS},
            'logros': {logro: False for logro in LOGROS},
            'estadisticas': {
                'racha_actual': 0,
                'racha_maxima': 0,
                'tiempo_practica': 0,
                'ejercicios_hoy': 0,
                'ultima_practica': None
            }
        }
    
    def crear_botones_categorias(self):
        for categoria in self.CONSEJOS.keys():
            frame = ttk.Frame(self.panel_categorias)
            frame.pack(fill=tk.X, pady=5)
            
            ttk.Label(frame, text=categoria, width=15).pack(side=tk.LEFT)
            
            for subcat in self.CONSEJOS[categoria].keys():
                btn = ttk.Button(frame, text=subcat, 
                               command=lambda c=categoria, s=subcat: self.iniciar_practica(c, s))
                btn.pack(side=tk.LEFT, padx=5)
    
    def iniciar_practica(self, categoria, subcategoria):
        ejercicio = self.obtener_ejercicio(categoria, subcategoria)
        if ejercicio:
            ventana = tk.Toplevel(self)
            PracticaWindow(ventana, ejercicio, self.actualizar_progreso)
    
    def obtener_ejercicio(self, categoria, subcategoria):
        # Lógica para seleccionar ejercicio no completado
        return self.CONSEJOS[categoria][subcategoria][0]
    
    def actualizar_progreso(self, resultado):
        # Actualizar progreso y estadísticas
        self.progreso['estadisticas']['ejercicios_hoy'] += 1
        self.actualizar_ui()
        self.guardar_progreso()
    
    def actualizar_ui(self):
        puntos = self.calcular_puntos()
        self.barra_progreso['value'] = puntos
        self.lbl_nivel.config(text=f"Nivel: {self.determinar_nivel(puntos)}")
    
    def calcular_puntos(self):
        return sum(
            sum(subcat) 
            for cat in self.progreso['progreso'].values() 
            for subcat in cat.values()
        )
    
    def determinar_nivel(self, puntos):
        niveles = {
            0: "Principiante",
            10: "Novato",
            30: "Aprendiz",
            50: "Intermedio",
            75: "Avanzado",
            90: "Experto",
            100: "Maestro"
        }
        return next((v for k, v in niveles.items() if puntos >= k), "Principiante")
    
    def mostrar_logros(self):
        ventana = tk.Toplevel(self)
        LogrosWindow(ventana, self.progreso['logros'])
    
    def guardar_progreso(self):
        with open('progreso.json', 'w') as f:
            json.dump(self.progreso, f)
    
    def guardar_y_salir(self):
        self.guardar_progreso()
        self.destroy()

class PracticaWindow(tk.Toplevel):
    def __init__(self, parent, ejercicio, callback):
        super().__init__(parent)
        self.ejercicio = ejercicio
        self.callback = callback
        self.configurar_ventana()
        self.crear_interfaz()
    
    def configurar_ventana(self):
        self.title("Práctica")
        self.geometry("600x400")
        self.grab_set()
    
    def crear_interfaz(self):
        ttk.Label(self, text="Ejercicio de Práctica", font=('Arial', 14)).pack(pady=10)
        ttk.Label(self, text=self.ejercicio['ejemplo'], wraplength=500).pack(pady=20)
        
        self.respuesta = ttk.Entry(self, width=50)
        self.respuesta.pack(pady=10)
        
        ttk.Button(self, text="Verificar", command=self.verificar_respuesta).pack(pady=10)
    
    def verificar_respuesta(self):
        entrada = self.respuesta.get().strip().lower()
        correcta = self.ejercicio['consejo'].lower()
        
        if entrada == correcta:
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
            self.callback(True)
        else:
            messagebox.showerror("Incorrecto", f"La respuesta correcta era:\n{self.ejercicio['consejo']}")
            self.callback(False)
        
        self.destroy()

class LogrosWindow(tk.Toplevel):
    def __init__(self, parent, logros):
        super().__init__(parent)
        self.title("Tus Logros")
        self.geometry("800x600")
        self.crear_interfaz(logros)
    
    def crear_interfaz(self, logros):
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        frame = ttk.Frame(canvas)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        for logro, estado in logros.items():
            color = "#2ecc71" if estado else "#e74c3c"
            ttk.Label(frame, text=LOGROS[logro]['nombre'], 
                     foreground=color, font=('Arial', 12)).pack(pady=5, anchor='w')
        
        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

if __name__ == "__main__":
    LOGROS = {
        "primer_paso": {"nombre": "🚀 Primer Paso", "descripcion": "Completar 1 ejercicio"}
    }
    
    app = GrammarTutorApp()
    app.mainloop()
