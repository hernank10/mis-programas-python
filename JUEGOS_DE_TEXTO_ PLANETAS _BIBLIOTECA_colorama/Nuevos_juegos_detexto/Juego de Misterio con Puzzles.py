# Juego de Misterio con Puzzles

def mostrar_mensaje(mensaje):
    print("\n" + mensaje)

def obtener_pista():
    if 'pista1' not in inventario:
        inventario.append('pista1')
        mostrar_mensaje("Has encontrado una nota que dice: 'El culpable siempre lleva guantes.'")
    else:
        mostrar_mensaje("No encuentras más pistas aquí.")

def resolver_puzzle(respuesta):
    if respuesta.lower() == 'guantes':
        mostrar_mensaje("Correcto! El culpable era alguien que no quería dejar huellas.")
        return True
    else:
        mostrar_mensaje("Esa no es la respuesta correcta.")
        return False

habitaciones = {
    'Oficina': {
        'descripcion': 'Estás en la oficina del detective. Hay una mesa con una lámpara.',
        'acciones': ['buscar']
    },
    'Sala de Estar': {
        'descripcion': 'Una sala de estar elegante. Hay una ventana abierta.',
        'acciones': ['buscar']
    }
}

ubicacion = 'Oficina'
inventario = []
resuelto = False

mostrar_mensaje("Bienvenido al juego de misterio. Resuelve el acertijo para descubrir al culpable.")

while not resuelto:
    comando = input("\n¿Qué quieres hacer? ").lower().split()
    if not comando:
        continue
    acción = comando[0]
    if acción == 'ir':
        if len(comando) > 1:
            nueva_ubicacion = comando[1].capitalize()
            if nueva_ubicacion in habitaciones:
                ubicacion = nueva_ubicacion
                mostrar_mensaje(habitaciones[ubicacion]['descripcion'])
            else:
                mostrar_mensaje("No puedes ir allí.")
        else:
            mostrar_mensaje("¿A dónde quieres ir?")
    elif acción == 'buscar':
        obtener_pista()
    elif acción == 'resolver':
        if len(comando) > 1:
            respuesta = ' '.join(comando[1:])
            if resolver_puzzle(respuesta):
                resuelto = True
        else:
            mostrar_mensaje("¿Cuál es tu respuesta?")
    elif acción == 'inventario':
        print("Inventario:", inventario)
    elif acción == 'salir':
        mostrar_mensaje("Gracias por jugar.")
        break
    else:
        mostrar_mensaje("Comando no reconocido.")
