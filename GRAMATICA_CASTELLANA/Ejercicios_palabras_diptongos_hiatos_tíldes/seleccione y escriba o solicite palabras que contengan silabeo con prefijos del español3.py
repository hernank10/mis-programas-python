def contar_silabas(palabra):
    # Función para contar el número de sílabas en una palabra
    # Puedes personalizar esta función según tus necesidades

    # Implementa aquí tu lógica para contar las sílabas
    # Puede ser manual o utilizando alguna librería externa

    return 0  # Reemplaza con el número real de sílabas


def clasificar_palabra(palabra):
    num_silabas = contar_silabas(palabra)

    if num_silabas == 1:
        return "monosílaba"
    elif num_silabas == 2:
        return "bisílaba"
    elif num_silabas == 3:
        return "trisílaba"
    elif num_silabas == 4:
        return "tetrasílaba"
    else:
        return "polisílaba"


def main():
    fragmento = input("Ingresa un fragmento de texto: ")
    palabras = fragmento.split()

    for palabra in palabras:
        clasificacion = clasificar_palabra(palabra.lower())
        print(f"{palabra}: {clasificacion}")


if __name__ == "__main__":
    main()
