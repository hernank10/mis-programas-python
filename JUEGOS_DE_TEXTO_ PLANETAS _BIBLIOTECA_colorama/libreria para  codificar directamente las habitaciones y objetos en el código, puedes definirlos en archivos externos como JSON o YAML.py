import json

class Room:
    def __init__(self, name, description, exits, items):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items

class Game:
    def __init__(self, rooms_file):
        self.rooms = {}
        self.current_room = None
        self.load_rooms(rooms_file)
    
    def load_rooms(self, rooms_file):
        with open(rooms_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for name, details in data.items():
                room = Room(name, details['description'], details['exits'], details['items'])
                self.rooms[name] = room
        self.current_room = self.rooms["Nave Espacial"]
    
    def show_current_room(self):
        print(f"\nEstás en la {self.current_room.name}.")
        print(self.current_room.description)
        if self.current_room.items:
            print("Ves los siguientes objetos:")
            for item in self.current_room.items:
                print(f"- {item}")
        print("Salidas disponibles: " + ", ".join(self.current_room.exits.keys()))
        print()

# Uso del Juego
game = Game("rooms.json")
game.show_current_room()
