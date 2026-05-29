import time
import random
import os

# Lista de las 28 letras del alfabeto árabe
letras_arabes = [
    {"letra": "ا", "nombre": "Alif", "sonido": "a", "unicode": "U+0627"},
    {"letra": "ب", "nombre": "Ba", "sonido": "b", "unicode": "U+0628"},
    {"letra": "ت", "nombre": "Ta", "sonido": "t", "unicode": "U+062A"},
    {"letra": "ث", "nombre": "Tha", "sonido": "th", "unicode": "U+062B"},
    {"letra": "ج", "nombre": "Jim", "sonido": "j", "unicode": "U+062C"},
    {"letra": "ح", "nombre": "Ha", "sonido": "h (aspirado)", "unicode": "U+062D"},
    {"letra": "خ", "nombre": "Kha", "sonido": "kh", "unicode": "U+062E"},
    {"letra": "د", "nombre": "Dal", "sonido": "d", "unicode": "U+062F"},
    {"letra": "ذ", "nombre": "Dhal", "sonido": "dh", "unicode": "U+0630"},
    {"letra": "ر", "nombre": "Ra", "sonido": "r", "unicode": "U+0631"},
    {"letra": "ز", "nombre": "Zay", "sonido": "z", "unicode": "U+0632"},
    {"letra": "س", "nombre": "Sin", "sonido": "s", "unicode": "U+0633"},
    {"letra": "ش", "nombre": "Shin", "sonido": "sh", "unicode": "U+0634"},
    {"letra": "ص", "nombre": "Sad", "sonido": "s (enfático)", "unicode": "U+0635"},
    {"letra": "ض", "nombre": "Dad", "sonido": "d (enfático)", "unicode": "U+0636"},
    {"letra": "ط", "nombre": "Ta", "sonido": "t (enfático)", "unicode": "U+0637"},
    {"letra": "ظ", "nombre": "Za", "sonido": "z (enfático)", "unicode": "U+0638"},
    {"letra": "ع", "nombre": "Ayn", "sonido": "ʿ", "unicode": "U+0639"},
    {"letra": "غ", "nombre": "Ghayn", "sonido": "gh", "unicode": "U+063A"},
    {"letra": "ف", "nombre": "Fa", "sonido": "f", "unicode": "U+0641"},
    {"letra": "ق", "nombre": "Qaf", "sonido": "q", "unicode": "U+0642"},
    {"letra": "ك", "nombre": "Kaf", "sonido": "k", "unicode": "U+0643"},
    {"letra": "ل", "nombre": "Lam", "sonido": "l", "unicode": "U+0644"},
    {"letra": "م", "nombre": "Mim", "sonido": "m", "unicode": "U+0645"},
    {"letra": "ن", "nombre": "Nun", "sonido": "n", "unicode": "U+0646"},
    {"letra": "هـ", "nombre": "Ha", "sonido": "h", "unicode": "U+0647"},
    {"letra": "و", "nombre": "Waw", "sonido": "w/u", "unicode": "U+0648"},
    {"letra": "ي", "nombre": "Ya", "sonido": "y/i", "unicode": "U+064A"}
]

# Mostrar con estilo y pausa
def mostrar_letra(letra_info):
    os.system('clear')  # En Windows usa 'cls'
    print("\033[1;36m" + "=" * 40 + "\033[0m")
    print(f"\033[1;32m   Letra Árabe: \033[1;37m{letra_info['letra']}")
    print(f"\033[1;32m   Nombre:      \033[1;37m{letra_info['nombre']}")
    print(f"\033[1;32m   Sonido:      \033[1;37m{letra_info['sonido']}")
    print(f"\033[1;32m   Unicode:     \033[1;37m{letra_info['unicode']}")
    print("\033[1;36m" + "=" * 40 + "\033[0m")
    time.sleep(2)

# Mostrar en orden
def mostrar_en_orden():
    for letra in letras_arabes:
        mostrar_letra(letra)

# Mostrar al azar
def mostrar_azar():
    letra = random.choice(letras_arabes)
    mostrar_letra(letra)

# Menú interactivo
def menu():
    while True:
        print("\n\033[1;34m*** Aprende el alfabeto árabe ***\033[0m")
        print("1. Mostrar letras en orden")
        print("2. Mostrar una letra al azar")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            mostrar_en_orden()
        elif opcion == "2":
            mostrar_azar()
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciar
if __name__ == "__main__":
    menu()
