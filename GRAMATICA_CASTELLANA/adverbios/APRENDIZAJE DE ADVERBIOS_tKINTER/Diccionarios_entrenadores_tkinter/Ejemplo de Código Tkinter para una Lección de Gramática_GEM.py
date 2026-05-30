import tkinter as tk
from tkinter import ttk, scrolledtext
import language_tool_python
import threading # Para no bloquear la interfaz al revisar la gramática

class CursoGramaticaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Curso de Gramática Castellana")
        self.root.geometry("800x600") # Tamaño inicial de la ventana

        # Inicializar la herramienta de corrección gramatical (puede tardar un poco)
        # Se inicia en un hilo separado para no congelar la GUI
        self.tool = None
        self.status_label = ttk.Label(self.root, text="Cargando corrector gramatical...")
        self.status_label.pack(pady=10)
        threading.Thread(target=self._load_grammar_tool).start()

        self.puntos = 0
        self.nivel_actual = 1
        self.barra_nivel = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
        self.barra_nivel.pack(pady=5)
        self.actualizar_puntos_nivel()

        self._crear_interfaz_leccion()

    def _load_grammar_tool(self):
        try:
            self.tool = language_tool_python.LanguageTool('es') # 'es' para español
            self.status_label.config(text="Corrector gramatical cargado. ¡Comienza a aprender!")
        except Exception as e:
            self.status_label.config(text=f"Error al cargar corrector: {e}. Revisa tu conexión/instalación.")
            self.tool = None # Asegurarse de que tool sea None si falla la carga

    def _crear_interfaz_leccion(self):
        # Frame principal para la lección
        self.leccion_frame = ttk.Frame(self.root, padding="10")
        self.leccion_frame.pack(expand=True, fill="both")

        # --- Título de la Lección ---
        ttk.Label(self.leccion_frame, text="Lección 1: Uso de 'Hay', 'Ahí' y 'Ay'", font=("Helvetica", 16, "bold")).pack(pady=10)

        # --- Contenido Teórico ---
        teoria_texto = """
        ¡Hola! Hoy aprenderemos a diferenciar tres palabras homófonas muy comunes en español:

        * **Hay**: Es una forma del verbo "haber" (existencia). Se usa para indicar que algo existe o está presente.
            Ejemplo: "Hay mucha gente en la plaza." (Existe mucha gente)

        * **Ahí**: Es un adverbio de lugar. Se usa para indicar un lugar o posición.
            Ejemplo: "Tu libro está ahí, sobre la mesa." (En ese lugar)

        * **Ay**: Es una interjección que expresa dolor, sorpresa o emoción.
            Ejemplo: "¡Ay, qué dolor de cabeza!" (Expresión de dolor)

        Presta mucha atención a sus usos para evitar errores.
        """
        self.teoria_display = scrolledtext.ScrolledText(self.leccion_frame, wrap=tk.WORD, width=70, height=10, font=("Arial", 10))
        self.teoria_display.insert(tk.END, teoria_texto)
        self.teoria_display.config(state=tk.DISABLED) # Hacerlo de solo lectura
        self.teoria_display.pack(pady=5)

        # --- Espacio para la Práctica ---
        ttk.Label(self.leccion_frame, text="Escribe una frase usando correctamente 'hay', 'ahí' y 'ay':", font=("Helvetica", 12)).pack(pady=10)
        self.ejercicio_input = scrolledtext.ScrolledText(self.leccion_frame, wrap=tk.WORD, width=70, height=5, font=("Arial", 10))
        self.ejercicio_input.pack(pady=5)

        # --- Botón de Comprobar ---
        self.boton_comprobar = ttk.Button(self.leccion_frame, text="Comprobar Respuesta", command=self.comprobar_respuesta)
        self.boton_comprobar.pack(pady=10)

        # --- Área de Retroalimentación ---
        self.feedback_label = ttk.Label(self.leccion_frame, text="", font=("Helvetica", 11, "italic"))
        self.feedback_label.pack(pady=5)

    def comprobar_respuesta(self):
        if not self.tool:
            self.feedback_label.config(text="El corrector gramatical aún no está cargado o hubo un error.", foreground="orange")
            return

        respuesta_alumno = self.ejercicio_input.get("1.0", tk.END).strip()

        if not respuesta_alumno:
            self.feedback_label.config(text="Por favor, escribe algo para comprobar.", foreground="red")
            return

        # Simulación de evaluación: muy básica para este ejemplo
        # Para una evaluación real, necesitarías lógica más compleja
        # o un modelo de IA más avanzado.
        
        # Usar language_tool_python para detectar errores generales
        matches = self.tool.check(respuesta_alumno)
        
        # Una forma muy rudimentaria de verificar el uso específico de 'hay', 'ahí', 'ay'
        # Esto debería mejorarse con lógica más específica para cada lección.
        contiene_hay = "hay" in respuesta_alumno.lower()
        contiene_ahi = "ahí" in respuesta_alumno.lower()
        contiene_ay = "ay" in respuesta_alumno.lower()

        if len(matches) == 0 and contiene_hay and contiene_ahi and contiene_ay:
            self.feedback_label.config(text="¡Excelente! Tu frase es gramaticalmente correcta y usaste las palabras. +10 puntos.", foreground="green")
            self.actualizar_puntos(10)
        elif len(matches) > 0:
            errores_str = "\n".join([f"- {m.message} (Sugerencia: {', '.join(m.replacements)})" for m in matches[:3]]) # Mostrar hasta 3 errores
            self.feedback_label.config(text=f"¡Revisa tu frase! Se encontraron errores:\n{errores_str}", foreground="red")
            # Podrías restar puntos o no dar puntos aquí
        else:
            self.feedback_label.config(text="Tu frase no tiene errores obvios, pero asegúrate de usar las palabras clave de la lección.", foreground="blue")
            # Podrías dar menos puntos o indicar que falta algo

    def actualizar_puntos(self, puntos_ganados):
        self.puntos += puntos_ganados
        # Ejemplo de lógica para subir de nivel
        if self.puntos >= self.nivel_actual * 50: # Se sube de nivel cada 50 puntos
            self.nivel_actual += 1
            self.feedback_label.config(text=f"¡Felicidades! Has subido al Nivel {self.nivel_actual}.", foreground="purple")
        self.actualizar_puntos_nivel()

    def actualizar_puntos_nivel(self):
        self.barra_nivel['value'] = self.puntos % 50 # El progreso dentro del nivel actual
        self.barra_nivel['maximum'] = 50 # Cada nivel requiere 50 puntos
        self.status_label.config(text=f"Puntos: {self.puntos} | Nivel: {self.nivel_actual} - Cargando corrector gramatical...") # Actualizar también el status label
        
        # Re-actualizar el texto del status_label si ya se cargó el corrector
        if self.tool:
            self.status_label.config(text=f"Puntos: {self.puntos} | Nivel: {self.nivel_actual} - Corrector gramatical cargado. ¡Comienza a aprender!")
        else:
            self.status_label.config(text=f"Puntos: {self.puntos} | Nivel: {self.nivel_actual} - Cargando corrector gramatical...")


if __name__ == "__main__":
    root = tk.Tk()
    app = CursoGramaticaApp(root)
    root.mainloop()
