import re

def identificar_diptongos(palabra):
    # Definir patrón de diptongos utilizando expresiones regulares
    patron_diptongo = re.compile(r'[aeiouáéíóúü]+[aeiouáéíóúü]+', re.IGNORECASE)

    # Buscar coincidencias en la palabra
    coincidencias = re.findall(patron_diptongo, palabra)

    # Devolver True si hay diptongos, False en caso contrario
    return len(coincidencias) > 0

# Presentar un poema
poema = """
En la tranquila tarde de verano,
el sol se oculta tras las montañas.
Las aves cantan melodías celestiales,
mientras el viento susurra secretos antiguos.
"""

print("¡Bienvenido al desafío de identificación de diptongos!")
print("Lee el siguiente poema y escribe palabras que contengan diptongos.")

# Solicitar al usuario que identifique palabras con diptongos
palabras_con_diptongos = []
for i in range(5):  # Puedes ajustar el número según tus necesidades
    palabra = input(f"Ingrese la palabra con diptongo #{i + 1}: ")
    palabras_con_diptongos.append(palabra)

# Verificar y mostrar resultado
print("\nResultado:")
for palabra in palabras_con_diptongos:
    if identificar_diptongos(palabra):
        print(f"{palabra}: Contiene diptongo")
    else:
        print(f"{palabra}: No contiene diptongo")
