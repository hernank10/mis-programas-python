import json
import time
import os
import pygame
import tkinter as tk
from tkinter import messagebox, scrolledtext
from rich.console import Console
from rich.text import Text

class EnunciadosNoOracionales:
    def __init__(self):
        self.ejemplos_usuario = []
        self.archivo = "ejemplos_usuario.json"
        self.puntuacion = 0
        self.cargar_ejemplos()
        pygame.mixer.init()
        self.console = Console()
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicios de Enunciados No Oracionales")
        self.ventana.geometry("600x500")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        self.texto_teoria = scrolledtext.ScrolledText(self.ventana, width=70, height=10, wrap=tk.WORD)
        self.texto_teoria.insert(tk.INSERT, """
        TEORÍA SOBRE ENUNCIADOS NO ORACIONALES:
        --------------------------------------------------
        - La coordinación permite unir elementos que pueden ser oraciones completas o fragmentos sin verbo.
        - La subordinación requiere un verbo conjugado en la proposición subordinada.
        - Ejemplos de coordinación válida:
          * Llegamos temprano, y la comida, deliciosa.
          * Viajamos mucho, pero el clima, terrible.
        - Ejemplos de subordinación inválida:
          * *Si la película, interesante.*
          * *Porque la cena, excelente.*
        """)
        self.texto_teoria.pack(pady=10)
        
        self.boton_ejercicios = tk.Button(self.ventana, text="Ejercicios de completación", command=self.ejercicios_completacion)
        self.boton_ejercicios.pack(pady=5)
        
        self.boton_redaccion = tk.Button(self.ventana, text="Ejercicios de redacción", command=self.ejercicios_redaccion)
        self.boton_redaccion.pack(pady=5)
        
        self.boton_ver_ejemplos = tk.Button(self.ventana, text="Ver ejemplos guardados", command=self.ver_ejemplos_guardados)
        self.boton_ver_ejemplos.pack(pady=5)
        
        self.boton_puntuacion = tk.Button(self.ventana, text="Ver puntuación", command=self.mostrar_puntuacion)
        self.boton_puntuacion.pack(pady=5)
    
    def reproducir_sonido(self, archivo):
        pygame.mixer.Sound(archivo).play()
    
    def ejercicios_completacion(self):
        ejercicios = [
            ("Llegamos temprano, y la comida, ________.", "deliciosa"),
            ("Viajamos mucho, pero el clima, ________.", "terrible"),
            ("No encontramos hotel, aunque el viaje, ________.", "interesante")
        ]
        
        for oracion, respuesta_correcta in ejercicios:
            respuesta = tk.simpledialog.askstring("Ejercicio de completación", f"{oracion}\nEscribe la palabra correcta:")
            if respuesta and respuesta.lower() == respuesta_correcta:
                messagebox.showinfo("Correcto!", "✅ Respuesta correcta!")
                self.reproducir_sonido("correcto.wav")
                self.puntuacion += 10
            else:
                messagebox.showerror("Incorrecto", f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
                self.reproducir_sonido("incorrecto.wav")
    
    def ejercicios_redaccion(self):
        if len(self.ejemplos_usuario) >= 100:
            messagebox.showwarning("Límite alcanzado", "Has alcanzado el límite de 100 ejemplos guardados.")
            return
        
        ejemplo = tk.simpledialog.askstring("Ejercicio de redacción", "Escribe un ejemplo de enunciado no oracional:")
        traduccion = tk.simpledialog.askstring("Ejercicio de redacción", "Escribe la traducción al inglés:")
        
        if ejemplo and traduccion:
            self.ejemplos_usuario.append({"espanol": ejemplo, "ingles": traduccion})
            self.guardar_ejemplos()
            messagebox.showinfo("Guardado", "Ejemplo guardado con éxito!")
            self.reproducir_sonido("guardar.wav")
    
    def guardar_ejemplos(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.ejemplos_usuario, f, ensure_ascii=False, indent=4)
    
    def cargar_ejemplos(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.ejemplos_usuario = json.load(f)
        except FileNotFoundError:
            self.ejemplos_usuario = []
    
    def ver_ejemplos_guardados(self):
        ejemplos_texto = "\n".join([f"{i+1}. Español: {ej['espanol']}\n   Inglés: {ej['ingles']}" for i, ej in enumerate(self.ejemplos_usuario)])
        messagebox.showinfo("Ejemplos Guardados", ejemplos_texto if ejemplos_texto else "No hay ejemplos guardados aún.")
    
    def mostrar_puntuacion(self):
        messagebox.showinfo("Puntuación", f"Tu puntuación actual es: {self.puntuacion}")
    
    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = EnunciadosNoOracionales()
    app.ejecutar()
