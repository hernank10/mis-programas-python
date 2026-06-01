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
    print("📚 **TEORÍA: EL PREDICADO Y SU NÚCLEO (EL VERBO)** 📚")
    print("---")
    
    print("\n1. **Recordando: Sujeto y Verbo**")
    print("   Ya sabes que una oración tiene dos partes muy importantes:")
    print("   - El **Sujeto**: ¿Quién o qué hace la acción?")
    print("   - El **Verbo**: La acción que hace el sujeto.")
    print("   - Ej: **El pájaro** (Sujeto) **vuela** (Verbo).")
    esperar()

    print("\n2. **¿Qué es el Predicado? ¡La Otra Parte de la Oración!**")
    print("   Después de encontrar al **sujeto**, todo lo demás en la oración es el **Predicado**.")
    print("   El **Predicado** nos cuenta **qué hace el sujeto** o **qué se dice del sujeto**.")
    print("   - En 'El pájaro **vuela alto**', el predicado es 'vuela alto'.")
    print("   - En 'Mi hermana **lee un libro**', el predicado es 'lee un libro'.")
    esperar()

    print("\n3. **El Corazón del Predicado: ¡El Verbo es el Núcleo!**")
    print("   Dentro del predicado, hay una palabra que es la más, más, más importante: ¡es el **VERBO**!")
    print("   A esa palabra tan importante la llamamos el **NÚCLEO del Predicado**.")
    print("   ¡El verbo es el corazón del predicado, sin él, el predicado no tiene sentido!")
    print("   - Ej: En 'El pájaro **vuela** alto', el verbo '**vuela**' es el NÚCLEO del Predicado.")
    print("   - Ej: En 'Mi hermana **lee** un libro', el verbo '**lee**' es el NÚCLEO del Predicado.")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: PREDICADO Y NÚCLEO** 💡")
    print("---")

    print("\n**Oración:** 'Los niños juegan en el parque.'")
    print(" - **Sujeto:** Los niños (¿Quiénes juegan?)")
    print(" - **Predicado:** juegan en el parque (¿Qué hacen los niños?)")
    print(" - **Núcleo del Predicado:** **juegan** (El verbo, la acción principal)")
    esperar()

    print("\n**Oración:** 'Mi abuela cocina una sopa deliciosa.'")
    print(" - **Sujeto:** Mi abuela (¿Quién cocina?)")
    print(" - **Predicado:** cocina una sopa deliciosa (¿Qué hace mi abuela?)")
    print(" - **Núcleo del Predicado:** **cocina** (El verbo, el corazón del predicado)")
    esperar()

    print("\n**Oración:** 'El sol calienta la Tierra.'")
    print(" - **Sujeto:** El sol (¿Qué calienta?)")
    print(" - **Predicado:** calienta la Tierra (¿Qué hace el sol?)")
    print(" - **Núcleo del Predicado:** **calienta** (El verbo)")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡ENCONTRANDO EL CORAZÓN DEL PREDICADO!** 📝")
    print("---")
    print("¡Vamos a leer oraciones y encontrar el predicado y su núcleo!")
    esperar("¡Empecemos!")

    ejercicios = [
        # Identificar Predicado (10 ejercicios)
        {"tipo": "predicado", "oracion": "El perro ladra muy fuerte.", "sujeto": "El perro", "predicado_correcto": "ladra muy fuerte", "feedback": "Todo lo que se dice del sujeto."},
        {"tipo": "predicado", "oracion": "Mi mamá lee un cuento.", "sujeto": "Mi mamá", "predicado_correcto": "lee un cuento", "feedback": "Lo que la mamá hace."},
        {"tipo": "predicado", "oracion": "Las flores crecen en el jardín.", "sujeto": "Las flores", "predicado_correcto": "crecen en el jardín", "feedback": "La acción y lo que la acompaña."},
        {"tipo": "predicado", "oracion": "Los estudiantes aprenden mucho.", "sujeto": "Los estudiantes", "predicado_correcto": "aprenden mucho", "feedback": "Qué hacen los estudiantes."},
        {"tipo": "predicado", "oracion": "El avión vuela por el cielo.", "sujeto": "El avión", "predicado_correcto": "vuela por el cielo", "feedback": "Qué hace el avión."},
        {"tipo": "predicado", "oracion": "Mi hermano juega fútbol.", "sujeto": "Mi hermano", "predicado_correcto": "juega fútbol", "feedback": "Lo que tu hermano hace."},
        {"tipo": "predicado", "oracion": "La luna brilla en la noche.", "sujeto": "La luna", "predicado_correcto": "brilla en la noche", "feedback": "Qué hace la luna."},
        {"tipo": "predicado", "oracion": "Yo escribo una carta.", "sujeto": "Yo", "predicado_correcto": "escribo una carta", "feedback": "Tu acción."},
        {"tipo": "predicado", "oracion": "El bebé duerme tranquilamente.", "sujeto": "El bebé", "predicado_correcto": "duerme tranquilamente", "feedback": "Qué hace el bebé."},
        {"tipo": "predicado", "oracion": "Las campanas suenan fuerte.", "sujeto": "Las campanas", "predicado_correcto": "suenan fuerte", "feedback": "La acción de las campanas."},

        # Identificar Núcleo del Predicado (Verbo) (10 ejercicios)
        {"tipo": "nucleo", "oracion": "El perro ladra muy fuerte.", "predicado": "ladra muy fuerte", "nucleo_correcto": "ladra", "feedback": "Busca la palabra que es la acción."},
        {"tipo": "nucleo", "oracion": "Mi mamá lee un cuento.", "predicado": "lee un cuento", "nucleo_correcto": "lee", "feedback": "El corazón del predicado es el verbo."},
        {"tipo": "nucleo", "oracion": "Las flores crecen en el jardín.", "predicado": "crecen en el jardín", "nucleo_correcto": "crecen", "feedback": "La acción principal."},
        {"tipo": "nucleo", "oracion": "Los estudiantes aprenden mucho.", "predicado": "aprenden mucho", "nucleo_correcto": "aprenden", "feedback": "Qué hacen los estudiantes."},
        {"tipo": "nucleo", "oracion": "El avión vuela por el cielo.", "predicado": "vuela por el cielo", "nucleo_correcto": "vuela", "feedback": "La acción del avión."},
        {"tipo": "nucleo", "oracion": "Mi hermano juega fútbol.", "predicado": "juega fútbol", "nucleo_correcto": "juega", "feedback": "Lo que tu hermano hace."},
        {"tipo": "nucleo", "oracion": "La luna brilla en la noche.", "predicado": "brilla en la noche", "nucleo_correcto": "brilla", "feedback": "Qué hace la luna."},
        {"tipo": "nucleo", "oracion": "Yo escribo una carta.", "predicado": "escribo una carta", "nucleo_correcto": "escribo", "feedback": "Tu acción."},
        {"tipo": "nucleo", "oracion": "El bebé duerme tranquilamente.", "predicado": "duerme tranquilamente", "nucleo_correcto": "duerme", "feedback": "La acción del bebé."},
        {"tipo": "nucleo", "oracion": "Las campanas suenan fuerte.", "predicado": "suenan fuerte", "nucleo_correcto": "suenan", "feedback": "La acción de las campanas."},
    ]

    puntuacion = 0
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ejercicio in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        print(f"Oración: '{ejercicio['oracion']}'")

        if ejercicio["tipo"] == "predicado":
            print(f"El sujeto es: '{ejercicio['sujeto']}'.")
            respuesta_usuario = input("Escribe el PREDICADO de la oración: ").strip().lower()
            if respuesta_usuario == ejercicio['predicado_correcto'].lower():
                print("✅ ¡Muy bien! ¡Ese es el predicado!")
                puntuacion += 1
            else:
                print(f"❌ ¡Intenta de nuevo!")
                print(f"El predicado correcto es: '{ejercicio['predicado_correcto']}'.")
                print(f"Pista: {ejercicio['feedback']}")
        elif ejercicio["tipo"] == "nucleo":
            print(f"El predicado es: '{ejercicio['predicado']}'.")
            respuesta_usuario = input("Escribe el NÚCLEO del Predicado (el verbo): ").strip().lower()
            if respuesta_usuario == ejercicio['nucleo_correcto'].lower():
                print("✅ ¡Excelente! ¡Ese es el corazón del predicado!")
                puntuacion += 1
            else:
                print(f"❌ ¡Puedes mejorar!")
                print(f"El núcleo del predicado es: '{ejercicio['nucleo_correcto']}'.")
                print(f"Pista: {ejercicio['feedback']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Increíble! ¡Eres un experto en el predicado y su núcleo!")
    elif puntuacion >= 10:
        print("👍 ¡Buen trabajo! Sigue practicando y serás un maestro.")
    else:
        print("✍️ ¡Sigue intentándolo! Con más práctica, identificarás el corazón del predicado sin problema.")
    esperar(limpiar=True)

