import random

# Teoría sobre prefijos categorizadores
teoria = """
En español, se considera que los prefijos no cambian la categoría gramatical de la base. 
Sin embargo, algunos prefijos como 'poli-' y 'multi-' pueden convertir sustantivos en adjetivos. 
Ejemplos:
- 'sílaba' (sustantivo) → 'polisílabo' (adjetivo)
- 'color' (sustantivo) → 'multicolor' (adjetivo)
"""

def ocultar_letras(palabra, num_ocultas=2):
    """Oculta aleatoriamente algunas letras de la palabra con guiones bajos."""
    indices = random.sample(range(len(palabra)), num_ocultas)
    palabra_oculta = list(palabra)
    for i in indices:
        palabra_oculta[i] = '_'
    return ''.join(palabra_oculta)

def completar_oraciones():
    """Ejercicios de completación de oraciones con palabras derivadas por prefijación."""
    oraciones = [
        ("El edificio tiene una estructura __________ resistente.", "multidimensional"),
        ("El texto contiene palabras __________, lo que facilita su pronunciación.", "polisílabas"),
        ("El equipo es __________ y puede adaptarse a cualquier función.", "multifuncional"),
        ("Los deportistas entrenan en un centro __________.", "polideportivo"),
        ("Esa empresa tiene presencia __________ en muchos países.", "multinacional")
    ]
    
    for oracion, respuesta in oraciones:
        print(oracion)
        intento = input("Completa la oración: ").strip().lower()
        if intento == respuesta:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era: {respuesta}")
        print()

def redaccion_ejemplos():
    """Permite al usuario escribir y guardar ejemplos de palabras con prefijos categorizadores."""
    ejemplos = []
    print("Escribe ejemplos de palabras con 'poli-' o 'multi-'. Puedes guardar hasta 100 ejemplos.")
    while len(ejemplos) < 100:
        palabra = input("Escribe una palabra (o 'salir' para terminar): ").strip().lower()
        if palabra == "salir":
            break
        ejemplos.append(palabra)
        print("Ejemplo guardado.")
    print("Ejemplos guardados:", ejemplos)

def juego_practica():
    palabras = [
        "polisílabo", "policromático", "polifacético", "politécnico", "poligonal", "polimórfico", "polilingüe", "polimétrico", "polifónico", "polivalente",
        "políglota", "polimolecular", "politonal", "polideportivo", "poliestratégico", "politético", "polidimensional", "polineuronal", "polifuncional", "polimaterial",
        "policéfalo", "poligrafía", "polimérico", "multicolor", "multiforme", "multilingüe", "multilateral", "multimodal", "multinacional", "multirracial", "multiorgánico",
        "multigrado", "multipropósito", "multimillonario", "multirregional", "multiescalar", "multifacético", "multiconsciente", "multitemático", "multidimensional", "multivariado",
        "multigeneracional", "multilateralista", "multitarea", "multifunción", "multiangular", "multicausal", "multimotor"
    ]
    
    palabra = random.choice(palabras)
    palabra_oculta = ocultar_letras(palabra)
    
    print("Escribe la palabra correctamente completando las letras ocultas:")
    print(palabra_oculta)
    
    intento = input("Tu respuesta: ").strip().lower()
    
    if intento == palabra:
        print("¡Correcto! Has escrito la palabra correctamente.")
    else:
        print(f"Incorrecto. La respuesta correcta era: {palabra}")

if __name__ == "__main__":
    print("Bienvenido al programa sobre prefijos categorizadores.")
    print(teoria)
    
    while True:
        print("\nOpciones:")
        print("1. Practicar escritura de palabras con prefijos")
        print("2. Completar oraciones con palabras derivadas")
        print("3. Escribir y guardar ejemplos de palabras")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            juego_practica()
        elif opcion == "2":
            completar_oraciones()
        elif opcion == "3":
            redaccion_ejemplos()
        elif opcion == "4":
            print("¡Gracias por participar!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
