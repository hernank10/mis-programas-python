def escribir_ensayo(palabras, categoria):
    print(f"\nEscribiendo un ensayo para la categoría {categoria}:")
    print("\n📌 Consejo: Usa al menos 5 palabras que hayas aprendido de esta categoría.")
    ensayo = input("Escribe un pequeño ensayo usando algunas de las palabras aprendidas: ")
    print("\nGracias por tu ensayo. Aquí está lo que escribiste:")
    print(ensayo)

    ver_ejemplo = input("\n¿Quieres ver un ejemplo de ensayo? (sí/no): ").strip().lower()
    if ver_ejemplo == "sí":
        if categoria == "Sinónimos":
            ejemplo = (
                "\nEjemplo de ensayo con sinónimos:\n\n"
                "En mi casa siempre me siento alegre y contento cuando todos están reunidos. "
                "El ambiente es bello y hermoso, especialmente cuando mi madre prepara una comida "
                "rápida pero veloz para todos. Aunque a veces la tarea de matemáticas es difícil, "
                "intento no frustrarme y encontrar un método más complicado para resolverla. "
                "Siempre que tengo dudas, mi hermano mayor me enseña y me instruye con paciencia."
            )
            print(ejemplo)
        else:
            print("Pronto habrá un ejemplo para esta categoría.")
