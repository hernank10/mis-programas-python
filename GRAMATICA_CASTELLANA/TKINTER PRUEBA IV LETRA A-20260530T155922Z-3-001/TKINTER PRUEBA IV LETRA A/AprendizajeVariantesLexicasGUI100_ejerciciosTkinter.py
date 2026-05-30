import tkinter as tk
from tkinter import ttk, messagebox
import random
import json

class AprendizajeVariantesLexicasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Variantes Léxicas")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f8ff')
        
        # Datos de los sistemas de formación
        self.sistemas = {
            "prefijacion": {
                "definicion": "Adición de un prefijo al inicio de una palabra base",
                "funcion": "Modificar o precisar el significado sin cambiar categoría gramatical",
                "ejemplos_es": ["deshacer", "antinatural", "sobreestimar", "releer", "subdirector", "contraatacar", "precocinar"],
                "ejemplos_en": ["unhappy", "disagree", "rewrite", "supermarket", "submarine", "antibacterial", "prepay"],
                "reglas_escritura": {
                    "español": "Se escriben unidos a la palabra sin guion",
                    "inglés": "Generalmente unidos, guion con mayúsculas o siglas"
                },
                "clasificacion_semantica": ["Negación/Opuesto", "Cantidad/Medida", "Tiempo", "Lugar/Orientación"]
            },
            "sufijacion": {
                "definicion": "Adición de un sufijo al final de una palabra base",
                "funcion": "Puede cambiar categoría gramatical y añadir matices",
                "ejemplos_es": ["librería", "cantante", "cafecito", "verdadero", "acelerar", "amoroso", "cariñosamente"],
                "ejemplos_en": ["teacher", "hopeful", "quickly", "kingdom", "piglet", "happiness", "beautifully"],
                "reglas_escritura": {
                    "español": "Atención a cambios ortográficos (c->z, g->j)",
                    "inglés": "Duplicación consonante final en ciertos casos"
                },
                "clasificacion_semantica": ["Forma sustantivos", "Forma adjetivos", "Forma verbos", "Aprecio/Desprecio"]
            },
            "parasintesis": {
                "definicion": "Adición simultánea de prefijo y sufijo a una misma base",
                "funcion": "Crear verbos que expresan estados o acciones complejas",
                "ejemplos_es": ["alunizar", "enrojecer", "embarcar", "anochecer", "entristecer", "ensordecer", "amancebarse"],
                "ejemplos_en": ["enlighten", "embolden", "encircle", "enslave", "endanger"],
                "reglas_escritura": {
                    "español": "Se escriben unidos, no existe la forma con solo prefijo o sufijo",
                    "inglés": "Menos común que en español"
                },
                "clasificacion_semantica": ["Poner en un estado", "Introducir en un lugar", "Cubrir con algo"]
            },
            "composicion": {
                "definicion": "Unión de dos o más palabras léxicas independientes",
                "funcion": "Crear nueva palabra con significado único",
                "ejemplos_es": ["paraguas", "abrelatas", "agridulce", "pelirrojo", "máquina de escribir", "sordomudo", "cortacésped"],
                "ejemplos_en": ["notebook", "smartphone", "greenhouse", "swimming pool", "mother-in-law", "football", "breakfast"],
                "reglas_escritura": {
                    "español": "Unidos, con guion o separados según el caso",
                    "inglés": "Unidos, con guion o separados (tendencia a unión)"
                },
                "clasificacion_semantica": ["Unión significados", "Especificación", "Acción y objeto", "Relación espacial"]
            }
        }
        
        # 100 ejercicios basados en clasificación RAE
        self.ejercicios = self.generar_ejercicios()
        
        self.puntaje = 0
        self.preguntas_realizadas = 0
        self.ejercicio_actual = 0
        
        self.crear_interfaz_principal()
    
    def generar_ejercicios(self):
        ejercicios = []
        
        # Ejercicios de identificación de sistemas (25)
        sistemas_list = list(self.sistemas.keys())
        for sistema in sistemas_list:
            for ejemplo in self.sistemas[sistema]["ejemplos_es"][:6]:
                ejercicios.append({
                    "tipo": "identificacion",
                    "pregunta": f"¿A qué sistema pertenece la palabra: '{ejemplo}'?",
                    "opciones": sistemas_list.copy(),
                    "respuesta": sistema,
                    "explicacion": f"'{ejemplo}' es un ejemplo de {sistema}. {self.sistemas[sistema]['definicion']}"
                })
        
        # Ejercicios de clasificación semántica (25)
        clasificaciones = []
        for sistema, datos in self.sistemas.items():
            for clasif in datos["clasificacion_semantica"]:
                clasificaciones.append((sistema, clasif))
        
        for _ in range(25):
            sistema, clasif = random.choice(clasificaciones)
            ejemplo = random.choice(self.sistemas[sistema]["ejemplos_es"])
            otras_clasif = [c for s, c in clasificaciones if s == sistema and c != clasif]
            opciones = [clasif] + random.sample(otras_clasif, min(3, len(otras_clasif)))
            random.shuffle(opciones)
            
            ejercicios.append({
                "tipo": "clasificacion_semantica",
                "pregunta": f"¿Qué clasificación semántica tiene la palabra '{ejemplo}'?",
                "opciones": opciones,
                "respuesta": clasif,
                "explicacion": f"'{ejemplo}' pertenece a la clasificación '{clasif}' del sistema {sistema}"
            })
        
        # Ejercicios de reglas ortográficas (25)
        reglas_pairs = []
        for sistema, datos in self.sistemas.items():
            reglas_pairs.append((sistema, "español", datos["reglas_escritura"]["español"]))
            reglas_pairs.append((sistema, "inglés", datos["reglas_escritura"]["inglés"]))
        
        for _ in range(25):
            sistema, idioma, regla = random.choice(reglas_pairs)
            otras_reglas = [r for s, i, r in reglas_pairs if (s, i) != (sistema, idioma)]
            opciones = [regla] + random.sample(otras_reglas, min(3, len(otras_reglas)))
            random.shuffle(opciones)
            
            ejercicios.append({
                "tipo": "reglas_ortograficas",
                "pregunta": f"¿Cuál es la regla de escritura en {idioma} para la {sistema}?",
                "opciones": opciones,
                "respuesta": regla,
                "explicacion": f"En {idioma}, la {sistema} sigue la regla: {regla}"
            })
        
        # Ejercicios de completar ejemplos (25)
        for _ in range(25):
            sistema = random.choice(sistemas_list)
            ejemplo_base = random.choice(self.sistemas[sistema]["ejemplos_es"])
            # Crear versión incompleta (quitar parte)
            if sistema == "prefijacion":
                partes = ejemplo_base.split('-') if '-' in ejemplo_base else [ejemplo_base]
                if len(partes) > 1:
                    incompleto = f"____-{partes[1]}"
                else:
                    incompleto = f"____{ejemplo_base[4:]}"
            else:
                incompleto = f"{ejemplo_base[:-3]}____"
            
            ejercicios.append({
                "tipo": "completar",
                "pregunta": f"Completa la palabra: {incompleto}",
                "opciones": [ejemplo_base] + random.sample(
                    [e for e in self.sistemas[sistema]["ejemplos_es"] if e != ejemplo_base], 
                    min(3, len(self.sistemas[sistema]["ejemplos_es"])-1)
                ),
                "respuesta": ejemplo_base,
                "explicacion": f"La palabra completa es '{ejemplo_base}'. {self.sistemas[sistema]['definicion']}"
            })
        
        random.shuffle(ejercicios)
        return ejercicios
    
    def crear_interfaz_principal(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = tk.Label(main_frame, text="🎓 APRENDIZAJE DE VARIANTES LÉXICAS 🎓", 
                         font=('Arial', 16, 'bold'), bg='#f0f8ff', fg='#2c3e50')
        titulo.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Botones principales
        botones_info = [
            ("📊 Ver Tabla Completa", self.mostrar_tabla_completa),
            ("❓ Quiz de Definiciones", self.quiz_definiciones),
            ("🔍 Identificar Sistemas", self.identificar_sistemas),
            ("✍️ Práctica de Escritura", self.practica_escritura),
            ("📚 100 Ejercicios RAE", self.ejercicios_rae),
            ("📈 Estadísticas", self.mostrar_estadisticas)
        ]
        
        for i, (texto, comando) in enumerate(botones_info):
            btn = tk.Button(main_frame, text=texto, command=comando,
                           font=('Arial', 12), bg='#3498db', fg='white',
                           width=25, height=2)
            btn.grid(row=i+1, column=0, columnspan=2, pady=10, padx=20)
        
        # Info de progreso
        self.label_progreso = tk.Label(main_frame, 
                                      text=f"Progreso: {self.puntaje} puntos",
                                      font=('Arial', 10), bg='#f0f8ff')
        self.label_progreso.grid(row=len(botones_info)+1, column=0, columnspan=2, pady=10)
    
    def mostrar_tabla_completa(self):
        ventana_tabla = tk.Toplevel(self.root)
        ventana_tabla.title("Tabla Completa de Sistemas Léxicos")
        ventana_tabla.geometry("900x600")
        
        # Notebook para pestañas
        notebook = ttk.Notebook(ventana_tabla)
        
        for sistema, datos in self.sistemas.items():
            frame = ttk.Frame(notebook, padding="10")
            notebook.add(frame, text=sistema.upper())
            
            # Contenido de cada pestaña
            tk.Label(frame, text=f"SISTEMA: {sistema.upper()}", 
                    font=('Arial', 14, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
            
            info_labels = [
                ("Definición:", datos["definicion"]),
                ("Función:", datos["funcion"]),
                ("Clasificación Semántica:", ", ".join(datos["clasificacion_semantica"])),
                ("Ejemplos Español:", ", ".join(datos["ejemplos_es"])),
                ("Ejemplos Inglés:", ", ".join(datos["ejemplos_en"])),
                ("Reglas Español:", datos["reglas_escritura"]["español"]),
                ("Reglas Inglés:", datos["reglas_escritura"]["inglés"])
            ]
            
            for i, (titulo, contenido) in enumerate(info_labels, 1):
                tk.Label(frame, text=titulo, font=('Arial', 10, 'bold')).grid(row=i, column=0, sticky='w', pady=2)
                tk.Label(frame, text=contenido, font=('Arial', 10), wraplength=800).grid(row=i, column=1, sticky='w', pady=2)
        
        notebook.grid(row=0, column=0, sticky='nsew')
    
    def quiz_definiciones(self):
        self.crear_ventana_quiz("Quiz de Definiciones")
    
    def identificar_sistemas(self):
        self.crear_ventana_quiz("Identificar Sistemas")
    
    def practica_escritura(self):
        self.crear_ventana_quiz("Práctica de Escritura")
    
    def crear_ventana_quiz(self, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("600x400")
        
        frame = ttk.Frame(ventana, padding="20")
        frame.grid(row=0, column=0, sticky='nsew')
        
        self.label_pregunta = tk.Label(frame, text="", font=('Arial', 12), wraplength=500)
        self.label_pregunta.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.botones_opciones = []
        for i in range(4):
            btn = tk.Button(frame, text="", font=('Arial', 10), width=50,
                           command=lambda idx=i: self.verificar_respuesta(idx))
            btn.grid(row=i+1, column=0, columnspan=2, pady=5)
            self.botones_opciones.append(btn)
        
        self.label_explicacion = tk.Label(frame, text="", font=('Arial', 10), 
                                         wraplength=500, fg='blue')
        self.label_explicacion.grid(row=5, column=0, columnspan=2, pady=10)
        
        btn_siguiente = tk.Button(frame, text="Siguiente Pregunta", 
                                 command=self.nueva_pregunta)
        btn_siguiente.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.ventana_quiz = ventana
        self.nueva_pregunta()
    
    def nueva_pregunta(self):
        self.label_explicacion.config(text="")
        ejercicio = random.choice(self.ejercicios)
        
        self.label_pregunta.config(text=ejercicio["pregunta"])
        self.ejercicio_actual = ejercicio
        
        for i, btn in enumerate(self.botones_opciones):
            if i < len(ejercicio["opciones"]):
                btn.config(text=ejercicio["opciones"][i], state='normal')
            else:
                btn.config(text="", state='disabled')
    
    def verificar_respuesta(self, indice):
        respuesta_seleccionada = self.botones_opciones[indice].cget('text')
        respuesta_correcta = self.ejercicio_actual["respuesta"]
        
        if respuesta_seleccionada == respuesta_correcta:
            self.puntaje += 1
            mensaje = "¡Correcto! +1 punto"
            color = 'green'
        else:
            mensaje = f"Incorrecto. La respuesta era: {respuesta_correcta}"
            color = 'red'
        
        self.label_explicacion.config(text=f"{mensaje}\n\n{self.ejercicio_actual['explicacion']}", fg=color)
        self.actualizar_progreso()
        
        for btn in self.botones_opciones:
            btn.config(state='disabled')
    
    def ejercicios_rae(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("100 Ejercicios RAE - Variantes Léxicas")
        ventana.geometry("700x500")
        
        frame = ttk.Frame(ventana, padding="20")
        frame.grid(row=0, column=0, sticky='nsew')
        
        tk.Label(frame, text="EJERCICIOS BASADOS EN CLASIFICACIÓN RAE", 
                font=('Arial', 14, 'bold')).grid(row=0, column=0, pady=10)
        
        # Contador de ejercicios
        self.contador_ejercicios = 0
        self.label_contador = tk.Label(frame, text=f"Ejercicio 1 de 100", font=('Arial', 12))
        self.label_contador.grid(row=1, column=0, pady=10)
        
        self.label_pregunta_rae = tk.Label(frame, text="", font=('Arial', 11), wraplength=600)
        self.label_pregunta_rae.grid(row=2, column=0, pady=20)
        
        self.frame_opciones_rae = ttk.Frame(frame)
        self.frame_opciones_rae.grid(row=3, column=0, pady=10)
        
        btn_siguiente_rae = tk.Button(frame, text="Siguiente Ejercicio", 
                                     command=self.siguiente_ejercicio_rae)
        btn_siguiente_rae.grid(row=4, column=0, pady=20)
        
        self.ventana_rae = ventana
        self.siguiente_ejercicio_rae()
    
    def siguiente_ejercicio_rae(self):
        if self.contador_ejercicios >= len(self.ejercicios):
            messagebox.showinfo("Completado", "¡Has completado todos los ejercicios!")
            return
        
        # Limpiar opciones anteriores
        for widget in self.frame_opciones_rae.winfo_children():
            widget.destroy()
        
        ejercicio = self.ejercicios[self.contador_ejercicios]
        self.contador_ejercicios += 1
        
        self.label_contador.config(text=f"Ejercicio {self.contador_ejercicios} de 100")
        self.label_pregunta_rae.config(text=ejercicio["pregunta"])
        
        # Crear botones de opciones
        for i, opcion in enumerate(ejercicio["opciones"]):
            btn = tk.Button(self.frame_opciones_rae, text=opcion, font=('Arial', 10),
                           command=lambda opc=opcion, ej=ejercicio: self.verificar_ejercicio_rae(opc, ej))
            btn.grid(row=i, column=0, pady=5, sticky='w')
    
    def verificar_ejercicio_rae(self, opcion_seleccionada, ejercicio):
        if opcion_seleccionada == ejercicio["respuesta"]:
            self.puntaje += 1
            messagebox.showinfo("Correcto", f"¡Bien! +1 punto\n\n{ejercicio['explicacion']}")
        else:
            messagebox.showinfo("Incorrecto", 
                              f"La respuesta correcta era: {ejercicio['respuesta']}\n\n{ejercicio['explicacion']}")
        
        self.actualizar_progreso()
    
    def mostrar_estadisticas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Estadísticas de Progreso")
        ventana.geometry("400x300")
        
        frame = ttk.Frame(ventana, padding="20")
        frame.grid(row=0, column=0, sticky='nsew')
        
        tk.Label(frame, text="📊 ESTADÍSTICAS DE APRENDIZAJE", 
                font=('Arial', 14, 'bold')).grid(row=0, column=0, pady=10)
        
        total_posible = self.contador_ejercicios + self.preguntas_realizadas
        porcentaje = (self.puntaje / total_posible * 100) if total_posible > 0 else 0
        
        estadisticas = [
            f"Puntuación Total: {self.puntaje} puntos",
            f"Ejercicios Realizados: {total_posible}",
            f"Porcentaje de Aciertos: {porcentaje:.1f}%",
            f"Ejercicios RAE Completados: {self.contador_ejercicios}/100"
        ]
        
        for i, stat in enumerate(estadisticas, 1):
            tk.Label(frame, text=stat, font=('Arial', 12)).grid(row=i, column=0, pady=5, sticky='w')
        
        # Mensaje de motivación
        if porcentaje >= 90:
            mensaje = "¡Excelente! Eres un experto en variantes léxicas"
        elif porcentaje >= 70:
            mensaje = "Muy buen trabajo, sigue practicando"
        elif porcentaje >= 50:
            mensaje = "Buen progreso, continúa así"
        else:
            mensaje = "Sigue practicando, mejorarás con el tiempo"
        
        tk.Label(frame, text=mensaje, font=('Arial', 11), fg='blue', wraplength=350).grid(row=5, column=0, pady=20)
    
    def actualizar_progreso(self):
        self.label_progreso.config(text=f"Progreso: {self.puntaje} puntos")

def main():
    root = tk.Tk()
    app = AprendizajeVariantesLexicasGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
