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
        self.player_name = "Tomsom y Dra. Elena"

    def create_rooms(self):
        # Crear las habitaciones en el Planeta Zeta
        nave_espacial = Room("Nave Espacial", "La nave espacial de Tomsom y su equipo, estacionada en una extraña llanura.")
        selva = Room("Selva Misteriosa", "Una densa selva con plantas bioluminiscentes y sonidos desconocidos.")
        cueva = Room("Cueva Oscura", "Una cueva profunda llena de rocas brillantes y extrañas criaturas.")
        lago = Room("Lago Ácido", "Un lago que desprende vapores tóxicos, con un brillo verde inquietante.")
        ruinas = Room("Ruinas Antiguas", "Restos de una antigua civilización alienígena, llenos de inscripciones desconocidas.")
        sonda_perdida = Room("Sonda Espacial Perdida", "Aquí está la sonda espacial perdida, cubierta de enredaderas alienígenas.")

        # Definir salidas entre habitaciones
        nave_espacial.set_exit("norte", selva)
        selva.set_exit("sur", nave_espacial)
        selva.set_exit("oeste", cueva)
        selva.set_exit("este", lago)
        cueva.set_exit("este", selva)
        lago.set_exit("oeste", selva)
        lago.set_exit("norte", ruinas)
        ruinas.set_exit("sur", lago)
        ruinas.set_exit("oeste", sonda_perdida)
        sonda_perdida.set_exit("este", ruinas)

        # Agregar ítems
        nave_espacial.add_item("Traje de Exploración")
        selva.add_item("Muestra de Planta Alienígena")
        cueva.add_item("Cristal Energético")
        lago.add_item("Máscara Antigás")
        ruinas.add_item("Llave Antigua")
        sonda_perdida.add_item("Datos de la Sonda")

        # Guardar habitaciones
        self.rooms["Nave Espacial"] = nave_espacial
        self.rooms["Selva Misteriosa"] = selva
        self.rooms["Cueva Oscura"] = cueva
        self.rooms["Lago Ácido"] = lago
        self.rooms["Ruinas Antiguas"] = ruinas
        self.rooms["Sonda Espacial Perdida"] = sonda_perdida

        # Habitación inicial
        self.current_room = nave_espacial

    def start(self):
        print("¡Bienvenidos a la misión de exploración en el Planeta Zeta!")
        print("Eres Tomsom, acompañado por la Dra. Elena, y debes descubrir qué le pasó a la sonda espacial.")
        print("Escribe 'ayuda' para ver los comandos disponibles.\n")
        self.show_current_room()

    def show_current_room(self):
        print(f"Estás en {self.current_room.name}.")
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
        print("usar [objeto] - Usar un objeto de tu inventario")
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

    def use(self, item):
        if item in self.inventory:
            if item == "Traje de Exploración" and self.current_room.name == "Selva Misteriosa":
                print("Has puesto el Traje de Exploración. Ahora puedes explorar sin peligro.\n")
            elif item == "Máscara Antigás" and self.current_room.name == "Lago Ácido":
                print("Has usado la Máscara Antigás. Puedes cruzar el lago tóxico con seguridad.\n")
            elif item == "Llave Antigua" and self.current_room.name == "Sonda Espacial Perdida":
                print("Usaste la Llave Antigua y desbloqueaste la sonda. ¡Recuperaste los datos!\n")
            elif item == "Cristal Energético" and self.current_room.name == "Nave Espacial":
                print("Has usado el Cristal Energético para reactivar la nave. ¡La misión está casi completa!\n")
            else:
                print(f"No puedes usar {item} aquí.\n")
        else:
            print(f"No tienes {item} en tu inventario.\n")

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
                    item = ' '.join(command[1:]).capitalize()
                    self.grab(item)
                else:
                    print("¿Qué quieres agarrar?\n")
            elif command[0] == "usar":
                if len(command) > 1:
                    item = ' '.join(command[1:]).capitalize()
                    self.use(item)
                else:
                    print("¿Qué quieres usar?\n")
            elif command[0] == "inventario":
                self.show_inventory()
            elif command[0] == "ayuda":
                self.show_help()
            elif command[0] == "salir":
                print("¡Gracias por jugar! Buena suerte en tu misión.")
                break
            else:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n")


if __name__ == "__main__":
    game = Game()
    game.create_rooms()
    game.play()
