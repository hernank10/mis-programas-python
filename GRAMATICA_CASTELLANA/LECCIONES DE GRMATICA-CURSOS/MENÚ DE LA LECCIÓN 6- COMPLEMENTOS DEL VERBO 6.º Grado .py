import time
import random
import sys

def limpiar_consola():
    """Simula la limpieza de la consola (funciona mejor en entornos de terminal)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar(mensaje="Presiona Enter para continuar...", limpiar=False):
    """Pausa la ejecución para que el usuario pueda leer."""
    input(f"\n{mensaje}")
    if limpiar:
        limpiar_consola()

def mostrar_teoria():
    limpiar_consola()
    print("📚 **TEORÍA: COMPLEMENTOS DEL VERBO (OBJETO DIRECTO E INDIRECTO)** 📚")
    print("---")
    
    print("\n1. **Recordando el Verbo: El Corazón del Predicado**")
    print("   Ya sabes que el **verbo** es la palabra más importante en el predicado, ¡es la acción!")
    print("   - Ej: Mi hermano **compra** un libro.")
    print("   El verbo nos cuenta qué hace el sujeto.")
    esperar()

    print("\n2. **Los Complementos del Verbo: ¡Los Ayudantes!**")
    print("   A veces, el verbo necesita otras palabras para que la oración se entienda mejor. Esas palabras se llaman **complementos del verbo**.")
    print("   Nos dan más información sobre la acción del verbo. Hoy veremos dos muy importantes: el Objeto Directo y el Objeto Indirecto.")
    esperar()

    print("\n3. **El Objeto Directo (OD): ¿Qué o Quién Recibe la Acción?**")
    print("   El **Objeto Directo (OD)** es la parte que **recibe la acción del verbo directamente**.")
    print("   Para encontrarlo, puedes hacer dos preguntas al verbo:")
    print("   - **¿Qué?** + verbo + sujeto?")
    print("   - **¿A quién?** + verbo + sujeto? (si es una persona o animal)")
    print("   También puedes probar si puedes reemplazar el OD por los pronombres: **lo, la, los, las**.")
    print("   - Ej: 'El niño **come una manzana**.'")
    print("     - ¿Qué come el niño? → una manzana (OD)")
    print("     - El niño **la** come. (Funciona con 'la')")
    esperar()

    print("\n4. **El Objeto Indirecto (OI): ¿A Quién o Para Quién es la Acción?**")
    print("   El **Objeto Indirecto (OI)** es la parte que nos dice **a quién o para quién va destinada la acción** (o el objeto directo).")
    print("   Para encontrarlo, puedes hacer estas preguntas al verbo (o al verbo + OD):")
    print("   - **¿A quién?** + verbo + OD + sujeto?")
    print("   - **¿Para quién?** + verbo + OD + sujeto?")
    print("   El OI casi siempre empieza con las preposiciones **'a'** o **'para'**.")
    print("   También puedes probar si puedes reemplazar el OI por los pronombres: **le, les**.")
    print("   - Ej: 'Ella **dio un regalo a su mamá**.'")
    print("     - ¿Qué dio ella? → un regalo (OD)")
    print("     - ¿A quién dio un regalo? → a su mamá (OI)")
    print("     - Ella **le** dio un regalo. (Funciona con 'le')")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: VERBO, OBJETO DIRECTO Y OBJETO INDIRECTO** 💡")
    print("---")

    print("\n**Ejemplo 1:** 'Mi abuela compra flores.'")
    print(" - **Verbo:** compra")
    print(" - **OD:** flores (¿Qué compra mi abuela?)")
    print(" - **Prueba:** Mi abuela **las** compra.")
    esperar()

    print("\n**Ejemplo 2:** 'El cartero entregó una carta al vecino.'")
    print(" - **Verbo:** entregó")
    print(" - **OD:** una carta (¿Qué entregó el cartero?)")
    print(" - **OI:** al vecino (¿A quién entregó una carta el cartero?)")
    print(" - **Prueba OD:** El cartero **la** entregó al vecino.")
    print(" - **Prueba OI:** El cartero **le** entregó una carta.")
    esperar()

    print("\n**Ejemplo 3:** 'La profesora enseña matemáticas a los alumnos.'")
    print(" - **Verbo:** enseña")
    print(" - **OD:** matemáticas (¿Qué enseña la profesora?)")
    print(" - **OI:** a los alumnos (¿A quiénes enseña matemáticas la profesora?)")
    print(" - **Prueba OD:** La profesora **las** enseña a los alumnos.")
    print(" - **Prueba OI:** La profesora **les** enseña matemáticas.")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡ENCONTRANDO LOS COMPLEMENTOS!** 📝")
    print("---")
    print("¡Lee cada oración, identifica el verbo y luego el Objeto Directo (OD) y el Objeto Indirecto (OI)!")
    esperar("¡Empecemos!")

    ejercicios = [
        # Identificar OD (10 ejercicios)
        {"tipo": "od", "oracion": "El niño lee un libro.", "verbo": "lee", "respuesta_od": "un libro", "feedback_od": "Pregunta: ¿Qué lee el niño?"},
        {"tipo": "od", "oracion": "Mi mamá prepara la cena.", "verbo": "prepara", "respuesta_od": "la cena", "feedback_od": "Pregunta: ¿Qué prepara mi mamá?"},
        {"tipo": "od", "oracion": "Los estudiantes escuchan al profesor.", "verbo": "escuchan", "respuesta_od": "al profesor", "feedback_od": "Pregunta: ¿A quién escuchan los estudiantes? (¡Ojo! 'a' es preposición, pero es un OD de persona)"},
        {"tipo": "od", "oracion": "Yo escribo un cuento.", "verbo": "escribo", "respuesta_od": "un cuento", "feedback_od": "Pregunta: ¿Qué escribo yo?"},
        {"tipo": "od", "oracion": "El perro persigue la pelota.", "verbo": "persigue", "respuesta_od": "la pelota", "feedback_od": "Pregunta: ¿Qué persigue el perro?"},
        {"tipo": "od", "oracion": "Ella compra zapatos.", "verbo": "compra", "respuesta_od": "zapatos", "feedback_od": "Pregunta: ¿Qué compra ella?"},
        {"tipo": "od", "oracion": "Nosotros visitamos el museo.", "verbo": "visitamos", "respuesta_od": "el museo", "feedback_od": "Pregunta: ¿Qué visitamos nosotros?"},
        {"tipo": "od", "oracion": "Mi tío arregla el coche.", "verbo": "arregla", "respuesta_od": "el coche", "feedback_od": "Pregunta: ¿Qué arregla mi tío?"},
        {"tipo": "od", "oracion": "Ustedes estudian la lección.", "verbo": "estudian", "respuesta_od": "la lección", "feedback_od": "Pregunta: ¿Qué estudian ustedes?"},
        {"tipo": "od", "oracion": "Los pájaros construyen nidos.", "verbo": "construyen", "respuesta_od": "nidos", "feedback_od": "Pregunta: ¿Qué construyen los pájaros?"},

        # Identificar OI (10 ejercicios)
        {"tipo": "oi", "oracion": "El profesor explica la tarea a los alumnos.", "verbo": "explica", "od_existente": "la tarea", "respuesta_oi": "a los alumnos", "feedback_oi": "Pregunta: ¿A quién explica la tarea el profesor?"},
        {"tipo": "oi", "oracion": "Mi abuela dio un regalo a su nieta.", "verbo": "dio", "od_existente": "un regalo", "respuesta_oi": "a su nieta", "feedback_oi": "Pregunta: ¿A quién dio un regalo mi abuela?"},
        {"tipo": "oi", "oracion": "Compré flores para mi mamá.", "verbo": "compré", "od_existente": "flores", "respuesta_oi": "para mi mamá", "feedback_oi": "Pregunta: ¿Para quién compré flores?"},
        {"tipo": "oi", "oracion": "Leí un cuento a mi hermano.", "verbo": "leí", "od_existente": "un cuento", "respuesta_oi": "a mi hermano", "feedback_oi": "Pregunta: ¿A quién leí un cuento?"},
        {"tipo": "oi", "oracion": "Ella escribe una carta para su amiga.", "verbo": "escribe", "od_existente": "una carta", "respuesta_oi": "para su amiga", "feedback_oi": "Pregunta: ¿Para quién escribe una carta ella?"},
        {"tipo": "oi", "oracion": "Daremos un premio al ganador.", "verbo": "daremos", "od_existente": "un premio", "respuesta_oi": "al ganador", "feedback_oi": "Pregunta: ¿A quién daremos un premio?"},
        {"tipo": "oi", "oracion": "El camarero sirvió la comida a los clientes.", "verbo": "sirvió", "od_existente": "la comida", "respuesta_oi": "a los clientes", "feedback_oi": "Pregunta: ¿A quiénes sirvió la comida el camarero?"},
        {"tipo": "oi", "oracion": "Preparamos una sorpresa para papá.", "verbo": "preparamos", "od_existente": "una sorpresa", "respuesta_oi": "para papá", "feedback_oi": "Pregunta: ¿Para quién preparamos una sorpresa?"},
        {"tipo": "oi", "oracion": "El médico recetó un medicamento al paciente.", "verbo": "recetó", "od_existente": "un medicamento", "respuesta_oi": "al paciente", "feedback_oi": "Pregunta: ¿A quién recetó un medicamento el médico?"},
        {"tipo": "oi", "oracion": "Contaron una historia a los niños.", "verbo": "contaron", "od_existente": "una historia", "respuesta_oi": "a los niños", "feedback_oi": "Pregunta: ¿A quiénes contaron una historia?"},
    ]

    puntuacion = 0
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ejercicio in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        print(f"Oración: '{ejercicio['oracion']}'")
        print(f"Verbo: '{ejercicio['verbo']}'")

        if ejercicio["tipo"] == "od":
            respuesta_usuario = input("Escribe el OBJETO DIRECTO (OD): ").strip().lower()
            if respuesta_usuario == ejercicio['respuesta_od'].lower():
                print("✅ ¡Correcto! ¡Ese es el Objeto Directo!")
                puntuacion += 1
            else:
                print(f"❌ ¡Intenta de nuevo!")
                print(f"El OD correcto es: '{ejercicio['respuesta_od']}'.")
                print(f"Pista: {ejercicio['feedback_od']}")
        elif ejercicio["tipo"] == "oi":
            print(f"Objeto Directo (OD): '{ejercicio['od_existente']}'")
            respuesta_usuario = input("Escribe el OBJETO INDIRECTO (OI): ").strip().lower()
            if respuesta_usuario == ejercicio['respuesta_oi'].lower():
                print("✅ ¡Excelente! ¡Ese es el Objeto Indirecto!")
                puntuacion += 1
            else:
                print(f"❌ ¡Puedes mejorar!")
                print(f"El OI correcto es: '{ejercicio['respuesta_oi']}'.")
                print(f"Pista: {ejercicio['feedback_oi']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Felicidades! ¡Eres un gran detective de complementos verbales!")
    elif puntuacion >= 10:
        print("👍 ¡Buen trabajo! Estás aprendiendo mucho sobre cómo se conectan las palabras.")
    else:
        print("✍️ ¡Sigue practicando! Con más esfuerzo, ¡dominarás los complementos del verbo!")
    esperar(limpiar=True)

def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIAS ORACIONES CON OBJETOS DIRECTOS E INDIRECTOS!** ✍️")
    print("---")
    print("¡Vamos a inventar 20 oraciones e identificar sus complementos!")
    print("Intenta incluir un OD y, si puedes, también un OI en tus oraciones.")
    esperar("¡Manos a la obra!")

    ejemplos_propios = []
    
    for i in range(20):
        print(f"\n--- Tu Oración {i+1}/20 ---")
        oracion = input("Escribe una oración (ej: Mi amigo compró un libro para su hermana.): ").strip()
        
        print(f"\nAnaliza el predicado de tu oración: '{oracion}'")
        verbo_propuesto = input("1. Escribe el VERBO: ").strip()
        od_propuesto = input("2. Escribe el OBJETO DIRECTO (OD) (si lo hay, si no, deja vacío): ").strip()
        oi_propuesto = input("3. Escribe el OBJETO INDIRECTO (OI) (si lo hay, si no, deja vacío): ").strip()

        ejemplos_propios.append(f"{i+1}. Oración: '{oracion}'\n   Verbo: '{verbo_propuesto}'\n   OD: '{od_propuesto if od_propuesto else 'N/A'}'\n   OI: '{oi_propuesto if oi_propuesto else 'N/A'}'\n")
        print("¡Ejemplo guardado!")

    limpiar_consola()
    print("--- ¡TUS ORACIONES Y SUS COMPLEMENTOS ANALIZADOS! ---")
    print("\nAquí están tus 20 oraciones con sus complementos:")
    for ejemplo in ejemplos_propios:
        print(ejemplo)
    print("\n¡Excelente trabajo creando y analizando oraciones con complementos!")
    esperar(limpiar=True)


def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: COMPLEMENTOS DEL VERBO (6.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos sobre los ayudantes del verbo!)")
        print("2. Ejemplos (¡Vemos el OD y OI en acción!)")
        print("3. Ejercicios (¡A encontrar los complementos!)")
        print("4. Crear Mis Propias Oraciones (¡Inventa y analiza tus frases!)")
        print("5. Salir")
        print("---")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            mostrar_ejemplos()
        elif opcion == '3':
            realizar_ejercicios()
        elif opcion == '4':
            crear_ejemplos_propios()
        elif opcion == '5':
            print("\n¡Gracias por aprender sobre los complementos del verbo! ¡Sigue construyendo oraciones increíbles!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
