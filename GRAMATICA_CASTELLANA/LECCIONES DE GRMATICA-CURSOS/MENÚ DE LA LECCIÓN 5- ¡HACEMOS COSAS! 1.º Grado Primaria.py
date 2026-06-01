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
    print("📚 **TEORÍA: ¡HACEMOS COSAS! VERBOS Y ORACIONES SIMPLES** 📚")
    print("---")
    
    print("\n1. **¿Qué son los Verbos? ¡Palabras de Acción!**")
    print("   Los **verbos** son palabras que nos dicen qué hacen las personas, los animales o las cosas.")
    print("   ¡Son las palabras de las **acciones**!")
    print("   - Ejemplos de verbos: **comer**, **jugar**, **dormir**, **correr**, **leer**, **saltar**.")
    print("   Piensa en algo que puedas hacer... ¡esa es una acción, un verbo!")
    esperar()

    print("\n2. **¡Sí, lo hago! Oraciones Afirmativas**")
    print("   Cuando queremos decir que algo **SÍ** está pasando, o que alguien **SÍ** hace algo, usamos una **oración afirmativa**.")
    print("   - Ej: 'El perro **corre**.' (Sí, el perro corre.)")
    print("   - Ej: 'La niña **come**.' (Sí, la niña come.)")
    print("   ¡Son oraciones que nos dicen lo que **SÍ** pasa!")
    esperar()

    print("\n3. **¡No, no lo hago! Oraciones Negativas**")
    print("   Cuando queremos decir que algo **NO** está pasando, o que alguien **NO** hace algo, usamos una **oración negativa**.")
    print("   ¡Para eso, usamos la palabra mágica **NO** antes del verbo!")
    print("   - Ej: 'El perro **NO salta**.' (El perro no está saltando.)")
    print("   - Ej: 'La niña **NO duerme**.' (La niña no está durmiendo.)")
    print("   ¡Son oraciones que nos dicen lo que **NO** pasa!")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS DE ORACIONES** 💡")
    print("---")

    print("\n**Verbos:**")
    print(" - ¿Qué hace el pato? El pato **nada**.")
    print(" - ¿Qué hace la abeja? La abeja **vuela**.")
    print(" - ¿Qué hace el bebé? El bebé **llora**.")
    esperar()

    print("\n**Oraciones Afirmativas (Sí lo hace):**")
    print(" - 'El gato **juega** con la pelota.'")
    print(" - 'La maestra **escribe** en la pizarra.'")
    print(" - 'Yo **dibujo** un sol.'")
    esperar()

    print("\n**Oraciones Negativas (No lo hace):**")
    print(" - 'El perro **NO canta**.'")
    print(" - 'Papá **NO salta** muy alto.'")
    print(" - 'Nosotros **NO comemos** piedras.'")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡PRACTICANDO LAS ACCIONES!** 📝")
    print("---")
    print("¡Vamos a ver si lo aprendimos bien! Responde con 'afirmativa' o 'negativa', o escribe la palabra que falta.")
    esperar("¡Empecemos!")

    ejercicios = [
        # Identificar Verbos (5 ejercicios)
        {"tipo": "verbo", "consigna": "¿Cuál es la palabra de acción (verbo) en: 'El niño **corre** muy rápido'?", "respuesta": "corre", "feedback": "El verbo nos dice qué hace el niño."},
        {"tipo": "verbo", "consigna": "¿Cuál es la palabra de acción (verbo) en: 'Mi hermana **lee** un libro'?", "respuesta": "lee", "feedback": "La acción que hace la hermana."},
        {"tipo": "verbo", "consigna": "¿Cuál es la palabra de acción (verbo) en: 'Los pájaros **cantan** bonito'?", "respuesta": "cantan", "feedback": "Lo que hacen los pájaros."},
        {"tipo": "verbo", "consigna": "¿Cuál es la palabra de acción (verbo) en: 'Tú **duermes** en tu cama'?", "respuesta": "duermes", "feedback": "La acción que tú haces."},
        {"tipo": "verbo", "consigna": "¿Cuál es la palabra de acción (verbo) en: 'El pez **nada** en el agua'?", "respuesta": "nada", "feedback": "Lo que hace el pez."},

        # Afirmativas/Negativas - Identificar (5 ejercicios)
        {"tipo": "oracion_identificar", "consigna": "¿Qué tipo de oración es: 'El sol **brilla**.'? (afirmativa/negativa)", "respuesta": "afirmativa", "feedback": "No usa la palabra 'no'."},
        {"tipo": "oracion_identificar", "consigna": "¿Qué tipo de oración es: 'La luna **NO** tiene luz propia.'? (afirmativa/negativa)", "respuesta": "negativa", "feedback": "Usa la palabra 'no'."},
        {"tipo": "oracion_identificar", "consigna": "¿Qué tipo de oración es: 'Los perros **NO vuelan**.'? (afirmativa/negativa)", "respuesta": "negativa", "feedback": "Usa la palabra 'no'."},
        {"tipo": "oracion_identificar", "consigna": "¿Qué tipo de oración es: 'Las flores **crecen** en el jardín.'? (afirmativa/negativa)", "respuesta": "afirmativa", "feedback": "No usa la palabra 'no'."},
        {"tipo": "oracion_identificar", "consigna": "¿Qué tipo de oración es: 'Yo **NO quiero** dulces.'? (afirmativa/negativa)", "respuesta": "negativa", "feedback": "Usa la palabra 'no'."},

        # Completar (5 ejercicios)
        {"tipo": "completar", "consigna": "Completa con 'NO' para que sea negativa: 'El gato ____ ____ agua.'", "respuesta": "no bebe", "feedback": "Recuerda la palabra mágica para negar."},
        {"tipo": "completar", "consigna": "Completa con un verbo de acción: 'El conejo ____ una zanahoria.'", "respuesta": "come", "otras_respuestas": ["muerde"], "feedback": "Piensa en lo que hace el conejo con la zanahoria."},
        {"tipo": "completar", "consigna": "Completa para decir que SÍ lo hace: 'Los niños ____ en el parque.'", "respuesta": "juegan", "otras_respuestas": ["corren", "ríen"], "feedback": "Qué hacen los niños en el parque."},
        {"tipo": "completar", "consigna": "Completa para decir que NO lo hace: 'Mi hermano ____ ____ libros.'", "respuesta": "no lee", "feedback": "Usa la palabra 'no' y una acción opuesta a leer si fuera el caso."},
        {"tipo": "completar", "consigna": "Completa con un verbo de acción: 'La Luna ____ en el cielo por la noche.'", "respuesta": "brilla", "otras_respuestas": ["aparece", "está"], "feedback": "Lo que hace la Luna en el cielo."},

        # Afirmar o Negar (5 ejercicios)
        {"tipo": "afirmar_negar", "consigna": "Si un pájaro puede volar, ¿cómo lo dices en una oración afirmativa? 'El pájaro ____.'", "respuesta": "vuela", "feedback": "¡Qué hace el pájaro!"},
        {"tipo": "afirmar_negar", "consigna": "Si un pez no puede hablar, ¿cómo lo dices en una oración negativa? 'El pez ____ ____.'", "respuesta": "no habla", "feedback": "Usa la palabra 'no' antes de la acción."},
        {"tipo": "afirmar_negar", "consigna": "Si tú comes fruta, ¿cómo lo dices en una oración afirmativa? 'Yo ____ fruta.'", "respuesta": "como", "feedback": "Tu acción."},
        {"tipo": "afirmar_negar", "consigna": "Si un gato no ladra, ¿cómo lo dices en una oración negativa? 'El gato ____ ____.'", "respuesta": "no ladra", "feedback": "El sonido que NO hace el gato."},
        {"tipo": "afirmar_negar", "consigna": "Si los niños ríen, ¿cómo lo dices en una oración afirmativa? 'Los niños ____.'", "respuesta": "ríen", "feedback": "La acción de los niños."},
    ]

    puntuacion = 0
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ejercicio in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        print(f"Consigna: {ejercicio['consigna']}")
        
        es_correcta = False
        respuesta_usuario = input("Tu respuesta: ").strip().lower() # Todo en minúsculas para comparar

        if "otras_respuestas" in ejercicio: # Para ejercicios con múltiples respuestas válidas
            if respuesta_usuario == ejercicio['respuesta'] or respuesta_usuario in ejercicio['otras_respuestas']:
                es_correcta = True
        elif respuesta_usuario == ejercicio['respuesta']:
            es_correcta = True

        if es_correcta:
            print("✅ ¡Muy bien! ¡Correcto!")
            puntuacion += 1
        else:
            print(f"❌ ¡Ups! No es lo que esperaba.")
            print(f"La respuesta correcta era: \"{ejercicio['respuesta']}\"")
            if "feedback" in ejercicio:
                print(f"Pista: {ejercicio['feedback']}")
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 15:
        print("🎉 ¡Felicidades! ¡Eres un campeón identificando verbos y usando el SÍ y el NO!")
    elif puntuacion >= 10:
        print("👍 ¡Lo estás haciendo muy bien! Sigue practicando y serás un experto.")
    else:
        print("✍️ ¡No te preocupes! Sigue practicando las acciones y el NO, ¡lo lograrás!")
    esperar(limpiar=True)

