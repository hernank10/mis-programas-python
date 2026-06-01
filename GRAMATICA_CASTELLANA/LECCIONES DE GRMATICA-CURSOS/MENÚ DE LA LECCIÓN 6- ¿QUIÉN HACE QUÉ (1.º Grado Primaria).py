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
    print("📚 **TEORÍA: ¿QUIÉN HACE QUÉ? SUJETO Y VERBO** 📚")
    print("---")
    
    print("\n1. **Repaso: ¿Qué son los Verbos? ¡Palabras de Acción!**")
    print("   Recuerda que los **verbos** son las palabras que nos dicen **qué hacen** las personas, los animales o las cosas.")
    print("   - Ejemplos: **comer**, **jugar**, **dormir**, **correr**.")
    esperar()

    print("\n2. **¿Quién hace la acción? ¡El Sujeto!**")
    print("   Cada vez que algo se hace, hay alguien o algo que lo está haciendo. Esa persona o cosa es el **sujeto**.")
    print("   El **sujeto** es **quién** o **qué** hace la acción (el verbo).")
    print("   - Ej: En 'El niño **corre**', el **sujeto** es 'El niño'. ¿Quién corre? ¡El niño!")
    print("   - Ej: En 'La pelota **rebota**', el **sujeto** es 'La pelota'. ¿Qué rebota? ¡La pelota!")
    esperar()

    print("\n3. **¡Sujeto y Verbo Juntos!**")
    print("   Para que una oración tenga sentido, necesitamos saber **quién hace** algo y **qué hace**.")
    print("   - **Sujeto + Verbo = Oración simple**")
    print("   - Ej: **El perro** (sujeto) **ladra** (verbo).")
    print("   - Ej: **Yo** (sujeto) **salto** (verbo).")
    esperar()

    print("\n4. **Preguntas Mágicas: ¿Quién...? y ¿Qué hace...?**")
    print("   Podemos hacer preguntas para encontrar al sujeto y al verbo:")
    print("   - Para encontrar el **Sujeto**: Pregunta **¿QUIÉN?** o **¿QUÉ?** antes del verbo.")
    print("     - En 'Mi mamá **lee**', ¿QUIÉN lee? -> 'Mi mamá' (Sujeto).")
    print("   - Para encontrar el **Verbo**: Pregunta **¿QUÉ HACE?** el sujeto.")
    print("     - En 'Mi mamá **lee**', ¿QUÉ HACE mi mamá? -> 'Lee' (Verbo).")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS CLAROS** 💡")
    print("---")

    print("\n**Ejemplos de Sujetos y Verbos:**")
    print(" - **El sol** (sujeto) **brilla** (verbo).")
    print(" - **Las flores** (sujeto) **crecen** (verbo).")
    print(" - **Mi papá** (sujeto) **trabaja** (verbo).")
    esperar()

    print("\n**Identificando con preguntas:**")
    print(" - Oración: 'La tortuga **camina** lento.'")
    print("   - ¿QUIÉN camina? -> **La tortuga** (Sujeto)")
    print("   - ¿QUÉ HACE la tortuga? -> **Camina** (Verbo)")
    esperar()

    print(" - Oración: 'Los niños **juegan** en el parque.'")
    print("   - ¿QUIÉNES juegan? -> **Los niños** (Sujeto)")
    print("   - ¿QUÉ HACEN los niños? -> **Juegan** (Verbo)")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡ENCONTRANDO SUJETO Y VERBO!** 📝")
    print("---")
    print("¡Lee con atención! Vamos a descubrir quién hace qué.")
    esperar("¡Empecemos!")

    ejercicios = [
        # Identificar Sujeto (7 ejercicios)
        {"tipo": "sujeto", "consigna": "En la oración 'El gato come pescado.', ¿QUIÉN come?", "respuesta": "el gato", "feedback": "El sujeto es quien realiza la acción."},
        {"tipo": "sujeto", "consigna": "En 'María canta una canción.', ¿QUIÉN canta?", "respuesta": "maría", "feedback": "Piensa en la persona que hace la acción."},
        {"tipo": "sujeto", "consigna": "En 'El carro frena rápido.', ¿QUÉ frena?", "respuesta": "el carro", "feedback": "El sujeto puede ser una cosa también."},
        {"tipo": "sujeto", "consigna": "En 'Los pájaros vuelan alto.', ¿QUIÉNES vuelan?", "respuesta": "los pájaros", "feedback": "Recuerda que pueden ser varios."},
        {"tipo": "sujeto", "consigna": "En 'El tren llega a la estación.', ¿QUÉ llega?", "respuesta": "el tren", "feedback": "Qué cosa hace la acción."},
        {"tipo": "sujeto", "consigna": "En 'Yo bailo salsa.', ¿QUIÉN baila?", "respuesta": "yo", "feedback": "Cuando hablas de ti, 'yo' es el sujeto."},
        {"tipo": "sujeto", "consigna": "En 'Mi abuela cocina rico.', ¿QUIÉN cocina?", "respuesta": "mi abuela", "feedback": "La persona que hace la acción de cocinar."},

        # Identificar Verbo (7 ejercicios)
        {"tipo": "verbo", "consigna": "En 'El perro juega en el jardín.', ¿QUÉ HACE el perro?", "respuesta": "juega", "feedback": "El verbo es la acción que hace el sujeto."},
        {"tipo": "verbo", "consigna": "En 'La flor crece rápido.', ¿QUÉ HACE la flor?", "respuesta": "crece", "feedback": "Lo que hace la flor es el verbo."},
        {"tipo": "verbo", "consigna": "En 'Tú escribes una carta.', ¿QUÉ HACES tú?", "respuesta": "escribes", "feedback": "Tu acción."},
        {"tipo": "verbo", "consigna": "En 'El niño duerme en su cama.', ¿QUÉ HACE el niño?", "respuesta": "duerme", "feedback": "La acción de dormir."},
        {"tipo": "verbo", "consigna": "En 'El agua hierve en la olla.', ¿QUÉ HACE el agua?", "respuesta": "hierve", "feedback": "Lo que le pasa al agua, su acción."},
        {"tipo": "verbo", "consigna": "En 'Nosotros aprendemos mucho.', ¿QUÉ HACEMOS nosotros?", "respuesta": "aprendemos", "feedback": "La acción que están haciendo."},
        {"tipo": "verbo", "consigna": "En 'El viento sopla fuerte.', ¿QUÉ HACE el viento?", "respuesta": "sopla", "feedback": "La acción que hace el viento."},

        # Completar Oraciones (6 ejercicios)
        {"tipo": "completar", "consigna": "Completa la oración: 'El bebé ____.' (acción)", "respuesta": "llora", "otras_respuestas": ["duerme", "come", "ríe"], "feedback": "Piensa en algo que haga un bebé."},
        {"tipo": "completar", "consigna": "Completa la oración: '____ salta alto.' (quién)", "respuesta": "el conejo", "otras_respuestas": ["la niña", "el niño", "la rana"], "feedback": "¿Quién o qué puede saltar alto?"},
        {"tipo": "completar", "consigna": "Completa la oración: 'Las estrellas ____ en la noche.' (acción)", "respuesta": "brillan", "otras_respuestas": ["aparecen"], "feedback": "Qué hacen las estrellas en el cielo."},
        {"tipo": "completar", "consigna": "Completa la oración: '____ lee un cuento.' (quién)", "respuesta": "la mamá", "otras_respuestas": ["el papá", "la abuela", "el niño"], "feedback": "¿Quién puede leer un cuento?"},
        {"tipo": "completar", "consigna": "Completa la oración: 'Los peces ____ en el río.' (acción)", "respuesta": "nadan", "feedback": "Qué hacen los peces en el agua."},
        {"tipo": "completar", "consigna": "Completa la oración: '____ ladra mucho.' (quién)", "respuesta": "el perro", "feedback": "¿Qué animal ladra?"},
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
            print("✅ ¡Fantástico! ¡Correcto!")
            puntuacion += 1
        else:
            print(f"❌ ¡Inténtalo de nuevo!")
            print(f"La respuesta correcta era: \"{ejercicio['respuesta']}\"")
            if "feedback" in ejercicio:
                print(f"Pista: {ejercicio['feedback']}")
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Eres un campeón! ¡Sabes muy bien quién hace qué y qué se hace en las oraciones!")
    elif puntuacion >= 10:
        print("👍 ¡Muy bien! Sigue practicando y serás un detective de las oraciones.")
    else:
        print("✍️ ¡No te rindas! Sigue repasando el sujeto y el verbo, ¡lo lograrás!")
    esperar(limpiar=True)

def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIOS EJEMPLOS DE SUJETO Y VERBO!** ✍️")
    print("---")
    print("¡Vamos a inventar 20 ejemplos como los que vimos en la lección!")
    print("Puedes escribir oraciones o solo quién/qué o la acción.")
    esperar("¡Manos a la obra!")

    ejemplos_propios = []
    tipos_ejemplo = [
        "un sujeto (quién/qué hace algo)", "un verbo (la acción)", "una oración completa (sujeto + verbo)",
        "un sujeto", "un verbo", "una oración completa",
        "un sujeto", "un verbo", "una oración completa",
        "un sujeto", "un verbo", "una oración completa",
        "un sujeto", "un verbo", "una oración completa",
        "un sujeto", "un verbo", "una oración completa",
        "un sujeto", "un verbo" # Los últimos dos para completar 20
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
    print("\n¡Excelente trabajo creando tus propios ejemplos! ¡Eres un gran escritor!")
    esperar(limpiar=True)

def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: ¿QUIÉN HACE QUÉ? (1.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos sobre Sujeto y Verbo!)")
        print("2. Ejemplos (¡Vemos más oraciones!)")
        print("3. Ejercicios (¡A practicar y adivinar!)")
        print("4. Crear Mis Propios Ejemplos (¡Inventa tus oraciones!)")
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
            print("\n¡Gracias por aprender sobre sujeto y verbo! ¡Nos vemos pronto!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
