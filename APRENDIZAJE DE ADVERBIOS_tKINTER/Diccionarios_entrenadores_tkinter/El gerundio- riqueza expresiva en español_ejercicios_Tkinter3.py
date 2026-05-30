import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
from textwrap import dedent

class GerundioMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Master Gerundios - Spanish Tutor Pro")
        self.root.geometry("1000x800")
        
        # Configuración inicial
        self.categorias = {
            1: {
                "nombre": "Instantaneidad",
                "ejemplos": [
                    "Estoy *escribiendo* un correo ahora mismo.",
                    "Mi hermana está *cocinando* la cena.",
                    "¡Mira! Los niños están *jugando* en el parque.",
                    "¿Por qué estás *llorando*? ¿Pasó algo?",
                    "El profesor está *explicando* el tema ahora."
                ],
                "practicadas": 0,
                "explicacion": "Acciones en este momento exacto"
            },
            2: {
                "nombre": "Duración",
                "ejemplos": [
                    "Llevo horas *estudiando* para el examen.",
                    "Estamos *renovando* la casa desde enero.",
                    "Siguen *trabajando* en el proyecto.",
                    "El paciente sigue *mejorando* día a día.",
                    "Estoy *leyendo* la trilogía completa."
                ],
                "practicadas": 0,
                "explicacion": "Acciones en proceso prolongado"
            },
            3: {
                "nombre": "Repetición",
                "ejemplos": [
                    "Siempre está *quejándose* de todo.",
                    "Mi vecino pasa *talando* árboles.",
                    "El reloj sigue *dando* la hora mal.",
                    "Está *enviando* mensajes sin parar.",
                    "El bebé sigue *tirando* la comida."
                ],
                "practicadas": 0,
                "explicacion": "Acciones repetitivas o habituales"
            },
            4: {
                "nombre": "Percepción",
                "ejemplos": [
                    "Vi a Juan *corriendo* hacia el tren.",
                    "Escuché al bebé *riéndose*.",
                    "Olí algo *quemándose* en la cocina.",
                    "Noté a María *temblando* de frío.",
                    "Descubrí a mi hijo *comiendo* chocolate."
                ],
                "practicadas": 0,
                "explicacion": "Acciones percibidas en progreso"
            },
            5: {
                "nombre": "Simultaneidad",
                "ejemplos": [
                    "Ana salió *llorando* de la habitación.",
                    "El chef prepara la salsa *cantando*.",
                    "El perro entró *arrastrando* las patas.",
                    "Los niños caminaban *recogiendo* flores.",
                    "El anciano leía *bebiendo* café."
                ],
                "practicadas": 0,
                "explicacion": "Acciones simultáneas con valor adverbial"
            },
            6: {
                "nombre": "Causalidad",
                "ejemplos": [
                    "Viendo tu esfuerzo, continuaré ayudando.",
                    "Sab iendo la verdad, decidió callar.",
                    "Oliendo humo, corrimos a evacuar.",
                    "Pensando en ti, cancelé la reunión.",
                    "Notando el error, corrigió el documento."
                ],
                "practicadas": 0,
                "explicacion": "Explicación de causas o motivos"
            },
            7: {
                "nombre": "Concesión/Condición",
                "ejemplos": [
                    "Siendo sincero, no me gusta.",
                    "Habiendo terminado, podremos descansar.",
                    "Estudiando diario, aprobarás.",
                    "Estando enfermo, igual fue.",
                    "Viviendo allá, aprenderás cultura."
                ],
                "practicadas": 0,
                "explicacion": "Expresar condiciones o concesiones"
            }
        }
        
        self.frases_reescribir = [
            "El niño lee un libro",
            "Los estudiantes hacen la tarea",
            "María cocina paella",
            "Yo escribo un poema",
            "El equipo desarrolla software",
            "Aprendo francés",
            "Los pájaros cantan",
            "El profesor explica la lección",
            "Ellos viajan por Europa",
            "Tú miras la televisión"
        ]
        
        self.puntaje_total = 0
        self.progreso = {cat: {"correctas": 0, "intentos": 0} for cat in self.categorias}
        self.frase_actual = 0
        
        # Interfaz gráfica
        self.crear_menu_principal()
        self.crear_barra_estado()
        self.crear_ayuda_gramatical()
        
    def crear_menu_principal(self):
        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        ttk.Label(self.frame_principal, 
                text="MASTER GERUNDIOS", 
                font=("Arial", 18, "bold"),
                foreground="#2c3e50").pack(pady=15)
                
        botones = [
            ("📚 Ver Categorías", self.mostrar_categorias, "#3498db"),
            ("✍️ Practicar Gerundios", self.practicar_gerundios, "#2ecc71"),
            ("🔄 Reescribir Frases", self.reescribir_frases, "#e67e22"),
            ("📊 Mi Progreso", self.mostrar_progreso, "#9b59b6"),
            ("❓ Ayuda Gramatical", self.mostrar_ayuda, "#34495e"),
            ("🚪 Salir", self.root.quit, "#e74c3c")
        ]
        
        for texto, comando, color in botones:
            btn = ttk.Button(self.frame_principal, 
                            text=texto,
                            command=comando,
                            style=f"TButton{color}")
            btn.pack(pady=7, fill=tk.X)
            self.root.option_add(f"*TButton{color}*background", color)
            self.root.option_add(f"*TButton{color}*foreground", "white")

    def crear_barra_estado(self):
        self.barra_estado = ttk.Frame(self.root)
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.label_puntaje = ttk.Label(self.barra_estado, 
                                      text=f"Puntaje: {self.puntaje_total}")
        self.label_puntaje.pack(side=tk.LEFT, padx=10)
        
        self.label_progreso = ttk.Label(self.barra_estado, 
                                       text="Progreso General: 0%")
        self.label_progreso.pack(side=tk.RIGHT, padx=10)

    def crear_ayuda_gramatical(self):
        self.help_content = dedent("""📘 Reglas Esenciales del Gerundio:
        
        1. Formación:
           - Verbos -AR: -ando (habl + ando = hablando)
           - Verbos -ER/-IR: -iendo (com + iendo = comiendo)
           - Excepciones: ir → yendo, poder → pudiendo

        2. Usos Correctos:
           ✔️ Acciones en progreso: "Estoy comiendo"
           ✔️ Simultaneidad: "Caminando habla por teléfono"
           ✔️ Causa inmediata: "Viendo el peligro, actuó"

        3. Errores Comunes:
           ❌ Usar para características permanentes: "Siendo alto, juega básquet"
           ❌ Secuencias temporales: "Habiendo comido, salió" (Mejor: "Después de comer...")
           ❌ Con verbos de estado: "Estoy sabiendo la respuesta"

        4. Consejos:
           🔹 Mantén la simultaneidad temporal
           🔹 Usa verbos de acción, no de estado
           🔹 Evita gerundios compuestos innecesarios
        """)

    def mostrar_categorias(self):
        self.ventana_categorias = tk.Toplevel()
        self.ventana_categorias.title("Categorías de Estudio")
        
        notebook = ttk.Notebook(self.ventana_categorias)
        
        for cat_id, datos in self.categorias.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=f"{datos['nombre']}")
            
            # Explicación
            ttk.Label(frame, 
                     text=f"Explicación: {datos['explicacion']}",
                     font=("Arial", 10, "italic"),
                     wraplength=400).pack(pady=10)
            
            # Ejemplos
            ttk.Label(frame, 
                     text="Ejemplos (gerundios destacados):",
                     font=("Arial", 10, "bold")).pack(pady=5)
            
            for ejemplo in datos['ejemplos']:
                ttk.Label(frame, 
                         text=ejemplo.replace('*', ''),
                         foreground="#2c3e50",
                         font=("Arial", 9)).pack(pady=2)
            
            # Botón de práctica
            ttk.Button(frame, 
                      text="Practicar esta categoría",
                      command=lambda c=cat_id: self.iniciar_practica(c)).pack(pady=10)
        
        notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.ventana_categorias.geometry("600x500")

    def practicar_gerundios(self):
        self.categoria_actual = None
        self.ventana_practica = tk.Toplevel()
        self.ventana_practica.title("Modo Práctica")
        
        self.frame_superior = ttk.Frame(self.ventana_practica)
        self.frame_superior.pack(pady=10)
        
        ttk.Label(self.frame_superior, 
                 text="Selecciona una categoría:",
                 font=("Arial", 12)).pack(side=tk.LEFT)
        
        self.combo_categorias = ttk.Combobox(self.frame_superior,
                                           values=[d["nombre"] for d in self.categorias.values()])
        self.combo_categorias.pack(side=tk.LEFT, padx=10)
        self.combo_categorias.bind("<<ComboboxSelected>>", self.actualizar_practica)
        
        self.frame_principal_practica = ttk.Frame(self.ventana_practica)
        self.frame_principal_practica.pack(pady=10)
        
        self.ventana_practica.geometry("800x600")

    def actualizar_practica(self, event):
        cat_nombre = self.combo_categorias.get()
        cat_id = [k for k, v in self.categorias.items() if v["nombre"] == cat_nombre][0]
        self.categoria_actual = cat_id
        
        for widget in self.frame_principal_practica.winfo_children():
            widget.destroy()
        
        # Ejemplos
        ttk.Label(self.frame_principal_practica, 
                 text="Ejemplos de la categoría:",
                 font=("Arial", 11, "bold")).pack(pady=5)
        
        for ejemplo in self.categorias[cat_id]["ejemplos"]:
            ttk.Label(self.frame_principal_practica,
                     text=ejemplo,
                     foreground="#27ae60").pack(pady=2)
        
        # Entrada de práctica
        ttk.Label(self.frame_principal_practica,
                 text="\nCrea tus propias oraciones:",
                 font=("Arial", 11, "bold")).pack(pady=10)
        
        self.entrada_practica = scrolledtext.ScrolledText(self.frame_principal_practica,
                                                         width=60,
                                                         height=8,
                                                         wrap=tk.WORD)
        self.entrada_practica.pack(pady=10)
        
        ttk.Button(self.frame_principal_practica,
                  text="Validar Gerundios",
                  command=self.validar_practica).pack()

    def validar_practica(self):
        texto = self.entrada_practica.get("1.0", tk.END)
        lineas = [line.strip() for line in texto.split('\n') if line.strip()]
        resultados = []
        
        for oracion in lineas:
            if any(palabra.strip(".,¡!¿?").endswith(('ando', 'iendo')) for palabra in oracion.split():
                resultados.append(f"✓ {oracion}")
                self.puntaje_total += 5
                self.progreso[self.categoria_actual]["correctas"] += 1
            else:
                resultados.append(f"✗ {oracion} (Falta gerundio)")
                self.puntaje_total = max(0, self.puntaje_total - 2)
                self.progreso[self.categoria_actual]["intentos"] += 1
        
        self.mostrar_resultados(resultados)
        self.actualizar_ui()

    def mostrar_resultados(self, resultados):
        ventana_resultados = tk.Toplevel()
        ventana_resultados.title("Resultados de Validación")
        
        text_widget = scrolledtext.ScrolledText(ventana_resultados,
                                               width=60,
                                               height=15,
                                               wrap=tk.WORD)
        text_widget.pack(padx=10, pady=10)
        
        for resultado in resultados:
            if resultado.startswith("✓"):
                text_widget.insert(tk.END, resultado + "\n", "correcto")
            else:
                text_widget.insert(tk.END, resultado + "\n", "incorrecto")
        
        text_widget.tag_config("correcto", foreground="green")
        text_widget.tag_config("incorrecto", foreground="red")
        text_widget.config(state=tk.DISABLED)

    def reescribir_frases(self):
        self.ventana_reescribir = tk.Toplevel()
        self.ventana_reescribir.title("Reescribir Frases")
        
        self.frame_instrucciones = ttk.Frame(self.ventana_reescribir)
        self.frame_instrucciones.pack(pady=10)
        
        ttk.Label(self.frame_instrucciones,
                 text="Reescribe las siguientes frases usando gerundios:",
                 font=("Arial", 12)).pack()
        
        self.frame_contenido = ttk.Frame(self.ventana_reescribir)
        self.frame_contenido.pack(pady=10)
        
        self.mostrar_siguiente_frase()

    def mostrar_siguiente_frase(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()
        
        if self.frase_actual < len(self.frases_reescribir):
            frase = self.frases_reescribir[self.frase_actual]
            
            ttk.Label(self.frame_contenido,
                     text=f"Frase original:\n{frase}",
                     font=("Arial", 11, "bold")).pack(pady=10)
            
            self.entrada_reescritura = ttk.Entry(self.frame_contenido, width=50)
            self.entrada_reescritura.pack(pady=10)
            self.entrada_reescritura.bind("<Return>", self.validar_reescritura)
            
            ttk.Button(self.frame_contenido,
                      text="Validar",
                      command=self.validar_reescritura).pack()
        else:
            messagebox.showinfo("Completado", "¡Todas las frases practicadas!")
            self.ventana_reescribir.destroy()

    def validar_reescritura(self, event=None):
        original = self.frases_reescribir[self.frase_actual]
        reescrita = self.entrada_reescritura.get()
        
        if any(palabra.endswith(('ando', 'iendo')) for palabra in reescrita.split():
            self.puntaje_total += 10
            messagebox.showinfo("Correcto", 
                              f"Original: {original}\nTu versión: {reescrita}")
            self.frase_actual += 1
            self.mostrar_siguiente_frase()
        else:
            messagebox.showerror("Error", "Incluye al menos un gerundio válido (-ando/-iendo)")
            self.puntaje_total = max(0, self.puntaje_total - 5)
        
        self.actualizar_ui()

    def mostrar_progreso(self):
        ventana_progreso = tk.Toplevel()
        ventana_progreso.title("Progreso Detallado")
        
        # Estadísticas generales
        ttk.Label(ventana_progreso,
                 text=f"Puntaje Total: {self.puntaje_total}",
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        # Tabla de categorías
        tree = ttk.Treeview(ventana_progreso, columns=("Categoría", "Prácticas", "Éxito"), show="headings")
        tree.heading("Categoría", text="Categoría")
        tree.heading("Prácticas", text="Prácticas")
        tree.heading("Éxito", text="% Éxito")
        tree.pack(pady=10, padx=10)
        
        for cat_id, datos in self.categorias.items():
            total = self.progreso[cat_id]["intentos"] + self.progreso[cat_id]["correctas"]
            porcentaje = (self.progreso[cat_id]["correctas"] / total * 100) if total > 0 else 0
            tree.insert("", tk.END, values=(
                datos["nombre"],
                f"{self.progreso[cat_id]['correctas']}/{total}",
                f"{porcentaje:.1f}%"
            ))
        
        # Gráfico de progreso
        canvas = tk.Canvas(ventana_progreso, width=600, height=300)
        canvas.pack(pady=10)
        
        colors = ["#3498db", "#2ecc71", "#e74c3c", "#9b59b6", "#f1c40f", "#1abc9c", "#34495e"]
        max_val = max([p["correctas"] for p in self.progreso.values()]) or 1
        
        for idx, (cat_id, datos) in enumerate(self.progreso.items()):
            height = (datos["correctas"] / max_val) * 250
            canvas.create_rectangle(
                50 + idx*80, 280 - height,
                120 + idx*80, 280,
                fill=colors[idx % len(colors)]
            )
            canvas.create_text(
                85 + idx*80, 290,
                text=self.categorias[cat_id]["nombre"][:3],
                angle=45
            )

    def mostrar_ayuda(self):
        ventana_ayuda = tk.Toplevel()
        ventana_ayuda.title("Ayuda Gramatical")
        
        text_widget = scrolledtext.ScrolledText(ventana_ayuda,
                                               width=70,
                                               height=25,
                                               wrap=tk.WORD,
                                               font=("Arial", 10))
        text_widget.pack(padx=10, pady=10)
        text_widget.insert(tk.END, self.help_content)
        text_widget.config(state=tk.DISABLED)

    def actualizar_ui(self):
        self.label_puntaje.config(text=f"Puntaje: {self.puntaje_total}")
        
        total_ejercicios = sum(cat["practicadas"] for cat in self.categorias.values())
        max_ejercicios = len(self.categorias) * 10
        progreso_general = (total_ejercicios / max_ejercicios * 100) if max_ejercicios > 0 else 0
        self.label_progreso.config(text=f"Progreso General: {progreso_general:.1f}%")

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    root.tk.call("source", "forest-dark.tcl")
    style.theme_use("forest-dark")
    
    app = GerundioMasterApp(root)
    root.mainloop()
