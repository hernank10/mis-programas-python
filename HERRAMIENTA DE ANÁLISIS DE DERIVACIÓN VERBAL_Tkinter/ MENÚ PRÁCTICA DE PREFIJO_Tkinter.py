import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import sys
import platform

class InstaladorPrefijos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Prefijos Español")
        self.geometry("800x600")
        
        # Variables de control
        self.dependencias_instaladas = False
        
        # Crear interfaz
        self.crear_interfaz()
        
        # Verificar dependencias
        self.verificar_dependencias()

    def crear_interfaz(self):
        # Panel de notificaciones
        self.txt_log = tk.Text(self, wrap=tk.WORD, state='disabled')
        self.txt_log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Botonera
        frame_botones = ttk.Frame(self)
        frame_botones.pack(pady=10)
        
        self.btn_instalar = ttk.Button(frame_botones, text="Instalar Dependencias", command=self.instalar_dependencias)
        self.btn_tablas = ttk.Button(frame_botones, text="Abrir Tablas CRUD", command=self.abrir_tablas_crud, state='disabled')
        self.btn_quiz = ttk.Button(frame_botones, text="Modo Práctica", command=self.iniciar_quiz)
        self.btn_salir = ttk.Button(frame_botones, text="Salir", command=self.destroy)
        
        self.btn_instalar.pack(side=tk.LEFT, padx=5)
        self.btn_tablas.pack(side=tk.LEFT, padx=5)
        self.btn_quiz.pack(side=tk.LEFT, padx=5)
        self.btn_salir.pack(side=tk.LEFT, padx=5)

    def log(self, mensaje):
        self.txt_log.config(state='normal')
        self.txt_log.insert(tk.END, mensaje + "\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state='disabled')
    
    def verificar_dependencias(self):
        try:
            import kivy
            import fastapi
            self.dependencias_instaladas = True
            self.btn_tablas.config(state='normal')
            self.log("✓ Dependencias ya instaladas")
        except ImportError:
            self.log("⚠️ Dependencias no instaladas. Click en 'Instalar Dependencias'")

    def instalar_dependencias(self):
        self.log("🔧 Instalando dependencias...")
        
        requerimientos = [
            'kivy', 
            'fastapi', 
            'uvicorn', 
            'python-multipart'
        ]
        
        try:
            # Instalar paquetes pip
            for paquete in requerimientos:
                subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])
                self.log(f"✓ {paquete} instalado")
            
            # Instalar dependencias para Kivy en macOS
            if platform.system() == "Darwin":
                self.log("⚙️ Instalando dependencias para macOS...")
                subprocess.run(['brew', 'install', 'sdl2', 'sdl2_image', 'sdl2_ttf', 'sdl2_mixer', 'portaudio'])
            
            self.dependencias_instaladas = True
            self.btn_tablas.config(state='normal')
            messagebox.showinfo("Éxito", "Dependencias instaladas correctamente")
            
        except Exception as e:
            messagebox.showerror("Error", f"Fallo en instalación: {str(e)}")

    def abrir_tablas_crud(self):
        ventana_crud = tk.Toplevel(self)
        ventana_crud.title("Tablas CRUD - Prefijos")
        
        # Crear tabla
        columnas = ("Palabra", "Prefijo", "Clasificación", "Significado")
        tree = ttk.Treeview(ventana_crud, columns=columnas, show='headings')
        
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        # Datos de ejemplo
        datos = [
            ("Antinuclear", "anti-", "Oposición", "Contra energía nuclear"),
            ("Deshacer", "des-", "Negación", "Revertir acción")
        ]
        
        for item in datos:
            tree.insert('', tk.END, values=item)
        
        # Botones CRUD
        frame_controles = ttk.Frame(ventana_crud)
        ttk.Button(frame_controles, text="Añadir", command=lambda: self.anadir_item(tree)).pack(side=tk.LEFT)
        ttk.Button(frame_controles, text="Eliminar", command=lambda: self.eliminar_item(tree)).pack(side=tk.LEFT)
        
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        frame_controles.pack(pady=5)

    def anadir_item(self, tree):
        dialogo = tk.Toplevel(self)
        dialogo.title("Nuevo Prefijo")
        
        entradas = []
        ttk.Label(dialogo, text="Palabra:").grid(row=0, column=0, padx=5, pady=5)
        palabra = ttk.Entry(dialogo)
        palabra.grid(row=0, column=1, padx=5, pady=5)
        entradas.append(palabra)
        
        ttk.Label(dialogo, text="Prefijo:").grid(row=1, column=0, padx=5, pady=5)
        prefijo = ttk.Entry(dialogo)
        prefijo.grid(row=1, column=1, padx=5, pady=5)
        entradas.append(prefijo)
        
        ttk.Label(dialogo, text="Clasificación:").grid(row=2, column=0, padx=5, pady=5)
        clasificacion = ttk.Entry(dialogo)
        clasificacion.grid(row=2, column=1, padx=5, pady=5)
        entradas.append(clasificacion)
        
        ttk.Label(dialogo, text="Significado:").grid(row=3, column=0, padx=5, pady=5)
        significado = ttk.Entry(dialogo)
        significado.grid(row=3, column=1, padx=5, pady=5)
        entradas.append(significado)
        
        def guardar():
            valores = [e.get() for e in entradas]
            if all(valores):
                tree.insert('', tk.END, values=valores)
                dialogo.destroy()
        
        ttk.Button(dialogo, text="Guardar", command=guardar).grid(row=4, columnspan=2, pady=10)

    def eliminar_item(self, tree):
        seleccionado = tree.selection()
        if seleccionado:
            tree.delete(seleccionado)

    def iniciar_quiz(self):
        ventana_quiz = tk.Toplevel(self)
        ventana_quiz.title("Práctica de Prefijos")
        
        preguntas = [
            {"prefijo": "anti-", "palabra": "nuclear", "respuesta": "antinuclear"},
            {"prefijo": "des-", "palabra": "hacer", "respuesta": "deshacer"},
            {"prefijo": "re-", "palabra": "escribir", "respuesta": "reescribir"}
        ]
        
        current_pregunta = tk.IntVar(value=0)
        puntaje = tk.IntVar(value=0)
        
        def mostrar_pregunta():
            idx = current_pregunta.get()
            if idx < len(preguntas):
                pregunta = preguntas[idx]
                lbl_prefijo.config(text=pregunta["prefijo"])
                lbl_palabra.config(text=pregunta["palabra"])
                entrada.delete(0, tk.END)
            else:
                messagebox.showinfo("Resultado", f"Puntuación final: {puntaje.get()}/{len(preguntas)}")
                ventana_quiz.destroy()
        
        def verificar_respuesta():
            idx = current_pregunta.get()
            respuesta_usuario = entrada.get().lower()
            respuesta_correcta = preguntas[idx]["respuesta"]
            
            if respuesta_usuario == respuesta_correcta:
                puntaje.set(puntaje.get() + 1)
                messagebox.showinfo("Correcto", "¡Respuesta correcta!")
            else:
                messagebox.showerror("Incorrecto", f"La respuesta correcta era: {respuesta_correcta}")
            
            current_pregunta.set(current_pregunta.get() + 1)
            mostrar_pregunta()
        
        # Widgets
        frame = ttk.Frame(ventana_quiz, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        lbl_prefijo = ttk.Label(frame, text="", font=('Arial', 24))
        lbl_prefijo.pack()
        
        lbl_palabra = ttk.Label(frame, text="", font=('Arial', 24))
        lbl_palabra.pack(pady=10)
        
        entrada = ttk.Entry(frame, font=('Arial', 18))
        entrada.pack(pady=10)
        
        btn_verificar = ttk.Button(frame, text="Verificar", command=verificar_respuesta)
        btn_verificar.pack()
        
        mostrar_pregunta()

if __name__ == "__main__":
    app = InstaladorPrefijos()
    
    # Verificar Homebrew en macOS
    if platform.system() == "Darwin":
        try:
            subprocess.check_output(['brew', '--version'])
        except:
            messagebox.showwarning(
                "Requisito macOS",
                "Necesitas Homebrew para dependencias gráficas.\n"
                "Instálalo desde https://brew.sh"
            )
    
    app.mainloop()
