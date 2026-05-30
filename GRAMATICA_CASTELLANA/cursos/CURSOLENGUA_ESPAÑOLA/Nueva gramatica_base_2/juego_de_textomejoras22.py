import sys
import json

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.characters = []
        self.events = []

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

    def add_event(self, event):
        self.events.append(event)

class Character:
    def __init__(self, name, description, dialogues, is_active=True):
        self.name = name
        self.description = description
        self.dialogues = dialogues  # Dict of dialogues based on game state
        self.is_active = is_active
        self.has_given_hint = False

    def talk(self, game_state):
        # Return dialogue based on current game state
        if game_state in self.dialogues:
            return self.dialogues[game_state]
        elif 'default' in self.dialogues:
            return self.dialogues['default']
        else:
            return f"{self.name} no tiene nada que decir ahora."

class Event:
    def __init__(self, trigger, description, action):
        self.trigger = trigger  # Function that returns True/False
        self.description = description
        self.action = action  # Function to execute when event is triggered

class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.inventory = []
        self.player_name = "Tomson y el Equipo"
        self.game_state = "inicio"
        self.game_over = False
        self.load_rooms()

    def load_rooms(self):
        # Aquí puedes cargar las habitaciones desde un archivo JSON para mayor flexibilidad
        # Por simplicidad, definiremos las habitaciones directamente en el código
        # Habitaciones
        spaceship = Room("Nave Espacial", "La nave espacial de Tomson, equipada con tecnología avanzada.")
        gravis_workshop = Room("Taller de Gravis", "El taller de Gravis, lleno de herramientas y equipos tecnológicos avanzados.")
        elysian_forest = Room("Bosque de Elysius", "Un bosque denso con flora bioluminiscente y sonidos misteriosos.")
        ancient_ruins = Room("Ruinas Antiguas", "Restos de una civilización alienígena con inscripciones enigmáticas.")
        underground_lab = Room("Laboratorio Subterráneo", "Un laboratorio oculto bajo la superficie de Elysius, ahora en caos.")
        ai_hub = Room("Centro de IA", "El núcleo de inteligencia artificial de Elysius, controlado por máquinas antiguas.")
        rescue_site = Room("Sitio de Rescate", "El lugar donde Lira fue vista por última vez, rodeado de tecnología inestable.")
        dark_cave = Room("Cueva Oscura", "Una cueva profunda y oscura que parece no tener fin.")

        # Definir salidas
        spaceship.set_exit("norte", gravis_workshop)
        gravis_workshop.set_exit("sur", spaceship)
        gravis_workshop.set_exit("este", elysian_forest)
        elysian_forest.set_exit("oeste", gravis_workshop)
        elysian_forest.set_exit("norte", ancient_ruins)
        ancient_ruins.set_exit("sur", elysian_forest)
        ancient_ruins.set_exit("este", underground_lab)
        underground_lab.set_exit("oeste", ancient_ruins)
        underground_lab.set_exit("norte", ai_hub)
        ai_hub.set_exit("sur", underground_lab)
        ai_hub.set_exit("este", rescue_site)
        rescue_site.set_exit("oeste", ai_hub)
        rescue_site.set_exit("norte", dark_cave)
        dark_cave.set_exit("sur", rescue_site)

        # Agregar ítems
        spaceship.add_item("Mapa de Elysius")
        gravis_workshop.add_item("Herramientas de Reparación")
        elysian_forest.add_item("Muestra de Flora Alienígena")
        ancient_ruins.add_item("Llave Antigua")
        underground_lab.add_item("Dispositivo de Comunicación")
        ai_hub.add_item("Cristal Energético")
        rescue_site.add_item("Datos de la Sonda")
        dark_cave.add_item("Linterna")

        # Agregar personajes
        gravis_dialogues = {
            "inicio": "Gravis: Gracias por venir, Tomson. Necesitamos encontrar a Lira antes de que sea demasiado tarde.",
            "after_rescue": "Gravis: ¡Has encontrado a Lira! Gracias a ti, Elysius está a salvo.",
            "default": "Gravis: Estamos en una carrera contra el tiempo."
        }
        gravis = Character("Gravis", "Un técnico experimentado con conocimientos avanzados en tecnología alienígena.", gravis_dialogues)

        lira_dialogues = {
            "inicio": "Lira: No puedo hablar mucho, Tomson. Debes encontrar el Centro de IA.",
            "after_rescue": "Lira: Gracias por rescatarme. Juntos podemos restaurar la energía de Elysius.",
            "default": "Lira: Estoy aquí para ayudarte."
        }
        lira = Character("Lira", "La asistente de Gravis, desaparecida durante la misión de restauración.", lira_dialogues, is_active=False)

        spaceship.add_character(gravis)
        spaceship.add_character(lira)

        # Guardar habitaciones
        self.rooms["Nave Espacial"] = spaceship
        self.rooms["Taller de Gravis"] = gravis_workshop
        self.rooms["Bosque de Elysius"] = elysian_forest
        self.rooms["Ruinas Antiguas"] = ancient_ruins
        self.rooms["Laboratorio Subterráneo"] = underground_lab
        self.rooms["Centro de IA"] = ai_hub
        self.rooms["Sitio de Rescate"] = rescue_site
        self.rooms["Cueva Oscura"] = dark_cave

        # Eventos (ejemplo de evento simple)
        def check_rescue_event(game):
            if "Datos de la Sonda" in game.inventory and "Llave Antigua" in game.inventory:
                return True
            return False

        rescue_event = Event(
            trigger=check_rescue_event,
            description="Has recolectado los Datos de la Sonda y la Llave Antigua. Puedes acceder al Sitio de Rescate.",
            action=lambda: print("Usa la Llave Antigua para desbloquear el acceso al Sitio de Rescate.")
        )
        rescue_site.add_event(rescue_event)

        # Establecer habitación inicial
        self.current_room = spaceship

    def start(self):
        print("¡Bienvenidos a 'Tomson y el Misterio de Elysius'!")
        print("Eres Tomson, un técnico informático que ha llegado al misterioso planeta Elysius para ayudar a tu viejo amigo, Gravis.")
        print("Gravis te ha informado que su asistente, Lira, ha desaparecido durante una misión crítica para restaurar la energía de las ciudades subterráneas.")
        print("Tu misión es encontrar a Lira y completar la misión antes de que Elysius caiga en el caos.")
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
        # Verificar y procesar eventos
        self.process_events()
        print()

    def process_events(self):
        for event in self.current_room.events:
            if event.trigger(self):
                print(f"*** Evento: {event.description} ***")
                event.action()

    def show_help(self):
        print("\nComandos disponibles:")
        print("ir [dirección] - Moverse a otra habitación (norte, sur, este, oeste)")
        print("agarrar [objeto] - Agarrar un objeto de la habitación")
        print("usar [objeto] - Usar un objeto de tu inventario")
        print("hablar [nombre] - Hablar con un personaje en la habitación")
        print("inventario - Mostrar tu inventario")
        print("guardar [nombre_archivo] - Guardar el juego")
        print("cargar [nombre_archivo] - Cargar una partida guardada")
        print("ayuda - Mostrar esta ayuda")
        print("salir - Salir del juego\n")

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.rooms[self.current_room.exits[direction]]
            self.show_current_room()
        else:
            print("No puedes ir en esa dirección.\n")

    def grab(self, item):
        item = item.title()
        if item in self.current_room.items:
            self.current_room.remove_item(item)
            self.inventory.append(item)
            print(f"Has agarrado '{item}'.\n")
        else:
            print(f"No ves '{item}' aquí.\n")

    def use(self, item):
        item = item.title()
        if item in self.inventory:
            if item == "Mapa De Elysius" and self.current_room.name == "Taller de Gravis":
                print("Has consultado el Mapa de Elysius y descubierto la ubicación del Sitio de Rescate.\n")
                self.game_state = "map_used"
            elif item == "Herramientas De Reparación" and self.current_room.name == "Taller de Gravis":
                print("Has usado las Herramientas de Reparación para arreglar el Dispositivo de Comunicación de Gravis.\n")
                self.game_state = "communication_fixed"
            elif item == "Muestra De Flora Alienígena" and self.current_room.name == "Bosque de Elysius":
                print("Has examinado la Muestra de Flora Alienígena. Descubres que ciertas plantas pueden purificar el agua tóxica.\n")
                self.game_state = "flora_examined"
            elif item == "Llave Antigua" and self.current_room.name == "Ruinas Antiguas":
                print("Has usado la Llave Antigua para desbloquear una puerta secreta en las Ruinas Antiguas.\n")
                self.game_state = "secret_door_unlocked"
            elif item == "Dispositivo De Comunicación" and self.current_room.name == "Laboratorio Subterráneo":
                if "communication_fixed" in self.game_state:
                    print("Has usado el Dispositivo de Comunicación para contactar con Gravis. Recibes información crucial sobre el paradero de Lira.\n")
                    self.game_state = "received_info"
                else:
                    print("El Dispositivo de Comunicación está dañado. Necesitas repararlo primero.\n")
            elif item == "Cristal Energético" and self.current_room.name == "Centro De IA":
                print("Has insertado el Cristal Energético en el Centro de IA, restaurando parcialmente el sistema de energía de Elysius.\n")
                self.game_state = "energy_restored"
            elif item == "Datos De La Sonda" and self.current_room.name == "Sitio De Rescate":
                print("Has descargado los Datos de la Sonda. Ahora tienes toda la información necesaria para completar la misión.\n")
                self.game_state = "mission_complete"
                self.end_game()
            elif item == "Linterna" and self.current_room.name == "Cueva Oscura":
                print("Has encendido la Linterna, iluminando la Cueva Oscura y descubriendo el camino hacia el Sitio de Rescate.\n")
                self.game_state = "cave_illuminated"
            else:
                print(f"No puedes usar '{item}' aquí.\n")
        else:
            print(f"No tienes '{item}' en tu inventario.\n")

    def hablar(self, character_name):
        character_name = character_name.title()
        for character in self.current_room.characters:
            if character.name.lower() == character_name.lower() and character.is_active:
                dialogue = character.talk(self.game_state)
                print(f"\n{dialogue}\n")
                # Cambiar el estado del juego basado en la conversación
                if character.name == "Gravis" and "mission_complete" in self.game_state:
                    character.dialogues["after_rescue"] = "Gravis: ¡Has encontrado a Lira y completado la misión! Elysius está a salvo gracias a ti."
                if character.name == "Lira" and "mission_complete" in self.game_state:
                    character.is_active = False  # Lira ya ha sido rescatada
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

    def save_game(self, filename):
        game_data = {
            "current_room": self.current_room.name,
            "inventory": self.inventory,
            "game_state": self.game_state
        }
        with open(filename, 'w') as f:
            json.dump(game_data, f)
        print(f"Juego guardado en '{filename}'.\n")

    def load_game(self, filename):
        try:
            with open(filename, 'r') as f:
                game_data = json.load(f)
            self.current_room = self.rooms.get(game_data["current_room"], self.current_room)
            self.inventory = game_data.get("inventory", [])
            self.game_state = game_data.get("game_state", "inicio")
            print(f"Juego cargado desde '{filename}'.\n")
            self.show_current_room()
        except FileNotFoundError:
            print(f"No se encontró el archivo '{filename}'.\n")
        except json.JSONDecodeError:
            print(f"El archivo '{filename}' está corrupto o tiene un formato inválido.\n")

    def end_game(self):
        print("¡Has encontrado a Lira y completado la misión! Elysius ha sido salvada gracias a tu valentía y habilidades.")
        print("¡Felicidades! Has completado el juego.")
        self.game_over = True
        sys.exit()

    def play(self):
        self.start()
        while not self.game_over:
            comando = input("> ").lower().strip().split()
            if not comando:
                continue
            accion = comando[0]
            if accion == "ir":
                if len(comando) > 1:
                    direccion = comando[1]
                    self.move(direccion)
                else:
                    print("¿A dónde quieres ir?\n")
            elif accion == "agarrar":
                if len(comando) > 1:
                    objeto = ' '.join(comando[1:]).title()
                    self.grab(objeto)
                else:
                    print("¿Qué quieres agarrar?\n")
            elif accion == "usar":
                if len(comando) > 1:
                    objeto = ' '.join(comando[1:]).title()
                    self.use(objeto)
                else:
                    print("¿Qué quieres usar?\n")
            elif accion == "hablar":
                if len(comando) > 1:
                    personaje = ' '.join(comando[1:]).title()
                    self.hablar(personaje)
                else:
                    print("¿Con quién quieres hablar?\n")
            elif accion == "inventario":
                self.show_inventory()
            elif accion == "guardar":
                if len(comando) > 1:
                    archivo = comando[1]
                    self.save_game(archivo)
                else:
                    print("¿Cómo quieres llamar al archivo de guardado?\n")
            elif accion == "cargar":
                if len(comando) > 1:
                    archivo = comando[1]
                    self.load_game(archivo)
                else:
                    print("¿Qué archivo de guardado quieres cargar?\n")
            elif accion == "ayuda":
                self.show_help()
            elif accion == "salir":
                print("¡Gracias por jugar! ¡Hasta la próxima!")
                break
            else:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n")

if __name__ == "__main__":
    game = Game()
    game.play()

