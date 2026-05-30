import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
from collections import defaultdict

class ConcordanciaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Practicador de Concordancia")
        self.root.geometry("800x600")
        
        # Datos iniciales
        self.categorias = {
            1: "Concordancia con múltiples sustantivos",
            2: "Género/número en adjetivos",
            3: "Verbos con sujetos compuestos",
            4: "Excepciones y anomalías"
        }
        
        self.ejemplos = self.cargar_ejemplos()
        self.progreso = defaultdict(int)
        self.total_ejemplos = 0
        self.ejemplo_actual = None
        self.categoria_actual = None
        
        # Configurar interfaz
        self.crear_menu_principal()
    
    def cargar_ejemplos(self):
        return {
            1: [
                {"incorrecto": "Las valientes madre e hija", "correcto": "Los valientes madre e hija"},
                {"incorrecto": "Las talentosas Pedro y Luis", "correcto": "Los talentosos Pedro y Luis"}
            ],
            2: [
                {"incorrecto": "Talento y habilidad extremada", "correcto": "Talento y habilidad extremados"},
                {"incorrecto": "Talentos y habilidades raras", "correcto": "Talentos y habilidades raros"}
            ],
            3: [
                {"incorrecto": "Se alababa su honestidad y generosidad", "correcto": "Se alababan su honestidad y generosidad"},
                {"incorrecto": "¿Qué se ha hecho de aquel entusiasmo?", "correcto": "¿Qué se han hecho de aquel entusiasmo?"}
            ],
            4: [
                {"incorrecto": "Media Valencia fue inundada", "correcto": "Medio Valencia fue inundado"},
                {"incorrecto": "Una Barcelona moderna", "correcto": "Un Barcelona moderno"}
            ]
        }
    
    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        title = ttk.Label(self.root, text="¡Practica Concordancia Gramatical!", font=("Arial", 20))
        title.pack(pady=20)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=30)
        
        for cat_id, cat_nombre in self.categorias.items():
            btn = ttk.Button(
                btn_frame,
                text=f"Categoría {cat_id}\n{cat_nombre}",
                command=lambda c=cat_id: self.iniciar_categoria(c),
                width=30
            )
            btn.pack(pady=10)
        
        ttk.Button(self.root, text="Ver Progreso", command=self.mostrar_progreso).pack(pady=10)
        ttk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)
    
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def mostrar_reglas(self, categoria):
        reglas = {
            1: "REGLA 1: Con nombres propios o de persona, el masculino precede y el adjetivo va en masculino plural.",
            2: "REGLA 2: Con varios sustantivos, el adjetivo concuerda con el más cercano o en masculino plural.",
            3: "REGLA 3: Verbos después de sujetos compuestos deben ir en plural.",
            4: "REGLA 4: Ciudades femeninas usan artículo masculino con 'un' o 'medio'."
        }
        messagebox.showinfo("Regla Gramatical", reglas[categoria])
    
    def iniciar_categoria(self, categoria):
        self.categoria_actual = categoria
        self.mostrar_reglas(categoria)
        self.mostrar_ejercicio()
    
    def mostrar_ejercicio(self):
        self.limpiar_pantalla()
        
        # Obtener ejemplo
        if not self.ejemplos[self.categoria_actual]:
            self.agregar_nuevo_ejemplo()
            return
            
        self.ejemplo_actual = random.choice(self.ejemplos[self.categoria_actual])
        
        # Interfaz ejercicio
        ttk.Label(self.root, text="Corrige la siguiente frase:", font=("Arial", 14)).pack(pady=20)
        
        ttk.Label(self.root, 
                text=f"INCORRECTO:\n{self.ejemplo_actual['incorrecto']}", 
                font=("Arial", 12, "bold"),
                foreground="red").pack(pady=10)
        
        self.respuesta_entry = ttk.Entry(self.root, width=60, font=("Arial", 12))
        self.respuesta_entry.pack(pady=20)
        
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Comprobar", command=self.verificar_respuesta).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Saltar", command=self.mostrar_ejercicio).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Menú Principal", command=self.crear_menu_principal).pack(side=tk.LEFT, padx=5)
    
    def verificar_respuesta(self):
        respuesta = self.respuesta_entry.get().strip()
        
        if respuesta == self.ejemplo_actual['correcto']:
            messagebox.showinfo("Resultado", "¡Correcto! ✅")
            self.progreso[self.categoria_actual] += 1
            self.total_ejemplos += 1
            self.ejemplos[self.categoria_actual].remove(self.ejemplo_actual)
        else:
            messagebox.showerror("Resultado", 
                                f"Mejor opción: ❌\nCORRECTO: {self.ejemplo_actual['correcto']}")
        
        if self.total_ejemplos >= 100:
            messagebox.showinfo("¡Felicidades!", "Has completado 100 ejercicios 🎉")
            self.root.quit()
        else:
            self.mostrar_ejercicio()
    
    def agregar_nuevo_ejemplo(self):
        nuevo_ej = simpledialog.askstring("Nuevo Ejemplo", 
                                         "Formato: Incorrecto|Correcto\nEj: Las casa grandes|Las casas grandes")
        if nuevo_ej and '|' in nuevo_ej:
            incorrecto, correcto = nuevo_ej.split('|', 1)
            self.ejemplos[self.categoria_actual].append({
                "incorrecto": incorrecto.strip(),
                "correcto": correcto.strip()
            })
            messagebox.showinfo("Éxito", "¡Ejemplo agregado correctamente!")
            self.mostrar_ejercicio()
    
    def mostrar_progreso(self):
        progreso_texto = "PROGRESO:\n\n"
        for cat_id, cat_nombre in self.categorias.items():
            progreso_texto += f"{cat_nombre}: {self.progreso[cat_id]} ejercicios\n"
        
        progreso_texto += f"\nTOTAL: {self.total_ejemplos}/100"
        messagebox.showinfo("Progreso", progreso_texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcordanciaApp(root)
    root.mainloop()
