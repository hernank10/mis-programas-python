import re

def mostrar_reglas():
    reglas = [
        "Regla 1: Los verbos terminados en 'cer' y 'cir' y sus afines y derivados se escriben con 'C', así como las demás palabras que acaben en 'cer'.",
        "Regla 2: Ejemplo de otra regla ortográfica.",
        # Agrega más reglas aquí
    ]
    print("Reglas:")
    for i, regla in enumerate(reglas, start=1):
        print(f"{i}. {regla}")
    return reglas

def seleccionar_regla(reglas):
    while True:
        try:
            seleccion = int(input("Selecciona el número de la regla que deseas ver: ")) - 1
            if 0 <= seleccion < len(reglas):
                return reglas[seleccion]
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def mostrar_historia(historia):
    print(historia)
    return historia

def seleccionar_historia(historias):
    print("\nHistorias disponibles:")
    for i, _ in enumerate(historias, start=1):
        print(f"{i}. Historia {i}")
    while True:
        try:
            seleccion = int(input("Selecciona el número de la historia que deseas escuchar: ")) - 1
            if 0 <= seleccion < len(historias):
                return historias[seleccion]
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def extraer_palabras_con_cer_y_cir(texto):
    palabras = re.findall(r'\b\w+cer\b|\b\w+cir\b', texto)
    return palabras

def dictado_palabras(palabras):
    for palabra in palabras:
        respuesta = input(f"Escribe la palabra que termina en 'cer' o 'cir' que escuchaste: ").strip().lower()
        if respuesta == palabra:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es '{palabra}'.")

def main():
    reglas = mostrar_reglas()
    regla_seleccionada = seleccionar_regla(reglas)
    print(f"\nHas seleccionado: {regla_seleccionada}\n")

    historias = [
        """
        En un pequeño pueblo, había un anciano que solía crecer hermosas flores en su jardín. 
        A pesar de su avanzada edad, siempre se encontraba haciendo cosas que le hacían parecer más joven. 
        Le gustaba conocer a nuevas personas y compartir su conocimiento sobre el crecimiento de las plantas. 
        Su jardín siempre estaba lleno de flores crecientes que atraían a muchas abejas. 
        Un día, decidió construir un pequeño estanque para que los patos pudieran nadar y crecer en un ambiente seguro. 
        Cada vez que alguien pasaba por su jardín, no podía evitar admirar la dedicación y el esfuerzo que el anciano ponía en hacer crecer su pequeño paraíso. 
        Con el tiempo, el jardín se convirtió en un lugar de encuentro para todos los vecinos que querían aprender a cultivar y cuidar sus propias plantas.
        """,
        """
        En una ciudad lejana, una científica descubrió un método para hacer crecer plantas de manera acelerada. 
        Ella comenzó a colaborar con varias universidades para conocer más sobre los efectos de este descubrimiento. 
        Su laboratorio siempre estaba lleno de plantas en crecimiento y se convirtió en un centro de investigación muy importante. 
        Muchos estudiantes querían aprender de ella y aplicar sus conocimientos en otros campos de la ciencia. 
        A pesar de algunos contratiempos, la científica siguió creciendo en su carrera y haciendo importantes contribuciones al mundo.
        """
        # Agrega más historias aquí
    ]
    
    historia_seleccionada = seleccionar_historia(historias)
    print(f"\nHas seleccionado la siguiente historia:\n")
    historia = mostrar_historia(historia_seleccionada)
    
    palabras = extraer_palabras_con_cer_y_cir(historia)
    print("\nAhora, escribe las palabras que terminan en 'cer' o 'cir' que escuchaste en la historia.\n")
    dictado_palabras(palabras)

if __name__ == "__main__":
    main()
