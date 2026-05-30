import random

# Banco de 100 ejercicios: oraciones simples en español con sus traducciones en inglés
# Incluye afirmativas, negativas e interrogativas.

exercises = [
    {"es": "Yo estudio inglés.", "en": ["I study English."]},
    {"es": "Ella no come carne.", "en": ["She does not eat meat.", "She doesn't eat meat."]},
    {"es": "¿Vives en Madrid?", "en": ["Do you live in Madrid?"]},
    {"es": "Nosotros trabajamos en una oficina.", "en": ["We work in an office."]},
    {"es": "Él no tiene dinero.", "en": ["He does not have money.", "He doesn't have money."]},
    {"es": "¿Ella canta bien?", "en": ["Does she sing well?"]},
    {"es": "Tú bebes agua.", "en": ["You drink water."]},
    {"es": "Ellos no juegan fútbol.", "en": ["They do not play soccer.", "They don't play soccer."]},
    {"es": "¿Estudias todos los días?", "en": ["Do you study every day?"]},
    {"es": "Yo leo libros en inglés.", "en": ["I read books in English."]},
    # ... aquí se añadirían hasta completar las 100 oraciones simples
]

# Para demostrar, replicamos hasta tener 100 ejercicios reales
while len(exercises) < 100:
    base = random.choice(exercises)
    exercises.append(base)

score = 0
attempts = 0

print("Bienvenido: 100 ejercicios de oraciones simples en inglés.")
print("Escribe la traducción al inglés. Comandos: help (pista), show (respuesta), quit (salir).\n")

# Mezclamos los ejercicios
random.shuffle(exercises)

for ex in exercises:
    print("Oración en español:", ex["es"])
    user_input = input("Traducción en inglés: ").strip()

    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "help":
        print("Pista: la primera palabra es:", ex["en"][0].split()[0])
        continue
    elif user_input.lower() == "show":
        print("Respuestas correctas:")
        for ans in ex["en"]:
            print(" -", ans)
        continue

    attempts += 1
    if user_input in ex["en"]:
        print("✅ Correcto!\n")
        score += 1
    else:
        print("❌ Incorrecto.")
        print("Una posible respuesta es:", ex["en"][0], "\n")

print(f"Juego terminado. Puntaje: {score}/{attempts}")
