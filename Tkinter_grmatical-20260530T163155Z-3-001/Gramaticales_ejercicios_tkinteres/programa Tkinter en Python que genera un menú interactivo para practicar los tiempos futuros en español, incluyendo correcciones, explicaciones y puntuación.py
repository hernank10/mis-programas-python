import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import json

class AprendizajeFuturosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Tiempos Futuros")
        self.root.geometry("800x600")
        
        # Cargar datos de ejercicios
        self.cargar_ejercicios()
        
        # Variables de estado
        self.puntaje = 0
        self.total_preguntas = 0
        self.ejercicios_mostrados = []
        self.categoria_actual = ""
        
        # Configurar interfaz
        self.crear_interfaz()
    
    def cargar_ejercicios(self):
        try:
            with open("ejercicios.json", "r", encoding="utf-8") as f:
                self.ejercicios = json.load(f)
        except FileNotFoundError:
            self.ejercicios = {
                "Futuro simple": [],
                "Antefuturo": [],
                "Futuro perifrástico": []
            }
    
    def guardar_ejercicios(self):
        with open("ejercicios.json", "w", encoding="utf-8") as f:
            json.dump(self.ejercicios, f, ensure_ascii=False, indent=2)
    
    def crear_interfaz(self):
        # Marco principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(self.main_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)
        
        # Botones principales
        ttk.Button(self.main_frame, text="Nuevo Ejercicio", command=self.iniciar_ejercicio).pack(pady=5)
        ttk.Button(self.main_frame, text="Añadir Ejemplo", command=self.agregar_ejemplo).pack(pady=5)
        ttk.Button(self.main_frame, text="Ver Progreso", command=self.mostrar_progreso).pack(pady=5)
        ttk.Button(self.main_frame, text="Salir", command=self.root.quit).pack(pady=5)
        
        # Marco de ejercicio
        self.exercise_frame = ttk.Frame(self.root)
        
        # Componentes de ejercicio
        self.lbl_categoria = ttk.Label(self.exercise_frame, font=('Arial', 14))
        self.lbl_categoria.pack(pady=10)
        
        self.lbl_ejercicio = ttk.Label(self.exercise_frame, font=('Arial', 12))
        self.lbl_ejercicio.pack(pady=10)
        
        self.entrada_respuesta = ttk.Entry(self.exercise_frame, font=('Arial', 12))
        self.entrada_respuesta.pack(pady=10)
        
        self.btn_verificar = ttk.Button(self.exercise_frame, text="Verificar", command=self.verificar_respuesta)
        self.btn_verificar.pack(pady=5)
        
        self.lbl_resultado = ttk.Label(self.exercise_frame, font=('Arial', 12))
        self.lbl_resultado.pack(pady=10)
        
        self.lbl_explicacion = ttk.Label(self.exercise_frame, font=('Arial', 10), wraplength=600)
        self.lbl_explicacion.pack(pady=10)
        
        ttk.Button(self.exercise_frame, text="Volver al Menú", command=self.volver_menu).pack(pady=5)
    
    def actualizar_progreso(self):
        total_ejercicios = sum(len(cat) for cat in self.ejercicios.values())
        completados = min(self.total_preguntas, total_ejercicios)
        self.progress['value'] = (completados / total_ejercicios * 100) if total_ejercicios > 0 else 0
    
    def iniciar_ejercicio(self):
        categorias = [cat for cat in self.ejercicios if len(self.ejercicios[cat]) >= 10]
        if not categorias:
            messagebox.showinfo("Información", "Primero añade ejemplos en las categorías")
            return
        
        self.categoria_actual = random.choice(categorias)
        self.ejercicios_mostrados = random.sample(self.ejercicios[self.categoria_actual], 10)
        self.mostrar_siguiente_ejercicio()
        self.main_frame.pack_forget()
        self.exercise_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    
    def mostrar_siguiente_ejercicio(self):
        if not self.ejercicios_mostrados:
            self.volver_menu()
            return
        
        self.ejercicio_actual = self.ejercicios_mostrados.pop(0)
        self.lbl_categoria.config(text=f"Categoría: {self.categoria_actual}")
        self.lbl_ejercicio.config(text=self.ejercicio_actual['oracion'])
        self.entrada_respuesta.delete(0, tk.END)
        self.lbl_resultado.config(text="")
        self.lbl_explicacion.config(text="")
    
    def verificar_respuesta(self):
        respuesta = self.entrada_respuesta.get().strip().lower()
        correcta = self.ejercicio_actual['respuesta'].lower()
        
        self.total_preguntas += 1
        if respuesta == correcta:
            self.puntaje += 1
            self.lbl_resultado.config(text="¡Correcto! +1 punto", foreground="green")
        else:
            self.lbl_resultado.config(text=f"Incorrecto. Respuesta correcta: {correcta}", foreground="red")
        
        self.lbl_explicacion.config(text=f"Explicación: {self.ejercicio_actual['explicacion']}")
        self.actualizar_progreso()
        self.root.after(2000, self.mostrar_siguiente_ejercicio)
    
    def agregar_ejemplo(self):
        categoria = simpledialog.askstring("Categoría", "Ingrese la categoría (Futuro simple/Antefuturo/Futuro perifrástico):")
        if categoria and categoria in self.ejercicios:
            oracion = simpledialog.askstring("Oración", "Ingrese la oración incompleta (use ___ para el espacio en blanco):")
            respuesta = simpledialog.askstring("Respuesta", "Ingrese la respuesta correcta:")
            explicacion = simpledialog.askstring("Explicación", "Ingrese la explicación gramatical:")
            
            if all([oracion, respuesta, explicacion]):
                self.ejercicios[categoria].append({
                    "oracion": oracion,
                    "respuesta": respuesta,
                    "explicacion": explicacion
                })
                self.guardar_ejercicios()
                messagebox.showinfo("Éxito", "Ejemplo agregado correctamente")
            else:
                messagebox.showerror("Error", "Debes completar todos los campos")
    
    def mostrar_progreso(self):
        total = sum(len(cat) for cat in self.ejercicios.values())
        messagebox.showinfo("Progreso", 
            f"Puntaje total: {self.puntaje}\n"
            f"Ejercicios completados: {self.total_preguntas}\n"
            f"Progreso general: {self.progress['value']:.1f}%")
    
    def volver_menu(self):
        self.exercise_frame.pack_forget()
        self.main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = AprendizajeFuturosApp(root)
    root.mainloop()
