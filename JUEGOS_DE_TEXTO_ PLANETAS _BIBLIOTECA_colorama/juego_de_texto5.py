import sys

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.characters = []

    def set_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        if character in self.characters:
            self.characters.remove(character)

class Character:
    def __init__(self, name, description, is_active=True):
        self.name = name
        self.description = description
        self.is_active = is_active

class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.inventory = []
        self.player_name = "Tomson"
        self.friends = ["Gravis"]
        self.game_over = False

    def create_rooms(self):
        # Crear las habitaciones en Zephyria
        spaceship = Room("Nave Espacial", "La nave espacial de Tomson, estacionada en una vasta llanura rocosa.")
        gravis_workshop = Room("Taller de Gravis", "El taller de Gravis, lleno de herramientas y equipos tecnológicos avanzados.")
        alien_forest = Room("Selva Alienígena", "Una selva densa con flora bioluminiscente y sonidos desconocidos.")
        ancient_ruins = Room("Ruinas Antiguas", "Restos de una antigua civilización alienígena, con inscripciones misteriosas.")
        underground_city = Room("Ciudad Subterránea", "Una ciudad subterránea que una vez fue el corazón de Zephyria, ahora en decadencia.")
        ai_hub = Room("Centro de IA", "Un centro de inteligencia artificial oculto, donde las antiguas máquinas aún operan.")
        rescue_site = Room("Sitio de Rescate", "El lugar donde Lira fue vista por última vez, rodeado de tecnología inestable.")
        dark_cave = Room("Cueva Oscura", "Una cueva profunda y oscura que parece no tener fin.")

        # Definir salidas entre habitaciones
        spaceship.set_exit("norte", gravis_workshop)
        gravis_workshop.set_exit("sur", spaceship)
        gravis_workshop.set_exit("este", alien_forest)
        alien_forest.set_exit("oeste", gravis_workshop)
        alien_forest.set_exit("norte", ancient_ruins)
        ancient_ruins.set_exit("sur", alien_forest)
        ancient_ruins.set_exit("este", underground_city)
        underground_city.set_exit("oeste", ancient_ruins)
        underground_city.set_exit("norte", ai_hub)
        ai_hub.set_exit("sur", underground_city)
        ai_hub.set_exit("este", rescue_site)
        rescue_site.set_exit("oeste", ai_hub)
        rescue_site.set_exit("norte", dark_cave)
        dark_cave.set_exit("sur", rescue_site)

        # Agregar ítems
        spaceship.add_item("Mapa de Zephyria")
        gravis_workshop.add_item("Herramientas de Reparación")
        alien_forest.add_item("Muestra de Flora Alienígena")
        ancient_ruins.add_item("Llave Antigua")
        underground_city.add_item("Dispositivo de Comunicación")
        ai_hub.add_item("Cristal Energético")
        rescue_site.add_item("Datos de la Sonda")
        dark_cave.add_item("Linterna")

        # Agregar personajes
        gravis = Character("Gravis", "Un técnico experimentado con conocimientos avanzados en tecnología alienígena.")
        lira = Character("Lira", "La asistente de Gravis, desaparecida durante la misión de restauración.", is_active=False)
        spaceship.add_character(gravis)

        # Guardar habitaciones
        self.rooms["Nave Espacial"] = spaceship
        self.rooms["Taller de Gravis"] = gravis_workshop
        self.rooms["Selva Alienígena"] = alien_forest
        self.rooms["Ruinas Antiguas"] = ancient_ruins
        self.rooms["Ciudad Subterránea"] = underground_city
        self.rooms["Centro de IA"] = ai_hub
        self.rooms["Sitio de Rescate"] = rescue_site
        self.rooms["Cueva Oscura"] = dark_cave

        # Habitación inicial
        self.current_room = spaceship

    def start(self):
        print("¡Bienvenidos a 'Tomson y la Búsqueda en Zephyria'!")
        print("Eres Tomson, un técnico informático que ha llegado al misterioso planeta Zephyria para ayudar a tu viejo amigo, Gravis.")
        print("Gravis te ha informado que su asistente, Lira, ha desaparecido durante una misión crítica para restaurar la energía de las ciudades subterráneas.")
        print("Tu misión es encontrar a Lira y completar la misión antes de que Zephyria caiga en el caos.")
        print("Escribe 'ayuda' para ver los comandos disponibles.\n")
        self.show_current_room()

    def show_current_room(self):
        print(f"\nEstás en la {self.current_room.name}.")
        print(self.current_room.description)
        if self.current_room.characters:
            for character in self.current_room.characters:
                if character.is_active:
                    print(f"Ves a {character.name}: {character.description}")
        if self.current_room.items:
            print("Ves los siguientes objetos:")
            for item in self.current_room.items:
                print(f"- {item}")
        print("Salidas disponibles: " + ", ".join(self.current_room.exits.keys()))
        print()

    def show_help(self):
        print("\nComandos disponibles:")
        print("ir [dirección] - Moverse a otra habitación (norte, sur, este, oeste)")
        print("agarrar [objeto] - Agarrar un objeto de la habitación")
        print("usar [objeto] - Usar un objeto de tu inventario")
        print("hablar [nombre] - Hablar con un personaje en la habitación")
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
            print(f"No ves '{item}' aquí.\n")

    def use(self, item):
        if item in self.inventory:
            if item == "Mapa de Zephyria" and self.current_room.name == "Taller de Gravis":
                print("Has consultado el Mapa de Zephyria y descubierto la ubicación del Sitio de Rescate.\n")
            elif item == "Herramientas de Reparación" and self.current_room.name == "Taller de Gravis":
                print("Has usado las Herramientas de Reparación para arreglar el dispositivo de comunicación de Gravis.\n")
                # Posiblemente agregar lógica adicional
            elif item == "Muestra de Flora Alienígena" and self.current_room.name == "Selva Alienígena":
                print("Has examinado la Muestra de Flora Alienígena. Descubres que ciertas plantas pueden ser usadas para purificar el agua.\n")
                # Posiblemente agregar habilidades o desbloquear acciones
            elif item == "Llave Antigua" and self.current_room.name == "Ruinas Antiguas":
                print("Has usado la Llave Antigua para desbloquear una puerta secreta en las Ruinas Antiguas.\n")
                # Desbloquear nueva habitación o contenido
            elif item == "Dispositivo de Comunicación" and self.current_room.name == "Ciudad Subterránea":
                print("Has usado el Dispositivo de Comunicación para contactar con Gravis. Recibes información crucial sobre el paradero de Lira.\n")
                # Posiblemente avanzar en la historia
            elif item == "Cristal Energético" and self.current_room.name == "Centro de IA":
                print("Has insertado el Cristal Energético en el Centro de IA, restaurando parcialmente el sistema de energía de Zephyria.\n")
                # Desbloquear nuevas áreas o habilidades
            elif item == "Datos de la Sonda" and self.current_room.name == "Sitio de Rescate":
                print("Has descargado los Datos de la Sonda. Ahora tienes toda la información necesaria para completar la misión.\n")
                print("¡Has encontrado a Lira y completado la misión! Zephyria ha sido salvada gracias a tu valentía y habilidades.\n")
                print("¡Felicidades! Has completado el juego.")
                self.game_over = True
                sys.exit()
            elif item == "Linterna" and self.current_room.name == "Cueva Oscura":
                print("Has encendido la Linterna, iluminando la Cueva Oscura y descubriendo el camino hacia el Sitio de Rescate.\n")
            else:
                print(f"No puedes usar '{item}' aquí.\n")
        else:
            print(f"No tienes '{item}' en tu inventario.\n")

    def hablar(self, character_name):
        for character in self.current_room.characters:
            if character.name.lower() == character_name.lower() and character.is_active:
                if character.name == "Gravis":
                    print(f"\n{character.name}: 'Gracias por venir, Tomson. Lira desapareció mientras trabajaba en la restauración de la energía. Necesitamos encontrarla antes de que sea demasiado tarde.'\n")
                else:
                    print(f"\nNo hay nada que decir con '{character.name}'.\n")
                return
        print(f"No hay a '{character_name}' aquí para hablar.\n")

    def show_inventory(self):
        if self.inventory:
            print("\nTienes los siguientes objetos en tu inventario:")
            for item in self.inventory:
                print(f"- {item}")
            print()
        else:
            print("\nTu inventario está vacío.\n")

    def play(self):
        self.start()
        while not self.game_over:
            command = input("> ").lower().strip().split()
            if not command:
                continue
            action = command[0]
            if action == "ir":
                if len(command) > 1:
                    self.move(command[1])
                else:
                    print("¿A dónde quieres ir?\n")
            elif action == "agarrar":
                if len(command) > 1:
                    item = ' '.join(command[1:]).title()
                    self.grab(item)
                else:
                    print("¿Qué quieres agarrar?\n")
            elif action == "usar":
                if len(command) > 1:
                    item = ' '.join(command[1:]).title()
                    self.use(item)
                else:
                    print("¿Qué quieres usar?\n")
            elif action == "hablar":
                if len(command) > 1:
                    character = ' '.join(command[1:]).title()
                    self.hablar(character)
                else:
                    print("¿Con quién quieres hablar?\n")
            elif action == "inventario":
                self.show_inventory()
            elif action == "ayuda":
                self.show_help()
            elif action == "salir":
                print("¡Gracias por jugar! ¡Buena suerte en tu aventura!")
                break
            else:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n")

if __name__ == "__main__":
    game = Game()
    game.create_rooms()
    game.play()
