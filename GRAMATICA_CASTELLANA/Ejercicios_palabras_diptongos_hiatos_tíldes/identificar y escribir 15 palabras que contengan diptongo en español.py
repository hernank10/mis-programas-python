def identificar_diptongos(palabra):
    # Definir patrón de diptongos utilizando expresiones regulares
    patron_diptongo = re.compile(r'[aeiouáéíóúü]+[aeiouáéíóúü]+', re.IGNORECASE)

    # Buscar coincidencias en la palabra
    coincidencias = re.findall(patron_diptongo, palabra)

    # Devolver True si hay diptongos, False en caso contrario
    return len(coincidencias) > 0

# Lista de palabras conocidas con diptongos
palabras_con_diptongos = ["aire", "puerta", "tierra", "poesía", "cuídate", "héroe", "violín", "maíz", "poeta", "país", "cuaderno", "teatro", "ciudad", "ahí", "tío"]

# Identificar palabras con diptongos e imprimir el resultado
for palabra in palabras_con_diptongos:
    if identificar_diptongos(palabra):
        print(f"{palabra}: Contiene diptongo")
    else:
        print(f"{palabra}: No contiene diptongo")
