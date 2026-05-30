import random

# Base de datos de ejercicios
ejercicios = [
    {"pista": "¿Es él un doctor?", "correcta": "Is he a doctor?", "opciones": ["Is he a doctor?", "Is she a doctor?", "Are they doctors?"]},
    {"pista": "¿Es ella una profesora?", "correcta": "Is she a teacher?", "opciones": ["Is he a teacher?", "Is she a teacher?", "Are they teachers?"]},
    {"pista": "¿Son ellos músicos?", "correcta": "Are they musicians?", "opciones": ["Is he a musician?", "Is she a musician?", "Are they musicians?"]},
    {"pista": "¿Eres tú un estudiante?", "correcta": "Are you a student?", "opciones": ["Is he a student?", "Is she a student?", "Are you a student?"]},
    {"pista": "¿Soy yo un desarrollador?", "correcta": "Am I a developer?", "opciones": ["Is he a developer?", "Are they developers?", "Am I a developer?"]},
    # Puedes agregar más aquí o generar dinámicamente
]

# Generar más ejemplos automáticamente
pronombres = ["he", "she", "they", "you", "I"]
roles = ["doctor", "teacher", "musician", "student", "engineer", "pilot", "chef", "artist", "developer", "nurse"]
for _ in range(95):
    pron = random.choice(pronombres)
    rol = random.choice(roles)
    pista = f"¿Es {pron} un {rol}?" if pron != "they" else f"¿Son ellos {rol}s?"
    correcta = f"Is {pron} a {rol}?" if pron != "they" else f"Are they {rol}s?"
    distractores = []
    while len(distractores) < 2:
        otro = random.choice([p for p in pronombres if p != pron])
        distractor = f"Is {otro} a {rol}?" if otro != "they" else f"Are they {rol}s?"
        if distractor != correcta and distractor not in distractores:
            distractores.append(distractor)
    opciones = [correcta] + distractores
    random.shuffle(opciones)
    ejercicios.append({"pista": pista, "correcta": correcta, "opciones": opciones})

# Estadísticas
puntaje = 0
aciertos = 0
errores = 0

# Juego principal
def practicar():
    global puntaje, aciertos, errores
    print("\n🧠 Memorización de preguntas interrogativas – 100 ejercicios")
    for i, ej in enumerate(ejercicios, 1):
        print(f"\n🔹 Ejercicio {i}")
        print(f"🎯 Pista: {ej['pista']}")
        for idx, opcion in enumerate(ej["opciones"], 1):
            print(f"{idx}. {opcion}")
        try:
            eleccion = int(input("✍️ Elige la opción correcta (1-3): "))
            seleccionada = ej["opciones"][eleccion - 1]
        except:
            print("⚠️ Entrada inválida. Se contará como error.")
            errores += 1
            puntaje -= 5
            continue

        if seleccionada == ej["correcta"]:
            print("✅ ¡Correcto!")
            puntaje += 10
            aciertos += 1
        else:
            print(f"❌ Incorrecto. La respuesta era: {ej['correcta']}")
            puntaje -= 5
            errores += 1

    # Resultados finales
    print("\n🎉 Repaso completado")
    print(f"✅ Aciertos: {aciertos}")
    print(f"❌ Errores: {errores}")
    print(f"🏆 Puntaje total: {puntaje}")

# Ejecutar
if __name__ == "__main__":
    practicar()
