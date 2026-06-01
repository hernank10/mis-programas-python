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
    print("📚 **TEORÍA: ¿CÓMO SE COMPONE EL SUJETO?** 📚")
    print("---")
    
    print("\n1. **Recordando el Sujeto: ¿Quién o Qué?**")
    print("   El **sujeto** es la parte de la oración que nos dice **quién** o **qué** hace la acción, o de quién o qué se habla.")
    print("   - Ej: **El gato** come pescado. (¿Quién come? El gato)")
    print("   - Ej: **Mi libro** es interesante. (¿Qué es interesante? Mi libro)")
    esperar()

    print("\n2. **El Corazón del Sujeto: ¡El Núcleo del Sujeto!**")
    print("   Dentro del sujeto, hay una palabra que es la más importante. A esa palabra la llamamos el **Núcleo del Sujeto**.")
    print("   El Núcleo del Sujeto casi siempre es un **sustantivo** (una palabra que nombra personas, animales, cosas o ideas) o un **pronombre** (palabras como yo, tú, él, ella, nosotros, ellos).")
    print("   - Ej: En '**El** **gato** **grande**', el núcleo es **gato** (un sustantivo).")
    print("   - Ej: En '**Ella** canta', el núcleo es **Ella** (un pronombre).")
    esperar()

    print("\n3. **Los Modificadores del Sujeto: ¡Los Acompañantes!**")
    print("   Los modificadores son palabras que **acompañan** al núcleo del sujeto para darnos más información sobre él.")
    print("   Los más comunes son los **Modificadores Directos (MD)**:")
    print("   - **Artículos**: Palabras como 'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas'. (Ej: **La** casa, **un** perro)")
    print("   - **Adjetivos**: Palabras que nos dicen cómo es o cómo está el sustantivo. (Ej: La casa **grande**, el perro **bonito**)")
    print("   - Ej: En '**El** **gato** **grande**', 'El' y 'grande' son modificadores directos (MD).")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: COMPOSICIÓN DEL SUJETO** 💡")
    print("---")

    print("\n**Ejemplo 1:** 'La pequeña ardilla come nueces.'")
    print(" - **Sujeto completo:** La pequeña ardilla")
    print(" - **Núcleo del Sujeto:** ardilla (sustantivo)")
    print(" - **Modificadores Directos (MD):** La (artículo), pequeña (adjetivo)")
    esperar()

    print("\n**Ejemplo 2:** 'Un viejo árbol da mucha sombra.'")
    print(" - **Sujeto completo:** Un viejo árbol")
    print(" - **Núcleo del Sujeto:** árbol (sustantivo)")
    print(" - **Modificadores Directos (MD):** Un (artículo), viejo (adjetivo)")
    esperar()

    print("\n**Ejemplo 3:** 'Mis amigos juegan fútbol.'")
    print(" - **Sujeto completo:** Mis amigos")
    print(" - **Núcleo del Sujeto:** amigos (sustantivo)")
    print(" - **Modificadores Directos (MD):** Mis (adjetivo posesivo, funciona como un adjetivo aquí)")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡ANALIZANDO EL SUJETO!** 📝")
    print("---")
    print("¡Vamos a encontrar las partes del sujeto en cada oración!")
    esperar("¡Comencemos!")

    ejercicios = [
        # Identificar Núcleo del Sujeto (10 ejercicios)
        {"tipo": "nucleo", "oracion": "El **perro** juguetón salta.", "sujeto_completo": "El perro juguetón", "respuesta": "perro", "feedback": "Es la palabra principal del sujeto, el animal."},
        {"tipo": "nucleo", "oracion": "La **casa** grande tiene un jardín.", "sujeto_completo": "La casa grande", "respuesta": "casa", "feedback": "El objeto principal."},
        {"tipo": "nucleo", "oracion": "**Ella** canta muy bonito.", "sujeto_completo": "Ella", "respuesta": "ella", "feedback": "Cuando el sujeto es un pronombre, ese es el núcleo."},
        {"tipo": "nucleo", "oracion": "Los **niños** traviesos ríen fuerte.", "sujeto_completo": "Los niños traviesos", "respuesta": "niños", "feedback": "La persona principal."},
        {"tipo": "nucleo", "oracion": "Mi **bicicleta** nueva es veloz.", "sujeto_completo": "Mi bicicleta nueva", "respuesta": "bicicleta", "feedback": "El objeto."},
        {"tipo": "nucleo", "oracion": "Una **flor** roja creció en el campo.", "sujeto_completo": "Una flor roja", "respuesta": "flor", "feedback": "La planta principal."},
        {"tipo": "nucleo", "oracion": "Los **aviones** grandes vuelan alto.", "sujeto_completo": "Los aviones grandes", "respuesta": "aviones", "feedback": "El medio de transporte."},
        {"tipo": "nucleo", "oracion": "**Nosotros** estudiamos con ganas.", "sujeto_completo": "Nosotros", "respuesta": "nosotros", "feedback": "El pronombre."},
        {"tipo": "nucleo", "oracion": "El **árbol** frondoso da mucha sombra.", "sujeto_completo": "El árbol frondoso", "respuesta": "árbol", "feedback": "La palabra principal del sujeto."},
        {"tipo": "nucleo", "oracion": "Mi **hermano** pequeño juega.", "sujeto_completo": "Mi hermano pequeño", "respuesta": "hermano", "feedback": "La persona principal en el sujeto."},
        
        # Identificar Modificadores Directos (10 ejercicios)
        {"tipo": "md", "oracion": "El perro **juguetón** salta.", "sujeto_completo": "El perro juguetón", "nucleo": "perro", "respuesta": "el, juguetón", "feedback": "Busca el artículo y el adjetivo que acompañan al núcleo.", "otras_respuestas": ["juguetón, el"]},
        {"tipo": "md", "oracion": "La casa **grande** tiene un jardín.", "sujeto_completo": "La casa grande", "nucleo": "casa", "respuesta": "la, grande", "feedback": "El artículo y el adjetivo.", "otras_respuestas": ["grande, la"]},
        {"tipo": "md", "oracion": "Un **valiente** bombero apagó el fuego.", "sujeto_completo": "Un valiente bombero", "nucleo": "bombero", "respuesta": "un, valiente", "feedback": "El artículo y la cualidad del bombero.", "otras_respuestas": ["valiente, un"]},
        {"tipo": "md", "oracion": "Los **altos** árboles dan mucha sombra.", "sujeto_completo": "Los altos árboles", "nucleo": "árboles", "respuesta": "los, altos", "feedback": "El artículo y el adjetivo que describen a los árboles.", "otras_respuestas": ["altos, los"]},
        {"tipo": "md", "oracion": "Mi **nueva** computadora es muy rápida.", "sujeto_completo": "Mi nueva computadora", "nucleo": "computadora", "respuesta": "mi, nueva", "feedback": "El posesivo y el adjetivo.", "otras_respuestas": ["nueva, mi"]},
        {"tipo": "md", "oracion": "El **pequeño** pájaro construyó un nido.", "sujeto_completo": "El pequeño pájaro", "nucleo": "pájaro", "respuesta": "el, pequeño", "feedback": "El artículo y el adjetivo.", "otras_respuestas": ["pequeño, el"]},
        {"tipo": "md", "oracion": "Una **gran** idea surgió en la reunión.", "sujeto_completo": "Una gran idea", "nucleo": "idea", "respuesta": "una, gran", "feedback": "El artículo y el adjetivo que describe la idea.", "otras_respuestas": ["gran, una"]},
        {"tipo": "md", "oracion": "Los **primeros** invitados llegaron temprano.", "sujeto_completo": "Los primeros invitados", "nucleo": "invitados", "respuesta": "los, primeros", "feedback": "El artículo y el adjetivo que indica orden.", "otras_respuestas": ["primeros, los"]},
        {"tipo": "md", "oracion": "Mi **vieja** guitarra suena bien.", "sujeto_completo": "Mi vieja guitarra", "nucleo": "guitarra", "respuesta": "mi, vieja", "feedback": "El posesivo y el adjetivo.", "otras_respuestas": ["vieja, mi"]},
        {"tipo": "md", "oracion": "El **cielo** azul es hermoso.", "sujeto_completo": "El cielo azul", "nucleo": "cielo", "respuesta": "el, azul", "feedback": "El artículo y el color que lo describe.", "otras_respuestas": ["azul, el"]},
    ]

    puntuacion = 0
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ejercicio in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        print(f"Oración: '{ejercicio['oracion']}'")
        print(f"Sujeto completo: '{ejercicio['sujeto_completo']}'")

        if ejercicio["tipo"] == "nucleo":
            respuesta_usuario = input("Escribe el NÚCLEO del sujeto: ").strip().lower()
            if respuesta_usuario == ejercicio['respuesta'].lower():
                print("✅ ¡Muy bien! ¡Ese es el corazón del sujeto!")
                puntuacion += 1
            else:
                print(f"❌ ¡Intenta de nuevo!")
                print(f"El núcleo del sujeto es: '{ejercicio['respuesta']}'.")
                print(f"Pista: {ejercicio['feedback']}")
        elif ejercicio["tipo"] == "md":
            print(f"El núcleo del sujeto es: '{ejercicio['nucleo']}'.")
            respuesta_usuario = input("Escribe los MODIFICADORES DIRECTOS (separados por coma si hay más de uno): ").strip().lower()
            respuestas_correctas = [r.strip() for r in ejercicio['respuesta'].lower().split(',')]
            respuestas_usuario_lista = [r.strip() for r in respuesta_usuario.split(',')]
            
            # Comprobar si todas las respuestas correctas están en las del usuario, sin importar el orden
            if all(r in respuestas_usuario_lista for r in respuestas_correctas) and \
               len(respuestas_usuario_lista) == len(respuestas_correctas):
                print("✅ ¡Excelente! ¡Encontraste todos los modificadores!")
                puntuacion += 1
            else:
                print(f"❌ ¡Puedes mejorar!")
                print(f"Los modificadores directos correctos son: '{ejercicio['respuesta']}'.")
                print(f"Pista: {ejercicio['feedback']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Genial! ¡Eres un experto en desarmar el sujeto y encontrar sus partes!")
    elif puntuacion >= 10:
        print("👍 ¡Muy bien! Ya entiendes cómo se compone el sujeto.")
    else:
        print("✍️ ¡Sigue practicando! Con más práctica, ¡identificarás todas las partes del sujeto!")
    esperar(limpiar=True)

