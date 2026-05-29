import random

# Base de datos de ejercicios
ejercicios = [
    {
        "oracion": "Cuando llegué a la estación, el tren ya __________.",
        "respuesta": "había salido",
        "tiempo": "pluscuamperfecto",
        "explicacion": "La acción de 'salir' ocurrió antes que 'llegar', por eso usamos pluscuamperfecto: 'había salido'."
    },
    {
        "oracion": "Hoy __________ una buena noticia.",
        "respuesta": "he recibido",
        "tiempo": "pretérito perfecto",
        "explicacion": "La acción ocurrió hoy y tiene relación con el presente, por eso se usa pretérito perfecto."
    },
    {
        "oracion": "Cuando me llamaste, ya __________ la tarea.",
        "respuesta": "había terminado",
        "tiempo": "pluscuamperfecto",
        "explicacion": "La tarea se completó antes de la llamada, se usa pluscuamperfecto: 'había terminado'."
    },
    {
        "oracion": "El año pasado __________ a París con mi familia.",
        "respuesta": "viajé",
        "tiempo": "pretérito indefinido",
        "explicacion": "El pretérito indefinido se usa para acciones concluidas en un tiempo pasado definido: 'el año pasado'."
    },
    {
        "oracion": "Ella no entendía porque nunca __________ esa palabra.",
        "respuesta": "había escuchado",
        "tiempo": "pluscuamperfecto",
        "explicacion": "La falta de comprensión se explica por un hecho anterior: no la había escuchado antes."
    }
]

def practicar():
    puntaje = 0
    intentos = 0

    print("🧠 Práctica del Pluscuamperfecto y otros tiempos verbales\n")
    print("Escribe la forma verbal correcta según el contexto.\n")

    while True:
        ejercicio = random.choice(ejercicios)
        print(f"Oración: {ejercicio['oracion']}")
        respuesta = input("Completa la oración: ").strip().lower()
        intentos += 1

        if respuesta == ejercicio["respuesta"]:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {ejercicio['respuesta']}")
        
        print(f"📘 Explicación: {ejercicio['explicacion']}")
        print(f"🔢 Puntaje: {puntaje}/{intentos}\n")

        continuar = input("¿Quieres intentar otra oración? (s/n): ").strip().lower()
        if continuar != "s":
            print("\nGracias por practicar. ¡Sigue mejorando!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    practicar()
