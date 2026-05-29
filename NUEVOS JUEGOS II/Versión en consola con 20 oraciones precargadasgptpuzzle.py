import random

def main():
    print("🧩 Bienvenido al Puzzle de la Oración")
    print("Instrucciones: Ordena correctamente las palabras de la oración.\n")

    ejercicios = [
        "El perro corre en el parque",
        "María canta una canción hermosa",
        "Los niños juegan en la escuela",
        "El sol brilla en la mañana",
        "Mi hermano lee un libro interesante",
        "Los estudiantes estudian para el examen",
        "La maestra explica la lección con paciencia",
        "El tren salió temprano de la estación",
        "Los gatos duermen en el sillón",
        "Ana escribe una carta a su amiga",
        "Pedro toca la guitarra en la fiesta",
        "Mis padres viajan a Madrid mañana",
        "La lluvia cae suavemente en la noche",
        "El profesor corrige los exámenes",
        "La computadora funciona muy rápido",
        "El avión aterrizó sin problemas",
        "Mi abuela cocina una sopa deliciosa",
        "Los amigos juegan cartas en casa",
        "El viento sopla fuerte en la montaña",
        "Carlos corre todos los días en el parque"
    ]

    puntaje = 0

    for i, oracion in enumerate(ejercicios, 1):
        palabras = oracion.split()
        random.shuffle(palabras)

        print(f"\nEjercicio {i}:")
        print("Palabras desordenadas:", " / ".join(palabras))

        respuesta = input("👉 Escribe la oración ordenada: ").strip()

        if respuesta.lower() == oracion.lower():
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print("❌ Incorrecto.")
            print(f"   La respuesta correcta era: {oracion}")

    print(f"\n🎉 Fin del juego. Tu puntaje fue: {puntaje}/{len(ejercicios)}")

if __name__ == "__main__":
    main()
