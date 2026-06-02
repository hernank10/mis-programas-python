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
            descripcion="Estás en la base de lanzamiento de tu nave espacial. Hay caminos a diferentes planetas.",
            conexiones={'este': 'Planeta Verde', 'oeste': 'Planeta Azul'}
        )
        
        self.mapa["Planeta Verde"] = Escenario(
            nombre="Planeta Verde",
            descripcion="Has llegado a un planeta cubierto de vegetación. Hay una cueva al norte y una montaña al sur.",
            conexiones={'oeste': 'Base Espacial', 'norte': 'Cueva', 'sur': 'Montaña'},
            objetos=['ramas']
        )
        
        self.mapa["Planeta Azul"] = Escenario(
            nombre="Planeta Azul",
            descripcion="Este planeta tiene océanos extensos y ciudades flotantes. Hay una playa al este y una ciudad al oeste.",
            conexiones={'este': 'Playa', 'oeste': 'Ciudad Flotante', 'este': 'Base Espacial'},
            objetos=['conchas']
        )
        
        self.mapa["Cueva"] = Escenario(
            nombre="Cueva",
            descripcion="Una oscura cueva con sonidos misteriosos. Hay una lámpara en la pared.",
            conexiones={'sur': 'Planeta Verde'},
            objetos=['lámpara'],
            personajes=[Personaje(
                nombre="Guardia de la Cueva",
                descripcion="Un guardia fantasma que protege la cueva.",
                dialogos={"ayuda": "Debes encontrar la llave oculta en la cueva."},
                pistas={"ayuda": "Busca detrás de la lámpara."}
            )]
        )
        
        self.mapa["Montaña"] = Escenario(
            nombre="Montaña",
            descripcion="Una alta montaña con nieve en la cima. Hay un sendero que lleva a la cima.",
            conexiones={'norte': 'Planeta Verde'},
            objetos=['hielo']
        )
        
        self.mapa["Playa"] = Escenario(
            nombre="Playa",
            descripcion="Una playa soleada con arena blanca. Puedes nadar hacia el horizonte.",
            conexiones={'oeste': 'Planeta Azul'},
            objetos=['conchas']
        )
        
        self.mapa["Ciudad Flotante"] = Escenario(
            nombre="Ciudad Flotante",
            descripcion="Una ciudad construida sobre el agua con tecnología avanzada.",
            conexiones={'este': 'Planeta Azul'},
            objetos=['tecnología avanzada']
        )
        
        # Definir acertijos
        self.acertijos["cueva_puzzle"] = Acertijo(
            pregunta="¿Qué tiene un ojo pero no puede ver?",
            opciones=["Perro", "Aguja", "Tornado", "Piano"],
            respuesta_correcta="aguja",
            recompensa="llave"
        )
        
        self.acertijos["montaña_puzzle"] = Acertijo(
            pregunta="¿Cuál es el punto más alto de la Tierra?",
            opciones=["Monte Everest", "K2", "Kangchenjunga", "Lhotse"],
            respuesta_correcta="Monte Everest",
            recompensa="herramienta de reparación"
        )
        
        # Definir comandos
        self.definir_comandos()
    
    def definir_comandos(self):
        # Navegación
        self.comandos.update({
            "ir norte": self.ir_norte,
            "ir sur": self.ir_sur,
            "ir este": self.ir_este,
            "ir oeste": self.ir_oeste,
            "subir": self.subir,
            "bajar": self.bajar,
            "entrar": self.entrar,
            "salir": self.salir,
            "explorar": self.explorar,
            "caminar": self.caminar,
            "viajar a": self.viajar_a,
            "saltar": self.saltar,
            "navegar río": self.navegar_rio,
            "descender escaleras": self.descender_escaleras,
            "ascender torre": self.ascender_torre,
            "caminar hacia": self.caminar_hacia,
            "teletransportarse a": self.teletransportarse_a,
            "seguir camino": self.seguir_camino,
            "retornar": self.retornar
        })
        
        # Interacción con Objetos
        self.comandos.update({
            "examinar": self.examinar,
            "tomar": self.tomar,
            "dejar": self.dejar,
            "usar": self.usar,
            "combinar": self.combinar,
            "mirar alrededor": self.mirar_alrededor,
            "abrir": self.abrir,
            "cerrar": self.cerrar,
            "sacar": self.sacar,
            "guardar": self.guardar_objeto,
            "entregar": self.entregar_objeto,
            "insertar": self.insertar_objeto,
            "quitar": self.quitar_objeto,
            "destruir": self.destruir_objeto,
            "limpiar": self.limpiar_objeto,
            "encender": self.encender_objeto,
            "apagar": self.apagar_objeto,
            "activar": self.activar_objeto,
            "desactivar": self.desactivar_objeto,
            "revisar": self.revisar_objeto
        })
        
        # Interacción con Personajes
        self.comandos.update({
            "hablar con": self.hablar_con,
            "saludar": self.saludar,
            "preguntar a": self.preguntar_a,
            "interrogar": self.interrogar,
            "ayudar a": self.ayudar_a,
            "ofrecer ayuda a": self.ofrecer_ayuda_a,
            "ignorar a": self.ignorar_a,
            "ofrecer": self.ofrecer_objeto,
            "aceptar": self.aceptar_objeto,
            "rechazar": self.rechazar_objeto,
            "seguir a": self.seguir_a,
            "atacar a": self.atacar_a,
            "proteger a": self.proteger_a,
            "cooperar con": self.cooperar_con,
            "discutir con": self.discutir_con,
            "mentir a": self.mentir_a,
            "confesar a": self.confesar_a,
            "preguntar a": self.preguntar_a_personaje,
            "escuchar a": self.escuchar_a,
            "olvidar a": self.olvidar_a
        })
        
        # Gestión de Inventario
        self.comandos.update({
            "inventario": self.ver_inventario,
            "listar inventario": self.ver_inventario,
            "gestionar inventario": self.gestionar_inventario,
            "ordenar inventario": self.ordenar_inventario,
            "limpiar inventario": self.limpiar_inventario,
            "comparar": self.comparar_objetos,
            "equipo": self.equipo_objeto,
            "desequipo": self.desequipo_objeto,
            "equipar": self.equipar_objeto,
            "desactivar": self.desactivar_equipo,
            "activar": self.activar_equipo,
            "descartar": self.descartar_objeto,
            "vender": self.vender_objeto,
            "comprar": self.comprar_objeto,
            "evaluar": self.evaluar_objeto,
            "reparar": self.reparar_objeto,
            "mejorar": self.mejorar_objeto,
            "guardar inventario": self.guardar_inventario,
            "cargar inventario": self.cargar_inventario
        })
        
        # Estado del Jugador
        self.comandos.update({
            "mostrar estado": self.jugador.mostrar_estado,
            "ver salud": self.ver_salud,
            "ver energía": self.ver_energia,
            "ver experiencia": self.ver_experiencia,
            "ver nivel": self.ver_nivel,
            "ver habilidades": self.ver_habilidades,
            "ver estadísticas": self.ver_estadisticas,
            "ver misión actual": self.ver_mision_actual,
            "ver progreso": self.ver_progreso,
            "ver puntos de habilidad": self.ver_puntos_habilidad,
            "ver puntos de vida": self.ver_puntos_vida,
            "ver puntos de magia": self.ver_puntos_magia,
            "ver puntos de resistencia": self.ver_puntos_resistencia,
            "ver atributos": self.ver_atributos,
            "ver equipo": self.ver_equipo,
            "ver puntos de acción": self.ver_puntos_accion,
            "ver puntos de movimiento": self.ver_puntos_movimiento,
            "ver estado de ánimo": self.ver_estado_animo,
            "ver habilidades desbloqueadas": self.ver_habilidades_desbloqueadas,
            "ver logros": self.ver_logros
        })
        
        # Ayuda y otros comandos
        self.comandos.update({
            "ayuda": self.ayuda,
            "info": self.info,
            "repetir": self.repetir,
            "guardar": self.guardar_juego,
            "cargar": self.cargar_juego,
            "salir del juego": self.salir_juego,
            "acerca de": self.acerca_de,
            "configuración": self.configuracion,
            "música activar": self.musica_activar,
            "música desactivar": self.musica_desactivar,
            "modo fácil": self.modo_facil,
            "modo difícil": self.modo_dificil,
            "anular último comando": self.anular_ultimo_comando
        })
        
    # Funciones de Navegación
    def ir_norte(self, argumentos):
        self.mover("norte")
    
    def ir_sur(self, argumentos):
        self.mover("sur")
    
    def ir_este(self, argumentos):
        self.mover("este")
    
    def ir_oeste(self, argumentos):
        self.mover("oeste")
    
    def subir(self, argumentos):
        print("Subes por la colina.")
    
    def bajar(self, argumentos):
        print("Bajas por la colina.")
    
    def entrar(self, argumentos):
        print("Entrando al edificio cercano.")
    
    def salir(self, argumentos):
        print("Saliendo del edificio.")
    
    def explorar(self, argumentos):
        print("Exploras el área a tu alrededor.")
    
    def caminar(self, argumentos):
        print("Caminas hacia adelante.")
    
    def viajar_a(self, argumentos):
        destino = argumentos
        if destino in self.mapa:
            self.ubicacion = destino
            print(f"Te has viajado a {destino}.")
            print(self.mapa[self.ubicacion].descripcion)
        else:
            print("No puedes viajar a ese lugar.")
    
    def saltar(self, argumentos):
        print("Saltas alto en el aire.")
    
    def navegar_rio(self, argumentos):
        print("Navegas por el río.")
    
    def descender_escaleras(self, argumentos):
        print("Descendes las escaleras hacia abajo.")
    
    def ascender_torre(self, argumentos):
        print("Ascendes la torre hacia arriba.")
    
    def caminar_hacia(self, argumentos):
        direccion = argumentos
        print(f"Caminas hacia el {direccion}.")
    
    def teletransportarse_a(self, argumentos):
        destino = argumentos
        if destino in self.mapa:
            self.ubicacion = destino
            print(f"Te has teletransportado a {destino}.")
            print(self.mapa[self.ubicacion].descripcion)
        else:
            print("No puedes teletransportarte a ese lugar.")
    
    def seguir_camino(self, argumentos):
        print("Sigues el camino hacia adelante.")
    
    def retornar(self, argumentos):
        print("Retornas al punto anterior.")
    
    # Funciones de Interacción con Objetos
    def examinar(self, argumentos):
        objeto = argumentos
        if objeto in self.mapa[self.ubicacion].objetos:
            print(f"Examinas el {objeto}.")
            # Descripciones de objetos
            descripciones = {
                "llave": "Una llave dorada antigua, parece muy valiosa.",
                "ramas": "Ramas secas de árboles que podrían ser útiles.",
                "conchas": "Conchas marinas de colores vibrantes.",
                "lámpara": "Una lámpara de aceite que puede iluminar la cueva.",
                "cuchillo": "Un cuchillo afilado, útil para cortar."
            }
            print(descripciones.get(objeto, "No hay nada especial sobre ese objeto."))
        else:
            print("No ves ese objeto aquí.")
    
    def tomar(self, argumentos):
        objeto = argumentos
        if objeto in self.mapa[self.ubicacion].objetos:
            self.jugador.inventario.append(objeto)
            self.mapa[self.ubicacion].objetos.remove(objeto)
            print(f"Has tomado el {objeto}.")
        else:
            print("No ves ese objeto aquí.")
    
    def dejar(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.inventario:
            self.jugador.inventario.remove(objeto)
            self.mapa[self.ubicacion].objetos.append(objeto)
            print(f"Has dejado el {objeto}.")
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def usar(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.inventario:
            print(f"Usas el {objeto}.")
            # Implementar efectos de usar objetos
            if objeto == "llave":
                if self.ubicacion == "Cueva":
                    if "llave" in self.jugador.inventario:
                        print("Usas la llave para abrir la puerta secreta.")
                        # Agregar lógica para desbloquear áreas
                else:
                    print("No hay nada que puedas hacer con la llave aquí.")
            elif objeto == "cuchillo":
                print("Usas el cuchillo para cortar la cuerda.")
                # Agregar lógica para resolver puzzles
            else:
                print("No puedes usar ese objeto de esa manera.")
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def combinar(self, argumentos):
        objetos = argumentos.split(" y ")
        if len(objetos) != 2:
            print("Debes especificar dos objetos para combinar.")
            return
        obj1, obj2 = objetos
        if obj1 in self.jugador.inventario and obj2 in self.jugador.inventario:
            # Definir combinaciones posibles
            combinaciones = {
                ("ramas", "lámpara"): "antorcha",
                ("conchas", "ramas"): "decoración",
                ("llave", "herramienta de reparación"): "llave completa"
            }
            key = tuple(sorted([obj1, obj2]))
            if key in combinaciones:
                nuevo_objeto = combinaciones[key]
                self.jugador.inventario.remove(obj1)
                self.jugador.inventario.remove(obj2)
                self.jugador.inventario.append(nuevo_objeto)
                print(f"Has combinado {obj1} y {obj2} para crear {nuevo_objeto}.")
            else:
                print("No puedes combinar esos objetos.")
        else:
            print("No tienes ambos objetos en tu inventario.")
    
    def mirar_alrededor(self, argumentos):
        print(self.mapa[self.ubicacion].descripcion)
        if self.mapa[self.ubicacion].objetos:
            print("Objetos visibles:")
            for obj in self.mapa[self.ubicacion].objetos:
                print(f"- {obj}")
        if self.mapa[self.ubicacion].personajes:
            print("Personajes presentes:")
            for personaje in self.mapa[self.ubicacion].personajes:
                print(f"- {personaje.nombre}")
    
    def abrir(self, argumentos):
        objeto = argumentos
        print(f"Intentas abrir el {objeto}.")
        # Implementar lógica para abrir objetos
        if objeto == "puerta":
            if "llave completa" in self.jugador.inventario:
                print("La puerta se abre revelando una sala secreta.")
                # Agregar nueva área o objetos
                self.mapa["Sala Secreta"] = Escenario(
                    nombre="Sala Secreta",
                    descripcion="Una pequeña sala con un cofre en el centro.",
                    conexiones={'oeste': 'Cueva'},
                    objetos=['tesoro']
                )
                print("Has descubierto una nueva área: Sala Secreta.")
            else:
                print("La puerta está cerrada. Necesitas una llave completa para abrirla.")
        else:
            print("No hay nada que puedas hacer con ese objeto.")
    
    def cerrar(self, argumentos):
        objeto = argumentos
        print(f"Intentas cerrar el {objeto}.")
        # Implementar lógica para cerrar objetos
        if objeto == "puerta":
            print("La puerta ahora está cerrada.")
        else:
            print("No hay nada que puedas hacer con ese objeto.")
    
    def sacar(self, argumentos):
        partes = argumentos.split(" del ")
        if len(partes) != 2:
            print("Formato incorrecto. Usa 'sacar [objeto] del [contenedor]'.")
            return
        objeto, contenedor = partes
        if objeto in self.mapa[self.ubicacion].objetos:
            print(f"Has sacado el {objeto} del {contenedor}.")
        else:
            print(f"No encuentras {objeto} en el {contenedor}.")
    
    def guardar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Guardas el {objeto}.")
        # Implementar lógica para guardar objetos
    
    def entregar_objeto(self, argumentos):
        partes = argumentos.split(" a ")
        if len(partes) != 2:
            print("Formato incorrecto. Usa 'entregar [objeto] a [personaje]'.")
            return
        objeto, personaje = partes
        if objeto in self.jugador.inventario:
            print(f"Entregas el {objeto} a {personaje}.")
            self.jugador.inventario.remove(objeto)
            # Implementar lógica para dar recompensas o cambiar estados
        else:
            print(f"No tienes {objeto} en tu inventario.")
    
    def insertar_objeto(self, argumentos):
        partes = argumentos.split(" en ")
        if len(partes) != 2:
            print("Formato incorrecto. Usa 'insertar [objeto] en [objeto]'.")
            return
        objeto, contenedor = partes
        print(f"Insertas el {objeto} en el {contenedor}.")
        # Implementar lógica para insertar objetos
    
    def quitar_objeto(self, argumentos):
        partes = argumentos.split(" de ")
        if len(partes) != 2:
            print("Formato incorrecto. Usa 'quitar [objeto] de [objeto]'.")
            return
        objeto, contenedor = partes
        print(f"Has quitado el {objeto} del {contenedor}.")
        # Implementar lógica para quitar objetos
    
    def destruir_objeto(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.inventario:
            self.jugador.inventario.remove(objeto)
            print(f"Has destruido el {objeto}.")
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def limpiar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Has limpiado el {objeto}.")
        # Implementar lógica para limpiar objetos
    
    def encender_objeto(self, argumentos):
        objeto = argumentos
        print(f"Has encendido el {objeto}.")
        # Implementar lógica para encender objetos
    
    def apagar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Has apagado el {objeto}.")
        # Implementar lógica para apagar objetos
    
    def activar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Has activado el {objeto}.")
        # Implementar lógica para activar objetos
    
    def desactivar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Has desactivado el {objeto}.")
        # Implementar lógica para desactivar objetos
    
    def revisar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Revisas el {objeto}.")
        # Implementar lógica para revisar objetos
    
    # Funciones de Interacción con Personajes
    def hablar_con(self, argumentos):
        nombre = argumentos
        for personaje in self.mapa[self.ubicacion].personajes:
            if personaje.nombre.lower() == nombre.lower():
                accion = input(f"¿Qué quieres preguntar a {nombre}? (ayuda/salir): ").lower()
                personaje.hablar(accion)
                # Implementar lógica basada en diálogos
                if accion == "ayuda":
                    # Verificar si el jugador tiene la llave para avanzar
                    if "llave completa" in self.jugador.inventario:
                        print("Tienes la llave completa. Puedes abrir la puerta secreta.")
                return
        print("No encuentras a esa persona aquí.")
    
    def saludar(self, argumentos):
        print("Saludas amablemente.")
    
    def preguntar_a(self, argumentos):
        print("Preguntas sobre algo específico.")
    
    def interrogar(self, argumentos):
        print("Interrogas a alguien intensamente.")
    
    def ayudar_a(self, argumentos):
        print("Ofreces tu ayuda.")
    
    def ofrecer_ayuda_a(self, argumentos):
        print("Ofreces ayuda a alguien.")
    
    def ignorar_a(self, argumentos):
        print("Ignoras a la persona.")
    
    def ofrecer_objeto(self, argumentos):
        partes = argumentos.split(" a ")
        if len(partes) != 2:
            print("Formato incorrecto. Usa 'ofrecer [objeto] a [personaje]'.")
            return
        objeto, personaje = partes
        if objeto in self.jugador.inventario:
            print(f"Ofreces el {objeto} a {personaje}.")
            self.jugador.inventario.remove(objeto)
            # Implementar lógica para dar recompensas
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def aceptar_objeto(self, argumentos):
        partes = argumentos.split(" de ")
        if len(partes) != 2:
            print("Formato incorrecto. Usa 'aceptar [objeto] de [personaje]'.")
            return
        objeto, personaje = partes
        print(f"Has aceptado el {objeto} de {personaje}.")
        self.jugador.inventario.append(objeto)
        # Implementar lógica para recibir objetos
    
    def rechazar_objeto(self, argumentos):
        partes = argumentos.split(" de ")
        if len(partes) != 2:
            print("Formato incorrecto. Usa 'rechazar [objeto] de [personaje]'.")
            return
        objeto, personaje = partes
        print(f"Has rechazado el {objeto} de {personaje}.")
        # Implementar lógica para rechazar objetos
    
    def seguir_a(self, argumentos):
        nombre = argumentos
        print(f"Sigues a {nombre}.")
        # Implementar lógica para seguir personajes
    
    def atacar_a(self, argumentos):
        nombre = argumentos
        print(f"Atacas a {nombre}.")
        # Implementar lógica para atacar personajes
    
    def proteger_a(self, argumentos):
        nombre = argumentos
        print(f"Proteges a {nombre}.")
        # Implementar lógica para proteger personajes
    
    def cooperar_con(self, argumentos):
        nombre = argumentos
        print(f"Cooperas con {nombre}.")
        # Implementar lógica para cooperar con personajes
    
    def discutir_con(self, argumentos):
        nombre = argumentos
        print(f"Discutes con {nombre}.")
        # Implementar lógica para discutir con personajes
    
    def mentir_a(self, argumentos):
        nombre = argumentos
        print(f"Le mientes a {nombre}.")
        # Implementar lógica para mentir a personajes
    
    def confesar_a(self, argumentos):
        nombre = argumentos
        print(f"Confiesas a {nombre}.")
        # Implementar lógica para confesar a personajes
    
    def preguntar_a_personaje(self, argumentos):
        print("Haces una pregunta específica.")
    
    def escuchar_a(self, argumentos):
        print("Escuchas atentamente.")
    
    def olvidar_a(self, argumentos):
        nombre = argumentos
        print(f"Olvidas a {nombre}.")
        # Implementar lógica para olvidar personajes
    
    # Funciones de Gestión de Inventario
    def ver_inventario(self, argumentos=None):
        if self.jugador.inventario:
            print("\nInventario:")
            for obj in self.jugador.inventario:
                print(f"- {obj}")
        else:
            print("\nTu inventario está vacío.")
    
    def gestionar_inventario(self, argumentos):
        print("Gestionas tu inventario.")
        # Implementar lógica para gestionar inventario
    
    def ordenar_inventario(self, argumentos):
        self.jugador.inventario.sort()
        print("Has ordenado tu inventario.")
    
    def limpiar_inventario(self, argumentos):
        self.jugador.inventario = []
        print("Has limpiado tu inventario.")
    
    def comparar_objetos(self, argumentos):
        objetos = argumentos.split(" y ")
        if len(objetos) != 2:
            print("Debes especificar dos objetos para comparar.")
            return
        obj1, obj2 = objetos
        print(f"Comparas {obj1} y {obj2}.")
        # Implementar lógica para comparar objetos
    
    def equipo_objeto(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.inventario:
            self.jugador.equipo.append(objeto)
            self.jugador.inventario.remove(objeto)
            print(f"Has equipado el {objeto}.")
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def desequipo_objeto(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.equipo:
            self.jugador.equipo.remove(objeto)
            self.jugador.inventario.append(objeto)
            print(f"Has desequipado el {objeto}.")
        else:
            print("No tienes ese objeto equipado.")
    
    def equipar_objeto(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.inventario:
            self.jugador.equipo.append(objeto)
            self.jugador.inventario.remove(objeto)
            print(f"Has equipado el {objeto}.")
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def desactivar_equipo(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.equipo:
            print(f"Has desactivado el {objeto}.")
            # Implementar lógica para desactivar equipo
        else:
            print("No tienes ese objeto equipado.")
    
    def activar_equipo(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.equipo:
            print(f"Has activado el {objeto}.")
            # Implementar lógica para activar equipo
        else:
            print("No tienes ese objeto equipado.")
    
    def descartar_objeto(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.inventario:
            self.jugador.inventario.remove(objeto)
            print(f"Has descartado el {objeto}.")
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def vender_objeto(self, argumentos):
        objeto = argumentos
        if objeto in self.jugador.inventario:
            self.jugador.inventario.remove(objeto)
            print(f"Has vendido el {objeto}.")
            # Implementar lógica para recibir dinero
        else:
            print("No tienes ese objeto en tu inventario.")
    
    def comprar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Has comprado el {objeto}.")
        self.jugador.inventario.append(objeto)
        # Implementar lógica para gastar dinero
    
    def evaluar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Evaluas el {objeto}.")
        # Implementar lógica para evaluar objetos
    
    def reparar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Reparas el {objeto}.")
        # Implementar lógica para reparar objetos
    
    def mejorar_objeto(self, argumentos):
        objeto = argumentos
        print(f"Mejoras el {objeto}.")
        # Implementar lógica para mejorar objetos
    
    def guardar_inventario(self, argumentos):
        print("Has guardado tu inventario.")
        # Implementar lógica para guardar inventario
    
    def cargar_inventario(self, argumentos):
        print("Has cargado tu inventario.")
        # Implementar lógica para cargar inventario
    
    # Funciones de Estado del Jugador
    def ver_salud(self, argumentos):
        print(f"Salud: {self.jugador.salud}")
    
    def ver_energia(self, argumentos):
        print(f"Energía: {self.jugador.energia}")
    
    def ver_experiencia(self, argumentos):
        print(f"Experiencia: {self.jugador.experiencia}")
    
    def ver_nivel(self, argumentos):
        print(f"Nivel: {self.jugador.nivel}")
    
    def ver_habilidades(self, argumentos):
        print(f"Habilidades: {', '.join(self.jugador.habilidades)}")
    
    def ver_estadisticas(self, argumentos):
        self.jugador.mostrar_estado()
    
    def ver_mision_actual(self, argumentos):
        print("Tu misión actual es reparar la nave espacial para regresar a casa.")
    
    def ver_progreso(self, argumentos):
        print(f"Progreso: {self.jugador.experiencia}/100 experiencia.")
    
    def ver_puntos_habilidad(self, argumentos):
        print("Puntos de habilidad: 5")
    
    def ver_puntos_vida(self, argumentos):
        print(f"Puntos de vida: {self.jugador.salud}")
    
    def ver_puntos_magia(self, argumentos):
        print("Puntos de magia: 50")
    
    def ver_puntos_resistencia(self, argumentos):
        print("Puntos de resistencia: 30")
    
    def ver_atributos(self, argumentos):
        print("Atributos: Fuerza, Inteligencia, Agilidad")
    
    def ver_equipo(self, argumentos):
        if self.jugador.equipo:
            print(f"Equipo: {', '.join(self.jugador.equipo)}")
        else:
            print("No tienes equipo equipado.")
    
    def ver_puntos_accion(self, argumentos):
        print("Puntos de acción: 10")
    
    def ver_puntos_movimiento(self, argumentos):
        print("Puntos de movimiento: 5")
    
    def ver_estado_animo(self, argumentos):
        print("Estado de ánimo: Neutral")
    
    def ver_habilidades_desbloqueadas(self, argumentos):
        print(f"Habilidades desbloqueadas: {', '.join(self.jugador.habilidades)}")
    
    def ver_logros(self, argumentos):
        print("Logros: Ninguno por el momento.")
    
    # Funciones de Ayuda y Otros
    def ayuda(self, argumentos=None):
        print("\n" + Fore.CYAN + "Comandos disponibles:" + Style.RESET_ALL)
        print("1. Navegación:")
        print("   - ir norte, ir sur, ir este, ir oeste")
        print("   - subir, bajar, entrar, salir")
        print("   - explorar, caminar, viajar a, saltar")
        print("   - navegar río, descender escaleras, ascender torre")
        print("   - caminar hacia, teletransportarse a, seguir camino, retornar")
        print("2. Interacción con Objetos:")
        print("   - examinar [objeto], tomar [objeto], dejar [objeto]")
        print("   - usar [objeto], combinar [objeto1] y [objeto2]")
        print("   - mirar alrededor, abrir [objeto], cerrar [objeto]")
        print("   - sacar [objeto] del [contenedor], guardar [objeto]")
        print("   - entregar [objeto] a [personaje], insertar [objeto] en [objeto]")
        print("   - quitar [objeto] de [objeto], destruir [objeto]")
        print("   - limpiar [objeto], encender [objeto], apagar [objeto]")
        print("   - activar [objeto], desactivar [objeto], revisar [objeto]")
        print("3. Interacción con Personajes:")
        print("   - hablar con [nombre], saludar [nombre]")
        print("   - preguntar a [nombre] sobre [tema], interrogar [nombre]")
        print("   - ayudar a [nombre], ofrecer ayuda a [nombre]")
        print("   - ignorar a [nombre], ofrecer [objeto] a [nombre]")
        print("   - aceptar [objeto] de [nombre], rechazar [objeto] de [nombre]")
        print("   - seguir a [nombre], atacar a [nombre]")
        print("   - proteger a [nombre], cooperar con [nombre]")
        print("   - discutir con [nombre], mentir a [nombre]")
        print("   - confesar a [nombre], preguntar a [nombre] por [información]")
        print("   - escuchar a [nombre], olvidar a [nombre]")
        print("4. Gestión de Inventario:")
        print("   - inventario, listar inventario, gestionar inventario")
        print("   - ordenar inventario, limpiar inventario")
        print("   - comparar [objeto1] y [objeto2], equipo [objeto]")
        print("   - desequipo [objeto], equipar [objeto]")
        print("   - desactivar [objeto], activar [objeto]")
        print("   - descartar [objeto], vender [objeto], comprar [objeto]")
        print("   - evaluar [objeto], reparar [objeto], mejorar [objeto]")
        print("   - guardar inventario, cargar inventario")
        print("5. Estado del Jugador:")
        print("   - mostrar estado, ver salud, ver energía")
        print("   - ver experiencia, ver nivel, ver habilidades")
        print("   - ver estadísticas, ver misión actual, ver progreso")
        print("   - ver puntos de habilidad, ver puntos de vida")
        print("   - ver puntos de magia, ver puntos de resistencia")
        print("   - ver atributos, ver equipo, ver puntos de acción")
        print("   - ver puntos de movimiento, ver estado de ánimo")
        print("   - ver habilidades desbloqueadas, ver logros")
        print("6. Otros Comandos:")
        print("   - ayuda, info, repetir")
        print("   - guardar, cargar, salir del juego")
        print("   - acerca de, configuración")
        print("   - música activar, música desactivar")
        print("   - modo fácil, modo difícil")
        print("   - anular último comando")
        print("\n")
    
    def info(self, argumentos=None):
        print("\n" + Fore.CYAN + "Información del Juego:" + Style.RESET_ALL)
        print("Nombre del juego: La Aventura de Tomsom")
        print("Objetivo: Explorar planetas, recolectar objetos y reparar tu nave espacial para regresar a casa.")
        print("Comienza en la Base Espacial y viaja a diferentes planetas para recolectar los objetos necesarios.")
        print("Usa los comandos para interactuar con el mundo y avanzar en la misión.\n")
    
    def repetir(self, argumentos=None):
        print("Repetir la última acción no está implementado aún.")
        # Implementar lógica para repetir la última acción
    
    def guardar_juego(self, argumentos=None):
        print("Guardar el juego no está implementado aún.")
        # Implementar lógica para guardar el estado del juego
    
    def cargar_juego(self, argumentos=None):
        print("Cargar el juego no está implementado aún.")
        # Implementar lógica para cargar el estado del juego
    
    def salir_juego(self, argumentos=None):
        print("Gracias por jugar. ¡Hasta la próxima!")
        sys.exit()
    
    def acerca_de(self, argumentos=None):
        print("\n" + Fore.CYAN + "Acerca de:" + Style.RESET_ALL)
        print("La Aventura de Tomsom fue desarrollada como un ejemplo de juego de texto en Python.")
        print("Proporciona una experiencia interactiva donde el jugador debe explorar, recolectar objetos y resolver acertijos para reparar su nave espacial.")
        print("¡Disfruta la aventura!\n")
    
    def configuracion(self, argumentos=None):
        print("\n" + Fore.CYAN + "Configuración:" + Style.RESET_ALL)
        print("Ajustes no implementados aún.\n")
        # Implementar lógica para configurar el juego
    
    def musica_activar(self, argumentos=None):
        print("La música se ha activado.")
        # Implementar lógica para activar música
    
    def musica_desactivar(self, argumentos=None):
        print("La música se ha desactivado.")
        # Implementar lógica para desactivar música
    
    def modo_facil(self, argumentos=None):
        print("Has cambiado al modo fácil.")
        # Implementar lógica para cambiar a modo fácil
    
    def modo_dificil(self, argumentos=None):
        print("Has cambiado al modo difícil.")
        # Implementar lógica para cambiar a modo difícil
    
    def anular_ultimo_comando(self, argumentos=None):
        print("Anular el último comando no está implementado aún.")
        # Implementar lógica para anular el último comando
    
    # Funciones de Juego
    def mover(self, direccion):
        if direccion in self.mapa[self.ubicacion].conexiones:
            self.ubicacion = self.mapa[self.ubicacion].conexiones[direccion]
            print(f"Te has movido hacia el {direccion} y ahora estás en {self.ubicacion}.")
            print(self.mapa[self.ubicacion].descripcion)
        else:
            print("No puedes ir en esa dirección.")
    
    def reparar_nave(self):
        print("\nHas recolectado todos los objetos necesarios para reparar tu nave espacial.")
        print("Usas la herramienta de reparación y combinas los objetos.")
        if "herramienta de reparación" in self.jugador.inventario and "llave completa" in self.jugador.inventario:
            print(Fore.GREEN + "¡Has reparado la nave con éxito!" + Style.RESET_ALL)
            self.estado["nave_reparada"] = True
            print("Estás listo para regresar a casa.")
        else:
            print(Fore.RED + "No tienes todos los objetos necesarios para reparar la nave." + Style.RESET_ALL)
    
    def iniciar_juego(self):
        print(Fore.CYAN + "Bienvenido a La Aventura de Tomsom!" + Style.RESET_ALL)
        print("Tu misión es recolectar los objetos necesarios para reparar tu nave espacial y regresar a casa.")
        print("Escribe 'ayuda' para ver la lista de comandos disponibles.\n")
        print(self.mapa[self.ubicacion].descripcion)
        
        while True:
            comando = input("\n¿Qué quieres hacer? ").lower()
            if not comando:
                continue
            encontrado = False
            for clave, funcion in self.comandos.items():
                if comando.startswith(clave):
                    argumentos = comando[len(clave):].strip()
                    funcion(argumentos)
                    encontrado = True
                    break
            if not encontrado:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.")
            
            # Verificar si el jugador ha recolectado todos los objetos necesarios
            if self.estado["nave_reparada"]:
                print(Fore.BLUE + "¡Felicidades! Has completado la misión y reparado tu nave espacial." + Style.RESET_ALL)
                sys.exit()
            
            # Lógica adicional para detectar cuando el jugador ha recolectado todos los objetos
            # Por ejemplo, en la ubicación "Planeta Verde", después de recolectar la llave completa
            if self.ubicacion == "Sala Secreta" and "tesoro" in self.jugador.inventario:
                print(Fore.BLUE + "Has encontrado el tesoro necesario para reparar tu nave." + Style.RESET_ALL)
                self.reparar_nave()

# Ejecutar el juego
if __name__ == Juego()
    juego.iniciar_juego()

