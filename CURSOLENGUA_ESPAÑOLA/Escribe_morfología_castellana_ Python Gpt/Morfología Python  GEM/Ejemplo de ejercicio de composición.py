def ejercicio_composicion():
    prefijo = random.choice(["re", "des", "in"])
    raiz = random.choice(["hacer", "decir", "volver"])
    sufijo = random.choice(["-ción", "-miento", "-dor"])
    palabra_compuesta = prefijo + raiz + sufijo

    print(f"Forma una palabra compuesta utilizando '{prefijo}', '{raiz}' y '{sufijo}':")
    respuesta = input()

    if respuesta.lower() == palabra_compuesta.lower():
        print("¡Correcto!")
    else:
        print(f"La palabra compuesta correcta es: {palabra_compuesta}")
