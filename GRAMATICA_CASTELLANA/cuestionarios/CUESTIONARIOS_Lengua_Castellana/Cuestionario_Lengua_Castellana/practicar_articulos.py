def practicar_articulos():
    ejercicios = [
        {"frase": "___ perro está ladrando en el jardín. (español)", "respuesta": "El"},
        {"frase": "She found ___ apple on the table. (inglés)", "respuesta": "an"},
        {"frase": "___ chicas están jugando en el parque. (español)", "respuesta": "Las"},
        {"frase": "I saw ___ bird flying in the sky. (inglés)", "respuesta": "a"},
        {"frase": "___ agua en el vaso está fría. (español)", "respuesta": "El"},
        {"frase": "___ orange is on the counter. (inglés)", "respuesta": "The"},
        {"frase": "___ niños están en la escuela. (español)", "respuesta": "Los"},
        {"frase": "They brought ___ cake to the party. (inglés)", "respuesta": "a"},
        {"frase": "___ problema es más complicado de lo que parece. (español)", "respuesta": "El"},
        {"frase": "She opened ___ book and started reading. (inglés)", "respuesta": "the"},
    ]

    print("¡Bienvenido al programa de práctica de artículos en español e inglés!")
    print("Completa las siguientes frases con el artículo correcto.\n")

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios):
        print(f"Frase {i+1}: {ejercicio['frase']}")
        respuesta_usuario = input("Escribe el artículo correcto: ").strip()

        if respuesta_usuario.lower() == ejercicio["respuesta"].lower():
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{ejercicio['respuesta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("¡Excelente trabajo! ¡Has acertado todas las respuestas!")
    elif puntaje >= len(ejercicios) * 0.7:
        print("¡Buen trabajo! Aún puedes mejorar.")
    else:
        print("Sigue practicando, ¡puedes hacerlo mejor!")

# Ejecutar el programa
practicar_articulos()
