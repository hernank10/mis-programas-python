class Juego:
    def __init__(self):
        self.personajes = []
        self.acertijos = []

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)

    def agregar_acertijo(self, acertijo):
        self.acertijos.append(acertijo)

    def iniciar(self):
        print("Bienvenido al juego de texto.")
        for personaje in self.personajes:
            personaje.mostrar_descripcion()

        for acertijo in self.acertijos:
            while not acertijo.resolver():
                continue

# Creación y ejecución del juego
juego = Juego()
juego.agregar_personaje(gandalf)
juego.agregar_personaje(frodo)
juego.agregar_acertijo(acertijo1)
juego.iniciar()


class Jugador:
    def __init__(self):
        self.inventario = []
        self.salud = 100

    def mostrar_estado(self):
        print(f"Salud: {self.salud}")
        print(f"Inventario: {self.inventario}")

class Escenario:
    def __init__(self, descripcion):
        self.descripcion = descripcion
def ir_norte():
    print("Te mueves al norte.")

def hablar_con(nombre):
    print(f"Hablando con {nombre}.")

def examinar(objeto):
    print(f"Examinando {objeto}.")

comandos = {
    "ir norte": ir_norte,
    "hablar con": hablar_con,
    "examinar": examinar
}

def juego():
    jugador = Jugador()
    while True:
        entrada = input("¿Qué deseas hacer? ").strip().lower()
        if entrada in comandos:
            comandos[entrada]()
        elif entrada.startswith("hablar con "):
            nombre = entrada.split(" ", 2)[2]
            comandos["hablar con"](nombre)
        elif entrada.startswith("examinar "):
            objeto = entrada.split(" ", 1)[1]
            comandos["examinar"](objeto)
        elif entrada == "salir":
            print("Gracias por jugar.")
            break
        else:
            print("Comando no reconocido. Intenta de nuevo.")

juego()

def ayuda():
    print("Comandos disponibles:")
    for comando in comandos.keys():
        print(f"- {comando}")

# Añadir el comando de ayuda al diccionario
comandos["ayuda"] = ayuda

class Jugador:
    def __init__(self):
        self.inventario = []
        self.salud = 100

    def mostrar_estado(self):
        print(f"Salud: {self.salud}")
        print(f"Inventario: {self.inventario}")

class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.comandos = {
            "ir norte": self.ir_norte,
            "ayuda": self.ayuda
        }

    def ir_norte(self):
        print("Te mueves al norte.")

    def ayuda(self):
        print("Comandos disponibles:")
        for comando in self.comandos.keys():
            print(f"- {comando}")

    def iniciar(self):
        while True:
            entrada = input("¿Qué deseas hacer? ").strip().lower()
            if entrada in self.comandos:
                self.comandos[entrada]()
            elif entrada == "salir":
                print("Gracias por jugar.")
                break
            else:
                print("Comando no reconocido. Intenta de nuevo.")

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()
