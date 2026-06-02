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


class Objeto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def usar(self, personaje):
        pass

class Poción(Objeto):
    def __init__(self, nombre, descripcion, curacion):
        super().__init__(nombre, descripcion)
        self.curacion = curacion

    def usar(self, personaje):
        print(f"{personaje.nombre} usa {self.nombre} y recupera {self.curacion} puntos de salud.")
        personaje.salud += self.curacion

# Crear un personaje y un objeto
frodo = Personaje("Frodo", 50)
pocion = Poción("Poción de Salud", "Una poción que cura al personaje.", 30)

# Usar el objeto
pocion.usar(frodo)
print(f"Salud de {frodo.nombre}: {frodo.salud}")



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





class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def atacar(self, otro_personaje):
        pass

class Guerrero(Personaje):
    def __init__(self, nombre, salud, fuerza):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self, otro_personaje):
        print(f"{self.nombre} ataca a {otro_personaje.nombre} con {self.fuerza} puntos de daño.")
        otro_personaje.salud -= self.fuerza

class Mago(Personaje):
    def __init__(self, nombre, salud, magia):
        super().__init__(nombre, salud)
        self.magia = magia

    def atacar(self, otro_personaje):
        print(f"{self.nombre} lanza un hechizo a {otro_personaje.nombre} con {self.magia} puntos de daño.")
        otro_personaje.salud -= self.magia
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        self.inventario = []

    def recoger_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"{self.nombre} ha recogido {objeto.nombre}.")

    def mostrar_inventario(self):
        if self.inventario:
            print(f"{self.nombre} tiene los siguientes objetos:")
            for objeto in self.inventario:
                print(f"- {objeto.nombre}")
        else:
            print(f"{self.nombre} no tiene ningún objeto.")
class Personaje:
    def __init__(self, nombre, descripcion, salud):
        self.nombre = nombre
        self.descripcion = descripcion
        self.salud = salud

    def mostrar_descripcion(self):
        print(f"{self.nombre}: {self.descripcion} (Salud: {self.salud})")

# Creación de personajes
gandalf = Personaje("Gandalf", "Un poderoso mago de larga barba blanca.", 100)
frodo = Personaje("Frodo", "Un hobbit valiente con una gran misión.", 80)

# Mostrar descripciones
gandalf.mostrar_descripcion()
frodo.mostrar_descripcion()


class Acertijo:
    def __init__(self, pregunta, respuesta_correcta):
        self.pregunta = pregunta
        self.respuesta_correcta = respuesta_correcta

    def resolver(self):
        respuesta = input(f"{self.pregunta} ")
        if respuesta.lower() == self.respuesta_correcta.lower():
            print("¡Correcto! Has resuelto el acertijo.")
            return True
        else:
            print("Respuesta incorrecta. Intenta de nuevo.")
            return False

# Creación de un acertijo
acertijo1 = Acertijo("¿Qué tiene un ojo pero no puede ver?", "aguja")

# Intentar resolver el acertijo
while not acertijo1.resolver():
    continue
