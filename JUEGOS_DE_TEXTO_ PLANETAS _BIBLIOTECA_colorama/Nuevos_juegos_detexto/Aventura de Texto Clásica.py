# Aventura de Texto Clásica

def mostrar_descripcion(habitacion):
    print("\n" + habitaciones[habitacion]['descripcion'])

def mover(direccion):
    global ubicacion
    if direccion in habitaciones[ubicacion]['conexiones']:
        ubicacion = habitaciones[ubicacion]['conexiones'][direccion]
        mostrar_descripcion(ubicacion)
    else:
        print("No puedes ir en esa dirección.")

def recoger(objeto):
    if objeto in habitaciones[ubicacion]['objetos']:
        inventario.append(objeto)
        habitaciones[ubicacion]['objetos'].remove(objeto)
        print(f"Has recogido {objeto}.")
    else:
        print("No hay ese objeto aquí.")

habitaciones = {
    'Entrada': {
        'descripcion': 'Estás en la entrada de una antigua mansión. Hay puertas al norte y al este.',
        'conexiones': {'norte': 'Salón', 'este': 'Cocina'},
        'objetos': ['llave']
    },
    'Salón': {
        'descripcion': 'Un salón amplio con muebles antiguos. Hay una puerta al sur.',
        'conexiones': {'sur': 'Entrada'},
        'objetos': []
    },
    'Cocina': {
        'descripcion': 'Una cocina vieja con utensilios dispersos. Hay una puerta al oeste.',
        'conexiones': {'oeste': 'Entrada'},
        'objetos': ['cuchillo']
    }
}

ubicacion = 'Entrada'
inventario = []

mostrar_descripcion(ubicacion)

while True:
    comando = input("\n¿Qué quieres hacer? ").lower().split()
    if not comando:
        continue
    acción = comando[0]
    if acción == 'mover' or acción == 'ir':
        if len(comando) > 1:
            mover(comando[1])
        else:
            print("¿A dónde quieres ir?")
    elif acción == 'mirar':
        mostrar_descripcion(ubicacion)
    elif acción == 'recoger':
        if len(comando) > 1:
            recoger(comando[1])
        else:
            print("¿Qué quieres recoger?")
    elif acción == 'inventario':
        print("Inventario:", inventario)
    elif acción == 'salir':
        print("Gracias por jugar.")
        break
    else:
        print("Comando no reconocido.")
