import tkinter as tk
from tkinter import ttk, messagebox
import json
import random

class AplicacionSubordinadas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprendizaje de Subordinadas Sustantivas")
        self.geometry("800x600")
        self.config(bg="#f0f0f0")
        
        # Cargar datos
        self.ejemplos_base = self.cargar_ejemplos_base()
        self.user_ejemplos = self.cargar_ejemplos_usuario()
        self.categorias = list(self.ejemplos_base.keys())
        
        # Variables de estado
        self.puntaje = 0
        self.intentos = 0
        self.slide_index = 0
        self.auto_play = False
        
        # Crear interfaz
        self.crear_menu()
        self.crear_frames()
        self.mostrar_frame("inicio")
        
    def crear_menu(self):
        menubar = tk.Menu(self)
        
        # Menú principal
        menu_principal = tk.Menu(menubar, tearoff=0)
        menu_principal.add_command(label="Práctica", command=lambda: self.mostrar_frame("practica"))
        menu_principal.add_command(label="Crear Ejemplo", command=lambda: self.mostrar_frame("crear"))
        menu_principal.add_command(label="Ver Ejemplos", command=lambda: self.mostrar_frame("ver"))
        menu_principal.add_command(label="Diapositivas", command=lambda: self.iniciar_diapositivas())
        menu_principal.add_separator()
        menu_principal.add_command(label="Salir", command=self.quit)
        
        menubar.add_cascade(label="Menú", menu=menu_principal)
        self.config(menu=menubar)
    
    def crear_frames(self):
        # Frame de inicio
        self.frame_inicio = ttk.Frame(self)
        lbl_titulo = ttk.Label(self.frame_inicio, text="Aprendizaje de Subordinadas Sustantivas", 
                             font=("Arial", 16, "bold"))
        lbl_instrucciones = ttk.Label(self.frame_inicio, text="Selecciona una opción del menú superior para comenzar",
                                    wraplength=400)
        lbl_titulo.pack(pady=50)
        lbl_instrucciones.pack(pady=20)
        
        # Frame de práctica
        self.frame_practica = ttk.Frame(self)
        self.lbl_ejemplo = ttk.Label(self.frame_practica, font=("Arial", 12), wraplength=600)
        self.lbl_resultado = ttk.Label(self.frame_practica, font=("Arial", 12))
        self.crear_botones_categorias()
        self.lbl_puntaje = ttk.Label(self.frame_practica, text="Puntaje: 0/0")
        
        self.lbl_ejemplo.pack(pady=20)
        self.lbl_resultado.pack(pady=10)
        self.lbl_puntaje.pack(pady=10)
        
        # Frame de creación
        self.frame_crear = ttk.Frame(self)
        self.combo_categoria = ttk.Combobox(self.frame_crear, values=self.categorias)
        self.txt_ejemplo = tk.Text(self.frame_crear, height=4, width=50)
        btn_guardar = ttk.Button(self.frame_crear, text="Guardar Ejemplo", command=self.guardar_ejemplo)
        
        ttk.Label(self.frame_crear, text="Categoría:").pack(pady=5)
        self.combo_categoria.pack(pady=5)
        ttk.Label(self.frame_crear, text="Ejemplo:").pack(pady=5)
        self.txt_ejemplo.pack(pady=5)
        btn_guardar.pack(pady=10)
        
        # Frame de visualización
        self.frame_ver = ttk.Frame(self)
        self.tree = ttk.Treeview(self.frame_ver, columns=("Categoría", "Ejemplo"), show="headings")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Ejemplo", text="Ejemplo")
        self.tree.column("Categoría", width=150)
        self.tree.column("Ejemplo", width=500)
        scroll = ttk.Scrollbar(self.frame_ver, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        
        # Frame de diapositivas
        self.frame_diapositivas = ttk.Frame(self)
        self.lbl_diapo = ttk.Label(self.frame_diapositivas, font=("Arial", 14), wraplength=600)
        self.lbl_categoria = ttk.Label(self.frame_diapositivas, font=("Arial", 12, "bold"))
        btn_controles = ttk.Frame(self.frame_diapositivas)
        self.btn_auto = ttk.Button(btn_controles, text="Auto Play", command=self.toggle_auto_play)
        btn_anterior = ttk.Button(btn_controles, text="< Anterior", command=lambda: self.cambiar_diapositiva(-1))
        btn_siguiente = ttk.Button(btn_controles, text="Siguiente >", command=lambda: self.cambiar_diapositiva(1))
        
        self.lbl_diapo.pack(pady=30)
        self.lbl_categoria.pack(pady=10)
        btn_controles.pack(pady=20)
        btn_anterior.pack(side="left", padx=10)
        self.btn_auto.pack(side="left", padx=10)
        btn_siguiente.pack(side="left", padx=10)
        
    def crear_botones_categorias(self):
        frame_botones = ttk.Frame(self.frame_practica)
        for i, cat in enumerate(self.categorias, 1):
            btn = ttk.Button(frame_botones, text=f"{i}. {cat}", 
                           command=lambda c=cat: self.verificar_respuesta(c))
            btn.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)
        frame_botones.pack(pady=20)
        
    def mostrar_frame(self, nombre_frame):
        frames = {
            "inicio": self.frame_inicio,
            "practica": self.frame_practica,
            "crear": self.frame_crear,
            "ver": self.frame_ver
        }
        for frame in frames.values():
            frame.pack_forget()
        frames[nombre_frame].pack(fill="both", expand=True)
        
        if nombre_frame == "practica":
            self.nuevo_ejemplo()
        elif nombre_frame == "ver":
            self.actualizar_arbol()
            
    def cargar_ejemplos_base(self):
        return {
            "Sujeto": ["Que llueva es una bendición...", "Que estudies medicina..."],
            "Complemento Directo": ["Quiero que me escuches...", "Ella cree que..."],
            "Complemento Indirecto": ["Le dije que...", "Le pregunté si..."],
            "Complemento Circunstancial": ["Llegamos antes de que...", "Saldré después de que..."],
            "Complemento Preposicional": ["La idea de que...", "Estoy seguro de que..."]
        }
        
    def cargar_ejemplos_usuario(self):
        try:
            with open("user_ejemplos.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {k: [] for k in self.categorias}
            
    def guardar_ejemplos_usuario(self):
        with open("user_ejemplos.json", "w") as f:
            json.dump(self.user_ejemplos, f, indent=2)
            
    def nuevo_ejemplo(self):
        todas_categorias = {**self.ejemplos_base, **self.user_ejemplos}
        categorias_validas = [k for k, v in todas_categorias.items() if v]
        if not categorias_validas:
            messagebox.showwarning("Error", "No hay ejemplos disponibles")
            return
            
        self.categoria_actual = random.choice(categorias_validas)
        ejemplos = todas_categorias[self.categoria_actual]
        self.ejemplo_actual = random.choice(ejemplos)
        self.lbl_ejemplo.config(text=self.ejemplo_actual)
        self.lbl_resultado.config(text="")
        
    def verificar_respuesta(self, categoria_seleccionada):
        self.intentos += 1
        if categoria_seleccionada == self.categoria_actual:
            self.puntaje += 1
            resultado = "¡Correcto! ✅"
        else:
            resultado = f"❌ Incorrecto. Categoría correcta: {self.categoria_actual}"
            
        self.lbl_resultado.config(text=resultado)
        self.lbl_puntaje.config(text=f"Puntaje: {self.puntaje}/{self.intentos}")
        self.after(1500, self.nuevo_ejemplo)
        
    def guardar_ejemplo(self):
        categoria = self.combo_categoria.get()
        ejemplo = self.txt_ejemplo.get("1.0", "end").strip()
        
        if not categoria or not ejemplo:
            messagebox.showwarning("Error", "Completa todos los campos")
            return
            
        if categoria not in self.user_ejemplos:
            self.user_ejemplos[categoria] = []
            
        self.user_ejemplos[categoria].append(ejemplo)
        self.guardar_ejemplos_usuario()
        messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        self.txt_ejemplo.delete("1.0", "end")
        
    def actualizar_arbol(self):
        self.tree.delete(*self.tree.get_children())
        for categoria, ejemplos in self.user_ejemplos.items():
            for ejemplo in ejemplos:
                self.tree.insert("", "end", values=(categoria, ejemplo))
                
    def iniciar_diapositivas(self):
        self.mostrar_frame("inicio")
        self.frame_diapositivas.pack(fill="both", expand=True)
        self.slide_index = 0
        self.cambiar_diapositiva(0)
        
    def cambiar_diapositiva(self, direccion):
        todos_ejemplos = []
        for cat, ejemplos in {**self.ejemplos_base, **self.user_ejemplos}.items():
            for ej in ejemplos:
                todos_ejemplos.append((cat, ej))
                
        if not todos_ejemplos:
            messagebox.showwarning("Error", "No hay ejemplos para mostrar")
            return
            
        self.slide_index = (self.slide_index + direccion) % len(todos_ejemplos)
        cat, ej = todos_ejemplos[self.slide_index]
        self.lbl_diapo.config(text=ej)
        self.lbl_categoria.config(text=f"Categoría: {cat}")
        
        if self.auto_play:
            self.after(3000, lambda: self.cambiar_diapositiva(1))
            
    def toggle_auto_play(self):
        self.auto_play = not self.auto_play
        self.btn_auto.config(text="Detener" if self.auto_play else "Auto Play")
        if self.auto_play:
            self.cambiar_diapositiva(1)

if __name__ == "__main__":
    app = AplicacionSubordinadas()
    app.mainloop()
