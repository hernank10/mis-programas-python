class Paquete:
    def __init__(self, remitente, destinatario, contenido, estado="En tránsito"):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
        self.estado = estado

    def mostrar_estado(self):
        print(f"Paquete de '{self.remitente}' a '{self.destinatario}': {self.estado}")

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Nuevo estado del paquete: {self.estado}")


# Crear un paquete
paquete1 = Paquete("Juan", "María", "Libros")

# Mostrar el estado inicial
paquete1.mostrar_estado()

# Cambiar el estado del paquete
paquete1.cambiar_estado("En reparto")

# Mostrar el nuevo estado
paquete1.mostrar_estado()
