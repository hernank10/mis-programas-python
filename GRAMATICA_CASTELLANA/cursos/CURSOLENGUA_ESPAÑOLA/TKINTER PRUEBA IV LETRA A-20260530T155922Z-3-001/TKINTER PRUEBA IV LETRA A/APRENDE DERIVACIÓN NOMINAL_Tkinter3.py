import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
from reportlab.pdfgen import canvas
import random

class DerivacionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprendizaje de Derivación")
        self.geometry("1000x700")
        self.configure(bg='#F0F0F0')
        
        # Configuración de la base de datos
        self.conn = sqlite3.connect('derivacion.db')
        self.crear_tablas()
        self.cargar_datos_iniciales()
        
        # Variables de estado
        self.usuario_actual = None
        self.puntos = 0
        self.racha = 0
        
        # Configurar interfaz
        self.crear_menu()
        self.crear_interfaz_principal()
        self.mostrar_login()
        
    def crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT UNIQUE,
                        puntos INTEGER DEFAULT 0,
                        racha INTEGER DEFAULT 0)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS afijos (
                        id INTEGER PRIMARY KEY,
                        tipo TEXT,
                        forma TEXT,
                        categoria TEXT,
                        regla TEXT,
                        ejemplo TEXT)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS progreso (
                        id INTEGER PRIMARY KEY,
                        usuario_id INTEGER,
                        fecha TEXT,
                        puntos INTEGER)''')
        self.conn.commit()

    def cargar_datos_iniciales(self):
        # ... (similar a la versión anterior)
        
    def crear_menu(self):
        menubar = tk.Menu(self)
        
        menu_usuario = tk.Menu(menubar, tearoff=0)
        menu_usuario.add_command(label="Perfil", command=self.mostrar_perfil)
        menu_usuario.add_command(label="Cerrar sesión", command=self.cerrar_sesion)
        
        menu_ejercicios = tk.Menu(menubar, tearoff=0)
        menu_ejercicios.add_command(label="Nuevo ejercicio", command=self.nuevo_ejercicio)
        
        menubar.add_cascade(label="Usuario", menu=menu_usuario)
        menubar.add_cascade(label="Ejercicios", menu=menu_ejercicios)
        menubar.add_command(label="Progreso", command=self.mostrar_progreso)
        menubar.add_command(label="Salir", command=self.destroy)
        
        self.config(menu=menubar)
    
    def crear_interfaz_principal(self):
        self.frame_login = ttk.Frame(self)
        self.frame_ejercicio = ttk.Frame(self)
        self.frame_progreso = ttk.Frame(self)
        self.frame_perfil = ttk.Frame(self)
        
        # Configurar todos los frames
        self.configurar_login()
        self.configurar_ejercicio()
        self.configurar_progreso()
        self.configurar_perfil()
        
    def configurar_login(self):
        ttk.Label(self.frame_login, text="Nombre de usuario:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_usuario = ttk.Entry(self.frame_login)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Button(self.frame_login, text="Ingresar", command=self.verificar_usuario).grid(row=1, column=0, columnspan=2, pady=10)
    
    def configurar_ejercicio(self):
        self.label_ejercicio = ttk.Label(self.frame_ejercicio, text="", font=('Arial', 14))
        self.label_ejercicio.pack(pady=20)
        
        self.entry_respuesta = ttk.Entry(self.frame_ejercicio, font=('Arial', 12))
        self.entry_respuesta.pack(pady=10)
        
        ttk.Button(self.frame_ejercicio, text="Verificar", command=self.verificar_respuesta).pack(pady=10)
        
        self.label_puntos = ttk.Label(self.frame_ejercicio, text="Puntos: 0 | Racha: 0")
        self.label_puntos.pack(pady=10)
    
    def configurar_progreso(self):
        self.figura = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, self.frame_progreso)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def nuevo_ejercicio(self):
        self.ocultar_todos_frames()
        self.frame_ejercicio.pack(fill=tk.BOTH, expand=True)
        self.generar_ejercicio()
    
    def generar_ejercicio(self):
        tipos = ["formacion", "identificacion", "excepcion"]
        tipo = random.choice(tipos)
        
        if tipo == "formacion":
            afijo = self.obtener_afijo_aleatorio()
            base = self.generar_palabra_aleatoria()
            self.ejercicio_actual = {
                "tipo": tipo,
                "afijo": afijo,
                "base": base,
                "respuesta_correcta": f"{base}{afijo[1]}" if afijo[0] == 'sufijo' else f"{afijo[1]}{base}"
            }
            self.label_ejercicio.config(text=f"Forma una palabra usando: {afijo[1]}\nBase: {base}")
        
        self.entry_respuesta.delete(0, tk.END)
    
    def verificar_respuesta(self):
        respuesta = self.entry_respuesta.get().strip().lower()
        if respuesta == self.ejercicio_actual["respuesta_correcta"]:
            self.puntos += 10
            self.racha += 1
            messagebox.showinfo("Correcto", "¡Respuesta correcta! +10 puntos")
        else:
            self.racha = 0
            messagebox.showerror("Incorrecto", f"La respuesta correcta era: {self.ejercicio_actual['respuesta_correcta']}")
        
        self.actualizar_puntos()
        self.nuevo_ejercicio()
    
    def mostrar_progreso(self):
        self.ocultar_todos_frames()
        self.frame_progreso.pack(fill=tk.BOTH, expand=True)
        self.actualizar_grafico()
    
    def actualizar_grafico(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT fecha, SUM(puntos) FROM progreso WHERE usuario_id = ? GROUP BY fecha", 
                      (self.usuario_actual[0],))
        datos = cursor.fetchall()
        
        self.ax.clear()
        if datos:
            fechas = [d[0] for d in datos]
            puntos = [d[1] for d in datos]
            self.ax.plot(fechas, puntos, marker='o')
            self.ax.set_title("Progreso de Aprendizaje")
            self.ax.set_xlabel("Fecha")
            self.ax.set_ylabel("Puntos Acumulados")
            self.canvas.draw()
    
    def exportar_datos(self):
        formato = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                              filetypes=[("Excel", "*.xlsx"), ("PDF", "*.pdf")])
        if formato:
            if formato.endswith('.xlsx'):
                self.exportar_excel(formato)
            else:
                self.exportar_pdf(formato)
    
    def mostrar_perfil(self):
        self.ocultar_todos_frames()
        self.frame_perfil.pack(fill=tk.BOTH, expand=True)
        # ... (configurar widgets de perfil)
    
    def ocultar_todos_frames(self):
        for frame in [self.frame_login, self.frame_ejercicio, self.frame_progreso, self.frame_perfil]:
            frame.pack_forget()
    
    def verificar_usuario(self):
        nombre = self.entry_usuario.get()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
        usuario = cursor.fetchone()
        
        if usuario:
            self.usuario_actual = usuario
            self.puntos = usuario[2]
            self.racha = usuario[3]
            self.ocultar_todos_frames()
            self.nuevo_ejercicio()
        else:
            messagebox.showerror("Error", "Usuario no registrado")
    
    def actualizar_puntos(self):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE usuarios SET puntos = ?, racha = ? WHERE id = ?",
                      (self.puntos, self.racha, self.usuario_actual[0]))
        self.conn.commit()
        self.label_puntos.config(text=f"Puntos: {self.puntos} | Racha: {self.racha}")
    
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = DerivacionApp()
    app.run()
