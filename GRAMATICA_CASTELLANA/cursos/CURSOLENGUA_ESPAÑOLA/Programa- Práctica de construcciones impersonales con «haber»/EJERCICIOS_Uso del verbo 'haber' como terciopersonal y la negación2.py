puntaje_total = 0  # Puntuación acumulativa global

def mostrar_teoria():
    print("\nTEORÍA: Uso del verbo 'haber' como terciopersonal y la negación\n")
    print("""
En español, el verbo 'haber' se usa en construcciones impersonales para expresar necesidad u obligación general.

Ejemplo:
    Hay que estudiar.     (Significa: Es necesario estudiar)

Cuando negamos este tipo de construcciones, la negación recae sobre 'haber', no sobre el verbo principal.
Ejemplo:
    No hay que desanimarse.   (Significa: Es necesario no desanimarse)

Desde un punto de vista lógico, la forma correcta sería:
    Hay que no desanimarse.

Pero esta última suena forzada. Por eso, se prefiere 'No hay que desanimarse' por motivos de claridad y fluidez.
    """)

def cuestionario():
    global puntaje_total
    print("\nCUESTIONARIO: Elige la opción correcta\n")
    preguntas = [
        {
            "pregunta": "¿Qué significa la oración 'No hay que rendirse'?",
            "opciones": [
                "a) No es necesario rendirse",
                "b) Es necesario no rendirse",
                "c) Nadie debe rendirse"
            ],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Cuál es la forma más común en español para expresar obligación negada?",
            "opciones": [
                "a) Usar la negación con el verbo principal",
                "b) Usar la negación con 'haber'",
                "c) Usar una doble negación"
            ],
            "respuesta": "b"
        }
    ]
    puntos = 0
    for q in preguntas:
        print(q["pregunta"])
        for opcion in q["opciones"]:
            print(opcion)
        respuesta = input("Tu respuesta (a, b o c): ").lower()
        if respuesta == q["respuesta"]:
            print("✔️ Correcto\n")
            puntos += 1
        else:
            print("❌ Incorrecto. La respuesta correcta era:", q["respuesta"], "\n")
    print(f"Puntaje obtenido: {puntos}/{len(preguntas)}")
    puntaje_total += puntos

def ejercicios_redaccion():
    global puntaje_total
    print("\nEJERCICIOS DE REDACCIÓN\n")
    ejemplos = [
        {
            "instruccion": "Transforma esta oración lógica en la forma más común del español:\nHay que no preocuparse.",
            "esperada": "No hay que preocuparse"
        },
        {
            "instruccion": "Transforma esta oración lógica en la forma común:\nHay que no rendirse.",
            "esperada": "No hay que rendirse"
        }
    ]
    puntos = 0
    for e in ejemplos:
        print(e["instruccion"])
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == e["esperada"].lower():
            print("✔️ ¡Muy bien!\n")
            puntos += 1
        else:
            print(f"❌ No es del todo correcto. Una mejor opción sería: {e['esperada']}\n")
    print(f"Puntaje obtenido: {puntos}/{len(ejemplos)}")
    puntaje_total += puntos

def analisis_sintactico():
    global puntaje_total
    print("\nEJERCICIOS DE ANÁLISIS SINTÁCTICO\n")
    oraciones = [
        {
            "texto": "No hay que rendirse.",
            "auxiliar": "hay",
            "principal": "rendirse",
            "negacion": "haber"
        },
        {
            "texto": "Hay que no gritar.",
            "auxiliar": "hay",
            "principal": "gritar",
            "negacion": "verbo principal"
        }
    ]
    puntos = 0
    for o in oraciones:
        print(f"\nOración: {o['texto']}")
        r1 = input("¿Cuál es el verbo auxiliar? ").strip().lower()
        r2 = input("¿Cuál es el verbo principal? ").strip().lower()
        r3 = input("¿La negación afecta al verbo 'haber' o al verbo principal? ").strip().lower()
        aciertos = 0
        if r1 == o["auxiliar"]:
            aciertos += 1
        if r2 == o["principal"]:
            aciertos += 1
        if r3 in o["negacion"]:
            aciertos += 1
        print(f"✔️ Aciertos: {aciertos}/3")
        puntos += aciertos
    puntaje_total += puntos
    print(f"\nPuntaje total en análisis sintáctico: {puntos}/{len(oraciones)*3}")

def mostrar_puntaje():
    print(f"\n🏅 PUNTAJE TOTAL ACUMULADO: {puntaje_total} puntos\n")

def menu():
    while True:
        print("\n=== MENÚ DE PRÁCTICA ===")
        print("1. Leer teoría")
        print("2. Cuestionario")
        print("3. Ejercicios de redacción")
        print("4. Análisis sintáctico")
        print("5. Ver puntaje total")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            cuestionario()
        elif opcion == "3":
            ejercicios_redaccion()
        elif opcion == "4":
            analisis_sintactico()
        elif opcion == "5":
            mostrar_puntaje()
        elif opcion == "6":
            print("¡Hasta la próxima práctica!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
menu()
