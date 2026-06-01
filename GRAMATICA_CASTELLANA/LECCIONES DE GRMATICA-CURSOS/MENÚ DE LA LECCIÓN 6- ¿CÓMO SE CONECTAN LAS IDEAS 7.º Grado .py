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
    print("📚 **TEORÍA: CONJUNCIONES Y PREPOSICIONES - LOS PEGAMENTOS DEL LENGUAJE** 📚")
    print("---")
    
    print("\n1. **¿Por Qué Conectamos Ideas?**")
    print("   Cuando hablamos o escribimos, no decimos palabras sueltas. ¡Las unimos para formar ideas completas! Para que todo se entienda bien y 'fluya', usamos palabras que son como **'pegamentos'** o **'puentes'** entre las ideas.")
    print("   Estas palabras nos ayudan a mostrar cómo se relacionan las cosas: si algo se suma, se opone, es una opción, una razón, un lugar o un tiempo.")
    esperar()

    print("\n2. **Las Conjunciones: ¡Uniendo Oraciones y Palabras!**")
    print("   Las **conjunciones** son palabras que **unen** palabras, frases u oraciones. Nos dicen si las ideas se **suman**, se **oponen**, si hay una **opción** o una **razón**.")
    print("   Algunos tipos de conjunciones son:")
    print("   - **Copulativas (suman/añaden):** y, e, ni")
    print("     - Ej: Juan **y** María juegan. No tiene dinero **ni** comida.")
    print("   - **Disyuntivas (dan opción):** o, u")
    print("     - Ej: ¿Quieres té **o** café? Siete **u** ocho.")
    print("   - **Adversativas (contrastan/se oponen):** pero, mas, sino")
    print("     - Ej: Es inteligente **pero** perezoso. No es azul **sino** verde.")
    print("   - **Causales (indican razón/causa):** porque, pues")
    print("     - Ej: Lloro **porque** estoy triste. Lo hizo, **pues** era necesario.")
    print("   - **Consecutivas (indican resultado/consecuencia):** luego, así que, por lo tanto")
    print("     - Ej: Estudió, **así que** aprobó.")
    esperar()

    print("\n3. **Las Preposiciones: ¡Ubicando y Relacionando!**")
    print("   Las **preposiciones** son palabras pequeñas que **relacionan** una palabra con otra. Nos indican una conexión de lugar, tiempo, causa, posesión, compañía, etc.")
    print("   ¡Son como pequeñas flechas que nos guían!")
    print("   Algunas preposiciones comunes son: **a, ante, bajo, con, contra, de, desde, en, entre, hacia, hasta, para, por, según, sin, sobre, tras.**")
    print("   - Ejemplos:")
    print("     - Ir **a** la escuela (dirección).")
    print("     - El libro está **sobre** la mesa (lugar).")
    print("     - Café **sin** azúcar (ausencia).")
    print("     - Jugar **con** mis amigos (compañía).")
    print("     - La casa **de** Juan (posesión).")
    esperar(limpiar=True)

def mostrar_ejemplos():
    limpiar_consola()
    print("💡 **EJEMPLOS: CONJUNCIONES Y PREPOSICIONES EN ACCIÓN** 💡")
    print("---")

    print("\n**Ejemplos de Conjunciones:**")
    print(" - Estudié mucho **y** saqué buena nota. (Unión)")
    print(" - Quiero helado **pero** no tengo dinero. (Oposición)")
    print(" - ¿Vienes hoy **o** mañana? (Opción)")
    print(" - Me fui a casa **porque** llovía. (Razón)")
    esperar()

    print("\n**Ejemplos de Preposiciones:**")
    print(" - Viajo **en** autobús. (Medio de transporte)")
    print(" - El regalo es **para** mi hermana. (Destino)")
    print(" - Vivo **en** Bogotá. (Lugar)")
    print(" - La película es **de** aventura. (Característica/Tipo)")
    print(" - Estaré aquí **desde** las diez **hasta** las cinco. (Tiempo)")
    esperar(limpiar=True)