def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIAS ORACIONES Y ENCUENTRA SU CORAZÓN!** ✍️")
    print("---")
    print("¡Vamos a inventar 20 oraciones y encontrar su sujeto, predicado y núcleo!")
    print("Piensa en quién hace algo y qué hace.")
    esperar("¡Manos a la obra!")

    ejemplos_propios = []
    
    for i in range(20):
        print(f"\n--- Tu Oración {i+1}/20 ---")
        oracion = input("Escribe una oración simple (ej: El perro juega en el jardín.): ").strip()
        
        # Intentar obtener sujeto y predicado
        # Esta es una simplificación, en un sistema real sería más robusto.
        partes = oracion.lower().split(' ', 1) # Divide en la primera palabra y el resto
        if len(partes) > 1:
            posible_sujeto_inicio = partes[0]
            posible_predicado_resto = partes[1]
        else:
            posible_sujeto_inicio = oracion.lower()
            posible_predicado_resto = ""

        sujeto_propuesto = input(f"¿Quién/Qué hace la acción en '{oracion}'? (Sujeto): ").strip()
        predicado_propuesto = input(f"¿Qué se dice del sujeto en '{oracion}'? (Predicado): ").strip()
        nucleo_propuesto = input(f"¿Cuál es el verbo (el núcleo) del predicado en '{predicado_propuesto}'?: ").strip()

        ejemplos_propios.append(f"{i+1}. Oración: '{oracion}'\n   Sujeto: {sujeto_propuesto}\n   Predicado: {predicado_propuesto}\n   Núcleo: {nucleo_propuesto}\n")
        print("¡Ejemplo guardado!")

    limpiar_consola()
    print("--- ¡TUS ORACIONES Y SUS CORAZONES! ---")
    print("\nAquí están tus 20 oraciones con sus partes identificadas:")
    for ejemplo in ejemplos_propios:
        print(ejemplo)
    print("\n¡Qué bien! ¡Eres un gran analista de oraciones!")
    esperar(limpiar=True)


def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: EL PREDICADO Y SU NÚCLEO (4.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos sobre el predicado y su corazón!)")
        print("2. Ejemplos (¡Vemos oraciones y sus partes!)")
        print("3. Ejercicios (¡A encontrar el predicado y su núcleo!)")
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
            print("\n¡Gracias por aprender sobre el predicado! ¡Sigue descubriendo el lenguaje!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
