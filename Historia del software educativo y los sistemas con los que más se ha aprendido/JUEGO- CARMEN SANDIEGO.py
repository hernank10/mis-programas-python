import random
import time

# ==========================================
#   DATOS DEL MUNDO
# ==========================================

CITIES = {
    "París": {
        "pistas": [
            "Escuchaste a alguien mencionar croissants.",
            "Un testigo vio a la sospechosa frente a la Torre Eiffel.",
            "Alguien hablaba de moda y alta costura."
        ],
        "salidas": ["Londres", "Roma", "Madrid"]
    },
    "Londres": {
        "pistas": [
            "Una pista menciona lluvia y paraguas.",
            "Alguien mencionó el Big Ben.",
            "Escuchaste sobre té de la tarde."
        ],
        "salidas": ["París", "Dublín", "Berlín"]
    },
    "Roma": {
        "pistas": [
            "Mencionaron ruinas antiguas.",
            "Alguien hablaba de pasta fresca.",
            "Un testigo vio a la sospechosa cerca del Coliseo."
        ],
        "salidas": ["París", "Atenas", "Madrid"]
    },
    "Madrid": {
        "pistas": [
            "Oíste sobre flamenco.",
            "Alguien mencionó la Puerta del Sol.",
            "Se habló sobre tapas y paella."
        ],
        "salidas": ["París", "Roma", "Lisboa"]
    },
    "Lisboa": {
        "pistas": [
            "Se habló de fados tristes.",
            "Un testigo vio tranvías amarillos.",
            "Escuchaste sobre pasteles de nata."
        ],
        "salidas": ["Madrid", "Dublín"]
    },
    "Berlín": {
        "pistas": [
            "Mencionaron el Muro y museos.",
            "Alguien hablaba de currywurst.",
            "Un testigo oyó música electrónica."
        ],
        "salidas": ["Londres", "Praga"]
    },
    "Atenas": {
        "pistas": [
            "Escuchaste algo sobre templos antiguos.",
            "Mencionaron la Acrópolis.",
            "Alguien hablaba de mitología griega."
        ],
        "salidas": ["Roma", "Estambul"]
    },
}

SUSPECTS = [
    "Lola la Escurridiza",
    "Marcos el Sombrío",
    "Isabel la Fantasma",
    "Rafael Rápido",
    "Carmen Sandiego"
]

# LA VILLANA REAL
TARGET = "Carmen Sandiego"

# ==========================================
#   ESTADO DEL JUEGO
# ==========================================

class Game:
    def __init__(self):
        self.current_city = random.choice(list(CITIES.keys()))
        self.route = self.generate_route()
        self.position = 0
        self.hours = 72  # tienes 3 días para atraparla

    def generate_route(self):
        """Genera un camino aleatorio que sigue la villana."""
        cities = list(CITIES.keys())
        route = [random.choice(cities)]
        for _ in range(5):
            route.append(random.choice(CITIES[route[-1]]["salidas"]))
        return route

    def show_status(self):
        print("\n──────── ESTADO ────────")
        print(f"Ciudad actual: {self.current_city}")
        print(f"Horas restantes: {self.hours}")
        print(f"Pista: Viajó a {self.route[self.position] if self.position < len(self.route) else '???'}")
        print("─────────────────────────\n")

    def get_clue(self):
        print("\nBuscando pista...\n")
        time.sleep(1)
        pista = random.choice(CITIES[self.current_city]["pistas"])
        print(f"📌 Pista encontrada: {pista}\n")
        self.hours -= 3

    def travel(self):
        print("\nCiudades disponibles para viajar:")
        for i, c in enumerate(CITIES[self.current_city]["salidas"], 1):
            print(f"{i}. {c}")

        choice = input("¿A qué ciudad deseas viajar? (número): ")

        try:
            index = int(choice) - 1
            if index < 0:
                raise ValueError
            dest = CITIES[self.current_city]["salidas"][index]
        except:
            print("Entrada inválida.")
            return

        print(f"\n✈ Viajando a {dest}...\n")
        time.sleep(1)

        self.current_city = dest
        self.hours -= 5

        if self.position < len(self.route) and dest == self.route[self.position]:
            self.position += 1

    def guess(self):
        print("\n¿Quién crees que es la sospechosa?")
        for i, s in enumerate(SUSPECTS, 1):
            print(f"{i}. {s}")

        choice = input("Elige un número: ")

        try:
            suspect = SUSPECTS[int(choice)-1]
        except:
            print("Selección inválida.")
            return

        if suspect == TARGET:
            print("\n🎉 ¡La atrapaste! Carmen Sandiego está bajo custodia.\n")
            exit()
        else:
            print("\n❌ Has arrestado a la persona equivocada.\n")
            self.hours -= 10

    def play(self):
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("   🕵️ JUEGO: CARMEN SANDIEGO   ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Comienzas en: {self.current_city}")
        print("Tienes 72 horas para atraparla.\n")

        while self.hours > 0:
            print("1. Buscar pista")
            print("2. Viajar")
            print("3. Estado")
            print("4. Adivinar sospechosa")
            print("5. Salir\n")

            option = input("Elige una opción: ")

            if option == "1":
                self.get_clue()
            elif option == "2":
                self.travel()
            elif option == "3":
                self.show_status()
            elif option == "4":
                self.guess()
            elif option == "5":
                print("Juego terminado.")
                break
            else:
                print("Opción inválida.\n")

            if self.position == len(self.route):
                print("\n💥 ¡Has seguido toda la ruta! Carmen está en esta ciudad.")
                print("Adivina correctamente para capturarla.\n")

        if self.hours <= 0:
            print("\n⏳ Tiempo agotado. Carmen escapó.\n")

# ==========================================
#   INICIO DEL JUEGO
# ==========================================

if __name__ == "__main__":
    Game().play()
