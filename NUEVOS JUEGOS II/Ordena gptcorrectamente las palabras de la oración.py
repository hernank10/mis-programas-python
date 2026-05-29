import random

def main():
    print("🧩 Bienvenido al Puzzle de la Oración")
    print("Instrucciones: Ordena correctamente las palabras de la oración.\n")

    # Lista de oraciones correctas
    ejercicios = [
        "El perro corre en el parque",
        "María canta una canción",
        "Los niños juegan en la escuela",
        "El sol brilla en la mañana",
        "Mi hermano lee un libro interesante"
    ]

    puntaje = 0

    for i, oracion in enumerate(ejercicios, 1):
        palabras = oracion.split()
        random.shuffle(palabras)  # Mezcla las palabras

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