def realizar_ejercicios():
    limpiar_consola()
    print("📝 **EJERCICIOS: ¡CONECTANDO LAS IDEAS!** 📝")
    print("---")
    print("¡Lee cada frase y elige la palabra correcta para conectar!")
    esperar("¡Empecemos!")

    ejercicios = [
        # Elegir conjunción (10 ejercicios)
        {"tipo": "conjuncion", "oracion": "Tengo sed ___ quiero agua.", "opciones": ["y", "pero", "o"], "respuesta": "y", "feedback": "Para sumar dos ideas."},
        {"tipo": "conjuncion", "oracion": "Es tarde ___ no me iré.", "opciones": ["y", "pero", "porque"], "respuesta": "pero", "feedback": "Hay una oposición, algo contrario."},
        {"tipo": "conjuncion", "oracion": "¿Estudias ___ juegas?", "opciones": ["y", "o", "porque"], "respuesta": "o", "feedback": "Es una elección entre dos cosas."},
        {"tipo": "conjuncion", "oracion": "No vino ___ estaba enfermo.", "opciones": ["y", "o", "porque"], "respuesta": "porque", "feedback": "Indica la razón de por qué no vino."},
        {"tipo": "conjuncion", "oracion": "Hice la tarea ___ así que puedo jugar.", "opciones": ["y", "o", "así que"], "respuesta": "así que", "feedback": "Indica una consecuencia o resultado."},
        {"tipo": "conjuncion", "oracion": "Mi mamá ___ mi papá salieron.", "opciones": ["ni", "o", "y"], "respuesta": "y", "feedback": "Para añadir una persona a otra."},
        {"tipo": "conjuncion", "oracion": "No es fácil ___ tampoco imposible.", "opciones": ["o", "ni", "pero"], "respuesta": "ni", "feedback": "Para negar dos cosas a la vez."},
        {"tipo": "conjuncion", "oracion": "Es pequeño ___ muy inteligente.", "opciones": ["pero", "o", "porque"], "respuesta": "pero", "feedback": "Contrasta dos cualidades."},
        {"tipo": "conjuncion", "oracion": "Tengo frío ___ me puse el abrigo.", "opciones": ["y", "así que", "pero"], "respuesta": "así que", "feedback": "Es la consecuencia de tener frío."},
        {"tipo": "conjuncion", "oracion": "¿Vamos al cine ___ al parque?", "opciones": ["y", "o", "porque"], "respuesta": "o", "feedback": "Pregunta por una opción."},

        # Elegir preposición (10 ejercicios)
        {"tipo": "preposicion", "oracion": "El libro está ___ la mesa.", "opciones": ["a", "en", "con"], "respuesta": "en", "feedback": "Indica lugar."},
        {"tipo": "preposicion", "oracion": "Voy ___ casa de mi abuela.", "opciones": ["de", "para", "a"], "respuesta": "a", "feedback": "Indica dirección o destino."},
        {"tipo": "preposicion", "oracion": "Hablo ___ mis amigos.", "opciones": ["por", "con", "sin"], "respuesta": "con", "feedback": "Indica compañía."},
        {"tipo": "preposicion", "oracion": "El pastel es ___ mi cumpleaños.", "opciones": ["de", "para", "en"], "respuesta": "para", "feedback": "Indica finalidad o destino."},
        {"tipo": "preposicion", "oracion": "El perro duerme ___ el sofá.", "opciones": ["sobre", "bajo", "a"], "respuesta": "sobre", "feedback": "Indica lugar (encima)."},
        {"tipo": "preposicion", "oracion": "Soy ___ Colombia.", "opciones": ["a", "de", "con"], "respuesta": "de", "feedback": "Indica origen o procedencia."},
        {"tipo": "preposicion", "oracion": "No puedo vivir ___ música.", "opciones": ["con", "sin", "por"], "respuesta": "sin", "feedback": "Indica ausencia."},
        {"tipo": "preposicion", "oracion": "Pasearemos ___ el parque.", "opciones": ["a", "por", "en"], "respuesta": "por", "feedback": "Indica lugar o tránsito."},
        {"tipo": "preposicion", "oracion": "El vaso está hecho ___ cristal.", "opciones": ["con", "de", "para"], "respuesta": "de", "feedback": "Indica material."},
        {"tipo": "preposicion", "oracion": "Lucharé ___ la injusticia.", "opciones": ["con", "para", "contra"], "respuesta": "contra", "feedback": "Indica oposición."},
    ]

    puntuacion = 0
    random.shuffle(ejercicios) # Mezclar ejercicios

    for i, ejercicio in enumerate(ejercicios):
        print(f"\n--- Ejercicio {i+1}/20 ---")
        
        opciones_str = ", ".join(ejercicio["opciones"])
        pregunta = f"Completa la oración: '{ejercicio['oracion'].replace('___', '___')}'\nOpciones: ({opciones_str})"
        print(pregunta)
        
        respuesta_usuario = input("Tu respuesta: ").strip().lower()

        if respuesta_usuario == ejercicio['respuesta'].lower():
            print("✅ ¡Correcto! ¡Esa es la palabra que conecta!")
            puntuacion += 1
        else:
            print(f"❌ ¡Intenta de nuevo!")
            print(f"La respuesta correcta era: '{ejercicio['respuesta']}'.")
            print(f"Pista: {ejercicio['feedback']}")
        
        esperar()

    limpiar_consola()
    print("--- ¡FIN DE LOS EJERCICIOS! ---")
    print(f"\nHas completado los ejercicios. ¡Tu puntuación final es: {puntuacion}/{len(ejercicios)}!")
    if puntuacion >= 16:
        print("🎉 ¡Felicidades! ¡Eres un maestro conectando ideas y palabras!")
    elif puntuacion >= 10:
        print("👍 ¡Buen trabajo! Estás entendiendo cómo se unen las frases.")
    else:
        print("✍️ ¡Sigue practicando! Pronto serás un experto en conjunciones y preposiciones.")
    esperar(limpiar=True)

