def ejercicio_traduccion(idioma, datos):
    print(f"=== Aprende {idioma.capitalize()} ===\n")
    aciertos = 0
    for i, frase in enumerate(datos, start=1):
        print(f"Frase {i}: {frase['frase']}")
        respuesta = input("Traduce al español: ")
        if respuesta.strip().lower() == frase["traducción"].strip().lower():
            print("¡Correcto!\n")
            aciertos += 1
        else:
            print(f"Incorrecto. La respuesta es: {frase['traducción']}\n")
    print(f"¡Has completado el ejercicio con {aciertos}/{len(datos)} aciertos!")
