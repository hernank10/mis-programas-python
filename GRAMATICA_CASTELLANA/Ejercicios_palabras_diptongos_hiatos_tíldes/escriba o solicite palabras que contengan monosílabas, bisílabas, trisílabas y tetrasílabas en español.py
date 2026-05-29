def contar_silabas(palabra):
    # Definir patrón de sílabas utilizando expresiones regulares
    patron_silabas = re.compile(r'[aeiouáéíóúü]+', re.IGNORECASE)

    # Contar el número de sílabas en la palabra
    silabas = re.findall(patron_silabas, palabra)
    return len(silabas)


def clasificar_palabra(palabra):
    num_silabas = contar_silabas(palabra)

    if num_silabas == 1:
        return 'monosílaba'
    elif num_silabas == 2:
        return 'bisílaba'
    elif num_silabas == 3:
        return 'trisílaba'
    elif num_silabas == 4:
        return 'tetrásilaba'
    else:
        return 'polisílaba'


# Solicitar al usuario un fragmento de texto
fragmento_texto = input("Ingrese un fragmento de texto: ")

# Dividir el fragmento de texto en palabras
palabras = re.findall(r'\b\w+\b', fragmento_texto)

# Solicitar al usuario que clasifique palabras por número de sílabas
palabras_clasificadas = []
for palabra in palabras:
    clasificacion = clasificar_palabra(palabra)
    respuesta = input(f"¿La palabra '{palabra}' es {clasificacion}? (Sí/No): ").lower()

    if respuesta == 'sí':
        palabras_clasificadas.append((palabra, clasificacion))

# Mostrar las palabras clasificadas
print("\nPalabras clasificadas:")
for palabra, clasificacion in palabras_clasificadas:
    print(f"{palabra}: {clasificacion}")
