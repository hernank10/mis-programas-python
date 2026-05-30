import json
import os
import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class DerivadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estudio de Derivados Verbales")
        self.root.geometry("800x600")
        
        # Archivos de datos
        self.ejemplos_file = "ejemplos.json"
        self.usuario_file = "usuario_ejemplos.json"
        
        # Cargar datos
        self.ejemplos = self.cargar_ejemplos()
        self.ejemplos_usuario = self.cargar_usuario()
        
        # Interfaz principal
        self.crear_menu_principal()
        self.crear_diapositiva_conceptual()
    
    def cargar_ejemplos(self):
        if os.path.exists(self.ejemplos_file):
            with open(self.ejemplos_file, 'r') as f:
                return json.load(f)
        return []
    
    def cargar_usuario(self):
        if os.path.exists(self.usuario_file):
            with open(self.usuario_file, 'r') as f:
                return json.load(f)
        return []
    
    def guardar_ejemplo(self, ejemplo):
        if len(self.ejemplos_usuario) < 100:
            self.ejemplos_usuario.append(ejemplo)
            with open(self.usuario_file, 'w') as f:
                json.dump(self.ejemplos_usuario, f)
            return True
        return False
    
    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        titulo = ttk.Label(self.root, text="ESTUDIO DE DERIVADOS VERBALES", font=('Arial', 16, 'bold'))
        titulo.pack(pady=20)
        
        marco_botones = ttk.Frame(self.root)
        marco_botones.pack(pady=10)
        
        botones = [
            ("Modo Estudio", self.modo_estudio),
            ("Cuestionario", self.cuestionario),
            ("Crear Ejemplos", self.crear_ejemplos),
            ("Ver Ejemplos", self.ver_ejemplos),
            ("Ayuda Conceptual", self.mostrar_ayuda),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones:
            boton = ttk.Button(marco_botones, text=texto, command=comando, width=20)
            boton.pack(pady=5, padx=10)
    
    def crear_diapositiva_conceptual(self):
        self.ventana_ayuda = tk.Toplevel(self.root)
        self.ventana_ayuda.withdraw()
        
        texto = """CONCEPTOS CLAVE:

Infinitivo: 
- Termina en -ar, -er, -ir
- Funciona como sustantivo
- Ejemplo: 'Estudiar es importante'

Participio:
- Termina en -ado/-ido
- Con 'ser/estar' (adjetivo): 'La puerta está cerrada'
- Con 'haber' (invariable): 'He terminado'

Gerundio:
- Termina en -ando/-iendo
- Modifica al verbo principal
- Ejemplo: 'Caminando rápido'"""
        
        self.texto_ayuda = scrolledtext.ScrolledText(self.ventana_ayuda, wrap=tk.WORD, width=60, height=15)
        self.texto_ayuda.insert(tk.INSERT, texto)
        self.texto_ayuda.config(state=tk.DISABLED)
        self.texto_ayuda.pack(padx=20, pady=20)
    
    def modo_estudio(self):
        self.limpiar_pantalla()
        self.indice_actual = 0
        self.todos_ejemplos = self.ejemplos + self.ejemplos_usuario
        
        marco_principal = ttk.Frame(self.root)
        marco_principal.pack(fill=tk.BOTH, expand=True)
        
        # Controles de navegación
        marco_navegacion = ttk.Frame(marco_principal)
        marco_navegacion.pack(pady=10)
        
        self.etiqueta_progreso = ttk.Label(marco_navegacion, text=f"Ejemplo 1/{len(self.todos_ejemplos)}")
        self.etiqueta_progreso.pack(side=tk.LEFT, padx=10)
        
        boton_anterior = ttk.Button(marco_navegacion, text="Anterior", command=self.anterior_ejemplo)
        boton_anterior.pack(side=tk.LEFT, padx=5)
        
        boton_siguiente = ttk.Button(marco_navegacion, text="Siguiente", command=self.siguiente_ejemplo)
        boton_siguiente.pack(side=tk.LEFT, padx=5)
        
        # Contenido
        marco_contenido = ttk.Frame(marco_principal)
        marco_contenido.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.etiqueta_ejemplo = ttk.Label(marco_contenido, text="", font=('Arial', 12))
        self.etiqueta_ejemplo.pack(pady=10)
        
        ttk.Label(marco_contenido, text="Categoría:").pack()
        self.entrada_categoria = ttk.Entry(marco_contenido, width=20)
        self.entrada_categoria.pack(pady=5)
        
        ttk.Label(marco_contenido, text="Escribe una oración:").pack()
        self.entrada_oracion = ttk.Entry(marco_contenido, width=50)
        self.entrada_oracion.pack(pady=5)
        
        self.etiqueta_feedback = ttk.Label(marco_contenido, text="")
        self.etiqueta_feedback.pack(pady=5)
        
        self.mostrar_ejemplo_actual()
    
    def mostrar_ejemplo_actual(self):
        if self.indice_actual < len(self.todos_ejemplos):
            ejemplo = self.todos_ejemplos[self.indice_actual]
            self.etiqueta_progreso.config(text=f"Ejemplo {self.indice_actual + 1}/{len(self.todos_ejemplos)}")
            self.etiqueta_ejemplo.config(text=ejemplo['ejemplo'])
            self.entrada_categoria.delete(0, tk.END)
            self.entrada_oracion.delete(0, tk.END)
            self.etiqueta_feedback.config(text="")
        else:
            messagebox.showinfo("Fin", "¡Has completado todos los ejemplos!")
            self.crear_menu_principal()
    
    def anterior_ejemplo(self):
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_ejemplo_actual()
    
    def siguiente_ejemplo(self):
        if self.indice_actual < len(self.todos_ejemplos) - 1:
            self.indice_actual += 1
            self.mostrar_ejemplo_actual()
        else:
            messagebox.showinfo("Fin", "¡Has completado todos los ejemplos!")
            self.crear_menu_principal()
    
    def cuestionario(self):
        self.limpiar_pantalla()
        self.puntaje = 0
        self.preguntas = random.sample(self.ejemplos + self.ejemplos_usuario, 
                                     min(10, len(self.ejemplos + self.ejemplos_usuario)))
        self.pregunta_actual = 0
        
        marco_principal = ttk.Frame(self.root)
        marco_principal.pack(fill=tk.BOTH, expand=True)
        
        self.etiqueta_pregunta = ttk.Label(marco_principal, text="", font=('Arial', 12))
        self.etiqueta_pregunta.pack(pady=20)
        
        ttk.Label(marco_principal, text="Introduce la categoría:").pack()
        self.entrada_respuesta = ttk.Entry(marco_principal)
        self.entrada_respuesta.pack(pady=10)
        
        boton_verificar = ttk.Button(marco_principal, text="Verificar", command=self.verificar_respuesta)
        boton_verificar.pack(pady=10)
        
        self.etiqueta_resultado = ttk.Label(marco_principal, text="")
        self.etiqueta_resultado.pack(pady=10)
        
        self.mostrar_siguiente_pregunta()
    
    def mostrar_siguiente_pregunta(self):
        if self.pregunta_actual < len(self.preguntas):
            pregunta = self.preguntas[self.pregunta_actual]
            self.etiqueta_pregunta.config(text=pregunta['ejemplo'])
            self.entrada_respuesta.delete(0, tk.END)
            self.etiqueta_resultado.config(text="")
        else:
            messagebox.showinfo("Resultado", f"Puntaje final: {self.puntaje}/{len(self.preguntas)}")
            self.crear_menu_principal()
    
    def verificar_respuesta(self):
        respuesta = self.entrada_respuesta.get().lower()
        if self.pregunta_actual < len(self.preguntas):
            correcta = self.preguntas[self.pregunta_actual]['categoria']
            if respuesta == correcta:
                self.puntaje += 1
                self.etiqueta_resultado.config(text="✅ Correcto!", foreground='green')
            else:
                self.etiqueta_resultado.config(text=f"❌ Incorrecto. Correcto: {correcta}", foreground='red')
            self.pregunta_actual += 1
            self.root.after(1500, self.mostrar_siguiente_pregunta)
    
    def crear_ejemplos(self):
        self.ventana_crear = tk.Toplevel(self.root)
        self.ventana_crear.title("Crear Nuevos Ejemplos")
        
        ttk.Label(self.ventana_crear, text="Ejemplo:").pack(pady=5)
        self.entrada_nuevo = ttk.Entry(self.ventana_crear, width=40)
        self.entrada_nuevo.pack(pady=5)
        
        self.etiqueta_categoria = ttk.Label(self.ventana_crear, text="Categoría detectada: ")
        self.etiqueta_categoria.pack(pady=5)
        
        ttk.Button(self.ventana_crear, text="Guardar", command=self.guardar_nuevo).pack(pady=10)
        ttk.Button(self.ventana_crear, text="Cerrar", command=self.ventana_crear.destroy).pack(pady=5)
        
        self.entrada_nuevo.bind("<KeyRelease>", self.actualizar_categoria)
    
    def actualizar_categoria(self, event):
        texto = self.entrada_nuevo.get().lower()
        categoria = ""
        
        if texto.endswith(('ar', 'er', 'ir')):
            categoria = 'infinitivo'
        elif texto.endswith(('ado', 'ada', 'idos', 'idas', 'ido', 'ida')):
            categoria = 'participio'
        elif texto.endswith(('ando', 'endo')):
            categoria = 'gerundio'
        
        self.etiqueta_categoria.config(text=f"Categoría detectada: {categoria.capitalize() if categoria else 'No válida'}")
    
    def guardar_nuevo(self):
        ejemplo = self.entrada_nuevo.get().strip()
        categoria = self.etiqueta_categoria.cget("text").split(": ")[1].lower()
        
        if categoria not in ['infinitivo', 'participio', 'gerundio']:
            messagebox.showerror("Error", "Formato no válido. Revise las terminaciones.")
            return
            
        if len(ejemplo) < 3:
            messagebox.showerror("Error", "El ejemplo debe tener al menos 3 caracteres")
            return
            
        if self.guardar_ejemplo({'categoria': categoria, 'ejemplo': ejemplo}):
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
            self.entrada_nuevo.delete(0, tk.END)
            self.etiqueta_categoria.config(text="Categoría detectada: ")
        else:
            messagebox.showerror("Error", "Límite de 100 ejemplos alcanzado")
    
    def ver_ejemplos(self):
        self.ventana_lista = tk.Toplevel(self.root)
        self.ventana_lista.title("Ejemplos Guardados")
        
        contenedor = ttk.Frame(self.ventana_lista)
        contenedor.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(contenedor)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lista = tk.Listbox(contenedor, yscrollcommand=scrollbar.set, width=80)
        self.lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista.yview)
        
        for idx, item in enumerate(self.ejemplos + self.ejemplos_usuario, 1):
            self.lista.insert(tk.END, f"{idx}. [{item['categoria'].upper()}] {item['ejemplo']}")
    
    def mostrar_ayuda(self):
        self.ventana_ayuda.deiconify()
    
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DerivadosApp(root)
    root.mainloop()
