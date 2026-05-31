def mostrar_teoria():
    teoria = """
    === TEORÍA ===
    En español, cuando usamos el verbo impersonal «haber» para expresar obligación o necesidad:
    - La estructura afirmativa es: *"Hay que + infinitivo"* (Ej: "Hay que estudiar").
    - Al negar, el adverbio «no» suele anteponerse a «haber»: *"No hay que + infinitivo"* (Ej: "No hay que mentir").
    
    ¿Por qué ocurre esto?
    1. **Economía lingüística**: Es más natural anteponer «no» al verbo conjugado.
    2. **Analogía con otros verbos modales**: Como en "No debes fumar" o "No tienes que gritar".
    3. **Convención social**: La forma *"No hay que..."* se ha impuesto como norma, aunque técnicamente *"Hay que no..."* también es válida (pero menos usada).
    
    Ejemplos:
    - Correcto y común: "No hay que desanimarse" (≈ "Es necesario evitar desanimarse").
    - Menos frecuente: "Hay que no desanimarse" (Literal: "Es necesario no desanimarse").
    """
    print(teoria)

def ejercicio_redaccion():
    ejercicios = [
        {
            "frase": "Es necesario no olvidar las llaves.",
            "solucion": "No hay que olvidar las llaves."
        },
        {
            "frase": "Debes no hablar durante la película.",
            "solucion": "No hay que hablar durante la película."
        },
        {
            "frase": "Es importante no contaminar el río.",
            "solucion": "No hay que contaminar el río."
        }
    ]
    
    print("\n=== EJERCICIOS DE REDACCIÓN ===")
    print("Reescribe las siguientes oraciones usando «haber» como impersonal:")
    for i, ejercicio in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}: {ejercicio['frase']}")
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == ejercicio["solucion"].lower():
            print("✅ ¡Correcto! Has usado la estructura adecuada.")
        else:
            print(f"❌ Mejorable. La solución esperada es: {ejercicio['solucion']}")
    print("\n")

def cuestionario():
    preguntas = [
        {
            "pregunta": "¿Cuál es la estructura más común para negar en «hay que ayudar»?",
            "opciones": ["A) Hay que no ayudar", "B) No hay que ayudar", "C) Ninguna"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Por qué se prefiere «No hay que...» en lugar de «Hay que no...»?",
            "opciones": ["A) Es más lógico", "B) Es más corto y natural", "C) Suena más formal"],
            "respuesta": "B"
        },
        {
            "pregunta": "«Hay que no comer azúcar» es:",
            "opciones": ["A) Incorrecto", "B) Poco común pero válido", "C) Un error gramatical"],
            "respuesta": "B"
        }
    ]
    
    print("\n=== CUESTIONARIO ===")
    puntaje = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)
        respuesta = input("Elige (A/B/C): ").upper()
        if respuesta == pregunta['respuesta']:
            puntaje += 1
            print("✅ Correcto")
        else:
            print(f"❌ Incorrecto. La respuesta es {pregunta['respuesta']}")
    print(f"\nPuntaje final: {puntaje}/{len(preguntas)}")

def main():
    print("""
    ¡Bienvenido al programa de práctica con «haber» impersonal!
    Elige una opción:
    1. Ver teoría
    2. Hacer ejercicios de redacción
    3. Realizar cuestionario
    4. Salir
    """)
    
    while True:
        opcion = input("Opción (1-4): ").strip()
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_redaccion()
        elif opcion == "3":
            cuestionario()
        elif opcion == "4":
            print("¡Hasta pronto! ✨")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