def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIAS ORACIONES Y ANALIZA EL SUJETO!** ✍️")
    print("---")
    print("¡Vamos a inventar 20 oraciones y encontrar las partes de su sujeto!")
    print("Intenta que el sujeto tenga un artículo y un adjetivo si puedes.")
    esperar("¡Manos a la obra!")

    ejemplos_propios = []
    
    for i in range(20):
        print(f"\n--- Tu Oración {i+1}/20 ---")
        oracion = input("Escribe una oración (ej: La niña pequeña juega en el parque.): ").strip()
        
        print(f"\nAnaliza el sujeto de tu oración: '{oracion}'")
        sujeto_completo = input("1. Escribe el SUJETO COMPLETO: ").strip()
        nucleo_propuesto = input("2. Escribe el NÚCLEO del Sujeto (sustantivo o pronombre): ").strip()
        md_propuestos = input("3. Escribe los MODIFICADORES DIRECTOS (artículos o adjetivos, separados por coma): ").strip()

        ejemplos_propios.append(f"{i+1}. Oración: '{oracion}'\n   Sujeto: '{sujeto_completo}'\n   Núcleo: '{nucleo_propuesto}'\n   MD: '{md_propuestos}'\n")
        print("¡Ejemplo guardado!")

    limpiar_consola()
    print("--- ¡TUS ORACIONES Y SUS SUJETOS ANALIZADOS! ---")
    print("\nAquí están tus 20 oraciones con las partes de su sujeto:")
    for ejemplo in ejemplos_propios:
        print(ejemplo)
    print("\n¡Excelente trabajo analizando la composición del sujeto en tus propias frases!")
    esperar(limpiar=True)


def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: LAS PARTES DEL SUJETO (5.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos a desarmar el sujeto!)")
        print("2. Ejemplos (¡Vemos cómo se compone el sujeto!)")
        print("3. Ejercicios (¡A encontrar el núcleo y los modificadores!)")
        print("4. Crear Mis Propias Oraciones (¡Inventa y analiza tus sujetos!)")
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
            print("\n¡Gracias por aprender sobre las partes del sujeto! ¡Sigue explorando el lenguaje!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
