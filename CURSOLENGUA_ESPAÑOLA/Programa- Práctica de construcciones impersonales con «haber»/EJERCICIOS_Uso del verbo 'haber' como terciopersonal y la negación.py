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

Pero esta última suena forzada en el uso real. Por eso, el español prefiere 'No hay que desanimarse' por motivos de economía y claridad.
    """)

def cuestionario():
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
    puntaje = 0
    for q in preguntas:
        print(q["pregunta"])
        for opcion in q["opciones"]:
            print(opcion)
        respuesta = input("Tu respuesta (a, b o c): ").lower()
        if respuesta == q["respuesta"]:
            print("✔️ Correcto\n")
            puntaje += 1
        else:
            print("❌ Incorrecto. La respuesta correcta era:", q["respuesta"], "\n")
    print(f"Puntaje final: {puntaje}/{len(preguntas)}")

def ejercicios_redaccion():
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
    for e in ejemplos:
        print(e["instruccion"])
        respuesta = input("Tu respuesta: ").strip()
        if respuesta.lower() == e["esperada"].lower():
            print("✔️ ¡Muy bien!\n")
        else:
            print(f"❌ No es del todo correcto. Una mejor opción sería: {e['esperada']}\n")

def menu():
    while True:
        print("\n=== MENÚ DE PRÁCTICA ===")
        print("1. Leer teoría")
        print("2. Cuestionario")
        print("3. Ejercicios de redacción")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            cuestionario()
        elif opcion == "3":
            ejercicios_redaccion()
        elif opcion == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
menu()
