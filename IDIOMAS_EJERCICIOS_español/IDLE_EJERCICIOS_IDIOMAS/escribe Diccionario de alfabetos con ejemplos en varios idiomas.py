import os

# Diccionario de alfabetos con ejemplos en varios idiomas
alfabetos = {
    "Español": {
        "nombre": "alfabeto español",
        "letras": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "ejemplo": "El alfabeto español tiene 27 letras, incluyendo la letra ñ."
    },
    "Inglés": {
        "nombre": "alfabeto inglés",
        "letras": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "ejemplo": "El alfabeto inglés tiene 26 letras."
    },
    "Francés": {
        "nombre": "alfabeto francés",
        "letras": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "ejemplo": "El francés usa acentos como é, à, è, â, ù."
    },
    "Portugués": {
        "nombre": "alfabeto portugués",
        "letras": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "ejemplo": "El portugués incluye caracteres como ç y tildes como ã y õ."
    },
    "Alemán": {
        "nombre": "alfabeto alemán",
        "letras": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "ü", "ß"],
        "ejemplo": "El alemán tiene caracteres especiales como ä, ö, ü y ß."
    },
    "Polaco": {
        "nombre": "alfabeto polaco",
        "letras": ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ż", "ź"],
        "ejemplo": "El polaco tiene caracteres únicos como ą, ę, ł y ż."
    },
}

def mostrar_menu():
    print("\nIdiomas disponibles para practicar:")
    for i, idioma in enumerate(alfabetos.keys(), 1):
        print(f"{i}. {idioma}")
    print("0. Salir")

def practicar_idioma(eleccion):
    idioma = list(alfabetos.keys())[eleccion - 1]
    datos = alfabetos[idioma]

    print(f"\nPracticando el {datos['nombre']}:")
    print("Letras:", ", ".join(datos["letras"]))
    print("Ejemplo:", datos["ejemplo"])

    input("\nPresiona Enter para regresar al menú.")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menu()

        try:
            opcion = int(input("\nElige una opción: "))
            if opcion == 0:
                print("\nGracias por practicar los alfabetos. ¡Hasta pronto!")
                break
            elif 1 <= opcion <= len(alfabetos):
                practicar_idioma(opcion)
            else:
                print("\nOpción inválida. Inténtalo de nuevo.")
        except ValueError:
            print("\nPor favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
