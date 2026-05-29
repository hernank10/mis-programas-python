# Juego: Cazador de Sujeto y Predicado
# Versión en consola con 20 ejercicios
# Autor: Hernán & ChatGPT

def main():
    print("🎯 Bienvenido al juego: Cazador de Sujeto y Predicado")
    print("Instrucciones: Lee la oración y escribe el sujeto y el predicado.\n")

    ejercicios = [
        {"oracion": "El perro ladra en el jardín.", 
         "sujeto": "El perro", "predicado": "ladra en el jardín"},
        {"oracion": "María canta una canción hermosa.", 
         "sujeto": "María", "predicado": "canta una canción hermosa"},
        {"oracion": "Los estudiantes estudian para el examen.", 
         "sujeto": "Los estudiantes", "predicado": "estudian para el examen"},
        {"oracion": "El sol brilla intensamente.", 
         "sujeto": "El sol", "predicado": "brilla intensamente"},
        {"oracion": "Mi hermano juega fútbol en el parque.", 
         "sujeto": "Mi hermano", "predicado": "juega fútbol en el parque"},
        {"oracion": "La maestra explica la lección con paciencia.", 
         "sujeto": "La maestra", "predicado": "explica la lección con paciencia"},
        {"oracion": "El tren salió temprano de la estación.", 
         "sujeto": "El tren", "predicado": "salió temprano de la estación"},
        {"oracion": "Los niños corren felices.", 
         "sujeto": "Los niños", "predicado": "corren felices"},
        {"oracion": "El viento sopla fuerte en la montaña.", 
         "sujeto": "El viento", "predicado": "sopla fuerte en la montaña"},
        {"oracion": "Ana lee un libro interesante.", 
         "sujeto": "Ana", "predicado": "lee un libro interesante"},
        {"oracion": "La lluvia cae suavemente.", 
         "sujeto": "La lluvia", "predicado": "cae suavemente"},
        {"oracion": "Pedro y Juan juegan ajedrez.", 
         "sujeto": "Pedro y Juan", "predicado": "juegan ajedrez"},
        {"oracion": "El gato duerme en el sillón.", 
         "sujeto": "El gato", "predicado": "duerme en el sillón"},
        {"oracion": "La computadora funciona rápido.", 
         "sujeto": "La computadora", "predicado": "funciona rápido"},
        {"oracion": "Mis padres viajan a Madrid.", 
         "sujeto": "Mis padres", "predicado": "viajan a Madrid"},
        {"oracion": "El profesor corrige los exámenes.", 
         "sujeto": "El profesor", "predicado": "corrige los exámenes"},
        {"oracion": "El avión aterrizó sin problemas.", 
         "sujeto": "El avión", "predicado": "aterrizó sin problemas"},
        {"oracion": "La película terminó tarde.", 
         "sujeto": "La película", "predicado": "terminó tarde"},
        {"oracion": "Mi abuela cocina muy rico.", 
         "sujeto": "Mi abuela", "predicado": "cocina muy rico"},
        {"oracion": "Los amigos juegan cartas.", 
         "sujeto": "Los amigos", "predicado": "juegan cartas"}
    ]

    puntaje = 0

    for i, ejercicio in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}: {ejercicio['oracion']}")
        sujeto = input("👉 Escribe el sujeto: ").strip()
        predicado = input("👉 Escribe el predicado: ").strip()

        if sujeto.lower() == ejercicio["sujeto"].lower() and predicado.lower() == ejercicio["predicado"].lower():
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print("❌ Incorrecto.")
            print(f"   Sujeto correcto: {ejercicio['sujeto']}")
            print(f"   Predicado correcto: {ejercicio['predicado']}")

    print(f"\n🎉 Fin del juego. Tu puntaje fue: {puntaje}/{len(ejercicios)}")

if __name__ == "__main__":
    main()
