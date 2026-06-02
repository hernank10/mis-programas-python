jugador = "Tomson"
ubicacion = "Plaza Central"
inventario = ["Mapa de la Ciudad", "Linterna"]
puntos_de_vida = 100

salud = 100  # int
nombre = "Tomson"  # str
inventario = ["Cuchillo", "Linterna"]  # list
objetos = {"Cuchillo": "Afilado y resistente", "Linterna": "Funciona con baterías"}  # dict
es_vivo = True  # bool

juego_activo = True
while juego_activo:
    comando = input("> ").lower()
    if comando == "salir":
        juego_activo = False
    # Más lógica del juego

if ubicacion == "Plaza Central":
    print("Estás en la Plaza Central. Puedes ir al norte, este u oeste.")
elif ubicacion == "Supermercado Abandonado":
    print("Has entrado al Supermercado Abandonado. Hay pasillos oscuros por todas partes.")
else:
    print("No reconoces esta ubicación.")

def mover(direccion):
    global ubicacion
    if direccion == "norte" and ubicacion == "Plaza Central":
        ubicacion = "Supermercado Abandonado"
        print("Te has movido al norte hacia el Supermercado Abandonado.")
    elif direccion == "salir":
        global juego_activo
        juego_activo = False
    else:
        print("No puedes moverte en esa dirección desde aquí.")

comando = input("> ").lower()
if comando.startswith("ir "):
    direccion = comando.split(" ")[1]
    mover(direccion)

class Jugador:
    def __init__(self, nombre, salud=100):
        self.nombre = nombre
        self.salud = salud
        self.inventario = []
    
    def agregar_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"Has agregado {objeto} al inventario.")
    
    def mostrar_inventario(self):
        print("Inventario del jugador:")
        for objeto in self.inventario:
            print(f"- {objeto}")

jugador = Jugador("Tomson")
jugador.agregar_objeto("Mapa de la Ciudad")
jugador.mostrar_inventario()

class Habitacion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetos = []
        self.salidas = {}
    
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)
    
    def establecer_salida(self, direccion, habitacion):
        self.salidas[direccion] = habitacion

class Jugador:
    def __init__(self, nombre, salud=100):
        self.nombre = nombre
        self.salud = salud
        self.inventario = []
    
    def agregar_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"Has agregado {objeto} al inventario.")
    
    def mostrar_inventario(self):
        print("Inventario del jugador:")
        for objeto in self.inventario:
            print(f"- {objeto}")

jugador = Jugador("Tomson")
jugador.agregar_objeto("Mapa de la Ciudad")
jugador.mostrar_inventario()

inventario = ["Cuchillo", "Linterna"]
objetos_en_habitacion = ["Mapa", "Comida Enlatada"]

salidas = {
    "norte": "Supermercado Abandonado",
    "este": "Calle Desierta",
    "oeste": "Parque Olvidado"
}

comandos = {
    "ir": mover,
    "agarrar": agarrar_objeto,
    "usar": usar_objeto,
    "inventario": jugador.mostrar_inventario
}

def mostrar_objetos(objetos):
    print("Objetos disponibles:")
    for objeto in objetos:
        print(f"- {objeto}")

objetos_disponibles = [objeto for objeto in objetos_en_habitacion if objeto not in jugador.inventario]
print("Objetos que puedes recoger:")
for objeto in objetos_disponibles:
    print(f"- {objeto}")

comando = input("> ").lower()
print("Has entrado en la Supermercado Abandonado.")


import json

def guardar_partida(nombre_archivo, estado_juego):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(estado_juego, archivo)
    print(f"Juego guardado en {nombre_archivo}.")

def cargar_partida(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            estado_juego = json.load(archivo)
        print(f"Juego cargado desde {nombre_archivo}.")
        return estado_juego
    except FileNotFoundError:
        print("Archivo de guardado no encontrado.")
        return None

mostrar_objetos(objetos_en_habitacion)


# archivo: jugador.py
class Jugador:
    # Definición de la clase

def mover(direccion):
    """
    Mueve al jugador en la dirección especificada si es posible.
    """
    pass

import unittest

class TestJugador(unittest.TestCase):
    def test_agregar_objeto(self):
        jugador = Jugador("Tomson")
        jugador.agregar_objeto("Linterna")
        self.assertIn("Linterna", jugador.inventario)

if __name__ == '__main__':
    unittest.main()
    
try:
    guardar_partida("partida_guardada.json", estado_juego)
except Exception as e:
    print(f"Error al guardar la partida: {e}")
