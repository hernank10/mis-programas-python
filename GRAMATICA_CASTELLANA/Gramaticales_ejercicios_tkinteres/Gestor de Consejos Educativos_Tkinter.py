import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os

class ConsejosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Consejos Educativos")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)
        
        # Datos y configuración
        self.categorias = ['Estudiantes', 'Profesores', 'Desarrolladores', 'IA']
        self.consejos = {cat: [] for cat in self.categorias}
        self.archivo_actual = None
        
        # Cargar datos iniciales
        self.cargar_datos_base()
        
        # Interfaz gráfica
        self.crear_widgets()
        self.actualizar_lista()
    
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo - Categorías y controles
        panel_izq = ttk.Frame(main_frame, width=250)
        panel_izq.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Lista de categorías
        self.lista_categorias = ttk.Treeview(panel_izq, show='tree', selectmode='browse')
        self.lista_categorias.pack(fill=tk.BOTH, expand=True, pady=5)
        for cat in self.categorias:
            self.lista_categorias.insert('', tk.END, text=cat, values=(cat,))
        self.lista_categorias.bind('<<TreeviewSelect>>', self.cambiar_categoria)
        
        # Controles principales
        ttk.Button(panel_izq, text="Nuevo Consejo", command=self.nuevo_consejo).pack(fill=tk.X, pady=2)
        ttk.Button(panel_izq, text="Eliminar", command=self.eliminar_consejo).pack(fill=tk.X, pady=2)
        
        # Panel derecho - Lista y editor
        panel_der = ttk.Frame(main_frame)
        panel_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Lista de consejos
        self.lista_consejos = ttk.Treeview(panel_der, columns=('num', 'contenido'), show='headings')
        self.lista_consejos.heading('num', text='#')
        self.lista_consejos.heading('contenido', text='Contenido')
        self.lista_consejos.column('num', width=50, anchor=tk.CENTER)
        self.lista_consejos.column('contenido', width=800)
        self.lista_consejos.pack(fill=tk.BOTH, expand=True, pady=5)
        self.lista_consejos.bind('<<TreeviewSelect>>', self.mostrar_consejo)
        
        # Editor de texto
        self.editor = tk.Text(panel_der, wrap=tk.WORD, font=('Arial', 12), padx=10, pady=10)
        self.editor.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Barra de herramientas
        toolbar = ttk.Frame(panel_der)
        toolbar.pack(fill=tk.X, pady=2)
        ttk.Button(toolbar, text="Guardar", command=self.guardar_consejo).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Exportar JSON", command=self.exportar_json).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Importar JSON", command=self.importar_json).pack(side=tk.LEFT, padx=2)
    
    def cargar_datos_base(self):
        # Datos de ejemplo
        self.consejos['Estudiantes'] = [
            "Usa la técnica Pomodoro (25 min estudio + 5 descanso)",
            "Crea mapas mentales para conceptos complejos"
        ]
    
    def actualizar_lista(self):
        self.lista_consejos.delete(*self.lista_consejos.get_children())
        categoria = self.categoria_actual()
        if categoria:
            for idx, consejo in enumerate(self.consejos[categoria], 1):
                self.lista_consejos.insert('', tk.END, values=(idx, consejo))
    
    def categoria_actual(self):
        seleccion = self.lista_categorias.selection()
        if seleccion:
            return self.lista_categorias.item(seleccion[0])['text']
        return None
    
    def cambiar_categoria(self, event=None):
        self.actualizar_lista()
        self.editor.delete('1.0', tk.END)
    
    def nuevo_consejo(self):
        categoria = self.categoria_actual()
        if categoria is None:
            messagebox.showerror("Error", "Selecciona una categoría primero")
            return
        
        self.consejos[categoria].append("Nuevo consejo - edita aquí")
        self.actualizar_lista()
    
    def eliminar_consejo(self):
        seleccion = self.lista_consejos.selection()
        if not seleccion:
            return
        
        categoria = self.categoria_actual()
        if categoria:
            index = self.lista_consejos.index(seleccion[0])
            del self.consejos[categoria][index]
            self.actualizar_lista()
    
    def mostrar_consejo(self, event=None):
        seleccion = self.lista_consejos.selection()
        if not seleccion:
            return
        
        categoria = self.categoria_actual()
        if categoria:
            index = self.lista_consejos.index(seleccion[0])
            self.editor.delete('1.0', tk.END)
            self.editor.insert('1.0', self.consejos[categoria][index])
    
    def guardar_consejo(self):
        seleccion = self.lista_consejos.selection()
        if not seleccion:
            return
        
        categoria = self.categoria_actual()
        if categoria:
            index = self.lista_consejos.index(seleccion[0])
            nuevo_texto = self.editor.get('1.0', tk.END).strip()
            self.consejos[categoria][index] = nuevo_texto
            self.actualizar_lista()
            messagebox.showinfo("Guardado", "Consejo actualizado correctamente")
    
    def exportar_json(self):
        archivo = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if archivo:
            try:
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(self.consejos, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("Éxito", f"Datos exportados a:\n{archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al exportar:\n{str(e)}")
    
    def importar_json(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    nuevos_datos = json.load(f)
                
                # Validar estructura
                if not all(cat in nuevos_datos for cat in self.categorias):
                    raise ValueError("Formato de archivo inválido")
                
                self.consejos = nuevos_datos
                self.actualizar_lista()
                messagebox.showinfo("Éxito", "Datos importados correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al importar:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsejosApp(root)
    root.mainloop()