def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIOS EJEMPLOS!** ✍️")
    print("---")
    print("¡Vamos a inventar 20 ejemplos como los que vimos en la lección!")
    print("Piensa con calma y escribe lo que se te ocurra.")
    esperar("¡Empecemos a crear!")

    ejemplos_propios = []
    tipos_ejemplo = [
        "un verbo (palabra de acción)", "una oración afirmativa", "una oración negativa",
        "un verbo", "una oración afirmativa", "una oración negativa",
        "un verbo", "una oración afirmativa", "una oración negativa",
        "un verbo", "una oración afirmativa", "una oración negativa",
        "un verbo", "una oración afirmativa", "una oración negativa",
        "un verbo", "una oración afirmativa", "una oración negativa",
        "un verbo", "una oración afirmativa" # Últimos dos para llegar a 20 y variar un poco el final
    ]

    for i in range(20):
        print(f"\nEjemplo {i+1}/20: Escribe {tipos_ejemplo[i]}:")
        ejemplo = input("Tu ejemplo: ").strip()
        ejemplos_propios.append(f"{i+1}. {ejemplo} ({tipos_ejemplo[i]})")
        print("¡Guardado!")

    limpiar_consola()
    print("--- ¡TUS EJEMPLOS INVENTADOS! ---")
    print("\nAquí están tus 20 ejemplos:")
    for ejemplo in ejemplos_propios:
        print(ejemplo)
    print("\n¡Qué bien que creaste tus propios ejemplos! ¡Sigue practicando!")
    esperar(limpiar=True)

def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 5: ¡HACEMOS COSAS! (1.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos sobre los verbos!)")
        print("2. Ejemplos (¡Vemos más oraciones!)")
        print("3. Ejercicios (¡A practicar!)")
        print("4. Crear Mis Propios Ejemplos (¡Inventa tus oraciones!)") # Nueva opción
        print("5. Salir")
        print("---")

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == '1':
            mostrar_teoria()
        elif opcion == '2':
            mostrar_ejemplos()
        elif opcion == '3':
            realizar_ejercicios()
        elif opcion == '4': # Llama a la nueva función
            crear_ejemplos_propios()
        elif opcion == '5':
            print("\n¡Gracias por aprender! ¡Nos vemos pronto!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
