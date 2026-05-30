import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import json
import os

class AprendizajeFuturosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Tiempos Futuros - Avanzado")
        self.root.geometry("1200x800")
        
        # Configuración inicial
        self.cargar_datos()
        self.configurar_estilos()
        
        # Variables de estado
        self.puntaje = 0
        self.total_preguntas = 0
        self.logros_desbloqueados = []
        self.nivel_dificultad = 1  # 1: Básico, 2: Intermedio, 3: Avanzado
        
        # Interfaz principal
        self.crear_interfaz_principal()
    
    def configurar_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Arial', 12), padding=6)
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('Achievement.TLabel', font=('Arial', 10), foreground='gold')
    
    def cargar_datos(self):
        self.datos = {
            "ejercicios": [],
            "logros": [],
            "progreso": {}
        }
        try:
            with open("datos_aprendizaje.json", "r", encoding="utf-8") as f:
                self.datos = json.load(f)
        except FileNotFoundError:
            self.inicializar_datos_predeterminados()
    
    def inicializar_datos_predeterminados(self):
        self.datos["ejercicios"] = [
            {
                "categoria": "Futuro simple",
                "dificultad": 1,
                "oracion": "Mañana yo ___ (estudiar) para el examen.",
                "respuesta": "estudiaré",
                "explicacion": "Futuro simple para acciones concretas"
            },
            # ... más ejercicios iniciales
        ]
        self.datos["logros"] = [
            {"nombre": "Principiante", "descripcion": "Completar 5 ejercicios"},
            {"nombre": "Experto", "descripcion": "90% de respuestas correctas"}
        ]
    
    def guardar_datos(self):
        with open("datos_aprendizaje.json", "w", encoding="utf-8") as f:
            json.dump(self.datos, f, ensure_ascii=False, indent=2)
    
    def crear_interfaz_principal(self):
        # Panel principal
        self.main_panel = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.main_panel.pack(fill=tk.BOTH, expand=True)
        
        # Panel izquierdo (menú)
        self.panel_izquierdo = ttk.Frame(self.main_panel, width=300)
        self.main_panel.add(self.panel_izquierdo)
        
        # Panel derecho (contenido)
        self.panel_derecho = ttk.Frame(self.main_panel)
        self.main_panel.add(self.panel_derecho)
        
        # Widgets del panel izquierdo
        self.crear_menu_principal()
        self.crear_barra_progreso()
        self.crear_logros()
        
        # Configuración inicial del panel derecho
        self.mostrar_pantalla_bienvenida()
    
    def crear_menu_principal(self):
        frame_menu = ttk.Frame(self.panel_izquierdo)
        frame_menu.pack(pady=20, padx=10, fill=tk.X)
        
        ttk.Label(frame_menu, text="Menú Principal", style='Title.TLabel').pack(pady=10)
        
        botones_menu = [
            ("Nueva Práctica", self.menu_practica),
            ("Progreso y Estadísticas", self.mostrar_estadisticas),
            ("Logros", self.mostrar_logros_completos),
            ("Importar/Exportar", self.menu_importar_exportar),
            ("Configuración", self.menu_configuracion),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones_menu:
            ttk.Button(frame_menu, text=texto, command=comando).pack(pady=5, fill=tk.X)
    
    def crear_barra_progreso(self):
        frame_progreso = ttk.Frame(self.panel_izquierdo)
        frame_progreso.pack(pady=10, padx=10, fill=tk.X)
        
        self.barra_progreso = ttk.Progressbar(frame_progreso, orient=tk.HORIZONTAL, length=280)
        self.barra_progreso.pack(pady=5)
        
        self.lbl_nivel = ttk.Label(frame_progreso, text="Nivel: 1")
        self.lbl_nivel.pack()
    
    def crear_logros(self):
        frame_logros = ttk.Frame(self.panel_izquierdo)
        frame_logros.pack(pady=10, padx=10, fill=tk.X)
        
        ttk.Label(frame_logros, text="Logros Recientes", style='Title.TLabel').pack()
        self.logros_container = ttk.Frame(frame_logros)
        self.logros_container.pack()
    
    def actualizar_ui(self):
        self.actualizar_barra_progreso()
        self.actualizar_logros()
        self.actualizar_nivel()
    
    def menu_practica(self):
        self.limpiar_panel_derecho()
        frame = ttk.Frame(self.panel_derecho)
        frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Seleccionar Modo de Práctica", style='Title.TLabel').pack(pady=10)
        
        opciones = [
            ("Práctica Libre", self.practica_libre),
            ("Por Categoría", self.seleccionar_categoria),
            ("Por Dificultad", self.seleccionar_dificultad),
            ("Desafío Cronometrado", self.practica_cronometrada)
        ]
        
        for texto, comando in opciones:
            ttk.Button(frame, text=texto, command=comando).pack(pady=5, fill=tk.X)
    
    def practica_libre(self):
        self.iniciar_practica(modo="libre")
    
    def seleccionar_categoria(self):
        categorias = list({e["categoria"] for e in self.datos["ejercicios"]})
        self.selector_opciones("Categoría", categorias, self.iniciar_practica)
    
    def seleccionar_dificultad(self):
        self.selector_opciones("Dificultad", [1, 2, 3], self.iniciar_practica)
    
    def selector_opciones(self, titulo, opciones, callback):
        ventana = tk.Toplevel(self.root)
        ventana.title(f"Seleccionar {titulo}")
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=20, padx=20)
        
        ttk.Label(frame, text=f"Seleccione {titulo}:").pack()
        
        for opcion in opciones:
            ttk.Button(frame, text=str(opcion), 
                      command=lambda o=opcion: [callback(o), ventana.destroy()]).pack(pady=5)
    
    def iniciar_practica(self, modo):
        # Lógica para filtrar ejercicios según el modo seleccionado
        # ... (implementación de filtrado)
        self.mostrar_interfaz_practica()
    
    def mostrar_interfaz_practica(self):
        self.limpiar_panel_derecho()
        # Implementar interfaz de práctica con temporizador y elementos de UI
        # ... (componentes de práctica interactiva)
    
    def mostrar_estadisticas(self):
        self.limpiar_panel_derecho()
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Generar gráficas con matplotlib
        categorias = list({e["categoria"] for e in self.datos["ejercicios"]})
        valores = [self.obtener_progreso(cat) for cat in categorias]
        
        ax.barh(categorias, valores)
        ax.set_title("Progreso por Categoría")
        
        canvas = FigureCanvasTkAgg(fig, master=self.panel_derecho)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    
    def menu_importar_exportar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Importar/Exportar Datos")
        
        ttk.Button(ventana, text="Importar Ejercicios", 
                  command=self.importar_ejercicios).pack(pady=10)
        ttk.Button(ventana, text="Exportar Progreso", 
                  command=self.exportar_progreso).pack(pady=10)
    
    def importar_ejercicios(self):
        archivo = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if archivo:
            try:
                with open(archivo, "r", encoding="utf-8") as f:
                    nuevos_ejercicios = json.load(f)
                self.datos["ejercicios"].extend(nuevos_ejercicios)
                self.guardar_datos()
                messagebox.showinfo("Éxito", "Ejercicios importados correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al importar: {str(e)}")
    
    def exportar_progreso(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".json")
        if archivo:
            try:
                with open(archivo, "w", encoding="utf-8") as f:
                    json.dump(self.datos["progreso"], f, indent=2)
                messagebox.showinfo("Éxito", "Progreso exportado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al exportar: {str(e)}")
    
    # ... (resto de métodos de funcionalidad)
    
    def verificar_logros(self):
        nuevos_logros = []
        # Lógica para verificar condiciones de logros
        if self.total_preguntas >= 5 and "Principiante" not in self.logros_desbloqueados:
            nuevos_logros.append("Principiante")
        
        # Añadir logros nuevos y mostrar notificación
        if nuevos_logros:
            self.logros_desbloqueados.extend(nuevos_logros)
            self.mostrar_notificacion_logro(nuevos_logros)
    
    def mostrar_notificacion_logro(self, logros):
        ventana = tk.Toplevel(self.root)
        ventana.title("¡Nuevo Logro Desbloqueado!")
        
        frame = ttk.Frame(ventana)
        frame.pack(pady=20, padx=20)
        
        ttk.Label(frame, text="🏆 ¡Logro Desbloqueado! 🏆", 
                style='Achievement.TLabel').pack()
        for logro in logros:
            ttk.Label(frame, text=logro, 
                     style='Achievement.TLabel').pack(pady=5)
        
        ventana.after(3000, ventana.destroy)
    
    def limpiar_panel_derecho(self):
        for widget in self.panel_derecho.winfo_children():
            widget.destroy()
    
    def actualizar_barra_progreso(self):
        total = len(self.datos["ejercicios"])
        completados = sum(1 for e in self.datos["ejercicios"] 
                        if e.get("completado", False))
        self.barra_progreso["value"] = (completados / total) * 100 if total > 0 else 0
    
    def actualizar_nivel(self):
        # Lógica para determinar el nivel basado en el progreso
        self.lbl_nivel.config(text=f"Nivel: {self.nivel_dificultad}")
    
    def actualizar_logros(self):
        for widget in self.logros_container.winfo_children():
            widget.destroy()
        
        for logro in self.logros_desbloqueados[-3:]:  # Mostrar últimos 3
            ttk.Label(self.logros_container, text=logro, 
                     style='Achievement.TLabel').pack(pady=2)
    
    def menu_configuracion(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Configuración")
        
        ttk.Label(ventana, text="Nivel de Dificultad:").pack(pady=10)
        
        dificultad = tk.IntVar(value=self.nivel_dificultad)
        ttk.Radiobutton(ventana, text="Básico", variable=dificultad, value=1).pack()
        ttk.Radiobutton(ventana, text="Intermedio", variable=dificultad, value=2).pack()
        ttk.Radiobutton(ventana, text="Avanzado", variable=dificultad, value=3).pack()
        
        ttk.Button(ventana, text="Guardar", 
                  command=lambda: [self.actualizar_dificultad(dificultad.get()),
                                  ventana.destroy()]).pack(pady=10)
    
    def actualizar_dificultad(self, nivel):
        self.nivel_dificultad = nivel
        messagebox.showinfo("Configuración", f"Dificultad actualizada a nivel {nivel}")
    
    def __del__(self):
        self.guardar_datos()

if __name__ == "__main__":
    root = tk.Tk()
    app = AprendizajeFuturosApp(root)
    root.mainloop()
