import random

def aprender_reglas_z():
    """Función para aprender las reglas de la letra z."""

    reglas = [
        "Se escribe con z al final de palabras como 'paz', 'luz', 'mezcla'.",
        "Antes de las vocales a, o y u se escribe z, como en 'zapato', 'zorro', 'azul'.",
        "Los verbos que terminan en -izar suelen llevar z, como 'realizar', 'organizar'.",
        "Los sustantivos abstractos que terminan en -ez o -eza llevan z, como 'belleza', 'fortaleza'.",
        "Los aumentativos y diminutivos que terminan en -azo, -aza, -uza suelen llevar z, como 'golpazo', 'cicatriz'.",
        "Los sustantivos que terminan en -azgo llevan z, como 'almirantazgo'.",
        "Los adjetivos y sustantivos que terminan en -az llevan z, como 'locuaz', 'tenaz'.",
        # Agrega aquí más reglas si las encuentras
    ]

    while True:
        # Elegir una regla al azar
        regla_aleatoria = random.choice(reglas)

        # Mostrar la regla y pedir que se escriba
        print(regla_aleatoria)
        respuesta = input("Escribe la regla con tus palabras: ")

        # Comparar la respuesta con la regla original (opcional)
        # Puedes implementar una función más compleja para evaluar la respuesta
        # si deseas ser más preciso en la corrección.

        # Preguntar si quiere continuar
        continuar = input("¿Quieres seguir practicando? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    aprender_reglas_z()
