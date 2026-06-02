import sys
import json
from colorama import Fore, Style, init
init(autoreset=True)

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.characters = []

    def set_exit(self, direction, room_name):
        self.exits[direction] = room_name

    def add_item(self, item):
        self.items.append(item)

    def add_character(self, character):
        self.characters.append(character)

class Character:
    def __init__(self, name, description, dialogues):
        self.name = name
        self.description = description
        self.dialogues = dialogues  # Dict with dialogues based on game state
        self.is_active = True

    def talk(self, game_state):
        return self.dialogues.get(game_state, self.dialogues.get('default', f"{self.name} no tiene nada que decir ahora."))

class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.inventory = []
        self.game_state = "inicio"
        self.commands = {
            'ir': self.move,
            'moverse': self.move,
            'caminar': self.move,
            'agarrar': self.grab,
            'usar': self.use_item,
            'hablar': self.talk,
            'inventario': self.show_inventory,
            'ayuda': self.show_help,
            'salir': self.exit_game,
            'guardar': self.save_game,
            'cargar': self.load_game,
            'pista': self.give_hint
        }
        self.setup_game()

    def setup_game(self):
        # Crear habitaciones
        sala = Room("Sala", "Una sala acogedora con un sofá y una mesa.")
        cocina = Room("Cocina", "Una cocina bien equipada con una nevera y un horno.")
        dormitorio = Room("Dormitorio", "Un dormitorio tranquilo con una cama grande.")

        # Definir salidas
        sala.set_exit("norte", "Cocina")
        sala.set_exit("este", "Dormitorio")
        cocina.set_exit("sur", "Sala")
        dormitorio.set_exit("oeste", "Sala")

        # Agregar objetos
        sala.add_item("libro")
        cocina.add_item("cuchillo")
        dormitorio.add_item("llave")

        # Crear personajes
        ana_dialogues = {
            "inicio": "Ana: Hola, Tomson. ¿Necesitas ayuda con algo?",
            "after_grab_llave": "Ana: Gracias por traerme la llave. Ahora podemos abrir la puerta secreta.",
            "default": "Ana: Estoy aquí para ayudarte."
        }
        ana = Character("Ana", "Una amiga de confianza que siempre está dispuesta a ayudar.", ana_dialogues)

        sala.add_character(ana)

        # Guardar habitaciones
        self.rooms["Sala"] = sala
        self.rooms["Cocina"] = cocina
        self.rooms["Dormitorio"] = dormitorio

        # Establecer habitación inicial
        self.current_room = sala

    def show_current_room(self):
        print(f"\n{Fore.CYAN}Estás en la {self.current_room.name}.{Style.RESET_ALL}")
        print(self.current_room.description)
        if self.current_room.characters:
            for character in self.current_room.characters:
                if character.is_active:
                    print(f"{Fore.YELLOW}Ves a {character.name}: {character.description}{Style.RESET_ALL}")
        if self.current_room.items:
            print(f"{Fore.GREEN}Ves los siguientes objetos:{Style.RESET_ALL}")
            for item in self.current_room.items:
                print(f"- {item}")
        print(f"{Fore.MAGENTA}Salidas disponibles: {', '.join(self.current_room.exits.keys())}{Style.RESET_ALL}\n")
        self.check_events()

    def check_events(self):
        # Implementar eventos basados en el estado del juego
        if self.current_room.name == "Dormitorio" and "llave" in self.inventory and self.game_state == "inicio":
            print("*** Evento: Has encontrado una llave en el dormitorio. ***\n")
            self.game_state = "has_llave"

    def show_help(self, args=None):
        print("\nComandos disponibles:")
        print("ir [dirección] - Moverse a otra habitación (norte, sur, este, oeste)")
        print("agarrar [objeto] - Agarrar un objeto de la habitación")
        print("usar [objeto] - Usar un objeto de tu inventario")
        print("hablar [nombre] - Hablar con un personaje en la habitación")
        print("inventario - Mostrar tu inventario")
        print("guardar [nombre_archivo] - Guardar el juego")
        print("cargar [nombre_archivo] - Cargar una partida guardada")
        print("pista - Obtener una pista")
        print("ayuda - Mostrar esta ayuda")
        print("salir - Salir del juego\n")

    def move(self, args):
        if not args:
            print("¿A dónde quieres ir?\n")
            return
        direction = args[0]
        if direction in self.current_room.exits:
            next_room_name = self.current_room.exits[direction]
            self.current_room = self.rooms[next_room_name]
            self.show_current_room()
        else:
            print("No puedes ir en esa dirección.\n")

    def grab(self, args):
        if not args:
            print("¿Qué quieres agarrar?\n")
            return
        item_name = ' '.join(args).title()
        if item_name in self.current_room.items:
            self.inventory.append(item_name)
            self.current_room.items.remove(item_name)
            print(f"Has agarrado '{item_name}'.\n")
            # Actualizar estado del juego si es necesario
            if item_name.lower() == "llave":
                self.game_state = "has_llave"
        else:
            print(f"No ves '{item_name}' aquí.\n")

    def use_item(self, args):
        if not args:
            print("¿Qué quieres usar?\n")
            return
        item_name = ' '.join(args).title()
        if item_name in self.inventory:
            if item_name == "Llave":
                print("Has usado la Llave para abrir la puerta secreta.\n")
                # Implementar lógica adicional, como desbloquear una nueva habitación
            elif item_name == "Libro":
                print("Has leído el libro. Adquieres nuevos conocimientos.\n")
                # Implementar lógica adicional
            else:
                print(f"No puedes usar '{item_name}' aquí.\n")
        else:
            print(f"No tienes '{item_name}' en tu inventario.\n")

    def talk(self, args):
        if not args:
            print("¿Con quién quieres hablar?\n")
            return
        character_name = ' '.join(args).title()
        for character in self.current_room.characters:
            if character.name == character_name and character.is_active:
                dialogue = character.talk(self.game_state)
                print(f"\n{dialogue}\n")
                # Actualizar estado del juego basado en la conversación
                if character.name == "Ana" and "has_llave" in self.game_state:
                    print("Ana: Gracias por traerme la llave. Ahora podemos abrir la puerta secreta.\n")
                    self.game_state = "door_unlocked"
                return
        print(f"No hay a '{character_name}' aquí para hablar.\n")

    def show_inventory(self, args=None):
        if self.inventory:
            print("\nTienes los siguientes objetos en tu inventario:")
            for item in self.inventory:
                print(f"- {item}")
            print()
        else:
            print("\nTu inventario está vacío.\n")

    def give_hint(self, args=None):
        if self.current_room.name == "Sala":
            print("Pista: Explora las habitaciones cercanas para encontrar objetos útiles.\n")
        elif self.current_room.name == "Dormitorio" and "llave" not in self.inventory:
            print("Pista: Revisa el dormitorio para encontrar algo que pueda ayudarte.\n")
        elif self.current_room.name == "Cocina":
            print("Pista: El cuchillo podría ser útil en una situación de emergencia.\n")
        else:
            print("No hay pistas disponibles en este momento.\n")

    def save_game(self, args):
        if not args:
            print("¿Cómo quieres llamar al archivo de guardado?\n")
            return
        filename = args[0] + ".json"
        game_data = {
            "current_room": self.current_room.name,
            "inventory": self.inventory,
            "game_state": self.game_state
        }
        with open(filename, 'w') as f:
            json.dump(game_data, f)
        print(f"Juego guardado en '{filename}'.\n")

    def load_game(self, args):
        if not args:
            print("¿Qué archivo de guardado quieres cargar?\n")
            return
        filename = args[0] + ".json"
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

    def give_hint(self, args=None):
        if self.current_room.name == "Sala":
            print("Pista: Explora las habitaciones cercanas para encontrar objetos útiles.\n")
        elif self.current_room.name == "Dormitorio" and "llave" not in self.inventory:
            print("Pista: Revisa el dormitorio para encontrar algo que pueda ayudarte.\n")
        elif self.current_room.name == "Cocina":
            print("Pista: El cuchillo podría ser útil en una situación de emergencia.\n")
        else:
            print("No hay pistas disponibles en este momento.\n")

    def show_help(self, args=None):
        print("\nComandos disponibles:")
        print("ir [dirección] - Moverse a otra habitación (norte, sur, este, oeste)")
        print("agarrar [objeto] - Agarrar un objeto de la habitación")
        print("usar [objeto] - Usar un objeto de tu inventario")
        print("hablar [nombre] - Hablar con un personaje en la habitación")
        print("inventario - Mostrar tu inventario")
        print("guardar [nombre_archivo] - Guardar el juego")
        print("cargar [nombre_archivo] - Cargar una partida guardada")
        print("pista - Obtener una pista")
        print("ayuda - Mostrar esta ayuda")
        print("salir - Salir del juego\n")

    def exit_game(self, args=None):
        print("¡Gracias por jugar! ¡Hasta la próxima!")
        sys.exit()

    def end_game(self):
        print("¡Has completado tu misión! Elysius está a salvo gracias a ti.")
        print("¡Felicidades! Has completado el juego.")
        self.game_over = True
        sys.exit()

    def play(self):
        print("¡Bienvenido al juego de aventuras de texto!")
        print("Escribe 'ayuda' para ver los comandos disponibles.\n")
        self.show_current_room()
        while True:
            user_input = input("> ").lower().strip()
            self.process_command(user_input)

    def process_command(self, user_input):
        if not user_input:
            return
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]
        # Manejar sinónimos
        synonyms = {
            'moverse': 'ir',
            'caminar': 'ir',
            'desplazarse': 'ir',
            'examinar': 'agarrar',
            'observar': 'agarrar',
            'interactuar': 'usar',
            # Agregar más sinónimos según sea necesario
        }
        command = synonyms.get(command, command)
        action = self.commands.get(command)
        if action:
            action(args)
        else:
            print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n")

if __name__ == "__main__":
    game = Game()
    game.play()
