palabras_ortografia = ["canción", "lápiz", "árbol", "camión"]
# Agregar una nueva palabra
palabras_ortografia.append("corazón")
# Ordenar las palabras alfabéticamente
palabras_ortografia.sort()

#Un programa que necesita analizar textos y extraer un conjunto único de palabras clave puede beneficiar a los conjuntos
palabras_texto = {"libro", "escuela", "maestro", "libro", "estudiante"}
palabras_unicas = set(palabras_texto)
# Salida: {'libro', 'escuela', 'maestro', 'estudiante'}

# Acceder a la definición
diccionario_definiciones = {
    "morfofonología": "Estudio de las interacciones entre los sistemas fonológico y morfológico.",
    "lexema": "Unidad mínima de significado léxico.",
    "sílaba": "Unidad de pronunciación de una palabra."
}
# Acceder a la definición
print(diccionario_definiciones["lexema"])  # Salida: Unidad mínima de significado léxico.

respuestas_correctas = ("a", "b", "c", "d")
# Intentar modificar una tupla causará un error
# respuestas_correctas[0] = "e"  # Error: las tuplas son inmutables
