import json
import os
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class AumentativosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estudio de Aumentativos y Diminutivos")
        self.root.geometry("800x600")
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#F0F0F0')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', background='#F0F0F0', font=('Arial', 11))
        
        # Cargar datos
        self.ejemplos = self.cargar_datos('ejemplos.json')
        self.custom_ejemplos = self.cargar_datos('custom_ejemplos.json')
        self.historial = []
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.crear_menu_principal()
    
    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def guardar_datos(self, archivo, datos):
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
    
    def limpiar_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def crear_menu_principal(self):
        self.limpiar_frame()
        
        titulo = ttk.Label(self.main_frame, text="Estudio de Aumentativos y Diminutivos", 
                          font=('Arial', 16, 'bold'))
        titulo.pack(pady=20)
        
        btn_estilo = {'width': 25, 'pady': 10}
        
        ttk.Button(self.main_frame, text="Práctica con Ejemplos", 
                  command=self.practica_ejemplos).pack(**btn_estilo)
        ttk.Button(self.main_frame, text="Diapositiva Conceptual", 
                  command=self.mostrar_conceptos).pack(**btn_estilo)
        ttk.Button(self.main_frame, text="Cuestionario Interactivo", 
                  command=self.cuestionario).pack(**btn_estilo)
        ttk.Button(self.main_frame, text="Gestionar Ejemplos", 
                  command=self.gestion_ejemplos).pack(**btn_estilo)
        ttk.Button(self.main_frame, text="Salir", 
                  command=self.root.quit).pack(**btn_estilo)
    
    def practica_ejemplos(self):
        self.limpiar_frame()
        self.ejemplo_actual = 0
        self.todos_ejemplos = self.ejemplos + self.custom_ejemplos
        random.shuffle(self.todos_ejemplos)
        
        ttk.Button(self.main_frame, text="Regresar", command=self.crear_menu_principal).pack(anchor='nw', padx=10, pady=10)
        
        self.frame_practica = ttk.Frame(self.main_frame)
        self.frame_practica.pack(pady=20)
        
        self.mostrar_siguiente_ejemplo()
    
    def mostrar_siguiente_ejemplo(self):
        if self.ejemplo_actual >= len(self.todos_ejemplos[:50]):
            messagebox.showinfo("Completado", "¡Has completado todos los ejemplos!")
            self.crear_menu_principal()
            return
        
        ejemplo = self.todos_ejemplos[self.ejemplo_actual]
        
        for widget in self.frame_practica.winfo_children():
            widget.destroy()
        
        ttk.Label(self.frame_practica, text=f"Ejemplo {self.ejemplo_actual+1}/50", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        ttk.Label(self.frame_practica, text=f"Palabra base: {ejemplo['base']}").pack()
        ttk.Label(self.frame_practica, text=f"Forma modificada ({ejemplo['tipo'].upper()}):", 
                 font=('Arial', 11, 'bold')).pack(pady=5)
        ttk.Label(self.frame_practica, text=ejemplo['modificado'], 
                 font=('Arial', 12, 'italic')).pack()
        
        self.entry_oracion = ttk.Entry(self.frame_practica, width=50)
        self.entry_oracion.pack(pady=15)
        
        ttk.Button(self.frame_practica, text="Verificar Oración", 
                  command=lambda: self.verificar_oracion(ejemplo)).pack()
    
    def verificar_oracion(self, ejemplo):
        oracion = self.entry_oracion.get()
        if ejemplo['modificado'].lower() in oracion.lower():
            self.historial.append(f"{ejemplo['modificado']}: {oracion}")
            self.ejemplo_actual += 1
            self.mostrar_siguiente_ejemplo()
        else:
            messagebox.showerror("Error", f"La oración debe contener: {ejemplo['modificado']}")
    
    def mostrar_conceptos(self):
        self.limpiar_frame()
        ttk.Button(self.main_frame, text="Regresar", command=self.crear_menu_principal).pack(anchor='nw', padx=10, pady=10)
        
        frame_contenido = ttk.Frame(self.main_frame)
        frame_contenido.pack(pady=20, padx=20)
        
        conceptos = """
        AUMENTATIVOS:
        - Expresan aumento de tamaño/intensidad
        - Sufijos comunes: -azo, -ón, -ote
        - Ej: gigantazo (de gigante), señorón (de señor)
        
        DIMINUTIVOS:
        - Expresan pequeño tamaño o afecto
        - Sufijos comunes: -ito, -illo, -ico
        - Ej: florecilla (de flor), manecita (de mano)
        
        SUPERLATIVOS:
        - Expresan grado máximo (-ísimo/-ísima)
        - Ej: grandísimo, blanquísimo
        """
        
        ttk.Label(frame_contenido, text="Conceptos Clave", font=('Arial', 14, 'bold')).pack()
        ttk.Label(frame_contenido, text=conceptos.strip(), justify=tk.LEFT).pack(pady=10)
    
    def cuestionario(self):
        self.limpiar_frame()
        self.pregunta_actual = 0
        self.puntaje = 0
        self.todos_ejemplos = self.ejemplos + self.custom_ejemplos
        random.shuffle(self.todos_ejemplos)
        
        ttk.Button(self.main_frame, text="Regresar", command=self.crear_menu_principal).pack(anchor='nw', padx=10, pady=10)
        
        self.frame_cuestionario = ttk.Frame(self.main_frame)
        self.frame_cuestionario.pack(pady=20)
        
        self.mostrar_siguiente_pregunta()
    
    def mostrar_siguiente_pregunta(self):
        if self.pregunta_actual >= 10:
            self.mostrar_resultados()
            return
        
        ejemplo = self.todos_ejemplos[self.pregunta_actual]
        
        for widget in self.frame_cuestionario.winfo_children():
            widget.destroy()
        
        ttk.Label(self.frame_cuestionario, 
                 text=f"Pregunta {self.pregunta_actual+1}/10", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        ttk.Label(self.frame_cuestionario, 
                 text=f"¿Qué tipo de modificación es:\n{ejemplo['modificado']}?", 
                 font=('Arial', 11)).pack(pady=10)
        
        self.respuesta = tk.StringVar()
        
        opciones = [
            ('Aumentativo', 'aumentativo'),
            ('Diminutivo', 'diminutivo'),
            ('Superlativo', 'superlativo')
        ]
        
        for texto, valor in opciones:
            ttk.Radiobutton(self.frame_cuestionario, text=texto, 
                            variable=self.respuesta, value=valor).pack(anchor='w', padx=20)
        
        ttk.Button(self.frame_cuestionario, text="Continuar", 
                  command=lambda: self.verificar_respuesta(ejemplo)).pack(pady=15)
    
    def verificar_respuesta(self, ejemplo):
        if self.respuesta.get() == ejemplo['tipo']:
            self.puntaje += 1
        self.pregunta_actual += 1
        self.mostrar_siguiente_pregunta()
    
    def mostrar_resultados(self):
        for widget in self.frame_cuestionario.winfo_children():
            widget.destroy()
        
        porcentaje = (self.puntaje / 10) * 100
        ttk.Label(self.frame_cuestionario, 
                 text=f"Resultado Final: {self.puntaje}/10 ({porcentaje:.0f}%)", 
                 font=('Arial', 12, 'bold')).pack(pady=20)
        
        ttk.Button(self.frame_cuestionario, text="Volver al Menú", 
                  command=self.crear_menu_principal).pack()
    
    def gestion_ejemplos(self):
        self.limpiar_frame()
        ttk.Button(self.main_frame, text="Regresar", command=self.crear_menu_principal).pack(anchor='nw', padx=10, pady=10)
        
        frame_gestion = ttk.Frame(self.main_frame)
        frame_gestion.pack(pady=20)
        
        ttk.Button(frame_gestion, text="Crear Nuevo Ejemplo", 
                  command=self.crear_ejemplo).pack(pady=10)
        ttk.Button(frame_gestion, text="Ver Ejemplos Guardados", 
                  command=self.ver_ejemplos).pack(pady=10)
    
    def crear_ejemplo(self):
        if len(self.custom_ejemplos) >= 100:
            messagebox.showerror("Error", "Límite de 100 ejemplos alcanzado.")
            return
        
        dialogo = tk.Toplevel(self.root)
        dialogo.title("Nuevo Ejemplo")
        
        ttk.Label(dialogo, text="Palabra base:").grid(row=0, column=0, padx=5, pady=5)
        entry_base = ttk.Entry(dialogo)
        entry_base.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(dialogo, text="Forma modificada:").grid(row=1, column=0, padx=5, pady=5)
        entry_modificado = ttk.Entry(dialogo)
        entry_modificado.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(dialogo, text="Tipo:").grid(row=2, column=0, padx=5, pady=5)
        combo_tipo = ttk.Combobox(dialogo, values=['aumentativo', 'diminutivo'])
        combo_tipo.grid(row=2, column=1, padx=5, pady=5)
        
        def guardar():
            nuevo_ejemplo = {
                'base': entry_base.get(),
                'modificado': entry_modificado.get(),
                'tipo': combo_tipo.get()
            }
            self.custom_ejemplos.append(nuevo_ejemplo)
            self.guardar_datos('custom_ejemplos.json', self.custom_ejemplos)
            dialogo.destroy()
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        
        ttk.Button(dialogo, text="Guardar", command=guardar).grid(row=3, columnspan=2, pady=10)
    
    def ver_ejemplos(self):
        dialogo = tk.Toplevel(self.root)
        dialogo.title("Ejemplos Personalizados")
        
        scroll = ttk.Scrollbar(dialogo)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        lista = tk.Listbox(dialogo, width=60, height=15, yscrollcommand=scroll.set)
        lista.pack(padx=10, pady=10)
        
        for idx, ejemplo in enumerate(self.custom_ejemplos, 1):
            lista.insert(tk.END, f"{idx}. {ejemplo['base']} -> {ejemplo['modificado']} ({ejemplo['tipo']})")
        
        scroll.config(command=lista.yview)

if __name__ == "__main__":
    root = tk.Tk()
    app = AumentativosApp(root)
    root.mainloop()
