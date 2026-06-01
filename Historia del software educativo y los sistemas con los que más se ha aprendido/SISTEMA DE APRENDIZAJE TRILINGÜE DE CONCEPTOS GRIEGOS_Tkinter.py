import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import json
import os
from datetime import datetime
import threading
import time

class AplicacionGriego(tk.Tk):
    """Aplicación principal Tkinter para aprendizaje de conceptos griegos"""
    
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Sistema de Aprendizaje Trilingüe - Conceptos Griegos")
        self.geometry("1200x700")
        self.minsize(1000, 600)
        
        # Cargar recursos
        self.conceptos = self.cargar_conceptos()
        self.estadisticas = self.cargar_estadisticas()
        self.concepto_actual = None
        self.tiempo_inicio = None
        self.puntuacion_desafio = 0
        self.preguntas_desafio = []
        self.indice_pregunta = 0
        
        # Configurar estilos
        self.configurar_estilos()
        
        # Crear contenedor principal
        self.contenedor = ttk.Frame(self)
        self.contenedor.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Diccionario de frames
        self.frames = {}
        
        # Crear todos los frames
        for F in (MenuPrincipalFrame, EscrituraCompletaFrame, ComparacionFrame,
                 DesafioFrame, FrasesFrame, ConceptosFrame, EstadisticasFrame, ExamenFrame):
            frame_name = F.__name__
            frame = F(parent=self.contenedor, controller=self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Mostrar menú principal
        self.mostrar_frame("MenuPrincipalFrame")
        
        # Configurar grid del contenedor
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)
        
        # Barra de estado
        self.crear_barra_estado()
        
        # Proteger cierre
        self.protocol("WM_DELETE_WINDOW", self.al_salir)
    
    def configurar_estilos(self):
        """Configura los estilos de la aplicación"""
        style = ttk.Style()
        style.theme_use("clam")
        
        # Colores griegos
        self.colores = {
            "fondo": "#f5f5f5",
            "azul_griego": "#0054a6",  # Azul bandera griega
            "blanco": "#ffffff",
            "gris": "#e0e0e0",
            "texto": "#2c3e50",
            "exito": "#27ae60",
            "error": "#e74c3c",
            "advertencia": "#f39c12"
        }
        
        # Configurar estilos de widgets
        style.configure("Titulo.TLabel", font=("Helvetica", 16, "bold"), 
                       foreground=self.colores["azul_griego"])
        style.configure("Subtitulo.TLabel", font=("Helvetica", 12, "bold"))
        style.configure("Concepto.TLabel", font=("Courier", 14, "bold"))
        style.configure("Griego.TLabel", font=("Noto Sans", 16), 
                       foreground=self.colores["azul_griego"])
        style.configure("BotonPrincipal.TButton", font=("Helvetica", 10, "bold"),
                       padding=10)
    
    def crear_barra_estado(self):
        """Crea la barra de estado inferior"""
        self.barra_estado = ttk.Frame(self)
        self.barra_estado.pack(side="bottom", fill="x", padx=10, pady=5)
        
        self.estado_conceptos = ttk.Label(
            self.barra_estado, 
            text=f"Conceptos: {len(self.conceptos)} | Practicados: {len(self.estadisticas.get('conceptos_practicados', set()))}"
        )
        self.estado_conceptos.pack(side="left")
        
        self.estado_aciertos = ttk.Label(
            self.barra_estado,
            text="Aciertos: 0%"
        )
        self.estado_aciertos.pack(side="right")
        
        self.actualizar_barra_estado()
    
    def actualizar_barra_estado(self):
        """Actualiza la información en la barra de estado"""
        practicados = len(self.estadisticas.get('conceptos_practicados', set()))
        total = len(self.conceptos)
        
        intentos = self.estadisticas.get('intentos', 0)
        aciertos = self.estadisticas.get('aciertos', 0)
        porcentaje = (aciertos / (intentos * 2)) * 100 if intentos > 0 else 0
        
        self.estado_conceptos.config(
            text=f"Conceptos: {total} | Practicados: {practicados} ({practicados/total*100:.1f}%)"
        )
        self.estado_aciertos.config(
            text=f"Aciertos: {aciertos}/{intentos*2} ({porcentaje:.1f}%)"
        )
    
    def cargar_conceptos(self):
        """Carga la base de datos de conceptos griegos"""
        try:
            with open('conceptos_griegos.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            # Datos por defecto si no existe el archivo
            return [
                {
                    "id": 1,
                    "griego": "Γνῶθι σαυτόν",
                    "transliteracion": "Gnōthi seautón",
                    "espanol": "Conócete a ti mismo",
                    "ingles": "Know thyself",
                    "categoria": "Filosofía",
                    "explicacion": "Máxima délfica que invita al autoconocimiento"
                },
                {
                    "id": 2,
                    "griego": "Ἀρετή",
                    "transliteracion": "Aretḗ",
                    "espanol": "Virtud, excelencia",
                    "ingles": "Virtue, excellence",
                    "categoria": "Filosofía",
                    "explicacion": "Excelencia en el cumplimiento de la función propia"
                }
            ]
    
    def cargar_estadisticas(self):
        """Carga las estadísticas de aprendizaje"""
        try:
            with open('estadisticas_griego.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {
                'intentos': 0,
                'aciertos': 0,
                'conceptos_practicados': set(),
                'historial': []
            }
    
    def guardar_estadisticas(self):
        """Guarda las estadísticas en archivo"""
        # Convertir set a list para JSON
        stats = self.estadisticas.copy()
        stats['conceptos_practicados'] = list(stats.get('conceptos_practicados', set()))
        
        with open('estadisticas_griego.json', 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
    
    def al_salir(self):
        """Maneja el cierre de la aplicación"""
        self.guardar_estadisticas()
        self.destroy()
    
    def mostrar_frame(self, frame_name):
        """Muestra un frame específico"""
        frame = self.frames[frame_name]
        frame.tkraise()
        
        # Actualizar barra de estado
        self.actualizar_barra_estado()
    
    def obtener_concepto_aleatorio(self):
        """Devuelve un concepto aleatorio"""
        return random.choice(self.conceptos)
    
    def registrar_intento(self, concepto_id, correcto=False):
        """Registra un intento de respuesta"""
        self.estadisticas['intentos'] = self.estadisticas.get('intentos', 0) + 1
        
        if correcto:
            self.estadisticas['aciertos'] = self.estadisticas.get('aciertos', 0) + 1
        
        # Añadir a conceptos practicados
        practicados = self.estadisticas.get('conceptos_practicados', set())
        practicados.add(concepto_id)
        self.estadisticas['conceptos_practicados'] = practicados
        
        self.actualizar_barra_estado()


class MenuPrincipalFrame(ttk.Frame):
    """Frame del menú principal"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configurar grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Título
        titulo_frame = ttk.Frame(self)
        titulo_frame.grid(row=0, column=0, pady=(20, 40))
        
        ttk.Label(
            titulo_frame,
            text="ΣΥΣΤΗΜΑ ΜΑΘΗΣΗΣ ΕΛΛΗΝΙΚΩΝ ΕΝΝΟΙΩΝ",
            style="Titulo.TLabel"
        ).pack()
        
        ttk.Label(
            titulo_frame,
            text="Sistema Trilingüe de Aprendizaje - Griego, Español, Inglés",
            font=("Helvetica", 12)
        ).pack()
        
        # Botones principales
        botones_frame = ttk.Frame(self)
        botones_frame.grid(row=1, column=0, padx=50)
        
        # Crear 2 columnas de botones
        col1 = ttk.Frame(botones_frame)
        col1.pack(side="left", expand=True, padx=10)
        
        col2 = ttk.Frame(botones_frame)
        col2.pack(side="right", expand=True, padx=10)
        
        botones = [
            ("📝 Escritura Completa", "EscrituraCompletaFrame"),
            ("🔄 Comparación Bilingüe", "ComparacionFrame"),
            ("⚡ Modo Desafío", "DesafioFrame"),
            ("💬 Frases Personalizadas", "FrasesFrame"),
            ("📚 Ver Conceptos", "ConceptosFrame"),
            ("📊 Estadísticas", "EstadisticasFrame"),
            ("🎯 Examen Final", "ExamenFrame")
        ]
        
        # Distribuir botones en dos columnas
        for i, (texto, frame) in enumerate(botones):
            col = col1 if i % 2 == 0 else col2
            btn = ttk.Button(
                col,
                text=texto,
                style="BotonPrincipal.TButton",
                command=lambda f=frame: controller.mostrar_frame(f),
                width=25
            )
            btn.pack(pady=5, fill="x")
        
        # Información de progreso
        info_frame = ttk.Frame(self)
        info_frame.grid(row=2, column=0, pady=20)
        
        practicados = len(controller.estadisticas.get('conceptos_practicados', set()))
        total = len(controller.conceptos)
        porcentaje = (practicados / total * 100) if total > 0 else 0
        
        # Barra de progreso
        ttk.Label(info_frame, text="Progreso general:").pack()
        self.barra_progreso = ttk.Progressbar(
            info_frame,
            length=400,
            mode='determinate'
        )
        self.barra_progreso.pack(pady=5)
        self.barra_progreso['value'] = porcentaje
        
        ttk.Label(
            info_frame,
            text=f"{practicados}/{total} conceptos practicados ({porcentaje:.1f}%)"
        ).pack()


class EscrituraCompletaFrame(ttk.Frame):
    """Frame para ejercicio de escritura completa"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.concepto_actual = None
        
        # Configurar grid
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        barra_superior = ttk.Frame(self)
        barra_superior.grid(row=0, column=0, sticky="ew", pady=10)
        
        ttk.Button(
            barra_superior,
            text="← Menú Principal",
            command=lambda: controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left")
        
        ttk.Button(
            barra_superior,
            text="Nuevo Concepto",
            command=self.nuevo_concepto
        ).pack(side="right")
        
        # Área principal dividida
        main_frame = ttk.Frame(self)
        main_frame.grid(row=1, column=0, sticky="nsew", pady=20)
        
        # Panel izquierdo: Concepto y escritura
        izquierda = ttk.Frame(main_frame)
        izquierda.pack(side="left", fill="both", expand=True, padx=10)
        
        # Panel derecho: Información y frases
        derecha = ttk.Frame(main_frame)
        derecha.pack(side="right", fill="both", expand=True, padx=10)
        
        # --- PANEL IZQUIERDO ---
        # Mostrar concepto griego
        self.lbl_griego = ttk.Label(
            izquierda,
            text="",
            style="Griego.TLabel",
            font=("Noto Sans", 24)
        )
        self.lbl_griego.pack(pady=20)
        
        self.lbl_explicacion = ttk.Label(
            izquierda,
            text="",
            wraplength=400,
            font=("Helvetica", 10)
        )
        self.lbl_explicacion.pack(pady=10)
        
        # Campos para escribir
        campos_frame = ttk.LabelFrame(izquierda, text="Escribe las traducciones", padding=10)
        campos_frame.pack(fill="x", pady=20)
        
        ttk.Label(campos_frame, text="Transliteración:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_translit = ttk.Entry(campos_frame, width=40)
        self.entry_translit.grid(row=0, column=1, padx=5)
        
        ttk.Label(campos_frame, text="Español:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_espanol = ttk.Entry(campos_frame, width=40)
        self.entry_espanol.grid(row=1, column=1, padx=5)
        
        ttk.Label(campos_frame, text="Inglés:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_ingles = ttk.Entry(campos_frame, width=40)
        self.entry_ingles.grid(row=2, column=1, padx=5)
        
        # Botones de verificación
        botones_frame = ttk.Frame(izquierda)
        botones_frame.pack(pady=10)
        
        ttk.Button(
            botones_frame,
            text="Verificar Respuestas",
            command=self.verificar_respuestas
        ).pack(side="left", padx=5)
        
        ttk.Button(
            botones_frame,
            text="Mostrar Respuestas",
            command=self.mostrar_respuestas
        ).pack(side="left", padx=5)
        
        # --- PANEL DERECHO ---
        # Área para frases
        frases_frame = ttk.LabelFrame(derecha, text="Crea tus propias frases", padding=10)
        frases_frame.pack(fill="both", expand=True)
        
        ttk.Label(frases_frame, text="Frase en Español:").pack(anchor="w", pady=(0, 5))
        self.text_espanol = scrolledtext.ScrolledText(frases_frame, height=4, width=40)
        self.text_espanol.pack(fill="x", pady=(0, 15))
        
        ttk.Label(frases_frame, text="Frase en Inglés:").pack(anchor="w", pady=(0, 5))
        self.text_ingles = scrolledtext.ScrolledText(frases_frame, height=4, width=40)
        self.text_ingles.pack(fill="x", pady=(0, 15))
        
        ttk.Button(
            frases_frame,
            text="Guardar Frases",
            command=self.guardar_frases
        ).pack()
        
        # Iniciar con un concepto
        self.nuevo_concepto()
    
    def nuevo_concepto(self):
        """Carga un nuevo concepto aleatorio"""
        self.concepto_actual = self.controller.obtener_concepto_aleatorio()
        
        # Actualizar display
        self.lbl_griego.config(text=self.concepto_actual["griego"])
        self.lbl_explicacion.config(text=self.concepto_actual["explicacion"])
        
        # Limpiar campos
        self.entry_translit.delete(0, tk.END)
        self.entry_espanol.delete(0, tk.END)
        self.entry_ingles.delete(0, tk.END)
        self.text_espanol.delete(1.0, tk.END)
        self.text_ingles.delete(1.0, tk.END)
        
        # Poner foco en primer campo
        self.entry_translit.focus()
    
    def verificar_respuestas(self):
        """Verifica las respuestas del usuario"""
        if not self.concepto_actual:
            return
        
        translit = self.entry_translit.get().strip()
        espanol = self.entry_espanol.get().strip()
        ingles = self.entry_ingles.get().strip()
        
        correctas = 0
        
        # Verificar transliteración
        if translit.lower() == self.concepto_actual["transliteracion"].lower():
            self.entry_translit.config(foreground="green")
            correctas += 1
        else:
            self.entry_translit.config(foreground="red")
        
        # Verificar español
        if (self.concepto_actual["espanol"].lower() in espanol.lower() or 
            espanol.lower() in self.concepto_actual["espanol"].lower()):
            self.entry_espanol.config(foreground="green")
            correctas += 1
        else:
            self.entry_espanol.config(foreground="red")
        
        # Verificar inglés
        if (self.concepto_actual["ingles"].lower() in ingles.lower() or 
            ingles.lower() in self.concepto_actual["ingles"].lower()):
            self.entry_ingles.config(foreground="green")
            correctas += 1
        else:
            self.entry_ingles.config(foreground="red")
        
        # Registrar intento
        self.controller.registrar_intento(
            self.concepto_actual["id"],
            correcto=(correctas > 1)
        )
        
        messagebox.showinfo(
            "Resultado",
            f"Tienes {correctas}/3 respuestas correctas\n\n"
            f"Transliteración correcta: {self.concepto_actual['transliteracion']}\n"
            f"Español correcto: {self.concepto_actual['espanol']}\n"
            f"English correcto: {self.concepto_actual['ingles']}"
        )
    
    def mostrar_respuestas(self):
        """Muestra las respuestas correctas"""
        if self.concepto_actual:
            self.entry_translit.delete(0, tk.END)
            self.entry_translit.insert(0, self.concepto_actual["transliteracion"])
            self.entry_translit.config(foreground="green")
            
            self.entry_espanol.delete(0, tk.END)
            self.entry_espanol.insert(0, self.concepto_actual["espanol"])
            self.entry_espanol.config(foreground="green")
            
            self.entry_ingles.delete(0, tk.END)
            self.entry_ingles.insert(0, self.concepto_actual["ingles"])
            self.entry_ingles.config(foreground="green")
    
    def guardar_frases(self):
        """Guarda las frases creadas por el usuario"""
        frase_es = self.text_espanol.get(1.0, tk.END).strip()
        frase_en = self.text_ingles.get(1.0, tk.END).strip()
        
        if frase_es and frase_en and self.concepto_actual:
            registro = {
                'fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
                'concepto': self.concepto_actual["transliteracion"],
                'frase_espanol': frase_es,
                'frase_ingles': frase_en
            }
            
            historial = self.controller.estadisticas.get('historial', [])
            historial.append(registro)
            self.controller.estadisticas['historial'] = historial
            
            # Guardar en archivo
            with open('frases_griego.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n[{registro['fecha']}]\n")
                f.write(f"Concepto: {registro['concepto']}\n")
                f.write(f"Español: {frase_es}\n")
                f.write(f"English: {frase_en}\n")
                f.write("-" * 40 + "\n")
            
            messagebox.showinfo("Éxito", "Frases guardadas correctamente")
            
            # Limpiar para nuevo ejercicio
            self.text_espanol.delete(1.0, tk.END)
            self.text_ingles.delete(1.0, tk.END)
            self.nuevo_concepto()


class ComparacionFrame(ttk.Frame):
    """Frame para práctica de comparación bilingüe"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.modo = "es-en"  # español a inglés por defecto
        
        # Configurar grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        barra_superior = ttk.Frame(self)
        barra_superior.grid(row=0, column=0, sticky="ew", pady=10)
        
        ttk.Button(
            barra_superior,
            text="← Menú Principal",
            command=lambda: controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left")
        
        # Selector de modo
        modo_frame = ttk.Frame(barra_superior)
        modo_frame.pack(side="right")
        
        ttk.Label(modo_frame, text="Modo:").pack(side="left", padx=(0, 5))
        
        self.modo_var = tk.StringVar(value="es-en")
        modos = [
            ("Español → Inglés", "es-en"),
            ("Inglés → Español", "en-es"),
            ("Griego → Ambos", "griego")
        ]
        
        for texto, valor in modos:
            rb = ttk.Radiobutton(
                modo_frame,
                text=texto,
                variable=self.modo_var,
                value=valor,
                command=self.cambiar_modo
            )
            rb.pack(side="left", padx=5)
        
        # Área central
        centro_frame = ttk.Frame(self)
        centro_frame.grid(row=1, column=0, sticky="nsew", padx=50, pady=20)
        
        # Pregunta
        self.lbl_pregunta = ttk.Label(
            centro_frame,
            text="",
            style="Titulo.TLabel",
            wraplength=600
        )
        self.lbl_pregunta.pack(pady=30)
        
        # Respuesta (dependiendo del modo)
        self.respuesta_frame = ttk.Frame(centro_frame)
        self.respuesta_frame.pack(pady=20)
        
        # Botones
        botones_frame = ttk.Frame(centro_frame)
        botones_frame.pack(pady=20)
        
        ttk.Button(
            botones_frame,
            text="Nueva Pregunta",
            command=self.nueva_pregunta
        ).pack(side="left", padx=5)
        
        ttk.Button(
            botones_frame,
            text="Verificar",
            command=self.verificar_respuesta
        ).pack(side="left", padx=5)
        
        # Información
        self.info_frame = ttk.LabelFrame(centro_frame, text="Información del Concepto", padding=10)
        self.info_frame.pack(fill="x", pady=20)
        
        self.lbl_info = ttk.Label(
            self.info_frame,
            text="",
            wraplength=500
        )
        self.lbl_info.pack()
        
        # Inicializar
        self.cambiar_modo()
        self.nueva_pregunta()
    
    def cambiar_modo(self):
        """Cambia el modo de práctica"""
        self.modo = self.modo_var.get()
        
        # Limpiar frame de respuesta
        for widget in self.respuesta_frame.winfo_children():
            widget.destroy()
        
        # Crear widgets según modo
        if self.modo == "es-en":
            ttk.Label(self.respuesta_frame, text="Traducción al inglés:").pack()
            self.entry_respuesta = ttk.Entry(self.respuesta_frame, width=50)
            self.entry_respuesta.pack()
            
        elif self.modo == "en-es":
            ttk.Label(self.respuesta_frame, text="Traducción al español:").pack()
            self.entry_respuesta = ttk.Entry(self.respuesta_frame, width=50)
            self.entry_respuesta.pack()
            
        elif self.modo == "griego":
            ttk.Label(self.respuesta_frame, text="Traducción al español:").pack()
            self.entry_espanol = ttk.Entry(self.respuesta_frame, width=50)
            self.entry_espanol.pack(pady=5)
            
            ttk.Label(self.respuesta_frame, text="Traducción al inglés:").pack()
            self.entry_ingles = ttk.Entry(self.respuesta_frame, width=50)
            self.entry_ingles.pack()
    
    def nueva_pregunta(self):
        """Genera una nueva pregunta"""
        self.concepto_actual = self.controller.obtener_concepto_aleatorio()
        
        # Actualizar pregunta según modo
        if self.modo == "es-en":
            self.lbl_pregunta.config(
                text=f"¿Cuál es la traducción al inglés de:\n\n\"{self.concepto_actual['espanol']}\"?"
            )
            if hasattr(self, 'entry_respuesta'):
                self.entry_respuesta.delete(0, tk.END)
                self.entry_respuesta.focus()
                
        elif self.modo == "en-es":
            self.lbl_pregunta.config(
                text=f"¿Cuál es la traducción al español de:\n\n\"{self.concepto_actual['ingles']}\"?"
            )
            if hasattr(self, 'entry_respuesta'):
                self.entry_respuesta.delete(0, tk.END)
                self.entry_respuesta.focus()
                
        elif self.modo == "griego":
            self.lbl_pregunta.config(
                text=f"Griego: {self.concepto_actual['griego']}\n\n"
                     f"Transliteración: {self.concepto_actual['transliteracion']}\n\n"
                     f"Proporcione ambas traducciones:"
            )
            if hasattr(self, 'entry_espanol'):
                self.entry_espanol.delete(0, tk.END)
                self.entry_ingles.delete(0, tk.END)
                self.entry_espanol.focus()
        
        # Ocultar información
        self.info_frame.pack_forget()
    
    def verificar_respuesta(self):
        """Verifica la respuesta del usuario"""
        if not self.concepto_actual:
            return
        
        correcto = False
        
        if self.modo == "es-en":
            respuesta = self.entry_respuesta.get().strip()
            if (self.concepto_actual['ingles'].lower() in respuesta.lower() or 
                respuesta.lower() in self.concepto_actual['ingles'].lower()):
                correcto = True
                self.entry_respuesta.config(foreground="green")
            else:
                self.entry_respuesta.config(foreground="red")
                
        elif self.modo == "en-es":
            respuesta = self.entry_respuesta.get().strip()
            if (self.concepto_actual['espanol'].lower() in respuesta.lower() or 
                respuesta.lower() in self.concepto_actual['espanol'].lower()):
                correcto = True
                self.entry_respuesta.config(foreground="green")
            else:
                self.entry_respuesta.config(foreground="red")
                
        elif self.modo == "griego":
            espanol = self.entry_espanol.get().strip()
            ingles = self.entry_ingles.get().strip()
            
            es_correcto = (self.concepto_actual['espanol'].lower() in espanol.lower() or 
                          espanol.lower() in self.concepto_actual['espanol'].lower())
            en_correcto = (self.concepto_actual['ingles'].lower() in ingles.lower() or 
                          ingles.lower() in self.concepto_actual['ingles'].lower())
            
            if es_correcto and en_correcto:
                correcto = True
                self.entry_espanol.config(foreground="green")
                self.entry_ingles.config(foreground="green")
            else:
                if es_correcto:
                    self.entry_espanol.config(foreground="green")
                else:
                    self.entry_espanol.config(foreground="red")
                
                if en_correcto:
                    self.entry_ingles.config(foreground="green")
                else:
                    self.entry_ingles.config(foreground="red")
        
        # Registrar intento
        self.controller.registrar_intento(
            self.concepto_actual["id"],
            correcto=correcto
        )
        
        # Mostrar información completa
        self.mostrar_informacion()
    
    def mostrar_informacion(self):
        """Muestra la información completa del concepto"""
        info_text = (
            f"Griego: {self.concepto_actual['griego']}\n"
            f"Transliteración: {self.concepto_actual['transliteracion']}\n"
            f"Español: {self.concepto_actual['espanol']}\n"
            f"English: {self.concepto_actual['ingles']}\n"
            f"\nExplicación: {self.concepto_actual['explicacion']}"
        )
        
        self.lbl_info.config(text=info_text)
        self.info_frame.pack(fill="x", pady=20)


class DesafioFrame(ttk.Frame):
    """Frame para modo desafío con tiempo"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.tiempo_restante = 30
        self.temporizador_activo = False
        
        # Configurar grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        barra_superior = ttk.Frame(self)
        barra_superior.grid(row=0, column=0, sticky="ew", pady=10)
        
        ttk.Button(
            barra_superior,
            text="← Menú Principal",
            command=lambda: controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left")
        
        # Panel de control
        control_frame = ttk.Frame(barra_superior)
        control_frame.pack(side="right")
        
        self.lbl_temporizador = ttk.Label(
            control_frame,
            text="30s",
            font=("Helvetica", 14, "bold"),
            foreground="red"
        )
        self.lbl_temporizador.pack(side="left", padx=10)
        
        self.lbl_puntuacion = ttk.Label(
            control_frame,
            text="Puntuación: 0",
            font=("Helvetica", 12)
        )
        self.lbl_puntuacion.pack(side="left", padx=10)
        
        # Área central
        self.centro_frame = ttk.Frame(self)
        self.centro_frame.grid(row=1, column=0, sticky="nsew", padx=50, pady=20)
        
        # Pantalla de inicio
        self.mostrar_pantalla_inicio()
    
    def mostrar_pantalla_inicio(self):
        """Muestra la pantalla de inicio del desafío"""
        # Limpiar frame
        for widget in self.centro_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(
            self.centro_frame,
            text="⚡ MODO DESAFÍO ⚡",
            style="Titulo.TLabel",
            font=("Helvetica", 20)
        ).pack(pady=20)
        
        ttk.Label(
            self.centro_frame,
            text="Responde correctamente a 5 preguntas con tiempo limitado",
            font=("Helvetica", 12)
        ).pack(pady=10)
        
        ttk.Label(
            self.centro_frame,
            text="Reglas:\n• 30 segundos por pregunta\n• Puntos dobles por respuesta completa\n• ¡La velocidad cuenta!",
            justify="center"
        ).pack(pady=20)
        
        ttk.Button(
            self.centro_frame,
            text="Comenzar Desafío",
            command=self.iniciar_desafio,
            style="BotonPrincipal.TButton"
        ).pack(pady=30)
    
    def iniciar_desafio(self):
        """Inicia un nuevo desafío"""
        # Reiniciar variables
        self.controller.puntuacion_desafio = 0
        self.controller.preguntas_desafio = random.sample(
            self.controller.conceptos, 
            min(5, len(self.controller.conceptos))
        )
        self.controller.indice_pregunta = 0
        self.tiempo_restante = 30
        
        # Mostrar primera pregunta
        self.mostrar_pregunta()
    
    def mostrar_pregunta(self):
        """Muestra la pregunta actual"""
        # Limpiar frame
        for widget in self.centro_frame.winfo_children():
            widget.destroy()
        
        if self.controller.indice_pregunta >= len(self.controller.preguntas_desafio):
            self.mostrar_resultados()
            return
        
        # Obtener pregunta actual
        pregunta = self.controller.preguntas_desafio[self.controller.indice_pregunta]
        
        # Mostrar número de pregunta
        ttk.Label(
            self.centro_frame,
            text=f"Pregunta {self.controller.indice_pregunta + 1} de {len(self.controller.preguntas_desafio)}",
            font=("Helvetica", 12, "bold")
        ).pack(pady=10)
        
        # Mostrar pregunta según tipo aleatorio
        tipo = random.choice(['espanol', 'ingles', 'griego'])
        
        if tipo == 'espanol':
            ttk.Label(
                self.centro_frame,
                text=f"¿Cuál es la traducción al inglés de:",
                font=("Helvetica", 12)
            ).pack(pady=10)
            
            ttk.Label(
                self.centro_frame,
                text=f"\"{pregunta['espanol']}\"",
                style="Concepto.TLabel"
            ).pack(pady=10)
            
            self.entry_respuesta = ttk.Entry(self.centro_frame, width=50)
            self.entry_respuesta.pack(pady=20)
            self.tipo_respuesta = 'ingles'
            
        elif tipo == 'ingles':
            ttk.Label(
                self.centro_frame,
                text=f"¿Cuál es la traducción al español de:",
                font=("Helvetica", 12)
            ).pack(pady=10)
            
            ttk.Label(
                self.centro_frame,
                text=f"\"{pregunta['ingles']}\"",
                style="Concepto.TLabel"
            ).pack(pady=10)
            
            self.entry_respuesta = ttk.Entry(self.centro_frame, width=50)
            self.entry_respuesta.pack(pady=20)
            self.tipo_respuesta = 'espanol'
            
        else:  # griego
            ttk.Label(
                self.centro_frame,
                text=f"Griego: {pregunta['griego']}",
                style="Griego.TLabel"
            ).pack(pady=10)
            
            ttk.Label(
                self.centro_frame,
                text=f"Transliteración: {pregunta['transliteracion']}",
                font=("Courier", 12)
            ).pack(pady=10)
            
            ttk.Label(
                self.centro_frame,
                text="Proporcione ambas traducciones:",
                font=("Helvetica", 12)
            ).pack(pady=10)
            
            ttk.Label(self.centro_frame, text="Español:").pack()
            self.entry_espanol = ttk.Entry(self.centro_frame, width=50)
            self.entry_espanol.pack(pady=5)
            
            ttk.Label(self.centro_frame, text="Inglés:").pack()
            self.entry_ingles = ttk.Entry(self.centro_frame, width=50)
            self.entry_ingles.pack(pady=5)
            
            self.tipo_respuesta = 'ambos'
        
        # Guardar datos de la pregunta
        self.pregunta_actual = pregunta
        self.tipo_pregunta = tipo
        
        # Botón de respuesta
        ttk.Button(
            self.centro_frame,
            text="Responder",
            command=self.verificar_respuesta_desafio
        ).pack(pady=20)
        
        # Iniciar temporizador
        self.iniciar_temporizador()
    
    def iniciar_temporizador(self):
        """Inicia el temporizador para la pregunta actual"""
        self.temporizador_activo = True
        self.actualizar_temporizador()
    
    def actualizar_temporizador(self):
        """Actualiza el temporizador cada segundo"""
        if not self.temporizador_activo:
            return
        
        self.tiempo_restante -= 1
        self.lbl_temporizador.config(text=f"{self.tiempo_restante}s")
        
        # Cambiar color según tiempo
        if self.tiempo_restante <= 10:
            self.lbl_temporizador.config(foreground="red")
        elif self.tiempo_restante <= 20:
            self.lbl_temporizador.config(foreground="orange")
        else:
            self.lbl_temporizador.config(foreground="green")
        
        if self.tiempo_restante <= 0:
            self.temporizador_activo = False
            messagebox.showwarning("Tiempo agotado", "¡Se acabó el tiempo!")
            self.siguiente_pregunta()
        else:
            # Programar siguiente actualización
            self.after(1000, self.actualizar_temporizador)
    
    def verificar_respuesta_desafio(self):
        """Verifica la respuesta en modo desafío"""
        self.temporizador_activo = False
        
        puntos = 0
        correcto = False
        
        if self.tipo_respuesta in ['espanol', 'ingles']:
            respuesta = self.entry_respuesta.get().strip()
            correcta = self.pregunta_actual[self.tipo_respuesta]
            
            if correcta.lower() in respuesta.lower() or respuesta.lower() in correcta.lower():
                puntos = 10
                correcto = True
        else:  # ambos
            espanol = self.entry_espanol.get().strip()
            ingles = self.entry_ingles.get().strip()
            
            es_correcto = (self.pregunta_actual['espanol'].lower() in espanol.lower() or 
                          espanol.lower() in self.pregunta_actual['espanol'].lower())
            en_correcto = (self.pregunta_actual['ingles'].lower() in ingles.lower() or 
                          ingles.lower() in self.pregunta_actual['ingles'].lower())
            
            if es_correcto and en_correcto:
                puntos = 20
                correcto = True
            elif es_correcto or en_correcto:
                puntos = 10
        
        # Actualizar puntuación
        self.controller.puntuacion_desafio += puntos
        self.lbl_puntuacion.config(
            text=f"Puntuación: {self.controller.puntuacion_desafio}"
        )
        
        # Registrar intento
        self.controller.registrar_intento(
            self.pregunta_actual["id"],
            correcto=correcto
        )
        
        # Mostrar feedback
        if puntos > 0:
            messagebox.showinfo("¡Correcto!", f"+{puntos} puntos")
        else:
            messagebox.showinfo("Incorrecto", "Mejor suerte en la siguiente")
        
        # Siguiente pregunta
        self.siguiente_pregunta()
    
    def siguiente_pregunta(self):
        """Pasa a la siguiente pregunta"""
        self.controller.indice_pregunta += 1
        self.tiempo_restante = 30
        self.mostrar_pregunta()
    
    def mostrar_resultados(self):
        """Muestra los resultados finales del desafío"""
        # Limpiar frame
        for widget in self.centro_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(
            self.centro_frame,
            text="🏆 DESAFÍO COMPLETADO 🏆",
            style="Titulo.TLabel",
            font=("Helvetica", 20)
        ).pack(pady=20)
        
        puntuacion = self.controller.puntuacion_desafio
        max_puntos = len(self.controller.preguntas_desafio) * 20
        
        ttk.Label(
            self.centro_frame,
            text=f"Puntuación final: {puntuacion}/{max_puntos}",
            font=("Helvetica", 16, "bold")
        ).pack(pady=10)
        
        porcentaje = (puntuacion / max_puntos) * 100
        
        # Mostrar mensaje según puntuación
        if porcentaje >= 90:
            mensaje = "¡EXCELENTE! Dominio total"
            color = "green"
        elif porcentaje >= 70:
            mensaje = "¡MUY BIEN! Buen conocimiento"
            color = "blue"
        elif porcentaje >= 50:
            mensaje = "APROBADO. Sigue practicando"
            color = "orange"
        else:
            mensaje = "Necesitas más práctica"
            color = "red"
        
        ttk.Label(
            self.centro_frame,
            text=mensaje,
            foreground=color,
            font=("Helvetica", 14)
        ).pack(pady=10)
        
        # Botones
        botones_frame = ttk.Frame(self.centro_frame)
        botones_frame.pack(pady=30)
        
        ttk.Button(
            botones_frame,
            text="Nuevo Desafío",
            command=self.iniciar_desafio
        ).pack(side="left", padx=10)
        
        ttk.Button(
            botones_frame,
            text="Menú Principal",
            command=lambda: self.controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left", padx=10)


class FrasesFrame(ttk.Frame):
    """Frame para creación de frases personalizadas"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configurar grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        barra_superior = ttk.Frame(self)
        barra_superior.grid(row=0, column=0, sticky="ew", pady=10)
        
        ttk.Button(
            barra_superior,
            text="← Menú Principal",
            command=lambda: controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left")
        
        # Panel principal con dos columnas
        main_frame = ttk.Frame(self)
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        # Columna izquierda: Selección de concepto
        izquierda = ttk.LabelFrame(main_frame, text="Seleccionar Concepto", padding=10)
        izquierda.pack(side="left", fill="both", expand=True, padx=10)
        
        # Búsqueda
        ttk.Label(izquierda, text="Buscar concepto:").pack(anchor="w", pady=(0, 5))
        self.entry_busqueda = ttk.Entry(izquierda)
        self.entry_busqueda.pack(fill="x", pady=(0, 10))
        self.entry_busqueda.bind("<KeyRelease>", self.buscar_conceptos)
        
        ttk.Button(
            izquierda,
            text="Buscar",
            command=self.buscar_conceptos
        ).pack(pady=(0, 10))
        
        # Lista de conceptos
        self.lista_conceptos = tk.Listbox(izquierda, height=15)
        self.lista_conceptos.pack(fill="both", expand=True, pady=(0, 10))
        self.lista_conceptos.bind("<<ListboxSelect>>", self.seleccionar_concepto)
        
        # Cargar todos los conceptos
        self.conceptos_filtrados = controller.conceptos
        self.actualizar_lista()
        
        # Columna derecha: Creación de frases
        derecha = ttk.LabelFrame(main_frame, text="Crear Frases", padding=10)
        derecha.pack(side="right", fill="both", expand=True, padx=10)
        
        # Información del concepto seleccionado
        self.lbl_concepto_seleccionado = ttk.Label(
            derecha,
            text="Ningún concepto seleccionado",
            style="Subtitulo.TLabel"
        )
        self.lbl_concepto_seleccionado.pack(anchor="w", pady=(0, 10))
        
        # Frase en español
        ttk.Label(derecha, text="Frase en Español:").pack(anchor="w", pady=(0, 5))
        self.text_espanol = scrolledtext.ScrolledText(derecha, height=5)
        self.text_espanol.pack(fill="x", pady=(0, 15))
        
        # Frase en inglés
        ttk.Label(derecha, text="Frase en Inglés:").pack(anchor="w", pady=(0, 5))
        self.text_ingles = scrolledtext.ScrolledText(derecha, height=5)
        self.text_ingles.pack(fill="x", pady=(0, 15))
        
        # Botones
        botones_frame = ttk.Frame(derecha)
        botones_frame.pack(pady=10)
        
        ttk.Button(
            botones_frame,
            text="Guardar Frases",
            command=self.guardar_frases_personalizadas
        ).pack(side="left", padx=5)
        
        ttk.Button(
            botones_frame,
            text="Limpiar",
            command=self.limpiar_campos
        ).pack(side="left", padx=5)
        
        # Historial de frases recientes
        historial_frame = ttk.LabelFrame(main_frame, text="Frases Recientes", padding=10)
        historial_frame.pack(side="bottom", fill="x", pady=20)
        
        self.text_historial = scrolledtext.ScrolledText(historial_frame, height=6)
        self.text_historial.pack(fill="x")
        self.actualizar_historial()
    
    def actualizar_lista(self):
        """Actualiza la lista de conceptos"""
        self.lista_conceptos.delete(0, tk.END)
        for concepto in self.conceptos_filtrados:
            texto = f"{concepto['transliteracion']} - {concepto['espanol']}"
            self.lista_conceptos.insert(tk.END, texto)
    
    def buscar_conceptos(self, event=None):
        """Filtra la lista de conceptos según búsqueda"""
        busqueda = self.entry_busqueda.get().lower()
        
        if not busqueda:
            self.conceptos_filtrados = self.controller.conceptos
        else:
            self.conceptos_filtrados = [
                c for c in self.controller.conceptos
                if (busqueda in c['transliteracion'].lower() or 
                    busqueda in c['espanol'].lower() or 
                    busqueda in c['ingles'].lower() or 
                    busqueda in c['griego'].lower())
            ]
        
        self.actualizar_lista()
    
    def seleccionar_concepto(self, event):
        """Selecciona un concepto de la lista"""
        seleccion = self.lista_conceptos.curselection()
        if seleccion:
            indice = seleccion[0]
            if indice < len(self.conceptos_filtrados):
                self.concepto_actual = self.conceptos_filtrados[indice]
                
                # Mostrar información
                texto = (
                    f"Griego: {self.concepto_actual['griego']}\n"
                    f"Transliteración: {self.concepto_actual['transliteracion']}\n"
                    f"Español: {self.concepto_actual['espanol']}\n"
                    f"English: {self.concepto_actual['ingles']}"
                )
                self.lbl_concepto_seleccionado.config(text=texto)
    
    def guardar_frases_personalizadas(self):
        """Guarda las frases personalizadas"""
        if not hasattr(self, 'concepto_actual') or not self.concepto_actual:
            messagebox.showwarning("Advertencia", "Selecciona un concepto primero")
            return
        
        frase_es = self.text_espanol.get(1.0, tk.END).strip()
        frase_en = self.text_ingles.get(1.0, tk.END).strip()
        
        if not frase_es or not frase_en:
            messagebox.showwarning("Advertencia", "Escribe frases en ambos idiomas")
            return
        
        # Guardar en historial
        registro = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'concepto': self.concepto_actual['transliteracion'],
            'frase_espanol': frase_es,
            'frase_ingles': frase_en,
            'tipo': 'personalizada'
        }
        
        historial = self.controller.estadisticas.get('historial', [])
        historial.append(registro)
        self.controller.estadisticas['historial'] = historial
        
        # Guardar en archivo
        with open('frases_personalizadas.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n[{registro['fecha']}]\n")
            f.write(f"Concepto: {registro['concepto']}\n")
            f.write(f"Español: {frase_es}\n")
            f.write(f"English: {frase_en}\n")
            f.write("-" * 50 + "\n")
        
        messagebox.showinfo("Éxito", "Frases guardadas correctamente")
        
        # Actualizar historial y limpiar
        self.actualizar_historial()
        self.limpiar_campos()
    
    def limpiar_campos(self):
        """Limpia los campos de texto"""
        self.text_espanol.delete(1.0, tk.END)
        self.text_ingles.delete(1.0, tk.END)
        self.lista_conceptos.selection_clear(0, tk.END)
        self.lbl_concepto_seleccionado.config(text="Ningún concepto seleccionado")
        if hasattr(self, 'concepto_actual'):
            delattr(self, 'concepto_actual')
    
    def actualizar_historial(self):
        """Actualiza el historial de frases"""
        self.text_historial.delete(1.0, tk.END)
        
        historial = self.controller.estadisticas.get('historial', [])
        historial_reciente = historial[-5:]  # Últimas 5
        
        for registro in historial_reciente:
            if 'frase_espanol' in registro:
                self.text_historial.insert(tk.END, f"[{registro['fecha']}]\n")
                self.text_historial.insert(tk.END, f"Concepto: {registro['concepto']}\n")
                self.text_historial.insert(tk.END, f"Español: {registro['frase_espanol'][:50]}...\n")
                self.text_historial.insert(tk.END, f"English: {registro['frase_ingles'][:50]}...\n")
                self.text_historial.insert(tk.END, "-" * 40 + "\n")


class ConceptosFrame(ttk.Frame):
    """Frame para ver todos los conceptos"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configurar grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        barra_superior = ttk.Frame(self)
        barra_superior.grid(row=0, column=0, sticky="ew", pady=10)
        
        ttk.Button(
            barra_superior,
            text="← Menú Principal",
            command=lambda: controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left")
        
        # Filtros
        filtros_frame = ttk.Frame(barra_superior)
        filtros_frame.pack(side="right")
        
        ttk.Label(filtros_frame, text="Filtrar por categoría:").pack(side="left", padx=5)
        
        self.categoria_var = tk.StringVar(value="Todas")
        categorias = ["Todas"] + sorted(set(c["categoria"] for c in controller.conceptos))
        
        self.combo_categorias = ttk.Combobox(
            filtros_frame,
            textvariable=self.categoria_var,
            values=categorias,
            state="readonly",
            width=15
        )
        self.combo_categorias.pack(side="left", padx=5)
        self.combo_categorias.bind("<<ComboboxSelected>>", self.filtrar_conceptos)
        
        # Área principal con Treeview
        main_frame = ttk.Frame(self)
        main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Crear Treeview con scrollbar
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill="both", expand=True)
        
        # Scrollbars
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        vsb.pack(side="right", fill="y")
        
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        hsb.pack(side="bottom", fill="x")
        
        # Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Griego", "Transliteracion", "Espanol", "Ingles", "Categoria"),
            show="headings",
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set,
            height=20
        )
        
        # Configurar columnas
        columnas = [
            ("ID", 50),
            ("Griego", 150),
            ("Transliteracion", 150),
            ("Espanol", 200),
            ("Ingles", 200),
            ("Categoria", 100)
        ]
        
        for col, width in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, minwidth=50)
        
        # Configurar scrollbars
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        self.tree.pack(fill="both", expand=True)
        
        # Doble click para ver detalles
        self.tree.bind("<Double-1>", self.mostrar_detalles)
        
        # Botón de detalles
        ttk.Button(
            main_frame,
            text="Ver Detalles del Concepto Seleccionado",
            command=self.mostrar_detalles
        ).pack(pady=10)
        
        # Cargar datos
        self.cargar_conceptos()
    
    def cargar_conceptos(self, filtro_categoria="Todas"):
        """Carga los conceptos en el Treeview"""
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Filtrar conceptos
        if filtro_categoria == "Todas":
            conceptos = self.controller.conceptos
        else:
            conceptos = [c for c in self.controller.conceptos if c["categoria"] == filtro_categoria]
        
        # Insertar datos
        for concepto in conceptos:
            self.tree.insert("", "end", values=(
                concepto["id"],
                concepto["griego"],
                concepto["transliteracion"],
                concepto["espanol"],
                concepto["ingles"],
                concepto["categoria"]
            ))
        
        # Mostrar contador
        total = len(self.controller.conceptos)
        filtrados = len(conceptos)
        self.tree.heading("ID", text=f"ID ({filtrados}/{total})")
    
    def filtrar_conceptos(self, event=None):
        """Filtra los conceptos por categoría"""
        categoria = self.categoria_var.get()
        self.cargar_conceptos(categoria)
    
    def mostrar_detalles(self, event=None):
        """Muestra los detalles del concepto seleccionado"""
        seleccion = self.tree.selection()
        if not seleccion:
            return
        
        item = seleccion[0]
        valores = self.tree.item(item, "values")
        
        # Encontrar el concepto completo
        concepto_id = int(valores[0])
        concepto = next((c for c in self.controller.conceptos if c["id"] == concepto_id), None)
        
        if concepto:
            detalles = (
                f"ID: {concepto['id']}\n\n"
                f"Griego: {concepto['griego']}\n\n"
                f"Transliteración: {concepto['transliteracion']}\n\n"
                f"Español: {concepto['espanol']}\n\n"
                f"English: {concepto['ingles']}\n\n"
                f"Categoría: {concepto['categoria']}\n\n"
                f"Explicación: {concepto['explicacion']}"
            )
            
            # Crear ventana de diálogo
            dialog = tk.Toplevel(self)
            dialog.title(f"Detalles: {concepto['transliteracion']}")
            dialog.geometry("500x400")
            dialog.transient(self)
            dialog.grab_set()
            
            # Texto con scroll
            text_frame = ttk.Frame(dialog)
            text_frame.pack(fill="both", expand=True, padx=10, pady=10)
            
            text_widget = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD)
            text_widget.pack(fill="both", expand=True)
            text_widget.insert(1.0, detalles)
            text_widget.config(state="disabled")
            
            # Botón cerrar
            ttk.Button(dialog, text="Cerrar", command=dialog.destroy).pack(pady=10)


class EstadisticasFrame(ttk.Frame):
    """Frame para mostrar estadísticas"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configurar grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        barra_superior = ttk.Frame(self)
        barra_superior.grid(row=0, column=0, sticky="ew", pady=10)
        
        ttk.Button(
            barra_superior,
            text="← Menú Principal",
            command=lambda: controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left")
        
        ttk.Button(
            barra_superior,
            text="Actualizar",
            command=self.actualizar_estadisticas
        ).pack(side="right")
        
        # Área principal
        main_frame = ttk.Frame(self)
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        # Crear notebook para pestañas
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill="both", expand=True)
        
        # Pestaña 1: Resumen general
        tab_resumen = ttk.Frame(notebook)
        notebook.add(tab_resumen, text="Resumen General")
        self.crear_pestaña_resumen(tab_resumen)
        
        # Pestaña 2: Progreso por categoría
        tab_categorias = ttk.Frame(notebook)
        notebook.add(tab_categorias, text="Por Categoría")
        self.crear_pestaña_categorias(tab_categorias)
        
        # Pestaña 3: Historial de actividad
        tab_historial = ttk.Frame(notebook)
        notebook.add(tab_historial, text="Historial")
        self.crear_pestaña_historial(tab_historial)
        
        # Pestaña 4: Gráficos
        tab_graficos = ttk.Frame(notebook)
        notebook.add(tab_graficos, text="Gráficos")
        self.crear_pestaña_graficos(tab_graficos)
    
    def crear_pestaña_resumen(self, parent):
        """Crea la pestaña de resumen general"""
        # Frame principal con scroll
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Datos
        total_conceptos = len(self.controller.conceptos)
        practicados = len(self.controller.estadisticas.get('conceptos_practicados', set()))
        porcentaje_practicados = (practicados / total_conceptos * 100) if total_conceptos > 0 else 0
        
        intentos = self.controller.estadisticas.get('intentos', 0)
        aciertos = self.controller.estadisticas.get('aciertos', 0)
        total_respuestas = intentos * 2
        porcentaje_aciertos = (aciertos / total_respuestas * 100) if total_respuestas > 0 else 0
        
        # Título
        ttk.Label(
            scrollable_frame,
            text="📊 ESTADÍSTICAS DE APRENDIZAJE",
            style="Titulo.TLabel"
        ).pack(pady=20)
        
        # Tarjetas de estadísticas
        tarjetas_frame = ttk.Frame(scrollable_frame)
        tarjetas_frame.pack(pady=10)
        
        tarjetas = [
            ("Conceptos Practicados", f"{practicados}/{total_conceptos}", f"{porcentaje_practicados:.1f}%"),
            ("Intentos Totales", str(intentos), "Ejercicios"),
            ("Respuestas Correctas", f"{aciertos}/{total_respuestas}", f"{porcentaje_aciertos:.1f}%"),
            ("Tasa de Éxito", f"{porcentaje_aciertos:.1f}%", "Promedio")
        ]
        
        for i, (titulo, valor, subtitulo) in enumerate(tarjetas):
            if i % 2 == 0:
                frame_fila = ttk.Frame(tarjetas_frame)
                frame_fila.pack(pady=5)
            
            tarjeta = ttk.Frame(frame_fila, relief="solid", borderwidth=1)
            tarjeta.pack(side="left", padx=5, fill="x", expand=True)
            
            ttk.Label(tarjeta, text=titulo, font=("Helvetica", 10)).pack(pady=5)
            ttk.Label(tarjeta, text=valor, font=("Helvetica", 16, "bold")).pack(pady=5)
            ttk.Label(tarjeta, text=subtitulo, font=("Helvetica", 9)).pack(pady=5)
        
        # Barra de progreso para conceptos practicados
        ttk.Label(scrollable_frame, text="Progreso general de conceptos:").pack(pady=(20, 5))
        
        progress = ttk.Progressbar(
            scrollable_frame,
            length=400,
            mode='determinate',
            maximum=100
        )
        progress.pack(pady=5)
        progress['value'] = porcentaje_practicados
        
        ttk.Label(
            scrollable_frame,
            text=f"{porcentaje_practicados:.1f}% completado"
        ).pack(pady=5)
        
        # Distribución por categoría
        ttk.Label(
            scrollable_frame,
            text="Distribución por Categoría:",
            style="Subtitulo.TLabel"
        ).pack(pady=(30, 10))
        
        categorias = {}
        for concepto in self.controller.conceptos:
            cat = concepto['categoria']
            if cat not in categorias:
                categorias[cat] = {'total': 0, 'practicados': 0}
            categorias[cat]['total'] += 1
        
        # Contar practicados por categoría
        for concepto_id in self.controller.estadisticas.get('conceptos_practicados', set()):
            concepto = next((c for c in self.controller.conceptos if c['id'] == concepto_id), None)
            if concepto:
                categorias[concepto['categoria']]['practicados'] += 1
        
        for categoria, datos in categorias.items():
            frame_cat = ttk.Frame(scrollable_frame)
            frame_cat.pack(fill="x", pady=2)
            
            ttk.Label(frame_cat, text=categoria, width=20).pack(side="left")
            
            progress_cat = ttk.Progressbar(
                frame_cat,
                length=300,
                mode='determinate'
            )
            progress_cat.pack(side="left", padx=5)
            
            porcentaje = (datos['practicados'] / datos['total'] * 100) if datos['total'] > 0 else 0
            progress_cat['value'] = porcentaje
            
            ttk.Label(
                frame_cat,
                text=f"{datos['practicados']}/{datos['total']} ({porcentaje:.1f}%)"
            ).pack(side="left", padx=5)
    
    def crear_pestaña_categorias(self, parent):
        """Crea la pestaña de progreso por categoría"""
        ttk.Label(
            parent,
            text="Progreso detallado por categoría",
            style="Subtitulo.TLabel"
        ).pack(pady=20)
        
        # Obtener estadísticas por categoría
        categorias = {}
        for concepto in self.controller.conceptos:
            cat = concepto['categoria']
            if cat not in categorias:
                categorias[cat] = {
                    'total': 0,
                    'practicados': 0,
                    'intentos': 0,
                    'aciertos': 0
                }
            categorias[cat]['total'] += 1
        
        # Calcular intentos y aciertos por categoría
        for concepto_id in self.controller.estadisticas.get('conceptos_practicados', set()):
            concepto = next((c for c in self.controller.conceptos if c['id'] == concepto_id), None)
            if concepto:
                categorias[concepto['categoria']]['practicados'] += 1
        
        # Treeview para mostrar datos
        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        vsb.pack(side="right", fill="y")
        
        # Treeview
        tree = ttk.Treeview(
            tree_frame,
            columns=("Categoria", "Total", "Practicados", "%", "Intento", "Acierto", "% Acierto"),
            show="headings",
            yscrollcommand=vsb.set,
            height=10
        )
        
        vsb.config(command=tree.yview)
        
        # Configurar columnas
        columnas = [
            ("Categoria", 150),
            ("Total", 80),
            ("Practicados", 100),
            ("%", 80),
            ("Intento", 80),
            ("Acierto", 80),
            ("% Acierto", 100)
        ]
        
        for col, width in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=width)
        
        tree.pack(fill="both", expand=True)
        
        # Insertar datos
        for categoria, datos in categorias.items():
            porcentaje_pract = (datos['practicados'] / datos['total'] * 100) if datos['total'] > 0 else 0
            porcentaje_acierto = (datos['aciertos'] / (datos['intentos'] * 2) * 100) if datos['intentos'] > 0 else 0
            
            tree.insert("", "end", values=(
                categoria,
                datos['total'],
                datos['practicados'],
                f"{porcentaje_pract:.1f}%",
                datos['intentos'],
                datos['aciertos'],
                f"{porcentaje_acierto:.1f}%"
            ))
    
    def crear_pestaña_historial(self, parent):
        """Crea la pestaña de historial de actividad"""
        ttk.Label(
            parent,
            text="Historial de Actividad Reciente",
            style="Subtitulo.TLabel"
        ).pack(pady=20)
        
        # Área de texto con scroll
        text_frame = ttk.Frame(parent)
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.text_historial = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD)
        self.text_historial.pack(fill="both", expand=True)
        
        # Botones
        botones_frame = ttk.Frame(parent)
        botones_frame.pack(pady=10)
        
        ttk.Button(
            botones_frame,
            text="Actualizar Historial",
            command=self.actualizar_historial_texto
        ).pack(side="left", padx=5)
        
        ttk.Button(
            botones_frame,
            text="Exportar a Archivo",
            command=self.exportar_historial
        ).pack(side="left", padx=5)
        
        # Cargar historial inicial
        self.actualizar_historial_texto()
    
    def actualizar_historial_texto(self):
        """Actualiza el texto del historial"""
        self.text_historial.delete(1.0, tk.END)
        
        historial = self.controller.estadisticas.get('historial', [])
        
        if not historial:
            self.text_historial.insert(tk.END, "No hay actividad registrada todavía.")
            return
        
        for registro in reversed(historial[-20:]):  # Últimas 20 actividades
            self.text_historial.insert(tk.END, f"[{registro.get('fecha', 'Sin fecha')}]\n")
            
            if 'tipo' in registro and registro['tipo'] == 'examen_final':
                self.text_historial.insert(tk.END, f"Examen Final - Puntuación: {registro.get('puntuacion', 0)}/100\n")
            elif 'frase_espanol' in registro:
                self.text_historial.insert(tk.END, f"Concepto: {registro.get('concepto', 'Desconocido')}\n")
                self.text_historial.insert(tk.END, f"Frase Español: {registro.get('frase_espanol', '')}\n")
                self.text_historial.insert(tk.END, f"Frase Inglés: {registro.get('frase_ingles', '')}\n")
            else:
                self.text_historial.insert(tk.END, f"Actividad: {registro.get('tipo', 'Ejercicio')}\n")
            
            self.text_historial.insert(tk.END, "-" * 60 + "\n\n")
    
    def exportar_historial(self):
        """Exporta el historial a un archivo"""
        try:
            with open('historial_completo.txt', 'w', encoding='utf-8') as f:
                historial = self.controller.estadisticas.get('historial', [])
                for registro in historial:
                    f.write(f"{registro.get('fecha', 'Sin fecha')}\n")
                    f.write(f"{registro}\n")
                    f.write("-" * 40 + "\n")
            
            messagebox.showinfo("Éxito", "Historial exportado a 'historial_completo.txt'")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {str(e)}")
    
    def crear_pestaña_graficos(self, parent):
        """Crea la pestaña de gráficos (simulados con texto)"""
        ttk.Label(
            parent,
            text="Gráficos de Progreso",
            style="Subtitulo.TLabel"
        ).pack(pady=20)
        
        # Simular gráficos con texto
        text_frame = ttk.Frame(parent)
        text_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        info_text = (
            "Gráficos disponibles en versión avanzada:\n\n"
            "1. Evolución temporal de aciertos\n"
            "2. Distribución por categoría (tarta)\n"
            "3. Progreso semanal\n"
            "4. Comparativa entre modos de ejercicio\n\n"
            "Para gráficos interactivos, ejecuta la versión\n"
            "web con librerías como Plotly o Matplotlib."
        )
        
        ttk.Label(
            text_frame,
            text=info_text,
            justify="center",
            font=("Helvetica", 11)
        ).pack(expand=True)
    
    def actualizar_estadisticas(self):
        """Actualiza todas las estadísticas"""
        self.actualizar_barra_estado()
        self.crear_pestaña_resumen(self)  # Esto recrearía la pestaña
        messagebox.showinfo("Actualizado", "Estadísticas actualizadas")


class ExamenFrame(ttk.Frame):
    """Frame para examen final"""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configurar grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Barra superior
        barra_superior = ttk.Frame(self)
        barra_superior.grid(row=0, column=0, sticky="ew", pady=10)
        
        ttk.Button(
            barra_superior,
            text="← Menú Principal",
            command=lambda: controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left")
        
        # Área central inicial
        self.centro_frame = ttk.Frame(self)
        self.centro_frame.grid(row=1, column=0, sticky="nsew", padx=50, pady=50)
        
        self.mostrar_pantalla_inicio()
    
    def mostrar_pantalla_inicio(self):
        """Muestra la pantalla de inicio del examen"""
        # Limpiar frame
        for widget in self.centro_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(
            self.centro_frame,
            text="🎯 EXAMEN FINAL COMPRENSIVO 🎯",
            style="Titulo.TLabel",
            font=("Helvetica", 20)
        ).pack(pady=20)
        
        ttk.Label(
            self.centro_frame,
            text="Demuestra tu dominio completo de los conceptos griegos",
            font=("Helvetica", 12)
        ).pack(pady=10)
        
        info_text = (
            "El examen consta de 10 preguntas de diferentes tipos:\n\n"
            "• Traducciones (español ↔ inglés ↔ griego)\n"
            "• Creación de frases en contexto\n"
            "• Identificación de conceptos\n"
            "• Preguntas teóricas\n\n"
            "Cada pregunta vale 10 puntos\n"
            "Puntuación máxima: 100 puntos\n"
            "Tiempo estimado: 15-20 minutos"
        )
        
        ttk.Label(
            self.centro_frame,
            text=info_text,
            justify="center",
            font=("Helvetica", 11)
        ).pack(pady=20)
        
        ttk.Button(
            self.centro_frame,
            text="Comenzar Examen",
            command=self.iniciar_examen,
            style="BotonPrincipal.TButton"
        ).pack(pady=30)
    
    def iniciar_examen(self):
        """Inicia un nuevo examen"""
        # Inicializar variables del examen
        self.preguntas_examen = []
        self.respuestas_usuario = []
        self.pregunta_actual = 0
        self.puntuacion_examen = 0
        
        # Generar 10 preguntas aleatorias
        conceptos_disponibles = self.controller.conceptos.copy()
        random.shuffle(conceptos_disponibles)
        
        for i in range(min(10, len(conceptos_disponibles))):
            concepto = conceptos_disponibles[i]
            tipo = random.choice(['traduccion', 'frase_es', 'frase_en', 'completa'])
            
            self.preguntas_examen.append({
                'concepto': concepto,
                'tipo': tipo,
                'puntos': 10
            })
        
        # Mostrar primera pregunta
        self.mostrar_pregunta_examen()
    
    def mostrar_pregunta_examen(self):
        """Muestra la pregunta actual del examen"""
        # Limpiar frame
        for widget in self.centro_frame.winfo_children():
            widget.destroy()
        
        if self.pregunta_actual >= len(self.preguntas_examen):
            self.mostrar_resultados_examen()
            return
        
        pregunta = self.preguntas_examen[self.pregunta_actual]
        concepto = pregunta['concepto']
        
        # Mostrar número de pregunta
        ttk.Label(
            self.centro_frame,
            text=f"Pregunta {self.pregunta_actual + 1} de {len(self.preguntas_examen)}",
            font=("Helvetica", 12, "bold")
        ).pack(pady=10)
        
        # Mostrar según tipo
        if pregunta['tipo'] == 'traduccion':
            direccion = random.choice(['es-en', 'en-es', 'griego'])
            
            if direccion == 'es-en':
                ttk.Label(
                    self.centro_frame,
                    text=f"Traduce al inglés:\n\n\"{concepto['espanol']}\"",
                    font=("Helvetica", 12)
                ).pack(pady=20)
                
                self.entry_respuesta = ttk.Entry(self.centro_frame, width=50)
                self.entry_respuesta.pack(pady=10)
                
            elif direccion == 'en-es':
                ttk.Label(
                    self.centro_frame,
                    text=f"Traduce al español:\n\n\"{concepto['ingles']}\"",
                    font=("Helvetica", 12)
                ).pack(pady=20)
                
                self.entry_respuesta = ttk.Entry(self.centro_frame, width=50)
                self.entry_respuesta.pack(pady=10)
                
            else:  # griego
                ttk.Label(
                    self.centro_frame,
                    text=f"Griego: {concepto['griego']}",
                    style="Griego.TLabel"
                ).pack(pady=10)
                
                ttk.Label(
                    self.centro_frame,
                    text=f"Transliteración: {concepto['transliteracion']}",
                    font=("Helvetica", 12)
                ).pack(pady=10)
                
                ttk.Label(
                    self.centro_frame,
                    text="Proporciona ambas traducciones:",
                    font=("Helvetica", 12)
                ).pack(pady=10)
                
                ttk.Label(self.centro_frame, text="Español:").pack()
                self.entry_espanol = ttk.Entry(self.centro_frame, width=50)
                self.entry_espanol.pack(pady=5)
                
                ttk.Label(self.centro_frame, text="Inglés:").pack()
                self.entry_ingles = ttk.Entry(self.centro_frame, width=50)
                self.entry_ingles.pack(pady=5)
        
        elif pregunta['tipo'] == 'frase_es':
            ttk.Label(
                self.centro_frame,
                text=f"Crea una frase en español usando el concepto:",
                font=("Helvetica", 12)
            ).pack(pady=10)
            
            ttk.Label(
                self.centro_frame,
                text=f"\"{concepto['transliteracion']}\" ({concepto['espanol']})",
                style="Concepto.TLabel"
            ).pack(pady=10)
            
            self.text_frase = scrolledtext.ScrolledText(self.centro_frame, height=4, width=60)
            self.text_frase.pack(pady=10)
        
        elif pregunta['tipo'] == 'frase_en':
            ttk.Label(
                self.centro_frame,
                text=f"Create an English sentence using:",
                font=("Helvetica", 12)
            ).pack(pady=10)
            
            ttk.Label(
                self.centro_frame,
                text=f"\"{concepto['transliteracion']}\" ({concepto['ingles']})",
                style="Concepto.TLabel"
            ).pack(pady=10)
            
            self.text_frase = scrolledtext.ScrolledText(self.centro_frame, height=4, width=60)
            self.text_frase.pack(pady=10)
        
        else:  # completa
            ttk.Label(
                self.centro_frame,
                text=f"Completa toda la información para:",
                font=("Helvetica", 12)
            ).pack(pady=10)
            
            ttk.Label(
                self.centro_frame,
                text=f"{concepto['griego']}",
                style="Griego.TLabel"
            ).pack(pady=10)
            
            campos_frame = ttk.Frame(self.centro_frame)
            campos_frame.pack(pady=10)
            
            ttk.Label(campos_frame, text="Transliteración:").grid(row=0, column=0, sticky="w", pady=5)
            self.entry_translit = ttk.Entry(campos_frame, width=40)
            self.entry_translit.grid(row=0, column=1, padx=5)
            
            ttk.Label(campos_frame, text="Español:").grid(row=1, column=0, sticky="w", pady=5)
            self.entry_espanol = ttk.Entry(campos_frame, width=40)
            self.entry_espanol.grid(row=1, column=1, padx=5)
            
            ttk.Label(campos_frame, text="Inglés:").grid(row=2, column=0, sticky="w", pady=5)
            self.entry_ingles = ttk.Entry(campos_frame, width=40)
            self.entry_ingles.grid(row=2, column=1, padx=5)
        
        # Botones de navegación
        botones_frame = ttk.Frame(self.centro_frame)
        botones_frame.pack(pady=20)
        
        if self.pregunta_actual > 0:
            ttk.Button(
                botones_frame,
                text="← Anterior",
                command=self.pregunta_anterior
            ).pack(side="left", padx=5)
        
        ttk.Button(
            botones_frame,
            text="Siguiente →",
            command=self.siguiente_pregunta_examen
        ).pack(side="left", padx=5)
    
    def siguiente_pregunta_examen(self):
        """Guarda la respuesta y pasa a la siguiente pregunta"""
        # Guardar respuesta actual
        self.guardar_respuesta_actual()
        
        # Pasar a siguiente pregunta
        self.pregunta_actual += 1
        self.mostrar_pregunta_examen()
    
    def pregunta_anterior(self):
        """Regresa a la pregunta anterior"""
        if self.pregunta_actual > 0:
            self.pregunta_actual -= 1
            self.mostrar_pregunta_examen()
    
    def guardar_respuesta_actual(self):
        """Guarda la respuesta actual del usuario"""
        if self.pregunta_actual >= len(self.preguntas_examen):
            return
        
        pregunta = self.preguntas_examen[self.pregunta_actual]
        
        # Inicializar respuesta
        respuesta = {
            'pregunta_numero': self.pregunta_actual,
            'tipo': pregunta['tipo'],
            'concepto': pregunta['concepto']['transliteracion']
        }
        
        # Guardar según tipo
        if pregunta['tipo'] == 'traduccion':
            if hasattr(self, 'entry_respuesta'):
                respuesta['respuesta'] = self.entry_respuesta.get()
            elif hasattr(self, 'entry_espanol') and hasattr(self, 'entry_ingles'):
                respuesta['respuesta_espanol'] = self.entry_espanol.get()
                respuesta['respuesta_ingles'] = self.entry_ingles.get()
        
        elif pregunta['tipo'] in ['frase_es', 'frase_en']:
            respuesta['frase'] = self.text_frase.get(1.0, tk.END).strip()
        
        else:  # completa
            respuesta['transliteracion'] = self.entry_translit.get()
            respuesta['espanol'] = self.entry_espanol.get()
            respuesta['ingles'] = self.entry_ingles.get()
        
        # Añadir a respuestas
        if len(self.respuestas_usuario) <= self.pregunta_actual:
            self.respuestas_usuario.append(respuesta)
        else:
            self.respuestas_usuario[self.pregunta_actual] = respuesta
    
    def mostrar_resultados_examen(self):
        """Muestra los resultados finales del examen"""
        # Calcular puntuación
        self.calcular_puntuacion()
        
        # Limpiar frame
        for widget in self.centro_frame.winfo_children():
            widget.destroy()
        
        ttk.Label(
            self.centro_frame,
            text="🏅 RESULTADOS DEL EXAMEN 🏅",
            style="Titulo.TLabel",
            font=("Helvetica", 20)
        ).pack(pady=20)
        
        puntuacion = self.puntuacion_examen
        max_puntos = len(self.preguntas_examen) * 10
        
        ttk.Label(
            self.centro_frame,
            text=f"Puntuación final: {puntuacion}/{max_puntos}",
            font=("Helvetica", 18, "bold")
        ).pack(pady=10)
        
        porcentaje = (puntuacion / max_puntos) * 100
        
        # Determinar calificación
        if porcentaje >= 90:
            calificacion = "SOBRESALIENTE (A)"
            mensaje = "¡Excelente dominio de los conceptos!"
            color = "green"
        elif porcentaje >= 80:
            calificacion = "NOTABLE (B)"
            mensaje = "Muy buen conocimiento"
            color = "blue"
        elif porcentaje >= 70:
            calificacion = "BIEN (C)"
            mensaje = "Buen desempeño"
            color = "orange"
        elif porcentaje >= 60:
            calificacion = "SUFICIENTE (D)"
            mensaje = "Aprobado, pero necesita practicar más"
            color = "orange"
        else:
            calificacion = "INSUFICIENTE (F)"
            mensaje = "Necesita estudiar más los conceptos"
            color = "red"
        
        ttk.Label(
            self.centro_frame,
            text=f"Calificación: {calificacion}",
            foreground=color,
            font=("Helvetica", 16)
        ).pack(pady=5)
        
        ttk.Label(
            self.centro_frame,
            text=mensaje,
            font=("Helvetica", 12)
        ).pack(pady=10)
        
        # Mostrar respuestas incorrectas
        ttk.Label(
            self.centro_frame,
            text="Revisa los conceptos que necesitas practicar:",
            style="Subtitulo.TLabel"
        ).pack(pady=(30, 10))
        
        # Frame para scroll
        scroll_frame = ttk.Frame(self.centro_frame)
        scroll_frame.pack(fill="both", expand=True, padx=20)
        
        text_revision = scrolledtext.ScrolledText(scroll_frame, height=10)
        text_revision.pack(fill="both", expand=True)
        
        # Añadir conceptos para revisión
        for i, (pregunta, respuesta) in enumerate(zip(self.preguntas_examen, self.respuestas_usuario)):
            concepto = pregunta['concepto']
            
            # Verificar si la pregunta se respondió correctamente
            correcta = self.es_respuesta_correcta(pregunta, respuesta)
            
            if not correcta:
                text_revision.insert(tk.END, f"Pregunta {i+1}: {concepto['transliteracion']}\n")
                text_revision.insert(tk.END, f"  Griego: {concepto['griego']}\n")
                text_revision.insert(tk.END, f"  Español: {concepto['espanol']}\n")
                text_revision.insert(tk.END, f"  English: {concepto['ingles']}\n")
                text_revision.insert(tk.END, "-" * 40 + "\n")
        
        text_revision.config(state="disabled")
        
        # Botones
        botones_frame = ttk.Frame(self.centro_frame)
        botones_frame.pack(pady=20)
        
        ttk.Button(
            botones_frame,
            text="Nuevo Examen",
            command=self.iniciar_examen
        ).pack(side="left", padx=5)
        
        ttk.Button(
            botones_frame,
            text="Menú Principal",
            command=lambda: self.controller.mostrar_frame("MenuPrincipalFrame")
        ).pack(side="left", padx=5)
        
        # Guardar resultado en historial
        self.guardar_resultado_examen(puntuacion, porcentaje)
    
    def calcular_puntuacion(self):
        """Calcula la puntuación del examen"""
        self.puntuacion_examen = 0
        
        for i, (pregunta, respuesta) in enumerate(zip(self.preguntas_examen, self.respuestas_usuario)):
            if self.es_respuesta_correcta(pregunta, respuesta):
                self.puntuacion_examen += pregunta['puntos']
    
    def es_respuesta_correcta(self, pregunta, respuesta):
        """Determina si una respuesta es correcta"""
        concepto = pregunta['concepto']
        
        if pregunta['tipo'] == 'traduccion':
            if 'respuesta' in respuesta:
                resp = respuesta['respuesta'].lower()
                correcta = concepto['ingles'].lower() if 'es-en' in str(pregunta) else concepto['espanol'].lower()
                return correcta in resp or resp in correcta
            else:
                resp_es = respuesta.get('respuesta_espanol', '').lower()
                resp_en = respuesta.get('respuesta_ingles', '').lower()
                
                correcto_es = concepto['espanol'].lower() in resp_es or resp_es in concepto['espanol'].lower()
                correcto_en = concepto['ingles'].lower() in resp_en or resp_en in concepto['ingles'].lower()
                
                return correcto_es and correcto_en
        
        elif pregunta['tipo'] in ['frase_es', 'frase_en']:
            frase = respuesta.get('frase', '').lower()
            concepto_text = concepto['transliteracion'].lower()
            
            # Verificar si la frase contiene el concepto
            return concepto_text in frase
        
        else:  # completa
            translit = respuesta.get('transliteracion', '').lower()
            espanol = respuesta.get('espanol', '').lower()
            ingles = respuesta.get('ingles', '').lower()
            
            correcto_translit = concepto['transliteracion'].lower() == translit
            correcto_es = concepto['espanol'].lower() in espanol or espanol in concepto['espanol'].lower()
            correcto_en = concepto['ingles'].lower() in ingles or ingles in concepto['ingles'].lower()
            
            return correcto_translit and correcto_es and correcto_en
    
    def guardar_resultado_examen(self, puntuacion, porcentaje):
        """Guarda el resultado del examen en el historial"""
        registro = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'tipo': 'examen_final',
            'puntuacion': puntuacion,
            'porcentaje': porcentaje,
            'total_preguntas': len(self.preguntas_examen)
        }
        
        historial = self.controller.estadisticas.get('historial', [])
        historial.append(registro)
        self.controller.estadisticas['historial'] = historial


# Función principal
def main():
    """Función principal para ejecutar la aplicación"""
    # Crear archivos de datos si no existen
    if not os.path.exists('conceptos_griegos.json'):
        # Datos de ejemplo
        datos_ejemplo = [
            {
                "id": 1,
                "griego": "Γνῶθι σαυτόν",
                "transliteracion": "Gnōthi seautón",
                "espanol": "Conócete a ti mismo",
                "ingles": "Know thyself",
                "categoria": "Filosofía",
                "explicacion": "Máxima délfica que invita al autoconocimiento como base de la sabiduría"
            },
            {
                "id": 2,
                "griego": "Ἀρετή",
                "transliteracion": "Aretḗ",
                "espanol": "Virtud, excelencia",
                "ingles": "Virtue, excellence",
                "categoria": "Filosofía",
                "explicacion": "Excelencia en el cumplimiento de la función propia"
            },
            {
                "id": 3,
                "griego": "Λόγος",
                "transliteracion": "Lógos",
                "espanol": "Razón, palabra, principio",
                "ingles": "Reason, word, principle",
                "categoria": "Filosofía",
                "explicacion": "Principio racional que ordena el cosmos"
            }
        ]
        
        with open('conceptos_griegos.json', 'w', encoding='utf-8') as f:
            json.dump(datos_ejemplo, f, ensure_ascii=False, indent=2)
    
    # Ejecutar aplicación
    app = AplicacionGriego()
    app.mainloop()

if __name__ == "__main__":
    main()
