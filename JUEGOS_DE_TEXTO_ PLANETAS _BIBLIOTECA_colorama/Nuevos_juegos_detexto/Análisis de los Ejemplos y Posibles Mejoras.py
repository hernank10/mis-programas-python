import random

pistas = [
    "El culpable lleva guantes.",
    "El asesino siempre llega tarde.",
    "El sospechoso tiene una cicatriz en la mano."
]

def obtener_pista():
    if not pistas:
        print("No hay más pistas disponibles.")
    else:
        pista = random.choice(pistas)
        inventario.append(pista)
        pistas.remove(pista)
        print(f"Has encontrado una pista: {pista}")




inventario = {'objetos': [], 'peso_total': 0}

def recoger(objeto):
    peso = objetos[objeto]['peso']
    if inventario['peso_total'] + peso <= capacidad_inventario:
        inventario['objetos'].append(objeto)
        inventario['peso_total'] += peso
        print(f"Has recogido {objeto}.")
    else:
        print("No puedes recoger ese objeto, tu inventario está lleno.")

habitaciones = {
    'Entrada': {...},
    'Salón': {...},
    'Cocina': {...},
    'Biblioteca': {
        'descripcion': 'Una sala repleta de libros antiguos. Hay una puerta secreta al oeste.',
        'conexiones': {'sur': 'Entrada', 'oeste': 'Sala Secreta'},
        'objetos': ['libro mágico']
    },
    'Sala Secreta': {
        'descripcion': 'Una pequeña sala con un cofre en el centro.',
        'conexiones': {'este': 'Biblioteca'},
        'objetos': ['tesoro']
    }
}

estado_juego = {'ha_tomado_la_llave': False, 'ha_salido_del_bosque': False}

def tomar_llave():
    estado_juego['ha_tomado_la_llave'] = True
    print("Has tomado la llave.")

def usar_llave():
    if estado_juego['ha_tomado_la_llave']:
        print("Has usado la llave para abrir la puerta secreta.")
        estado_juego['ha_salido_del_bosque'] = True
    else:
        print("No tienes ninguna llave.")


def ganar_experiencia(jugador, cantidad):
    jugador['experiencia'] += cantidad
    if jugador['experiencia'] >= jugador['nivel'] * 100:
        jugador['nivel'] += 1
        jugador['experiencia'] -= jugador['nivel'] * 100
        jugador['salud'] += 10
        jugador['ataque'] += 2
        print(f"¡Felicidades! Has subido al nivel {jugador['nivel']}.")

relaciones = {
    'Ana': {'amistad': 5, 'confianza': 3},
    'Carlos': {'amistad': 2, 'confianza': 4},
    'Beatriz': {'amistad': 4, 'confianza': 5}
}

def interactuar(personaje, tipo_interaccion):
    if tipo_interaccion == 'saludar':
        relaciones[personaje]['amistad'] += 1
    elif tipo_interaccion == 'regalar':
        relaciones[personaje]['amistad'] += 2
    elif tipo_interaccion == 'conversar':
        relaciones[personaje]['confianza'] += 1
    # Añadir lógica adicional según las interacciones
