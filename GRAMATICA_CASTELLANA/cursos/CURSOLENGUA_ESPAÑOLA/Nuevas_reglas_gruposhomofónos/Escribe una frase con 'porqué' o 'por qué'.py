def practicar_porque_por_que():
    while True:
        print("Escribe una frase con 'porqué' o 'por qué':")
        frase = input("> ").strip().lower()

        if "porqué" in frase:
            print("¡Correcto! 'Porqué' se refiere a la causa o motivo.")
        elif "por qué" in frase:
            print("¡Excelente! 'Por qué' se utiliza para preguntar o expresar la razón.")
        else:
            print("No es una frase válida. Intenta de nuevo.")

        continuar = input("¿Quieres seguir practicando? (s/n): ").strip().lower()
        if continuar != "s":
            break

    print("¡Gracias por practicar! Espero que hayas aprendido la diferencia entre ambos usos.")

# Ejecutar la función
practicar_porque_por_que()
