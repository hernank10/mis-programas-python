import re


def identificar_diptongos_hiatos(palabra):
    # Definir patrón de diptongos utilizando expresiones regulares
    patron_diptongo = re.compile(r'[aeiouáéíóúü]+[aeiouáéíóúü]+', re.IGNORECASE)

    # Definir patrón de hiatos utilizando expresiones regulares
    patron_hiato = re.compile(r'[aeiouáéíóúü]+[aeiouáéíóúü]+', re.IGNORECASE)

    # Verificar si la palabra contiene diptongo o hiato
    diptongo = bool(re.search(patron_diptongo, palabra))
    hiato = bool(re.search(patron_hiato, palabra))

    return diptongo, hiato


# Texto de ejemplo (puedes reemplazarlo con un artículo real)
articulo = """
La educación es fundamental para el desarrollo de cualquier sociedad. En este sentido, los docentes
juegan un papel crucial en la formación de las nuevas generaciones. Es esencial que se fomente el 
aprendizaje y se promueva un ambiente educativo enriquecedor.

En las aulas, los estudiantes tienen la oportunidad de explorar nuevas ideas, conocer diferentes 
culturas y desarrollar habilidades clave para su futuro. La colaboración entre alumnos y maestros 
es esencial para el éxito del proceso educativo.

Además, el uso de tecnologías innovadoras puede mejorar significativamente la experiencia de aprendizaje.
La adaptación a los cambios y la preparación para los desafíos del siglo XXI son aspectos cruciales 
de la educación moderna.

En resumen, la educación es un derecho fundamental y una herramienta poderosa para el progreso 
individual y social.
"""

# Dividir el artículo en palabras
palabras_articulo = re.findall(r'\b\w+\b', articulo)

# Solicitar al usuario que identifique palabras con diptongos y hiatos
palabras_seleccionadas = []
for palabra in palabras_articulo:
    respuesta = input(f"¿La palabra '{palabra}' contiene diptongo (D), hiato (H) o ninguna de las dos (N)? ").lower()

    if respuesta == 'd':
        palabras_seleccionadas.append((palabra, 'diptongo'))
    elif respuesta == 'h':
        palabras_seleccionadas.append((palabra, 'hiato'))

# Mostrar las palabras seleccionadas
print("\nPalabras seleccionadas:")
for palabra, tipo in palabras_seleccionadas:
    print(f"{palabra}: {tipo}")
