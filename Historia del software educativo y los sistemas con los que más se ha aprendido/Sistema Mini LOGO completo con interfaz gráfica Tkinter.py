import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import turtle
import math
import json
import os

class MiniLOGOGUI:
    """
    Sistema Mini LOGO completo con interfaz gráfica Tkinter
    Incluye turtle embebida y todos los comandos LOGO estándar
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Mini LOGO - Sistema Educativo de Programación")
        self.root.geometry("1200x700")
        
        # Configuración inicial
        self.setup_variables()
        self.create_widgets()
        self.setup_turtle()
        self.bind_events()
        
        # Mostrar ayuda inicial
        self.show_help()
        
    def setup_variables(self):
        """Inicializa variables y estructuras de datos"""
        self.command_history = []
        self.procedures = {}
        self.variables = {}
        self.is_recording = False
        self.recorded_commands = []
        self.current_file = None
        
        # Colores disponibles
        self.colors = {
            'red': '#FF0000', 'blue': '#0000FF', 'green': '#00FF00',
            'black': '#000000', 'white': '#FFFFFF', 'yellow': '#FFFF00',
            'purple': '#800080', 'orange': '#FFA500', 'pink': '#FFC0CB',
            'brown': '#A52A2A', 'cyan': '#00FFFF', 'gray': '#808080'
        }
        
    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar pesos de filas y columnas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Frame para el canvas de Turtle
        self.turtle_frame = ttk.LabelFrame(main_frame, text="Área de Dibujo", padding="5")
        self.turtle_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        self.turtle_frame.columnconfigure(0, weight=1)
        self.turtle_frame.rowconfigure(0, weight=1)
        
        # Frame para controles
        control_frame = ttk.LabelFrame(main_frame, text="Controles", padding="5")
        control_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Frame para entrada de comandos
        command_frame = ttk.LabelFrame(main_frame, text="Comandos LOGO", padding="5")
        command_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        command_frame.columnconfigure(0, weight=1)
        command_frame.rowconfigure(1, weight=1)
        
        # Botones de control
        ttk.Button(control_frame, text="Ejecutar", command=self.execute_command, 
                  width=12).grid(row=0, column=0, padx=2)
        ttk.Button(control_frame, text="Limpiar", command=self.clear_canvas,
                  width=12).grid(row=0, column=1, padx=2)
        ttk.Button(control_frame, text="Inicio", command=self.go_home,
                  width=12).grid(row=0, column=2, padx=2)
        ttk.Button(control_frame, text="Ayuda", command=self.show_help,
                  width=12).grid(row=0, column=3, padx=2)
        
        # Botones de archivo
        ttk.Button(control_frame, text="Abrir", command=self.load_program,
                  width=12).grid(row=0, column=4, padx=2)
        ttk.Button(control_frame, text="Guardar", command=self.save_program,
                  width=12).grid(row=0, column=5, padx=2)
        ttk.Button(control_frame, text="Grabar", command=self.toggle_recording,
                  width=12).grid(row=0, column=6, padx=2)
        
        # Selector de color
        ttk.Label(control_frame, text="Color:").grid(row=0, column=7, padx=(10, 2))
        self.color_var = tk.StringVar(value='blue')
        color_combo = ttk.Combobox(control_frame, textvariable=self.color_var,
                                  values=list(self.colors.keys()), width=10,
                                  state='readonly')
        color_combo.grid(row=0, column=8, padx=2)
        color_combo.bind('<<ComboboxSelected>>', self.change_color)
        
        # Control de grosor
        ttk.Label(control_frame, text="Grosor:").grid(row=0, column=9, padx=(10, 2))
        self.width_var = tk.IntVar(value=2)
        ttk.Scale(control_frame, from_=1, to=10, variable=self.width_var,
                 orient=tk.HORIZONTAL, length=80,
                 command=lambda v: self.change_width()).grid(row=0, column=10, padx=2)
        
        # Control de velocidad
        ttk.Label(control_frame, text="Velocidad:").grid(row=0, column=11, padx=(10, 2))
        self.speed_var = tk.IntVar(value=5)
        ttk.Scale(control_frame, from_=1, to=10, variable=self.speed_var,
                 orient=tk.HORIZONTAL, length=80,
                 command=lambda v: self.change_speed()).grid(row=0, column=12, padx=2)
        
        # Entrada de comandos
        self.cmd_input = ttk.Entry(command_frame, font=('Courier', 12))
        self.cmd_input.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        self.cmd_input.bind('<Return>', lambda e: self.execute_command())
        
        # Historial de comandos
        self.history_text = scrolledtext.ScrolledText(command_frame, 
                                                      font=('Courier', 10),
                                                      height=15, width=40)
        self.history_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame para procedimientos
        proc_frame = ttk.LabelFrame(main_frame, text="Procedimientos Definidos", padding="5")
        proc_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        proc_frame.columnconfigure(0, weight=1)
        proc_frame.rowconfigure(0, weight=1)
        
        self.proc_text = scrolledtext.ScrolledText(proc_frame, 
                                                   font=('Courier', 9),
                                                   height=8)
        self.proc_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Barra de estado
        self.status_var = tk.StringVar(value="Listo")
        status_bar = ttk.Label(self.root, textvariable=self.status_var,
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
    def setup_turtle(self):
        """Configura el canvas de Turtle embebido en Tkinter"""
        # Crear canvas para turtle
        self.canvas = tk.Canvas(self.turtle_frame, width=600, height=500,
                               bg='white', relief=tk.SUNKEN, borderwidth=2)
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear screen de turtle
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        
        # Crear tortuga
        self.t = turtle.RawTurtle(self.screen)
        self.t.shape("turtle")
        self.t.color("blue")
        self.t.speed(5)
        self.t.pensize(2)
        
        # Configurar coordenadas
        self.screen.setworldcoordinates(-300, -250, 300, 250)
        
    def bind_events(self):
        """Vincula eventos del teclado"""
        self.root.bind('<Control-o>', lambda e: self.load_program())
        self.root.bind('<Control-s>', lambda e: self.save_program())
        self.root.bind('<Control-l>', lambda e: self.clear_canvas())
        self.root.bind('<Control-h>', lambda e: self.go_home())
        self.root.bind('<F1>', lambda e: self.show_help())
        
    def execute_command(self, cmd=None):
        """Ejecuta un comando LOGO"""
        if cmd is None:
            cmd = self.cmd_input.get().strip()
            self.cmd_input.delete(0, tk.END)
        
        if not cmd:
            return
        
        # Añadir al historial
        self.command_history.append(cmd)
        self.history_text.insert(tk.END, f"> {cmd}\n")
        self.history_text.see(tk.END)
        
        # Si estamos grabando, guardar el comando
        if self.is_recording:
            self.recorded_commands.append(cmd)
        
        # Ejecutar comando
        self.status_var.set(f"Ejecutando: {cmd}")
        success = self.parse_and_execute(cmd)
        
        if success:
            self.status_var.set("Comando ejecutado")
        else:
            self.status_var.set("Error en comando")
            
        # Actualizar lista de procedimientos
        self.update_procedures_list()
        
    def parse_and_execute(self, cmd_line):
        """Parse y ejecuta una línea de comandos LOGO"""
        try:
            # Convertir a mayúsculas y dividir
            cmd_line = cmd_line.strip().upper()
            
            # Manejar comandos compuestos con punto y coma
            if ';' in cmd_line:
                sub_commands = cmd_line.split(';')
                for sub_cmd in sub_commands:
                    if sub_cmd.strip():
                        self.parse_and_execute(sub_cmd.strip())
                return True
            
            # Manejar REPEAT
            if cmd_line.startswith('REPEAT '):
                return self.handle_repeat(cmd_line)
            
            # Manejar PROCEDURE
            if cmd_line.startswith('PROCEDURE ') or cmd_line.startswith('PROC '):
                return self.handle_procedure_definition(cmd_line)
            
            # Manejar otros comandos
            parts = cmd_line.split()
            if not parts:
                return True
                
            cmd = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            
            # Ejecutar comando
            if cmd in self.procedures:
                return self.run_procedure(cmd, args)
            else:
                return self.execute_single_command(cmd, args)
                
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
            return False
    
    def execute_single_command(self, cmd, args):
        """Ejecuta un solo comando"""
        try:
            if cmd == 'FD' or cmd == 'FORWARD':
                if args:
                    distance = self.evaluate_expression(args[0])
                    self.t.forward(distance)
                return True
                
            elif cmd == 'BK' or cmd == 'BACK' or cmd == 'BACKWARD':
                if args:
                    distance = self.evaluate_expression(args[0])
                    self.t.backward(distance)
                return True
                
            elif cmd == 'RT' or cmd == 'RIGHT':
                if args:
                    angle = self.evaluate_expression(args[0])
                    self.t.right(angle)
                return True
                
            elif cmd == 'LT' or cmd == 'LEFT':
                if args:
                    angle = self.evaluate_expression(args[0])
                    self.t.left(angle)
                return True
                
            elif cmd == 'PU' or cmd == 'PENUP':
                self.t.penup()
                return True
                
            elif cmd == 'PD' or cmd == 'PENDOWN':
                self.t.pendown()
                return True
                
            elif cmd == 'COLOR' or cmd == 'SETCOLOR':
                if args:
                    color = ' '.join(args).lower()
                    if color in self.colors:
                        self.t.color(self.colors[color])
                        self.color_var.set(color)
                    else:
                        self.t.color(color)
                return True
                
            elif cmd == 'GOTO':
                if len(args) >= 2:
                    x = self.evaluate_expression(args[0])
                    y = self.evaluate_expression(args[1])
                    self.t.penup()
                    self.t.goto(x, y)
                    self.t.pendown()
                return True
                
            elif cmd == 'CIRCLE':
                if args:
                    radius = self.evaluate_expression(args[0])
                    self.t.circle(radius)
                return True
                
            elif cmd == 'HOME':
                self.t.penup()
                self.t.home()
                self.t.pendown()
                return True
                
            elif cmd == 'CLEAR' or cmd == 'CS':
                self.t.clear()
                return True
                
            elif cmd == 'SPEED':
                if args:
                    speed = int(self.evaluate_expression(args[0]))
                    self.t.speed(max(1, min(10, speed)))
                    self.speed_var.set(speed)
                return True
                
            elif cmd == 'PENWIDTH' or cmd == 'PW':
                if args:
                    width = int(self.evaluate_expression(args[0]))
                    self.t.pensize(max(1, width))
                    self.width_var.set(width)
                return True
                
            elif cmd == 'LABEL':
                if args:
                    # Unir todos los argumentos como texto
                    text = ' '.join(args)
                    # Quitar comillas si existen
                    if (text.startswith('"') and text.endswith('"')) or \
                       (text.startswith("'") and text.endswith("'")):
                        text = text[1:-1]
                    
                    # Escribir texto en la posición actual
                    self.t.write(text, align="center", font=("Arial", 12, "normal"))
                return True
                
            elif cmd == 'RUN':
                if args:
                    filename = ' '.join(args)
                    self.load_and_run(filename)
                return True
                
            elif cmd == 'SAVE':
                if args:
                    filename = ' '.join(args)
                    self.save_current_script(filename)
                else:
                    self.save_program()
                return True
                
            elif cmd == 'LOAD':
                if args:
                    filename = ' '.join(args)
                    self.load_program_file(filename)
                else:
                    self.load_program()
                return True
                
            elif cmd == 'HELP':
                self.show_help()
                return True
                
            elif cmd == 'EXIT' or cmd == 'QUIT':
                self.root.quit()
                return True
                
            elif cmd == 'PRINT' or cmd == 'SHOW':
                if args:
                    value = ' '.join(args)
                    result = self.evaluate_expression(value)
                    self.history_text.insert(tk.END, f"= {result}\n")
                return True
                
            elif cmd == 'MAKE' or cmd == 'SET':
                if len(args) >= 2:
                    var_name = args[0]
                    if var_name.startswith('"'):
                        var_name = var_name[1:]
                    expr = ' '.join(args[1:])
                    value = self.evaluate_expression(expr)
                    self.variables[var_name] = value
                    self.history_text.insert(tk.END, f"Variable {var_name} = {value}\n")
                return True
                
            else:
                # Intentar como expresión matemática
                try:
                    result = self.evaluate_expression(cmd_line)
                    self.history_text.insert(tk.END, f"= {result}\n")
                    return True
                except:
                    self.show_error(f"Comando no reconocido: {cmd}")
                    return False
                    
        except Exception as e:
            self.show_error(f"Error ejecutando {cmd}: {str(e)}")
            return False
    
    def handle_repeat(self, cmd_line):
        """Maneja el comando REPEAT"""
        try:
            # Extraer número de repeticiones
            parts = cmd_line.split(None, 2)
            if len(parts) < 3:
                raise ValueError("Formato: REPEAT n [comandos]")
            
            repeat_count = int(self.evaluate_expression(parts[1]))
            block = parts[2]
            
            # Verificar que el bloque esté entre corchetes
            if not (block.startswith('[') and block.endswith(']')):
                raise ValueError("Los comandos deben estar entre [ ]")
            
            # Extraer comandos del bloque
            commands = block[1:-1].strip()
            
            # Ejecutar repetidamente
            for _ in range(repeat_count):
                # Dividir por punto y coma si hay múltiples comandos
                if ';' in commands:
                    sub_cmds = commands.split(';')
                    for sub_cmd in sub_cmds:
                        if sub_cmd.strip():
                            self.parse_and_execute(sub_cmd.strip())
                else:
                    self.parse_and_execute(commands)
            
            return True
            
        except Exception as e:
            self.show_error(f"Error en REPEAT: {str(e)}")
            return False
    
    def handle_procedure_definition(self, cmd_line):
        """Maneja la definición de procedimientos"""
        try:
            # Extraer nombre del procedimiento
            parts = cmd_line.split(None, 2)
            if len(parts) < 3:
                raise ValueError("Formato: PROCEDURE nombre [comandos]")
            
            proc_name = parts[1].upper()
            block = parts[2]
            
            # Verificar que el bloque esté entre corchetes
            if not (block.startswith('[') and block.endswith(']')):
                raise ValueError("Los comandos deben estar entre [ ]")
            
            # Guardar procedimiento
            self.procedures[proc_name] = block[1:-1].strip()
            self.history_text.insert(tk.END, f"Procedimiento {proc_name} definido\n")
            
            return True
            
        except Exception as e:
            self.show_error(f"Error definiendo procedimiento: {str(e)}")
            return False
    
    def run_procedure(self, proc_name, args):
        """Ejecuta un procedimiento definido"""
        try:
            if proc_name in self.procedures:
                commands = self.procedures[proc_name]
                
                # Si hay argumentos, reemplazarlos
                if args:
                    for i, arg in enumerate(args, 1):
                        commands = commands.replace(f":{i}", str(self.evaluate_expression(arg)))
                
                # Ejecutar comandos del procedimiento
                if ';' in commands:
                    sub_cmds = commands.split(';')
                    for sub_cmd in sub_cmds:
                        if sub_cmd.strip():
                            self.parse_and_execute(sub_cmd.strip())
                else:
                    self.parse_and_execute(commands)
                
                return True
            else:
                self.show_error(f"Procedimiento no encontrado: {proc_name}")
                return False
                
        except Exception as e:
            self.show_error(f"Error ejecutando procedimiento {proc_name}: {str(e)}")
            return False
    
    def evaluate_expression(self, expr):
        """Evalúa una expresión matemática, manejando variables"""
        try:
            # Reemplazar variables
            for var_name, value in self.variables.items():
                expr = expr.replace(var_name, str(value))
            
            # Reemplazar constantes matemáticas
            expr = expr.replace('PI', str(math.pi))
            
            # Evaluar expresión
            # Nota: Usar eval con precaución. En producción, usar parser seguro
            result = eval(expr, {"__builtins__": {}}, 
                         {"sin": math.sin, "cos": math.cos, "tan": math.tan,
                          "sqrt": math.sqrt, "abs": abs, "int": int, "float": float})
            return result
            
        except Exception as e:
            raise ValueError(f"Error evaluando expresión '{expr}': {str(e)}")
    
    def clear_canvas(self):
        """Limpia el canvas"""
        self.t.clear()
        self.t.penup()
        self.t.home()
        self.t.pendown()
        self.status_var.set("Canvas limpiado")
    
    def go_home(self):
        """Regresa la tortuga al origen"""
        self.t.penup()
        self.t.home()
        self.t.pendown()
        self.status_var.set("En posición inicial")
    
    def change_color(self, event=None):
        """Cambia el color de la tortuga"""
        color = self.color_var.get()
        if color in self.colors:
            self.t.color(self.colors[color])
    
    def change_width(self):
        """Cambia el grosor del trazo"""
        self.t.pensize(self.width_var.get())
    
    def change_speed(self):
        """Cambia la velocidad de la tortuga"""
        self.t.speed(self.speed_var.get())
    
    def toggle_recording(self):
        """Activa/desactiva la grabación de comandos"""
        self.is_recording = not self.is_recording
        if self.is_recording:
            self.recorded_commands = []
            self.status_var.set("Grabando comandos...")
        else:
            self.status_var.set(f"Grabación detenida ({len(self.recorded_commands)} comandos)")
    
    def save_program(self):
        """Guarda el programa actual en un archivo"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".logo",
            filetypes=[("Archivos LOGO", "*.logo"), ("Todos los archivos", "*.*")],
            title="Guardar programa LOGO"
        )
        
        if filename:
            try:
                # Guardar comandos del historial
                with open(filename, 'w', encoding='utf-8') as f:
                    for cmd in self.command_history:
                        f.write(cmd + '\n')
                
                self.current_file = filename
                self.status_var.set(f"Programa guardado: {os.path.basename(filename)}")
                
            except Exception as e:
                self.show_error(f"Error guardando archivo: {str(e)}")
    
    def save_current_script(self, filename):
        """Guarda el script actual en el archivo especificado"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for cmd in self.command_history:
                    f.write(cmd + '\n')
            
            self.current_file = filename
            self.status_var.set(f"Programa guardado: {os.path.basename(filename)}")
            
        except Exception as e:
            self.show_error(f"Error guardando archivo: {str(e)}")
    
    def load_program(self):
        """Carga un programa desde archivo"""
        filename = filedialog.askopenfilename(
            defaultextension=".logo",
            filetypes=[("Archivos LOGO", "*.logo"), ("Archivos de texto", "*.txt"), 
                      ("Todos los archivos", "*.*")],
            title="Abrir programa LOGO"
        )
        
        if filename:
            self.load_program_file(filename)
    
    def load_program_file(self, filename):
        """Carga y ejecuta un programa desde archivo"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Limpiar y ejecutar cada línea
            self.clear_canvas()
            self.command_history = []
            self.history_text.delete(1.0, tk.END)
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):  # Ignorar comentarios
                    self.execute_command(line)
            
            self.current_file = filename
            self.status_var.set(f"Programa cargado: {os.path.basename(filename)}")
            
        except Exception as e:
            self.show_error(f"Error cargando archivo: {str(e)}")
    
    def load_and_run(self, filename):
        """Carga y ejecuta un programa"""
        self.load_program_file(filename)
    
    def update_procedures_list(self):
        """Actualiza la lista de procedimientos en la interfaz"""
        self.proc_text.delete(1.0, tk.END)
        
        if self.procedures:
            for name, code in self.procedures.items():
                self.proc_text.insert(tk.END, f"{name}:\n")
                self.proc_text.insert(tk.END, f"  {code}\n\n")
        else:
            self.proc_text.insert(tk.END, "No hay procedimientos definidos")
    
    def show_help(self):
        """Muestra la ayuda de comandos"""
        help_text = """
=== COMANDOS MINI LOGO ===

MOVIMIENTO:
  FD <n>         - Avanzar n pasos (FORWARD)
  BK <n>         - Retroceder n pasos (BACK)
  RT <grados>    - Girar derecha (RIGHT)
  LT <grados>    - Girar izquierda (LEFT)
  GOTO <x> <y>   - Ir a coordenadas específicas
  HOME           - Regresar al centro

CONTROL DE LÁPIZ:
  PU             - Subir lápiz (PENUP)
  PD             - Bajar lápiz (PENDOWN)
  PENWIDTH <n>   - Cambiar grosor de línea

APARIENCIA:
  COLOR <nombre> - Cambiar color (red, blue, green, etc.)
  LABEL "texto"  - Escribir texto en pantalla
  SPEED <1-10>   - Cambiar velocidad de dibujo

ESTRUCTURAS DE CONTROL:
  REPEAT n [comandos] - Repetir comandos n veces
  PROCEDURE nombre [comandos] - Definir procedimiento
  nombre             - Ejecutar procedimiento

FORMAS GEOMÉTRICAS:
  CIRCLE <radio> - Dibujar círculo
  (Usando FD, RT, etc. se pueden hacer más formas)

OPERACIONES:
  MAKE "var valor - Crear variable
  PRINT expr     - Mostrar valor
  CLEAR          - Limpiar pantalla

ARCHIVOS:
  SAVE [nombre]  - Guardar programa
  LOAD [nombre]  - Cargar programa
  RUN nombre     - Ejecutar archivo

UTILIDADES:
  HELP           - Mostrar esta ayuda
  EXIT           - Salir del programa

EJEMPLOS:
  FD 100 RT 90 FD 100 RT 90 FD 100 RT 90 FD 100
  REPEAT 4 [FD 100 RT 90]
  COLOR red CIRCLE 50
  PROCEDURE SQUARE [REPEAT 4 [FD 100 RT 90]]
  SQUARE
  LABEL "Hola Mundo"
        """
        
        # Mostrar en ventana emergente
        help_window = tk.Toplevel(self.root)
        help_window.title("Ayuda de Mini LOGO")
        help_window.geometry("600x500")
        
        help_text_widget = scrolledtext.ScrolledText(help_window, font=('Courier', 10))
        help_text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        help_text_widget.insert(tk.END, help_text)
        help_text_widget.config(state=tk.DISABLED)
        
        ttk.Button(help_window, text="Cerrar", command=help_window.destroy).pack(pady=10)
    
    def show_error(self, message):
        """Muestra un mensaje de error"""
        messagebox.showerror("Error", message)
        self.history_text.insert(tk.END, f"ERROR: {message}\n")
    
    def run_example(self, example_name):
        """Ejecuta un ejemplo predefinido"""
        examples = {
            'cuadrado': 'REPEAT 4 [FD 100 RT 90]',
            'triangulo': 'REPEAT 3 [FD 100 RT 120]',
            'circulos': 'REPEAT 36 [CIRCLE 50 RT 10]',
            'espiral': 'REPEAT 20 [FD 100 RT 95 FD 100]',
            'estrella': 'REPEAT 5 [FD 100 RT 144]',
            'poligono': 'REPEAT 6 [FD 80 RT 60]',
            'texto': 'LABEL "Hola LOGO!"',
            'casa': """
PU GOTO -50 -50 PD
REPEAT 4 [FD 100 RT 90]
FD 100 RT 30
REPEAT 3 [FD 100 RT 120]
HOME
"""
        }
        
        if example_name in examples:
            self.execute_command(examples[example_name])

# ===========================================
# FUNCIÓN PRINCIPAL
# ===========================================
def main():
    """Función principal de la aplicación"""
    root = tk.Tk()
    app = MiniLOGOGUI(root)
    
    # Ejecutar ejemplo inicial
    root.after(1000, lambda: app.run_example('cuadrado'))
    
    root.mainloop()

if __name__ == "__main__":
    main()
