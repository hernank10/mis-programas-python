import time

# Diccionario de letras en arte ASCII (versión simplificada)
ascii_abc = {
    'A': [
        " █████╗ ",
        "██╔══██╗",
        "███████║",
        "██╔══██║",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],
    'B': [
        "██████╗ ",
        "██╔══██╗",
        "██████╦╝",
        "██╔══██╗",
        "██████╦╝",
        "╚═════╝ "
    ],
    'C': [
        " ██████╗",
        "██╔════╝",
        "██║     ",
        "██║     ",
        "╚██████╗",
        " ╚═════╝"
    ],
        'E': [
        "███████╗",
        "██╔════╝",
        "██████╗ ",
        "██╔═══╝ ",
        "███████╗",
        "╚══════╝"
    ],
    'F': [
        "███████╗",
        "██╔════╝",
        "██████╗ ",
        "██╔═══╝ ",
        "██║     ",
        "╚═╝     "
    ],
    'G': [
        " ██████╗ ",
        "██╔════╝ ",
        "██║  ███╗",
        "██║  ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ],
    'H': [
        "██╗  ██╗",
        "██║  ██║",
        "███████║",
        "██╔═══██╗",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],

    # Añadir el resto de letras siguiendo el mismo formato...
}

def imprimir_ascii_vertical():
    for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letra in ascii_abc:
            # Imprimir cada línea de la letra con pausa
            for linea in ascii_abc[letra]:
                print(linea)
                time.sleep(0.05)
            
            # Pausa entre letras
            time.sleep(0.5)
            
            # Limpiar entre caracteres (descomentar para efecto de limpieza)
            # print("\033[2J\033[H")  # Limpiar consola en sistemas Unix
            
        else:
            print(f" {letra} ")  # Versión simple para letras no definidas

if __name__ == "__main__":
    print("\n\033[32m")  # Color verde
    imprimir_ascii_vertical()
    print("\033[0m")     # Resetear color
