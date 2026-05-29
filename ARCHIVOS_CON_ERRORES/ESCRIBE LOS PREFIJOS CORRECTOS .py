import tkinter as tk
from tkinter import ttk, messagebox
import random

class EmojiPrefijosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Práctica de Prefijos ✍️")
        self.root.geometry("800x600")
        self.root.configure(bg='#F0F8FF')
        self.crear_interfaz()
        self.inicializar_juego()
        
    def crear_interfaz(self):
        # Estilo con emojis y colores
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')
        self.estilo.configure('TLabel', font=('Arial', 12), background='#F0F8FF')
        self.estilo.configure('TButton', font=('Arial', 10), padding=8)
        self.estilo.configure('Titulo.TLabel', font=('Arial', 16, 'bold'), 
                            foreground='#2F4F4F', background='#F0F8FF')
        
        # Marco principal
        self.marco_principal = ttk.Frame(self.root, padding=20)
        self.marco_principal.pack(fill=tk.BOTH, expand=True)
        
        # Cabecera con emojis
        self.titulo = ttk.Label(self.marco_principal, 
                              text="📚✨ ESCRIBE LOS PREFIJOS CORRECTOS ✍️🔍",
                              style='Titulo.TLabel')
        self.titulo.pack(pady=15)
        
        # Panel de información
        self.marco_info = ttk.Frame(self.marco_principal)
        self.marco_info.pack(fill=tk.X, pady=10)
        
        self.etq_puntaje = ttk.Label(self.marco_info, text="🏆 Puntos: 0")
        self.etq_puntaje.pack(side=tk.LEFT, padx=15)
        
        self.etq_nivel = ttk.Label(self.marco_info, text="🚀 Nivel: 1")
        self.etq_nivel.pack(side=tk.RIGHT, padx=15)
        
        # Panel de juego
        self.marco_juego = ttk.Frame(self.marco_principal)
        self.marco_juego.pack(pady=20)
        
        # Palabra oculta con estilo
        self.etq_palabra = ttk.Label(self.marco_juego, 
                                    text="", 
                                    font=('Courier New', 28, 'bold'),
                                    foreground='#2E8B57')
        self.etq_palabra.pack(pady=15)
        
        # Entrada de usuario
        self.entrada = ttk.Entry(self.marco_juego, 
                                font=('Arial', 16), 
                                width=25,
                                style='TEntry')
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', self.verificar_respuesta)
        
        # Botones con emojis
        self.marco_botones = ttk.Frame(self.marco_juego)
        self.marco_botones.pack(pady=15)
        
        self.btn_verificar = ttk.Button(self.marco_botones, 
                                      text="✅ Verificar", 
                                      command=self.verificar_respuesta)
        self.btn_verificar.pack(side=tk.LEFT, padx=8)
        
        self.btn_pista = ttk.Button(self.marco_botones, 
                                  text="💡 Pista (-5 pts)", 
                                  command=self.mostrar_pista)
        self.btn_pista.pack(side=tk.LEFT, padx=8)
        
        # Historial con emojis
        self.historial = ttk.Treeview(self.marco_principal, 
                                    columns=('Intento', 'Resultado'), 
                                    show='headings',
                                    height=8)
        self.historial.heading('Intento', text='📝 Intento')
        self.historial.heading('Resultado', text='🎯 Resultado')
        self.historial.column('Intento', width=400, anchor=tk.W)
        self.historial.column('Resultado', width=150, anchor=tk.CENTER)
        self.historial.pack(fill=tk.BOTH, expand=True, pady=10)

    # Resto del código igual al anterior (métodos de juego)
    # ... (métodos inicializar_juego, generar_nueva_palabra, etc.)

    def mostrar_pista(self):
        if not self.pista_mostrada and self.puntaje >= 5:
            pista = (
                f"🔍 Prefijo: {self.palabra_actual['palabra'][:3].upper()}\n"
                f"📖 Base: {self.palabra_actual['base']} (sustantivo)\n"
                f"📚 Categoría: {self.palabra_actual['categoria'].capitalize()}\n"
                f"📏 Longitud: {len(self.palabra_actual['palabra']} letras\n\n"
                f"💡 ¿Cambio categorial? {'Sí' if self.palabra_actual['categoria'] == 'adjetivo' else 'No'}"
            )
            messagebox.showinfo("🔎 Pista Morfológica", pista)
            self.puntaje -= 5
            self.pista_mostrada = True
            self.actualizar_interfaz()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmojiPrefijosApp(root)
    root.mainloop()
