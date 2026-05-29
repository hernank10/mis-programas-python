def mostrar_teoria():
    teoria = {
        "Introducción": """
        LA PERÍFRASIS 'IR A + INFINITIVO' EN CONTEXTOS MODALES

        Esta perífrasis expresa futuro próximo o intención, pero su uso está condicionado por:
        1. Tipo de predicado matriz
        2. Presencia/ausencia de negación
        3. Contexto sintáctico (oraciones volitivas, imperativos, etc.)
        """,

        "Contextos aceptables": """
        USOS LEGÍTIMOS:
        - Con predicados epistémicos/factivo-evaluativos:
          * "Dudo que vaya a llover" (subjuntivo dubitativo)
          * "Es bueno que vayas a estudiar" (valoración)
        - Con negación en contextos volitivos:
          * "Prohíbo que vayas a protestar" ❌
          * "Prohíbo que NO vayas a protestar" ✅
        """,

        "Contextos excluidos": """
        USOS NO ACEPTABLES:
        - Con predicados directivos/volitivos afirmativos:
          * "Quiero que vayas a comer" ❌
          * "Quiero que comas" ✅
        - En imperativos afirmativos:
          * "Ve a decirle" ❌
          * "No vayas a decirle" ✅
        """,

        "Mecanismo de negación": """
        LA NEGACIÓN COMO MODULADOR:
        La negación transforma la semántica:
        1. En volitivos: de 'control directo' a 'prevención'
        2. En imperativos: de 'orden' a 'advertencia'
        3. Crea espacio para la interpretación hipotética que necesita 'ir a'
        """
    }

    for seccion, contenido in teoria.items():
        print(f"\n=== {seccion.upper()} ===")
        print(contenido)
        input("Presiona Enter para continuar...")

def ejercicios():
    puntaje = 0
    ejercicios = [
        {
            "pregunta": "¿Cuál es correcta y por qué?\nA) Exijo que vayas a pagar\nB) Exijo que no vayas a pagar",
            "respuesta": "B",
            "explicacion": "La negación legitima 'ir a' en contextos volitivos (de prohibición)"
        },
        {
            "pregunta": "Corrige: 'El jefe quiere que vayamos a reunirnos'",
            "respuesta": "El jefe quiere que nos reunamos",
            "explicacion": "Los verbos volitivos requieren subjuntivo simple en afirmativo"
        },
        {
            "pregunta": "Analiza: 'No vayáis a creer todo lo que os digan'",
            "respuesta": "Uso legítimo: negación + imperativo + 'ir a' = advertencia preventiva",
            "explicacion": "La negación permite usar la perífrasis con valor de precaución"
        }
    ]

    print("\n=== EJERCICIOS ===")
    for i, ej in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}: {ej['pregunta']}")
        user_resp = input("Tu respuesta: ").strip()
        
        if i == 1:  # Opción múltiple
            if user_resp.upper() == ej["respuesta"]:
                puntaje += 1
                print("✅ Correcto!")
            else:
                print("❌ Incorrecto")
        else:
            print(f"Respuesta modelo: {ej['respuesta']}")
            print(f"Explicación: {ej['explicacion']}")
            puntaje += 1  # Asumimos participación completa

        print("-"*50)

    print(f"\nPuntuación final: {puntaje}/{len(ejercicios)}")
    if puntaje == len(ejercicios):
        print("🎉 Excelente dominio del tema!")
    else:
        print("💡 Revisa la teoría y sigue practicando!")

def main():
    while True:
        print("\n" + "="*50)
        print(" ESTUDIO DE 'IR A + INFINITIVO' EN CONTEXTOS MODALES")
        print("="*50)
        print("1. Ver teoría")
        print("2. Realizar ejercicios")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicios()
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
