class Escenario:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetos = []
        self.personajes = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def mostrar_escenario(self):
        print(f"Te encuentras en {self.nombre}. {self.descripcion}")
        if self.objetos:
            print("Objetos presentes:")
            for objeto in self.objetos:
                print(f"- {objeto.nombre}")
