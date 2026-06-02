class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def set_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.inventory = []

    def create_rooms(self):
        # Crear habitaciones
        living_room = Room("Sala", "Una sala cómoda con un sofá y una mesa.")
        kitchen = Room("Cocina", "Una cocina con una nevera y un horno.")
        bedroom = Room("Dormitorio", "Un dormitorio con una cama y un armario.")

        # Definir salidas
        living_room.set_exit("norte", kitchen)
        kitchen.set_exit("sur", living_room)
        living_room.set_exit("este", bedroom)
        bedroom.set_exit("oeste", living_room)

        # Agregar ítems
        kitchen.add_item("Llave")
        bedroom.add_item("Linterna")

        # Guardar habitaciones en el juego
        self.rooms["Sala"] = living_room
        self.rooms["Cocina"] = kitchen
        set
        self.rooms["Dormitorio"] = bedroom

        # Establecer habitación inicial
        self.current_room = living_room

    def start(self):
        print("¡Bienvenido al juego de aventuras de texto!")
        print("Escribe 'ayuda' para ver los comandos disponibles.\n")
        self.show_current_room()

    def show_current_room(self):
        print(f"Estás en la {self.current_room.name}.")
        print(self.current_room.description)
        if self.current_room.items:
            print("Ves los siguientes objetos:")
            for item in self.current_room.items:
                print(f"- {item}")
        print()

    def show_help(self):
        print("Comandos disponibles:")
        print("ir [dirección] - Moverse a otra habitación (norte, sur, este, oeste)")
        print("agarrar [objeto] - Agarrar un objeto de la habitación")
        print("inventario - Mostrar tu inventario")
        print("ayuda - Mostrar esta ayuda")
        print("salir - Salir del juego\n")

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            self.show_current_room()
        else:
            print("No puedes ir en esa dirección.\n")

    def grab(self, item):
        if item in self.current_room.items:
            self.current_room.remove_item(item)
            self.inventory.append(item)
            print(f"Has agarrado {item}.\n")
        else:
            print(f"No ves {item} aquí.\n")

    def show_inventory(self):
        if self.inventory:
            print("Tienes los siguientes objetos en tu inventario:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Tu inventario está vacío.")
        print()

    def play(self):
        self.start()
        while True:
            command = input("> ").lower().strip().split()
            if not command:
                continue
            if command[0] == "ir":
                if len(command) > 1:
                    self.move(command[1])
                else:
                    print("¿A dónde quieres ir?\n")
            elif command[0] == "agarrar":
                if len(command) > 1:
                    self.grab(command[1])
                else:
                    print("¿Qué quieres agarrar?\n")
            elif command[0] == "inventario":
                self.show_inventory()
            elif command[0] == "ayuda":
                self.show_help()
            elif command[0] == "salir":
                print("¡Gracias por jugar!")
                break
            else:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n")

if __name__ == "__main__":
    game = Game()
    game.create_rooms()
    game.play()
