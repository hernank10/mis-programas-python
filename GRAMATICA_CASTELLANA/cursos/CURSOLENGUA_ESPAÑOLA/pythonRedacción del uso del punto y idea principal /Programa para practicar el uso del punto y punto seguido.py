# Programa para practicar el uso del punto y punto seguido

# Reglas sobre el uso del punto y punto seguido
reglas = """
La función del punto es marcar que el sentido gramatical y lógico de un periodo ha llegado a su fin. 
De ahí que el punto y seguido refleje proximidad entre dos pensamientos que, si bien no están enlazados 
de manera íntima como lo indicaría el punto y coma, son bastante cercanos entre sí. En cambio, el punto y 
aparte expresa que el discurso ha cambiado de dirección, ya sea porque el tratamiento de cierta idea ha concluido, 
o bien porque el ángulo o perspectiva con que se abordará es distinto.

Desde el enfoque gramatical, el punto debe colocarse:
1. Para indicar que ha concluido una oración, un párrafo o un texto.
2. Después de toda abreviatura.
3. Después de " " (comillas) siempre y cuando no vaya una coma. (Para la colocación correcta del punto antes o después de comillas, consulta el capítulo 9.)
ATENCIÓN: Después de los signos de interrogación y admiración jamás debe ponerse punto.

Veamos un ejemplo de ERROR: estás seguro de que quieres ir a Colombia?. El punto después de una interrogación es ocioso: tanto el signo de cierre de interrogación como el de admiración señalan el fin del enunciado.
"""

# Mostrar las reglas al usuario
print("Reglas sobre el uso del punto y punto seguido:\n")
print(reglas)

# Solicitar al usuario que escriba ejemplos de oraciones utilizando las reglas
print("\nEscribe un ejemplo de oración utilizando cada una de las siguientes reglas:")

ejemplos = {}
reglas_pedidas = [
    "Indicar que ha concluido una oración, un párrafo o un texto.",
    "Después de toda abreviatura.",
    'Después de " " (comillas) siempre y cuando no vaya una coma.',
    "Después de los signos de interrogación y admiración jamás debe ponerse punto."
]

for i, regla in enumerate(reglas_pedidas):
    ejemplos[i] = input(f"{i+1}. {regla}\nEjemplo: ")

# Solicitar al usuario que escriba abreviaturas de 5 países
print("\nPor favor, escribe las abreviaturas de los siguientes 5 países (utilizando las abreviaturas oficiales de la RAE):")

paises = ["Argentina", "España", "Venezuela", "Países Bajos", "Puerto Rico"]
abrev_paises = {}

for pais in paises:
    abrev_paises[pais] = input(f"{pais}: ")

# Solicitar al usuario que escriba nombres de 3 personas
print("\nEscribe nombres de 3 personas:")
personas = []

for i in range(3):
    persona = input(f"Persona {i+1}: ")
    personas.append(persona)

# Solicitar al usuario que escriba 2 nombres de oficinas internacionales de comercio, cultura y gobierno
print("\nEscribe 2 nombres de oficinas internacionales de comercio, cultura y gobierno:")
oficinas = []

for i in range(2):
    oficina = input(f"Oficina {i+1}: ")
    oficinas.append(oficina)

# Mostrar los resultados ingresados por el usuario
print("\nResultados ingresados:")

print("Ejemplos de uso del punto:")
for i, ejemplo in ejemplos.items():
    print(f"Regla {i+1}: {regla}\nEjemplo: {ejemplo}")

print("\nAbreviaturas de países:")
for pais, abrev in abrev_paises.items():
    print(f"{pais}: {abrev}")

print("\nNombres de personas:")
for persona in personas:
    print(persona)

print("\nOficinas internacionales de comercio, cultura y gobierno:")
for oficina in oficinas:
    print(oficina)
