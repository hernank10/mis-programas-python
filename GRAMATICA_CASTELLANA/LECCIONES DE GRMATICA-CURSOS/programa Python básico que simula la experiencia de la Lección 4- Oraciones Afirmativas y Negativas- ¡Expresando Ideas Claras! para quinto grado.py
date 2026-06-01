import time
import random

def limpiar_consola():
    """Simula la limpieza de la consola (funciona mejor en entornos de terminal)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar():
    """Pausa la ejecución para que el usuario pueda leer."""
    input("\nPresiona Enter para continuar...")

def iniciar_leccion_quinto_grado():
    limpiar_consola()
    print("🧠 ¡Hola, arquitectos del lenguaje! 🧠")
    print("\n¡Bienvenidos a una lección donde construiremos oraciones AFIRMATIVAS y NEGATIVAS muy precisas!")
    print("Aprenderemos a usar palabras de diferentes formas para que nuestras ideas sean CLARAS.")
    print("¡Y veremos que cada oración tiene una INTENCIÓN especial: decir un hecho, una opinión, una prohibición, etc.!")
    esperar()

    # --- Actividad 1: Analizando la Intención ---
    limpiar_consola()
    print("🕵️‍♂️ Actividad 1: Analizando la Intención: ¿Qué Quiere Decir Esta Oración? 🕵️‍♀️")
    print("Leerás oraciones. Primero, di si es afirmativa o negativa. Luego, piensa: ¿Qué INTENCIÓN tiene?")
    esperar()

    oraciones_intencion = [
        ("Es probable que el equipo gane el partido.", "afirmativa", "expresar una posibilidad"),
        ("Está prohibido correr en los pasillos.", "negativa", "indicar una prohibición/orden"),
        ("Mi hermana no quiere comer verduras.", "negativa", "expresar un deseo/preferencia negativa"),
        ("Definitivamente, no iremos al paseo si llueve.", "negativa", "negar rotundamente una acción bajo una condición")
    ]

    for oracion, tipo_correcto, intencion_esperada in oraciones_intencion:
        print(f"\nOración: \"{oracion}\"")
        tipo_usuario = input("¿Es AFIRMATIVA o NEGATIVA?: ").strip().lower()
        if tipo_usuario == tipo_correcto:
            print(f"✅ ¡Correcto! Es {tipo_correcto.upper()}.")
        else:
            print(f"❌ Incorrecto. Es {tipo_correcto.upper()}.")

        intencion_usuario = input(f"¿Qué INTENCIÓN crees que tiene esta oración? (Ej: dar información, una orden, un deseo, una posibilidad, etc.): ").strip().lower()
        # Aquí la validación es más flexible, pues la interpretación puede variar ligeramente
        if intencion_esperada in intencion_usuario:
            print(f"🎉 ¡Muy bien! Una de sus intenciones es {intencion_esperada}.")
        else:
            print(f"🤔 La intención principal es {intencion_esperada}. ¡Buen intento!")
        esperar()

    # --- Actividad 2: Construyendo con Precisión ---
    limpiar_consola()
    print("✨ Actividad 2: Construyendo con Precisión: ¡Más Allá del 'No'! ✨")
    print("Transformaremos oraciones. Usaremos palabras como 'nunca', 'nadie', 'nada' para negar, ¡y construiremos con mucha precisión!")
    esperar()

    oraciones_precision = [
        ("Afirmativa", "Siempre hay mucha gente en la playa.", "nunca", "Nunca hay mucha gente en la playa."),
        ("Afirmativa", "Todo el mundo lo sabía.", "nadie", "Nadie lo sabía."),
        ("Afirmativa", "Mi mamá compró algunas cosas.", "nada", "Mi mamá no compró nada."),
        ("Negativa", "El ejercicio no es aburrido.", "afirmativa", "El ejercicio es divertido."), # Aquí buscamos un antónimo afirmativo
    ]

    for tipo_original, original, palabra_clave_o_tipo, transformada_esperada in oraciones_precision:
        print(f"\nOración {tipo_original}: \"{original}\"")
        if tipo_original == "Afirmativa":
            print(f"Conviértela en NEGATIVA usando la palabra: '{palabra_clave_o_tipo}'")
        else:
            print(f"Conviértela en AFIRMATIVA buscando una palabra contraria:")
            
        respuesta_usuario = input("Tu oración transformada: ").strip()

        if respuesta_usuario.lower() == transformada_esperada.lower():
            print("✅ ¡Perfecto! La transformaste correctamente y con precisión.")
        else:
            print(f"❌ Casi. La oración transformada podría ser: \"{transformada_esperada}\"")
        esperar()

    # --- Actividad 3: Redacción en Contexto ---
    limpiar_consola()
    print("📝 Actividad 3: Redacción en Contexto: Noticias, Opiniones y Reglas ✍️")
    print("Imaginarás escenarios y escribirás oraciones AFIRMATIVAS y NEGATIVAS que encajen, ¡con la intención correcta!")
    esperar()

    print("\n--- Escenario 1: Reglas de la biblioteca ---")
    print("El director anuncia las reglas de la biblioteca.")
    print("Escribe una regla que SÍ se puede hacer (afirmativa):")
    input("Regla afirmativa: ").strip() # No se valida contenido, solo la participación
    print("¡Muy bien! Esa es una buena regla afirmativa.")
    esperar()

    print("\nEscribe una regla que NO se puede hacer (negativa, usa 'no está permitido' o 'no se debe'):")
    regla_negativa = input("Regla negativa: ").strip().lower()
    if "no" in regla_negativa or "prohibido" in regla_negativa:
        print("¡Excelente! Has creado una regla negativa clara.")
    else:
        print("Recuerda usar palabras de negación como 'no' o 'prohibido'.")
    esperar()

    print("\n--- Escenario 2: Tu opinión sobre una película ---")
    print("Escribe una oración afirmativa sobre algo que te gustó de una película:")
    input("Opinión afirmativa: ").strip()
    print("¡Así se expresa una opinión afirmativa!")
    esperar()

    print("\nEscribe una oración negativa sobre algo que no te gustó de esa misma película (usa 'no', 'en absoluto', etc.):")
    opinion_negativa = input("Opinión negativa: ").strip().lower()
    if "no" in opinion_negativa or "absoluto" in opinion_negativa or "nada" in opinion_negativa:
        print("¡Muy bien! Tu opinión negativa está clara.")
    else:
        print("Asegúrate de que tu oración exprese negación.")
    esperar()

    # --- Actividad 4: Detective de Intenciones (Verdadero/Falso) ---
    limpiar_consola()
    print("🔍 Actividad 4: Detective de Intenciones: ¿Qué Ocurrió o No Ocurrió? 🧐")
    print("Te daré un contexto (una imagen o evento). Luego, lee las oraciones y di si son AFIRMATIVAS o NEGATIVAS, y si lo que dicen es VERDADERO o FALSO según el contexto.")
    esperar()

    contexto_futbol = {
        "descripcion": "Imagina que estás viendo un partido de fútbol. El equipo rojo gana 2-0. Está lloviendo un poco. Hay mucha gente aplaudiendo en las gradas.",
        "oraciones": [
            ("El equipo rojo ganó el partido claramente.", "afirmativa", "verdadero"),
            ("No llovió durante el juego.", "negativa", "falso"), # En el contexto sí llueve un poco
            ("Nadie aplaudió al final del partido.", "negativa", "falso"), # En el contexto sí aplaudieron
            ("Los jugadores estaban muy cansados al final.", "afirmativa", "verdadero") # Es una inferencia razonable
        ]
    }

    print(f"\n--- Contexto: {contexto_futbol['descripcion']} ---")
    esperar()

    for oracion, tipo_esperado, verdad_falsedad_esperada in contexto_futbol["oraciones"]:
        print(f"\nOración: \"{oracion}\"")
        tipo_usuario = input("¿Es AFIRMATIVA o NEGATIVA?: ").strip().lower()
        if tipo_usuario == tipo_esperado:
            print(f"✅ Tipo correcto: {tipo_esperado.upper()}.")
        else:
            print(f"❌ Tipo incorrecto. Es {tipo_esperado.upper()}.")
        
        verdad_falsedad_usuario = input("¿Es VERDADERA o FALSA según el contexto?: ").strip().lower()
        if verdad_falsedad_usuario == verdad_falsedad_esperada:
            print(f"🎉 ¡Correcto! Es **{verdad_falsedad_esperada.upper()}**.")
        else:
            print(f"🤔 Incorrecto. En este contexto, es **{verdad_falsedad_esperada.upper()}**.")
        esperar()

    # --- Cierre ---
    limpiar_consola()
    print("🎉 ¡Felicidades, Súper Arquitectos del Lenguaje! 🎉")
    print("¡Hoy aprendimos que las oraciones **afirmativas** y **negativas** tienen **intenciones** y pueden ser muy **precisas**!")
    print("¡Sigan construyendo ideas claras y comunicando con poder!")
    print("\n¡Hasta la próxima aventura de palabras! ✨")
    esperar()

# Ejecutar la lección
if __name__ == "__main__":
    iniciar_leccion_quinto_grado()
