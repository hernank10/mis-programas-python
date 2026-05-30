Download
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

class GestionAtributosApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor Avanzado de Atributos")
        self.geometry("1200x800")
        
        # Datos y configuración inicial
        self.categorias = self.cargar_categorias()
        self.ejemplos = self.cargar_ejemplos()
        self.archivo_actual = None
        
        # Interfaz principal
        self.crear_menu_principal()
        self.crear_widgets()
        self.actualizar_lista_categorias()
    
    def crear_menu_principal(self):
        menubar = tk.Menu(self)
        
        # Menú Archivo
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo)
        menu_archivo.add_command(label="Abrir...", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_command(label="Guardar como...", command=self.guardar_como)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        
        # Menú Edición
        menu_edicion = tk.Menu(menubar, tearoff=0)
        menu_edicion.add_command(label="Nueva Categoría", command=self.crear_categoria)
        menu_edicion.add_command(label="Editar Categoría", command=self.editar_categoria)
        menu_edicion.add_separator()
        menu_edicion.add_command(label="Importar Ejemplos", command=self.importar_ejemplos)
        menubar.add_cascade(label="Edición", menu=menu_edicion)
        
        self.config(menu=menubar)
    
    def crear_widgets(self):
        self.notebook = ttk.Notebook(self)
        
        # Pestaña Gestión
        self.frame_gestion = ttk.Frame(self.notebook)
        self.crear_panel_gestion()
        self.notebook.add(self.frame_gestion, text="📂 Gestión")
        
        # Pestañas existentes (Ejercicios, Progreso, etc.)
        # ... (mantener las pestañas anteriores y añadir nuevas funcionalidades)
        
        self.notebook.pack(expand=True, fill='both')
    
    def crear_panel_gestion(self):
        # Panel izquierdo: Lista de ejemplos
        self.frame_lista = ttk.Frame(self.frame_gestion)
        self.frame_lista.pack(side='left', fill='y', padx=10, pady=10)
        
        self.lista_ejemplos = ttk.Treeview(self.frame_lista, columns=('ID', 'Categoría'), show='headings')
        self.lista_ejemplos.heading('ID', text='ID')
        self.lista_ejemplos.heading('Categoría', text='Categoría')
        self.lista_ejemplos.pack(fill='both', expand=True)
        self.lista_ejemplos.bind('<<TreeviewSelect>>', self.mostrar_detalle)
        
        # Controles de lista
        self.frame_controles = ttk.Frame(self.frame_lista)
        self.frame_controles.pack(fill='x', pady=5)
        
        ttk.Button(self.frame_controles, text="➕ Nuevo", command=self.crear_ejemplo).pack(side='left', padx=2)
        ttk.Button(self.frame_controles, text="✏️ Editar", command=self.editar_ejemplo).pack(side='left', padx=2)
        ttk.Button(self.frame_controles, text="🗑️ Eliminar", command=self.eliminar_ejemplo).pack(side='left', padx=2)
        
        # Panel derecho: Detalle/Edición
        self.frame_detalle = ttk.Frame(self.frame_gestion)
        self.frame_detalle.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        self.crear_formulario_detalle()
    
    def crear_formulario_detalle(self):
        ttk.Label(self.frame_detalle, text="Categoría:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.combo_categorias = ttk.Combobox(self.frame_detalle, state='readonly')
        self.combo_categorias.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
        
        ttk.Label(self.frame_detalle, text="Oración:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.txt_oracion = tk.Text(self.frame_detalle, height=3, width=40, wrap=tk.WORD)
        self.txt_oracion.grid(row=1, column=1, columnspan=2, sticky='ew', padx=5, pady=5)
        
        ttk.Label(self.frame_detalle, text="Atributo:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.entry_atributo = ttk.Entry(self.frame_detalle)
        self.entry_atributo.grid(row=2, column=1, sticky='ew', padx=5, pady=5)
        
        ttk.Label(self.frame_detalle, text="Tipo:").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.combo_tipo = ttk.Combobox(self.frame_detalle, values=[
            'Atributo del sujeto', 
            'Atributo del objeto',
            'Preposicional',
            'Participio'
        ])
        self.combo_tipo.grid(row=3, column=1, sticky='ew', padx=5, pady=5)
        
        ttk.Label(self.frame_detalle, text="Semántica:").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        self.entry_semantica = ttk.Entry(self.frame_detalle)
        self.entry_semantica.grid(row=4, column=1, sticky='ew', padx=5, pady=5)
        
        ttk.Button(self.frame_detalle, text="💾 Guardar Cambios", command=self.guardar_cambios).grid(row=5, column=1, pady=10)
    
    # --------------------------
    # Funcionalidades CRUD
    # --------------------------
    
    def crear_categoria(self):
        nueva_cat = simpledialog.askstring("Nueva Categoría", "Nombre de la nueva categoría:")
        if nueva_cat and nueva_cat not in self.categorias:
            self.categorias.append(nueva_cat)
            self.actualizar_lista_categorias()
            messagebox.showinfo("Éxito", f"Categoría '{nueva_cat}' creada!")
    
    def editar_categoria(self):
        vieja = self.combo_categorias.get()
        nueva = simpledialog.askstring("Editar Categoría", f"Nuevo nombre para '{vieja}':")
        if nueva and nueva != vieja:
            index = self.categorias.index(vieja)
            self.categorias[index] = nueva
            self.actualizar_lista_categorias()
    
    def crear_ejemplo(self):
        self.limpiar_formulario()
        self.combo_categorias.config(state='normal')
        self.current_ejemplo = None
    
    def editar_ejemplo(self):
        seleccionado = self.lista_ejemplos.selection()
        if seleccionado:
            item = self.lista_ejemplos.item(seleccionado[0])
            self.current_ejemplo = item['values'][0]
            self.cargar_datos_formulario()
    
    def eliminar_ejemplo(self):
        seleccionado = self.lista_ejemplos.selection()
        if seleccionado:
            if messagebox.askyesno("Confirmar", "¿Eliminar este ejemplo permanentemente?"):
                self.lista_ejemplos.delete(seleccionado[0])
    
    def guardar_cambios(self):
        datos = {
            'categoria': self.combo_categorias.get(),
            'oracion': self.txt_oracion.get("1.0", tk.END).strip(),
            'atributo': self.entry_atributo.get(),
            'tipo': self.combo_tipo.get(),
            'semantica': self.entry_semantica.get()
        }
        
        if not all(datos.values()):
            messagebox.showerror("Error", "¡Todos los campos son obligatorios!")
            return
        
        if self.current_ejemplo:
            # Actualizar existente
            pass
        else:
            # Nuevo ejemplo
            self.ejemplos.append(datos)
            self.actualizar_lista_ejemplos()
        
        self.limpiar_formulario()
    
    # --------------------------
    # Funciones auxiliares
    # --------------------------
    
    def actualizar_lista_categorias(self):
        self.combo_categorias['values'] = self.categorias
    
    def actualizar_lista_ejemplos(self):
        self.lista_ejemplos.delete(*self.lista_ejemplos.get_children())
        for idx, ejemplo in enumerate(self.ejemplos):
            self.lista_ejemplos.insert('', 'end', iid=idx, values=(idx+1, ejemplo['categoria']))
    
    def cargar_datos_formulario(self):
        ejemplo = self.ejemplos[self.current_ejemplo]
        self.combo_categorias.set(ejemplo['categoria'])
        self.txt_oracion.delete("1.0", tk.END)
        self.txt_oracion.insert(tk.END, ejemplo['oracion'])
        self.entry_atributo.delete(0, tk.END)
        self.entry_atributo.insert(0, ejemplo['atributo'])
        self.combo_tipo.set(ejemplo['tipo'])
        self.entry_semantica.delete(0, tk.END)
        self.entry_semantica.insert(0, ejemplo['semantica'])
    
    def limpiar_formulario(self):
        self.combo_categorias.set('')
        self.txt_oracion.delete("1.0", tk.END)
        self.entry_atributo.delete(0, tk.END)
        self.combo_tipo.set('')
        self.entry_semantica.delete(0, tk.END)
    
    # --------------------------
    # Manejo de archivos
    # --------------------------
    
    def nuevo_archivo(self):
        self.ejemplos = []
        self.archivo_actual = None
        self.actualizar_lista_ejemplos()
    
    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.ejemplos = data['ejemplos']
                    self.categorias = data['categorias']
                    self.archivo_actual = archivo
                    self.actualizar_lista_ejemplos()
                    self.actualizar_lista_categorias()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{str(e)}")
    
    def guardar_archivo(self):
        if self.archivo_actual:
            self.guardar_como(self.archivo_actual)
        else:
            self.guardar_como()
    
    def guardar_como(self, archivo=None):
        if not archivo:
            archivo = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON Files", "*.json")]
            )
        if archivo:
            try:
                data = {
                    'ejemplos': self.ejemplos,
                    'categorias': self.categorias
                }
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                self.archivo_actual = archivo
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar:\n{str(e)}")
    
    def importar_ejemplos(self):
        # Implementar lógica de importación CSV/Excel
        pass
    
    def cargar_categorias(self):
        return ["Concordancia", "Profesiones", "Estados"]
    
    def cargar_ejemplos(self):
        return []

if __name__ == "__main__":
    app = GestionAtributosApp()
    app.mainloop()
