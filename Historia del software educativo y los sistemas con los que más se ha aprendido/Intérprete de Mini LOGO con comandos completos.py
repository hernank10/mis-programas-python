import turtle
import math
import sys

class MiniLOGO:
    """
    Intérprete de Mini LOGO con comandos completos.
    Similar a los primeros entornos LOGO educativos.
    """
    
    def __init__(self):
        self.tortuga = turtle.Turtle()
        self.pantalla = turtle.Screen()
        self.pantalla.title("Mini LOGO - Sistema Educativo")
        self.pantalla.setup(width=800, height=600)
        self.pantalla.bgcolor("white")
        
        # Configuración inicial
        self.tortuga.shape("turtle")
        self.tortuga.color("blue")
        self.tortuga.speed(5)
        self.tortuga.pensize(2)
        
        # Estado del lápiz
        self.lapiz_abajo = True
        
        # Historial de comandos
        self.historial = []
        
        # Variables del usuario
        self.variables = {}
        
        # Procedimientos definidos por el usuario
        self.procedimientos = {}
        
        # Modo de ejecución (inmediato o por procedimientos)
        self.modo_imediato = True
        
        print("=== MINI LOGO ===")
        print("Sistema educativo de programación")
        print("Escribe 'AYUDA' para ver los comandos disponibles")
        print("Escribe 'SALIR' para terminar")
        print()

    def ayuda(self):
        """Muestra la ayuda de comandos disponibles"""
        print("\n=== COMANDOS DISPONIBLES ===")
        print("MOVIMIENTO:")
        print("  AV <n>        - Avanzar n pasos")
        print("  RE <n>        - Retroceder n pasos")
        print("  GI <grados>   - Girar izquierda")
        print("  GD <grados>   - Girar derecha")
        print("  HO            - Ir al origen (Home)")
        
        print("\nCONTROL DE LÁPIZ:")
        print("  BP            - Bajar lápiz (dibujar)")
        print("  SP            - Subir lápiz (no dibujar)")
        
        print("\nAPARIENCIA:")
        print("  COLOR <color> - Cambiar color (rojo, azul, verde, etc.)")
        print("  GROSOR <n>    - Cambiar grosor de línea")
        print("  OT            - Ocultar tortuga")
        print("  MT            - Mostrar tortuga")
        
        print("\nCONTROL DE PROGRAMA:")
        print("  REPETIR <n> [<comandos>] - Repetir comandos n veces")
        print("  PROC <nombre> ... FIN   - Definir procedimiento")
        print("  <nombre_proc>           - Ejecutar procedimiento")
        print("  LIMPIAR     - Limpiar pantalla")
        print("  LISTAR      - Mostrar procedimientos definidos")
        print("  HISTORIAL   - Mostrar comandos ejecutados")
        
        print("\nOPERACIONES:")
        print("  PUEDO <n>    - Esperar n segundos")
        print("  CIRCULO <r>  - Dibujar círculo de radio r")
        print("  RECT <ancho> <alto> - Dibujar rectángulo")
        print("  POLIG <lados> <long> - Dibujar polígono regular")
        
        print("\nVARIABLES:")
        print("  HACER \"<nombre> <valor> - Crear variable")
        print("  USAR <nombre>          - Usar valor de variable")
        
        print("\nUTILIDADES:")
        print("  AYUDA       - Mostrar esta ayuda")
        print("  SALIR       - Salir del programa")
        print()

    def ejecutar_comando(self, comando):
        """Ejecuta un comando de Mini LOGO"""
        partes = comando.strip().split()
        if not partes:
            return True
            
        cmd = partes[0].upper()
        args = partes[1:]
        
        # Guardar en historial (excepto comandos internos)
        if cmd not in ['AYUDA', 'SALIR', 'HISTORIAL', 'LISTAR']:
            self.historial.append(comando)
        
        # Comandos básicos de movimiento
        if cmd == 'AV':
            if len(args) >= 1:
                try:
                    pasos = self._evaluar_expresion(args[0])
                    self.tortuga.forward(pasos)
                except:
                    print(f"Error: '{args[0]}' no es un número válido")
            else:
                print("Error: AV necesita un número de pasos")
                
        elif cmd == 'RE':
            if len(args) >= 1:
                try:
                    pasos = self._evaluar_expresion(args[0])
                    self.tortuga.backward(pasos)
                except:
                    print(f"Error: '{args[0]}' no es un número válido")
            else:
                print("Error: RE necesita un número de pasos")
                
        elif cmd == 'GI':
            if len(args) >= 1:
                try:
                    grados = self._evaluar_expresion(args[0])
                    self.tortuga.left(grados)
                except:
                    print(f"Error: '{args[0]}' no es un número válido")
            else:
                print("Error: GI necesita un número de grados")
                
        elif cmd == 'GD':
            if len(args) >= 1:
                try:
                    grados = self._evaluar_expresion(args[0])
                    self.tortuga.right(grados)
                except:
                    print(f"Error: '{args[0]}' no es un número válido")
            else:
                print("Error: GD necesita un número de grados")
                
        elif cmd == 'HO':
            self.tortuga.penup()
            self.tortuga.home()
            if self.lapiz_abajo:
                self.tortuga.pendown()
                
        # Control de lápiz
        elif cmd == 'BP':
            self.tortuga.pendown()
            self.lapiz_abajo = True
            
        elif cmd == 'SP':
            self.tortuga.penup()
            self.lapiz_abajo = False
            
        # Apariencia
        elif cmd == 'COLOR':
            if args:
                color = ' '.join(args).lower()
                try:
                    self.tortuga.color(color)
                except:
                    print(f"Error: '{color}' no es un color válido")
            else:
                print("Error: COLOR necesita un nombre de color")
                
        elif cmd == 'GROSOR':
            if len(args) >= 1:
                try:
                    grosor = int(self._evaluar_expresion(args[0]))
                    self.tortuga.pensize(max(1, grosor))
                except:
                    print(f"Error: '{args[0]}' no es un número válido")
            else:
                print("Error: GROSOR necesita un número")
                
        elif cmd == 'OT':
            self.tortuga.hideturtle()
            
        elif cmd == 'MT':
            self.tortuga.showturtle()
            
        # Control de programa
        elif cmd == 'REPETIR':
            if len(args) >= 2:
                try:
                    veces = int(self._evaluar_expresion(args[0]))
                    # Encontrar los comandos entre corchetes
                    comando_str = ' '.join(args[1:])
                    if '[' in comando_str and ']' in comando_str:
                        inicio = comando_str.find('[') + 1
                        fin = comando_str.rfind(']')
                        comandos_repetir = comando_str[inicio:fin].strip()
                        
                        for _ in range(veces):
                            # Dividir por puntos y comas si existen
                            if ';' in comandos_repetir:
                                subcomandos = comandos_repetir.split(';')
                                for sub in subcomandos:
                                    if sub.strip():
                                        self.ejecutar_comando(sub.strip())
                            else:
                                self.ejecutar_comando(comandos_repetir)
                    else:
                        print("Error: Los comandos deben estar entre [ ]")
                except:
                    print("Error en comando REPETIR")
            else:
                print("Error: REPETIR necesita número y comandos entre [ ]")
                
        elif cmd == 'PROC':
            if len(args) >= 1:
                nombre = args[0].upper()
                print(f"Definiendo procedimiento: {nombre}")
                print("Escribe los comandos (escribe 'FIN' en una línea para terminar):")
                
                comandos_proc = []
                while True:
                    linea = input("PROC> ").strip()
                    if linea.upper() == 'FIN':
                        break
                    comandos_proc.append(linea)
                
                self.procedimientos[nombre] = comandos_proc
                print(f"Procedimiento '{nombre}' definido con {len(comandos_proc)} comandos")
            else:
                print("Error: PROC necesita un nombre")
                
        elif cmd in self.procedimientos:
            # Ejecutar procedimiento definido por el usuario
            print(f"Ejecutando procedimiento: {cmd}")
            for comando_proc in self.procedimientos[cmd]:
                self.ejecutar_comando(comando_proc)
                
        elif cmd == 'LIMPIAR':
            self.tortuga.clear()
            
        elif cmd == 'LISTAR':
            print("\n=== PROCEDIMIENTOS DEFINIDOS ===")
            if self.procedimientos:
                for nombre, comandos in self.procedimientos.items():
                    print(f"{nombre}:")
                    for i, cmd in enumerate(comandos, 1):
                        print(f"  {i}. {cmd}")
            else:
                print("No hay procedimientos definidos")
            print()
            
        elif cmd == 'HISTORIAL':
            print("\n=== HISTORIAL DE COMANDOS ===")
            for i, cmd in enumerate(self.historial[-20:], 1):  # Últimos 20
                print(f"{i:3}. {cmd}")
            print()
            
        # Operaciones
        elif cmd == 'PUEDO':
            if len(args) >= 1:
                try:
                    segundos = float(self._evaluar_expresion(args[0]))
                    turtle.delay(segundos * 100)  # Convertir a milisegundos aproximados
                except:
                    print(f"Error: '{args[0]}' no es un número válido")
            else:
                print("Error: PUEDO necesita un número de segundos")
                
        elif cmd == 'CIRCULO':
            if len(args) >= 1:
                try:
                    radio = self._evaluar_expresion(args[0])
                    self.tortuga.circle(radio)
                except:
                    print(f"Error: '{args[0]}' no es un número válido")
            else:
                print("Error: CIRCULO necesita un radio")
                
        elif cmd == 'RECT':
            if len(args) >= 2:
                try:
                    ancho = self._evaluar_expresion(args[0])
                    alto = self._evaluar_expresion(args[1])
                    
                    # Dibujar rectángulo
                    for _ in range(2):
                        self.tortuga.forward(ancho)
                        self.tortuga.left(90)
                        self.tortuga.forward(alto)
                        self.tortuga.left(90)
                except:
                    print("Error en comando RECT")
            else:
                print("Error: RECT necesita ancho y alto")
                
        elif cmd == 'POLIG':
            if len(args) >= 2:
                try:
                    lados = int(self._evaluar_expresion(args[0]))
                    longitud = self._evaluar_expresion(args[1])
                    
                    angulo = 360 / lados
                    for _ in range(lados):
                        self.tortuga.forward(longitud)
                        self.tortuga.left(angulo)
                except:
                    print("Error en comando POLIG")
            else:
                print("Error: POLIG necesita número de lados y longitud")
                
        # Variables
        elif cmd == 'HACER':
            if len(args) >= 2:
                nombre = args[0]
                if nombre.startswith('"'):
                    nombre = nombre[1:]
                valor = self._evaluar_expresion(args[1])
                self.variables[nombre] = valor
                print(f"Variable '{nombre}' = {valor}")
            else:
                print("Error: HACER necesita nombre y valor")
                
        # Utilidades
        elif cmd == 'AYUDA':
            self.ayuda()
            
        elif cmd == 'SALIR':
            print("¡Hasta luego! Gracias por usar Mini LOGO")
            return False
            
        else:
            # Intentar ejecutar como expresión matemática simple
            try:
                resultado = self._evaluar_expresion(' '.join(partes))
                print(f"Resultado: {resultado}")
            except:
                print(f"Error: Comando '{cmd}' no reconocido")
        
        return True
    
    def _evaluar_expresion(self, expresion):
        """Evalúa una expresión matemática simple, permitiendo variables"""
        # Reemplazar variables
        for var, valor in self.variables.items():
            expresion = expresion.replace(var, str(valor))
        
        # Operaciones básicas
        if '+' in expresion:
            partes = expresion.split('+')
            return sum(float(p.strip()) for p in partes)
        elif '-' in expresion and expresion.count('-') == 1 and not expresion.startswith('-'):
            partes = expresion.split('-')
            return float(partes[0].strip()) - float(partes[1].strip())
        elif '*' in expresion:
            partes = expresion.split('*')
            resultado = 1
            for p in partes:
                resultado *= float(p.strip())
            return resultado
        elif '/' in expresion:
            partes = expresion.split('/')
            resultado = float(partes[0].strip())
            for p in partes[1:]:
                resultado /= float(p.strip())
            return resultado
        else:
            # Si no hay operadores, es solo un número
            return float(expresion.strip())
    
    def ejecutar_archivo(self, nombre_archivo):
        """Ejecuta comandos desde un archivo"""
        try:
            with open(nombre_archivo, 'r') as f:
                lineas = f.readlines()
                
            print(f"Ejecutando archivo: {nombre_archivo}")
            for linea in lineas:
                linea = linea.strip()
                if linea and not linea.startswith('#'):  # Ignorar líneas vacías y comentarios
                    print(f"> {linea}")
                    self.ejecutar_comando(linea)
                    
        except FileNotFoundError:
            print(f"Error: Archivo '{nombre_archivo}' no encontrado")
    
    def modo_interactivo(self):
        """Modo interactivo de Mini LOGO"""
        print("=== MODO INTERACTIVO MINI LOGO ===")
        continuar = True
        
        while continuar:
            try:
                entrada = input("LOGO> ").strip()
                if entrada:
                    continuar = self.ejecutar_comando(entrada)
            except KeyboardInterrupt:
                print("\n\nInterrumpido. Escribe 'SALIR' para salir.")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        turtle.bye()

