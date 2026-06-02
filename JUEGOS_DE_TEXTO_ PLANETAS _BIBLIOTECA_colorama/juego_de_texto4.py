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
        self.player_name = "Tomsom y sus Amigos"

    def create_rooms(self):
        # Crear las habitaciones
        casa = Room("Casa de Tomsom", "La acogedora casa de Tomsom, donde él y sus amigos se reúnen para planificar.")
        biblioteca = Room("Biblioteca Pública", "Un lugar tranquilo lleno de libros sobre informática y tecnología.")
        café = Room("Café Local", "Un café popular donde los personajes pueden encontrarse con otros y obtener información.")
        taller = Room("Taller de Electrónica", "Un taller equipado con herramientas y equipos para proyectos tecnológicos.")
        universidad = Room("Universidad Tecnológica", "El campus de la universidad donde Tomsom puede inscribirse en cursos.")
        oficina = Room("Oficina de Empresas", "El lugar donde Tomsom puede buscar oportunidades de empleo y prácticas.")

        # Definir salidas entre habitaciones
        casa.set_exit("norte", biblioteca)
        casa.set_exit("este", café)
        biblioteca.set_exit("sur", casa)
        biblioteca.set_exit("este", taller)
        café.set_exit("oeste", casa)
        café.set_exit("norte", taller)
        taller.set_exit("oeste", biblioteca)
        taller.set_exit("sur", café)
        taller.set_exit("este", universidad)
        universidad.set_exit("oeste", taller)
        universidad.set_exit("norte", oficina)
        oficina.set_exit("sur", universidad)

        # Agregar ítems
        casa.add_item("Currículum Vitae")
        biblioteca.add_item("Libro de Programación")
        café.add_item("Tarjeta de Networking")
        taller.add_item("Kit de Electrónica")
        universidad.add_item("Certificado de Curso")
        oficina.add_item("Oferta de Empleo")

        # Guardar habitaciones en el juego
        self.rooms["Casa de Tomsom"] = casa
        self.rooms["Biblioteca Pública"] = biblioteca
        self.rooms["Café Local"] = café
        self.rooms["Taller de Electrónica"] = taller
        self.rooms["Universidad Tecnológica"] = universidad
        self.rooms["Oficina de Empresas"] = oficina

        # Habitación inicial
        self.current_room = casa

    def start(self):
        print("¡Bienvenidos a la aventura de Tomsom!")
        print("Eres Tomsom, un hombre de 46 años que ha perdido su empleo en una granja espacial.")
        print("Junto a tus amigos Ana y Luis, decides reinventar tu vida convirtiéndote en técnico informático.")
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
            if item == "Libro de Programación" and self.current_room.name == "Biblioteca Pública":
                print("Has estudiado el Libro de Programación. Ahora tienes conocimientos básicos de Python.\n")
                # Aquí se puede agregar lógica adicional, como desbloquear nuevas áreas
            elif item == "Tarjeta de Networking" and self.current_room.name == "Café Local":
                print("Has entregado tu Tarjeta de Networking a un profesional de la informática. ¡Has hecho un nuevo contacto!\n")
                # Posiblemente agregar un objeto o desbloquear una habitación
            elif item == "Kit de Electrónica" and self.current_room.name == "Taller de Electrónica":
                print("Has utilizado el Kit de Electrónica para armar un pequeño proyecto. Ahora entiendes mejor los componentes.\n")
                # Posiblemente agregar habilidades o desbloquear acciones
            elif item == "Certificado de Curso" and self.current_room.name == "Universidad Tecnológica":
                print("Has presentado el Certificado de Curso para inscribirte en un programa avanzado de informática.\n")
                # Posiblemente desbloquear nuevas habitaciones o habilidades
            elif item == "Oferta de Empleo" and self.current_room.name == "Oficina de Empresas":
                print("Has aceptado la Oferta de Empleo. ¡Felicidades, has conseguido tu nuevo trabajo como técnico informático!\n")
                print("¡Has completado tu misión de reinvención! ¡Felicidades!")
                exit()
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
                print("¡Gracias por jugar! ¡Buena suerte en tu nueva carrera!")
                break
            else:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n")


if __name__ == "__main__":
    game = Game()
    game.create_rooms()
    game.play()
