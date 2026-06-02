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
        self.player_name = "Tomsom y la Científica"

    def create_rooms(self):
        # Crear habitaciones
        sala_control = Room("Sala de Control", "La sala de control de la nave espacial, llena de paneles y luces parpadeantes.")
        laboratorio = Room("Laboratorio", "Un laboratorio equipado con instrumentos científicos y equipos de reparación.")
        granja = Room("Granja Espacial", "Una granja dentro de la nave donde cultivan plantas para suministros.")
        motor = Room("Sala del Motor", "La sala del motor, ruidosa y llena de componentes mecánicos complejos.")
        cohete = Room("Cohete de Emergencia", "Un cohete de emergencia que podría ser clave para la reparación de la nave.")

        # Definir salidas
        sala_control.set_exit("norte", laboratorio)
        sala_control.set_exit("este", granja)
        laboratorio.set_exit("sur", sala_control)
        laboratorio.set_exit("este", motor)
        granja.set_exit("oeste", sala_control)
        motor.set_exit("oeste", laboratorio)
        motor.set_exit("norte", cohete)
        cohete.set_exit("sur", motor)

        # Agregar ítems
        sala_control.add_item("Manual de Navegación")
        laboratorio.add_item("Herramientas de Reparación")
        granja.add_item("Semillas de Algas")
        motor.add_item("Pieza de Motor")
        cohete.add_item("Combustible de Emergencia")

        # Guardar habitaciones en el juego
        self.rooms["Sala de Control"] = sala_control
        self.rooms["Laboratorio"] = laboratorio
        self.rooms["Granja Espacial"] = granja
        self.rooms["Sala del Motor"] = motor
        self.rooms["Cohete de Emergencia"] = cohete

        # Establecer habitación inicial
        self.current_room = sala_control

    def start(self):
        print("¡Bienvenidos a la misión de reparación espacial!")
        print("Eres Tomsom, un astronauta de 46 años, acompañado por una brillante científica.")
        print("Juntos, deben reparar la nave y la granja espacial para sobrevivir y completar la misión.")
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
            if item == "Manual de Navegación" and self.current_room.name == "Sala de Control":
                print("Has consultado el Manual de Navegación y encontrado la forma de reiniciar el sistema de control.\n")
                # Aquí se puede agregar lógica adicional
            elif item == "Herramientas de Reparación" and self.current_room.name == "Sala del Motor":
                print("Estás reparando el motor con las Herramientas de Reparación. El motor ahora funciona correctamente.\n")
                # Aquí se puede agregar lógica adicional
            elif item == "Combustible de Emergencia" and self.current_room.name == "Cohete de Emergencia":
                print("Has cargado el Combustible de Emergencia en el Cohete. Ahora puedes usarlos para emergencias.\n")
                # Aquí se puede agregar lógica adicional
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
                    # Unir las palabras del objeto si tiene más de una palabra
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
