import os

def mostrar_teoria():
    print("\n🧠 TEORÍA: Sujeto y Predicado")
    print("""
1. El sujeto es la parte de la oración que indica quién realiza la acción.
2. El predicado es la parte que nos dice qué hace el sujeto.
3. El sujeto puede ser explícito (visible) o implícito (tácito).
4. Toda oración tiene al menos un sujeto y un predicado.
    """)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS:")
    print("1. El perro (sujeto) corre por el parque (predicado).")
    print("2. María (sujeto) escribió un cuento hermoso (predicado).")
    print("3. (Yo) Voy al colegio todos los días. → Sujeto implícito.")

def actividad_crear_cuento():
    print("\n📝 ACTIVIDAD: Escribe un cuento corto")
    cuento = input("Escribe tu cuento aquí:\n")
    print("Ahora identifica los tipos de sujeto y predicado en tu cuento.")
    identificacion = input("Explica brevemente:\n")
    with open("cuento_5to.txt", "w", encoding="utf-8") as f:
        f.write("Cuento:\n" + cuento + "\n\nAnálisis:\n" + identificacion + "\n")
    print("✅ Tu cuento ha sido guardado en 'cuento_5to.txt'.")

def juego_de_roles():
    print("\n🎭 JUEGO DE ROL: Imagina representar esta oración:")
    print("“Salimos de paseo al bosque.”")
    print("Pregunta: ¿Dónde está el sujeto? ¿Está implícito?")
    respuesta = input("Tu respuesta: ")
    print("Gracias por participar. ¡Buen trabajo!\n")

def lectura_comprensiva():
    texto = "Los niños jugaban en el patio mientras la maestra los observaba."
    print("\n📖 LECTURA COMPRENSIVA:")
    print("Texto: " + texto)
    print("Subraya o escribe el sujeto y el predicado:")
    sujeto = input("¿Cuál es el sujeto?: ")
    predicado = input("¿Cuál es el predicado?: ")
    guardar = input("¿Deseas guardar tu respuesta? (s/n): ").lower()
    if guardar == 's':
        with open("respuesta_5to.txt", "w", encoding="utf-8") as f:
            f.write("Sujeto: " + sujeto + "\n")
            f.write("Predicado: " + predicado + "\n")
        print("✅ Respuestas guardadas en 'respuesta_5to.txt'.")
    else:
        print("No se guardaron las respuestas.")

def menu():
    while True:import os

def mostrar_teoria():
    print("\n🧠 TEORÍA: Sujeto y Predicado")
    print("""
1. El sujeto es la parte de la oración que indica quién realiza la acción.
2. El predicado es la parte que nos dice qué hace el sujeto.
3. El sujeto puede ser explícito (visible) o implícito (tácito).
4. Toda oración tiene al menos un sujeto y un predicado.
    """)

def mostrar_ejemplos():
    print("\n📚 EJEMPLOS:")
    print("1. El perro (sujeto) corre por el parque (predicado).")
    print("2. María (sujeto) escribió un cuento hermoso (predicado).")
    print("3. (Yo) Voy al colegio todos los días. → Sujeto implícito.")

def actividad_crear_cuento():
    print("\n📝 ACTIVIDAD: Escribe un cuento corto")
    cuento = input("Escribe tu cuento aquí:\n")
    print("Ahora identifica los tipos de sujeto y predicado en tu cuento.")
    identificacion = input("Explica brevemente:\n")
    with open("cuento_5to.txt", "w", encoding="utf-8") as f:
        f.write("Cuento:\n" + cuento + "\n\nAnálisis:\n" + identificacion + "\n")
    print("✅ Tu cuento ha sido guardado en 'cuento_5to.txt'.")

def juego_de_roles():
    print("\n🎭 JUEGO DE ROL: Imagina representar esta oración:")
    print("“Salimos de paseo al bosque.”")
    print("Pregunta: ¿Dónde está el sujeto? ¿Está implícito?")
    respuesta = input("Tu respuesta: ")
    print("Gracias por participar. ¡Buen trabajo!\n")

def lectura_comprensiva():
    texto = "Los niños jugaban en el patio mientras la maestra los observaba."
    print("\n📖 LECTURA COMPRENSIVA:")
    print("Texto: " + texto)
    print("Subraya o escribe el sujeto y el predicado:")
    sujeto = input("¿Cuál es el sujeto?: ")
    predicado = input("¿Cuál es el predicado?: ")
    guardar = input("¿Deseas guardar tu respuesta? (s/n): ").lower()
    if guardar == 's':
        with open("respuesta_5to.txt", "w", encoding="utf-8") as f:
            f.write("Sujeto: " + sujeto + "\n")
            f.write("Predicado: " + predicado + "\n")
        print("✅ Respuestas guardadas en 'respuesta_5to.txt'.")
    else:
        print("No se guardaron las respuestas.")

def menu():
    while True:
        print("\n📘 MENÚ – LECCIÓN 11 – 5º GRADO")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Crear cuento y analizar sujeto/predicado")
        print("4. Juego de roles con sujeto implícito")
        print("5. Lectura comprensiva y análisis")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            mostrar_ejemplos()
        elif opcion == '3':
            actividad_crear_cuento()
        elif opcion == '4':
            juego_de_roles()
        elif opcion == '5':
            lectura_comprensiva()
        elif opcion == '6':
            print("👋 ¡Gracias por participar en la lección!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()

        print("\n📘 MENÚ – LECCIÓN 11 – 5º GRADO")
        print("1. Ver teoría")
        print("2. Ver ejemplos")
        print("3. Crear cuento y analizar sujeto/predicado")
        print("4. Juego de roles con sujeto implícito")
        print("5. Lectura comprensiva y análisis")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            mostrar_ejemplos()
        elif opcion == '3':
            actividad_crear_cuento()
        elif opcion == '4':
            juego_de_roles()
        elif opcion == '5':
            lectura_comprensiva()
        elif opcion == '6':
            print("👋 ¡Gracias por participar en la lección!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
