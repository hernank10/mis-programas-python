from adventurelib import Room, when, start

# Definir las habitaciones
kitchen = Room("Cocina", "Una cocina limpia y ordenada.")
hall = Room("Salón", "Un salón acogedor con un sofá grande.")
kitchen.east = hall
hall.west = kitchen

# Definir la ubicación inicial
current_room = kitchen

@when("ir NORTH")
def go_north():
    global current_room
    print("No hay nada al norte.")
    
@when("ir SOUTH")
def go_south():
    global current_room
    print("No hay nada al sur.")
    
@when("ir EAST")
def go_east():
    global current_room
    if current_room == kitchen:
        current_room = hall
        print(current_room)
    else:
        print("No puedes ir al este desde aquí.")
        
@when("ir WEST")
def go_west():
    global current_room
    if current_room == hall:
        current_room = kitchen
        print(current_room)
    else:
        print("No puedes ir al oeste desde aquí.")

# Iniciar el juego
print(current_room)
start()
