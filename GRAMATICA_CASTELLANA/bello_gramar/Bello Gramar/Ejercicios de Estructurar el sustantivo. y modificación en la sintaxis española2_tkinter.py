import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class AplicacionGramatica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica de Sintaxis Española")
        self.geometry("1000x700")
        self.configure_styles()
        
        # Base de datos inicial ampliada
        self.ejemplos = [
            {"oracion": "El niño curioso preguntó sobre las estrellas.", "tipo": "adjetivo", 
             "modificador": "curioso", "oracion_parcial": "El niño [  ] preguntó sobre las estrellas."},
            {"oracion": "La montaña nevada brillaba bajo el sol.", "tipo": "adjetivo",
             "modificador": "nevada", "oracion_parcial": "La montaña [  ] brillaba bajo el sol."},
            {"oracion": "Las hojas del otoño cubrían el suelo.", "tipo": "complemento",
             "modificador": "del otoño", "oracion_parcial": "Las hojas [  ] cubrían el suelo."},
            {"oracion": "El hombre de sombrero caminaba despacio.", "tipo": "complemento",
             "modificador": "de sombrero", "oracion_parcial": "El hombre [  ] caminaba despacio."},
            {"oracion": "El libro que compré ayer tiene dedicatoria.", "tipo": "proposicion",
             "modificador": "que compré ayer", "oracion_parcial": "El libro [  ] tiene dedicatoria."},
            {"oracion": "La ciudad donde nací es hermosa.", "tipo": "proposicion",
             "modificador": "donde nací", "oracion_parcial": "La ciudad [  ] es hermosa."},
            {"oracion": "Un silencio inquietante llenó la sala.", "tipo": "adjetivo",
             "modificador": "inquietante", "oracion_parcial": "Un silencio [  ] llenó la sala."},
            {"oracion": "El camino hacia el bosque estaba bloqueado.", "tipo": "complemento",
             "modificador": "hacia el bosque", "oracion_parcial": "El camino [  ] estaba bloqueado."},
            {"oracion": "El artista cuyas obras exponen es famoso.", "tipo": "proposicion",
             "modificador": "cuyas obras exponen", "oracion_parcial": "El artista [  ] es famoso."}
        ]
        
        self.crear_interfaz()
    
    def configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Estilos personalizados
        self.style.configure('Titulo.TLabel', font=('Arial', 14, 'bold'), foreground='#2c3e50')
        self.style.configure('Instruccion.TLabel', font=('Arial', 11), foreground='#34495e')
        self.style.configure('Correcto.TLabel', foreground='#27ae60', font=('Arial', 11, 'bold'))
        self.style.configure('Incorrecto.TLabel', foreground='#c0392b', font=('Arial', 11, 'bold'))
        self.style.configure('Boton.TButton', font=('Arial', 10), padding=5)
        self.style.map('Boton.TButton', 
                      foreground=[('active', '#ffffff'), ('!active', '#ffffff')],
                      background=[('active', '#2980b9'), ('!active', '#3498db')])
    
    def crear_interfaz(self):
        self.notebook = ttk.Notebook(self)
        self.crear_tabs()
        self.notebook.pack(expand=True, fill='both')
    
    def crear_tabs(self):
        # Crear todas las pestañas
        tabs = [
            ('Clasificar', self.crear_tab_clasificar),
            ('Reescribir', self.crear_tab_reescribir),
            ('Crear', self.crear_tab_crear),
            ('Ejemplos', self.crear_tab_ejemplos),
            ('Cuestionarios', self.crear_tab_cuestionarios)
        ]
        
        for nombre, metodo in tabs:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=nombre)
            metodo(tab)
    
    def crear_tab_clasificar(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame, text="Clasifica el tipo de modificación", style='Titulo.TLabel').pack(pady=10)
        
        self.lbl_oracion_clasificar = ttk.Label(frame, text="", style='Instruccion.TLabel', wraplength=600)
        self.lbl_oracion_clasificar.pack(pady=15)
        
        self.cmb_tipo = ttk.Combobox(frame, values=["adjetivo", "complemento", "proposicion"], state="readonly")
        self.cmb_tipo.pack(pady=10)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="Comprobar", command=self.verificar_clasificacion, style='Boton.TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Nueva Oración", command=self.nueva_oracion_clasificar, style='Boton.TButton').pack(side='left', padx=5)
        
        self.lbl_resultado_clasificar = ttk.Label(frame, text="")
        self.lbl_resultado_clasificar.pack(pady=10)
        
        self.nueva_oracion_clasificar()
    
    def crear_tab_reescribir(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame, text="Reescribe la oración modificando el elemento", style='Titulo.TLabel').pack(pady=10)
        
        self.lbl_ejemplo_original = ttk.Label(frame, text="", style='Instruccion.TLabel', wraplength=600)
        self.lbl_ejemplo_original.pack(pady=15)
        
        self.txt_reescritura = tk.Text(frame, height=3, width=60, font=('Arial', 11))
        self.txt_reescritura.pack(pady=10)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="Comprobar", command=self.verificar_reescritura, style='Boton.TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Nuevo Ejemplo", command=self.nuevo_ejemplo_reescritura, style='Boton.TButton').pack(side='left', padx=5)
        
        self.lbl_resultado_reescritura = ttk.Label(frame, text="", wraplength=600)
        self.lbl_resultado_reescritura.pack(pady=10)
        
        self.nuevo_ejemplo_reescritura()
    
    def crear_tab_crear(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame, text="Crear Nueva Oración", style='Titulo.TLabel').pack(pady=10)
        
        # Controles del formulario
        form_frame = ttk.Frame(frame)
        form_frame.pack(pady=10)
        
        ttk.Label(form_frame, text="Tipo de modificación:", style='Instruccion.TLabel').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.cmb_tipo_crear = ttk.Combobox(form_frame, values=["adjetivo", "complemento", "proposicion"], state="readonly")
        self.cmb_tipo_crear.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Oración completa:", style='Instruccion.TLabel').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.entrada_oracion = ttk.Entry(form_frame, width=50)
        self.entrada_oracion.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="Modificador utilizado:", style='Instruccion.TLabel').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.entrada_modificador = ttk.Entry(form_frame, width=50)
        self.entrada_modificador.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(frame, text="Guardar Oración", command=self.guardar_oracion, style='Boton.TButton').pack(pady=15)
        
        self.lbl_mensaje_crear = ttk.Label(frame, text="")
        self.lbl_mensaje_crear.pack(pady=10)
    
    def crear_tab_ejemplos(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Treeview para mostrar ejemplos
        self.tree = ttk.Treeview(frame, columns=('Tipo', 'Oración'), show='headings')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.heading('Oración', text='Oración')
        self.tree.column('Tipo', width=120, anchor='center')
        self.tree.column('Oración', width=700, anchor='w')
        
        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')
        
        self.actualizar_treeview()
    
    def crear_tab_cuestionarios(self, parent):
        notebook = ttk.Notebook(parent)
        notebook.pack(expand=True, fill='both')
        
        # Subpestañas
        tab_completar = ttk.Frame(notebook)
        tab_opcion_multiple = ttk.Frame(notebook)
        
        notebook.add(tab_completar, text="Completar espacios")
        notebook.add(tab_opcion_multiple, text="Opción múltiple")
        
        self.crear_tab_completar(tab_completar)
        self.crear_tab_opcion_multiple(tab_opcion_multiple)
    
    def crear_tab_completar(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame, text="Completa el espacio en blanco", style='Titulo.TLabel').pack(pady=10)
        
        self.lbl_oracion_parcial = ttk.Label(frame, text="", style='Instruccion.TLabel', wraplength=600)
        self.lbl_oracion_parcial.pack(pady=15)
        
        self.entrada_completar = ttk.Entry(frame, width=50, font=('Arial', 11))
        self.entrada_completar.pack(pady=10)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="Comprobar", command=self.verificar_completar, style='Boton.TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Nueva Pregunta", command=self.nueva_pregunta_completar, style='Boton.TButton').pack(side='left', padx=5)
        
        self.lbl_resultado_completar = ttk.Label(frame, text="")
        self.lbl_resultado_completar.pack(pady=10)
        
        self.nueva_pregunta_completar()
    
    def crear_tab_opcion_multiple(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        
        ttk.Label(frame, text="Selecciona el tipo de modificación", style='Titulo.TLabel').pack(pady=10)
        
        self.lbl_oracion_multiple = ttk.Label(frame, text="", style='Instruccion.TLabel', wraplength=600)
        self.lbl_oracion_multiple.pack(pady=15)
        
        self.opciones_multiple = []
        self.respuesta_seleccionada = tk.IntVar()
        
        opciones_frame = ttk.Frame(frame)
        opciones_frame.pack(pady=10)
        
        for i in range(3):
            rb = ttk.Radiobutton(opciones_frame, text="", variable=self.respuesta_seleccionada, value=i)
            rb.grid(row=i, column=0, sticky='w', pady=5)
            self.opciones_multiple.append(rb)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=15)
        
        ttk.Button(btn_frame, text="Comprobar", command=self.verificar_opcion_multiple, style='Boton.TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Nueva Pregunta", command=self.nueva_pregunta_multiple, style='Boton.TButton').pack(side='left', padx=5)
        
        self.lbl_resultado_multiple = ttk.Label(frame, text="")
        self.lbl_resultado_multiple.pack(pady=10)
        
        self.nueva_pregunta_multiple()
    
    # Métodos de funcionalidad
    
    def nueva_oracion_clasificar(self):
        if not self.ejemplos:
            messagebox.showwarning("Advertencia", "No hay ejemplos disponibles")
            return
        
        self.ejemplo_actual = random.choice(self.ejemplos)
        self.lbl_oracion_clasificar.config(text=self.ejemplo_actual["oracion"])
        self.cmb_tipo.set('')
        self.lbl_resultado_clasificar.config(text="")
    
    def verificar_clasificacion(self):
        if not hasattr(self, 'ejemplo_actual'):
            return
        
        respuesta = self.cmb_tipo.get()
        if respuesta == self.ejemplo_actual["tipo"]:
            self.lbl_resultado_clasificar.config(text="¡Correcto!", style='Correcto.TLabel')
        else:
            mensaje = f"Incorrecto. Tipo correcto: {self.ejemplo_actual['tipo'].capitalize()}"
            self.lbl_resultado_clasificar.config(text=mensaje, style='Incorrecto.TLabel')
    
    def nuevo_ejemplo_reescritura(self):
        if not self.ejemplos:
            messagebox.showwarning("Advertencia", "No hay ejemplos disponibles")
            return
        
        self.ejemplo_reescritura = random.choice(self.ejemplos)
        self.lbl_ejemplo_original.config(text=self.ejemplo_reescritura["oracion"])
        self.txt_reescritura.delete('1.0', tk.END)
        self.lbl_resultado_reescritura.config(text="")
    
    def verificar_reescritura(self):
        nueva_version = self.txt_reescritura.get('1.0', tk.END).strip()
        if not nueva_version:
            return
        
        # Verificar que se haya modificado el elemento clave
        original = self.ejemplo_reescritura["modificador"]
        resultado = f"Original: {self.ejemplo_reescritura['oracion']}\nModificada: {nueva_version}"
        self.lbl_resultado_reescritura.config(text=resultado)
    
    def guardar_oracion(self):
        if len(self.ejemplos) >= 100:
            messagebox.showerror("Error", "Límite de 100 ejemplos alcanzado")
            return
        
        tipo = self.cmb_tipo_crear.get()
        oracion = self.entrada_oracion.get().strip()
        modificador = self.entrada_modificador.get().strip()
        
        # Validación de entrada
        if not tipo or not oracion or not modificador:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        if modificador not in oracion:
            messagebox.showerror("Error", "El modificador debe estar presente en la oración")
            return
        
        oracion_parcial = oracion.replace(modificador, "[  ]", 1)
        
        nuevo_ejemplo = {
            "oracion": oracion,
            "tipo": tipo,
            "modificador": modificador,
            "oracion_parcial": oracion_parcial
        }
        
        self.ejemplos.append(nuevo_ejemplo)
        self.actualizar_treeview()
        self.limpiar_formulario_crear()
        messagebox.showinfo("Éxito", "Oración añadida correctamente")
    
    def limpiar_formulario_crear(self):
        self.cmb_tipo_crear.set('')
        self.entrada_oracion.delete(0, tk.END)
        self.entrada_modificador.delete(0, tk.END)
    
    def actualizar_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for ejemplo in self.ejemplos:
            self.tree.insert('', 'end', values=(ejemplo['tipo'].capitalize(), ejemplo['oracion']))
    
    # Métodos para cuestionarios (continuar implementación similar)

if __name__ == "__main__":
    app = AplicacionGramatica()
    app.mainloop()
