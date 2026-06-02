class Evento:
    def __init__(self, descripcion, accion):
        self.descripcion = descripcion
        self.accion = accion

class Juego:
    def __init__(self):
        self.eventos = []
        self.estado = "inicio"

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def procesar_eventos(self):
        for evento in self.eventos:
            print(evento.descripcion)
            evento.accion()
        self.eventos = []

    def jugar(self):
        while True:
            comando = input("¿Qué deseas hacer? ")
            if comando == "salir":
                break
            elif comando == "evento":
                self.agregar_evento(Evento("Un extraño aparece.", lambda: print("Es un aliado.")))
            self.procesar_eventos()

if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