# ===========================================
# EJEMPLOS DE PROGRAMAS EN MINI LOGO
# ===========================================
def crear_ejemplos():
    """Crea archivos de ejemplo con programas en Mini LOGO"""
    
    # Ejemplo 1: Dibujar un cuadrado
    cuadrado = """# Ejemplo 1: Cuadrado básico
COLOR azul
GROSOR 3
AV 100
GD 90
AV 100
GD 90
AV 100
GD 90
AV 100
HO
"""
    
    # Ejemplo 2: Dibujo con procedimientos
    casa = """# Ejemplo 2: Casa con procedimientos
PROC TRIANGULO
  AV 100
  GI 120
  AV 100
  GI 120
  AV 100
FIN

PROC CUADRADO
  REPETIR 4 [AV 100 GD 90]
FIN

COLOR marron
GROSOR 2
CUADRADO
AV 100
GI 30
COLOR rojo
TRIANGULO
"""
    
    # Ejemplo 3: Patrón geométrico complejo
    patron = """# Ejemplo 3: Patrón geométrico
COLOR verde
GROSOR 1

REPETIR 36 [
  AV 100
  RE 100
  GD 10
]

COLOR rojo
GROSOR 2
OT
SP
AV 150
BP
MT

REPETIR 8 [
  CIRCULO 50
  GD 45
]
"""
    
    # Guardar ejemplos
    with open("cuadrado.logo", "w") as f:
        f.write(cuadrado)
    
    with open("casa.logo", "w") as f:
        f.write(casa)
    
    with open("patron.logo", "w") as f:
        f.write(patron)
    
    print("Archivos de ejemplo creados:")
    print("  - cuadrado.logo: Dibuja un cuadrado básico")
    print("  - casa.logo: Dibuja una casa usando procedimientos")
    print("  - patron.logo: Crea un patrón geométrico complejo")

# ===========================================
# PROGRAMA PRINCIPAL
# ===========================================
if __name__ == "__main__":
    logo = MiniLOGO()
    
    # Verificar si se pasó un archivo como argumento
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        logo.ejecutar_archivo(archivo)
        print("\nPresiona ENTER para continuar en modo interactivo...")
        input()
    
    # Crear archivos de ejemplo
    crear_ejemplos()
    
    # Iniciar modo interactivo
    logo.modo_interactivo()
