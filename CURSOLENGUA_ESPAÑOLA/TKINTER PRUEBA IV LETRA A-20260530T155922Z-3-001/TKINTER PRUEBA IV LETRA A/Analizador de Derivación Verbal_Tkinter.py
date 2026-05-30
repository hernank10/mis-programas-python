import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from collections import defaultdict

class DerivacionVerbalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analizador de Derivación Verbal")
        self.geometry("800x600")
        
        # Instancia del analizador
        self.analizador = DerivacionVerbal()
        
        # Configurar interfaz
        self.crear_widgets()
        self.cargar_datos()
    
    def crear_widgets(self):
        # Panel de pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de análisis
        self.crear_pestana_analisis()
        
        # Pestaña de agregar ejemplos
        self.crear_pestana_agregar()
        
        # Pestaña de ayuda
        self.crear_pestana_ayuda()
        
        # Barra de estado
        self.status_bar = tk.Label(self, text="Listo", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def crear_pestana_analisis(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Análisis")
        
        # Entrada de verbo
        lbl_verbo = ttk.Label(frame, text="Verbo a analizar:")
        lbl_verbo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        self.entrada_verbo = ttk.Entry(frame, width=30)
        self.entrada_verbo.grid(row=0, column=1, padx=5, pady=5)
        
        btn_analizar = ttk.Button(frame, text="Analizar", command=self.analizar_verbo)
        btn_analizar.grid(row=0, column=2, padx=5, pady=5)
        
        # Área de resultados
        self.resultados = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=70, height=20)
        self.resultados.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    
    def crear_pestana_agregar(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Agregar Ejemplo")
        
        # Campos del formulario
        labels = ["Verbo:", "Patrón:", "Región (opcional):"]
        self.campos = {}
        
        for i, texto in enumerate(labels):
            lbl = ttk.Label(frame, text=texto)
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entrada = ttk.Entry(frame, width=30)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.campos[texto[:-1]] = entrada
        
        btn_agregar = ttk.Button(frame, text="Guardar Ejemplo", command=self.agregar_ejemplo)
        btn_agregar.grid(row=3, column=1, padx=5, pady=10, sticky=tk.E)
    
    def crear_pestana_ayuda(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Ayuda")
        
        texto_ayuda = """Instrucciones de uso:
        
1. Análisis de verbos:
   - Ingrese un verbo en la pestaña de análisis
   - Haga clic en 'Analizar' para obtener resultados
   
2. Agregar ejemplos:
   - Complete los campos en la pestaña correspondiente
   - Los patrones deben seguir la notación:
     ej: -ear, a-N-ar, en-A-ecer
   
3. Los datos se guardan automáticamente al cerrar
   y se cargan al iniciar la aplicación"""
        
        lbl_ayuda = ttk.Label(frame, text=texto_ayuda, justify=tk.LEFT)
        lbl_ayuda.pack(padx=10, pady=10, anchor=tk.W)
    
    def actualizar_status(self, mensaje):
        self.status_bar.config(text=mensaje)
        self.after(3000, lambda: self.status_bar.config(text="Listo"))
    
    def analizar_verbo(self):
        verbo = self.entrada_verbo.get().strip().lower()
        if not verbo:
            messagebox.showerror("Error", "Por favor ingrese un verbo")
            return
        
        self.resultados.delete(1.0, tk.END)
        reporte = self.analizador.generar_informe_gui(verbo)
        self.resultados.insert(tk.INSERT, reporte)
        self.actualizar_status(f"Análisis completado para: {verbo}")
    
    def agregar_ejemplo(self):
        datos = {campo: entrada.get().strip() for campo, entrada in self.campos.items()}
        
        if not datos["Verbo"] or not datos["Patrón"]:
            messagebox.showerror("Error", "Verbo y Patrón son obligatorios")
            return
        
        self.analizador.agregar_ejemplo(
            datos["Verbo"], 
            datos["Patrón"], 
            datos["Región"] if datos["Región"] else None
        )
        
        for entrada in self.campos.values():
            entrada.delete(0, tk.END)
        
        self.actualizar_status(f"Ejemplo agregado: {datos['Verbo']}")
        messagebox.showinfo("Éxito", "Ejemplo agregado correctamente")
    
    def cargar_datos(self):
        try:
            self.analizador.cargar_datos()
            self.actualizar_status("Datos cargados exitosamente")
        except Exception as e:
            messagebox.showwarning("Advertencia", f"No se encontraron datos previos: {str(e)}")
    
    def on_cerrar(self):
        self.analizador.guardar_datos()
        self.destroy()

class DerivacionVerbal:
    def __init__(self):
        self.patrones = {
            'sufijos_comunes': ['-ar', '-ear', '-ecer', '-izar', '-ificar'],
            'parasintesis': ['a-...-ar', 'en-...-ar', 'des-...-ar'],
            'interfijos': ['-ec-', '-ific-', '-iz-']
        }
        
        self.ejemplos = defaultdict(list)
        self.variantes = {
            'diacronicas': defaultdict(str),
            'diatopicas': defaultdict(list)
        }
        
        try:
            self.cargar_datos()
        except FileNotFoundError:
            self.cargar_datos_base()
    
    def cargar_datos_base(self):
        self.ejemplos.update({
            '-ear': ['canturrear', 'matear', 'patear'],
            '-izar': ['argentinizar', 'computerizar'],
            'a-N-ar': ['abotonar', 'aterrizar'],
            'en-A-ecer': ['entristecer', 'enriquecer']
        })
        
        self.variantes['diacronicas'].update({
            'enriquir': 'enriquecer',
            'atristar': 'entristecer'
        })
        
        self.variantes['diatopicas'].update({
            'concientizar': ['América'],
            'liderizar': ['Región Andina']
        })
    
    def generar_informe_gui(self, verbo):
        reporte = []
        reporte.append(f"🔍 Análisis de: {verbo}\n")
        
        # Bases y afijos
        bases = self.identificar_bases(verbo)
        reporte.append("1. BASES Y AFIJOS:")
        for base, sufijo in bases:
            reporte.append(f"   - Posible base: {base.ljust(15)} | Sufijo: {sufijo}")
        
        # Patrones
        patrones = self.analizar_patron(verbo)
        reporte.append("\n2. PATRONES DETECTADOS:")
        for p in patrones:
            reporte.append(f"   - {p}")
        
        # Variantes
        variantes = self.verificar_variacion(verbo)
        reporte.append("\n3. VARIACIÓN:")
        if variantes:
            for v in variantes:
                reporte.append(f"   - {v}")
        else:
            reporte.append("   - No se registran variantes")
        
        # Ejemplos relacionados
        reporte.append("\n4. EJEMPLOS RELACIONADOS:")
        encontrados = False
        for patron, ejemplos in self.ejemplos.items():
            if verbo in ejemplos:
                encontrados = True
                reporte.append(f"   - Ejemplo de {patron}:")
                reporte.append(f"     {', '.join(e for e in ejemplos if e != verbo)[:50]}...")
        if not encontrados:
            reporte.append("   - No se encontraron ejemplos relacionados")
        
        return '\n'.join(reporte)
    
    # (Mantener los mismos métodos de análisis que en la versión anterior)
    # ... [Los métodos restantes son idénticos a la versión anterior del código]

if __name__ == "__main__":
    app = DerivacionVerbalApp()
    app.protocol("WM_DELETE_WINDOW", app.on_cerrar)
    app.mainloop()
