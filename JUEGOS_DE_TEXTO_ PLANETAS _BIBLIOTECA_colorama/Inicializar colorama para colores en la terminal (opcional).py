import sys
import time
import random
from collections import defaultdict

# Inicializar colorama para colores en la terminal (opcional)
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False

# Clase Jugador
class Jugador:
    def __init__(self, nombre="Tomsom"):
        self.nombre = nombre
        self.inventario = []
        self.salud = 100
        self.energia = 100
        self.experiencia = 0
        self.nivel = 1
        self.habilidades = ['explorar', 'atacar']
        self.equipo = []
    
    def mostrar_estado(self):
        print("\n" + "-"*30)
        print(f"{Fore.CYAN if COLOR_ENABLED else ''}Estado de {self.nombre}{Style.RESET_ALL}:")
        print(f"{Fore.RED if COLOR_ENABLED else ''}Salud:{Style.RESET_ALL} {self.salud}")
        print(f"{Fore.YELLOW if COLOR_ENABLED else ''}Energía:{Style.RESET_ALL} {self.energia}")
        print(f"{Fore.GREEN if COLOR_ENABLED else ''}Experiencia:{Style.RESET_ALL} {self.experiencia}")
        print(f"{Fore.MAGENTA if COLOR_ENABLED else ''}Nivel:{Style.RESET_ALL} {self.nivel}")
        print(f"{Fore.BLUE if COLOR_ENABLED else ''}Habilidades:{Style.RESET_ALL} {', '.join(self.habilidades)}")
        print(f"{Fore.WHITE if COLOR_ENABLED else ''}Equipo:{Style.RESET_ALL} {', '.join(self.equipo) if self.equipo else 'Ninguno'}")
        print(f"{Fore.WHITE if COLOR_ENABLED else ''}Inventario:{Style.RESET_ALL} {', '.join(self.inventario) if self.inventario else 'Vacío'}")
        print("-"*30 + "\n")

# Clase Personaje
class Personaje:
    def __init__(self, nombre, descripcion, dialogos, pistas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.dialogos = dialogos  # Diccionario de acciones y respuestas
        self.pistas = pistas      # Diccionario de pistas proporcionadas
    
    def hablar(self, accion):
        if accion in self.dialogos:
            print(f"{Fore.GREEN if COLOR_ENABLED else ''}{self.nombre}{Style.RESET_ALL} dice: '{self.dialogos[accion]}'")
            if accion in self.pistas:
                print(f"Pista: {self.pistas[accion]}")
        else:
            print(f"{self.nombre} no tiene nada que decir sobre eso.")

# Clase Escenario
class Escenario:
    def __init__(self, nombre, descripcion, conexiones, objetos=None, personajes=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.conexiones = conexiones  # Diccionario de direcciones y destinos
        self.objetos = objetos if objetos else []
        self.personajes = personajes if personajes else []

# Clase Acertijo
class Acertijo:
    def __init__(self, pregunta, opciones, respuesta_correcta, recompensa=None):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.recompensa = recompensa  # Objeto a otorgar al resolver
    
    def resolver(self):
        print("\n" + Fore.YELLOW + self.pregunta + Style.RESET_ALL)
        for idx, opcion in enumerate(self.opciones, 1):
            print(f"{idx}. {opcion}")
        try:
            respuesta = int(input("Selecciona la opción correcta (1-4): "))
            if self.opciones[respuesta - 1].lower() == self.respuesta_correcta.lower():
                print(Fore.GREEN + "¡Respuesta correcta!" + Style.RESET_ALL)
                if self.recompensa:
                    print(f"Has recibido: {self.recompensa}")
                return True
            else:
                print(Fore.RED + "Respuesta incorrecta. Intenta de nuevo." + Style.RESET_ALL)
                return False
        except (IndexError, ValueError):
            print(Fore.RED + "Entrada no válida. Por favor, selecciona una opción del 1 al 4." + Style.RESET_ALL)
            return False

# Clase Juego
class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.ubicacion = "Base Espacial"
        self.mapa = {}
        self.comandos = {}
        self.acertijos = {}
        self.estado = {"nave_reparada": False}
        self.setup_juego()
    
    def setup_juego(self):
        # Definir escenarios
        self.mapa["Base Espacial"] = Escenario(
            nombre="Base Espacial",
            descripcion="Estás en la
