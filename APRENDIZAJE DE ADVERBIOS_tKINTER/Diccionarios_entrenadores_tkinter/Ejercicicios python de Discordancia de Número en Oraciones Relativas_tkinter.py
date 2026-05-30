import json
import tkinter as tk
from tkinter import messagebox

class ConcordanciaEjercicios:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Concordancia de Número")
        self.ejemplos_usuario = []
        self.max_ejemplos = 100
        self.teoria = """
        Discordancia de Número en Oraciones Relativas:
        En construcciones partitivas como "Fui de los que se {negaron/negó} a aceptar la propuesta", 
        el verbo puede aparecer en plural o singular. La normativa favorece el plural porque el sujeto 
        de la relativa es "los que", pero el singular se usa por una reestructuración sintáctica.
        """
        self.ejercicios_completacion = [
            ("Pedro fue de los que se ______ (opuso/opusieron) a la decisión.", "opusieron"),
            ("Ana es de las que siempre ______ (defiende/defienden) sus ideas.", "defienden"),
            ("Luis es de los que nunca ______ (acepta/aceptan) una derrota.", "aceptan")
        ]
        self.ejercicios_traduccion = [
            ("Fui de los que se negaron a aceptar la propuesta.", "I was one of those who refused to accept the proposal."),
            ("Él era de los que siempre defendían sus ideas.", "He was one of those who always defended their ideas."),
            ("Ana es de las que nunca aceptan una crítica.", "Ana is one of those who never accept criticism.")
        ]
        self.crear_interfaz()
    
    def mostrar_teoria(self):
        messagebox.showinfo("Teoría", self.teoria)
    
    def practicar_completacion(self):
        def verificar_respuesta():
            respuesta = entrada.get().strip()
            correcta = self.ejercicios_completacion[indice][1]
            if respuesta.lower() == correcta.lower():
                messagebox.showinfo("Correcto", "✅ Respuesta correcta!")
            else:
                messagebox.showwarning("Incorrecto", "❌ Respuesta incorrecta. Intente de nuevo.")
        
        indice = 0
        ventana = tk.Toplevel(self.root)
        ventana.title("Ejercicio de completación")
        tk.Label(ventana, text=self.ejercicios_completacion[indice][0]).pack()
        entrada = tk.Entry(ventana)
        entrada.pack()
        tk.Button(ventana, text="Verificar", command=verificar_respuesta).pack()
    
    def practicar_redaccion(self):
        if len(self.ejemplos_usuario) >= self.max_ejemplos:
            messagebox.showwarning("Límite alcanzado", "Has alcanzado el límite de ejemplos guardados (100).")
            return
        
        def guardar_ejemplo():
            ejemplo = entrada.get().strip()
            if ejemplo:
                self.ejemplos_usuario.append(ejemplo)
                messagebox.showinfo("Guardado", "Ejemplo guardado correctamente.")
                ventana.destroy()
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Redacción de ejemplos")
        tk.Label(ventana, text="Escribe tu propia oración siguiendo el patrón de discordancia:").pack()
        entrada = tk.Entry(ventana, width=50)
        entrada.pack()
        tk.Button(ventana, text="Guardar", command=guardar_ejemplo).pack()
    
    def practicar_traduccion(self):
        def verificar_traduccion():
            respuesta = entrada.get().strip()
            correcta = self.ejercicios_traduccion[indice][1]
            if respuesta.lower() == correcta.lower():
                messagebox.showinfo("Correcto", "✅ Respuesta correcta!")
            else:
                messagebox.showwarning("Incorrecto", "❌ Respuesta incorrecta. Intente de nuevo.")
        
        indice = 0
        ventana = tk.Toplevel(self.root)
        ventana.title("Ejercicio de traducción")
        tk.Label(ventana, text=f"Traduce al inglés: '{self.ejercicios_traduccion[indice][0]}'").pack()
        entrada = tk.Entry(ventana)
        entrada.pack()
        tk.Button(ventana, text="Verificar", command=verificar_traduccion).pack()
    
    def guardar_ejemplos(self):
        with open("ejemplos_usuario.json", "w") as f:
            json.dump(self.ejemplos_usuario, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Guardado", "Ejemplos guardados en archivo.")
    
    def cargar_ejemplos(self):
        try:
            with open("ejemplos_usuario.json", "r") as f:
                self.ejemplos_usuario = json.load(f)
            messagebox.showinfo("Cargado", "Ejemplos cargados correctamente.")
        except FileNotFoundError:
            messagebox.showwarning("Error", "No hay ejemplos guardados aún.")
    
    def crear_interfaz(self):
        tk.Button(self.root, text="Ver teoría", command=self.mostrar_teoria).pack(fill=tk.X)
        tk.Button(self.root, text="Practicar completación", command=self.practicar_completacion).pack(fill=tk.X)
        tk.Button(self.root, text="Escribir y guardar ejemplos", command=self.practicar_redaccion).pack(fill=tk.X)
        tk.Button(self.root, text="Practicar traducción", command=self.practicar_traduccion).pack(fill=tk.X)
        tk.Button(self.root, text="Guardar ejemplos", command=self.guardar_ejemplos).pack(fill=tk.X)
        tk.Button(self.root, text="Cargar ejemplos", command=self.cargar_ejemplos).pack(fill=tk.X)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(fill=tk.X)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcordanciaEjercicios(root)
    root.mainloop()
