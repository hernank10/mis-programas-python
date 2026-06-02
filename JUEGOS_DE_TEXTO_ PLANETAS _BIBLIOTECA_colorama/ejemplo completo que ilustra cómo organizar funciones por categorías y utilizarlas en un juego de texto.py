# Definición de clases y estructuras
class Jugador:
    def __init__(self):
        self.inventario = []
        self.salud = 100
        self.energia = 100
        self.experiencia = 0
        self.nivel = 1
        self.habilidades = ['explorar', 'atacar']

    def mostrar_estado(self):
        print("\nEstado del Jugador:")
        print(f"Salud: {self.salud}")
        print(f"Energía: {self.energia}")
        print(f"Experiencia: {self.experiencia}")
        print(f"Nivel: {self.nivel}")
        print(f"Habilidades: {', '.join(self.habilidades)}")

class Escenario:
    def __init__(self, nombre, descripcion, conexiones, objetos=None, personajes=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.conexiones = conexiones  # Diccionario de direcciones y destinos
        self.objetos = objetos if objetos else []
        self.personajes = personajes if personajes else []

class Personaje:
    def __init__(self, nombre, descripcion, dialogos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.dialogos = dialogos  # Diccionario de acciones y respuestas

    def hablar(self, accion):
        if accion in self.dialogos:
            print(f"{self.nombre} dice: '{self.dialogos[accion]}'")
        else:
            print(f"{self.nombre} no tiene nada que decir sobre eso.")

# Creación de escenarios
entrada = Escenario(
    nombre="Entrada",
    descripcion="Te encuentras en la entrada de una antigua mansión. Hay caminos al norte y al este.",
    conexiones={'norte': 'Salón', 'este': 'Cocina'},
    objetos=['llave']
)

salon = Escenario(
    nombre="Salón",
    descripcion="Un amplio salón con muebles antiguos y cuadros en las paredes.",
    conexiones={'sur': 'Entrada'},
    objetos=[],
    personajes=[Personaje("Gandalf", "Un mago sabio con una larga barba blanca.", {"ayuda": "Debes encontrar la llave en el bosque."})]
)

cocina = Escenario(
    nombre="Cocina",
    descripcion="Una cocina vieja con utensilios dispersos por el suelo.",
    conexiones={'oeste': 'Entrada'},
    objetos=['cuchillo'],
    personajes=[]
)

# Mapa del juego
mapa = {
    'Entrada': entrada,
    'Salón': salon,
    'Cocina': cocina
}

# Funciones de comando por categoría

# Funciones de Navegación
def ir_norte(argumentos):
    mover("norte")

def ir_sur(argumentos):
    mover("sur")

def ir_este(argumentos):
    mover("este")

def ir_oeste(argumentos):
    mover("oeste")

# Funciones de Inventario
def examinar_objeto(objeto):
    if objeto in mapa[ubicacion].objetos:
        print(f"Examinas el {objeto}: {objetos[objeto]['descripcion']}")
    else:
        print("No ves ese objeto aquí.")

def tomar_objeto(objeto):
    if objeto in mapa[ubicacion].objetos:
        jugador.inventario.append(objeto)
        mapa[ubicacion].objetos.remove(objeto)
        print(f"Has tomado el {objeto}.")
    else:
        print("No ves ese objeto aquí.")

# Funciones de Interacción con Personajes
def hablar_con(nombre):
    for personaje in mapa[ubicacion].personajes:
        if personaje.nombre.lower() == nombre.lower():
            accion = input(f"¿Qué quieres preguntar a {nombre}? (ayuda/salir): ").lower()
            personaje.hablar(accion)
            return
    print("No encuentras a esa persona aquí.")

# Funciones de Estado del Jugador
def mostrar_estado():
    jugador.mostrar_estado()

# Funciones de Ayuda
def ayuda():
    print("\nComandos disponibles:")
    print("- ir [norte/sur/este/oeste]")
    print("- examinar [objeto]")
    print("- tomar [objeto]")
    print("- hablar con [nombre]")
    print("- inventario")
    print("- estado")
    print("- ayuda")
    print("- salir")

# Función general para mover al jugador
def mover(direccion):
    global ubicacion
    if direccion in mapa[ubicacion].conexiones:
        ubicacion = mapa[ubicacion].conexiones[direccion]
        print(f"Te has movido hacia el {direccion} y ahora estás en el {ubicacion}.")
        print(mapa[ubicacion].descripcion)
    else:
        print("No puedes ir en esa dirección.")

# Diccionario de comandos
comandos = {
    "ir norte": ir_norte,
    "ir sur": ir_sur,
    "ir este": ir_este,
    "ir oeste": ir_oeste,
    "examinar objeto": examinar_objeto,
    "tomar objeto": tomar_objeto,
    "hablar con": hablar_con,
    "inventario": lambda args: ver_inventario(),
    "estado": mostrar_estado,
    "ayuda": ayuda,
    "salir": lambda args: salir_juego()
}

# Función para ver el inventario
def ver_inventario():
    if jugador.inventario:
        print("Inventario:")
        for obj in jugador.inventario:
            print(f"- {obj}")
    else:
        print("Tu inventario está vacío.")

# Función para salir del juego
def salir_juego():
    print("Gracias por jugar.")
    exit()

# Inicialización del juego
jugador = Jugador()
ubicacion = 'Entrada'
objetos = {
    'llave': {'descripcion': 'Una llave dorada antigua.', 'puede_usar': True},
    'cuchillo': {'descripcion': 'Un cuchillo afilado.', 'puede_usar': True}
}

print(mapa[ubicacion].descripcion)

# Bucle principal del juego
while True:
    entrada = input("\n¿Qué quieres hacer? ").lower()
    if not entrada:
        continue
    encontrado = False
    for comando, funcion in comandos.items():
        if entrada.startswith(comando):
            argumentos = entrada[len(comando):].strip()
            if comando in ["examinar objeto", "tomar objeto"]:
                funcion(argumentos)
            elif comando == "hablar con":
                nombre = argumentos
                funcion(nombre)
            else:
                funcion(argumentos)
            encontrado = True
            break
    if not encontrado:
        print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.")