def crear_ejemplos_propios():
    limpiar_consola()
    print("✍️ **¡CREA TUS PROPIAS ORACIONES CON CONJUNCIONES Y PREPOSICIONES!** ✍️")
    print("---")
    print("¡Vamos a inventar 20 oraciones usando conjunciones y preposiciones!")
    print("Intenta usar diferentes tipos para conectar tus ideas.")
    esperar("¡Manos a la obra!")

    ejemplos_propios = []
    
    for i in range(20):
        print(f"\n--- Tu Oración {i+1}/20 ---")
        oracion = input("Escribe una oración usando al menos una conjunción o preposición: ").strip()
        
        tipo_palabra = ""
        # Simplemente pedir al usuario que identifique lo que usó
        print("\nAhora, intenta identificar lo que usaste:")
        es_conjuncion = input("¿Usaste alguna CONJUNCIÓN (y, o, pero, porque, así que...)? (Sí/No): ").strip().lower()
        if es_conjuncion == 's':
            conjuncion_usada = input("¿Cuál conjunción usaste?: ").strip()
            tipo_palabra += f"Conjunción: {conjuncion_usada}; "
        
        es_preposicion = input("¿Usaste alguna PREPOSICIÓN (a, de, en, con, para, sobre...)? (Sí/No): ").strip().lower()
        if es_preposicion == 's':
            preposicion_usada = input("¿Cuál preposición usaste?: ").strip()
            tipo_palabra += f"Preposición: {preposicion_usada}"

        if not tipo_palabra:
            tipo_palabra = "No se identificaron conectores principales."

        ejemplos_propios.os.append(f"{i+1}. Oración: '{oracion}'\n   Conectores identificados: {tipo_palabra}\n")
        print("¡Ejemplo guardado!")

    limpiar_consola()
    print("--- ¡TUS ORACIONES CONECTADAS! ---")
    print("\nAquí están tus 20 oraciones y los conectores que identificaste:")
    for ejemplo in ejemplos_propios:
        print(ejemplo)
    print("\n¡Qué buen trabajo creando oraciones bien conectadas!")
    esperar(limpiar=True)


def mostrar_menu():
    while True:
        limpiar_consola()
        print("--- MENÚ DE LA LECCIÓN 6: ¿CÓMO SE CONECTAN LAS IDEAS? (7.º Grado Primaria) ---")
        print("\n1. Teoría (¡Aprendemos sobre los pegamentos del lenguaje!)")
        print("2. Ejemplos (¡Vemos conjunciones y preposiciones en acción!)")
        print("3. Ejercicios (¡A conectar ideas correctamente!)")
        print("4. Crear Mis Propias Oraciones (¡Inventa y usa conectores!)")
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
            print("\n¡Gracias por aprender a conectar ideas! ¡Sigue uniendo tus palabras con maestría!")
            sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
            esperar()

# Iniciar la aplicación
if __name__ == "__main__":
    mostrar_menu()
