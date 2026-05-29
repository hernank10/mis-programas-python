import random

# Función para guardar el progreso en un archivo
def guardar_progreso(ejercicio, resultado):
    with open("progreso.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{ejercicio}: {resultado}\n")

# 1. Concordancia verbal
def concordancia_verbal():
    ejercicios = [
        ("Él ___ temprano a la escuela. (llegar)", "llega"),
        ("Nosotros ___ la tarea. (hacer)", "hacemos"),
        ("Tú ___ muy bien en ajedrez. (jugar)", "juegas"),
        ("Ellos ___ en la competencia. (participar)", "participan")
    ]
    oracion, respuesta_correcta = random.choice(ejercicios)

    print(f"\n🔹 Oración: {oracion}")
    respuesta_usuario = input("✍️ Escribe el verbo correcto: ").strip()

    if respuesta_usuario.lower() == respuesta_correcta:
        print("✅ ¡Correcto!")
        guardar_progreso("Concordancia Verbal", "Correcto")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        guardar_progreso("Concordancia Verbal", "Incorrecto")

# 2. Uso de conectores
def uso_de_conectores():
    ejercicios = [
        ("Quería ir a la fiesta, ___ tenía que estudiar.", "pero"),
        ("No tenía hambre, ___ no comí.", "por eso"),
        ("Hace frío, ___ me puse abrigo.", "por lo tanto"),
        ("Juan no vino, ___ estaba enfermo.", "porque")
    ]
    oracion, respuesta_correcta = random.choice(ejercicios)

    print(f"\n🔹 Oración: {oracion}")
    respuesta_usuario = input("✍️ Escribe el conector correcto: ").strip()

    if respuesta_usuario.lower() == respuesta_correcta:
        print("✅ ¡Correcto!")
        guardar_progreso("Uso de Conectores", "Correcto")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        guardar_progreso("Uso de Conectores", "Incorrecto")

# 3. Reconocimiento de sustantivos
def reconocimiento_sustantivos():
    palabras = [
        ("sol", "sustantivo"),
        ("azul", "no"),
        ("perro", "sustantivo"),
        ("rápido", "no"),
        ("mesa", "sustantivo")
    ]
    palabra, respuesta_correcta = random.choice(palabras)

    print(f"\n🔹 ¿La palabra '{palabra}' es un sustantivo? (sustantivo/no)")
    respuesta_usuario = input("✍️ Responde: ").strip().lower()

    if respuesta_usuario == respuesta_correcta:
        print("✅ ¡Correcto!")
        guardar_progreso("Reconocimiento de Sustantivos", "Correcto")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        guardar_progreso("Reconocimiento de Sustantivos", "Incorrecto")

# 4. Corrección de errores gramaticales
def correccion_errores():
    ejercicios = [
        ("Nosotros está feliz.", "Nosotros estamos felices."),
        ("Ella juegan en el parque.", "Ella juega en el parque."),
        ("Yo comer pizza ayer.", "Yo comí pizza ayer."),
        ("Ellos va a la escuela.", "Ellos van a la escuela.")
    ]
    oracion_erronea, respuesta_correcta = random.choice(ejercicios)

    print(f"\n🔹 Corrige la siguiente oración:\n{oracion_erronea}")
    respuesta_usuario = input("✍️ Escribe la corrección: ").strip()

    if respuesta_usuario.lower() == respuesta_correcta.lower():
        print("✅ ¡Correcto!")
        guardar_progreso("Corrección de Errores", "Correcto")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        guardar_progreso("Corrección de Errores", "Incorrecto")

# 5. Transformación de oraciones
def transformar_oraciones():
    ejercicios = [
        ("Yo corro en el parque. (pasado)", "Yo corrí en el parque."),
        ("Nosotros viajamos a Colombia. (futuro)", "Nosotros viajaremos a España."),
        ("Él estudia para el examen. (pasado)", "Él estudió para el examen."),
        ("Tú comes pizza. (futuro)", "Tú comerás pizza.")
    ]
    oracion, respuesta_correcta = random.choice(ejercicios)

    print(f"\n🔹 Transforma la oración:\n{oracion}")
    respuesta_usuario = input("✍️ Escribe la transformación: ").strip()

    if respuesta_usuario.lower() == respuesta_correcta.lower():
        print("✅ ¡Correcto!")
        guardar_progreso("Transformación de Oraciones", "Correcto")
    else:
        print(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
        guardar_progreso("Transformación de Oraciones", "Incorrecto")

# Función del menú
def menu():
    while True:
        print("\n📚 **Juegos de Gramática Castellana** 📚")
        print("1. Concordancia verbal")
        print("2. Uso de conectores")
        print("3. Reconocimiento de sustantivos")
        print("4. Corrección de errores gramaticales")
        print("5. Transformación de oraciones")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            concordancia_verbal()
        elif opcion == "2":
            uso_de_conectores()
        elif opcion == "3":
            reconocimiento_sustantivos()
        elif opcion == "4":
            correccion_errores()
        elif opcion == "5":
            transformar_oraciones()
        elif opcion == "6":
            print("¡Gracias por jugar! 📝")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
