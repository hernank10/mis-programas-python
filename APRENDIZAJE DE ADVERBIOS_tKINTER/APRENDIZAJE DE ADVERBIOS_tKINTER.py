import json
import os
import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class AdverbiosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Adverbios")
        self.root.geometry("800x600")
        
        # Cargar datos
        self.categorias = self.cargar_categorias()
        self.ejemplos = self.cargar_ejemplos()
        self.ejemplos_usuario = self.cargar_ejemplos_usuario()
        
        # Estilos
        self.estilo = ttk.Style()
        self.estilo.configure('Titulo.TLabel', font=('Arial', 16, 'bold'), foreground='navy')
        self.estilo.configure('Boton.TButton', font=('Arial', 10), padding=10)
        
        self.crear_menu_principal()

    def cargar_categorias(self):
        return {
            "lugar": ["cerca", "arriba", "dentro", "debajo", "mar afuera"],
            # ... completar con todas las categorías
        }

    def cargar_ejemplos(self):
        return [
            {"categoria": "lugar", "ejemplo": "El parque está cerca de mi casa"},
            # ... completar con todos los ejemplos
        ]

    def cargar_ejemplos_usuario(self):
        if os.path.exists("ejemplos_usuario.json"):
            with open("ejemplos_usuario.json", "r") as f:
                return json.load(f)
        return []

    def guardar_ejemplo_usuario(self, ejemplo):
        if len(self.ejemplos_usuario) < 100:
            self.ejemplos_usuario.append(ejemplo)
            with open("ejemplos_usuario.json", "w") as f:
                json.dump(self.ejemplos_usuario, f)
            return True
        return False

    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        marco = ttk.Frame(self.root)
        marco.pack(pady=50, expand=True)
        
        ttk.Label(marco, text="APRENDIZAJE DE ADVERBIOS", style='Titulo.TLabel').pack(pady=20)
        
        botones = [
            ("Diapositiva Conceptual", self.mostrar_diapositiva),
            ("Práctica Guiada", self.iniciar_practica),
            ("Cuestionario Interactivo", self.iniciar_cuestionario),
            ("Gestionar Ejemplos", self.gestionar_ejemplos),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones:
            ttk.Button(marco, text=texto, command=comando, style='Boton.TButton').pack(fill='x', pady=5)

    def mostrar_diapositiva(self):
        self.limpiar_pantalla()
        
        marco = ttk.Frame(self.root)
        marco.pack(pady=20, padx=20, fill='both', expand=True)
        
        texto = scrolledtext.ScrolledText(marco, wrap=tk.WORD, font=('Arial', 12))
        texto.pack(fill='both', expand=True)
        
        contenido = """ADVERBIOS - CLASIFICACIÓN CONCEPTUAL

1. Lugar: Indican ubicación espacial (ej: cerca, arriba)
2. Tiempo: Señalan momento temporal (ej: antes, nunca)
3. Modo: Describen forma de acción (ej: dulcemente, mal)
4. Cantidad: Expresan grado o medida (ej: mucho, casi)
5. Afirmación/Negación: Confirmación o negación (ej: sí, jamás)
6. Demostrativos: Señalan referentes contextuales (ej: aquí, ahora)
7. Relativos: Conectan proposiciones (ej: donde, cuando)
8. Interrogativos: Formulan preguntas (ej: dónde, cómo)
9. Especiales: Casos únicos o compuestos (ej: recién, cerquita)"""
        
        texto.insert(tk.INSERT, contenido)
        texto.configure(state='disabled')
        
        ttk.Button(marco, text="Regresar", command=self.crear_menu_principal).pack(pady=10)

    def iniciar_practica(self):
        self.limpiar_pantalla()
        self.indice_practica = 0
        self.mostrar_ejercicio_practica()

    def mostrar_ejercicio_practica(self):
        if self.indice_practica >= len(self.ejemplos):
            self.crear_menu_principal()
            return
        
        ejercicio = self.ejemplos[self.indice_practica]
        self.limpiar_pantalla()
        
        marco = ttk.Frame(self.root)
        marco.pack(pady=20, padx=20, fill='both', expand=True)
        
        ttk.Label(marco, text=f"Ejemplo {self.indice_practica + 1}/{len(self.ejemplos)}", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        ttk.Label(marco, text=ejercicio['ejemplo'], wraplength=600, 
                 font=('Arial', 12)).pack(pady=10)
        
        ttk.Label(marco, text="Selecciona la categoría correcta:", 
                 font=('Arial', 11)).pack(pady=5)
        
        self.combo_categoria = ttk.Combobox(marco, values=list(self.categorias.keys()))
        self.combo_categoria.pack(pady=5)
        
        ttk.Label(marco, text="Escribe tu propia oración:", 
                 font=('Arial', 11)).pack(pady=5)
        
        self.entrada_oracion = ttk.Entry(marco, width=60)
        self.entrada_oracion.pack(pady=5)
        
        marco_botones = ttk.Frame(marco)
        marco_botones.pack(pady=10)
        
        ttk.Button(marco_botones, text="Comprobar", 
                  command=lambda: self.verificar_respuesta(ejercicio)).pack(side='left', padx=5)
        ttk.Button(marco_botones, text="Siguiente", 
                  command=self.siguiente_ejercicio).pack(side='left', padx=5)

    def verificar_respuesta(self, ejercicio):
        categoria_usuario = self.combo_categoria.get()
        oracion_usuario = self.entrada_oracion.get()
        
        if categoria_usuario.lower() == ejercicio['categoria']:
            messagebox.showinfo("Resultado", "¡Correcto! ✅")
        else:
            messagebox.showerror("Resultado", 
                f"❌ Incorrecto. Categoría correcta: {ejercicio['categoria']}")
        
        if oracion_usuario:
            messagebox.showinfo("Oración Guardada", "Tu oración ha sido registrada")

    def siguiente_ejercicio(self):
        self.indice_practica += 1
        self.mostrar_ejercicio_practica()

    def iniciar_cuestionario(self):
        self.puntaje = 0
        self.preguntas = random.sample(self.ejemplos + self.ejemplos_usuario, 10)
        self.indice_pregunta = 0
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.indice_pregunta >= len(self.preguntas):
            self.mostrar_resultados()
            return
        
        self.limpiar_pantalla()
        pregunta = self.preguntas[self.indice_pregunta]
        
        marco = ttk.Frame(self.root)
        marco.pack(pady=20, padx=20, fill='both', expand=True)
        
        ttk.Label(marco, text=f"Pregunta {self.indice_pregunta + 1}/10", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        ttk.Label(marco, text=pregunta['ejemplo'], wraplength=600, 
                 font=('Arial', 12)).pack(pady=10)
        
        ttk.Label(marco, text="Selecciona la categoría:", 
                 font=('Arial', 11)).pack(pady=5)
        
        self.combo_respuesta = ttk.Combobox(marco, values=list(self.categorias.keys()))
        self.combo_respuesta.pack(pady=5)
        
        ttk.Button(marco, text="Responder", 
                  command=lambda: self.verificar_respuesta_cuestionario(pregunta)).pack(pady=10)

    def verificar_respuesta_cuestionario(self, pregunta):
        respuesta = self.combo_respuesta.get().lower()
        if respuesta == pregunta['categoria']:
            self.puntaje += 10
            messagebox.showinfo("Correcto", "¡Respuesta correcta! +10 puntos 🎉")
        else:
            messagebox.showerror("Incorrecto", 
                f"Respuesta incorrecta. La categoría correcta es: {pregunta['categoria']}")
        
        self.indice_pregunta += 1
        self.mostrar_pregunta()

    def mostrar_resultados(self):
        self.limpiar_pantalla()
        
        marco = ttk.Frame(self.root)
        marco.pack(pady=50, expand=True)
        
        resultado = f"Puntuación Final: {self.puntaje}/100\n"
        if self.puntaje >= 70:
            resultado += "¡Excelente dominio! 🌟"
        else:
            resultado += "Sigue practicando 💪"
        
        ttk.Label(marco, text=resultado, font=('Arial', 14)).pack(pady=20)
        ttk.Button(marco, text="Volver al Menú", command=self.crear_menu_principal).pack(pady=10)

    def gestionar_ejemplos(self):
        self.limpiar_pantalla()
        
        marco = ttk.Frame(self.root)
        marco.pack(pady=20, padx=20, fill='both', expand=True)
        
        ttk.Label(marco, text="GESTIONAR EJEMPLOS", font=('Arial', 14, 'bold')).pack(pady=10)
        
        ttk.Label(marco, text="Categoría:", font=('Arial', 11)).pack()
        self.entrada_categoria = ttk.Entry(marco, width=30)
        self.entrada_categoria.pack(pady=5)
        
        ttk.Label(marco, text="Oración completa:", font=('Arial', 11)).pack()
        self.entrada_ejemplo = ttk.Entry(marco, width=60)
        self.entrada_ejemplo.pack(pady=5)
        
        marco_botones = ttk.Frame(marco)
        marco_botones.pack(pady=10)
        
        ttk.Button(marco_botones, text="Guardar Ejemplo", command=self.guardar_nuevo_ejemplo).pack(side='left', padx=5)
        ttk.Button(marco_botones, text="Ver Ejemplos", command=self.mostrar_ejemplos_guardados).pack(side='left', padx=5)
        ttk.Button(marco_botones, text="Volver", command=self.crear_menu_principal).pack(side='left', padx=5)

    def guardar_nuevo_ejemplo(self):
        categoria = self.entrada_categoria.get().lower()
        ejemplo = self.entrada_ejemplo.get()
        
        if categoria and ejemplo:
            if categoria in self.categorias:
                if self.guardar_ejemplo_usuario({"categoria": categoria, "ejemplo": ejemplo}):
                    messagebox.showinfo("Éxito", "Ejemplo guardado correctamente 📚")
                else:
                    messagebox.showerror("Error", "Límite alcanzado (100 ejemplos)")
            else:
                messagebox.showerror("Error", "Categoría no válida")
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos")

    def mostrar_ejemplos_guardados(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Mis Ejemplos Guardados")
        ventana.geometry("600x400")
        
        texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD)
        texto.pack(fill='both', expand=True, padx=20, pady=20)
        
        contenido = "\n".join([f"- [{e['categoria']}] {e['ejemplo']}" 
                             for e in self.ejemplos_usuario])
        texto.insert(tk.INSERT, contenido)
        texto.configure(state='disabled')

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdverbiosApp(root)
    root.mainloop()
