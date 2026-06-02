import sys
import json
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Dirección: Nombre de la habitación
        self.items = []  # Lista de objetos en la habitación
        self.characters = []  # Lista de personajes en la habitación
        self.events = []  # Lista de eventos en la habitación

    def set_exit(self, direction, room_name):
        self.exits[direction] = room_name

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def add_character(self, character):
        self.characters.append(character)

    def add_event(self, event):
        self.events.append(event)

class Character:
    def __init__(self, name, description, dialogues):
        self.name = name
        self.description = description
        self.dialogues = dialogues  # Diccionario con diálogos según el estado del juego
        self.is_active = True

    def talk(self, game_state):
        return self.dialogues.get(game_state, self.dialogues.get('default', f"{self.name} no tiene nada que decir ahora."))

class Event:
    def __init__(self, trigger, description, action):
        self.trigger = trigger  # Función que retorna True/False
        self.description = description
        self.action = action  # Función a ejecutar cuando el evento se desencadena

class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None
        self.inventory = []
        self.game_state = "inicio"
        self.game_over = False
        self.commands = {
            'ir': self.move,
            'moverse': self.move,
            'caminar': self.move,
            'agarrar': self.grab,
            'usar': self.use_item,
            'hablar': self.talk,
            'inventario': self.show_inventory,
            'guardar': self.save_game,
            'cargar': self.load_game,
            'ayuda': self.show_help,
            'salir': self.exit_game
        }
        self.setup_game()

    def setup_game(self):
        # Crear habitaciones
        plaza = Room("Plaza Central", "Una amplia plaza con fuentes y estatuas abandonadas.")
        supermercado = Room("Supermercado Abandonado", "Estantes vacíos y pasillos oscuros.")
        refugio = Room("Refugio Subterráneo", "Un refugio seguro con suministros básicos.")
        calle = Room("Calle Desierta", "Calles vacías con edificios deteriorados.")
        parque = Room("Parque Olvidado", "Áreas verdes descuidadas y caminos de tierra.")

        # Definir salidas
        plaza.set_exit("norte", "Supermercado Abandonado")
        plaza.set_exit("este", "Calle Desierta")
        plaza.set_exit("oeste", "Parque Olvidado")
        supermercado.set_exit("sur", "Plaza Central")
        calle.set_exit("oeste", "Plaza Central")
        parque.set_exit("este", "Plaza Central")
        refugio.set_exit("abajo", "Calle Desierta")

        # Agregar objetos
        plaza.add_item("Mapa de la Ciudad")
        supermercado.add_item("Linterna")
        supermercado.add_item("Cuerda")
        refugio.add_item("Kit de Primeros Auxilios")
        calle.add_item("Batería de Respaldo")
        parque.add_item("Comida Enlatada")

        # Crear personajes
        ana_dialogues = {
            "inicio": "Ana: Hola, Tomson. Gracias por venir. Necesitamos encontrar más suministros.",
            "after_collect_supplies": "Ana: ¡Excelente! Con estos suministros podemos sobrevivir más tiempo.",
            "default": "Ana: Estamos en una situación difícil."
        }
        ana = Character("Ana", "Una sobreviviente inteligente y valiente.", ana_dialogues)

        # Agregar personajes a habitaciones
        plaza.add_character(ana)

        # Crear eventos
        def encontrar_personaje(game):
            return "Linterna" in game.inventory and not any(isinstance(c, Character) and c.name == "Carlos" for c in game.current_room.characters)

        def evento_encontrar_carlos(game):
            carlos_dialogues = {
                "inicio": "Carlos: ¡Gracias por la linterna! Estaba perdido en el Supermercado.",
                "after_collect_supplies": "Carlos: Con tus suministros, podemos mejorar nuestro refugio.",
                "default": "Carlos: Estoy aquí para ayudarte."
            }
            carlos = Character("Carlos", "Un técnico con conocimientos en electricidad.", carlos_dialogues)
            game.current_room.add_character(carlos)
            print(Fore.GREEN + "*** Evento: Carlos ha aparecido en la habitación. ***" + Style.RESET_ALL)

        encontrar_event = Event(encontrar_personaje, "Carlos ha encontrado su camino al refugio gracias a la linterna.", evento_encontrar_carlos)
        plaza.add_event(encontrar_event)

        # Guardar habitaciones
        self.rooms = {
            "Plaza Central": plaza,
            "Supermercado Abandonado": supermercado,
            "Refugio Subterráneo": refugio,
            "Calle Desierta": calle,
            "Parque Olvidado": parque
        }

        # Establecer habitación inicial
        self.current_room = plaza

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
        self.process_events()

    def process_events(self):
        for event in self.current_room.events:
            if event.trigger(self):
                print(Fore.GREEN + f"*** Evento: {event.description} ***" + Style.RESET_ALL)
                event.action(self)

    def show_help(self, args=None):
        print("\n" + Fore.BLUE + "Comandos disponibles:" + Style.RESET_ALL)
        print("ir [dirección] - Moverse a otra habitación (norte, sur, este, oeste, abajo)")
        print("agarrar [objeto] - Agarrar un objeto de la habitación")
        print("usar [objeto] - Usar un objeto de tu inventario")
        print("hablar [nombre] - Hablar con un personaje en la habitación")
        print("inventario - Mostrar tu inventario")
        print("guardar [nombre_archivo] - Guardar el juego")
        print("cargar [nombre_archivo] - Cargar una partida guardada")
        print("ayuda - Mostrar esta ayuda")
        print("salir - Salir del juego\n")

    def move(self, args):
        if not args:
            print(Fore.RED + "¿A dónde quieres ir?\n" + Style.RESET_ALL)
            return
        direction = args[0].lower()
        if direction in self.current_room.exits:
            next_room_name = self.current_room.exits[direction]
            self.current_room = self.rooms.get(next_room_name)
            self.show_current_room()
        else:
            print(Fore.RED + "No puedes ir en esa dirección.\n" + Style.RESET_ALL)

    def grab(self, args):
        if not args:
            print(Fore.RED + "¿Qué quieres agarrar?\n" + Style.RESET_ALL)
            return
        item_name = ' '.join(args).title()
        if item_name in self.current_room.items:
            self.inventory.append(item_name)
            self.current_room.remove_item(item_name)
            print(Fore.GREEN + f"Has agarrado '{item_name}'.\n" + Style.RESET_ALL)
            # Actualizar estado del juego si es necesario
            if item_name == "Linterna":
                self.game_state = "tiene_linterna"
        else:
            print(Fore.RED + f"No ves '{item_name}' aquí.\n" + Style.RESET_ALL)

    def use_item(self, args):
        if not args:
            print(Fore.RED + "¿Qué quieres usar?\n" + Style.RESET_ALL)
            return
        item_name = ' '.join(args).title()
        if item_name in self.inventory:
            if item_name == "Mapa De La Ciudad":
                print(Fore.GREEN + "Has consultado el Mapa de la Ciudad. Ahora sabes dónde están los refugios seguros.\n" + Style.RESET_ALL)
                self.game_state = "usa_mapa"
            elif item_name == "Linterna":
                print(Fore.GREEN + "Has encendido la Linterna. La oscuridad en el Supermercado Abandonado ahora es manejable.\n" + Style.RESET_ALL)
                self.game_state = "usa_linterna"
            elif item_name == "Cuerda":
                print(Fore.GREEN + "Has usado la Cuerda para escalar el edificio y acceder a un área elevada.\n" + Style.RESET_ALL)
                self.game_state = "usa_cuerda"
            elif item_name == "Kit De Primeros Auxilios":
                print(Fore.GREEN + "Has usado el Kit de Primeros Auxilios para tratar una herida.\n" + Style.RESET_ALL)
                self.game_state = "usa_kit"
            elif item_name == "Batería De Respaldo":
                print(Fore.GREEN + "Has cargado tu teléfono con la Batería de Respaldo. Ahora puedes contactar ayuda.\n" + Style.RESET_ALL)
                self.game_state = "usa_bateria"
            elif item_name == "Comida Enlatada":
                print(Fore.GREEN + "Has consumido algo de la Comida Enlatada. Recuperas energía.\n" + Style.RESET_ALL)
                self.game_state = "usa_comida"
            else:
                print(Fore.YELLOW + f"No sabes cómo usar '{item_name}' aquí.\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"No tienes '{item_name}' en tu inventario.\n" + Style.RESET_ALL)

    def talk(self, args):
        if not args:
            print(Fore.RED + "¿Con quién quieres hablar?\n" + Style.RESET_ALL)
            return
        character_name = ' '.join(args).title()
        for character in self.current_room.characters:
            if character.name == character_name and character.is_active:
                dialogue = character.talk(self.game_state)
                print(Fore.YELLOW + f"\n{dialogue}\n" + Style.RESET_ALL)
                # Actualizar estado del juego basado en la conversación
                if character.name == "Ana" and self.game_state == "usa_comida":
                    print(Fore.GREEN + "Ana: ¡Gracias por compartir la comida! Ahora estamos más fuertes juntos.\n" + Style.RESET_ALL)
                    self.game_state = "after_collect_supplies"
                return
        print(Fore.RED + f"No hay a '{character_name}' aquí para hablar.\n" + Style.RESET_ALL)

    def show_inventory(self, args=None):
        if self.inventory:
            print(Fore.CYAN + "\nTienes los siguientes objetos en tu inventario:" + Style.RESET_ALL)
            for item in self.inventory:
                print(f"- {item}")
            print()
        else:
            print(Fore.CYAN + "\nTu inventario está vacío.\n" + Style.RESET_ALL)

    def save_game(self, args):
        if not args:
            print(Fore.RED + "¿Cómo quieres llamar al archivo de guardado?\n" + Style.RESET_ALL)
            return
        filename = args[0] + ".json"
        game_data = {
            "current_room": self.current_room.name,
            "inventory": self.inventory,
            "game_state": self.game_state
        }
        with open(filename, 'w') as f:
            json.dump(game_data, f)
        print(Fore.GREEN + f"Juego guardado en '{filename}'.\n" + Style.RESET_ALL)

    def load_game(self, args):
        if not args:
            print(Fore.RED + "¿Qué archivo de guardado quieres cargar?\n" + Style.RESET_ALL)
            return
        filename = args[0] + ".json"
        try:
            with open(filename, 'r') as f:
                game_data = json.load(f)
            self.current_room = self.rooms.get(game_data["current_room"], self.current_room)
            self.inventory = game_data.get("inventory", [])
            self.game_state = game_data.get("game_state", "inicio")
            print(Fore.GREEN + f"Juego cargado desde '{filename}'.\n" + Style.RESET_ALL)
            self.show_current_room()
        except FileNotFoundError:
            print(Fore.RED + f"No se encontró el archivo '{filename}'.\n" + Style.RESET_ALL)
        except json.JSONDecodeError:
            print(Fore.RED + f"El archivo '{filename}' está corrupto o tiene un formato inválido.\n" + Style.RESET_ALL)

    def exit_game(self, args=None):
        print(Fore.GREEN + "¡Gracias por jugar! ¡Hasta la próxima!\n" + Style.RESET_ALL)
        sys.exit()

    def end_game(self):
        print(Fore.GREEN + "¡Has completado tu misión y sobrevivido en la Ciudad Salvaje! Elysius está a salvo gracias a tu valentía y habilidades." + Style.RESET_ALL)
        print(Fore.GREEN + "¡Felicidades! Has completado el juego.\n" + Style.RESET_ALL)
        self.game_over = True
        sys.exit()

    def play(self):
        print(Fore.BLUE + "¡Bienvenido a 'Tomson en la Ciudad Salvaje'!" + Style.RESET_ALL)
        print("Eres Tomson, un sobreviviente que ha llegado a una ciudad post-apocalíptica.")
        print("Tu objetivo es sobrevivir, encontrar suministros y descubrir qué causó el colapso de la civilización.")
        print("Escribe 'ayuda' para ver los comandos disponibles.\n")
        self.show_current_room()

        while not self.game_over:
            user_input = input(Fore.CYAN + "> " + Style.RESET_ALL).lower().strip()
            if not user_input:
                continue
            parts = user_input.split()
            command = parts[0]
            args = parts[1:]
            action = self.commands.get(command)
            if action:
                action(args)
                # Verificar si se ha alcanzado el final del juego
                if self.game_state == "after_collect_supplies" and "Carlos" in [c.name for c in self.current_room.characters]:
                    self.end_game()
            else:
                print(Fore.RED + "Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n" + Style.RESET_ALL)

# Ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.play()
